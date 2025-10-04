#!/usr/bin/env python
"""
Create superuser script for production deployment
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

from django.contrib.auth import get_user_model

User = get_user_model()

def create_superuser():
    """Create superuser if it doesn't exist"""
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

if __name__ == '__main__':
    create_superuser()
