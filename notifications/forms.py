from django import forms
from django.contrib.auth import get_user_model
from .models import Notification, NotificationTemplate

User = get_user_model()


class NotificationForm(forms.ModelForm):
    """
    Notification form
    """
    class Meta:
        model = Notification
        fields = ['title', 'message', 'notification_type', 'priority', 'recipients', 'is_scheduled', 'scheduled_date']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
            'scheduled_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Arabic labels and CSS classes
        self.fields['title'].label = 'عنوان الإشعار'
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['message'].label = 'نص الإشعار'
        self.fields['message'].widget.attrs.update({'class': 'form-control'})
        self.fields['notification_type'].label = 'نوع الإشعار'
        self.fields['notification_type'].widget.attrs.update({'class': 'form-select'})
        self.fields['priority'].label = 'الأولوية'
        self.fields['priority'].widget.attrs.update({'class': 'form-select'})
        self.fields['recipients'].label = 'المستقبلون'
        self.fields['recipients'].widget.attrs.update({'class': 'form-select'})
        self.fields['is_scheduled'].label = 'مجدول'
        self.fields['is_scheduled'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['scheduled_date'].label = 'تاريخ الإرسال المجدول'
        self.fields['scheduled_date'].widget.attrs.update({'class': 'form-control'})
        
        # Make some fields optional
        self.fields['scheduled_date'].required = False


class NotificationTemplateForm(forms.ModelForm):
    """
    Notification template form
    """
    class Meta:
        model = NotificationTemplate
        fields = ['name', 'title_template', 'message_template', 'notification_type']
        widgets = {
            'title_template': forms.TextInput(attrs={'placeholder': 'مثال: إشعار جديد لـ {student_name}'}),
            'message_template': forms.Textarea(attrs={'rows': 5, 'placeholder': 'مثال: مرحباً {student_name}، لديك {notification_type} جديد.'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Arabic labels and CSS classes
        self.fields['name'].label = 'اسم القالب'
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['title_template'].label = 'قالب العنوان'
        self.fields['title_template'].widget.attrs.update({'class': 'form-control'})
        self.fields['message_template'].label = 'قالب الرسالة'
        self.fields['message_template'].widget.attrs.update({'class': 'form-control'})
        self.fields['notification_type'].label = 'نوع الإشعار'
        self.fields['notification_type'].widget.attrs.update({'class': 'form-select'})
