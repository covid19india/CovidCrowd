from rest_framework import serializers
from .models import Patient, PatientHistory


class PatientHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientHistory
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    history = PatientHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = '__all__'


class PatientOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            "id",
            "unique_id",
            "government_id",
            "diagnosed_date",
            "age",
            "gender",
            "detected_city",
            "detected_city_pt",
            "detected_district",
            "detected_state",
            "nationality",
            "current_status",
            "status_change_date",
            "notes",
            "current_location",
            "current_location_pt",
            "contacts"
        ]
