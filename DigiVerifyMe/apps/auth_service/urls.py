# auth_service/urls.py
from django.urls import path
from .views import UserLoginView, UserSignupView, UserDetailView, UserLogoutView, home

app_name = 'auth_service'

urlpatterns = [
    path('', home, name='home'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('profile/', UserDetailView.as_view(), name='profile'),
    path('logout/', UserLogoutView.as_view(), name='logout'),  # Add this line
]
