from django.db import models
from django.conf import settings


class Notification(models.Model):
    """
    Notification model for School Management System
    """
    NOTIFICATION_TYPE_CHOICES = [
        ('general', 'عام'),
        ('grade', 'درجة'),
        ('attendance', 'حضور'),
        ('payment', 'دفعة'),
        ('exam', 'امتحان'),
        ('event', 'فعالية'),
        ('announcement', 'إعلان'),
    ]
    
    PRIORITY_CHOICES = [
        ('low', 'منخفض'),
        ('medium', 'متوسط'),
        ('high', 'عالي'),
        ('urgent', 'عاجل'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='العنوان')
    message = models.TextField(verbose_name='الرسالة')
    notification_type = models.CharField(
        max_length=15, 
        choices=NOTIFICATION_TYPE_CHOICES,
        verbose_name='نوع الإشعار'
    )
    priority = models.CharField(
        max_length=10, 
        choices=PRIORITY_CHOICES,
        default='medium',
        verbose_name='الأولوية'
    )
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='sent_notifications',
        verbose_name='المرسل'
    )
    recipients = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='received_notifications',
        verbose_name='المستقبلون'
    )
    is_scheduled = models.BooleanField(default=False, verbose_name='مجدول')
    scheduled_date = models.DateTimeField(
        null=True, 
        blank=True,
        verbose_name='تاريخ الإرسال المجدول'
    )
    is_sent = models.BooleanField(default=False, verbose_name='تم الإرسال')
    sent_date = models.DateTimeField(
        null=True, 
        blank=True,
        verbose_name='تاريخ الإرسال'
    )
    is_read = models.BooleanField(default=False, verbose_name='تم القراءة')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    class Meta:
        verbose_name = 'إشعار'
        verbose_name_plural = 'الإشعارات'

    def __str__(self):
        return f"{self.title} - {self.get_priority_display()}"


class NotificationTemplate(models.Model):
    """
    Notification Template model for reusable notification formats
    """
    name = models.CharField(max_length=100, verbose_name='اسم القالب')
    title_template = models.CharField(max_length=200, verbose_name='قالب العنوان')
    message_template = models.TextField(verbose_name='قالب الرسالة')
    notification_type = models.CharField(
        max_length=15, 
        choices=Notification.NOTIFICATION_TYPE_CHOICES,
        verbose_name='نوع الإشعار'
    )
    is_active = models.BooleanField(default=True, verbose_name='نشط')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    class Meta:
        verbose_name = 'قالب إشعار'
        verbose_name_plural = 'قوالب الإشعارات'

    def __str__(self):
        return self.name


class NotificationLog(models.Model):
    """
    Notification Log model for tracking notification delivery
    """
    notification = models.ForeignKey(
        Notification, 
        on_delete=models.CASCADE,
        verbose_name='الإشعار'
    )
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        verbose_name='المستقبل'
    )
    delivery_status = models.CharField(
        max_length=20,
        choices=[
            ('sent', 'تم الإرسال'),
            ('delivered', 'تم التسليم'),
            ('read', 'تم القراءة'),
            ('failed', 'فشل الإرسال'),
        ],
        verbose_name='حالة التسليم'
    )
    delivery_date = models.DateTimeField(
        null=True, 
        blank=True,
        verbose_name='تاريخ التسليم'
    )
    read_date = models.DateTimeField(
        null=True, 
        blank=True,
        verbose_name='تاريخ القراءة'
    )
    error_message = models.TextField(
        blank=True,
        verbose_name='رسالة الخطأ'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')

    class Meta:
        verbose_name = 'سجل الإشعار'
        verbose_name_plural = 'سجلات الإشعارات'
        unique_together = ['notification', 'recipient']

    def __str__(self):
        return f"{self.notification.title} - {self.recipient} - {self.delivery_status}"