import os.path
import csv

from datetime import datetime
from django.core.management.base import BaseCommand

from patients.models import Patient
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
    "Nationality",
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
                        existing = Patient.objects.get(unique_id=row["Patient number"])
                    except Patient.DoesNotExist:
                        existing = None

                    if existing:
                        print(
                            f"Patient with patient number {row['Patient number']} already exits as Patient #{existing.id}. Skipping."
                        )
                        skipped += 1
                        continue
                self._create_new_patient(row)
                counter += 1
        print(
            f"SUCCESS: CSV File was imported. Patients created: {counter}, Skipped: {skipped}"
        )

    @staticmethod
    def _create_new_patient(row):
        print(f"Adding patient {row['Patient number']}")
        patient = Patient()

        patient.unique_id = row["Patient number"]
        patient.diagnosed_date = datetime.strptime(row["Date Announced"], "%d/%m/%Y")
        patient.status_change_date = datetime.strptime(row["Status Change Date"], "%d/%m/%Y")
        if row["Age Bracket"].strip():
            patient.age = int(row["Age Bracket"])
        if row["Gender"] == "M":
            patient.gender = Gender.MALE
        elif row["Gender"] == "F":
            patient.gender = Gender.FEMALE
        elif row["Gender"]:
            patient.gender = Gender.OTHERS
        else:
            patient.gender = Gender.UNKNOWN
        city = row.get("Detected City", None).strip()
        patient.detected_city = city
        patient.detected_district = row["Detected District"]
        state = row.get("Detected State", None).strip()
        patient.detected_state = state
        patient.detected_city_pt = Patient.get_point_for_location(city=city, state=state)
        patient.current_location_pt = patient.detected_city_pt
        patient.nationality = ""
        if row["Current Status"] in PatientStatus.CHOICES:
            patient.current_status = row["Current Status"]

        patient.notes = row["Notes"]
        patient.source = "\n".join([row["Source_1"], row["Source_2"], row["Source_3"]]).strip()
        patient.nationality = row["Nationality"]


        patient.save()
