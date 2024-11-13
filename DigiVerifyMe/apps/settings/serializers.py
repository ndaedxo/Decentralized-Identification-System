from rest_framework import serializers
from .models import UserSettings
from .models import SecuritySettings,UserSettings


from .models import ZKPSettings

from .models import NotificationSettings

from .models import PrivacySettings

class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = [
            'display_name', 
            'email_notifications', 
            'two_factor_auth',
            'zkp_age_verification', 
            'zkp_identity_verification',
        ]



class SecuritySettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecuritySettings
        fields = ['two_factor_auth', 'auto_logout_timer']


# serializers.py


class PrivacySettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacySettings
        fields = ['default_sharing_mode', 'automatic_verification', 'activity_logging']



class NotificationSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationSettings
        fields = ['verification_requests', 'security_alerts', 'credential_updates']


class ZKPSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZKPSettings
        fields = ['enable_age_verification', 'enable_identity_verification', 'default_proof_type']
