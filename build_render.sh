#!/usr/bin/env bash
# Build script for Render deployment

echo "Starting build process..."

# Set environment variables
export DJANGO_SETTINGS_MODULE=school_management.settings_production

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Run migrations first
echo "Running database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Create superuser if it doesn't exist
echo "Creating superuser..."
python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@school.com', 'admin123')
    print('Superuser created successfully')
else:
    print('Superuser already exists')
EOF

echo "Build completed successfully!"
