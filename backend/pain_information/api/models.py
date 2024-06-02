from django.db import models
from .utils.generate_code import generate_code

class PainInformation(models.Model):
    """Model used to store information about pain. It has a one-to-one relationship with the Diagnosis and AdditionalInfo models."""
    TYPE_OF_PAIN_CHOICES = (
        ('pulsating', 'Pulsating'),
        ('sharp', 'Sharp'),
        ('dull', 'Dull'),
        ('throbbing', 'Throbbing'),
    )
    TYPE_OF_BODY_SIDE_CHOICES = (
        ('front', 'Front'),
        ('back', 'Back'),
        ('leftSide', 'Left Side'),
        ('rightSide', 'Right Side'),
    )

    code = models.CharField(max_length=6, primary_key=True, default=generate_code, editable=False)
    note = models.TextField(blank=True)
    pain_location_x = models.DecimalField(default=-500, max_digits=4, decimal_places=1)
    pain_location_y = models.DecimalField(default=-500, max_digits=4, decimal_places=1)
    body_side = models.CharField(max_length=10, blank=True, choices=TYPE_OF_BODY_SIDE_CHOICES)
    type_of_pain = models.CharField(max_length=12, choices=TYPE_OF_PAIN_CHOICES)
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
    current_medications = models.TextField(blank=True)
    note = models.TextField(blank=True)
    
    def __str__(self):
        return f"Additional Information for Pain Information (code: {self.code.code})"
