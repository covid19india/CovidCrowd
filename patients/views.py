from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView

from django_tables2.views import SingleTableMixin
from django_tables2.export.views import ExportMixin
from django_filters.views import FilterView


from .forms import ReportForm, PatientForm
from .models import Report, Patient, STATES
from .tables import ReportsTable, PatientsTable
from .filters import ReportsTableFilter, PatientsTableFilter


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


class PatientDetails(DetailView):
    model = Patient


def report(request):
    if request.method == "POST":
        form = ReportForm(request.POST)
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

    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            if "submit" in request.POST:
                form.save()
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
            del request.session["reviewing_report"]
            return redirect("patients:report-queue")
    else:
        form = PatientForm(instance=patient)
    return render(
        request,
        "patients/add_patient.html",
        {"patient": patient, "form": form, "report_id": report_id},
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
