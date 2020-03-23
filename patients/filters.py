import django_filters

from .models import Report, ErrorReport
from .forms import FilterForm


class ReportsTableFilter(django_filters.FilterSet):
    class Meta:
        model = Report
        fields = (
            "diagnosed_date",
            "detected_state",
            "detected_city",
            "gender",
            "current_status",
        )
        form = FilterForm


class PatientsTableFilter(django_filters.FilterSet):
    class Meta:
        model = Report
        fields = (
            "diagnosed_date",
            "detected_state",
            "detected_city",
            "gender",
            "current_status",
        )
        form = FilterForm

class ErrorReportsTableFilter(django_filters.FilterSet):
    class Meta:
        model = ErrorReport
        fields = (
            "patient__id",
            "error_fields",
            "corrections",
            "status",
            "reported_on",
        )
        form = FilterForm
