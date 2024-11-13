# Backend\DigiVerifyMe\apps\settings\views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserSettings, SecuritySettings, PrivacySettings, NotificationSettings, ZKPSettings
from .serializers import UserSettingsSerializer, SecuritySettingsSerializer, PrivacySettingsSerializer, NotificationSettingsSerializer, ZKPSettingsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from django.urls import reverse
from rest_framework.decorators import api_view
from django.shortcuts import render


@api_view(['GET'])
def home(request):
    urls = {
        'home': request.build_absolute_uri(reverse('settings:home')),
        'user-settings': request.build_absolute_uri(reverse('settings:user-settings')),
        'security-settings': request.build_absolute_uri(reverse('settings:security-settings')),
        'privacy-settings': request.build_absolute_uri(reverse('settings:privacy-settings')),
        'notification-settings': request.build_absolute_uri(reverse('settings:notification-settings')),
        'zkp-settings': request.build_absolute_uri(reverse('settings:zkp-settings')),
    }
    return Response({
        "message": "Welcome to Settings!",
        "available_urls": urls,
    })

class UserSettingsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user_settings = UserSettings.objects.get(user=request.user)
        except UserSettings.DoesNotExist:
            raise NotFound("User settings not found.")

        serializer = UserSettingsSerializer(user_settings)
        editable_fields = {field: serializer.data[field] for field in ['display_name', 'email_notifications', 'two_factor_auth', 'zkp_age_verification', 'zkp_identity_verification']}
        return Response({
            'form': editable_fields,
            'action': reverse('settings:user-settings'),  # Form submission URL
        })

    def post(self, request):
        user_settings, created = UserSettings.objects.get_or_create(user=request.user)
        serializer = UserSettingsSerializer(user_settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SecuritySettingsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            security_settings = SecuritySettings.objects.get(user=request.user)
        except SecuritySettings.DoesNotExist:
            raise NotFound("Security settings not found.")

        serializer = SecuritySettingsSerializer(security_settings)
        editable_fields = {field: serializer.data[field] for field in ['two_factor_auth', 'auto_logout_timer']}
        return Response({
            'form': editable_fields,
            'action': reverse('settings:security-settings'),  # Form submission URL
        })

    def post(self, request):
        security_settings, created = SecuritySettings.objects.get_or_create(user=request.user)
        serializer = SecuritySettingsSerializer(security_settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PrivacySettingsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            privacy_settings = PrivacySettings.objects.get(user=request.user)
        except PrivacySettings.DoesNotExist:
            raise NotFound("Privacy settings not found.")

        serializer = PrivacySettingsSerializer(privacy_settings)
        editable_fields = {field: serializer.data[field] for field in ['default_sharing_mode', 'automatic_verification', 'activity_logging']}
        return Response({
            'form': editable_fields,
            'action': reverse('settings:privacy-settings'),  # Form submission URL
        })

    def post(self, request):
        privacy_settings, created = PrivacySettings.objects.get_or_create(user=request.user)
        serializer = PrivacySettingsSerializer(privacy_settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotificationSettingsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            notification_settings = NotificationSettings.objects.get(user=request.user)
        except NotificationSettings.DoesNotExist:
            raise NotFound("Notification settings not found.")

        serializer = NotificationSettingsSerializer(notification_settings)
        editable_fields = {field: serializer.data[field] for field in ['verification_requests', 'security_alerts', 'credential_updates']}
        return Response({
            'form': editable_fields,
            'action': reverse('settings:notification-settings'),  # Form submission URL
        })

    def post(self, request):
        notification_settings, created = NotificationSettings.objects.get_or_create(user=request.user)
        serializer = NotificationSettingsSerializer(notification_settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ZKPSettingsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            zkp_settings = ZKPSettings.objects.get(user=request.user)
        except ZKPSettings.DoesNotExist:
            raise NotFound("ZKP settings not found.")

        serializer = ZKPSettingsSerializer(zkp_settings)
        editable_fields = {field: serializer.data[field] for field in ['enable_age_verification', 'enable_identity_verification', 'default_proof_type']}
        return Response({
            'form': editable_fields,
            'action': reverse('settings:zkp-settings'),  # Form submission URL
        })

    def post(self, request):
        zkp_settings, created = ZKPSettings.objects.get_or_create(user=request.user)
        serializer = ZKPSettingsSerializer(zkp_settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)