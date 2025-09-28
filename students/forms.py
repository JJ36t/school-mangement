from django import forms
from django.contrib.auth import get_user_model
from .models import Student, Parent, StudentParent

User = get_user_model()


class StudentForm(forms.ModelForm):
    """
    Student form
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
        model = Student
        fields = ['student_id', 'grade', 'section', 'gender', 'enrollment_date']
        widgets = {
            'enrollment_date': forms.DateInput(attrs={'type': 'date'}),
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
        
        self.fields['student_id'].label = 'رقم الطالب'
        self.fields['student_id'].widget.attrs.update({'class': 'form-control'})
        self.fields['grade'].label = 'الصف'
        self.fields['grade'].widget.attrs.update({'class': 'form-select'})
        self.fields['section'].label = 'الفصل'
        self.fields['section'].widget.attrs.update({'class': 'form-control'})
        self.fields['gender'].label = 'الجنس'
        self.fields['gender'].widget.attrs.update({'class': 'form-select'})
        self.fields['enrollment_date'].label = 'تاريخ التسجيل'
        self.fields['enrollment_date'].widget.attrs.update({'class': 'form-control'})
        
        # If editing existing student, populate user fields
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
        student = super().save(commit=False)
        
        if not student.pk:  # Creating new student
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
                role='student'
            )
            student.user = user
        else:  # Updating existing student
            user = student.user
            user.username = self.cleaned_data['username']
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.phone = self.cleaned_data['phone']
            user.address = self.cleaned_data['address']
            user.date_of_birth = self.cleaned_data['date_of_birth']
            user.save()
        
        if commit:
            student.save()
        
        return student


class ParentForm(forms.ModelForm):
    """
    Parent form
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
        model = Parent
        fields = ['relationship', 'occupation', 'workplace', 'emergency_contact']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Arabic labels
        self.fields['relationship'].label = 'صلة القرابة'
        self.fields['occupation'].label = 'المهنة'
        self.fields['workplace'].label = 'مكان العمل'
        self.fields['emergency_contact'].label = 'رقم الطوارئ'
        
        # If editing existing parent, populate user fields
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
        parent = super().save(commit=False)
        
        if not parent.pk:  # Creating new parent
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
                role='parent'
            )
            parent.user = user
        else:  # Updating existing parent
            user = parent.user
            user.username = self.cleaned_data['username']
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.phone = self.cleaned_data['phone']
            user.address = self.cleaned_data['address']
            user.date_of_birth = self.cleaned_data['date_of_birth']
            user.save()
        
        if commit:
            parent.save()
        
        return parent


class StudentParentForm(forms.ModelForm):
    """
    Student-Parent relationship form
    """
    class Meta:
        model = StudentParent
        fields = ['parent', 'is_primary']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Arabic labels
        self.fields['parent'].label = 'ولي الأمر'
        self.fields['is_primary'].label = 'ولي أمر أساسي'
