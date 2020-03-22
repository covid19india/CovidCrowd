import requests

from django.db import models
from django.contrib.gis.db import models as geomodels
from django.contrib.gis.geos import Point, Polygon
from django.utils import timezone

from .constants import COUNTRIES, STATES, PatientStatus, Gender,CITIES,DISTRICT_CHOICES


class Report(models.Model):
    REPORTED = "R"
    VERIFIED = "V"
    DUPLICATE = "D"
    CONVERTED = "C"
    INVALID = "I"

    REPORT_STATE_CHOICES = (
        (REPORTED, "Reported"),
        (VERIFIED, "Verified"),
        (DUPLICATE, "Duplicate"),
        (CONVERTED, "Converted"),
        (INVALID, "Invalid"),
    )
    diagnosed_date = models.DateField(default=timezone.now)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(
        max_length=15, choices=((c, c) for c in Gender.CHOICES), null=True, blank=True
    )
    detected_city = models.CharField(max_length=150,null=True, blank=True)
    detected_district = models.CharField(max_length=150, null=True, choices=((c, c) for c in DISTRICT_CHOICES), blank=True)
    detected_state = models.CharField(max_length=150, choices=STATES, null=True)
    nationality = models.CharField(max_length=150,choices=((c, c) for c in COUNTRIES),null=True, blank=True)
    current_status = models.CharField(
        max_length=25, choices=((c, c) for c in PatientStatus.CHOICES), null=True
    )
    notes = models.TextField(null=True, blank=True)
    current_location = models.CharField(max_length=150, null=True, blank=True)
    source = models.TextField(null=True, blank=True)
    patient_id = models.CharField(max_length=10, null=True, blank=True)

    # Meta fields
    reported_time = models.DateTimeField(auto_now_add=True)
    report_state = models.CharField(
        max_length=1, choices=REPORT_STATE_CHOICES, default="R"
    )
    duplicate_of = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Report #{self.id} ({self.detected_city}, {self.detected_state}, {self.gender}, {self.age})"


class StatusUpdate(models.Model):
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE, null=False)
    patient_status = models.CharField(
        max_length=25, choices=((c, c) for c in PatientStatus.CHOICES)
    )
    source = models.TextField()

    # Meta fields
    updated_on = models.DateTimeField(auto_now_add=True, editable=False)


class Patient(geomodels.Model):
    diagnosed_date = models.DateField()
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=15, choices=((c, c) for c in Gender.CHOICES))
    detected_city = models.CharField(max_length=150)
    detected_city_pt = geomodels.PointField()
    detected_district = models.CharField(max_length=150, null=True)
    detected_state = models.CharField(max_length=150, choices=STATES, null=True)
    nationality = models.CharField(max_length=150, choices=((c, c) for c in COUNTRIES))
    current_status = models.CharField(
        max_length=25, choices=((c, c) for c in PatientStatus.CHOICES)
    )
    status_change_date = models.DateField(null=True)
    notes = models.TextField()
    current_location = models.CharField(max_length=150)
    current_location_pt = geomodels.PointField()
    source = models.TextField()
    unique_id = models.CharField(max_length=10)
    government_id = models.CharField(max_length=20, null=True, blank=True)

    contacts = models.ManyToManyField("self", blank=True)

    # Meta Fields
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"Patient {self.unique_id}:{self.government_id}"

    @staticmethod
    def from_report(report):
        p = Patient()
        p.diagnosed_date = report.diagnosed_date
        p.age = report.age
        p.gender = report.gender
        p.detected_city = report.detected_city
        p.detected_city_pt = Patient.get_point_for_location(
            city=report.detected_city, state=report.detected_state
        )
        p.detected_district = report.detected_district
        p.detected_state = report.detected_state
        p.nationality = report.nationality
        p.current_status = report.current_status
        # p.status_change_date =
        p.notes = report.notes
        p.current_location = report.current_location or report.detected_city
        if p.current_location != report.detected_city:
            p.current_location_pt = Patient.get_point_for_location(
                city=report.current_location
            )
        else:
            p.current_location_pt = p.detected_city_pt
        p.source = report.source
        p.unique_id = report.patient_id
        return p

    @staticmethod
    def get_point_for_location(city=None, state=None):
        point = Point(80, 20)
        india = Polygon.from_bbox(
            (35.6745457, 6.2325274, 97.395561, 68.1113787,)
        ).prepared

        if not (city or state):
            return point

        base_url = "https://nominatim.openstreetmap.org/search/"
        payload = {"format": "json"}
        if city:
            payload["city"] = city
        if state:
            payload["state"] = state

        resp = requests.get(base_url, params=payload)
        if resp.status_code != 200:
            return point

        data = resp.json()
        for loc in data:
            print(loc)
            try:
                lon = float(loc["lon"])
                lat = float(loc["lat"])
            except:
                continue
            p = Point(lon, lat)
            if india.contains(p):
                point = p
                break
        return point
