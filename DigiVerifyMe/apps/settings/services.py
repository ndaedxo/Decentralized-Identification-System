from .models import UserSettings



def update_notification_preferences(user, preferences):
    user_settings = UserSettings.objects.get(user=user)
    user_settings.email_notifications = preferences.get('email_notifications', user_settings.email_notifications)
    user_settings.save()
    return user_settings
