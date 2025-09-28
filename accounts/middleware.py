from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages


class RoleBasedAccessMiddleware:
    """
    Middleware to check user roles and redirect accordingly
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Skip middleware for static files, admin, and API endpoints
        if (request.path.startswith('/static/') or 
            request.path.startswith('/media/') or 
            request.path.startswith('/admin/') or
            request.path.startswith('/api/')):
            return self.get_response(request)
        
        # Skip middleware for login and logout pages
        if (request.path in ['/accounts/login/', '/accounts/logout/'] or
            request.path.startswith('/accounts/register')):
            return self.get_response(request)
        
        # Check if user is authenticated
        if request.user.is_authenticated:
            # Define role-based access rules
            role_access_rules = {
                'admin': [
                    '/dashboard/admin/',
                    '/accounts/users/',
                    '/students/',
                    '/teachers/',
                    '/subjects/',
                    '/grades/',
                    '/attendance/',
                    '/payments/',
                    '/notifications/',
                ],
                'teacher': [
                    '/dashboard/teacher/',
                    '/grades/',
                    '/attendance/',
                ],
                'student': [
                    '/dashboard/student/',
                ],
                'parent': [
                    '/dashboard/parent/',
                ]
            }
            
            user_role = request.user.role
            allowed_paths = role_access_rules.get(user_role, [])
            
            # Check if current path is allowed for user role
            if not any(request.path.startswith(path) for path in allowed_paths):
                # Redirect to appropriate dashboard
                if user_role == 'admin':
                    return redirect('dashboard:admin_dashboard')
                elif user_role == 'teacher':
                    return redirect('dashboard:teacher_dashboard')
                elif user_role == 'student':
                    return redirect('dashboard:student_dashboard')
                elif user_role == 'parent':
                    return redirect('dashboard:parent_dashboard')
                else:
                    return redirect('dashboard:dashboard')
        
        return self.get_response(request)
