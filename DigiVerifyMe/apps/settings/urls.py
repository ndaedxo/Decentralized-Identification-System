# Backend\DigiVerifyMe\apps\settings\urls.py
from django.urls import path
from .views import home, UserSettingsView, SecuritySettingsView, PrivacySettingsView, NotificationSettingsView, ZKPSettingsView

app_name = 'settings'

urlpatterns = [
    path('', home, name='home'),
    path('user/', UserSettingsView.as_view(), name='user-settings'),
    path('security/', SecuritySettingsView.as_view(), name='security-settings'),
    path('privacy/', PrivacySettingsView.as_view(), name='privacy-settings'),
    path('notifications/', NotificationSettingsView.as_view(), name='notification-settings'),
    path('zkp/', ZKPSettingsView.as_view(), name='zkp-settings'),
]
