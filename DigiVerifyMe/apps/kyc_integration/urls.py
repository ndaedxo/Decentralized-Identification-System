from django.urls import path
from . import views  # Import your views
app_name = 'kyc_integration'
urlpatterns = [
    path('', views.home, name='home'),
    path('kyc/', views.InitiateKYCView.as_view(), name='kyc'),
    path('kycStatus/', views.KYCStatusView.as_view(), name='kycStatus'),
    # Add more paths as needed
]
