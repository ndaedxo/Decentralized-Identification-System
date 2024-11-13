from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserSettings

class UserSettingsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_create_user_settings(self):
        settings = UserSettings.objects.create(user=self.user)
        self.assertEqual(settings.user.username, 'testuser')
