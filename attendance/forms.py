from django import forms
from .models import Attendance, AttendanceSummary


class AttendanceForm(forms.ModelForm):
    """
    Attendance form
    """
    class Meta:
        model = Attendance
        fields = ['student', 'subject', 'teacher', 'date', 'status', 'check_in_time', 'check_out_time', 'attendance_type', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'check_in_time': forms.TimeInput(attrs={'type': 'time'}),
            'check_out_time': forms.TimeInput(attrs={'type': 'time'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
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
        self.fields['date'].label = 'التاريخ'
        self.fields['date'].widget.attrs.update({'class': 'form-control'})
        self.fields['status'].label = 'حالة الحضور'
        self.fields['status'].widget.attrs.update({'class': 'form-select'})
        self.fields['check_in_time'].label = 'وقت الحضور'
        self.fields['check_in_time'].widget.attrs.update({'class': 'form-control'})
        self.fields['check_out_time'].label = 'وقت الانصراف'
        self.fields['check_out_time'].widget.attrs.update({'class': 'form-control'})
        self.fields['attendance_type'].label = 'نوع الحضور'
        self.fields['attendance_type'].widget.attrs.update({'class': 'form-select'})
        self.fields['notes'].label = 'ملاحظات'
        self.fields['notes'].widget.attrs.update({'class': 'form-control'})


class AttendanceSummaryForm(forms.ModelForm):
    """
    Attendance summary form
    """
    class Meta:
        model = AttendanceSummary
        fields = ['student', 'subject', 'month', 'year', 'total_days', 'present_days', 'absent_days', 'late_days', 'excused_days']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Arabic labels and CSS classes
        self.fields['student'].label = 'الطالب'
        self.fields['student'].widget.attrs.update({'class': 'form-select'})
        self.fields['subject'].label = 'المادة'
        self.fields['subject'].widget.attrs.update({'class': 'form-select'})
        self.fields['month'].label = 'الشهر'
        self.fields['month'].widget.attrs.update({'class': 'form-select'})
        self.fields['year'].label = 'السنة'
        self.fields['year'].widget.attrs.update({'class': 'form-control'})
        self.fields['total_days'].label = 'إجمالي الأيام'
        self.fields['total_days'].widget.attrs.update({'class': 'form-control'})
        self.fields['present_days'].label = 'أيام الحضور'
        self.fields['present_days'].widget.attrs.update({'class': 'form-control'})
        self.fields['absent_days'].label = 'أيام الغياب'
        self.fields['absent_days'].widget.attrs.update({'class': 'form-control'})
        self.fields['late_days'].label = 'أيام التأخير'
        self.fields['late_days'].widget.attrs.update({'class': 'form-control'})
        self.fields['excused_days'].label = 'أيام الغياب بعذر'
        self.fields['excused_days'].widget.attrs.update({'class': 'form-control'})
