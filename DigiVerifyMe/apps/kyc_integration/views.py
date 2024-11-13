# kyc_integration/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import KYCRequest
from .serializers import KYCRequestSerializer
from .services import initiate_kyc_process, check_kyc_status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.urls import reverse

@api_view(['GET'])
def home(request):
    urls = {
        'home': request.build_absolute_uri(reverse('kyc_integration:home')),
        'kyc': request.build_absolute_uri(reverse('kyc_integration:kyc')),
        'kycStatus': request.build_absolute_uri(reverse('kyc_integration:kycStatus')),
    }
    return Response({
        "message": "Welcome to KYC Integration!",
        "available_urls": urls,
    })


class InitiateKYCView(generics.CreateAPIView):
    serializer_class = KYCRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        external_id = initiate_kyc_process(self.request.user, serializer.validated_data['provider'])
        serializer.save(user=self.request.user, external_id=external_id)

class KYCStatusView(generics.RetrieveAPIView):
    queryset = KYCRequest.objects.all()
    serializer_class = KYCRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        status = check_kyc_status(instance.provider, instance.external_id)
        instance.status = status
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)