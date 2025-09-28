from django.urls import path
from . import views

app_name = 'teachers'

urlpatterns = [
    # Teacher URLs
    path('', views.teacher_list_view, name='teacher_list'),
    path('create/', views.create_teacher_view, name='create_teacher'),
    path('<int:teacher_id>/', views.teacher_detail_view, name='teacher_detail'),
    path('<int:teacher_id>/edit/', views.edit_teacher_view, name='edit_teacher'),
    path('<int:teacher_id>/delete/', views.delete_teacher_view, name='delete_teacher'),
    
    # Teacher Subject Assignment URLs
    path('<int:teacher_id>/subjects/', views.teacher_subjects_view, name='teacher_subjects'),
    path('<int:teacher_id>/subjects/assign/', views.assign_subject_view, name='assign_subject'),
    path('<int:teacher_id>/subjects/<int:subject_id>/remove/', views.remove_subject_view, name='remove_subject'),
]
