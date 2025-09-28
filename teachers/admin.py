from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """
    Teacher Admin
    """
    list_display = ('user', 'teacher_id', 'specialization', 'qualification', 'experience_years', 'hire_date', 'is_active')
    list_filter = ('qualification', 'specialization', 'is_active', 'hire_date')
    search_fields = ('user__first_name', 'user__last_name', 'teacher_id', 'specialization')
    ordering = ('-hire_date',)
    
    fieldsets = (
        ('معلومات المستخدم', {'fields': ('user',)}),
        ('معلومات المعلم', {'fields': ('teacher_id', 'gender', 'qualification', 'specialization', 'experience_years', 'hire_date', 'salary', 'is_active')}),
    )