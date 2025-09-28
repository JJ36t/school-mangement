from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # Dashboard URLs
    path('', views.dashboard_view, name='dashboard'),
    path('admin/', views.admin_dashboard_view, name='admin_dashboard'),
    path('teacher/', views.teacher_dashboard_view, name='teacher_dashboard'),
    path('student/', views.student_dashboard_view, name='student_dashboard'),
    path('parent/', views.parent_dashboard_view, name='parent_dashboard'),
    
    # Statistics URLs
    path('stats/', views.statistics_view, name='statistics'),
    path('stats/students/', views.student_statistics_view, name='student_statistics'),
    path('stats/teachers/', views.teacher_statistics_view, name='teacher_statistics'),
    path('stats/grades/', views.grade_statistics_view, name='grade_statistics'),
    path('stats/attendance/', views.attendance_statistics_view, name='attendance_statistics'),
    path('stats/payments/', views.payment_statistics_view, name='payment_statistics'),
]
