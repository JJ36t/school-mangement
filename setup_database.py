#!/usr/bin/env python
"""
Database setup script for production deployment
"""
import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_management.settings_simple')

# Setup Django
django.setup()

from django.core.management import execute_from_command_line
from django.contrib.auth import get_user_model

User = get_user_model()

def setup_database():
    """Setup database and create superuser"""
    print("Setting up database...")
    
    # Run migrations
    print("Running migrations...")
    execute_from_command_line(['manage.py', 'migrate'])
    
    # Create superuser if it doesn't exist
    if not User.objects.filter(username='admin').exists():
        print("Creating superuser...")
        User.objects.create_superuser(
            username='admin',
            email='admin@school.com',
            password='admin123',
            first_name='مدير',
            last_name='النظام',
            role='admin'
        )
        print("Superuser created: admin / admin123")
    else:
        print("Superuser already exists")
    
    # Create sample users
    if not User.objects.filter(username='teacher1').exists():
        print("Creating sample teacher...")
        User.objects.create_user(
            username='teacher1',
            email='teacher1@school.com',
            password='teacher123',
            first_name='أحمد',
            last_name='المعلم',
            role='teacher'
        )
        print("Sample teacher created: teacher1 / teacher123")
    
    if not User.objects.filter(username='student1').exists():
        print("Creating sample student...")
        User.objects.create_user(
            username='student1',
            email='student1@school.com',
            password='student123',
            first_name='سارة',
            last_name='الطالبة',
            role='student'
        )
        print("Sample student created: student1 / student123")
    
    print("Database setup completed!")

if __name__ == '__main__':
    setup_database()
