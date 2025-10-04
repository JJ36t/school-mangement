#!/usr/bin/env python
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_management.settings')
django.setup()

from django.contrib.auth import get_user_model
from students.models import Student
from teachers.models import Teacher
from subjects.models import Subject, Class
from grades.models import Grade
from attendance.models import Attendance
from payments.models import Payment
from notifications.models import Notification
from datetime import date, datetime, timedelta
import random

User = get_user_model()

def create_test_data():
    print("إنشاء بيانات تجريبية...")
    
    # Create admin if not exists
    if not User.objects.filter(username='admin').exists():
        admin = User.objects.create_user(
            username='admin', 
            email='admin@school.com', 
            password='admin123', 
            first_name='مدير', 
            last_name='النظام', 
            role='admin'
        )
        print('تم إنشاء مدير النظام')
    
    # Create subjects
    subjects_data = [
        {'name': 'الرياضيات', 'code': 'MATH101', 'grade': '10'},
        {'name': 'اللغة العربية', 'code': 'ARAB101', 'grade': '10'},
        {'name': 'العلوم', 'code': 'SCI101', 'grade': '11'},
        {'name': 'اللغة الإنجليزية', 'code': 'ENG101', 'grade': '11'},
    ]
    
    subjects = []
    for subject_data in subjects_data:
        subject, created = Subject.objects.get_or_create(
            name=subject_data['name'],
            defaults={
                'code': subject_data['code'],
                'grade': subject_data['grade'],
                'description': f'وصف مادة {subject_data["name"]}',
                'credit_hours': 3
            }
        )
        subjects.append(subject)
        if created:
            print(f"تم إنشاء المادة: {subject_data['name']}")
    
    # Create classes
    classes_data = [
        {'name': 'الصف العاشر أ', 'grade': '10', 'section': 'أ'},
        {'name': 'الصف العاشر ب', 'grade': '10', 'section': 'ب'},
        {'name': 'الصف الحادي عشر أ', 'grade': '11', 'section': 'أ'},
        {'name': 'الصف الثاني عشر أ', 'grade': '12', 'section': 'أ'},
    ]
    
    classes = []
    for class_data in classes_data:
        class_obj, created = Class.objects.get_or_create(
            name=class_data['name'],
            defaults={
                'grade': class_data['grade'],
                'section': class_data['section'],
                'level': 'high',
                'capacity': 30,
                'location': f'قاعة {class_data["name"]}'
            }
        )
        classes.append(class_obj)
        if created:
            print(f"تم إنشاء الصف: {class_data['name']}")
    
    # Create teachers
    teachers_data = [
        {'first_name': 'أحمد', 'last_name': 'محمد', 'specialization': 'الرياضيات'},
        {'first_name': 'فاطمة', 'last_name': 'علي', 'specialization': 'اللغة العربية'},
        {'first_name': 'محمد', 'last_name': 'حسن', 'specialization': 'العلوم'},
        {'first_name': 'نور', 'last_name': 'أحمد', 'specialization': 'اللغة الإنجليزية'},
    ]
    
    teachers = []
    for i, teacher_data in enumerate(teachers_data):
        if not User.objects.filter(username=f'teacher{i+1}').exists():
            user = User.objects.create_user(
                username=f'teacher{i+1}',
                email=f'teacher{i+1}@school.com',
                password='teacher123',
                first_name=teacher_data['first_name'],
                last_name=teacher_data['last_name'],
                role='teacher'
            )
            teacher = Teacher.objects.create(
                user=user,
                teacher_id=f'T{i+1:03d}',
                gender=random.choice(['male', 'female']),
                qualification=random.choice(['bachelor', 'master', 'phd']),
                specialization=teacher_data['specialization'],
                experience_years=random.randint(1, 20),
                hire_date=date.today() - timedelta(days=random.randint(30, 365)),
                salary=random.randint(2000, 5000)
            )
            teachers.append(teacher)
            print(f"تم إنشاء المعلم: {teacher_data['first_name']} {teacher_data['last_name']}")
        else:
            try:
                teachers.append(Teacher.objects.get(user__username=f'teacher{i+1}'))
            except Teacher.DoesNotExist:
                pass
    
    # Create students
    students_data = [
        {'first_name': 'سارة', 'last_name': 'أحمد', 'grade': '10'},
        {'first_name': 'علي', 'last_name': 'محمد', 'grade': '10'},
        {'first_name': 'مريم', 'last_name': 'حسن', 'grade': '11'},
        {'first_name': 'يوسف', 'last_name': 'علي', 'grade': '11'},
        {'first_name': 'زينب', 'last_name': 'أحمد', 'grade': '12'},
        {'first_name': 'حسن', 'last_name': 'محمد', 'grade': '12'},
    ]
    
    students = []
    for i, student_data in enumerate(students_data):
        if not User.objects.filter(username=f'student{i+1}').exists():
            user = User.objects.create_user(
                username=f'student{i+1}',
                email=f'student{i+1}@school.com',
                password='student123',
                first_name=student_data['first_name'],
                last_name=student_data['last_name'],
                role='student'
            )
            student = Student.objects.create(
                user=user,
                student_id=f'S{i+1:03d}',
                grade=student_data['grade'],
                section='أ',
                gender=random.choice(['male', 'female']),
                enrollment_date=date.today() - timedelta(days=random.randint(30, 365)),
                parent_name=f'والد {student_data["first_name"]}',
                parent_phone=f'0790123456{i+20}',
                address=f'عنوان الطالب {i+1}'
            )
            students.append(student)
            print(f"تم إنشاء الطالب: {student_data['first_name']} {student_data['last_name']}")
        else:
            try:
                students.append(Student.objects.get(user__username=f'student{i+1}'))
            except Student.DoesNotExist:
                pass
    
    # Create grades
    print("إنشاء الدرجات...")
    for student in students:
        for subject in subjects:
            if subject.grade == student.grade:  # Only create grades for matching grades
                for exam_type in ['midterm', 'final', 'quiz']:
                    grade, created = Grade.objects.get_or_create(
                        student=student,
                        subject=subject,
                        exam_type=exam_type,
                        defaults={
                            'teacher': random.choice(teachers),
                            'marks_obtained': random.randint(60, 100),
                            'total_marks': 100,
                            'exam_date': date.today() - timedelta(days=random.randint(1, 30)),
                            'remarks': f'ملاحظات {exam_type}'
                        }
                    )
                    if created:
                        print(f"تم إنشاء درجة للطالب {student.user.get_full_name()} في {subject.name}")
    
    # Create attendance records
    print("إنشاء سجلات الحضور...")
    for student in students:
        for i in range(20):  # 20 days of attendance
            attendance_date = date.today() - timedelta(days=i)
            status = random.choice(['present', 'late', 'absent'])
            
            attendance, created = Attendance.objects.get_or_create(
                student=student,
                date=attendance_date,
                defaults={
                    'status': status,
                    'notes': f'ملاحظات الحضور {status}'
                }
            )
            if created:
                print(f"تم إنشاء سجل حضور للطالب {student.user.get_full_name()}")
    
    # Create payments
    print("إنشاء المدفوعات...")
    for student in students:
        for i in range(3):  # 3 payments per student
            payment, created = Payment.objects.get_or_create(
                student=student,
                payment_type='tuition',
                amount=random.randint(1000, 3000),
                payment_date=date.today() - timedelta(days=random.randint(1, 90)),
                defaults={
                    'status': random.choice(['paid', 'pending']),
                    'payment_method': random.choice(['cash', 'bank_transfer']),
                    'notes': f'دفعة رسوم دراسية {i+1}'
                }
            )
            if created:
                print(f"تم إنشاء دفعة للطالب {student.user.get_full_name()}")
    
    # Create notifications
    print("إنشاء الإشعارات...")
    notifications_data = [
        {'title': 'موعد الامتحانات النهائية', 'message': 'سيتم عقد الامتحانات النهائية في الأسبوع القادم'},
        {'title': 'إجازة الربيع', 'message': 'ستبدأ إجازة الربيع من الأسبوع القادم'},
        {'title': 'تحديث الجدول الدراسي', 'message': 'تم تحديث الجدول الدراسي للفصل الثاني'},
    ]
    
    for notification_data in notifications_data:
        notification, created = Notification.objects.get_or_create(
            title=notification_data['title'],
            defaults={
                'message': notification_data['message'],
                'notification_type': 'general',
                'priority': 'medium',
                'is_sent': True,
                'sent_date': datetime.now() - timedelta(hours=random.randint(1, 24))
            }
        )
        if created:
            print(f"تم إنشاء الإشعار: {notification_data['title']}")
    
    print("تم إنشاء البيانات التجريبية بنجاح!")

if __name__ == '__main__':
    create_test_data()
