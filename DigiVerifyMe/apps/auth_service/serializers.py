# auth_service/serializers.py
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate  # Add this line

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'email', 'wallet_address', 'did','role', 'status', 
            'profile_picture', 'social_media_links', 'reputation_score', 
            'multi_signature_requirements', 'last_active_timestamp'
        ]
        read_only_fields = ['id', 'wallet_address','last_active_timestamp']  # Prevent these fields from being updated

class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role']
        extra_kwargs = {
            'role': {'default': 'user'},  # Default role can be set here if not provided
        }

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])  # Ensure the password is hashed
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    username_or_email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username_or_email = data.get('username_or_email')
        password = data.get('password')
        if username_or_email and password:
            user = authenticate(username=username_or_email, password=password)  # Now authenticate is defined
            if user:
                data['user'] = user
            else:
                raise serializers.ValidationError("Invalid credentials")
        else:
            raise serializers.ValidationError("Must include username or email and password")
        return data


class UserLogoutSerializer(serializers.Serializer):
    pass