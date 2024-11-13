
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Notification
from .services import create_notification

class NotificationTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_create_notification(self):
        create_notification(self.user, "Test Notification", "This is a test message.")
        self.assertEqual(Notification.objects.count(), 1)

    def test_mark_notification_as_read(self):
        notification = Notification.objects.create(user=self.user, title="Test Notification", message="This is a test message.")
        notification.is_read = True
        notification.save()
        self.assertTrue(Notification.objects.get(id=notification.id).is_read)
