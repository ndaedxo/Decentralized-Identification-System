from django.urls import path
from . import views  # Import your views
app_name = 'verification_service'
urlpatterns = [
    path('', views.home, name='home'),
    path('submitVerification/', views.SubmitVerificationView.as_view(), name='submitVerification'),
    path('verificationStatus/', views.VerificationStatusView.as_view(), name='verificationStatus'),
    path('processVerification/', views.ProcessVerificationView.as_view(), name='processVerification'),
    # Add more paths as needed
]
