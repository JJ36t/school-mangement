from django.db import models
from django.conf import settings


class Payment(models.Model):
    """
    Payment model for School Management System
    """
    PAYMENT_TYPE_CHOICES = [
        ('tuition', 'رسوم دراسية'),
        ('transport', 'رسوم نقل'),
        ('books', 'رسوم كتب'),
        ('uniform', 'رسوم زي موحد'),
        ('activities', 'رسوم أنشطة'),
        ('other', 'أخرى'),
    ]
    
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'معلق'),
        ('paid', 'مدفوع'),
        ('overdue', 'متأخر'),
        ('cancelled', 'ملغي'),
    ]
    
    student = models.ForeignKey(
        'students.Student', 
        on_delete=models.CASCADE,
        related_name='student_payments',
        verbose_name='الطالب'
    )
    payment_type = models.CharField(
        max_length=10, 
        choices=PAYMENT_TYPE_CHOICES,
        verbose_name='نوع الدفع'
    )
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name='المبلغ'
    )
    due_date = models.DateField(verbose_name='تاريخ الاستحقاق')
    paid_date = models.DateField(null=True, blank=True, verbose_name='تاريخ الدفع')
    payment_method = models.CharField(
        max_length=20, 
        blank=True,
        null=True,
        verbose_name='طريقة الدفع'
    )
    status = models.CharField(
        max_length=10, 
        choices=PAYMENT_STATUS_CHOICES,
        default='pending',
        verbose_name='الحالة'
    )
    receipt_number = models.CharField(
        max_length=50, 
        unique=True, 
        null=True, 
        blank=True,
        verbose_name='رقم الإيصال'
    )
    notes = models.TextField(blank=True, verbose_name='ملاحظات')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    class Meta:
        verbose_name = 'دفعة'
        verbose_name_plural = 'الدفعات'

    def __str__(self):
        return f"{self.student} - {self.get_payment_type_display()} - {self.amount}"

    @property
    def is_overdue(self):
        """Check if payment is overdue"""
        from django.utils import timezone
        return self.due_date < timezone.now().date() and self.status != 'paid'


class PaymentSummary(models.Model):
    """
    Payment Summary model for financial reports
    """
    student = models.ForeignKey(
        'students.Student', 
        on_delete=models.CASCADE,
        related_name='student_payment_summaries',
        verbose_name='الطالب'
    )
    academic_year = models.CharField(max_length=20, verbose_name='السنة الدراسية')
    total_due = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0,
        verbose_name='إجمالي المستحق'
    )
    total_paid = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0,
        verbose_name='إجمالي المدفوع'
    )
    total_pending = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0,
        verbose_name='إجمالي المعلق'
    )
    total_overdue = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0,
        verbose_name='إجمالي المتأخر'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    class Meta:
        verbose_name = 'ملخص الدفعات'
        verbose_name_plural = 'ملخصات الدفعات'
        unique_together = ['student', 'academic_year']

    def __str__(self):
        return f"{self.student} - {self.academic_year}"

    def calculate_totals(self):
        """Calculate payment totals"""
        payments = Payment.objects.filter(
            student=self.student,
            created_at__year=self.academic_year.split('-')[0]
        )
        
        self.total_due = sum(p.amount for p in payments)
        self.total_paid = sum(p.amount for p in payments if p.status == 'paid')
        self.total_pending = sum(p.amount for p in payments if p.status == 'pending')
        self.total_overdue = sum(p.amount for p in payments if p.is_overdue)
        
        return {
            'total_due': self.total_due,
            'total_paid': self.total_paid,
            'total_pending': self.total_pending,
            'total_overdue': self.total_overdue
        }