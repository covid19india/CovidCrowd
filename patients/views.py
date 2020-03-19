from django.shortcuts import render, redirect

from .forms import ReportForm


def index(request):
    return render(request, "patients/index.html")


def report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("patients:thank_you")
    else:
        form = ReportForm()
    return render(request, "patients/report.html", {'form': form})


def thank_you(request):
    return render(request, "patients/thank_you.html")

