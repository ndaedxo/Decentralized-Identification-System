# DigiVerifyMe\apps\adminWebapp\urls.py
from django.urls import path
from . import views, api_views
from .views import signup_view, login_view, logout_view

app_name = 'adminWebapp'

urlpatterns = [
    # Existing view URLs
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('users/', views.UserManagementView.as_view(), name='user_management'),
    path('verifications/', views.VerificationManagementView.as_view(), name='verification_management'),
    path('logs/', views.AdminLogView.as_view(), name='admin_logs'),
    
    # API endpoints
    path('api/health/', views.SystemHealthAPIView.as_view(), name='system_health'),
    path('api/users/<int:user_id>/toggle-status/', api_views.toggle_user_status, name='toggle_user_status'),
    path('api/verifications/<int:verification_id>/<str:action>/', api_views.process_verification, name='process_verification'),
    path('api/export/<str:data_type>/', api_views.export_data, name='export_data'),



    path('webApp/signup/', signup_view, name='signupWeb'),
    path('webApp/login/', login_view, name='loginWeb'),  # Ensure this is correctly defined
    path('webApp/logout/', logout_view, name='logoutWeb'),
]