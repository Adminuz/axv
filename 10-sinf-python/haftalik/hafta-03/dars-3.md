# 9-dars. APIni testlash. APIni hujjatlashtirish. (Swagger, Redoc)

## Dars rejasi (80 daqiqa)

1. **O'tgan mavzuni takrorlash (10 daqiqa):** Statik va media fayllar, multipart upload, `FileResponse` bo'yicha savol-javob. 1-bobning yakuniy bosqichiga kirish.
2. **Yangi mavzu: APIni avtomatlashtirilgan testlash (25 daqiqa):**
   - Nega test yoziladi? (Regressiya xatolarining oldini olish, refaktoringda ishonchlilik).
   - Test tuzilishi: `APITestCase`, `APIClient`, `force_authenticate`.
   - Testlar uchun Factory/Seed yondashuvi (`apps/common/tests/factories.py`).
   - 4 ta asosiy ssenariy: Ro'yxatni ko'rish (200 OK), yangi post yaratish (201 Created), mehmonga ruxsat bermaslik (401 Unauthorized) va boshqa birovning postini o'zgartirishni taqiqlash (403 Forbidden).
   - `python manage.py test` orqali testlarni ishga tushirish.
3. **Yangi mavzu: APIni avtomatlashtirilgan hujjatlashtirish (25 daqiqa):**
   - OpenAPI 3.0 standarti nima?
   - `drf-spectacular` kutubxonasi va sozlamalar (`DEFAULT_SCHEMA_CLASS`).
   - Swagger UI interfeysi (`/api/docs/`): barcha endpointlarni brauzerda interaktiv sinash ("Try it out").
   - ReDoc interfeysi (`/api/redoc/`): toza va professional texnik hujjat.
4. **Amaliyot: Testlarni yurgazish va Swagger UI ni ochish (10 daqiqa):**
   - Terminalda testlarni ishga tushirish va barcha testlar yashil (`OK`) o'tganini ko'rish.
   - Brauzerda `/api/docs/` sahifasini ochib, Swagger orqali so'rov yuborish.
5. **Dars xulosasi va 1-bob yakuniy hisoboti (10 daqiqa):** 1-bob bo'yicha erishilgan barcha natijalarni sarhisob qilish, baholash, uyga vazifa.

---

## Mentor konspekti

### 1. Nima uchun test yozish zarur?

Dasturchilar ko'pincha: "Men kodni yozdim, brauzerda bir marta sinab ko'rdim, ishlayapti-ku, nega yana test yozishim kerak?" deb o'ylashadi.
Sabablari:
1. **Regressiya (Eski narsalarning buzilishi):** Siz loyihaning 10-haftasida yangi funksiya qo'shganingizda, 1-haftada yozilgan login yoki postlar ro'yxati tasodifan buzilib qolishi mumkin. Avtomatik testlar 5 soniyada barcha eski kodlar buzilmaganligini kafolatlaydi!
2. **Jamoaviy ishonch:** Boshqa dasturchi sizning kodingizni o'zgartirganda, testlar ishlasa, u xotirjam bo'ladi.
3. **Avtomatlashtirilgan CI/CD:** GitHub Actions kabi tizimlar yangi kodni serverga joylashdan (deploy) oldin barcha testlarni tekshiradi; agar bitta test yiqilsa ham, xato kod serverga kiritilmaydi.

### 2. DRF Test vositalari: `APITestCase` va `APIClient`

DRF da test yozish uchun maxsus `APITestCase` ishlatiladi.
U har safar test boshlanishida alohida **vaqtinchalik xotira ma'lumotlar bazasi** ochadi, test tugagach esa uni butunlay tozalab tashlaydi. Asosiy ishlab chiqish bazangizga hech qanday xalal yetmaydi!

**Asosiy metodlar:**
- `self.client.get(url)` &mdash; GET so'rovi yuborish;
- `self.client.post(url, data, format='json')` &mdash; POST so'rovi;
- `self.client.force_authenticate(user=user)` &mdash; foydalanuvchini parolsiz zudlik bilan tizimga kirgan deb e'lon qilish;
- `self.assertEqual(response.status_code, status.HTTP_200_OK)` &mdash; kutilgan natija bilan solishtirish.

### 3. API Hujjatlashtirish: Swagger UI va ReDoc

Frontend dasturchilar (React, Android, iOS) backend dasturchidan har doim: "API dokumentatsiyasi qani? Qaysi URL ga qanday ma'lumot yuborishim kerak?" deb so'rashadi.
Qo'lda Word yoki Notion-da hujjat yozish esa tezda eskirib qoladi.

**Yechim:** **`drf-spectacular`** kutubxonasi!
U sizning ViewSet, Serializer va modillaringizni avtomatik tahlil qiladi va eng so'nggi OpenAPI 3.0 formatidagi interaktiv hujjatni shakllantiradi:
- **/api/docs/ (Swagger UI):** Har bir endpointni ochib, ichidagi parametrlarni ko'rish va "Try it out" tugmasi orqali brauzerdan turib haqiqiy so'rov yuborish imkonini beradi.
- **/api/redoc/ (ReDoc):** Katta API lar uchun chiroyli 3 ustunli kitob shaklidagi rasmiy qo'llanma.

---

## Kod namunalari

### 1. Testlar kodi (`src/apps/news/tests/test_posts_api.py`)

