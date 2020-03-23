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