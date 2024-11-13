# DigiVerifyMe\apps\adminWebapp\views.py
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.db.models import Count, Q
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AdminLog, SystemMetrics
from apps.verification_service.models import VerificationRequest
from apps.auth_service.models import CustomUser
from .services import (
    get_system_metrics,
    get_verification_statistics,
    get_user_statistics
)
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from apps.auth_service.serializers import UserLoginSerializer, UserLogoutSerializer  # Make sure to import your serializers if needed
import logging
logger = logging.getLogger(__name__)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    login_url = 'webApp/login/'  # Redirect to the login page if the user is not authenticated

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff

class DashboardView(AdminRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_metrics'] = get_system_metrics()
        context['verification_stats'] = get_verification_statistics()
        context['user_stats'] = get_user_statistics()
        return context

class UserManagementView(AdminRequiredMixin, ListView):
    template_name = 'user_management.html'
    model = CustomUser
    context_object_name = 'users'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(username__icontains=search_query) |
                Q(email__icontains=search_query)
            )
        return queryset


class VerificationManagementView(AdminRequiredMixin, ListView):
    template_name = 'verification_management.html'
    model = VerificationRequest
    context_object_name = 'verifications'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        status_filter = self.request.GET.get('status', '')
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        return queryset
    

class AdminLogView(AdminRequiredMixin, ListView):
    template_name = 'admin_logs.html'
    model = AdminLog
    context_object_name = 'logs'
    paginate_by = 50

class SystemHealthAPIView(APIView):
    def get(self, request):
        metrics = get_system_metrics()
        return Response(metrics, status=status.HTTP_200_OK)


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Signup successful! You are now logged in.")
                return redirect('home')  # Redirect to a suitable page
            else:
                messages.error(request, "Login failed. Please try again.")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('adminWebapp:dashboard')  # Redirect to a suitable page
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')  # Redirect to a suitable page