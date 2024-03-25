from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from api.models import PainInformation, Diagnosis, AdditionalInfo
from rest_framework.response import Response
from rest_framework import status

class DiagnosisSerializer(ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = '__all__'
        
    def create(self, validated_data):
        code = validated_data.pop('code') 
        
        if code.has_diagnosis:
            raise ValidationError("Diagnosis object already exists for this PainInformation object.")
        
        code.has_diagnosis = True
        code.save()
        
        validated_data['code'] = code  
        return super().create(validated_data)
    
    def validate_diagnosis_note(self, value):
        if len(value.strip()) == 0:
            raise ValidationError("Diagnosis note cannot be empty.")
        return value
        if len(value) > 1000000:
            raise ValidationError("Diagnosis note cannot be longer than 1000000 characters.")


class AdditionalInfoSerializer(ModelSerializer):
    class Meta:
        model = AdditionalInfo
        fields = '__all__'

    def create(self, validated_data):
        code = validated_data.pop('code') 
        
        if code.has_additional_info:
            raise ValidationError("AdditionalInfo object already exists for this PainInformation object.")
        
        code.has_additional_info = True
        code.save()
        
        validated_data['code'] = code  
        return super().create(validated_data) 
    
    def validate_height_cm(self, value):
        if value < 0:
            raise ValidationError("Height cannot be negative.")
        return value
        if value > 300:
            raise ValidationError("Height cannot be greater than 300 cm.")
    
    def validate_weight_kg(self, value):
        if value < 0:
            raise ValidationError("Weight cannot be negative.")
        if value > 500:
            raise ValidationError("Weight cannot be greater than 500 kg.")
        return value
    
    def validate_age(self, value):
        if value < 0:
            raise ValidationError("Age cannot be negative.")
        if value > 120:
            raise ValidationError("Age cannot be greater than 150.")
        return value


class PainInformationSerializer(ModelSerializer):

    class Meta:
        model = PainInformation
        fields = '__all__'
        read_only_fields = ('created_at', 'has_additional_info', 'has_diagnosis')
    