from django import forms
from django.contrib.auth import get_user_model
from .models import Teacher

User = get_user_model()


class TeacherForm(forms.ModelForm):
    """
    Teacher form
    """
    # User fields
    username = forms.CharField(max_length=150, label='اسم المستخدم')
    email = forms.EmailField(label='البريد الإلكتروني')
    first_name = forms.CharField(max_length=30, label='الاسم الأول')
    last_name = forms.CharField(max_length=30, label='الاسم الأخير')
    phone = forms.CharField(max_length=15, required=False, label='رقم الهاتف')
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False, label='العنوان')
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='تاريخ الميلاد')
    
    class Meta:
        model = Teacher
        fields = ['teacher_id', 'gender', 'qualification', 'specialization', 'experience_years', 'hire_date', 'salary']
        widgets = {
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Arabic labels and CSS classes
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control'})
        self.fields['date_of_birth'].widget.attrs.update({'class': 'form-control'})
        
        self.fields['teacher_id'].label = 'رقم المعلم'
        self.fields['teacher_id'].widget.attrs.update({'class': 'form-control'})
        self.fields['gender'].label = 'الجنس'
        self.fields['gender'].widget.attrs.update({'class': 'form-select'})
        self.fields['qualification'].label = 'المؤهل العلمي'
        self.fields['qualification'].widget.attrs.update({'class': 'form-select'})
        self.fields['specialization'].label = 'التخصص'
        self.fields['specialization'].widget.attrs.update({'class': 'form-control'})
        self.fields['experience_years'].label = 'سنوات الخبرة'
        self.fields['experience_years'].widget.attrs.update({'class': 'form-control'})
        self.fields['hire_date'].label = 'تاريخ التعيين'
        self.fields['hire_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['salary'].label = 'الراتب'
        self.fields['salary'].widget.attrs.update({'class': 'form-control'})
        
        # If editing existing teacher, populate user fields
        if self.instance and self.instance.pk:
            user = self.instance.user
            self.fields['username'].initial = user.username
            self.fields['email'].initial = user.email
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['phone'].initial = user.phone
            self.fields['address'].initial = user.address
            self.fields['date_of_birth'].initial = user.date_of_birth
    
    def save(self, commit=True):
        teacher = super().save(commit=False)
        
        if not teacher.pk:  # Creating new teacher
            # Create user
            user = User.objects.create_user(
                username=self.cleaned_data['username'],
                email=self.cleaned_data['email'],
                password='default_password',  # Will be changed later
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                phone=self.cleaned_data['phone'],
                address=self.cleaned_data['address'],
                date_of_birth=self.cleaned_data['date_of_birth'],
                role='teacher'
            )
            teacher.user = user
        else:  # Updating existing teacher
            user = teacher.user
            user.username = self.cleaned_data['username']
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.phone = self.cleaned_data['phone']
            user.address = self.cleaned_data['address']
            user.date_of_birth = self.cleaned_data['date_of_birth']
            user.save()
        
        if commit:
            teacher.save()
        
        return teacher
