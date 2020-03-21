import os.path
import csv

from datetime import datetime
from django.core.management.base import BaseCommand

from patients.models import Report
from patients.constants import Gender, PatientStatus

columns = [
    "Patient number",
    "State Patient Number",
    "Date Announced",
    "Estimated Onset Date",
    "Age Bracket",
    "Gender",
    "Detected City",
    "Detected District",
    "Detected State",
    "Current Status",
    "Notes",
    "Contracted from which Patient (Suspected)",
    "Status Change Date",
    "Source_1",
    "Source_2",
    "Source_3",
]


class Command(BaseCommand):
    """Command to import the data from the GoogleSheets CSV into the applcation."""

    help = (
        "Imports the Google Sheets Raw Data CSV and creates a new report for every row."
    )

    def add_arguments(self, parser):
        parser.add_argument("csvfile", nargs=1, type=str)

    def handle(self, *args, **options):
        filepath = options["csvfile"]
        if not filepath:
            print("Error! Missing CSV File Path")
            return
        filepath = filepath[0]
        if not os.path.isfile(filepath):
            print(f"Error! Cannot find file at: {filepath}")
            return

        counter = 0
        skipped = 0
        with open(filepath, "r") as fp:
            reader = csv.DictReader(fp)
            for row in reader:
                if not row["Date Announced"]:
                    skipped += 1
                    continue
                if row["Patient number"]:
                    try:
                        existing = Report.objects.get(patient_id=row["Patient number"])
                    except Report.DoesNotExist:
                        existing = None

                    if existing:
                        print(
                            f"Report with patient number {row['Patient number']} already exits as Report #{existing.id}. Skipping."
                        )
                        skipped += 1
                        continue
                self._create_new_report(row)
                counter += 1
        print(
            f"SUCCESS: CSV File was imported. Reports created: {counter}, Skipped: {skipped}"
        )

    @staticmethod
    def _create_new_report(row):
        report = Report()

        report.patient_id = row["Patient number"]
        report.diagnosed_date = datetime.strptime(row["Date Announced"], "%d/%m/%Y")
        if row["Age Bracket"].strip():
            report.age = int(row["Age Bracket"])
        if row["Gender"] == "M":
            report.gender = Gender.MALE
        elif row["Gender"] == "F":
            report.gender = Gender.FEMALE
        elif row["Gender"]:
            report.gender = Gender.OTHERS
        else:
            report.gender = Gender.UNKNOWN
        report.detected_city = row["Detected City"]
        report.detected_district = row["Detected District"]
        report.detected_state = row["Detected State"]
        report.nationality = ""
        if row["Current Status"] in PatientStatus.CHOICES:
            report.current_status = row["Current Status"]

        report.notes = row["Notes"]
        report.source = "\n".join([row["Source_1"], row["Source_2"], row["Source_3"]])

        report.save()
