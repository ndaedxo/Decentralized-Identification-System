# Backend\DigiVerifyMe\apps\api\urls.py
# apps/api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HomeView  # Ensure this is the correct view import

app_name = 'api'
router = DefaultRouter()

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Home page link
    path('auth/', include('apps.auth_service.urls', namespace='auth_service')),  # Include auth_service URLs
    path('verification/', include('apps.verification_service.urls', namespace='verification_service')),
    path('blockchain/', include('apps.blockchain_service.urls', namespace='blockchain_service')),
    path('kyc/', include('apps.kyc_integration.urls', namespace='kyc_integration')),
    path('settings/', include('apps.settings.urls', namespace='settings')),
    path('zeroknowledgeproof/', include('apps.zeroknowledgeproof.urls', namespace='zeroknowledgeproof')),
    path('notifications/', include('apps.notifications.urls', namespace='notifications')),
    path('sessionManager/', include('apps.sessionManager.urls', namespace='sessionManager')),
    path('wallet/', include('apps.wallet.urls', namespace='wallet')),
    path('api-auth/', include('rest_framework.urls', namespace='api-auth')),  # Include DRF's authentication views
]
