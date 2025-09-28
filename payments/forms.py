from django import forms
from .models import Payment, PaymentSummary


class PaymentForm(forms.ModelForm):
    """
    Payment form
    """
    class Meta:
        model = Payment
        fields = ['student', 'payment_type', 'amount', 'due_date', 'paid_date', 'payment_method', 'status', 'notes']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'paid_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Arabic labels and CSS classes
        self.fields['student'].label = 'الطالب'
        self.fields['student'].widget.attrs.update({'class': 'form-select'})
        self.fields['payment_type'].label = 'نوع الدفعة'
        self.fields['payment_type'].widget.attrs.update({'class': 'form-select'})
        self.fields['amount'].label = 'المبلغ'
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})
        self.fields['due_date'].label = 'تاريخ الاستحقاق'
        self.fields['due_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['paid_date'].label = 'تاريخ الدفع'
        self.fields['paid_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['payment_method'].label = 'طريقة الدفع'
        self.fields['payment_method'].widget.attrs.update({'class': 'form-select'})
        self.fields['status'].label = 'حالة الدفع'
        self.fields['status'].widget.attrs.update({'class': 'form-select'})
        self.fields['notes'].label = 'ملاحظات'
        self.fields['notes'].widget.attrs.update({'class': 'form-control'})
        
        # Make some fields optional
        self.fields['paid_date'].required = False
        self.fields['payment_method'].required = False
        self.fields['notes'].required = False


class PaymentSummaryForm(forms.ModelForm):
    """
    Payment summary form
    """
    class Meta:
        model = PaymentSummary
        fields = ['student', 'academic_year', 'total_due', 'total_paid', 'total_pending', 'total_overdue']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Arabic labels and CSS classes
        self.fields['student'].label = 'الطالب'
        self.fields['student'].widget.attrs.update({'class': 'form-select'})
        self.fields['academic_year'].label = 'السنة الدراسية'
        self.fields['academic_year'].widget.attrs.update({'class': 'form-control'})
        self.fields['total_due'].label = 'إجمالي المستحق'
        self.fields['total_due'].widget.attrs.update({'class': 'form-control'})
        self.fields['total_paid'].label = 'إجمالي المدفوع'
        self.fields['total_paid'].widget.attrs.update({'class': 'form-control'})
        self.fields['total_pending'].label = 'إجمالي المعلق'
        self.fields['total_pending'].widget.attrs.update({'class': 'form-control'})
        self.fields['total_overdue'].label = 'إجمالي المتأخر'
        self.fields['total_overdue'].widget.attrs.update({'class': 'form-control'})
