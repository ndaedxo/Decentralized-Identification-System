# models.py

from django.db import models
from django.contrib.auth.models import User

class Credential(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    credential_type = models.CharField(max_length=100)
    issuer = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Revoked', 'Revoked')])
    expiry_date = models.DateField()
    id_number = models.CharField(max_length=50, unique=True)
    issued_date = models.DateField()

    def __str__(self):
        return f"{self.credential_type} from {self.issuer} for {self.user.username}"
