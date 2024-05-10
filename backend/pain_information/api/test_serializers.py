from django.test import TestCase
from api.models import PainInformation, Diagnosis, AdditionalInfo
from api.serializers import PainInformationSerializer, DiagnosisSerializer, AdditionalInfoSerializer

class PainInformationSerializerTest(TestCase):
    def setUp(self):
        self.pain_info = PainInformation.objects.create(
            note='Test note',
            area='Test area',
            detailed_area_place='Test detailed area',
            type_of_pain='pulsating',
            intensity_of_pain=5,
            has_additional_info=False,
            has_diagnosis=False
        )
        self.diagnosis = Diagnosis.objects.create(
            code=self.pain_info,
            diagnosis_note='Test diagnosis note'
        )
        self.additional_info = AdditionalInfo.objects.create(
            code=self.pain_info,
            height_cm=170.5,
            weight_kg=65.0,  
            age=30,
            past_illnesses='Test past illnesses',
            note='Test additional info note'
        )

    def test_pain_information_serializer(self):
        serializer = PainInformationSerializer(instance=self.pain_info)
        expected_data = {
            'id': self.pain_info.id,
            'note': 'Test note',
            'area': 'Test area',
            'detailed_area_place': 'Test detailed area',
            'type_of_pain': 'pulsating',
            'intensity_of_pain': 5,
            'has_additional_info': False,
            'has_diagnosis': False,
            'diagnosis': None,
            'additional_info': None
        }
        self.assertEqual(serializer.data, expected_data)

    def test_diagnosis_serializer(self):
        serializer = DiagnosisSerializer(instance=self.diagnosis)
        expected_data = {
            'id': self.diagnosis.id,
            'code': self.pain_info.id,
            'diagnosis_note': 'Test diagnosis note'
        }
        self.assertEqual(serializer.data, expected_data)

    def test_additional_info_serializer(self):
        serializer = AdditionalInfoSerializer(instance=self.additional_info)
        expected_data = {
            'id': self.additional_info.id,
            'code': self.pain_info.id,
            'height_cm': 170.5,
            'weight_kg': 65.0,
            'age': 30,
            'past_illnesses': 'Test past illnesses',
            'note': 'Test additional info note'
        }
        self.assertEqual(serializer.data, expected_data)