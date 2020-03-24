from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django_filters.views import FilterView
from django_tables2.export.views import ExportMixin
from django_tables2.views import SingleTableMixin
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .constants import STATE_WISE_DISTRICTS
from .filters import ReportsTableFilter, PatientsTableFilter
from .forms import ReportForm, PatientForm, ErrorReportForm, PatientEditForm
from .forms import SourceForm
from .models import Report, Patient, ErrorReport, PatientHistory
from .models import Source
from .serializers import PatientSerializer
from .tables import PatientsExportedTable
from .tables import ReportsTable, PatientsTable, PatientHistoryTable


@method_decorator(staff_member_required, name="dispatch")
class ReportQueue(SingleTableMixin, FilterView):
    model = Report
    queryset = Report.objects.filter(report_state=Report.REPORTED)
    table_class = ReportsTable
    filterset_class = ReportsTableFilter

    template_name = "patients/report_list.html"


class Index(SingleTableMixin, ExportMixin, FilterView):
    model = Patient
    table_class = PatientsTable
    filterset_class = PatientsTableFilter
    template_name = "patients/index.html"
    export_formats = ["csv", "json", "latex", "tsv"]


class Export(Index):
    table_class = PatientsExportedTable


class PatientDetails(DetailView):
    model = Patient

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        form = ErrorReportForm(initial={"patient_id": self.object.id})
        history_table = PatientHistoryTable(PatientHistory.objects.filter(patient_id=self.object.id).order_by('time_from'))
        context["form"] = form
        context["history_table"] = history_table

        if self.request.user.is_staff:
            context["error_report_count"] = ErrorReport.objects.filter(patient=self.object, status=ErrorReport.NEW).count()

        return context


def report(request):
    if request.method == "POST":
        form = ReportForm(request.POST)
        unit_id = request.POST.get('detected_district')
        form.fields['detected_district'].choices = [(unit_id, unit_id)]
        if form.is_valid():
            form.save()
            return redirect("patients:thank_you")
    else:
        form = ReportForm()
    return render(request, "patients/report.html", {"form": form})


def thank_you(request):
    return render(request, "patients/thank_you.html")


def login_form(request):
    return render(request, "patients/login.html")


@login_required
def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect("patients:index")


@staff_member_required
@login_required
def review_report(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    request.session["reviewing_report"] = report_id
    return render(request, "patients/review_report.html", {"report": report})


@staff_member_required
@login_required
def add_patient(request):
    report_id = request.session.get("reviewing_report", None)
    if not report_id:
        return redirect("patients:report-queue")

    report = get_object_or_404(Report, pk=report_id)
    patient = Patient.from_report(report)
    sourcelines = report.source.strip().split("\n")
    SourceFormset = formset_factory(SourceForm, extra=len(sourcelines) - 1)

    if request.method == "POST":
        form = PatientForm(request.POST)
        sformset = SourceFormset(request.POST)

        if form.is_valid() and sformset.is_valid():
            if "submit" in request.POST:
                patient = form.save()
                report.report_state = report.CONVERTED
                report.save()
                messages.success(
                    request,
                    "A new patient has been added. Thank you for the contribution.",
                )
            elif "mark_verified" in request.POST:
                report.report_state = report.VERIFIED
                report.save()
                messages.info(
                    request,
                    "The report has been marked as verfied. "
                    "One of the admins will review it shortly. Thank you for "
                    "verifying the report.",
                )

            for sform in sformset:
                if sform.is_valid() and sform.has_changed():
                    source = Source(
                        url=sform.cleaned_data["url"],
                        description=sform.cleaned_data["description"],
                        patient=patient
                    )
                    source.save()
            del request.session["reviewing_report"]
            return redirect("patients:report-queue")
    else:
        form = PatientForm(instance=patient)
        initials = []
        for line in sourcelines:
            if line.strip().startswith("http"):
                initials.append({"url": line.strip(), "description": ""})
            else:
                initials.append({"url": line.strip(), "description": ""})
        sformset = SourceFormset(initial=initials)

    return render(
        request,
        "patients/add_patient.html",
        {"patient": patient, "form": form, "sformset": sformset, "report_id": report_id},
    )


@staff_member_required
@login_required
def mark_report_invalid(request):
    report_id = request.session.get("reviewing_report", None)
    if not report_id:
        return redirect("patients:report-queue")

    report = get_object_or_404(Report, pk=report_id)
    report.report_state = Report.INVALID
    report.save()
    messages.success(
        request, "The report has been marked as Invalid. Thank you for flagging it."
    )
    del request.session["reviewing_report"]

    return redirect("patients:report-queue")


def get_statewise_districts(request):
    state = request.POST.get('state').lower()
    if STATE_WISE_DISTRICTS.get(state):
        return JsonResponse({'success': True, 'districts': STATE_WISE_DISTRICTS[state]})
    else:
        return JsonResponse({'success': False})


def report_error(request):
    if request.method == "POST":
        form = ErrorReportForm(request.POST)
        if form.is_valid():
            patient_id = form.cleaned_data["patient_id"]
            r = ErrorReport()
            r.patient_id = patient_id
            error_fields = form.cleaned_data["errors"]
            r.error_fields = ",".join(error_fields)
            r.corrections = form.cleaned_data["correction"]
            r.save()

            messages.success(
                request,
                "Thank you for your correction.  A volunteer from the team will "
                "review the information and make necessary changes."
            )
            return redirect("patients:patient-details", patient_id)
    return redirect("patients:index")


@api_view(['GET',])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def get_patient(request, id):
    patient = get_object_or_404(Patient, pk=id)
    serializer = PatientSerializer(patient)
    return Response(serializer.data)


@api_view(['GET',])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def get_patients(request):
    patient = Patient.objects.all()
    serializer = PatientSerializer(patient,many=True)
    return Response(serializer.data)


@staff_member_required
def review_errors_for_patient(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    errors = ErrorReport.objects.filter(patient=patient, status=ErrorReport.NEW)
    if not errors:
        messages.info(request, "Did not find any new errors.")
        return redirect("patients:patient-details", patient_id)

    if request.method == "POST":
        pass

    context = {
        "patient_form": PatientEditForm(instance=patient),
        "error_reports": errors
    }
    return render(request, "patients/review_errors_for_patient.html", context)
