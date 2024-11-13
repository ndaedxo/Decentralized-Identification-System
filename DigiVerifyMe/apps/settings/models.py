# Backend\DigiVerifyMe\apps\settings\models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='zkp_settings')
    display_name = models.CharField(max_length=100, blank=True)
    email_notifications = models.BooleanField(default=True)
    two_factor_auth = models.BooleanField(default=False)
    zkp_age_verification = models.BooleanField(default=False)
    zkp_identity_verification = models.BooleanField(default=False)

    def __str__(self):
        return f"Settings for {self.user.username}"


class SecuritySettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    two_factor_auth = models.BooleanField(default=False)
    auto_logout_timer = models.CharField(max_length=20, choices=[('15 minutes', '15 minutes'), ('30 minutes', '30 minutes'), ('1 hour', '1 hour'), ('Never', 'Never')], default='Never')

    def __str__(self):
        return f"Security Settings for {self.user.username}"


class PrivacySettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_sharing_mode = models.BooleanField(default=True)
    automatic_verification = models.BooleanField(default=False)
    activity_logging = models.BooleanField(default=True)

    def __str__(self):
        return f"Privacy Settings for {self.user.username}"




class NotificationSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verification_requests = models.BooleanField(default=True)
    security_alerts = models.BooleanField(default=True)
    credential_updates = models.BooleanField(default=True)

    def __str__(self):
        return f"Notification Settings for {self.user.username}"




class ZKPSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enable_age_verification = models.BooleanField(default=True)
    enable_identity_verification = models.BooleanField(default=True)
    default_proof_type = models.CharField(max_length=50, default="standard")

    def __str__(self):
        return f"ZKP Settings for {self.user.username}"
