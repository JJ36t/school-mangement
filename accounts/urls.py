from django.urls import path
from . import views, api_views

app_name = 'accounts'

urlpatterns = [
    # Authentication URLs
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    
    # Profile URLs
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    path('change-password/', views.change_password_view, name='change_password'),
    
    # User Management URLs (Admin only)
    path('users/', views.user_list_view, name='user_list'),
    path('users/create/', views.create_user_view, name='create_user'),
    path('users/<int:user_id>/', views.user_detail_view, name='user_detail'),
    path('users/<int:user_id>/edit/', views.edit_user_view, name='edit_user'),
    path('users/<int:user_id>/delete/', views.delete_user_view, name='delete_user'),
    
    # API URLs
    path('api/login/', api_views.login_api, name='api_login'),
    path('api/register/', api_views.register_api, name='api_register'),
    path('api/logout/', api_views.logout_api, name='api_logout'),
    path('api/profile/', api_views.profile_api, name='api_profile'),
    path('api/profile/update/', api_views.update_profile_api, name='api_update_profile'),
    path('api/change-password/', api_views.change_password_api, name='api_change_password'),
]
