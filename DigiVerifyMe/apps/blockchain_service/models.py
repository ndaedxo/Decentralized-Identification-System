# blockchain_service/models.py
from django.db import models
from django.conf import settings

class BlockchainTransaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    transaction_hash = models.CharField(max_length=66)  
    contract_address = models.CharField(max_length=42)  
    function_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('FAILED', 'Failed')
    ], default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
