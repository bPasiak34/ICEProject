from rest_framework.views import APIView 
from api.models import PainInformation, Diagnosis, AdditionalInfo

from rest_framework.response import Response
from rest_framework import status

from api.serializers import (
    PainInformationSerializer,
    DiagnosisSerializer,
    AdditionalInfoSerializer,
)
from django.shortcuts import get_object_or_404


class DiagnosisCreateAPIView(APIView):
    """
    View used to create a new Diagnosis object.
    """
    serializer_class = DiagnosisSerializer

    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdditionalInfoCreateAPIView(APIView):
    """
    View used to create a new AdditionalInfo object.
    """
    serializer_class = AdditionalInfoSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PainInformationCreateAPIView(APIView):
    """
    View used to create a new PainInformation object.
    """
    serializer_class = PainInformationSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PainInformationRetrieveAPIView(APIView):
    """
    View used to retrieve a PainInformation object.
    """
    serializer_class = PainInformationSerializer
    
    def get(self, request, code, *args, **kwargs):
        pain_info = PainInformation.objects.get(code=code)
        serializer = self.serializer_class(pain_info)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class AdditionalInfoRetrieveAPIView(APIView):
    """
    View used to retrieve an AdditionalInfo object.
    """
    serializer_class = AdditionalInfoSerializer
    
    def get(self, request, code, *args, **kwargs):
        try:
            additional_info = AdditionalInfo.objects.get(code=code)
            serializer = self.serializer_class(additional_info)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except AdditionalInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    

class DiagnosisRetrieveAPIView(APIView):
    """
    View used to retrieve a Diagnosis object.
    """
    serializer_class = DiagnosisSerializer
    
    def get(self, request, code, *args, **kwargs):
        try:
            diagnosis = Diagnosis.objects.get(code=code)
            serializer = self.serializer_class(diagnosis)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Diagnosis.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)