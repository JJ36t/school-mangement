from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Grade, GradeSummary
from .forms import GradeForm, GradeSummaryForm


@login_required
def grade_list_view(request):
    """
    Grade list view
    """
    grades = Grade.objects.all().order_by('-created_at')
    
    # Pagination
    paginator = Paginator(grades, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'grades/grade_list.html', {'page_obj': page_obj})


@login_required
def create_grade_view(request):
    """
    Create grade view
    """
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save()
            messages.success(request, f'تم إنشاء الدرجة بنجاح')
            return redirect('grades:grade_detail', grade_id=grade.id)
    else:
        form = GradeForm()
    
    return render(request, 'grades/create_grade.html', {'form': form})


@login_required
def grade_detail_view(request, grade_id):
    """
    Grade detail view
    """
    grade = get_object_or_404(Grade, id=grade_id)
    return render(request, 'grades/grade_detail.html', {'grade': grade})


@login_required
def edit_grade_view(request, grade_id):
    """
    Edit grade view
    """
    grade = get_object_or_404(Grade, id=grade_id)
    
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            messages.success(request, f'تم تحديث الدرجة بنجاح')
            return redirect('grades:grade_detail', grade_id=grade.id)
    else:
        form = GradeForm(instance=grade)
    
    return render(request, 'grades/edit_grade.html', {'form': form, 'grade': grade})


@login_required
def delete_grade_view(request, grade_id):
    """
    Delete grade view
    """
    grade = get_object_or_404(Grade, id=grade_id)
    
    if request.method == 'POST':
        grade.delete()
        messages.success(request, f'تم حذف الدرجة بنجاح')
        return redirect('grades:grade_list')
    
    return render(request, 'grades/delete_grade.html', {'grade': grade})


# Grade Summary views
@login_required
def grade_summary_list_view(request):
    """
    Grade summary list view
    """
    summaries = GradeSummary.objects.all().order_by('-created_at')
    
    # Pagination
    paginator = Paginator(summaries, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'grades/grade_summary_list.html', {'page_obj': page_obj})


@login_required
def create_grade_summary_view(request):
    """
    Create grade summary view
    """
    if request.method == 'POST':
        form = GradeSummaryForm(request.POST)
        if form.is_valid():
            summary = form.save()
            messages.success(request, f'تم إنشاء ملخص الدرجات بنجاح')
            return redirect('grades:grade_summary_detail', summary_id=summary.id)
    else:
        form = GradeSummaryForm()
    
    return render(request, 'grades/create_grade_summary.html', {'form': form})


@login_required
def grade_summary_detail_view(request, summary_id):
    """
    Grade summary detail view
    """
    summary = get_object_or_404(GradeSummary, id=summary_id)
    return render(request, 'grades/grade_summary_detail.html', {'summary': summary})


@login_required
def edit_grade_summary_view(request, summary_id):
    """
    Edit grade summary view
    """
    summary = get_object_or_404(GradeSummary, id=summary_id)
    
    if request.method == 'POST':
        form = GradeSummaryForm(request.POST, instance=summary)
        if form.is_valid():
            form.save()
            messages.success(request, f'تم تحديث ملخص الدرجات بنجاح')
            return redirect('grades:grade_summary_detail', summary_id=summary.id)
    else:
        form = GradeSummaryForm(instance=summary)
    
    return render(request, 'grades/edit_grade_summary.html', {'form': form, 'summary': summary})


@login_required
def delete_grade_summary_view(request, summary_id):
    """
    Delete grade summary view
    """
    summary = get_object_or_404(GradeSummary, id=summary_id)
    
    if request.method == 'POST':
        summary.delete()
        messages.success(request, f'تم حذف ملخص الدرجات بنجاح')
        return redirect('grades:grade_summary_list')
    
    return render(request, 'grades/delete_grade_summary.html', {'summary': summary})


# Student Grade Reports (placeholders)
@login_required
def student_grades_view(request, student_id):
    """
    Student grades view - placeholder
    """
    from students.models import Student
    student = get_object_or_404(Student, id=student_id)
    # Will be implemented when grades are properly linked
    grades = []
    
    return render(request, 'grades/student_grades.html', {
        'student': student,
        'grades': grades
    })


@login_required
def student_grade_report_view(request, student_id):
    """
    Student grade report view - placeholder
    """
    from students.models import Student
    student = get_object_or_404(Student, id=student_id)
    # Will be implemented when grades are properly linked
    
    return render(request, 'grades/student_grade_report.html', {'student': student})


@login_required
def subject_grades_view(request, subject_id):
    """
    Subject grades view - placeholder
    """
    from subjects.models import Subject
    subject = get_object_or_404(Subject, id=subject_id)
    # Will be implemented when grades are properly linked
    grades = []
    
    return render(request, 'grades/subject_grades.html', {
        'subject': subject,
        'grades': grades
    })