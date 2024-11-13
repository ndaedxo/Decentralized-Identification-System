# urls.py

from django.urls import path
from .views import UserSessionListView, RevokeSessionView, RevokeAllSessionsView,home
app_name = 'sessionManager'
urlpatterns = [
    path('', home, name='home'),
    path('sessions/', UserSessionListView.as_view(), name='session-list'),
    path('sessions/<int:session_id>/revoke/', RevokeSessionView.as_view(), name='revoke-session'),
    path('sessions/revoke-all/', RevokeAllSessionsView.as_view(), name='revoke-all-sessions'),
]
