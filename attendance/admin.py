from django.contrib import admin
from .models import Attendance, AttendanceSummary


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    """
    Attendance Admin
    """
    list_display = ('student', 'subject', 'date', 'status', 'teacher')
    list_filter = ('status', 'date', 'subject__grade')
    search_fields = ('student__user__first_name', 'student__user__last_name', 'subject__name')
    ordering = ('-date',)
    
    fieldsets = (
        ('معلومات الحضور', {'fields': ('student', 'subject', 'teacher', 'date', 'status', 'remarks')}),
    )


@admin.register(AttendanceSummary)
class AttendanceSummaryAdmin(admin.ModelAdmin):
    """
    Attendance Summary Admin
    """
    list_display = ('student', 'subject', 'month', 'year', 'attendance_percentage', 'present_days', 'total_days')
    list_filter = ('month', 'year', 'subject__grade')
    search_fields = ('student__user__first_name', 'student__user__last_name', 'subject__name')
    ordering = ('-year', '-month')
    
    fieldsets = (
        ('معلومات الملخص', {'fields': ('student', 'subject', 'month', 'year', 'total_days', 'present_days', 'absent_days', 'late_days', 'excused_days', 'attendance_percentage')}),
    )
    
    readonly_fields = ('attendance_percentage',)