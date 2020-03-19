from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin

from .models import Report, Patient


@admin.register(Patient)
class PatientAdmin(OSMGeoAdmin):
    pass


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    pass
