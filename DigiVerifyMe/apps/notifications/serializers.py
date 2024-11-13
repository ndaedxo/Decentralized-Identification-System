# serializers.py

from rest_framework import serializers
from .models import Notification, NotificationPreferences

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'title', 'message', 'created_at', 'is_read']


class NotificationPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationPreferences
        fields = ['receive_verification_requests', 'receive_security_alerts', 'receive_credential_updates']
