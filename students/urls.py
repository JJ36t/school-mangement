from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    # Student URLs
    path('', views.student_list_view, name='student_list'),
    path('create/', views.create_student_view, name='create_student'),
    path('<int:student_id>/', views.student_detail_view, name='student_detail'),
    path('<int:student_id>/edit/', views.edit_student_view, name='edit_student'),
    path('<int:student_id>/delete/', views.delete_student_view, name='delete_student'),
    
    # Parent URLs
    path('parents/', views.parent_list_view, name='parent_list'),
    path('parents/create/', views.create_parent_view, name='create_parent'),
    path('parents/<int:parent_id>/', views.parent_detail_view, name='parent_detail'),
    path('parents/<int:parent_id>/edit/', views.edit_parent_view, name='edit_parent'),
    path('parents/<int:parent_id>/delete/', views.delete_parent_view, name='delete_parent'),
    
    # Student-Parent Relationship URLs
    path('<int:student_id>/parents/', views.student_parents_view, name='student_parents'),
    path('<int:student_id>/parents/add/', views.add_student_parent_view, name='add_student_parent'),
    path('<int:student_id>/parents/<int:parent_id>/remove/', views.remove_student_parent_view, name='remove_student_parent'),
]
