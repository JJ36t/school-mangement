# حل مشكلة خطأ 500 في Render

## 🚨 المشكلة: Server Error (500)

هذا يعني أن التطبيق يعمل لكن هناك مشكلة في الإعدادات.

## 🔧 الحلول:

### 1. تغيير إعدادات Django

في Render Dashboard:
- اذهب إلى **Environment Variables**
- غير `DJANGO_SETTINGS_MODULE` إلى:
```
DJANGO_SETTINGS_MODULE=school_management.settings_simple
```

### 2. إضافة متغيرات البيئة المطلوبة

تأكد من وجود هذه المتغيرات:
```
SECRET_KEY=django-insecure-2n7whfb)s5+o6q=+xg(a4cm1v@!q8mbq0dkeeitomcw_j4r@6%
DEBUG=False
DJANGO_SETTINGS_MODULE=school_management.settings_simple
DISABLE_COLLECTSTATIC=0
```

### 3. تشغيل Migrations

بعد النشر، في Render Shell:
```bash
python manage.py migrate
```

### 4. إنشاء مستخدم مدير

```bash
python manage.py createsuperuser
```

### 5. جمع الملفات الثابتة

```bash
python manage.py collectstatic --noinput
```

## 🔍 خطوات التشخيص:

### 1. تحقق من Logs
- اذهب إلى Render Dashboard
- اختر Web Service
- اضغط على **"Logs"**
- ابحث عن رسائل الخطأ

### 2. تحقق من قاعدة البيانات
- تأكد من وجود PostgreSQL database
- تأكد من ربطها بـ Web Service
- تحقق من `DATABASE_URL` في Environment Variables

### 3. تحقق من Start Command
تأكد من أن Start Command هو:
```
gunicorn school_management.wsgi:application
```

## 🎯 الإعدادات الصحيحة:

### Environment Variables:
```
SECRET_KEY=django-insecure-2n7whfb)s5+o6q=+xg(a4cm1v@!q8mbq0dkeeitomcw_j4r@6%
DEBUG=False
DJANGO_SETTINGS_MODULE=school_management.settings_simple
DISABLE_COLLECTSTATIC=0
```

### Build Command:
```
pip install -r requirements.txt
```

### Start Command:
```
gunicorn school_management.wsgi:application
```

## 🚀 خطوات النشر:

1. **حدث Environment Variables** في Render
2. **اضغط "Save Changes"**
3. **اضغط "Manual Deploy"** → **"Deploy latest commit"**
4. **انتظر** حتى ينتهي النشر
5. **اذهب إلى Shell** في Render
6. **شغل**:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py collectstatic --noinput
   ```

## 🔧 إذا استمر الخطأ:

### جرب إعدادات أبسط:
غير `DJANGO_SETTINGS_MODULE` إلى:
```
DJANGO_SETTINGS_MODULE=school_management.settings
```

### تحقق من Logs:
- ابحث عن رسائل الخطأ المحددة
- تحقق من مشاكل قاعدة البيانات
- تحقق من مشاكل الملفات الثابتة

---

**الخطوة الأولى: غير `DJANGO_SETTINGS_MODULE` إلى `school_management.settings_simple`**
