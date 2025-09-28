from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Subject, Class, TeacherSubject
from .forms import SubjectForm, ClassForm, TeacherSubjectForm


@login_required
def subject_list_view(request):
    """
    Subject list view
    """
    subjects = Subject.objects.filter(is_active=True).order_by('name')
    
    # Pagination
    paginator = Paginator(subjects, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'subjects/subject_list.html', {'page_obj': page_obj})


@login_required
def create_subject_view(request):
    """
    Create subject view
    """
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save()
            messages.success(request, f'تم إنشاء المادة {subject.name} بنجاح')
            return redirect('subjects:subject_detail', subject_id=subject.id)
    else:
        form = SubjectForm()
    
    return render(request, 'subjects/create_subject.html', {'form': form})


@login_required
def subject_detail_view(request, subject_id):
    """
    Subject detail view
    """
    subject = get_object_or_404(Subject, id=subject_id)
    return render(request, 'subjects/subject_detail.html', {'subject': subject})


@login_required
def edit_subject_view(request, subject_id):
    """
    Edit subject view
    """
    subject = get_object_or_404(Subject, id=subject_id)
    
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            messages.success(request, f'تم تحديث المادة {subject.name} بنجاح')
            return redirect('subjects:subject_detail', subject_id=subject.id)
    else:
        form = SubjectForm(instance=subject)
    
    return render(request, 'subjects/edit_subject.html', {'form': form, 'subject': subject})


@login_required
def delete_subject_view(request, subject_id):
    """
    Delete subject view
    """
    subject = get_object_or_404(Subject, id=subject_id)
    
    if request.method == 'POST':
        subject_name = subject.name
        subject.delete()
        messages.success(request, f'تم حذف المادة {subject_name} بنجاح')
        return redirect('subjects:subject_list')
    
    return render(request, 'subjects/delete_subject.html', {'subject': subject})


@login_required
def assign_teacher_view(request, subject_id):
    """
    Assign teacher to subject view
    """
    subject = get_object_or_404(Subject, id=subject_id)
    
    if request.method == 'POST':
        form = TeacherSubjectForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.subject = subject
            assignment.save()
            messages.success(request, f'تم تعيين المعلم {assignment.teacher.user.get_full_name()} للمادة {subject.name} بنجاح')
            return redirect('subjects:subject_detail', subject_id=subject.id)
    else:
        form = TeacherSubjectForm()
    
    return render(request, 'subjects/assign_teacher.html', {'form': form, 'subject': subject})


# Class views
@login_required
def class_list_view(request):
    """
    Class list view
    """
    classes = Class.objects.filter(is_active=True).order_by('grade', 'section')
    
    # Pagination
    paginator = Paginator(classes, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'subjects/class_list.html', {'page_obj': page_obj})


@login_required
def create_class_view(request):
    """
    Create class view
    """
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            class_obj = form.save()
            messages.success(request, f'تم إنشاء الفصل {class_obj.name} بنجاح')
            return redirect('subjects:class_detail', class_id=class_obj.id)
    else:
        form = ClassForm()
    
    return render(request, 'subjects/create_class.html', {'form': form})


@login_required
def class_detail_view(request, class_id):
    """
    Class detail view
    """
    class_obj = get_object_or_404(Class, id=class_id)
    return render(request, 'subjects/class_detail.html', {'class_obj': class_obj})


@login_required
def edit_class_view(request, class_id):
    """
    Edit class view
    """
    class_obj = get_object_or_404(Class, id=class_id)
    
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=class_obj)
        if form.is_valid():
            form.save()
            messages.success(request, f'تم تحديث الفصل {class_obj.name} بنجاح')
            return redirect('subjects:class_detail', class_id=class_obj.id)
    else:
        form = ClassForm(instance=class_obj)
    
    return render(request, 'subjects/edit_class.html', {'form': form, 'class_obj': class_obj})


@login_required
def delete_class_view(request, class_id):
    """
    Delete class view
    """
    class_obj = get_object_or_404(Class, id=class_id)
    
    if request.method == 'POST':
        class_name = class_obj.name
        class_obj.delete()
        messages.success(request, f'تم حذف الفصل {class_name} بنجاح')
        return redirect('subjects:class_list')
    
    return render(request, 'subjects/delete_class.html', {'class_obj': class_obj})


# Teacher-Subject Assignment views
@login_required
def teacher_subject_list_view(request):
    """
    Teacher-Subject assignment list view
    """
    assignments = TeacherSubject.objects.all().order_by('-assigned_date')
    
    # Pagination
    paginator = Paginator(assignments, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'subjects/teacher_subject_list.html', {'page_obj': page_obj})


@login_required
def create_teacher_subject_view(request):
    """
    Create teacher-subject assignment view
    """
    if request.method == 'POST':
        form = TeacherSubjectForm(request.POST)
        if form.is_valid():
            assignment = form.save()
            messages.success(request, f'تم تعيين المعلم {assignment.teacher.user.get_full_name()} للمادة {assignment.subject.name} بنجاح')
            return redirect('subjects:teacher_subject_list')
    else:
        form = TeacherSubjectForm()
    
    return render(request, 'subjects/create_teacher_subject.html', {'form': form})


@login_required
def edit_teacher_subject_view(request, assignment_id):
    """
    Edit teacher-subject assignment view
    """
    assignment = get_object_or_404(TeacherSubject, id=assignment_id)
    
    if request.method == 'POST':
        form = TeacherSubjectForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            messages.success(request, f'تم تحديث تعيين المعلم {assignment.teacher.user.get_full_name()} للمادة {assignment.subject.name} بنجاح')
            return redirect('subjects:teacher_subject_list')
    else:
        form = TeacherSubjectForm(instance=assignment)
    
    return render(request, 'subjects/edit_teacher_subject.html', {'form': form, 'assignment': assignment})


@login_required
def delete_teacher_subject_view(request, assignment_id):
    """
    Delete teacher-subject assignment view
    """
    assignment = get_object_or_404(TeacherSubject, id=assignment_id)
    
    if request.method == 'POST':
        teacher_name = assignment.teacher.user.get_full_name()
        subject_name = assignment.subject.name
        assignment.delete()
        messages.success(request, f'تم إلغاء تعيين المعلم {teacher_name} للمادة {subject_name} بنجاح')
        return redirect('subjects:teacher_subject_list')
    
    return render(request, 'subjects/delete_teacher_subject.html', {'assignment': assignment})