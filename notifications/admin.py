from django.contrib import admin
from .models import Notification, NotificationTemplate, NotificationLog


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """
    Notification Admin
    """
    list_display = ('title', 'notification_type', 'priority', 'sender', 'is_sent', 'is_read', 'created_at')
    list_filter = ('notification_type', 'priority', 'is_sent', 'is_read', 'created_at')
    search_fields = ('title', 'message', 'sender__first_name', 'sender__last_name')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('معلومات الإشعار', {'fields': ('title', 'message', 'notification_type', 'priority', 'sender', 'recipients')}),
        ('جدولة الإرسال', {'fields': ('is_scheduled', 'scheduled_date')}),
        ('حالة الإرسال', {'fields': ('is_sent', 'sent_date', 'is_read')}),
    )
    
    filter_horizontal = ('recipients',)


@admin.register(NotificationTemplate)
class NotificationTemplateAdmin(admin.ModelAdmin):
    """
    Notification Template Admin
    """
    list_display = ('name', 'notification_type', 'is_active', 'created_at')
    list_filter = ('notification_type', 'is_active', 'created_at')
    search_fields = ('name', 'title_template', 'message_template')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('معلومات القالب', {'fields': ('name', 'notification_type', 'is_active')}),
        ('محتوى القالب', {'fields': ('title_template', 'message_template')}),
    )


@admin.register(NotificationLog)
class NotificationLogAdmin(admin.ModelAdmin):
    """
    Notification Log Admin
    """
    list_display = ('notification', 'recipient', 'delivery_status', 'delivery_date', 'read_date')
    list_filter = ('delivery_status', 'delivery_date', 'read_date')
    search_fields = ('notification__title', 'recipient__first_name', 'recipient__last_name')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('معلومات التسليم', {'fields': ('notification', 'recipient', 'delivery_status', 'delivery_date', 'read_date')}),
        ('تفاصيل الخطأ', {'fields': ('error_message',)}),
    )
    
    readonly_fields = ('created_at',)