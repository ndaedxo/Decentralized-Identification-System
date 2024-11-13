# serializers.py

from rest_framework import serializers
from .models import ZKPSettings, ZKPRecord

class ZKPSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZKPSettings
        fields = ['enable_age_verification', 'enable_identity_verification', 'default_proof_type']


class ZKPRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZKPRecord
        fields = ['proof_data', 'proof_type', 'verified_at']
