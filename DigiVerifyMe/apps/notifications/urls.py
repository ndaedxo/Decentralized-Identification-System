# urls.py

from django.urls import path
from .views import NotificationListView, MarkNotificationAsReadView, NotificationPreferencesView,home

app_name = 'notifications'
urlpatterns = [
    path('', home, name='home'),
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('notifications/<int:notification_id>/read/', MarkNotificationAsReadView.as_view(), name='mark-notification-as-read'),
    path('notifications/preferences/', NotificationPreferencesView.as_view(), name='notification-preferences'),
]
