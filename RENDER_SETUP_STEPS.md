# خطوات إعداد النشر على Render - نظام إدارة المدارس

## 🎯 المشروع جاهز للنشر!

تم رفع المشروع إلى GitHub بنجاح: `https://github.com/JJ36t/school-mangement.git`

## 📋 الخطوات التالية:

### 1. إنشاء حساب Render

1. **اذهب إلى**: [render.com](https://render.com)
2. **اضغط على**: "Get Started for Free"
3. **سجل حساب جديد** أو **سجل دخول** باستخدام GitHub
4. **اربط حساب GitHub** مع Render

### 2. إنشاء Web Service

1. **في لوحة التحكم**، اضغط على **"New +"**
2. **اختر**: "Web Service"
3. **اختر**: "Build and deploy from a Git repository"
4. **اختر المستودع**: `JJ36t/school-mangement`

### 3. إعداد Web Service

#### Basic Settings:
- **Name**: `school-management-system`
- **Environment**: `Python 3`
- **Region**: `Oregon (US West)` أو `Frankfurt (EU Central)`
- **Branch**: `master`

#### Build & Deploy:
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn school_management.wsgi:application`

#### Advanced Settings:
- **Python Version**: `3.11.7`

### 4. إعداد متغيرات البيئة

في قسم **Environment Variables**، أضف:

```
SECRET_KEY=django-insecure-2n7whfb)s5+o6q=+xg(a4cm1v@!q8mbq0dkeeitomcw_j4r@6%
DEBUG=False
DJANGO_SETTINGS_MODULE=school_management.settings_production
DISABLE_COLLECTSTATIC=1
```

### 5. إنشاء قاعدة بيانات PostgreSQL

1. **في لوحة التحكم**، اضغط على **"New +"**
2. **اختر**: "PostgreSQL"
3. **Name**: `school-management-db`
4. **Database**: `school_management`
5. **User**: `school_user`
6. **Region**: نفس منطقة Web Service
7. **Plan**: Free (للاختبار)

### 6. ربط قاعدة البيانات بـ Web Service

1. **اذهب إلى Web Service**
2. **في قسم Environment Variables**
3. **أضف**:
   ```
   DATABASE_URL=postgresql://school_user:password@host:port/school_management
   ```
   (سيتم توفير هذه القيمة تلقائياً من Render)

### 7. النشر

1. **اضغط على**: "Create Web Service"
2. **انتظر** حتى ينتهي البناء (5-10 دقائق)
3. **ستحصل على رابط** مثل: `https://school-management-system.onrender.com`

### 8. إنشاء مستخدم مدير

بعد النشر الناجح:

1. **اذهب إلى Web Service**
2. **اضغط على**: "Shell"
3. **شغل الأوامر**:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

### 9. اختبار التطبيق

1. **اذهب إلى الرابط** الذي حصلت عليه
2. **تأكد من** أن الموقع يعمل
3. **جرب تسجيل الدخول** باستخدام المستخدم الذي أنشأته

## 🔧 إعدادات إضافية

### تفعيل الملفات الثابتة

بعد النشر الأول، في Shell:
```bash
python manage.py collectstatic --noinput
```

### إعداد النطاق المخصص

1. **في Web Service Settings**
2. **Custom Domains**
3. **أضف نطاقك** (مثل: `yourdomain.com`)
4. **اتبع تعليمات DNS**

## 🚨 استكشاف الأخطاء

### إذا فشل البناء:
- تأكد من أن جميع المكتبات في `requirements.txt`
- تحقق من إصدار Python في `runtime.txt`

### إذا فشل النشر:
- راجع Logs في Render Dashboard
- تأكد من متغيرات البيئة

### إذا لم تعمل قاعدة البيانات:
- تأكد من ربط PostgreSQL بـ Web Service
- تحقق من `DATABASE_URL`

## 📊 مراقبة الأداء

- **Metrics**: لمراقبة الأداء
- **Logs**: لمراجعة الأخطاء
- **Uptime**: لمراقبة التوفر

## 💰 التكلفة

- **الخطة المجانية**: مناسبة للاختبار
- **الخطة المدفوعة**: $7/شهر للاستخدام الإنتاجي

---

## ✅ قائمة التحقق

- [x] رفع المشروع على GitHub
- [ ] إنشاء حساب Render
- [ ] إنشاء Web Service
- [ ] إعداد متغيرات البيئة
- [ ] إنشاء قاعدة بيانات PostgreSQL
- [ ] ربط قاعدة البيانات
- [ ] النشر الأول
- [ ] إنشاء مستخدم مدير
- [ ] اختبار التطبيق

---

**الرابط الحالي للمشروع**: `https://github.com/JJ36t/school-mangement.git`

**بعد النشر ستحصل على رابط مثل**: `https://school-management-system.onrender.com`
