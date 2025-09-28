from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages
from django.http import JsonResponse


def role_required(allowed_roles):
    """
    Decorator to check if user has required role
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                if request.headers.get('Accept') == 'application/json':
                    return JsonResponse({'error': 'غير مصرح'}, status=401)
                return redirect('accounts:login')
            
            if request.user.role not in allowed_roles:
                if request.headers.get('Accept') == 'application/json':
                    return JsonResponse({'error': 'ليس لديك صلاحية للوصول'}, status=403)
                
                messages.error(request, 'ليس لديك صلاحية للوصول إلى هذه الصفحة')
                return redirect('dashboard:dashboard')
            
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


def admin_required(view_func):
    """
    Decorator to check if user is admin
    """
    return role_required(['admin'])(view_func)


def teacher_required(view_func):
    """
    Decorator to check if user is teacher
    """
    return role_required(['teacher', 'admin'])(view_func)


def student_required(view_func):
    """
    Decorator to check if user is student
    """
    return role_required(['student', 'admin'])(view_func)


def parent_required(view_func):
    """
    Decorator to check if user is parent
    """
    return role_required(['parent', 'admin'])(view_func)


def api_role_required(allowed_roles):
    """
    API decorator to check if user has required role
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return JsonResponse({'error': 'غير مصرح'}, status=401)
            
            if request.user.role not in allowed_roles:
                return JsonResponse({'error': 'ليس لديك صلاحية للوصول'}, status=403)
            
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
