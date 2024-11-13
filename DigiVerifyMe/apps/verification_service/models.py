# verification_service/models.py
from django.db import models
from django.conf import settings

class VerificationRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='verification_requests', on_delete=models.CASCADE)
    zkp_proof = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('PENDING', 'Pending'),
            ('APPROVED', 'Approved'),
            ('REJECTED', 'Rejected')
        ],
        default='PENDING'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"VerificationRequest(id={self.id}, user={self.user}, status={self.status})"

