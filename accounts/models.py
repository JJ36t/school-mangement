from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User model for School Management System
    """
    ROLE_CHOICES = [
        ('admin', 'مدير النظام'),
        ('teacher', 'معلم'),
        ('student', 'طالب'),
        ('parent', 'ولي أمر'),
    ]
    
    role = models.CharField(
        max_length=10, 
        choices=ROLE_CHOICES, 
        default='student',
        verbose_name='الدور'
    )
    phone = models.CharField(max_length=15, blank=True, verbose_name='رقم الهاتف')
    address = models.TextField(blank=True, verbose_name='العنوان')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='تاريخ الميلاد')
    profile_picture = models.ImageField(
        upload_to='profile_pictures/', 
        null=True, 
        blank=True,
        verbose_name='صورة الملف الشخصي'
    )
    is_active = models.BooleanField(default=True, verbose_name='نشط')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    class Meta:
        verbose_name = 'مستخدم'
        verbose_name_plural = 'المستخدمون'

    def __str__(self):
        return f"{self.get_full_name()} ({self.get_role_display()})"

    def get_role_display(self):
        return dict(self.ROLE_CHOICES)[self.role]