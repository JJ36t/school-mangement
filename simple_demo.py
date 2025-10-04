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

def create_simple_demo():
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
    
    # Create a simple test
    print('تم إنشاء البيانات التجريبية بنجاح!')

if __name__ == '__main__':
    create_simple_demo()
