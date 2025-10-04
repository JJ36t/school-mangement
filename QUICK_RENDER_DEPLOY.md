# 🚀 رفع سريع على Render

## الخطوات السريعة:

### 1. اذهب إلى Render.com
- سجل حساب جديد أو سجل دخول
- اربط حساب GitHub

### 2. إنشاء Web Service
- اضغط "New +" → "Web Service"
- اربط: `https://github.com/JJ36t/school-mangement.git`

### 3. الإعدادات:
```
Name: school-management-system
Environment: Python 3
Build Command: ./build_render.sh
Start Command: gunicorn school_management.wsgi:application --bind 0.0.0.0:$PORT
```

### 4. متغيرات البيئة:
```
SECRET_KEY=django-insecure-your-secret-key-here
DEBUG=False
DJANGO_SETTINGS_MODULE=school_management.settings_production
```

### 5. قاعدة البيانات:
- اضغط "New +" → "PostgreSQL" (مجاني)
- انسخ DATABASE_URL
- أضفها كمتغير بيئة

### 6. النشر:
- اضغط "Create Web Service"
- انتظر 5-10 دقائق
- ✅ تم!

## 🔗 النتيجة:
- **الرابط**: `https://school-management-system.onrender.com`
- **المدير**: `admin` / `admin123`

## 📞 إذا واجهت مشاكل:
- تحقق من Logs في Render dashboard
- تأكد من إضافة جميع متغيرات البيئة
- تأكد من أن build_render.sh قابل للتنفيذ
