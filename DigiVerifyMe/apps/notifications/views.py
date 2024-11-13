# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Notification, NotificationPreferences
from .serializers import NotificationSerializer, NotificationPreferencesSerializer
from .services import create_notification, mark_notification_as_read
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.urls import reverse

@api_view(['GET'])
def home(request):
    urls = {
        'home': request.build_absolute_uri(reverse('notifications:home')),
        'notification-list': request.build_absolute_uri(reverse('notifications:notification-list')),
        'mark-notification-as-read': request.build_absolute_uri(reverse('notifications:mark-notification-as-read', kwargs={'notification_id': 1})),  # Example ID
        'notification-preferences': request.build_absolute_uri(reverse('notifications:notification-preferences')),
    }
    return Response({
        "message": "Welcome to Notifications!",
        "available_urls": urls,
    })


class NotificationListView(APIView):
    """
    API to list notifications for a user.
    """
    def get(self, request):
        notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)

class MarkNotificationAsReadView(APIView):
    """
    API to mark a notification as read.
    """
    def post(self, request, notification_id):
        notification = mark_notification_as_read(notification_id)
        if notification:
            return Response({"message": "Notification marked as read."}, status=status.HTTP_200_OK)
        return Response({"error": "Notification not found."}, status=status.HTTP_404_NOT_FOUND)

class NotificationPreferencesView(APIView):
    """
    API to update notification preferences for a user.
    """
    def get(self, request):
        preferences, created = NotificationPreferences.objects.get_or_create(user=request.user)
        serializer = NotificationPreferencesSerializer(preferences)
        return Response(serializer.data)

    def post(self, request):
        preferences, created = NotificationPreferences.objects.get_or_create(user=request.user)
        serializer = NotificationPreferencesSerializer(preferences, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
