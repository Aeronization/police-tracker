from rest_framework import serializers
from .models import (
    PoliceComplaint,
    Allegation,
    Ethnicity,
    Gender,
    Fado,
    Precinct,
    ContactReason,
    OutcomeDescription,
    BoardDisposition
)

class PoliceComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PoliceComplaint


class AllegationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Allegation


class EthnicitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Ethnicity


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Gender


class FadoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Fado


class PrecinctSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Precinct


class ContactReasonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ContactReason


class OutcomeDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = OutcomeDescription


class BoardDispositionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = BoardDisposition

