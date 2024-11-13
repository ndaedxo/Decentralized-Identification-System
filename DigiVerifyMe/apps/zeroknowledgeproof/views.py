# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ZKPSettings, ZKPRecord
from .serializers import ZKPSettingsSerializer, ZKPRecordSerializer
from .services import generate_zero_knowledge_proof, verify_zero_knowledge_proof, generate_mock_data
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.urls import reverse

@api_view(['GET'])
def home(request):
    urls = {
        'home': request.build_absolute_uri(reverse('zeroknowledgeproof:home')),
        'zkp-settings': request.build_absolute_uri(reverse('zeroknowledgeproof:zkp-settings')),
        'generate-zkp': request.build_absolute_uri(reverse('zeroknowledgeproof:generate-zkp')),
        'verify-zkp': request.build_absolute_uri(reverse('zeroknowledgeproof:verify-zkp')),
    }
    return Response({
        "message": "Welcome to Zero Knowledge Proof!",
        "available_urls": urls,
    })


class ZKPSettingsView(APIView):
    """
    API to get and update ZKP settings for the user.
    """
    def get(self, request):
        zkp_settings = ZKPSettings.objects.get(user=request.user)
        serializer = ZKPSettingsSerializer(zkp_settings)
        return Response(serializer.data)

    def post(self, request):
        zkp_settings, created = ZKPSettings.objects.get_or_create(user=request.user)
        serializer = ZKPSettingsSerializer(zkp_settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenerateZKPView(APIView):
    """
    API to generate a Zero-Knowledge Proof for the user.
    """
    def post(self, request):
        data = request.data.get('data', generate_mock_data())  # Allow custom data or generate mock data
        proof = generate_zero_knowledge_proof(data)
        zkp_record = ZKPRecord.objects.create(user=request.user, proof_data=proof, proof_type="custom")
        serializer = ZKPRecordSerializer(zkp_record)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class VerifyZKPView(APIView):
    """
    API to verify a Zero-Knowledge Proof.
    """
    def post(self, request):
        data = request.data.get('data')
        proof = request.data.get('proof')
        if verify_zero_knowledge_proof(proof, data):
            return Response({"message": "Proof verified successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Proof verification failed."}, status=status.HTTP_400_BAD_REQUEST)


# Get history
