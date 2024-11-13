from django.urls import path
from . import views  # Import your views
app_name = 'blockchain_service'
urlpatterns = [
    path('', views.home, name='home'),
    path('submitTransaction/', views.SubmitBlockchainTransactionView.as_view(), name='submitTransaction'),
    path('transactionStatus/', views.BlockchainTransactionStatusView.as_view(), name='transactionStatus'),
    # Add more paths as needed
]
