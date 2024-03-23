from rest_framework.serializers import ModelSerializer
from api.models import PainInformation, Diagnosis, AdditionalInfo

class DiagnosisSerializer(ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = '__all__'

class AdditionalInfoSerializer(ModelSerializer):
    class Meta:
        model = AdditionalInfo
        fields = '__all__'

class PainInformationSerializer(ModelSerializer):
    diagnosis = DiagnosisSerializer()
    additional_info = AdditionalInfoSerializer()

    class Meta:
        model = PainInformation
        fields = '__all__'
