# urls.py

from django.urls import path
from .views import home,CredentialListView, CredentialDetailView, RevokeCredentialView
app_name = 'wallet'
urlpatterns = [
    path('',home, name='home'),
    path('wallet/credentials/', CredentialListView.as_view(), name='credential-list'),
    path('wallet/credentials/<int:credential_id>/', CredentialDetailView.as_view(), name='credential-detail'),
    path('wallet/credentials/<int:credential_id>/revoke/', RevokeCredentialView.as_view(), name='revoke-credential'),
]
