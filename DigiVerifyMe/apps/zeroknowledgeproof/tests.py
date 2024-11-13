# tests.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import ZKPRecord
from .services import generate_zero_knowledge_proof

class ZKPTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_generate_zkp(self):
        proof = generate_zero_knowledge_proof("test_data")
        self.assertIsNotNone(proof)

    def test_zkp_record_creation(self):
        ZKPRecord.objects.create(user=self.user, proof_data="sample_proof", proof_type="age")
        self.assertEqual(ZKPRecord.objects.count(), 1)
