from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    # Payment URLs
    path('', views.payment_list_view, name='payment_list'),
    path('create/', views.create_payment_view, name='create_payment'),
    path('<int:payment_id>/', views.payment_detail_view, name='payment_detail'),
    path('<int:payment_id>/edit/', views.edit_payment_view, name='edit_payment'),
    path('<int:payment_id>/delete/', views.delete_payment_view, name='delete_payment'),
    path('<int:payment_id>/mark-paid/', views.mark_payment_paid_view, name='mark_payment_paid'),
    
    # Payment Summary URLs
    path('summaries/', views.payment_summary_list_view, name='payment_summary_list'),
    path('summaries/create/', views.create_payment_summary_view, name='create_payment_summary'),
    path('summaries/<int:summary_id>/', views.payment_summary_detail_view, name='payment_summary_detail'),
    path('summaries/<int:summary_id>/edit/', views.edit_payment_summary_view, name='edit_payment_summary'),
    path('summaries/<int:summary_id>/delete/', views.delete_payment_summary_view, name='delete_payment_summary'),
    
    # Payment Reports
    path('student/<int:student_id>/', views.student_payments_view, name='student_payments'),
    path('student/<int:student_id>/report/', views.student_payment_report_view, name='student_payment_report'),
    path('overdue/', views.overdue_payments_view, name='overdue_payments'),
    path('financial-report/', views.financial_report_view, name='financial_report'),
]
