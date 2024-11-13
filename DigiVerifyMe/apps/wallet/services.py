# services.py

from .models import Credential

def revoke_credential(credential_id, user):
    """
    Revoke a specific credential if it belongs to the user.
    """
    try:
        credential = Credential.objects.get(id=credential_id, user=user)
        credential.status = 'Revoked'
        credential.save()
        return True
    except Credential.DoesNotExist:
        return False
