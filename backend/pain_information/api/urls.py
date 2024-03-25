# urls.py file:

from django.urls import path
from .views import (
    PainInformationCreateAPIView,
    DiagnosisCreateAPIView,
    AdditionalInfoCreateAPIView,
    PainInformationRetrieveAPIView,
    DiagnosisRetrieveAPIView,
    AdditionalInfoRetrieveAPIView,
)

urlpatterns = [
    path('pain-information/create', PainInformationCreateAPIView.as_view(), name='pain-information-create'),
    path('pain-information/retrieve/<str:code>', PainInformationRetrieveAPIView.as_view(), name='pain-information-retrieve'),
    path('diagnosis/create', DiagnosisCreateAPIView.as_view(), name='diagnosis-create'),
    path('diagnosis/retrieve/<str:code>', DiagnosisRetrieveAPIView.as_view(), name='diagnosis-retrieve'),
    path('additional-info/create', AdditionalInfoCreateAPIView.as_view(), name='additional-info-create'),
    path('additional-info/retrieve/<str:code>', AdditionalInfoRetrieveAPIView.as_view(), name='additional-info-retrieve'),
]

