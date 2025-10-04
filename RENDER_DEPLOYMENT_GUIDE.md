# دليل رفع المشروع على Render

## 📋 المتطلبات

### 1. ملفات المشروع المطلوبة ✅
- `requirements.txt` - تبعيات Python
- `Procfile` - أوامر تشغيل الخادم
- `runtime.txt` - إصدار Python
- `build_render.sh` - سكريبت البناء
- `school_management/settings_production.py` - إعدادات الإنتاج

### 2. إعدادات قاعدة البيانات
- Render يوفر PostgreSQL مجاناً
- سيتم إنشاء `DATABASE_URL` تلقائياً

## 🚀 خطوات الرفع على Render

### الخطوة 1: إنشاء حساب على Render
1. اذهب إلى [render.com](https://render.com)
2. سجل حساب جديد أو سجل دخول
3. اربط حساب GitHub

### الخطوة 2: إنشاء Web Service جديد
1. اضغط على "New +"
2. اختر "Web Service"
3. اربط repository: `https://github.com/JJ36t/school-mangement.git`

### الخطوة 3: إعدادات الخدمة

#### Basic Settings:
- **Name**: `school-management-system`
- **Environment**: `Python 3`
- **Region**: `Oregon (US West)`
- **Branch**: `master`

#### Build & Deploy:
- **Build Command**: `./build_render.sh`
- **Start Command**: `gunicorn school_management.wsgi:application --bind 0.0.0.0:$PORT`

#### Advanced Settings:
- **Python Version**: `3.11.9`
- **Auto-Deploy**: `Yes`

### الخطوة 4: متغيرات البيئة (Environment Variables)

أضف هذه المتغيرات في قسم Environment Variables:

```
SECRET_KEY=django-insecure-your-secret-key-here
DEBUG=False
DJANGO_SETTINGS_MODULE=school_management.settings_production
```

### الخطوة 5: إعداد قاعدة البيانات

#### خيار 1: قاعدة بيانات Render المجانية
1. اذهب إلى "Dashboard"
2. اضغط "New +"
3. اختر "PostgreSQL"
4. اختر الخطة المجانية
5. انسخ `DATABASE_URL`
6. أضفها كمتغير بيئة في Web Service

#### خيار 2: قاعدة بيانات خارجية
- استخدم ElephantSQL أو أي خدمة PostgreSQL أخرى
- أضف `DATABASE_URL` كمتغير بيئة

### الخطوة 6: النشر
1. اضغط "Create Web Service"
2. انتظر حتى ينتهي البناء (5-10 دقائق)
3. ستظهر رسالة "Deployed successfully"

## 🔧 استكشاف الأخطاء

### مشاكل شائعة:

#### 1. خطأ في البناء
```bash
# تحقق من build_render.sh
chmod +x build_render.sh
```

#### 2. خطأ في قاعدة البيانات
- تأكد من إضافة `DATABASE_URL`
- تحقق من إعدادات `settings_production.py`

#### 3. خطأ في الملفات الثابتة
- تأكد من `collectstatic` في build script
- تحقق من إعدادات `STATIC_ROOT`

#### 4. خطأ في الـ CSRF
- أضف domain الخاص بك في `CSRF_TRUSTED_ORIGINS`

## 📊 مراقبة الأداء

### Logs:
- اذهب إلى "Logs" في dashboard
- راقب الأخطاء والتحذيرات

### Metrics:
- راقب استخدام الذاكرة والمعالج
- راقب استجابة الخادم

## 🔐 أمان الإنتاج

### متغيرات البيئة المهمة:
```
SECRET_KEY=your-very-secure-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.onrender.com
```

### إعدادات الأمان:
- تم تفعيل `SECURE_BROWSER_XSS_FILTER`
- تم تفعيل `SECURE_CONTENT_TYPE_NOSNIFF`
- تم تعيين `X_FRAME_OPTIONS = 'DENY'`

## 📱 الوصول للموقع

بعد النشر الناجح:
- **الرابط**: `https://your-app-name.onrender.com`
- **المدير**: `admin` / `admin123`

## 🔄 التحديثات المستقبلية

1. ادفع التغييرات إلى GitHub
2. Render سيقوم بالتحديث التلقائي
3. راقب logs للتأكد من النجاح

## 📞 الدعم

- **Render Docs**: [render.com/docs](https://render.com/docs)
- **Django Deployment**: [docs.djangoproject.com](https://docs.djangoproject.com/en/stable/howto/deployment/)