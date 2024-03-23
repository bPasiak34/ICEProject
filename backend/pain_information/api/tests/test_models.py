from django.test import TestCase
from api.models import PainInformation, Diagnosis, AdditionalInfo
from django.db import models
from django.core.exceptions import ValidationError

class PainInformationModelTest(TestCase):
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

    def test_pain_information_creation(self):
        self.assertEqual(self.pain_info.note, 'Test note')
        self.assertEqual(self.pain_info.area, 'Test area')
        self.assertEqual(self.pain_info.detailed_area_place, 'Test detailed area')
        self.assertEqual(self.pain_info.type_of_pain, 'pulsating')
        self.assertEqual(self.pain_info.intensity_of_pain, 5)
        self.assertFalse(self.pain_info.has_additional_info)
        self.assertFalse(self.pain_info.has_diagnosis)

    def test_pain_information_str(self):
        self.assertEqual(str(self.pain_info), f"Pain Information (code: {self.pain_info.code})")

class DiagnosisModelTest(TestCase):
    def setUp(self):
        self.pain_info = PainInformation.objects.create(
            note='Test note',
            area='Test area',
            detailed_area_place='Test detailed area',
            type_of_pain='pulsating',
            intensity_of_pain=5,
            has_additional_info=False,
            has_diagnosis=True
        )
        self.diagnosis = Diagnosis.objects.create(
            code=self.pain_info,
            diagnosis_note='Test diagnosis note'
        )

    def test_diagnosis_creation(self):
        self.assertEqual(self.diagnosis.code, self.pain_info)
        self.assertEqual(self.diagnosis.diagnosis_note, 'Test diagnosis note')

    def test_diagnosis_str(self):
        self.assertEqual(str(self.diagnosis), f"Diagnosis for Pain Information (code: {self.diagnosis.code.code})")
    
    def test_created_at_field_auto_now_add(self):
        field = Diagnosis._meta.get_field('created_at')
        self.assertTrue(field.auto_now_add)
        self.assertFalse(field.auto_now)


class AdditionalInfoModelTest(TestCase):
    def setUp(self):
        self.pain_info = PainInformation.objects.create(
            note='Test note',
            area='Test area',
            detailed_area_place='Test detailed area',
            type_of_pain='pulsating',
            intensity_of_pain=5,
            has_additional_info=True,
            has_diagnosis=False,
        )
        self.additional_info = AdditionalInfo.objects.create(
            code=self.pain_info,
            height_cm=170.5,
            weight_kg=65.0,  
            age=30,
            past_illnesses='Test past illnesses',
            note='Test additional info note'
        )

    def test_additional_info_creation(self):
        self.assertEqual(self.additional_info.code, self.pain_info)
        self.assertAlmostEqual(self.additional_info.height_cm, 170.5, places=1)
        self.assertAlmostEqual(self.additional_info.weight_kg, 65.0, places=1)
        self.assertEqual(self.additional_info.age, 30)
        self.assertEqual(self.additional_info.past_illnesses, 'Test past illnesses')
        self.assertEqual(self.additional_info.note, 'Test additional info note')

    def test_additional_info_str(self):
        self.assertEqual(str(self.additional_info), f"Additional Information for Pain Information (code: {self.additional_info.code.code})")
    
    def test_missing_height_cm(self):
        self.additional_info.height_cm = None
        with self.assertRaises(ValidationError):
            self.additional_info.full_clean()

    def test_missing_weight_kg(self):
        self.additional_info.weight_kg = None
        with self.assertRaises(ValidationError):
            self.additional_info.full_clean()

    def test_missing_age(self):
        self.additional_info.age = None
        with self.assertRaises(ValidationError):
            self.additional_info.full_clean() 

    def test_missing_past_illnesses_is_blank(self):
        self.additional_info.past_illnesses = ''
        self.additional_info.full_clean()        

    def test_missing_note_is_blank(self):
        self.additional_info.note = '' 
        self.additional_info.full_clean()