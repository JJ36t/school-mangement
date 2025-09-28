from django.contrib import admin
from .models import Student, Parent, StudentParent


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """
    Student Admin
    """
    list_display = ('user', 'student_id', 'grade', 'section', 'gender', 'enrollment_date', 'is_active')
    list_filter = ('grade', 'section', 'gender', 'is_active', 'enrollment_date')
    search_fields = ('user__first_name', 'user__last_name', 'student_id')
    ordering = ('-enrollment_date',)
    
    fieldsets = (
        ('معلومات المستخدم', {'fields': ('user',)}),
        ('معلومات الطالب', {'fields': ('student_id', 'grade', 'section', 'gender', 'enrollment_date', 'is_active')}),
    )


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    """
    Parent Admin
    """
    list_display = ('user', 'relationship', 'occupation', 'workplace', 'emergency_contact')
    list_filter = ('relationship', 'occupation')
    search_fields = ('user__first_name', 'user__last_name', 'occupation')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('معلومات المستخدم', {'fields': ('user',)}),
        ('معلومات ولي الأمر', {'fields': ('relationship', 'occupation', 'workplace', 'emergency_contact')}),
    )


@admin.register(StudentParent)
class StudentParentAdmin(admin.ModelAdmin):
    """
    Student-Parent Relationship Admin
    """
    list_display = ('student', 'parent', 'is_primary', 'created_at')
    list_filter = ('is_primary', 'created_at')
    search_fields = ('student__user__first_name', 'student__user__last_name', 'parent__user__first_name', 'parent__user__last_name')
    ordering = ('-created_at',)