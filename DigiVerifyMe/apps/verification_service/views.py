# verification_service/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import VerificationRequest
from .serializers import VerificationRequestSerializer
from .services import verify_zkp_proof  # Adjusted import
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.urls import reverse

@api_view(['GET'])
def home(request):
    urls = {
        'home': request.build_absolute_uri(reverse('verification_service:home')),
        'submitVerification': request.build_absolute_uri(reverse('verification_service:submitVerification')),
        'verificationStatus': request.build_absolute_uri(reverse('verification_service:verificationStatus')),
        'processVerification': request.build_absolute_uri(reverse('verification_service:processVerification')),
    }
    return Response({
        "message": "Welcome to the Verification Service!",
        "available_urls": urls,
    })


class SubmitVerificationView(generics.CreateAPIView):
    serializer_class = VerificationRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VerificationStatusView(generics.RetrieveAPIView):
    queryset = VerificationRequest.objects.all()
    serializer_class = VerificationRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class ProcessVerificationView(generics.UpdateAPIView):
    queryset = VerificationRequest.objects.all()
    serializer_class = VerificationRequestSerializer
    permission_classes = [permissions.IsAdminUser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if verify_zkp_proof(instance.zkp_proof):
            instance.status = 'APPROVED'
        else:
            instance.status = 'REJECTED'
        instance.save()
        return Response(self.get_serializer(instance).data)
