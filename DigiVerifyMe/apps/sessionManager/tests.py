# tests.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserSession
from .services import create_user_session, revoke_session

class UserSessionTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.session = create_user_session(self.user, "Chrome / MacBook Pro", "San Francisco, US", "192.168.1.1", True)

    def test_create_session(self):
        self.assertEqual(UserSession.objects.count(), 1)

    def test_revoke_session(self):
        revoke_session(self.session.id)
        self.assertEqual(UserSession.objects.count(), 0)
