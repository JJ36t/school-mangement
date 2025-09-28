from django.db import models
from django.conf import settings


class Student(models.Model):
    """
    Student model for School Management System
    """
    GENDER_CHOICES = [
        ('male', 'ذكر'),
        ('female', 'أنثى'),
    ]
    
    GRADE_CHOICES = [
        ('1', 'الصف الأول'),
        ('2', 'الصف الثاني'),
        ('3', 'الصف الثالث'),
        ('4', 'الصف الرابع'),
        ('5', 'الصف الخامس'),
        ('6', 'الصف السادس'),
        ('7', 'الصف السابع'),
        ('8', 'الصف الثامن'),
        ('9', 'الصف التاسع'),
        ('10', 'الصف العاشر'),
        ('11', 'الصف الحادي عشر'),
        ('12', 'الصف الثاني عشر'),
    ]
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        verbose_name='المستخدم'
    )
    student_id = models.CharField(
        max_length=20, 
        unique=True,
        verbose_name='رقم الطالب'
    )
    grade = models.CharField(
        max_length=2, 
        choices=GRADE_CHOICES,
        verbose_name='الصف'
    )
    section = models.CharField(max_length=10, verbose_name='الفصل')
    gender = models.CharField(
        max_length=6, 
        choices=GENDER_CHOICES,
        verbose_name='الجنس'
    )
    enrollment_date = models.DateField(verbose_name='تاريخ التسجيل')
    is_active = models.BooleanField(default=True, verbose_name='نشط')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    class Meta:
        verbose_name = 'طالب'
        verbose_name_plural = 'الطلاب'

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.get_grade_display()}"


class Parent(models.Model):
    """
    Parent model for School Management System
    """
    RELATIONSHIP_CHOICES = [
        ('father', 'أب'),
        ('mother', 'أم'),
        ('guardian', 'وصي'),
    ]
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        verbose_name='المستخدم'
    )
    relationship = models.CharField(
        max_length=10, 
        choices=RELATIONSHIP_CHOICES,
        verbose_name='صلة القرابة'
    )
    occupation = models.CharField(max_length=100, blank=True, verbose_name='المهنة')
    workplace = models.CharField(max_length=100, blank=True, verbose_name='مكان العمل')
    emergency_contact = models.CharField(max_length=15, verbose_name='رقم الطوارئ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    class Meta:
        verbose_name = 'ولي أمر'
        verbose_name_plural = 'أولياء الأمور'

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.get_relationship_display()})"


class StudentParent(models.Model):
    """
    Relationship between Student and Parent
    """
    student = models.ForeignKey(
        Student, 
        on_delete=models.CASCADE,
        verbose_name='الطالب'
    )
    parent = models.ForeignKey(
        Parent, 
        on_delete=models.CASCADE,
        verbose_name='ولي الأمر'
    )
    is_primary = models.BooleanField(default=False, verbose_name='ولي أمر أساسي')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')

    class Meta:
        verbose_name = 'علاقة طالب - ولي أمر'
        verbose_name_plural = 'علاقات الطلاب - أولياء الأمور'
        unique_together = ['student', 'parent']

    def __str__(self):
        return f"{self.student} - {self.parent}"