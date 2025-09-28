from django import forms
from .models import Subject, Class, TeacherSubject
from teachers.models import Teacher


class SubjectForm(forms.ModelForm):
    """
    Subject form
    """
    class Meta:
        model = Subject
        fields = ['name', 'name_en', 'code', 'description', 'level', 'grade', 'subject_type', 'credit_hours', 'objectives', 'assessment_method', 'textbook', 'reference_books', 'prerequisites', 'is_active']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Arabic labels and CSS classes
        self.fields['name'].label = 'اسم المادة'
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['name_en'].label = 'اسم المادة (إنجليزي)'
        self.fields['name_en'].widget.attrs.update({'class': 'form-control'})
        self.fields['code'].label = 'رمز المادة'
        self.fields['code'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].label = 'وصف المادة'
        self.fields['description'].widget = forms.Textarea(attrs={'rows': 3, 'class': 'form-control'})
        self.fields['level'].label = 'المرحلة'
        self.fields['level'].widget.attrs.update({'class': 'form-select'})
        self.fields['grade'].label = 'الصف'
        self.fields['grade'].widget.attrs.update({'class': 'form-select'})
        self.fields['subject_type'].label = 'نوع المادة'
        self.fields['subject_type'].widget.attrs.update({'class': 'form-select'})
        self.fields['credit_hours'].label = 'عدد الساعات'
        self.fields['credit_hours'].widget.attrs.update({'class': 'form-control'})
        self.fields['objectives'].label = 'أهداف المادة'
        self.fields['objectives'].widget = forms.Textarea(attrs={'rows': 3, 'class': 'form-control'})
        self.fields['assessment_method'].label = 'طريقة التقييم'
        self.fields['assessment_method'].widget = forms.Textarea(attrs={'rows': 3, 'class': 'form-control'})
        self.fields['textbook'].label = 'الكتاب المقرر'
        self.fields['textbook'].widget.attrs.update({'class': 'form-control'})
        self.fields['reference_books'].label = 'المراجع'
        self.fields['reference_books'].widget = forms.Textarea(attrs={'rows': 3, 'class': 'form-control'})
        self.fields['prerequisites'].label = 'المتطلبات السابقة'
        self.fields['prerequisites'].widget.attrs.update({'class': 'form-select'})
        self.fields['is_active'].label = 'المادة نشطة'
        self.fields['is_active'].widget.attrs.update({'class': 'form-check-input'})


class ClassForm(forms.ModelForm):
    """
    Class form
    """
    class Meta:
        model = Class
        fields = ['name', 'level', 'grade', 'section', 'capacity', 'location', 'class_teacher', 'is_active']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Arabic labels and CSS classes
        self.fields['name'].label = 'اسم الفصل'
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['level'].label = 'المرحلة'
        self.fields['level'].widget.attrs.update({'class': 'form-select'})
        self.fields['grade'].label = 'الصف'
        self.fields['grade'].widget.attrs.update({'class': 'form-select'})
        self.fields['section'].label = 'القسم'
        self.fields['section'].widget.attrs.update({'class': 'form-control'})
        self.fields['capacity'].label = 'السعة'
        self.fields['capacity'].widget.attrs.update({'class': 'form-control'})
        self.fields['location'].label = 'الموقع'
        self.fields['location'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_teacher'].label = 'معلم الفصل'
        self.fields['class_teacher'].widget.attrs.update({'class': 'form-select'})
        self.fields['is_active'].label = 'الصف نشط'
        self.fields['is_active'].widget.attrs.update({'class': 'form-check-input'})
        
        # Make class_teacher optional
        self.fields['class_teacher'].required = False


class TeacherSubjectForm(forms.ModelForm):
    """
    Teacher-Subject assignment form
    """
    class Meta:
        model = TeacherSubject
        fields = ['teacher', 'subject', 'is_primary']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Arabic labels and CSS classes
        self.fields['teacher'].label = 'المعلم'
        self.fields['teacher'].widget.attrs.update({'class': 'form-select'})
        self.fields['subject'].label = 'المادة'
        self.fields['subject'].widget.attrs.update({'class': 'form-select'})
        self.fields['is_primary'].label = 'معلم أساسي'
        self.fields['is_primary'].widget.attrs.update({'class': 'form-check-input'})
        
        # Filter active teachers only
        self.fields['teacher'].queryset = Teacher.objects.filter(is_active=True)
        
        # Make subject field optional when assigning from subject detail
        self.fields['subject'].required = False
