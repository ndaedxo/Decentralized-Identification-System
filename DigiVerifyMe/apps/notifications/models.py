# models.py

from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    """
    Model to store notifications for users.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username} - {self.title}"


class NotificationPreferences(models.Model):
    """
    Model to manage user preferences for receiving notifications.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    receive_verification_requests = models.BooleanField(default=True)
    receive_security_alerts = models.BooleanField(default=True)
    receive_credential_updates = models.BooleanField(default=True)

    def __str__(self):
        return f"Preferences for {self.user.username}"
