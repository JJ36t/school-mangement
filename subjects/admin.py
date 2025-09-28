from django.contrib import admin
from .models import Subject, Class, TeacherSubject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    """
    Subject Admin
    """
    list_display = ('name', 'code', 'grade', 'subject_type', 'credit_hours', 'is_active')
    list_filter = ('grade', 'subject_type', 'is_active')
    search_fields = ('name', 'code', 'description')
    ordering = ('grade', 'name')
    
    fieldsets = (
        ('معلومات المادة', {'fields': ('name', 'code', 'description', 'grade', 'subject_type', 'credit_hours', 'is_active')}),
    )


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    """
    Class Admin
    """
    list_display = ('name', 'grade', 'section', 'capacity', 'class_teacher', 'is_active')
    list_filter = ('grade', 'is_active')
    search_fields = ('name', 'section')
    ordering = ('grade', 'section')
    
    fieldsets = (
        ('معلومات الفصل', {'fields': ('name', 'grade', 'section', 'capacity', 'class_teacher', 'is_active')}),
    )


@admin.register(TeacherSubject)
class TeacherSubjectAdmin(admin.ModelAdmin):
    """
    Teacher-Subject Assignment Admin
    """
    list_display = ('teacher', 'subject', 'is_primary', 'assigned_date')
    list_filter = ('is_primary', 'assigned_date')
    search_fields = ('teacher__user__first_name', 'teacher__user__last_name', 'subject__name')
    ordering = ('-assigned_date',)