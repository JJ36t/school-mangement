from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Student, Parent, StudentParent
from .forms import StudentForm, ParentForm, StudentParentForm


@login_required
def student_list_view(request):
    """
    Student list view
    """
    students = Student.objects.filter(is_active=True).order_by('-created_at')
    
    # Pagination
    paginator = Paginator(students, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'students/student_list.html', {'page_obj': page_obj})


@login_required
def create_student_view(request):
    """
    Create student view
    """
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'تم إنشاء الطالب {student.user.get_full_name()} بنجاح')
            return redirect('students:student_detail', student_id=student.id)
    else:
        form = StudentForm()
    
    return render(request, 'students/create_student.html', {'form': form})


@login_required
def student_detail_view(request, student_id):
    """
    Student detail view
    """
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'students/student_detail.html', {'student': student})


@login_required
def edit_student_view(request, student_id):
    """
    Edit student view
    """
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, f'تم تحديث الطالب {student.user.get_full_name()} بنجاح')
            return redirect('students:student_detail', student_id=student.id)
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'students/edit_student.html', {'form': form, 'student': student})


@login_required
def delete_student_view(request, student_id):
    """
    Delete student view
    """
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        student_name = student.user.get_full_name()
        student.delete()
        messages.success(request, f'تم حذف الطالب {student_name} بنجاح')
        return redirect('students:student_list')
    
    return render(request, 'students/delete_student.html', {'student': student})


# Parent views
@login_required
def parent_list_view(request):
    """
    Parent list view
    """
    parents = Parent.objects.all().order_by('-created_at')
    
    # Pagination
    paginator = Paginator(parents, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'students/parent_list.html', {'page_obj': page_obj})


@login_required
def create_parent_view(request):
    """
    Create parent view
    """
    if request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            parent = form.save()
            messages.success(request, f'تم إنشاء ولي الأمر {parent.user.get_full_name()} بنجاح')
            return redirect('students:parent_detail', parent_id=parent.id)
    else:
        form = ParentForm()
    
    return render(request, 'students/create_parent.html', {'form': form})


@login_required
def parent_detail_view(request, parent_id):
    """
    Parent detail view
    """
    parent = get_object_or_404(Parent, id=parent_id)
    return render(request, 'students/parent_detail.html', {'parent': parent})


@login_required
def edit_parent_view(request, parent_id):
    """
    Edit parent view
    """
    parent = get_object_or_404(Parent, id=parent_id)
    
    if request.method == 'POST':
        form = ParentForm(request.POST, instance=parent)
        if form.is_valid():
            form.save()
            messages.success(request, f'تم تحديث ولي الأمر {parent.user.get_full_name()} بنجاح')
            return redirect('students:parent_detail', parent_id=parent.id)
    else:
        form = ParentForm(instance=parent)
    
    return render(request, 'students/edit_parent.html', {'form': form, 'parent': parent})


@login_required
def delete_parent_view(request, parent_id):
    """
    Delete parent view
    """
    parent = get_object_or_404(Parent, id=parent_id)
    
    if request.method == 'POST':
        parent_name = parent.user.get_full_name()
        parent.delete()
        messages.success(request, f'تم حذف ولي الأمر {parent_name} بنجاح')
        return redirect('students:parent_list')
    
    return render(request, 'students/delete_parent.html', {'parent': parent})


# Student-Parent relationship views
@login_required
def student_parents_view(request, student_id):
    """
    Student parents view
    """
    student = get_object_or_404(Student, id=student_id)
    student_parents = StudentParent.objects.filter(student=student)
    
    return render(request, 'students/student_parents.html', {
        'student': student,
        'student_parents': student_parents
    })


@login_required
def add_student_parent_view(request, student_id):
    """
    Add student parent view
    """
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        form = StudentParentForm(request.POST)
        if form.is_valid():
            student_parent = form.save(commit=False)
            student_parent.student = student
            student_parent.save()
            messages.success(request, 'تم ربط ولي الأمر بالطالب بنجاح')
            return redirect('students:student_parents', student_id=student.id)
    else:
        form = StudentParentForm()
    
    return render(request, 'students/add_student_parent.html', {'form': form, 'student': student})


@login_required
def remove_student_parent_view(request, student_id, parent_id):
    """
    Remove student parent view
    """
    student = get_object_or_404(Student, id=student_id)
    parent = get_object_or_404(Parent, id=parent_id)
    student_parent = get_object_or_404(StudentParent, student=student, parent=parent)
    
    if request.method == 'POST':
        student_parent.delete()
        messages.success(request, 'تم إلغاء ربط ولي الأمر بالطالب بنجاح')
        return redirect('students:student_parents', student_id=student.id)
    
    return render(request, 'students/remove_student_parent.html', {
        'student': student,
        'parent': parent,
        'student_parent': student_parent
    })