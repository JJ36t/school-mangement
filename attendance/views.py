from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Attendance, AttendanceSummary
from .forms import AttendanceForm, AttendanceSummaryForm


@login_required
def attendance_list_view(request):
    """
    Attendance list view
    """
    attendance_records = Attendance.objects.all().order_by('-date')
    
    # Pagination
    paginator = Paginator(attendance_records, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'attendance/attendance_list.html', {'page_obj': page_obj})


@login_required
def create_attendance_view(request):
    """
    Create attendance view
    """
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save()
            messages.success(request, f'تم تسجيل الحضور بنجاح')
            return redirect('attendance:attendance_detail', attendance_id=attendance.id)
    else:
        form = AttendanceForm()
    
    return render(request, 'attendance/create_attendance.html', {'form': form})


@login_required
def attendance_detail_view(request, attendance_id):
    """
    Attendance detail view
    """
    attendance = get_object_or_404(Attendance, id=attendance_id)
    return render(request, 'attendance/attendance_detail.html', {'attendance': attendance})


@login_required
def edit_attendance_view(request, attendance_id):
    """
    Edit attendance view
    """
    attendance = get_object_or_404(Attendance, id=attendance_id)
    
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            messages.success(request, f'تم تحديث تسجيل الحضور بنجاح')
            return redirect('attendance:attendance_detail', attendance_id=attendance.id)
    else:
        form = AttendanceForm(instance=attendance)
    
    return render(request, 'attendance/edit_attendance.html', {'form': form, 'attendance': attendance})


@login_required
def delete_attendance_view(request, attendance_id):
    """
    Delete attendance view
    """
    attendance = get_object_or_404(Attendance, id=attendance_id)
    
    if request.method == 'POST':
        attendance.delete()
        messages.success(request, f'تم حذف تسجيل الحضور بنجاح')
        return redirect('attendance:attendance_list')
    
    return render(request, 'attendance/delete_attendance.html', {'attendance': attendance})


# Bulk Attendance views (placeholders)
@login_required
def bulk_create_attendance_view(request):
    """
    Bulk create attendance view - placeholder
    """
    # Will be implemented for bulk attendance entry
    return render(request, 'attendance/bulk_create_attendance.html')


@login_required
def bulk_update_attendance_view(request):
    """
    Bulk update attendance view - placeholder
    """
    # Will be implemented for bulk attendance update
    return render(request, 'attendance/bulk_update_attendance.html')


# Attendance Summary views
@login_required
def attendance_summary_list_view(request):
    """
    Attendance summary list view
    """
    summaries = AttendanceSummary.objects.all().order_by('-created_at')
    
    # Pagination
    paginator = Paginator(summaries, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'attendance/attendance_summary_list.html', {'page_obj': page_obj})


@login_required
def create_attendance_summary_view(request):
    """
    Create attendance summary view
    """
    if request.method == 'POST':
        form = AttendanceSummaryForm(request.POST)
        if form.is_valid():
            summary = form.save()
            messages.success(request, f'تم إنشاء ملخص الحضور بنجاح')
            return redirect('attendance:attendance_summary_detail', summary_id=summary.id)
    else:
        form = AttendanceSummaryForm()
    
    return render(request, 'attendance/create_attendance_summary.html', {'form': form})


@login_required
def attendance_summary_detail_view(request, summary_id):
    """
    Attendance summary detail view
    """
    summary = get_object_or_404(AttendanceSummary, id=summary_id)
    return render(request, 'attendance/attendance_summary_detail.html', {'summary': summary})


@login_required
def edit_attendance_summary_view(request, summary_id):
    """
    Edit attendance summary view
    """
    summary = get_object_or_404(AttendanceSummary, id=summary_id)
    
    if request.method == 'POST':
        form = AttendanceSummaryForm(request.POST, instance=summary)
        if form.is_valid():
            form.save()
            messages.success(request, f'تم تحديث ملخص الحضور بنجاح')
            return redirect('attendance:attendance_summary_detail', summary_id=summary.id)
    else:
        form = AttendanceSummaryForm(instance=summary)
    
    return render(request, 'attendance/edit_attendance_summary.html', {'form': form, 'summary': summary})


@login_required
def delete_attendance_summary_view(request, summary_id):
    """
    Delete attendance summary view
    """
    summary = get_object_or_404(AttendanceSummary, id=summary_id)
    
    if request.method == 'POST':
        summary.delete()
        messages.success(request, f'تم حذف ملخص الحضور بنجاح')
        return redirect('attendance:attendance_summary_list')
    
    return render(request, 'attendance/delete_attendance_summary.html', {'summary': summary})


# Attendance Reports (placeholders)
@login_required
def student_attendance_view(request, student_id):
    """
    Student attendance view - placeholder
    """
    from students.models import Student
    student = get_object_or_404(Student, id=student_id)
    # Will be implemented when attendance is properly linked
    attendance_records = []
    
    return render(request, 'attendance/student_attendance.html', {
        'student': student,
        'attendance_records': attendance_records
    })


@login_required
def student_attendance_report_view(request, student_id):
    """
    Student attendance report view - placeholder
    """
    from students.models import Student
    student = get_object_or_404(Student, id=student_id)
    # Will be implemented when attendance is properly linked
    
    return render(request, 'attendance/student_attendance_report.html', {'student': student})


@login_required
def class_attendance_view(request, class_id):
    """
    Class attendance view - placeholder
    """
    from subjects.models import Class
    class_obj = get_object_or_404(Class, id=class_id)
    # Will be implemented when attendance is properly linked
    attendance_records = []
    
    return render(request, 'attendance/class_attendance.html', {
        'class_obj': class_obj,
        'attendance_records': attendance_records
    })


@login_required
def subject_attendance_view(request, subject_id):
    """
    Subject attendance view - placeholder
    """
    from subjects.models import Subject
    subject = get_object_or_404(Subject, id=subject_id)
    # Will be implemented when attendance is properly linked
    attendance_records = []
    
    return render(request, 'attendance/subject_attendance.html', {
        'subject': subject,
        'attendance_records': attendance_records
    })