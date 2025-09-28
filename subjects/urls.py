from django.urls import path
from . import views

app_name = 'subjects'

urlpatterns = [
    # Subject URLs
    path('', views.subject_list_view, name='subject_list'),
    path('create/', views.create_subject_view, name='create_subject'),
    path('<int:subject_id>/', views.subject_detail_view, name='subject_detail'),
    path('<int:subject_id>/edit/', views.edit_subject_view, name='edit_subject'),
    path('<int:subject_id>/delete/', views.delete_subject_view, name='delete_subject'),
    path('<int:subject_id>/assign-teacher/', views.assign_teacher_view, name='assign_teacher'),
    
    # Class URLs
    path('classes/', views.class_list_view, name='class_list'),
    path('classes/create/', views.create_class_view, name='create_class'),
    path('classes/<int:class_id>/', views.class_detail_view, name='class_detail'),
    path('classes/<int:class_id>/edit/', views.edit_class_view, name='edit_class'),
    path('classes/<int:class_id>/delete/', views.delete_class_view, name='delete_class'),
    
    # Teacher-Subject Assignment URLs
    path('assignments/', views.teacher_subject_list_view, name='teacher_subject_list'),
    path('assignments/create/', views.create_teacher_subject_view, name='create_teacher_subject'),
    path('assignments/<int:assignment_id>/edit/', views.edit_teacher_subject_view, name='edit_teacher_subject'),
    path('assignments/<int:assignment_id>/delete/', views.delete_teacher_subject_view, name='delete_teacher_subject'),
]
