from django.db import models
from django.contrib.gis.db import models as geomodels
from django.contrib.gis.geos import Point

STATES = (
    ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"),
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chandigarh", "Chandigarh"),
    ("Chattisgarh", "Chattisgarh"),
    ("Dadar and Nagar Haveli", "Dadar and Nagar Haveli"),
    ("Daman and Diu", "Daman and Diu"),
    ("Goa", "Goa"),
    ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jammu and Kashmir", "Jammu and Kashmir"),
    ("Jharkhand", "Jharkand"),
    ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"),
    ("Ladakh", "Ladakh"),
    ("Lakshadweep", "Lakshadweep"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharastra", "Maharastra"),
    ("Manipur", "Manipur"),
    ("Meghalaya", "Meghalaya"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("NCT of Delhi", "NCT of Delhi"),
    ("Odisha", "Odisha"),
    ("Puducherry", "Puducherry"),
    ("Punjab", "Punjab"),
    ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telengana", "Telengana"),
    ("Tripura", "Tripura"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("Uttarakhand", "Uttarakhand"),
    ("West Bengal", "West Bengal"),
)


class Report(models.Model):
    REPORTED = "R"
    VERIFIED = "V"
    DUPLICATE = "D"
    PATIENT_ADDED = "P"
    INVALID = "I"

    GENDER_CHOICES = (("M", "Male"), ("F", "Female"), ("O", "Other"))
    STATUS_CHOICES = (("R", "Recovered"), ("H", "Hospitalized"), ("D", "Deceased"))
    REPORT_STATE_CHOICES = (
        (REPORTED, "Reported"),
        (VERIFIED, "Verified"),
        (DUPLICATE, "Duplicate"),
        (PATIENT_ADDED, "Patient Added"),
        (INVALID, "Invalid")
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
    state = models.CharField(max_length=150, choices=STATES, null=True)
    duplicate_of = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)
    reported_time = models.DateTimeField(auto_now_add=True)
    report_state = models.CharField(max_length=1, choices=REPORT_STATE_CHOICES, default="R")


class Patient(geomodels.Model):
    GENDER_CHOICES = (("M", "Male"), ("F", "Female"), ("O", "Other"))
    STATUS_CHOICES = (("R", "Recovered"), ("H", "Hospitalized"), ("D", "Deceased"))

    onset_date = models.DateField()
    diagnosed_date = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    detected_location = models.CharField(max_length=150)
    current_location = models.CharField(max_length=150)
    detected_location_pt = geomodels.PointField()
    current_location_pt = geomodels.PointField()
    current_status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    # TODO travel_mode might have to be changed to a char field with limited choices
    travel_mode = models.TextField()
    notes = models.TextField()
    state = models.CharField(max_length=150, choices=STATES, null=True)
    district = models.CharField(max_length=150, null=True)
    source = models.TextField()

    contacts = models.ManyToManyField("self", blank=True)
    report = models.OneToOneField(Report, on_delete=models.SET_NULL, null=True)

    @staticmethod
    def from_report(report):
        p = Patient()
        p.onset_date = report.onset_date
        p.diagnosed_date = report.diagnosed_date
        p.age = report.age
        p.gender = report.gender
        p.detected_location = report.detected_location
        p.detected_location_pt = Point(80, 20)
        p.current_location = report.current_location
        p.current_location_pt = Point(80, 20)
        p.current_status = report.current_status
        p.travel_mode = report.travel_mode
        p.notes = report.notes
        p.source = report.source
        p.state = report.state
        p.report = report
        return p
