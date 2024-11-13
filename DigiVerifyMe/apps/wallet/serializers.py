# serializers.py

from rest_framework import serializers
from .models import Credential

class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credential
        fields = ['id', 'credential_type', 'issuer', 'status', 'expiry_date', 'id_number', 'issued_date']
