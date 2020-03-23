import django_tables2 as tables

from .models import Report, Patient, ErrorReport


class ReportsTable(tables.Table):
    review = tables.TemplateColumn(
        template_name="patients/_review_btn.html",
        verbose_name="Actions",
        orderable=False,
    )
    diagnosed_date = tables.DateTimeColumn(format='d/M/Y')

    class Meta:
        model = Report
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            "id",
            "diagnosed_date",
            "detected_state",
            "detected_city",
            "age",
            "gender",
            "current_status",
        )
        attrs = {"class": "table table-responsive"}


class PatientsTable(tables.Table):
    detail = tables.TemplateColumn(
        template_name="patients/_show_patient_details_btn.html",
        verbose_name="Details",
        orderable=False,
    )
    diagnosed_date = tables.DateTimeColumn(format='d/M/Y')

    class Meta:
        model = Patient
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            "id",
            "diagnosed_date",
            "detected_state",
            "detected_city",
            "age",
            "gender",
            "current_status",
        )
        attrs = {"class": "table table-responsive"}


class PatientsExportedTable(tables.Table):
    diagnosed_date = tables.DateTimeColumn(format='d/M/Y')

    class Meta:
        model = Patient
        fields = (
            "id",
            "unique_id",
            "government_id",
            "diagnosed_date",
            "age",
            "gender",
            "detected_city",
            "detected_city_pt",
            "detected_district",
            "detected_state",
            "nationality",
            "current_status",
            "status_change_date",
            "notes",
            "current_location",
            "current_location_pt",
            "created_on",
            "updated_on",
            "contacts"
        )

class ErrorReportsTable(tables.Table):
    review = tables.TemplateColumn(
        template_name="patients/_review_btn.html",
        verbose_name="Actions",
        orderable=False,
    )

    class Meta:
        model = ErrorReport
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            "patient__id",
            "error_fields",
            "corrections",
            "status",
            "reported_on",
        )
        attrs = {"class": "table table-responsive"}
