# serializers.py

from rest_framework import serializers
from .models import UserSession

class UserSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSession
        fields = ['id', 'device', 'location', 'ip_address', 'last_active', 'is_current']
