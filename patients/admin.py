from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin

from .models import Report, Patient, ErrorReport


@admin.register(Patient)
class PatientAdmin(OSMGeoAdmin):
    pass


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    pass


@admin.register(ErrorReport)
class ErrorReportAdmin(admin.ModelAdmin):
    pass
