from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Notification, NotificationTemplate, NotificationLog
from .forms import NotificationForm, NotificationTemplateForm


@login_required
def notification_list_view(request):
    """
    Notification list view
    """
    notifications = Notification.objects.all().order_by('-created_at')
    
    # Pagination
    paginator = Paginator(notifications, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'notifications/notification_list.html', {'page_obj': page_obj})


@login_required
def create_notification_view(request):
    """
    Create notification view
    """
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            notification = form.save(commit=False)
            notification.sender = request.user
            notification.save()
            form.save_m2m()  # Save many-to-many relationships
            messages.success(request, f'تم إنشاء الإشعار بنجاح')
            return redirect('notifications:notification_detail', notification_id=notification.id)
    else:
        form = NotificationForm()
    
    return render(request, 'notifications/create_notification.html', {'form': form})


@login_required
def notification_detail_view(request, notification_id):
    """
    Notification detail view
    """
    notification = get_object_or_404(Notification, id=notification_id)
    return render(request, 'notifications/notification_detail.html', {'notification': notification})


@login_required
def edit_notification_view(request, notification_id):
    """
    Edit notification view
    """
    notification = get_object_or_404(Notification, id=notification_id)
    
    if request.method == 'POST':
        form = NotificationForm(request.POST, instance=notification)
        if form.is_valid():
            form.save()
            messages.success(request, f'تم تحديث الإشعار بنجاح')
            return redirect('notifications:notification_detail', notification_id=notification.id)
    else:
        form = NotificationForm(instance=notification)
    
    return render(request, 'notifications/edit_notification.html', {'form': form, 'notification': notification})


@login_required
def delete_notification_view(request, notification_id):
    """
    Delete notification view
    """
    notification = get_object_or_404(Notification, id=notification_id)
    
    if request.method == 'POST':
        notification.delete()
        messages.success(request, f'تم حذف الإشعار بنجاح')
        return redirect('notifications:notification_list')
    
    return render(request, 'notifications/delete_notification.html', {'notification': notification})


@login_required
def send_notification_view(request, notification_id):
    """
    Send notification view
    """
    notification = get_object_or_404(Notification, id=notification_id)
    
    if request.method == 'POST':
        # Mark as sent and update sent_date
        notification.is_sent = True
        notification.save()
        messages.success(request, f'تم إرسال الإشعار بنجاح')
        return redirect('notifications:notification_detail', notification_id=notification.id)
    
    return render(request, 'notifications/send_notification.html', {'notification': notification})


@login_required
def mark_notification_read_view(request, notification_id):
    """
    Mark notification as read view
    """
    notification = get_object_or_404(Notification, id=notification_id)
    
    if request.method == 'POST':
        notification.is_read = True
        notification.save()
        messages.success(request, f'تم تمييز الإشعار كمقروء')
        return redirect('notifications:notification_detail', notification_id=notification.id)
    
    return render(request, 'notifications/mark_notification_read.html', {'notification': notification})


# Notification Template views
@login_required
def notification_template_list_view(request):
    """
    Notification template list view
    """
    templates = NotificationTemplate.objects.filter(is_active=True).order_by('name')
    
    # Pagination
    paginator = Paginator(templates, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'notifications/notification_template_list.html', {'page_obj': page_obj})


@login_required
def create_notification_template_view(request):
    """
    Create notification template view
    """
    if request.method == 'POST':
        form = NotificationTemplateForm(request.POST)
        if form.is_valid():
            template = form.save()
            messages.success(request, f'تم إنشاء قالب الإشعار بنجاح')
            return redirect('notifications:notification_template_detail', template_id=template.id)
    else:
        form = NotificationTemplateForm()
    
    return render(request, 'notifications/create_notification_template.html', {'form': form})


@login_required
def notification_template_detail_view(request, template_id):
    """
    Notification template detail view
    """
    template = get_object_or_404(NotificationTemplate, id=template_id)
    return render(request, 'notifications/notification_template_detail.html', {'template': template})


@login_required
def edit_notification_template_view(request, template_id):
    """
    Edit notification template view
    """
    template = get_object_or_404(NotificationTemplate, id=template_id)
    
    if request.method == 'POST':
        form = NotificationTemplateForm(request.POST, instance=template)
        if form.is_valid():
            form.save()
            messages.success(request, f'تم تحديث قالب الإشعار بنجاح')
            return redirect('notifications:notification_template_detail', template_id=template.id)
    else:
        form = NotificationTemplateForm(instance=template)
    
    return render(request, 'notifications/edit_notification_template.html', {'form': form, 'template': template})


@login_required
def delete_notification_template_view(request, template_id):
    """
    Delete notification template view
    """
    template = get_object_or_404(NotificationTemplate, id=template_id)
    
    if request.method == 'POST':
        template_name = template.name
        template.delete()
        messages.success(request, f'تم حذف قالب الإشعار {template_name} بنجاح')
        return redirect('notifications:notification_template_list')
    
    return render(request, 'notifications/delete_notification_template.html', {'template': template})


# Notification Log views
@login_required
def notification_log_list_view(request):
    """
    Notification log list view
    """
    logs = NotificationLog.objects.all().order_by('-created_at')
    
    # Pagination
    paginator = Paginator(logs, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'notifications/notification_log_list.html', {'page_obj': page_obj})


@login_required
def notification_log_detail_view(request, log_id):
    """
    Notification log detail view
    """
    log = get_object_or_404(NotificationLog, id=log_id)
    return render(request, 'notifications/notification_log_detail.html', {'log': log})


# User Notifications
@login_required
def my_notifications_view(request):
    """
    User's notifications view
    """
    notifications = request.user.received_notifications.all().order_by('-created_at')
    
    # Pagination
    paginator = Paginator(notifications, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'notifications/my_notifications.html', {'page_obj': page_obj})


@login_required
def unread_notifications_count_view(request):
    """
    Get unread notifications count (AJAX)
    """
    count = request.user.received_notifications.filter(is_read=False).count()
    return JsonResponse({'count': count})