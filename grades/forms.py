from django import forms
from .models import Grade, GradeSummary


class GradeForm(forms.ModelForm):
    """
    Grade form
    """
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'teacher', 'exam_type', 'marks_obtained', 'total_marks', 'exam_date', 'remarks']
        widgets = {
            'exam_date': forms.DateInput(attrs={'type': 'date'}),
            'remarks': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Arabic labels and CSS classes
        self.fields['student'].label = 'الطالب'
        self.fields['student'].widget.attrs.update({'class': 'form-select'})
        self.fields['subject'].label = 'المادة'
        self.fields['subject'].widget.attrs.update({'class': 'form-select'})
        self.fields['teacher'].label = 'المعلم'
        self.fields['teacher'].widget.attrs.update({'class': 'form-select'})
        self.fields['exam_type'].label = 'نوع الامتحان'
        self.fields['exam_type'].widget.attrs.update({'class': 'form-select'})
        self.fields['marks_obtained'].label = 'الدرجة المحققة'
        self.fields['marks_obtained'].widget.attrs.update({'class': 'form-control'})
        self.fields['total_marks'].label = 'الدرجة الكاملة'
        self.fields['total_marks'].widget.attrs.update({'class': 'form-control'})
        self.fields['exam_date'].label = 'تاريخ الامتحان'
        self.fields['exam_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['remarks'].label = 'ملاحظات'
        self.fields['remarks'].widget.attrs.update({'class': 'form-control'})


class GradeSummaryForm(forms.ModelForm):
    """
    Grade summary form
    """
    class Meta:
        model = GradeSummary
        fields = ['student', 'subject', 'semester', 'midterm_marks', 'final_marks', 'practical_marks']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Arabic labels and CSS classes
        self.fields['student'].label = 'الطالب'
        self.fields['student'].widget.attrs.update({'class': 'form-select'})
        self.fields['subject'].label = 'المادة'
        self.fields['subject'].widget.attrs.update({'class': 'form-select'})
        self.fields['semester'].label = 'الفصل الدراسي'
        self.fields['semester'].widget.attrs.update({'class': 'form-control'})
        self.fields['midterm_marks'].label = 'درجة منتصف الفصل'
        self.fields['midterm_marks'].widget.attrs.update({'class': 'form-control'})
        self.fields['final_marks'].label = 'درجة النهائي'
        self.fields['final_marks'].widget.attrs.update({'class': 'form-control'})
        self.fields['practical_marks'].label = 'درجة العملي'
        self.fields['practical_marks'].widget.attrs.update({'class': 'form-control'})
