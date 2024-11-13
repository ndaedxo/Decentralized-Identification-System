# models.py

from django.db import models
from django.contrib.auth.models import User

class UserSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    last_active = models.DateTimeField(auto_now=True)
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.device} @ {self.location} ({self.ip_address})"
