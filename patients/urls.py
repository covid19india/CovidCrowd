from django.urls import path
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from . import views

app_name = "patients"

urlpatterns = [
    path("", cache_page(10*60)(vary_on_cookie(views.Index.as_view())), name="index"),
    path("export", cache_page(10*60)(views.Export.as_view()), name="export"),
    path("report", cache_page(60*60)(views.report), name="report"),
    path("thank_you", cache_page(24*60*60)(views.thank_you), name="thank_you"),
    path("patient/<int:pk>/", cache_page(10*60)(vary_on_cookie(views.PatientDetails.as_view())), name="patient-details"),
    path("logout", views.logout, name="logout"),
    path("login-form", cache_page(24*60*60)(views.login_form), name="login-form"),
    path("review-report/<int:report_id>/", views.review_report, name="review-report"),
    path("add-patient", views.add_patient, name="add-patient"),
    path("report-invalid", views.mark_report_invalid, name="report-invalid"),
    path("report-queue", views.ReportQueue.as_view(), name="report-queue"),
    path("get_districts", views.get_statewise_districts, name="get_districts"),
    path("report-error", views.report_error, name="report-error"),
    path("error-queue", views.ErrorQueueView.as_view(), name="error-queue"),
    path("patient/<int:patient_id>/review-error-reports",
         views.review_errors_for_patient,
         name="review-errors-for-patient"),
    path("update-error-report", views.update_error_report, name="update-error-report"),
    # API paths
    path('api/patients/', cache_page(10*60)(views.get_patients),name='patient list'),
    path('api/patient/<int:id>', cache_page(10*60)(views.get_patient),name='patient'),
    path('api/patient/<int:patient_id>/sources', cache_page(10*60)(views.get_sources_for_patient), name='patient-sources'),
]
