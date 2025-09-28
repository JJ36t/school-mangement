from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Payment, PaymentSummary
from .forms import PaymentForm, PaymentSummaryForm


@login_required
def payment_list_view(request):
    """
    Payment list view
    """
    payments = Payment.objects.all().order_by('-created_at')
    
    # Pagination
    paginator = Paginator(payments, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'payments/payment_list.html', {'page_obj': page_obj})


@login_required
def create_payment_view(request):
    """
    Create payment view
    """
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save()
            messages.success(request, f'تم إنشاء الدفعة بنجاح')
            return redirect('payments:payment_detail', payment_id=payment.id)
    else:
        form = PaymentForm()
    
    return render(request, 'payments/create_payment.html', {'form': form})


@login_required
def payment_detail_view(request, payment_id):
    """
    Payment detail view
    """
    payment = get_object_or_404(Payment, id=payment_id)
    return render(request, 'payments/payment_detail.html', {'payment': payment})


@login_required
def edit_payment_view(request, payment_id):
    """
    Edit payment view
    """
    payment = get_object_or_404(Payment, id=payment_id)
    
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            messages.success(request, f'تم تحديث الدفعة بنجاح')
            return redirect('payments:payment_detail', payment_id=payment.id)
    else:
        form = PaymentForm(instance=payment)
    
    return render(request, 'payments/edit_payment.html', {'form': form, 'payment': payment})


@login_required
def delete_payment_view(request, payment_id):
    """
    Delete payment view
    """
    payment = get_object_or_404(Payment, id=payment_id)
    
    if request.method == 'POST':
        payment.delete()
        messages.success(request, f'تم حذف الدفعة بنجاح')
        return redirect('payments:payment_list')
    
    return render(request, 'payments/delete_payment.html', {'payment': payment})


@login_required
def mark_payment_paid_view(request, payment_id):
    """
    Mark payment as paid view
    """
    payment = get_object_or_404(Payment, id=payment_id)
    
    if request.method == 'POST':
        payment.status = 'paid'
        payment.save()
        messages.success(request, f'تم تسجيل الدفعة كمدفوعة بنجاح')
        return redirect('payments:payment_detail', payment_id=payment.id)
    
    return render(request, 'payments/mark_payment_paid.html', {'payment': payment})


# Payment Summary views
@login_required
def payment_summary_list_view(request):
    """
    Payment summary list view
    """
    summaries = PaymentSummary.objects.all().order_by('-created_at')
    
    # Pagination
    paginator = Paginator(summaries, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'payments/payment_summary_list.html', {'page_obj': page_obj})


@login_required
def create_payment_summary_view(request):
    """
    Create payment summary view
    """
    if request.method == 'POST':
        form = PaymentSummaryForm(request.POST)
        if form.is_valid():
            summary = form.save()
            messages.success(request, f'تم إنشاء ملخص الدفعات بنجاح')
            return redirect('payments:payment_summary_detail', summary_id=summary.id)
    else:
        form = PaymentSummaryForm()
    
    return render(request, 'payments/create_payment_summary.html', {'form': form})


@login_required
def payment_summary_detail_view(request, summary_id):
    """
    Payment summary detail view
    """
    summary = get_object_or_404(PaymentSummary, id=summary_id)
    return render(request, 'payments/payment_summary_detail.html', {'summary': summary})


@login_required
def edit_payment_summary_view(request, summary_id):
    """
    Edit payment summary view
    """
    summary = get_object_or_404(PaymentSummary, id=summary_id)
    
    if request.method == 'POST':
        form = PaymentSummaryForm(request.POST, instance=summary)
        if form.is_valid():
            form.save()
            messages.success(request, f'تم تحديث ملخص الدفعات بنجاح')
            return redirect('payments:payment_summary_detail', summary_id=summary.id)
    else:
        form = PaymentSummaryForm(instance=summary)
    
    return render(request, 'payments/edit_payment_summary.html', {'form': form, 'summary': summary})


@login_required
def delete_payment_summary_view(request, summary_id):
    """
    Delete payment summary view
    """
    summary = get_object_or_404(PaymentSummary, id=summary_id)
    
    if request.method == 'POST':
        summary.delete()
        messages.success(request, f'تم حذف ملخص الدفعات بنجاح')
        return redirect('payments:payment_summary_list')
    
    return render(request, 'payments/delete_payment_summary.html', {'summary': summary})


# Payment Reports (placeholders)
@login_required
def student_payments_view(request, student_id):
    """
    Student payments view - placeholder
    """
    from students.models import Student
    student = get_object_or_404(Student, id=student_id)
    # Will be implemented when payments are properly linked
    payments = []
    
    return render(request, 'payments/student_payments.html', {
        'student': student,
        'payments': payments
    })


@login_required
def student_payment_report_view(request, student_id):
    """
    Student payment report view - placeholder
    """
    from students.models import Student
    student = get_object_or_404(Student, id=student_id)
    # Will be implemented when payments are properly linked
    
    return render(request, 'payments/student_payment_report.html', {'student': student})


@login_required
def overdue_payments_view(request):
    """
    Overdue payments view - placeholder
    """
    # Will be implemented when payments are properly linked
    overdue_payments = []
    
    return render(request, 'payments/overdue_payments.html', {'overdue_payments': overdue_payments})


@login_required
def financial_report_view(request):
    """
    Financial report view - placeholder
    """
    # Will be implemented when payments are properly linked
    
    return render(request, 'payments/financial_report.html')