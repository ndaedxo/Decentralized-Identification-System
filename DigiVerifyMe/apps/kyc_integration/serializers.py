# kyc_integration/serializers.py
from rest_framework import serializers
from .models import KYCRequest

class KYCRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = KYCRequest
        fields = ['id', 'user', 'provider', 'status', 'external_id', 'created_at', 'updated_at']
        read_only_fields = ['user', 'status', 'external_id', 'created_at', 'updated_at']
