from django.db import models
from django.core.validators import MaxValueValidator


class PainInformation(models.Model):
    """Model used to store information about pain. It has a one-to-one relationship with the Diagnosis and AdditionalInfo models."""
    
    code = models.CharField(max_length=6, primary_key=True)
    note = models.TextField()
    area = models.CharField(max_length=50)  # Consider using a ChoiceField
    detailed_area_place = models.CharField(max_length=50)  # Not sure about this field
    type_of_pain = models.CharField(max_length=50)
    intensity_of_pain = models.PositiveIntegerField(validators=[MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)
    has_additional_info = models.BooleanField()
    has_diagnosis = models.BooleanField()
    
    def __str__(self):
        return f"Pain Information (code: {self.code})"


class Diagnosis(models.Model):
    """Model used to store the diagnosis of the pain (one-to-one relationship with PainInformation model)."""
    
    code = models.OneToOneField(PainInformation, on_delete=models.CASCADE)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Diagnosis for Pain Information (code: {self.code})"


class AdditionalInfo(models.Model):
    """Model used to store additional information about the pain of the patient (one-to-one relationship with PainInformation model)."""
    
    code = models.OneToOneField(PainInformation, on_delete=models.CASCADE)
    height = models.PositiveSmallIntegerField(validators=[MaxValueValidator(250)])
    weight_kg = models.PositiveSmallIntegerField(validators=[MaxValueValidator(1000)])
    age = models.PositiveSmallIntegerField(validators=[MaxValueValidator(150)])
    past_illnesses = models.TextField()
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Additional Information for Pain Information (code: {self.code})"
