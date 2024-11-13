# blockchain_service/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import BlockchainTransaction
from .serializers import BlockchainTransactionSerializer
from .services import submit_blockchain_transaction, get_transaction_status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.urls import reverse

@api_view(['GET'])
def home(request):
    urls = {
        'home': request.build_absolute_uri(reverse('blockchain_service:home')),
        'submitTransaction': request.build_absolute_uri(reverse('blockchain_service:submitTransaction')),
        'transactionStatus': request.build_absolute_uri(reverse('blockchain_service:transactionStatus')),
    }
    return Response({
        "message": "Welcome to the Blockchain Service!",
        "available_urls": urls,
    })


class SubmitBlockchainTransactionView(generics.CreateAPIView):
    serializer_class = BlockchainTransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        transaction_hash = submit_blockchain_transaction(
            self.request.user,
            serializer.validated_data['contract_address'],
            serializer.validated_data['function_name']
        )
        serializer.save(user=self.request.user, transaction_hash=transaction_hash)

class BlockchainTransactionStatusView(generics.RetrieveAPIView):
    queryset = BlockchainTransaction.objects.all()
    serializer_class = BlockchainTransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        status = get_transaction_status(instance.transaction_hash)
        instance.status = status
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)