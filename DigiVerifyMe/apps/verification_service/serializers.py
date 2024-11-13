# verification_service/serializers.py
from rest_framework import serializers
from .models import VerificationRequest

class VerificationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationRequest
        fields = ['id', 'user', 'zkp_proof', 'status', 'created_at', 'updated_at']
        read_only_fields = ['user', 'status', 'created_at', 'updated_at']
