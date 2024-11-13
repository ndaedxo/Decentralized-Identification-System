# services.py

import random
import hashlib

def generate_zero_knowledge_proof(data):
    """
    Mock function to generate a Zero-Knowledge Proof.
    In practice, you'd use a ZKP library here.
    """
    proof = hashlib.sha256(data.encode()).hexdigest()  # Simplified proof generation
    return proof

def verify_zero_knowledge_proof(proof, data):
    """
    Verify a Zero-Knowledge Proof.
    """
    expected_proof = hashlib.sha256(data.encode()).hexdigest()
    return proof == expected_proof

def generate_mock_data():
    """
    Generate mock data for ZKP testing purposes.
    """
    return f"mock_data_{random.randint(1000, 9999)}"
