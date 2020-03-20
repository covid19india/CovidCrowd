from django import forms
from django.contrib.gis import forms as geoforms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


from .models import Report, Patient


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [
            "age",
            "gender",
            "state",
            "current_status",
            "onset_date",
            "diagnosed_date",
            "detected_location",
            "current_location",
            "travel_mode",
            "source",
            "notes",
        ]
        widgets = {
            "source": forms.Textarea(attrs={"rows": 2, "cols": 15}),
            "notes": forms.Textarea(attrs={"rows": 2, "cols": 15}),
            "onset_date": forms.DateInput(attrs={"type": "date"}),
            "diagnosed_date": forms.DateInput(attrs={"type": "date"}),
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
            "age",
            "gender",
            "current_status",
            "onset_date",
            "diagnosed_date",
            "state",
            "district",
            "detected_location",
            "detected_location_pt",
            "current_location",
            "current_location_pt",
            "travel_mode",
            "notes",
        ]
        widgets = {
            "detected_location_pt": geoforms.OSMWidget(attrs={"default_zoom": 5}),
            "current_location_pt": geoforms.OSMWidget(attrs={"default_zoom": 5}),
            "source": forms.Textarea(attrs={"rows": 2, "cols": 15}),
            "travel_mode": forms.Textarea(attrs={"rows": 2, "cols": 15}),
            "notes": forms.Textarea(attrs={"rows": 2, "cols": 15}),
            "onset_date": forms.DateInput(attrs={"type": "date"}),
            "diagnosed_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = "form-horizontal mt-4"
        self.helper.wrapper_class = "row"
        self.helper.label_class = "col-md-2"
        self.helper.field_class = "col-md-10"

        self.helper.add_input(Submit("submit", "Add new Patient"))
        self.helper.add_input(Submit("mark_verified", "Mark Report Verified", css_class="btn-default float-right"))
