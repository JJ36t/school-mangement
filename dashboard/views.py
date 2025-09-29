from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum, Avg
from students.models import Student
from teachers.models import Teacher
from grades.models import Grade
from attendance.models import Attendance
from payments.models import Payment
from notifications.models import Notification


@login_required
def dashboard_view(request):
    """
    Main dashboard view - redirects based on user role
    """
    user = request.user
    
    if user.role == 'admin':
        return redirect('dashboard:admin_dashboard')
    elif user.role == 'teacher':
        return redirect('dashboard:teacher_dashboard')
    elif user.role == 'student':
        return redirect('dashboard:student_dashboard')
    elif user.role == 'parent':
        return redirect('dashboard:parent_dashboard')
    else:
        return render(request, 'dashboard/dashboard.html')


@login_required
def admin_dashboard_view(request):
    """
    Admin dashboard view
    """
    if request.user.role != 'admin':
        return redirect('dashboard:dashboard')
    
    # Get statistics
    total_students = Student.objects.filter(is_active=True).count()
    total_teachers = Teacher.objects.filter(is_active=True).count()
    total_grades = Grade.objects.count()
    total_payments = Payment.objects.filter(status='paid').aggregate(Sum('amount'))['amount__sum'] or 0
    
    # Recent activities (placeholder)
    recent_students = Student.objects.filter(is_active=True).order_by('-created_at')[:5]
    recent_teachers = Teacher.objects.filter(is_active=True).order_by('-created_at')[:5]
    
    # Get notifications
    recent_notifications = Notification.objects.filter(is_sent=True).order_by('-sent_date')[:5]
    
    context = {
        'total_students': total_students,
        'total_teachers': total_teachers,
        'total_grades': total_grades,
        'total_payments': total_payments,
        'recent_students': recent_students,
        'recent_teachers': recent_teachers,
        'recent_notifications': recent_notifications,
    }
    
    return render(request, 'dashboard/admin_dashboard.html', context)


@login_required
def teacher_dashboard_view(request):
    """
    Teacher dashboard view
    """
    if request.user.role != 'teacher':
        return redirect('dashboard:dashboard')
    
    # Get teacher instance
    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        teacher = None
    
    # Get teacher's subjects and students (placeholder)
    subjects = []  # Will be implemented in subjects module
    students = []  # Will be implemented when subjects are assigned
    
    # Get teacher's notifications
    my_notifications = request.user.received_notifications.filter(is_sent=True).order_by('-sent_date')[:5]
    
    context = {
        'teacher': teacher,
        'subjects': subjects,
        'students': students,
        'my_notifications': my_notifications,
    }
    
    return render(request, 'dashboard/teacher_dashboard.html', context)


@login_required
def student_dashboard_view(request):
    """
    Student dashboard view
    """
    if request.user.role != 'student':
        return redirect('dashboard:dashboard')
    
    # Get student instance
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        student = None
    
    # Get student's grades and attendance (placeholder)
    grades = []  # Will be implemented in grades module
    attendance = []  # Will be implemented in attendance module
    
    # Get student's notifications
    my_notifications = request.user.received_notifications.filter(is_sent=True).order_by('-sent_date')[:5]
    
    context = {
        'student': student,
        'grades': grades,
        'attendance': attendance,
        'my_notifications': my_notifications,
    }
    
    return render(request, 'dashboard/student_dashboard.html', context)


@login_required
def parent_dashboard_view(request):
    """
    Parent dashboard view
    """
    if request.user.role != 'parent':
        return redirect('dashboard:dashboard')
    
    # Get parent instance and their children (placeholder)
    try:
        from students.models import Parent
        parent = Parent.objects.get(user=request.user)
        children = []  # Will be implemented when student-parent relationships are set
    except Parent.DoesNotExist:
        parent = None
        children = []
    
    context = {
        'parent': parent,
        'children': children,
    }
    
    return render(request, 'dashboard/parent_dashboard.html', context)


@login_required
def statistics_view(request):
    """
    General statistics view
    """
    if request.user.role != 'admin':
        return redirect('dashboard:dashboard')
    
    # Basic statistics
    stats = {
        'total_students': Student.objects.filter(is_active=True).count(),
        'total_teachers': Teacher.objects.filter(is_active=True).count(),
        'total_grades': Grade.objects.count(),
        'total_payments': Payment.objects.filter(status='paid').count(),
    }
    
    return render(request, 'dashboard/statistics.html', {'stats': stats})


# Placeholder views for specific statistics
@login_required
def student_statistics_view(request):
    """Student statistics view - placeholder"""
    return render(request, 'dashboard/student_statistics.html')


@login_required
def teacher_statistics_view(request):
    """Teacher statistics view - placeholder"""
    return render(request, 'dashboard/teacher_statistics.html')


@login_required
def grade_statistics_view(request):
    """Grade statistics view - placeholder"""
    return render(request, 'dashboard/grade_statistics.html')


@login_required
def attendance_statistics_view(request):
    """Attendance statistics view - placeholder"""
    return render(request, 'dashboard/attendance_statistics.html')


@login_required
def payment_statistics_view(request):
    """Payment statistics view - placeholder"""
    return render(request, 'dashboard/payment_statistics.html')