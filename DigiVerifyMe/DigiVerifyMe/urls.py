# Backend\DigiVerifyMe\DigiVerifyMe\urls.py
from django.contrib import admin
from django.urls import path, include
from .views import HomeView  # Import the HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('api/', include('apps.api.urls', namespace='api')),  # Remove leading slash
    path('adminWebapp/', include('apps.adminWebapp.urls', namespace='adminWebapp')),
  # Home page link
    path('auth/', include('apps.auth_service.urls', namespace='auth_service')),  # Ensure namespace is set correctly
    path('verification/', include('apps.verification_service.urls', namespace='verification_service')),
    path('blockchain/', include('apps.blockchain_service.urls', namespace='blockchain_service')),
    path('kyc/', include('apps.kyc_integration.urls', namespace='kyc_integration')),
    path('settings/', include('apps.settings.urls', namespace='settings')),
    path('zeroknowledgeproof/', include('apps.zeroknowledgeproof.urls', namespace='zeroknowledgeproof')),
    path('notifications/', include('apps.notifications.urls', namespace='notifications')),
    path('sessionManager/', include('apps.sessionManager.urls', namespace='sessionManager')),
    path('wallet/', include('apps.wallet.urls', namespace='wallet')),
]

