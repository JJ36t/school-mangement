"""
WSGI config for school_management project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Choose settings based on environment
if os.environ.get('DJANGO_SETTINGS_MODULE'):
    # Use the environment variable if set
    settings_module = os.environ.get('DJANGO_SETTINGS_MODULE')
else:
    # Default to production settings for deployment
    settings_module = 'school_management.settings_production'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
