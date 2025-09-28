from django.contrib import admin
from .models import Grade, GradeSummary


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    """
    Grade Admin
    """
    list_display = ('student', 'subject', 'exam_type', 'marks_obtained', 'total_marks', 'exam_date', 'grade_letter')
    list_filter = ('exam_type', 'exam_date', 'subject__grade')
    search_fields = ('student__user__first_name', 'student__user__last_name', 'subject__name')
    ordering = ('-exam_date',)
    
    fieldsets = (
        ('معلومات الدرجة', {'fields': ('student', 'subject', 'teacher', 'exam_type', 'marks_obtained', 'total_marks', 'exam_date', 'remarks')}),
    )
    
    readonly_fields = ('grade_letter',)


@admin.register(GradeSummary)
class GradeSummaryAdmin(admin.ModelAdmin):
    """
    Grade Summary Admin
    """
    list_display = ('student', 'subject', 'semester', 'total_marks', 'percentage', 'grade_letter')
    list_filter = ('semester', 'subject__grade')
    search_fields = ('student__user__first_name', 'student__user__last_name', 'subject__name')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('معلومات الملخص', {'fields': ('student', 'subject', 'semester', 'midterm_marks', 'final_marks', 'practical_marks', 'total_marks', 'percentage', 'grade_letter')}),
    )
    
    readonly_fields = ('total_marks', 'percentage', 'grade_letter')