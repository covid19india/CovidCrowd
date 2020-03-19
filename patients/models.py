from django.db import models
from django.contrib.gis.db import models as geomodels

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
    state = models.CharField(max_length=150, choices=STATES, null=True)
    duplicate_of = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)
    reported_time = models.DateTimeField(auto_now_add=True)


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
    state = models.CharField(max_length=150, choices=STATES, null=True)
    district = models.CharField(max_length=150, null=True)
