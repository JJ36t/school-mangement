from django.db import models
from django.conf import settings


class Grade(models.Model):
    """
    Grade model for School Management System
    """
    EXAM_TYPE_CHOICES = [
        ('midterm', 'امتحان منتصف الفصل'),
        ('final', 'امتحان نهائي'),
        ('practical', 'عملي'),
        ('quiz', 'اختبار قصير'),
        ('assignment', 'واجب'),
    ]
    
    student = models.ForeignKey(
        'students.Student', 
        on_delete=models.CASCADE,
        related_name='student_grades',
        verbose_name='الطالب'
    )
    subject = models.ForeignKey(
        'subjects.Subject', 
        on_delete=models.CASCADE,
        related_name='subject_grades',
        verbose_name='المادة'
    )
    teacher = models.ForeignKey(
        'teachers.Teacher', 
        on_delete=models.CASCADE,
        related_name='teacher_grades',
        verbose_name='المعلم'
    )
    exam_type = models.CharField(
        max_length=10, 
        choices=EXAM_TYPE_CHOICES,
        verbose_name='نوع الامتحان'
    )
    marks_obtained = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        verbose_name='الدرجة المحصلة'
    )
    total_marks = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        verbose_name='الدرجة الكلية'
    )
    exam_date = models.DateField(verbose_name='تاريخ الامتحان')
    remarks = models.TextField(blank=True, verbose_name='ملاحظات')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    class Meta:
        verbose_name = 'درجة'
        verbose_name_plural = 'الدرجات'
        unique_together = ['student', 'subject', 'exam_type', 'exam_date']

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.get_exam_type_display()}"

    @property
    def percentage(self):
        """Calculate percentage"""
        if self.total_marks > 0:
            return (self.marks_obtained / self.total_marks) * 100
        return 0

    @property
    def grade_letter(self):
        """Convert percentage to letter grade"""
        percentage = self.percentage
        if percentage >= 90:
            return 'A+'
        elif percentage >= 80:
            return 'A'
        elif percentage >= 70:
            return 'B+'
        elif percentage >= 60:
            return 'B'
        elif percentage >= 50:
            return 'C+'
        elif percentage >= 40:
            return 'C'
        else:
            return 'F'


class GradeSummary(models.Model):
    """
    Grade Summary model for calculating overall grades
    """
    student = models.ForeignKey(
        'students.Student', 
        on_delete=models.CASCADE,
        related_name='student_grade_summaries',
        verbose_name='الطالب'
    )
    subject = models.ForeignKey(
        'subjects.Subject', 
        on_delete=models.CASCADE,
        related_name='subject_grade_summaries',
        verbose_name='المادة'
    )
    semester = models.CharField(max_length=20, verbose_name='الفصل الدراسي')
    midterm_marks = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=0,
        verbose_name='درجة منتصف الفصل'
    )
    final_marks = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=0,
        verbose_name='درجة النهائي'
    )
    practical_marks = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=0,
        verbose_name='درجة العملي'
    )
    total_marks = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=0,
        verbose_name='المجموع الكلي'
    )
    percentage = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=0,
        verbose_name='النسبة المئوية'
    )
    grade_letter = models.CharField(max_length=2, default='F', verbose_name='الدرجة')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    class Meta:
        verbose_name = 'ملخص الدرجات'
        verbose_name_plural = 'ملخصات الدرجات'
        unique_together = ['student', 'subject', 'semester']

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.semester}"

    def calculate_total(self):
        """Calculate total marks"""
        self.total_marks = self.midterm_marks + self.final_marks + self.practical_marks
        return self.total_marks

    def calculate_percentage(self):
        """Calculate percentage based on total marks"""
        # Assuming total possible marks is 100
        total_possible = 100
        if total_possible > 0:
            self.percentage = (self.total_marks / total_possible) * 100
        return self.percentage

    def calculate_grade_letter(self):
        """Calculate grade letter based on percentage"""
        percentage = self.percentage
        if percentage >= 90:
            self.grade_letter = 'A+'
        elif percentage >= 80:
            self.grade_letter = 'A'
        elif percentage >= 70:
            self.grade_letter = 'B+'
        elif percentage >= 60:
            self.grade_letter = 'B'
        elif percentage >= 50:
            self.grade_letter = 'C+'
        elif percentage >= 40:
            self.grade_letter = 'C'
        else:
            self.grade_letter = 'F'
        return self.grade_letter