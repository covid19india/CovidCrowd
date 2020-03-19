from django.urls import path

from . import views

app_name = "patients"

urlpatterns = [
    path("", views.index, name="index"),
    path("report", views.report, name="report"),
    path("thank_you", views.thank_you, name="thank_you")
]
