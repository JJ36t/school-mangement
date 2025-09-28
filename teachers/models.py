from django.db import models
from django.conf import settings


class Teacher(models.Model):
    """
    Teacher model for School Management System
    """
    GENDER_CHOICES = [
        ('male', 'ذكر'),
        ('female', 'أنثى'),
    ]
    
    QUALIFICATION_CHOICES = [
        ('bachelor', 'بكالوريوس'),
        ('master', 'ماجستير'),
        ('phd', 'دكتوراه'),
        ('diploma', 'دبلوم'),
    ]
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        verbose_name='المستخدم'
    )
    teacher_id = models.CharField(
        max_length=20, 
        unique=True,
        verbose_name='رقم المعلم'
    )
    gender = models.CharField(
        max_length=6, 
        choices=GENDER_CHOICES,
        verbose_name='الجنس'
    )
    qualification = models.CharField(
        max_length=10, 
        choices=QUALIFICATION_CHOICES,
        verbose_name='المؤهل العلمي'
    )
    specialization = models.CharField(max_length=100, verbose_name='التخصص')
    experience_years = models.PositiveIntegerField(default=0, verbose_name='سنوات الخبرة')
    hire_date = models.DateField(verbose_name='تاريخ التعيين')
    salary = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True,
        verbose_name='الراتب'
    )
    is_active = models.BooleanField(default=True, verbose_name='نشط')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    class Meta:
        verbose_name = 'معلم'
        verbose_name_plural = 'المعلمون'

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.specialization}"