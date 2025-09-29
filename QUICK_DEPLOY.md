# نشر سريع على Render 🚀

## المشروع جاهز! 

**GitHub Repository**: `https://github.com/JJ36t/school-mangement.git`

## خطوات سريعة:

### 1. اذهب إلى [render.com](https://render.com)
### 2. سجل دخول بـ GitHub
### 3. اضغط "New +" → "Web Service"
### 4. اختر المستودع: `JJ36t/school-mangement`

### 5. الإعدادات:
```
Name: school-management-system
Environment: Python 3
Build Command: pip install -r requirements.txt
Start Command: gunicorn school_management.wsgi:application
```

### 6. متغيرات البيئة:
```
SECRET_KEY=django-insecure-2n7whfb)s5+o6q=+xg(a4cm1v@!q8mbq0dkeeitomcw_j4r@6%
DEBUG=False
DJANGO_SETTINGS_MODULE=school_management.settings_production
DISABLE_COLLECTSTATIC=1
```

### 7. إنشاء قاعدة بيانات:
- اضغط "New +" → "PostgreSQL"
- اختر الخطة المجانية
- اربطها بـ Web Service

### 8. اضغط "Create Web Service"

### 9. بعد النشر، في Shell:
```bash
python manage.py migrate
python manage.py createsuperuser
```

## 🎉 انتهى!

ستحصل على رابط مثل: `https://school-management-system.onrender.com`

---
**ملاحظة**: استخدم الخطة المجانية للاختبار، والخطة المدفوعة ($7/شهر) للاستخدام الإنتاجي.
