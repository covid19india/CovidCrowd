import django_filters

from .models import Report
from .forms import ReportsFilterForm


class ReportsTableFilter(django_filters.FilterSet):
    class Meta:
        model = Report
        fields = ("diagnosed_date", "detected_state", "detected_city", "gender", "current_status")
        form = ReportsFilterForm
