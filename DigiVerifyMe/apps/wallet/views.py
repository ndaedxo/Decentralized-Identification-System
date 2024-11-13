# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Credential
from .serializers import CredentialSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.urls import reverse

@api_view(['GET'])
def home(request):
    urls = {
        'home': request.build_absolute_uri(reverse('wallet:home')),
        'credential-list': request.build_absolute_uri(reverse('wallet:credential-list')),
        'credential-detail': request.build_absolute_uri(reverse('wallet:credential-detail', kwargs={'credential_id': 1})),  # Example ID
        'revoke-credential': request.build_absolute_uri(reverse('wallet:revoke-credential', kwargs={'credential_id': 1})),  # Example ID
    }
    return Response({
        "message": "Welcome to Wallet!",
        "available_urls": urls,
    })

class CredentialListView(APIView):
    """
    API to retrieve all credentials for the current user.
    """
    def get(self, request):
        credentials = Credential.objects.filter(user=request.user)
        serializer = CredentialSerializer(credentials, many=True)
        return Response(serializer.data)

class CredentialDetailView(APIView):
    """
    API to retrieve a single credential by its ID.
    """
    def get(self, request, credential_id):
        try:
            credential = Credential.objects.get(id=credential_id, user=request.user)
            serializer = CredentialSerializer(credential)
            return Response(serializer.data)
        except Credential.DoesNotExist:
            return Response({"error": "Credential not found."}, status=status.HTTP_404_NOT_FOUND)

class RevokeCredentialView(APIView):
    """
    API to revoke a specific credential.
    """
    def post(self, request, credential_id):
        try:
            credential = Credential.objects.get(id=credential_id, user=request.user)
            credential.status = 'Revoked'
            credential.save()
            return Response({"message": "Credential revoked successfully."}, status=status.HTTP_200_OK)
        except Credential.DoesNotExist:
            return Response({"error": "Credential not found."}, status=status.HTTP_404_NOT_FOUND)
