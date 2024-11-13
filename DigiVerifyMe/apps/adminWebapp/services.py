# adminWebapp/services.py
from django.utils import timezone
from datetime import timedelta
from apps.verification_service.models import VerificationRequest
from apps.auth_service.models import CustomUser
from django.db.models import Count, Avg, F, ExpressionWrapper, DurationField

def get_system_metrics():
    """Get current system metrics and statistics."""
    now = timezone.now()
    last_24h = now - timedelta(hours=24)
    
    metrics = {
        'total_users': CustomUser.objects.count(),
        'active_users_24h': CustomUser.objects.filter(last_active_timestamp__gte=last_24h).count(),
        'pending_verifications': VerificationRequest.objects.filter(status='PENDING').count(),
        'completed_verifications_24h': VerificationRequest.objects.filter(
            status__in=['APPROVED', 'REJECTED'],
            updated_at__gte=last_24h
        ).count(),
        'system_health': 'healthy',  # You might want to implement actual health checking logic
        'average_verification_time': VerificationRequest.objects.filter(
            status__in=['APPROVED', 'REJECTED']
        ).aggregate(
            avg_time=Avg(
                ExpressionWrapper(
                    F('updated_at') - F('created_at'),
                    output_field=DurationField()
                )
            )
        )['avg_time']
    }
    
    return metrics

def get_verification_statistics():
    """Get detailed verification statistics."""
    return {
        'total': VerificationRequest.objects.count(),
        'pending': VerificationRequest.objects.filter(status='PENDING').count(),
        'approved': VerificationRequest.objects.filter(status='APPROVED').count(),
        'rejected': VerificationRequest.objects.filter(status='REJECTED').count(),
    }

def get_user_statistics():
    """Get detailed user statistics."""
    now = timezone.now()
    thirty_days_ago = now - timedelta(days=30)
    # verified_users = CustomUser.objects.filter(is_active=True)  # Example of valid filter
    return {
        'total_users': CustomUser.objects.count(),
        'active_users': CustomUser.objects.filter(is_active=True).count(),
        'new_users_30d': CustomUser.objects.filter(date_joined__gte=thirty_days_ago).count(),
        'verified_users': CustomUser.objects.filter(
            verification_requests__status='APPROVED'
        ).distinct().count()


    }
