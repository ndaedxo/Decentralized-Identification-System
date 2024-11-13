# services.py

from .models import Notification, User

def create_notification(user, title, message):
    """
    Create a notification for a user.
    """
    Notification.objects.create(user=user, title=title, message=message)


def mark_notification_as_read(notification_id):
    """
    Mark a specific notification as read.
    """
    try:
        notification = Notification.objects.get(id=notification_id)
        notification.is_read = True
        notification.save()
        return notification
    except Notification.DoesNotExist:
        return None


def send_bulk_notifications(users, title, message):
    """
    Send notifications to a group of users.
    """
    for user in users:
        create_notification(user, title, message)
