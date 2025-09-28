from django.urls import path
from . import views

app_name = 'grades'

urlpatterns = [
    # Grade URLs
    path('', views.grade_list_view, name='grade_list'),
    path('create/', views.create_grade_view, name='create_grade'),
    path('<int:grade_id>/', views.grade_detail_view, name='grade_detail'),
    path('<int:grade_id>/edit/', views.edit_grade_view, name='edit_grade'),
    path('<int:grade_id>/delete/', views.delete_grade_view, name='delete_grade'),
    
    # Grade Summary URLs
    path('summaries/', views.grade_summary_list_view, name='grade_summary_list'),
    path('summaries/create/', views.create_grade_summary_view, name='create_grade_summary'),
    path('summaries/<int:summary_id>/', views.grade_summary_detail_view, name='grade_summary_detail'),
    path('summaries/<int:summary_id>/edit/', views.edit_grade_summary_view, name='edit_grade_summary'),
    path('summaries/<int:summary_id>/delete/', views.delete_grade_summary_view, name='delete_grade_summary'),
    
    # Student Grade Reports
    path('student/<int:student_id>/', views.student_grades_view, name='student_grades'),
    path('student/<int:student_id>/report/', views.student_grade_report_view, name='student_grade_report'),
    path('subject/<int:subject_id>/', views.subject_grades_view, name='subject_grades'),
]
