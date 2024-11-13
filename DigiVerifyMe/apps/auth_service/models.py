# Backend\DigiVerifyMe\apps\auth_service\models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from apps.verification_service.models import VerificationRequest

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser, PermissionsMixin):
    wallet_address = models.CharField(max_length=142, blank=True)
    did = models.CharField(max_length=142, blank=True)

    role = models.CharField(max_length=50, choices=[('user', 'User')], default='user')
    status = models.CharField(max_length=50, default='active')
    profile_picture = models.URLField(blank=True, null=True)
    social_media_links = models.JSONField(null=True, blank=True)
    reputation_score = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    multi_signature_requirements = models.JSONField(null=True, default=dict, blank=True)
    last_active_timestamp = models.DateTimeField(auto_now=True)
    verification_requests = models.ManyToManyField(
        VerificationRequest,
        related_name='verified_users',
        blank=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    # Add related_name to avoid reverse accessor clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Custom related name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Custom related name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username
