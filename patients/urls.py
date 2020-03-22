from django.urls import path

from . import views

app_name = "patients"

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("report", views.report, name="report"),
    path("thank_you", views.thank_you, name="thank_you"),
    path("patient/<int:pk>/", views.PatientDetails.as_view(), name="patient-details"),
    path("logout", views.logout, name="logout"),
    path("login-form", views.login_form, name="login-form"),
    path("review-report/<int:report_id>/", views.review_report, name="review-report"),
    path("add-patient", views.add_patient, name="add-patient"),
    path("report-invalid", views.mark_report_invalid, name="report-invalid"),
    path("report-queue", views.ReportQueue.as_view(), name="report-queue"),
    path("get_districts", views.get_statewise_districts, name="get_districts"),
    path("report-error", views.report_error, name="report-error")
]
