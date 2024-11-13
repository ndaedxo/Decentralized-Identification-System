# services.py

from .models import UserSession

def create_user_session(user, device, location, ip_address, is_current=False):
    """
    Create a user session.
    """
    session = UserSession.objects.create(
        user=user,
        device=device,
        location=location,
        ip_address=ip_address,
        is_current=is_current
    )
    return session

def revoke_session(session_id):
    """
    Revoke a specific session.
    """
    try:
        session = UserSession.objects.get(id=session_id)
        session.delete()
        return True
    except UserSession.DoesNotExist:
        return False

def revoke_all_sessions(user):
    """
    Revoke all sessions for a user.
    """
    UserSession.objects.filter(user=user).delete()
