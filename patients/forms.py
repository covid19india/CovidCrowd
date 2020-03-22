from django import forms
from django.contrib.gis import forms as geoforms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls import reverse

from .models import Report, Patient, StatusUpdate


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [
            "diagnosed_date",
            "age",
            "gender",
            "detected_city",
            "detected_state",
            "detected_district",
            "nationality",
            "current_status",
            "notes",
            "current_location",
            "source",
        ]
        widgets = {
            "source": forms.Textarea(attrs={"rows": 2, "cols": 15}),
            "notes": forms.Textarea(attrs={"rows": 2, "cols": 15}),
            "diagnosed_date": forms.DateInput(attrs={"type": "text", "class": "datepicker"}),
        }

    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = "form-horizontal mt-4"
        self.helper.wrapper_class = "row"
        self.helper.label_class = "col-md-2"
        self.helper.field_class = "col-md-10"

        self.helper.add_input(Submit("submit", "Submit"))


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            "unique_id",
            "government_id",
            "diagnosed_date",
            "age",
            "gender",
            "detected_city",
            "detected_city_pt",
            "detected_state",
            "detected_district",
            "nationality",
            "current_status",
            "notes",
            "source",
            "current_location",
            "current_location_pt",
        ]
        widgets = {
            "detected_city_pt": geoforms.OSMWidget(attrs={"default_zoom": 6}),
            "current_location_pt": geoforms.OSMWidget(attrs={"default_zoom": 6}),
            "source": forms.Textarea(attrs={"rows": 2, "cols": 15}),
            "notes": forms.Textarea(attrs={"rows": 2, "cols": 15}),
            "diagnosed_date": forms.DateInput(attrs={"type": "text", "class": "datepicker"}),
        }

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = "form-horizontal mt-4"
        self.helper.wrapper_class = "row"
        self.helper.label_class = "col-md-2"
        self.helper.field_class = "col-md-10"

        self.helper.add_input(Submit("submit", "Add new Patient"))
        self.helper.add_input(
            Submit(
                "mark_verified",
                "Mark Report Verified",
                css_class="btn-default float-right",
            )
        )


class FilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = "get"
        self.helper.form_class = "form-horizontal"
        self.helper.wrapper_class = "row"
        self.helper.label_class = "col-md-2"
        self.helper.field_class = "col-md-10"
        self.helper.add_input(Submit("submit", "Apply Filters"))


class ErrorReportForm(forms.Form):
    patient_id = forms.IntegerField(widget=forms.HiddenInput())
    errors = forms.MultipleChoiceField(
        label="What details are wrong? (Use Ctrl+click to select multiple)",
        choices=(
            ("diagnosed_date", "Diagnosed Date"),
            ("age", "Age"),
            ("gender", "Gender"),
            ("detected_city", "City"),
            ("detected_district", "District"),
            ("detected_state", "State"),
            ("nationality", "Nationality"),
            ("current_status", "Current Status of the Patient"),
            ("status_change_date", "Date on which the patient status changed"),
            ("current_location", "Current Location of the patient"),
            ("others", "Any other information")
        ),
        widget=forms.SelectMultiple(attrs={"size": 10})
    )
    correction = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ErrorReportForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Submit"))
        self.helper.form_action = reverse("patients:report-error")
