from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    # Attendance URLs
    path('', views.attendance_list_view, name='attendance_list'),
    path('create/', views.create_attendance_view, name='create_attendance'),
    path('<int:attendance_id>/', views.attendance_detail_view, name='attendance_detail'),
    path('<int:attendance_id>/edit/', views.edit_attendance_view, name='edit_attendance'),
    path('<int:attendance_id>/delete/', views.delete_attendance_view, name='delete_attendance'),
    
    # Bulk Attendance URLs
    path('bulk-create/', views.bulk_create_attendance_view, name='bulk_create_attendance'),
    path('bulk-update/', views.bulk_update_attendance_view, name='bulk_update_attendance'),
    
    # Attendance Summary URLs
    path('summaries/', views.attendance_summary_list_view, name='attendance_summary_list'),
    path('summaries/create/', views.create_attendance_summary_view, name='create_attendance_summary'),
    path('summaries/<int:summary_id>/', views.attendance_summary_detail_view, name='attendance_summary_detail'),
    path('summaries/<int:summary_id>/edit/', views.edit_attendance_summary_view, name='edit_attendance_summary'),
    path('summaries/<int:summary_id>/delete/', views.delete_attendance_summary_view, name='delete_attendance_summary'),
    
    # Attendance Reports
    path('student/<int:student_id>/', views.student_attendance_view, name='student_attendance'),
    path('student/<int:student_id>/report/', views.student_attendance_report_view, name='student_attendance_report'),
    path('class/<int:class_id>/', views.class_attendance_view, name='class_attendance'),
    path('subject/<int:subject_id>/', views.subject_attendance_view, name='subject_attendance'),
]
