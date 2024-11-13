# adminWebapp/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class AdminLog(models.Model):
    admin_user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    target_model = models.CharField(max_length=100)
    target_id = models.IntegerField()
    details = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.admin_user.username} - {self.action} - {self.timestamp}"

class SystemMetrics(models.Model):
    total_users = models.IntegerField(default=0)
    active_verifications = models.IntegerField(default=0)
    completed_verifications = models.IntegerField(default=0)
    system_health = models.CharField(max_length=50, default='healthy')
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"System Metrics - {self.last_updated}"
