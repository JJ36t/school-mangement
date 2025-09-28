from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Teacher
from .forms import TeacherForm


@login_required
def teacher_list_view(request):
    """
    Teacher list view
    """
    teachers = Teacher.objects.filter(is_active=True).order_by('-created_at')
    
    # Pagination
    paginator = Paginator(teachers, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'teachers/teacher_list.html', {'page_obj': page_obj})


@login_required
def create_teacher_view(request):
    """
    Create teacher view
    """
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = form.save()
            messages.success(request, f'تم إنشاء المعلم {teacher.user.get_full_name()} بنجاح')
            return redirect('teachers:teacher_detail', teacher_id=teacher.id)
    else:
        form = TeacherForm()
    
    return render(request, 'teachers/create_teacher.html', {'form': form})


@login_required
def teacher_detail_view(request, teacher_id):
    """
    Teacher detail view
    """
    teacher = get_object_or_404(Teacher, id=teacher_id)
    return render(request, 'teachers/teacher_detail.html', {'teacher': teacher})


@login_required
def edit_teacher_view(request, teacher_id):
    """
    Edit teacher view
    """
    teacher = get_object_or_404(Teacher, id=teacher_id)
    
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, f'تم تحديث المعلم {teacher.user.get_full_name()} بنجاح')
            return redirect('teachers:teacher_detail', teacher_id=teacher.id)
    else:
        form = TeacherForm(instance=teacher)
    
    return render(request, 'teachers/edit_teacher.html', {'form': form, 'teacher': teacher})


@login_required
def delete_teacher_view(request, teacher_id):
    """
    Delete teacher view
    """
    teacher = get_object_or_404(Teacher, id=teacher_id)
    
    if request.method == 'POST':
        teacher_name = teacher.user.get_full_name()
        teacher.delete()
        messages.success(request, f'تم حذف المعلم {teacher_name} بنجاح')
        return redirect('teachers:teacher_list')
    
    return render(request, 'teachers/delete_teacher.html', {'teacher': teacher})


# Teacher Subject Assignment views (placeholders)
@login_required
def teacher_subjects_view(request, teacher_id):
    """
    Teacher subjects view - placeholder
    """
    teacher = get_object_or_404(Teacher, id=teacher_id)
    # Will be implemented when subjects module is ready
    subjects = []
    
    return render(request, 'teachers/teacher_subjects.html', {
        'teacher': teacher,
        'subjects': subjects
    })


@login_required
def assign_subject_view(request, teacher_id):
    """
    Assign subject to teacher view - placeholder
    """
    teacher = get_object_or_404(Teacher, id=teacher_id)
    # Will be implemented when subjects module is ready
    
    return render(request, 'teachers/assign_subject.html', {'teacher': teacher})


@login_required
def remove_subject_view(request, teacher_id, subject_id):
    """
    Remove subject from teacher view - placeholder
    """
    teacher = get_object_or_404(Teacher, id=teacher_id)
    # Will be implemented when subjects module is ready
    
    return render(request, 'teachers/remove_subject.html', {'teacher': teacher})