# إصلاح Start Command في Render

## 🎉 البناء نجح! لكن هناك مشكلة في التشغيل

### المشكلة:
Render يحاول تشغيل: `gunicorn app:app`
بينما يجب أن يكون: `gunicorn school_management.wsgi:application`

### الحل:

#### 1. اذهب إلى Render Dashboard
#### 2. اختر Web Service الخاص بك
#### 3. اذهب إلى Settings
#### 4. في قسم "Build & Deploy"
#### 5. غير Start Command إلى:
```
gunicorn school_management.wsgi:application
```

#### 6. تأكد من أن Build Command هو:
```
pip install -r requirements.txt
```

#### 7. تأكد من Environment Variables:
```
SECRET_KEY=django-insecure-2n7whfb)s5+o6q=+xg(a4cm1v@!q8mbq0dkeeitomcw_j4r@6%
DEBUG=False
DJANGO_SETTINGS_MODULE=school_management.settings_production
DISABLE_COLLECTSTATIC=0
```

#### 8. اضغط "Save Changes"
#### 9. اضغط "Manual Deploy" → "Deploy latest commit"

## 🔧 إعدادات Render الصحيحة:

### Basic Settings:
- **Name**: school-management-system
- **Environment**: Python 3
- **Region**: Oregon (US West) أو Frankfurt (EU Central)
- **Branch**: master

### Build & Deploy:
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn school_management.wsgi:application`

### Advanced Settings:
- **Python Version**: 3.11.9 (أو اتركه فارغاً ليستخدم الافتراضي)

### Environment Variables:
```
SECRET_KEY=django-insecure-2n7whfb)s5+o6q=+xg(a4cm1v@!q8mbq0dkeeitomcw_j4r@6%
DEBUG=False
DJANGO_SETTINGS_MODULE=school_management.settings_production
DISABLE_COLLECTSTATIC=0
```

## 🗄️ قاعدة البيانات:

تأكد من أن لديك PostgreSQL database مربوط بـ Web Service.

## 🎯 النتيجة المتوقعة:

بعد إصلاح Start Command:
- ✅ النشر سينجح
- ✅ الموقع سيعمل على الرابط
- ✅ يمكن إنشاء مستخدم مدير

---

**الخطوة الوحيدة المطلوبة الآن: تغيير Start Command في Render Dashboard!**
