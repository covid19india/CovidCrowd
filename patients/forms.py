from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


from .models import Report


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [
            "age",
            "gender",
            "onset_date",
            "diagnosed_date",
            "detected_location",
            "current_location",
            "current_status",
            "travel_mode",
            "source",
            "notes",
        ]
        widgets = {
            'source': forms.Textarea(attrs={'rows': 2, 'cols': 15}),
            'notes': forms.Textarea(attrs={'rows': 2, 'cols': 15}),
            'onset_date': forms.DateInput(attrs={'type': 'date'}),
            'diagnosed_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal mt-4'
        self.helper.wrapper_class = 'row'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-10'

        self.helper.add_input(Submit('submit', 'Submit'))
