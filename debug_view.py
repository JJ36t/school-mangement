#!/usr/bin/env python
"""
Debug view to test if Django is working
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

from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

def debug_view(request):
    """Simple debug view"""
    try:
        # Test basic Django functionality
        return HttpResponse(f"""
        <h1>Django Debug</h1>
        <p>Django is working!</p>
        <p>Settings: {settings.DATABASES}</p>
        <p>Debug: {settings.DEBUG}</p>
        <p>Installed Apps: {len(settings.INSTALLED_APPS)}</p>
        <p>Template Dirs: {settings.TEMPLATES[0]['DIRS']}</p>
        """)
    except Exception as e:
        return HttpResponse(f"<h1>Error</h1><p>{str(e)}</p>")

if __name__ == '__main__':
    print("Debug view created")
