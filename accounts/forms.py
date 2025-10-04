from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from .models import User


class UserRegistrationForm(UserCreationForm):
    """
    User registration form
    """
    email = forms.EmailField(required=True, label='البريد الإلكتروني')
    first_name = forms.CharField(max_length=30, required=True, label='الاسم الأول')
    last_name = forms.CharField(max_length=30, required=True, label='الاسم الأخير')
    phone = forms.CharField(max_length=15, required=False, label='رقم الهاتف')
    role = forms.ChoiceField(choices=User.ROLE_CHOICES, label='الدور')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'phone', 'role', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Arabic labels
        self.fields['username'].label = 'اسم المستخدم'
        self.fields['password1'].label = 'كلمة المرور'
        self.fields['password2'].label = 'تأكيد كلمة المرور'
        
        # Add help text
        self.fields['username'].help_text = 'مطلوب. 150 حرف أو أقل. أحرف وأرقام و @/./+/-/_ فقط.'
        self.fields['password1'].help_text = 'يجب أن تحتوي كلمة المرور على 8 أحرف على الأقل.'
        self.fields['password2'].help_text = 'أدخل نفس كلمة المرور للتأكيد.'


class UserEditForm(forms.ModelForm):
    """
    User edit form
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'address', 'date_of_birth', 'profile_picture')
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Arabic labels
        self.fields['first_name'].label = 'الاسم الأول'
        self.fields['last_name'].label = 'الاسم الأخير'
        self.fields['email'].label = 'البريد الإلكتروني'
        self.fields['phone'].label = 'رقم الهاتف'
        self.fields['address'].label = 'العنوان'
        self.fields['date_of_birth'].label = 'تاريخ الميلاد'
        self.fields['profile_picture'].label = 'صورة الملف الشخصي'


class CustomPasswordChangeForm(PasswordChangeForm):
    """
    Custom password change form with Arabic labels
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Arabic labels
        self.fields['old_password'].label = 'كلمة المرور الحالية'
        self.fields['new_password1'].label = 'كلمة المرور الجديدة'
        self.fields['new_password2'].label = 'تأكيد كلمة المرور الجديدة'
