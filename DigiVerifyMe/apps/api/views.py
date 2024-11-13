# DigiVerifyMe/apps/api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse

class HomeView(APIView):
    def get(self, request):
        app_links = [
            {'name': 'Authentication Service', 'url': request.build_absolute_uri(reverse('auth_service:home'))},  # Fix here
            {'name': 'Verification Service', 'url': request.build_absolute_uri(reverse('verification_service:home'))},
            {'name': 'Blockchain Service', 'url': request.build_absolute_uri(reverse('blockchain_service:home'))},
            {'name': 'KYC Integration', 'url': request.build_absolute_uri(reverse('kyc_integration:home'))},
            {'name': 'Settings', 'url': request.build_absolute_uri(reverse('settings:home'))},
            {'name': 'Zero Knowledge Proof', 'url': request.build_absolute_uri(reverse('zeroknowledgeproof:home'))},
            {'name': 'Notifications', 'url': request.build_absolute_uri(reverse('notifications:home'))},
            {'name': 'Session Manager', 'url': request.build_absolute_uri(reverse('sessionManager:home'))},
            {'name': 'Wallet', 'url': request.build_absolute_uri(reverse('wallet:home'))},
        ]
        
        return Response({'app_links': app_links}, status=status.HTTP_200_OK)
