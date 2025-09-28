from django.db import models
from django.conf import settings


class Subject(models.Model):
    """
    Subject model for School Management System
    """
    LEVEL_CHOICES = [
        ('elementary', 'ابتدائي'),
        ('middle', 'متوسط'),
        ('high', 'ثانوي'),
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
    
    SUBJECT_TYPE_CHOICES = [
        ('core', 'مادة أساسية'),
        ('elective', 'مادة اختيارية'),
        ('activity', 'نشاط'),
    ]
    
    name = models.CharField(max_length=100, verbose_name='اسم المادة')
    name_en = models.CharField(max_length=100, blank=True, verbose_name='اسم المادة (إنجليزي)')
    code = models.CharField(max_length=10, unique=True, verbose_name='رمز المادة')
    description = models.TextField(blank=True, verbose_name='وصف المادة')
    level = models.CharField(
        max_length=10, 
        choices=LEVEL_CHOICES,
        default='elementary',
        verbose_name='المرحلة'
    )
    grade = models.CharField(
        max_length=2, 
        choices=GRADE_CHOICES,
        verbose_name='الصف'
    )
    subject_type = models.CharField(
        max_length=10, 
        choices=SUBJECT_TYPE_CHOICES,
        default='core',
        verbose_name='نوع المادة'
    )
    credit_hours = models.PositiveIntegerField(default=1, verbose_name='عدد الساعات')
    objectives = models.TextField(blank=True, verbose_name='أهداف المادة')
    assessment_method = models.TextField(blank=True, verbose_name='طريقة التقييم')
    textbook = models.CharField(max_length=200, blank=True, verbose_name='الكتاب المقرر')
    reference_books = models.TextField(blank=True, verbose_name='المراجع')
    prerequisites = models.ManyToManyField('self', blank=True, symmetrical=False, verbose_name='المتطلبات السابقة')
    is_active = models.BooleanField(default=True, verbose_name='نشط')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    class Meta:
        verbose_name = 'مادة'
        verbose_name_plural = 'المواد'
        unique_together = ['name', 'grade']

    def __str__(self):
        return f"{self.name} - {self.get_grade_display()}"


class TeacherSubject(models.Model):
    """
    Relationship between Teacher and Subject
    """
    teacher = models.ForeignKey(
        'teachers.Teacher', 
        on_delete=models.CASCADE,
        verbose_name='المعلم'
    )
    subject = models.ForeignKey(
        Subject, 
        on_delete=models.CASCADE,
        verbose_name='المادة'
    )
    is_primary = models.BooleanField(default=True, verbose_name='معلم أساسي')
    assigned_date = models.DateField(auto_now_add=True, verbose_name='تاريخ التعيين')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')

    class Meta:
        verbose_name = 'تعيين معلم - مادة'
        verbose_name_plural = 'تعيينات المعلمين - المواد'
        unique_together = ['teacher', 'subject']

    def __str__(self):
        return f"{self.teacher} - {self.subject}"


class Class(models.Model):
    """
    Class model for School Management System
    """
    LEVEL_CHOICES = [
        ('elementary', 'ابتدائي'),
        ('middle', 'متوسط'),
        ('high', 'ثانوي'),
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
    
    name = models.CharField(max_length=50, verbose_name='اسم الفصل')
    level = models.CharField(
        max_length=10, 
        choices=LEVEL_CHOICES,
        default='elementary',
        verbose_name='المرحلة'
    )
    grade = models.CharField(
        max_length=2, 
        choices=GRADE_CHOICES,
        verbose_name='الصف'
    )
    section = models.CharField(max_length=10, verbose_name='القسم')
    capacity = models.PositiveIntegerField(default=30, verbose_name='السعة')
    location = models.CharField(max_length=100, blank=True, verbose_name='الموقع')
    class_teacher = models.ForeignKey(
        'teachers.Teacher', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        verbose_name='معلم الفصل'
    )
    is_active = models.BooleanField(default=True, verbose_name='نشط')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    class Meta:
        verbose_name = 'فصل'
        verbose_name_plural = 'الفصول'
        unique_together = ['grade', 'section']

    def __str__(self):
        return f"{self.get_grade_display()} - {self.section}"