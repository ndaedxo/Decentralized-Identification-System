# models.py

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class ZKPSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='zkp_settings_zeroknowledgeproof')
    enable_age_verification = models.BooleanField(default=True)
    enable_identity_verification = models.BooleanField(default=True)
    default_proof_type = models.CharField(max_length=50, default="standard")

    def __str__(self):
        return f"ZKP Settings for {self.user.username}"


class ZKPRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    proof_data = models.TextField()  # Store proof data as a large string
    proof_type = models.CharField(max_length=50)  # Example: age, identity
    verified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ZKP Record for {self.user.username} ({self.proof_type})"
