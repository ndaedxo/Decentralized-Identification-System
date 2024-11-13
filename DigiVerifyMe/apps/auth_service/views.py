from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from .serializers import UserSignupSerializer, UserSerializer, UserLoginSerializer, UserLogoutSerializer
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def home(request):
    urls = {
        'home': request.build_absolute_uri(reverse('auth_service:home')),
        'login': request.build_absolute_uri(reverse('auth_service:login')),
        'signup': request.build_absolute_uri(reverse('auth_service:signup')),
        'profile': request.build_absolute_uri(reverse('auth_service:profile')),
    }
    return Response({
        "message": "Welcome to the Authentication Service!",
        "available_urls": urls,
    })

class UserSignupView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSignupSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  # Save the new user
        return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)

class UserLoginView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']  # Get the authenticated user
        login(request, user)  # Log the user in
        return Response({"message": "Login successful."}, status=status.HTTP_200_OK)


class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        logger.info(f"User {user.username} accessed their profile.")
        return user


class UserLogoutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserLogoutSerializer  # Add this line

    def post(self, request):
        logout(request)  # Log the user out
        return Response({"message": "Logout successful."}, status=status.HTTP_200_OK)
