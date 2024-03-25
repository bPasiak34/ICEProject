from django.contrib import admin
from api.models import PainInformation, Diagnosis, AdditionalInfo

admin.site.register(PainInformation)
admin.site.register(Diagnosis)
admin.site.register(AdditionalInfo)