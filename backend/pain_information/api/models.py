from django.db import models
from .utils.generate_code import generate_code

class PainInformation(models.Model):
    """Model used to store information about pain. It has a one-to-one relationship with the Diagnosis and AdditionalInfo models."""


    code = models.CharField(max_length=6, primary_key=True, default=generate_code, editable=False)
    note = models.TextField(blank=True)
    area = models.CharField(max_length=50)  # Probably using a ChoiceField later
    detailed_area_place = models.CharField(max_length=50)  # Not sure about this field
    type_of_pain = models.CharField(max_length=50)
    intensity_of_pain = models.PositiveIntegerField() # 0-10
    created_at = models.DateTimeField(auto_now_add=True) 
    has_additional_info = models.BooleanField(default=False) 
    has_diagnosis = models.BooleanField(default=False) 

    def __str__(self):
        return f"Pain Information (code: {self.code})"


class Diagnosis(models.Model):
    """Model used to store the diagnosis of the pain (one-to-one relationship with PainInformation model)."""
    
    code = models.OneToOneField(PainInformation, primary_key=True, on_delete=models.CASCADE)
    diagnosis_note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Diagnosis for Pain Information (code: {self.code.code})"


class AdditionalInfo(models.Model):
    """Model used to store additional information about the pain of the patient (one-to-one relationship with PainInformation model)."""
    
    code = models.OneToOneField(PainInformation, primary_key=True, on_delete=models.CASCADE)
    height_cm = models.DecimalField(max_digits=4, decimal_places=1)
    weight_kg = models.DecimalField(max_digits=4, decimal_places=1)
    age = models.PositiveSmallIntegerField()
    past_illnesses = models.TextField(blank=True)
    note = models.TextField(blank=True)
    
    def __str__(self):
        return f"Additional Information for Pain Information (code: {self.code.code})"