```python
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from apps.news.models import Category, Post

User = get_user_model()

class PostAPITestCase(APITestCase):
    def setUp(self):
        # Test uchun dastlabki foydalanuvchi va kategoriya
        self.user = User.objects.create_user(email="test@mail.uz", password="password123")
        self.category = Category.objects.create(name="Texnologiya", slug="texnologiya")
        self.post = Post.objects.create(
            title="Birinchi maqola",
            slug="birinchi-maqola",
            body="Maqola matni",
            status="published",
            category=self.category,
            author=self.user,
        )

    def test_list_posts(self):
        """Maqolalar ro'yxatini olishni tekshirish"""
        response = self.client.get("/api/v1/posts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.data)
        self.assertEqual(len(response.data["results"]), 1)

    def test_create_post_authenticated(self):
        """Tizimga kirgan foydalanuvchi maqola yarata olishi kerak"""
        self.client.force_authenticate(user=self.user)
        payload = {
            "title": "Yangi yangilik",
            "body": "Yangi matn",
            "category": self.category.id,
            "status": "draft",
        }
        response = self.client.post("/api/v1/posts/", data=payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Yangi yangilik")

    def test_create_post_unauthenticated_forbidden(self):
        """Mehmon foydalanuvchi maqola yarata olmasligi kerak (401)"""
        payload = {"title": "Xakerlik", "body": "Xato", "category": self.category.id}
        response = self.client.post("/api/v1/posts/", data=payload)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
```

### 2. Swagger va ReDoc sozlamalari (`src/config/urls.py`)

```python
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("apps.news.urls")),
    path("api/v1/", include("apps.comments.urls")),

    # OpenAPI Schema va Hujjatlashtirish
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
```

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq (Oson): Test buyrug'i
Terminalda faqat `apps.news` ilovasining testlarini ishga tushirish uchun qanday buyruq beriladi?

**Yechim:**
```bash
python manage.py test apps.news
```

### 2-topshiriq (O'rta): Boshqa birovning postini o'zgartirish testini yozish
`PostAPITestCase` ichida 2-foydalanuvchi (`other_user`) 1-foydalanuvchining maqolasini `PATCH /api/v1/posts/{slug}/` orqali o'zgartirmoqchi bo'lganda `403 Forbidden` xatosi qaytishini tekshiruvchi test metodini yozing.

**Yechim:**
```python
def test_update_other_user_post_forbidden(self):
    other_user = User.objects.create_user(email="other@mail.uz", password="password123")
    self.client.force_authenticate(user=other_user)

    url = f"/api/v1/posts/{self.post.slug}/"
    response = self.client.patch(url, data={"title": "O'zgartirilgan sarlavha"})
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
```

### 3-topshiriq (Qiyin): drf-spectacular konfiguratsiyasi
`src/config/settings/base.py` faylida loyiha nomi "NewsPortal API", versiyasi "v1.0.0", muallifi "AXV 10-sinf" deb chiqishi uchun `SPECTACULAR_SETTINGS` lug'atini qanday sozlash kerak?

**Yechim:**
```python
INSTALLED_APPS += ["drf_spectacular"]

REST_FRAMEWORK["DEFAULT_SCHEMA_CLASS"] = "drf_spectacular.openapi.AutoSchema"

SPECTACULAR_SETTINGS = {
    "TITLE": "NewsPortal API",
    "DESCRIPTION": "10-sinf Muhammad al-Xorazmiy vorislari uchun NewsPortal REST API hujjatlari.",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}
```

---

## Tezkor nazorat savollari

1. Nima uchun test yozish yirik loyihalarda shart hisoblanadi?
   - **Javob:** Regressiyalarni (eski kodlarning kutilmaganda buzilishini) oldini olish va yangi o'zgarishlarning xavfsizligini ta'minlash uchun.
2. `APITestCase` ning oddiy `TestCase` dan qanday afzalligi bor?
   - **Javob:** U o'z ichiga REST API larni testlash uchun tayyorlangan `APIClient` vositasini oladi (`self.client`).
3. `force_authenticate` metodi nima vazifani bajaradi?
   - **Javob:** Test paytida murakkab login jarayonini aylanib o'tib, so'rovni ma'lum bir foydalanuvchi nomidan yuborish imkonini beradi.
4. Swagger UI va ReDoc ning frontend dasturchilar uchun qanday yordami bor?
   - **Javob:** U barcha mavjud endpointlar, kerakli parametrlar, so'rov va javob modellarini aniq ko'rsatadi va brauzerning o'zida testlash imkonini beradi.
5. OpenAPI 3.0 spetsifikatsiyasi nima?
   - **Javob:** REST API lar tuzilishi, yo'llari va modellarini tavsiflash uchun qabul qilingan xalqaro standart format (JSON yoki YAML).

---

## Uyga vazifa

1. `src/apps/news/tests/test_posts_api.py` faylini konspektdagi namuna asosida yarating va terminalda `python manage.py test` qilib, barcha testlar muvaffaqiyatli o'tganiga ishonch hosil qiling.
2. `pip install drf-spectacular` kutubxonasini o'rnating va `settings/base.py` hamda `urls.py` ga Swagger va ReDoc marshrutlarini ulang.
3. Brauzer orqali `http://127.0.0.1:8000/api/docs/` manzilini oching va Swagger interfeysidagi "Try it out" tugmasi orqali yangi maqola yaratib ko'ring.
