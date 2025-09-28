"""
URL configuration for school_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

# تخصيص واجهة الإدارة
admin.site.site_header = "نظام إدارة المدرسة"
admin.site.site_title = "إدارة المدرسة"
admin.site.index_title = "مرحباً بك في نظام إدارة المدرسة"

def root_redirect(request):
    """Redirect root URL to dashboard"""
    return redirect('dashboard:dashboard')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # App URLs
    path('dashboard/', include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('subjects/', include('subjects.urls')),
    path('grades/', include('grades.urls')),
    path('attendance/', include('attendance.urls')),
    path('payments/', include('payments.urls')),
    path('notifications/', include('notifications.urls')),
    
    # Root redirect to dashboard
    path('', root_redirect, name='root_redirect'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)