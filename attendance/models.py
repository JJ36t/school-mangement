from django.db import models
from django.conf import settings


class Attendance(models.Model):
    """
    Attendance model for School Management System
    """
    STATUS_CHOICES = [
        ('present', 'حاضر'),
        ('absent', 'غائب'),
        ('late', 'متأخر'),
        ('excused', 'غياب بعذر'),
    ]
    
    ATTENDANCE_TYPE_CHOICES = [
        ('regular', 'عادي'),
        ('exam', 'امتحان'),
        ('activity', 'نشاط'),
        ('field_trip', 'رحلة مدرسية'),
    ]
    
    student = models.ForeignKey(
        'students.Student', 
        on_delete=models.CASCADE,
        related_name='student_attendance',
        verbose_name='الطالب'
    )
    subject = models.ForeignKey(
        'subjects.Subject', 
        on_delete=models.CASCADE,
        related_name='subject_attendance',
        verbose_name='المادة'
    )
    teacher = models.ForeignKey(
        'teachers.Teacher', 
        on_delete=models.CASCADE,
        related_name='teacher_attendance',
        verbose_name='المعلم'
    )
    date = models.DateField(verbose_name='التاريخ')
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES,
        verbose_name='الحالة'
    )
    check_in_time = models.TimeField(null=True, blank=True, verbose_name='وقت الحضور')
    check_out_time = models.TimeField(null=True, blank=True, verbose_name='وقت الانصراف')
    attendance_type = models.CharField(
        max_length=15,
        choices=ATTENDANCE_TYPE_CHOICES,
        default='regular',
        verbose_name='نوع الحضور'
    )
    notes = models.TextField(blank=True, verbose_name='ملاحظات')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    class Meta:
        verbose_name = 'حضور'
        verbose_name_plural = 'الحضور والغياب'
        unique_together = ['student', 'subject', 'date']

    def __str__(self):
        return f"{self.student} - {self.date} - {self.get_status_display()}"
    
    @property
    def duration(self):
        """Calculate attendance duration"""
        if self.check_in_time and self.check_out_time:
            from datetime import datetime, timedelta
            check_in = datetime.combine(self.date, self.check_in_time)
            check_out = datetime.combine(self.date, self.check_out_time)
            duration = check_out - check_in
            hours = duration.seconds // 3600
            minutes = (duration.seconds % 3600) // 60
            return f"{hours}:{minutes:02d}"
        return None


class AttendanceSummary(models.Model):
    """
    Attendance Summary model for monthly/term reports
    """
    student = models.ForeignKey(
        'students.Student', 
        on_delete=models.CASCADE,
        related_name='student_attendance_summaries',
        verbose_name='الطالب'
    )
    subject = models.ForeignKey(
        'subjects.Subject', 
        on_delete=models.CASCADE,
        related_name='subject_attendance_summaries',
        verbose_name='المادة'
    )
    month = models.PositiveIntegerField(verbose_name='الشهر')
    year = models.PositiveIntegerField(verbose_name='السنة')
    total_days = models.PositiveIntegerField(default=0, verbose_name='إجمالي الأيام')
    present_days = models.PositiveIntegerField(default=0, verbose_name='أيام الحضور')
    absent_days = models.PositiveIntegerField(default=0, verbose_name='أيام الغياب')
    late_days = models.PositiveIntegerField(default=0, verbose_name='أيام التأخير')
    excused_days = models.PositiveIntegerField(default=0, verbose_name='أيام الغياب بعذر')
    attendance_percentage = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=0,
        verbose_name='نسبة الحضور'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    class Meta:
        verbose_name = 'ملخص الحضور'
        verbose_name_plural = 'ملخصات الحضور'
        unique_together = ['student', 'subject', 'month', 'year']

    def __str__(self):
        return f"{self.student} - {self.month}/{self.year} - {self.attendance_percentage}%"

    def calculate_attendance_percentage(self):
        """Calculate attendance percentage"""
        if self.total_days > 0:
            self.attendance_percentage = (self.present_days / self.total_days) * 100
        return self.attendance_percentage