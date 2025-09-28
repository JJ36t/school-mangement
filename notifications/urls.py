from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    # Notification URLs
    path('', views.notification_list_view, name='notification_list'),
    path('create/', views.create_notification_view, name='create_notification'),
    path('<int:notification_id>/', views.notification_detail_view, name='notification_detail'),
    path('<int:notification_id>/edit/', views.edit_notification_view, name='edit_notification'),
    path('<int:notification_id>/delete/', views.delete_notification_view, name='delete_notification'),
    path('<int:notification_id>/send/', views.send_notification_view, name='send_notification'),
    path('<int:notification_id>/mark-read/', views.mark_notification_read_view, name='mark_notification_read'),
    
    # Notification Template URLs
    path('templates/', views.notification_template_list_view, name='notification_template_list'),
    path('templates/create/', views.create_notification_template_view, name='create_notification_template'),
    path('templates/<int:template_id>/', views.notification_template_detail_view, name='notification_template_detail'),
    path('templates/<int:template_id>/edit/', views.edit_notification_template_view, name='edit_notification_template'),
    path('templates/<int:template_id>/delete/', views.delete_notification_template_view, name='delete_notification_template'),
    
    # Notification Log URLs
    path('logs/', views.notification_log_list_view, name='notification_log_list'),
    path('logs/<int:log_id>/', views.notification_log_detail_view, name='notification_log_detail'),
    
    # User Notifications
    path('my-notifications/', views.my_notifications_view, name='my_notifications'),
    path('unread-count/', views.unread_notifications_count_view, name='unread_notifications_count'),
]
