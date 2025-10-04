from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum, Avg, Max, Min
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
    
    # Basic statistics
    total_students = Student.objects.filter(is_active=True).count()
    total_teachers = Teacher.objects.filter(is_active=True).count()
    total_grades = Grade.objects.count()
    
    # Get subjects and classes count
    from subjects.models import Subject, Class
    total_subjects = Subject.objects.filter(is_active=True).count()
    total_classes = Class.objects.filter(is_active=True).count()
    
    # Payment statistics
    total_payments = Payment.objects.filter(status='paid').aggregate(Sum('amount'))['amount__sum'] or 0
    pending_payments = Payment.objects.filter(status='pending').aggregate(Sum('amount'))['amount__sum'] or 0
    
    # Calculate collection rate
    total_expected = total_payments + pending_payments
    collection_rate = (total_payments / total_expected * 100) if total_expected > 0 else 0
    
    # Attendance statistics
    from attendance.models import Attendance
    total_attendance_records = Attendance.objects.count()
    present_count = Attendance.objects.filter(status='present').count()
    late_count = Attendance.objects.filter(status='late').count()
    absent_count = Attendance.objects.filter(status='absent').count()
    
    attendance_rate = (present_count / total_attendance_records * 100) if total_attendance_records > 0 else 0
    
    # Grade statistics
    grade_stats = Grade.objects.aggregate(
        avg_marks=Avg('marks_obtained'),
        max_marks=Max('marks_obtained'),
        min_marks=Min('marks_obtained')
    )
    average_grade = grade_stats['avg_marks'] or 0
    excellent_students = Grade.objects.filter(marks_obtained__gte=90).values('student').distinct().count()
    weak_students = Grade.objects.filter(marks_obtained__lt=60).values('student').distinct().count()
    
    # Students by grade distribution
    from subjects.models import Class
    students_by_grade = []
    students_by_grade_labels = []
    students_by_grade_data = []
    
    for class_obj in Class.objects.filter(is_active=True):
        student_count = Student.objects.filter(grade=class_obj.grade, is_active=True).count()
        if student_count > 0:
            students_by_grade_labels.append(class_obj.name)
            students_by_grade_data.append(student_count)
    
    # Monthly payments (last 6 months)
    from django.utils import timezone
    from datetime import timedelta
    monthly_payments_labels = []
    monthly_payments_data = []
    
    for i in range(6):
        month = timezone.now() - timedelta(days=30*i)
        month_start = month.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        if i == 0:
            month_end = timezone.now()
        else:
            next_month = month_start + timedelta(days=32)
            month_end = next_month.replace(day=1) - timedelta(days=1)
        
        monthly_total = Payment.objects.filter(
            status='paid',
            paid_date__gte=month_start,
            paid_date__lte=month_end
        ).aggregate(Sum('amount'))['amount__sum'] or 0
        
        monthly_payments_labels.append(month.strftime('%Y-%m'))
        monthly_payments_data.append(float(monthly_total))
    
    # Reverse to show oldest first
    monthly_payments_labels.reverse()
    monthly_payments_data.reverse()
    
    # Recent activities
    recent_students = Student.objects.filter(is_active=True).order_by('-created_at')[:5]
    recent_teachers = Teacher.objects.filter(is_active=True).order_by('-created_at')[:5]
    
    # Get notifications
    recent_notifications = Notification.objects.filter(is_sent=True).order_by('-sent_date')[:5]
    
    context = {
        'total_students': total_students,
        'total_teachers': total_teachers,
        'total_grades': total_grades,
        'total_subjects': total_subjects,
        'total_classes': total_classes,
        'total_payments': total_payments,
        'pending_payments': pending_payments,
        'collection_rate': collection_rate,
        'attendance_rate': attendance_rate,
        'late_count': late_count,
        'absent_count': absent_count,
        'average_grade': average_grade,
        'excellent_students': excellent_students,
        'weak_students': weak_students,
        'students_by_grade_labels': students_by_grade_labels,
        'students_by_grade_data': students_by_grade_data,
        'monthly_payments_labels': monthly_payments_labels,
        'monthly_payments_data': monthly_payments_data,
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