from django.db import models
from django.contrib.gis.db import models as geomodels


class Source(models.Model):
    description = models.TextField()
    url = models.URLField()
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE)


class Report(models.Model):
    GENDER_CHOICES = (("M", "Male"), ("F", "Female"), ("O", "Other"))
    STATUS_CHOICES = (("R", "Recovered"), ("H", "Hospitalized"), ("D", "Deceased"))
    REPORT_STATE_CHOICES = (
        ("R", "Reported"),
        ("V", "Verified"),
        ("D", "Duplicate"),
        ("P", "Patient Added"),
    )
    onset_date = models.DateField()
    diagnosed_date = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    detected_location = models.CharField(max_length=150)
    current_location = models.CharField(max_length=150)
    current_status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    travel_mode = models.CharField(max_length=150)
    source = models.TextField()
    notes = models.TextField()
    duplicate_of = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)


class Patient(geomodels.Model):
    GENDER_CHOICES = (("M", "Male"), ("F", "Female"), ("O", "Other"))
    STATUS_CHOICES = (("R", "Recovered"), ("H", "Hospitalized"), ("D", "Deceased"))
    onset_date = models.DateField()
    diagnosed_date = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    detected_location = geomodels.PointField()
    current_location = geomodels.PointField()
    current_status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    contacts = models.ManyToManyField("self", blank=True)
    # TODO travel_mode might have to be changed to a char field with limited choices
    travel_mode = models.TextField()
    notes = models.TextField()
    report = models.OneToOneField(Report, on_delete=models.SET_NULL, null=True)
