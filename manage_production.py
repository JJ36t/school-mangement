#!/usr/bin/env python
"""
Production management script
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

def main():
    """Main function to run production setup"""
    print("Starting production setup...")
    
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
    
    # Collect static files
    print("Collecting static files...")
    execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])
    
    print("Production setup completed!")

if __name__ == '__main__':
    main()
