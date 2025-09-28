from django.contrib import admin
from .models import Payment, PaymentSummary


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """
    Payment Admin
    """
    list_display = ('student', 'payment_type', 'amount', 'due_date', 'status', 'paid_date')
    list_filter = ('payment_type', 'status', 'due_date')
    search_fields = ('student__user__first_name', 'student__user__last_name', 'receipt_number')
    ordering = ('-due_date',)
    
    fieldsets = (
        ('معلومات الدفعة', {'fields': ('student', 'payment_type', 'amount', 'due_date', 'paid_date', 'payment_method', 'status', 'receipt_number', 'notes')}),
    )


@admin.register(PaymentSummary)
class PaymentSummaryAdmin(admin.ModelAdmin):
    """
    Payment Summary Admin
    """
    list_display = ('student', 'academic_year', 'total_due', 'total_paid', 'total_pending', 'total_overdue')
    list_filter = ('academic_year',)
    search_fields = ('student__user__first_name', 'student__user__last_name')
    ordering = ('-academic_year',)
    
    fieldsets = (
        ('معلومات الملخص', {'fields': ('student', 'academic_year', 'total_due', 'total_paid', 'total_pending', 'total_overdue')}),
    )