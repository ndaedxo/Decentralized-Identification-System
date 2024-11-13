# Backend\DigiVerifyMe\DigiVerifyMe\views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse
from rest_framework import generics, permissions, status

class HomeView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        data = {
            'message': 'Welcome to DigiVerifyMe!',
            'description': 'Your decentralized identity verification solution.',
            'links': {
                # Correcting reverse URL lookups
                'api': request.build_absolute_uri(reverse('api:home')),  # Use 'api:home'
                'adminWebapp': request.build_absolute_uri(reverse('adminWebapp:dashboard')),  # Use 'adminWebapp:home' if it exists
            }
        }
        return Response(data, status=status.HTTP_200_OK)
