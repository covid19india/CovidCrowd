from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin

from .models import Report, Patient, ErrorReport, Source, PatientHistory


@admin.register(Patient)
class PatientAdmin(OSMGeoAdmin):
    pass


@admin.register(PatientHistory)
class PatientHistoryAdmin(OSMGeoAdmin):
    list_filter = (
            ("patient", admin.RelatedOnlyFieldListFilter),
    )


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_filter = ('report_state', )


@admin.register(ErrorReport)
class ErrorReportAdmin(admin.ModelAdmin):
    list_filter = ('status', )


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_filter = ("is_verified", )
