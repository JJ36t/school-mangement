#!/usr/bin/env bash
# Build script for Render deployment

echo "Starting build process..."

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --settings=school_management.settings_production

# Run migrations
echo "Running database migrations..."
python manage.py migrate --settings=school_management.settings_production

# Create superuser if it doesn't exist
echo "Creating superuser..."
python manage.py shell --settings=school_management.settings_production << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@school.com', 'admin123')
    print('Superuser created successfully')
else:
    print('Superuser already exists')
EOF

echo "Build completed successfully!"
