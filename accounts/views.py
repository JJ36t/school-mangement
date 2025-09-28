from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from .models import User
from .forms import UserRegistrationForm, UserEditForm, PasswordChangeForm
from .decorators import admin_required


@csrf_protect
@never_cache
def login_view(request):
    """
    User login view
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'تم تسجيل الدخول بنجاح')
            
            # Redirect based on user role
            if user.role == 'admin':
                return redirect('dashboard:admin_dashboard')
            elif user.role == 'teacher':
                return redirect('dashboard:teacher_dashboard')
            elif user.role == 'student':
                return redirect('dashboard:student_dashboard')
            elif user.role == 'parent':
                return redirect('dashboard:parent_dashboard')
            else:
                return redirect('dashboard:dashboard')
        else:
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة')
    
    return render(request, 'accounts/login.html')


@login_required
def logout_view(request):
    """
    User logout view
    """
    logout(request)
    messages.success(request, 'تم تسجيل الخروج بنجاح')
    return redirect('accounts:login')


def register_view(request):
    """
    User registration view
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'تم إنشاء الحساب بنجاح')
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile_view(request):
    """
    User profile view
    """
    return render(request, 'accounts/profile.html', {'user': request.user})


@login_required
def edit_profile_view(request):
    """
    Edit user profile view
    """
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تحديث الملف الشخصي بنجاح')
            return redirect('accounts:profile')
    else:
        form = UserEditForm(instance=request.user)
    
    return render(request, 'accounts/edit_profile.html', {'form': form})


@login_required
def change_password_view(request):
    """
    Change password view
    """
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تغيير كلمة المرور بنجاح')
            return redirect('accounts:profile')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'accounts/change_password.html', {'form': form})


@login_required
@admin_required
def user_list_view(request):
    """
    User list view (Admin only)
    """
    
    users = User.objects.all().order_by('-created_at')
    
    # Pagination
    paginator = Paginator(users, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'accounts/user_list.html', {'page_obj': page_obj})


@login_required
@admin_required
def create_user_view(request):
    """
    Create user view (Admin only)
    """
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'تم إنشاء المستخدم {user.username} بنجاح')
            return redirect('accounts:user_list')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'accounts/create_user.html', {'form': form})


@login_required
@admin_required
def user_detail_view(request, user_id):
    """
    User detail view (Admin only)
    """
    
    user = get_object_or_404(User, id=user_id)
    return render(request, 'accounts/user_detail.html', {'user_obj': user})


@login_required
@admin_required
def edit_user_view(request, user_id):
    """
    Edit user view (Admin only)
    """
    
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, f'تم تحديث المستخدم {user.username} بنجاح')
            return redirect('accounts:user_detail', user_id=user.id)
    else:
        form = UserEditForm(instance=user)
    
    return render(request, 'accounts/edit_user.html', {'form': form, 'user_obj': user})


@login_required
@admin_required
def delete_user_view(request, user_id):
    """
    Delete user view (Admin only)
    """
    
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        username = user.username
        user.delete()
        messages.success(request, f'تم حذف المستخدم {username} بنجاح')
        return redirect('accounts:user_list')
    
    return render(request, 'accounts/delete_user.html', {'user_obj': user})