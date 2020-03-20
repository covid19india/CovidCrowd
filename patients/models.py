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
    CONVERTED = "C"
    INVALID = "I"

    GENDER_CHOICES = (("M", "Male"), ("F", "Female"), ("O", "Other"))
    STATUS_CHOICES = (("R", "Recovered"), ("H", "Hospitalized"), ("D", "Deceased"))
    REPORT_STATE_CHOICES = (
        (REPORTED, "Reported"),
        (VERIFIED, "Verified"),
        (DUPLICATE, "Duplicate"),
        (CONVERTED, "Converted"),
        (INVALID, "Invalid"),
    )
    diagnosed_date = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    detected_city = models.CharField(max_length=150, null=True, blank=True)
    detected_district = models.CharField(max_length=150, null=True, blank=True)
    detected_state = models.CharField(max_length=150, choices=STATES, null=True)
    nationality = models.CharField(max_length=150, null=True, blank=True)
    current_status = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True)
    notes = models.TextField(null=True, blank=True)
    current_location = models.CharField(max_length=150, null=True, blank=True)
    source = models.TextField(null=True, blank=True)

    # Meta fields
    reported_time = models.DateTimeField(auto_now_add=True)
    report_state = models.CharField(
        max_length=1, choices=REPORT_STATE_CHOICES, default="R"
    )
    duplicate_of = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)


class StatusUpdate(models.Model):
    STATUS_CHOICES = (("R", "Recovered"), ("H", "Hospitalized"), ("D", "Deceased"))

    patient = models.ForeignKey("Patient", on_delete=models.CASCADE, null=False)
    patient_status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    source = models.TextField()

    # Meta fields
    updated_on = models.DateTimeField(auto_now_add=True, editable=False)


class Patient(geomodels.Model):
    GENDER_CHOICES = (("M", "Male"), ("F", "Female"), ("O", "Other"))
    STATUS_CHOICES = (("R", "Recovered"), ("H", "Hospitalized"), ("D", "Deceased"))

    diagnosed_date = models.DateField()
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    detected_city = models.CharField(max_length=150)
    detected_city_pt = geomodels.PointField()
    detected_district = models.CharField(max_length=150, null=True)
    detected_state = models.CharField(max_length=150, choices=STATES, null=True)
    nationality = models.CharField(max_length=5)
    current_status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    status_change_date = models.DateField()
    notes = models.TextField()
    current_location = models.CharField(max_length=150)
    current_location_pt = geomodels.PointField()
    source = models.TextField()

    contacts = models.ManyToManyField("self", blank=True)

    # Meta Fields
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)

    @staticmethod
    def from_report(report):
        p = Patient()
        p.diagnosed_date = report.diagnosed_date
        p.age = report.age
        p.gender = report.gender
        p.detected_city = report.detected_location
        p.detected_city_pt = Point(80, 20)
        p.detected_district = report.detected_district
        p.detected_state = report.detected_state
        p.nationality = report.nationality
        p.current_status = report.current_status
        # p.status_change_date =
        p.notes = report.notes
        p.current_location = report.current_location
        p.current_location_pt = Point(80, 20)
        p.source = report.source
        return p
