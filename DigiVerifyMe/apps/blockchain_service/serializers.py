# blockchain_service/serializers.py
from rest_framework import serializers
from .models import BlockchainTransaction

class BlockchainTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockchainTransaction
        fields = ['id', 'user', 'transaction_hash', 'contract_address', 'function_name', 'status', 'created_at', 'updated_at']
        read_only_fields = ['user', 'transaction_hash', 'status', 'created_at', 'updated_at']
