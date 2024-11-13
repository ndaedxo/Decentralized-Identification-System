# urls.py

from django.urls import path
from .views import home,ZKPSettingsView, GenerateZKPView, VerifyZKPView
app_name = 'zeroknowledgeproof'
urlpatterns = [
    path('',home, name='home'),
    path('settings/', ZKPSettingsView.as_view(), name='zkp-settings'),
    path('generate/', GenerateZKPView.as_view(), name='generate-zkp'),
    path('verify/', VerifyZKPView.as_view(), name='verify-zkp'),
]
