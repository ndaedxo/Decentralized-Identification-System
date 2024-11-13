# tests.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Credential

class WalletTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.credential = Credential.objects.create(
            user=self.user,
            credential_type="Government ID",
            issuer="National Identity Authority",
            status="Active",
            expiry_date="2025-12-31",
            id_number="123456789",
            issued_date="2020-01-01"
        )

    def test_credential_creation(self):
        self.assertEqual(Credential.objects.count(), 1)

    def test_revoke_credential(self):
        self.credential.status = 'Revoked'
        self.credential.save()
        self.assertEqual(self.credential.status, 'Revoked')
