import os.path
import csv
import re

from datetime import datetime

from django.contrib.gis.geos import Point
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from patients.models import Patient, PatientHistory, Source
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
        parser.add_argument("--type", action="store", type=str, choices=["patients", "travel"],
                            default="patients")

    def handle(self, *args, **options):
        filepath = options["csvfile"]
        if not filepath:
            print("Error! Missing CSV File Path")
            return
        filepath = filepath[0]
        file_type = options["type"]
        if not os.path.isfile(filepath):
            print(f"Error! Cannot find file at: {filepath}")
            return

        with open(filepath, "r") as fp:
            reader = csv.DictReader(fp)
            print(file_type)
            if file_type == "patients":
                self._patient_data_import(reader)
            elif file_type == "travel":
                self._travel_history_import(reader)
            else:
                print(f"Cannot import file data type: {file_type}")
                return

    def _patient_data_import(self, reader):
        counter = 0
        skipped = 0
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
        patient.government_id = row["State Patient Number"]
        patient.diagnosed_date = datetime.strptime(row["Date Announced"], "%d/%m/%Y")
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
        patient.status_change_date = datetime.strptime(row["Status Change Date"], "%d/%m/%Y")

        patient.notes = row["Notes"]
        if row["Backup Notes"].strip() and row["Backup Notes"] != row["Notes"]:
            patient.notes += ".\n" + row["Backup Notes"]
        patient.nationality = row["Nationality"]
        patient.save()

        links = row["Contracted from which Patient (Suspected)"].split(",")
        for link in links:
            link = link.strip().strip("P")
            try:
                contact = Patient.objects.get(unique_id=link)
                patient.contacts.add(contact)
            except Patient.DoesNotExist:
                continue
        patient.save()

        for source in ["Source_1", "Source_2", "Source_3"]:
            text = row.get(source, "")
            if not text:
                continue
            if text.startswith("http") or text.startswith("www"):
                patient.source_set.create(url=text, is_verified=True)
            else:
                patient.source_set.create(description=text, is_verified=True)

    def _travel_history_import(self, reader):
        counter = 0
        skipped = 0
        patient_id_pattern = re.compile("[P|R](\d+)")
        for row in reader:
            if not row['PID'] or not row['Address']:
                print(f"Cannot import row without PID or Address")
                skipped += 1
                continue
            try:
                matches = patient_id_pattern.match(row["PID"])
                if not matches:
                    print(f"Patient ID is specified in a wrong format: {row['PID']}")
                    skipped += 1
                    continue
                patient_id = int(matches.groups()[0])
                address = row['Address']
                patient = Patient.objects.get(unique_id=patient_id)
                from_time = self._safe_parse_datetime(row["time_from"])
                # Using a text field might not be the best approach to find duplicates.
                # But I can't find any other field which can be used
                history = PatientHistory.objects.filter(patient_id=patient_id,time_from=from_time,address=address)
                if history.exists() and from_time:
                    print(f"Patient history already exists for patient: {patient_id} at time: {from_time} and address {address}")
                    skipped += 1
                    continue
            except (Patient.DoesNotExist):
                print(f"Patient not found: {row['PID']} Skipping the history")
                skipped += 1
                continue
            self._create_patient_history(row, patient)
            counter += 1
        print(
            f"SUCCESS: CSV File was imported. History entries created: {counter}, Skipped: {skipped}"
        )

    def _create_patient_history(self, row, patient):
        print(f"Creating new travel history for patient: {row['PID']}")

        history = PatientHistory()
        history.patient = patient
        history.address = row['Address']

        history.time_from = self._safe_parse_datetime(row["time_from"])
        history.time_to = self._safe_parse_datetime(row["time_to"])
        if row["lat_long"] is not None and row["lat_long"].strip() != "":
            lat, long = tuple(map(lambda x: float(x), row["lat_long"].split(",")[0:2]))
            history.address_pt = Point(lat, long)
        else:
            history.address_pt = Point(80, 20)
        history.type = row['Type']
        history.travel_mode = row['Mode of Travel']
        history.place_name = row['PlaceName']
        history.data_source = row['DataSource']

        history.save()

    @staticmethod
    def _safe_parse_datetime(value):
        try:
            parsed = make_aware(datetime.strptime(value, "%d/%m/%Y %H:%M:%S"))
            return parsed
        except ValueError:
            pass

        try:
            parsed = make_aware(datetime.strptime(value, "%d/%m/%Y %H:%M"))
            return parsed
        except ValueError:
            pass

        try:
            parsed = make_aware(datetime.strptime(value, "%d/%m/%Y %H:%M %p"))
            return parsed
        except ValueError:
            pass

        try:
            parsed = make_aware(datetime.strptime(value, "%d/%m/%Y %H.%M %p"))
            return parsed
        except ValueError:
            pass

        try:
            parsed = make_aware(datetime.strptime(value, "%d/%m/%Y"))
            return parsed
        except ValueError:
            return None