# adminWebapp/api_views.py
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.http import HttpResponse
import csv
from datetime import datetime

from .models import AdminLog, SystemMetrics
from apps.verification_service.models import VerificationRequest
from apps.auth_service.models import CustomUser
from .services import get_system_metrics

@api_view(['POST'])
@permission_classes([IsAdminUser])
def toggle_user_status(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
        user.is_active = not user.is_active
        user.save()
        
        # Log the action
        AdminLog.objects.create(
            admin_user=request.user,
            action='TOGGLE_USER_STATUS',
            target_model='CustomUser',
            target_id=user.id,
            details={'new_status': 'active' if user.is_active else 'inactive'}
        )
        
        return Response({
            'success': True,
            'new_status': 'active' if user.is_active else 'inactive'
        })
    except CustomUser.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def process_verification(request, verification_id, action):
    try:
        verification = VerificationRequest.objects.get(id=verification_id)
        if action not in ['approve', 'reject']:
            return Response({'error': 'Invalid action'}, status=status.HTTP_400_BAD_REQUEST)
        
        verification.status = 'APPROVED' if action == 'approve' else 'REJECTED'
        verification.save()
        
        # Log the action
        AdminLog.objects.create(
            admin_user=request.user,
            action=f'{action.upper()}_VERIFICATION',
            target_model='VerificationRequest',
            target_id=verification.id,
            details={'new_status': verification.status}
        )
        
        return Response({'success': True})
    except VerificationRequest.DoesNotExist:
        return Response({'error': 'Verification request not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def export_data(request, data_type):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{data_type}-{datetime.now().strftime("%Y%m%d")}.csv"'
    
    writer = csv.writer(response)
    
    if data_type == 'users':
        writer.writerow(['Username', 'Email', 'Status', 'Role', 'Date Joined'])
        for user in CustomUser.objects.all():
            writer.writerow([
                user.username,
                user.email,
                'Active' if user.is_active else 'Inactive',
                user.role,
                user.date_joined.strftime('%Y-%m-%d %H:%M:%S')
            ])
    
    elif data_type == 'verifications':
        writer.writerow(['ID', 'User', 'Status', 'Created At', 'Updated At'])
        for verification in VerificationRequest.objects.all():
            writer.writerow([
                verification.id,
                verification.user.username,
                verification.status,
                verification.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                verification.updated_at.strftime('%Y-%m-%d %H:%M:%S')
            ])
    
    elif data_type == 'logs':
        writer.writerow(['Timestamp', 'Admin User', 'Action', 'Target Model', 'Target ID', 'Details'])
        for log in AdminLog.objects.all():
            writer.writerow([
                log.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                log.admin_user.username,
                log.action,
                log.target_model,
                log.target_id,
                str(log.details)
            ])
    
    else:
        return Response({'error': 'Invalid data type'}, status=status.HTTP_400_BAD_REQUEST)
    
    return response