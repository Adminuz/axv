# 10-dars. API havfsizligini ta'minlash

## Dars rejasi (80 daqiqa)

**Maqsad:** o'quvchi DRF loyiha API sini himoyalash usullari va mexanizmlarini (autentifikatsiya, JWT, ruxsatlar, throttling, CORS/CSRF, validatsiya, production sozlamalar) taniydi va NewsPortal loyihasida amalda qo'llaydi.

**Kutiladigan natija:** o'quvchi (1) Authentication va Authorization farqini tushuntiradi; (2) JWT ning 3 qismini va Access/Refresh farqini aytadi; (3) SimpleJWT, custom permission va throttling sozlaydi; (4) CORS va CSRF ni ajratadi; (5) security checklist bo'yicha o'z loyihasini tekshiradi.

| Vaqt | Bosqich |
|---|---|
| 10 daq | Takrorlash: 9-dars (APIni testlash, Swagger). Savol: ochiq API ga nima bo'lishi mumkin? |
| 30 daq | Yangi mavzu: API xavfsizligi, Authentication, Basic/Session/Token, JWT, Access/Refresh |
| 5 daq | Tanaffus |
| 20 daq | Ruxsatlar, custom permission, throttling, CORS, CSRF, inyeksiya |
| 10 daq | Amaliyot: SimpleJWT, IsAuthor, security checklist |
| 5 daq | Xulosa, tezkor nazorat, uyga vazifa |

---

## Mentor konspekti

### 1. API xavfsizligi nima?
Qo'llanmadagi o'xshatish: javohirlar saqlanadigan bino. Devorlar qalin, qulf mustahkam (bu ma'lumotlar bazasi), lekin hamma foydalanadigan ochiq eshiklar qolgan (bu API lar). Himoyalanmagan API bo'lsa, haker devorni buzmaydi, API orqali bazaga kirib boradi.

**API xavfsizligi** — tizimga ruxsatsiz kirish, ma'lumotni o'g'irlash, o'zgartirish yoki tizimni ishdan chiqarishga urinishlarning oldini olish mexanizmlari yig'indisi. Mobil ilova, veb-sayt, IoT qurilma: hammasi API orqali gaplashadi.

**Defense in Depth (chuqur himoya):** tizim bitta qulfga ishonmaydi. Birinchi qatlam (parol) buzilsa, ikkinchisi (ruxsatlar), keyin uchinchisi (so'rovlar sonini cheklash) to'xtatadi.

### 2. Autentifikatsiya: «Siz kimsiz?»
- DRF so'rovni View ga yetkazishdan oldin autentifikatsiya klasslaridan o'tkazadi. Kalit topilsa `request.user` ga foydalanuvchi biriktiriladi; aks holda `AnonymousUser`.
- **Autentifikatsiya foydalanuvchini bloklamaydi**, faqat «kim» ekanini aniqlaydi. Bloklash — Permissions ishi.

**DRF dagi standart turlar:**

| Tur | Qanday ishlaydi | Kamchiligi |
|---|---|---|
| Basic | Har so'rovda login:parol Base64 da | Base64 shifrlash emas! HTTPS siz parol o'g'irlanadi. Faqat test uchun |
| Session | Server sessiya yaratadi, brauzerga `sessionid` cookie | Faqat brauzer uchun qulay, CSRF ga moyil |
| Token | Server tasodifiy token yaratib bazaga saqlaydi, `Authorization: Token ...` | Har so'rovda bazaga murojaat (Database Lookup Performance) |

### 3. JWT (JSON Web Token)
- DRF ning standart paketida yo'q: `djangorestframework-simplejwt` o'rnatiladi.
- JWT o'z to'g'riligini o'zi tasdiqlaydi: server bazaga murojaat qilmasdan token soxta yoki haqiqiyligini biladi.
- Tuzilishi: `Header.Payload.Signature` (nuqta bilan ajratilgan).
  - **Header:** token turi (JWT) va algoritm (masalan HS256).
  - **Payload:** foydalanuvchi ID si, `iat` (yaratilgan vaqt), `exp` (eskirish vaqti). **Shifrlanmagan**: parol yoki karta raqamini yozmang!
  - **Signature:** server maxfiy kaliti (`SECRET_KEY`) bilan Header va Payload dan hosil qilingan xesh. Payload o'zgartirilsa imzo yaroqsiz bo'ladi.
- **Access token:** qisqa muddat (5-15 daqiqa), har so'rovda yuboriladi.
- **Refresh token:** uzoq muddat (1 kundan 1 oygacha), faqat yangi Access olish uchun.

### 4. Ruxsatlar (Permissions): «Siz nima qila olasiz?»
| Sinf | Kimga |
|---|---|
| `AllowAny` | Hammaga |
| `IsAuthenticated` | Tizimga kirganlarga (aks holda 401) |
| `IsAdminUser` | Faqat `is_staff=True` |
| `IsAuthenticatedOrReadOnly` | Mehmon faqat GET, o'zgartirish uchun login |

Custom permission: `BasePermission` dan meros. `has_permission` (URL ga kira oladimi) va `has_object_permission` (aniq obyektni o'zgartira oladimi). Shart `obj.author == request.user` bo'lmasa DRF **403 Forbidden** qaytaradi.

### 5. Throttling
- Maqsad: Brute-force (sekundiga minglab parol tekshirish) va DDoS dan himoya.
- `AnonRateThrottle` (IP bo'yicha mehmonlar), `UserRateThrottle` (login qilganlar), `ScopedRateThrottle` (alohida joylar, masalan parolni tiklash).
- Limit oshsa: **429 Too Many Requests**.
- Production uchun login ni qat'iyroq qilish: `"login_anon": "5/min"`. Kuchli variant: `django-axes` (ixtiyoriy).

### 6. CORS va CSRF
- **CORS:** brauzerning Same-Origin Policy qoidasi boshqa domendagi frontend dan so'rovni to'xtatadi. API `react-loyiha.uz` ga ruxsat berishi kerak: `django-cors-headers`. Productionda `CORS_ALLOW_ALL_ORIGINS = True` qo'ymaslik, faqat aniq originlar.
- **CSRF:** foydalanuvchi bankka kirgan (cookie bor), boshqa saytdagi yashirin forma shu cookie bilan so'rov yuboradi. Yechim: CSRF token. Faqat JWT/Token ishlatilsa CSRF muammo emas (brauzer tokenni o'zi yubormaydi).

### 7. Inyeksiya va validatsiya
«Never trust user input.» SQL Injection (`'; DROP TABLE users; --`) va XSS (izohga JavaScript yozish). Himoya: Serializer (masalan `EmailField`) va ORM escaping; Raw SQL dan qochish.

### 8. Production sozlamalari (uslubiy ko'rsatma, 8 blok)
`.env`, `DEBUG=False`, `ALLOWED_HOSTS`, HTTPS (`SECURE_SSL_REDIRECT`, secure cookie, HSTS), security headers, login throttling, upload xavfsizligi (MIME + 5 MB), logging.

---

## Kod namunalari

### 1. SimpleJWT (`settings/base.py`)
```python
from datetime import timedelta

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=10),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": True,
}

INSTALLED_APPS += ["rest_framework_simplejwt.token_blacklist"]
```
Keyin: `pip install djangorestframework-simplejwt` va `python manage.py migrate`.

### 2. Custom permission
```python
from rest_framework.permissions import BasePermission

class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
```

### 3. Throttling va CORS
```python
"DEFAULT_THROTTLE_RATES": {
    "anon": "60/min",
    "user": "300/min",
    "login_anon": "5/min",
}

INSTALLED_APPS += ["corsheaders"]
MIDDLEWARE = ["corsheaders.middleware.CorsMiddleware", *MIDDLEWARE]
CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "").split(",")
```

### 4. `prod.py` xavfsiz sozlamalari
```python
DEBUG = False
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000  # 1 yil
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
SECURE_REFERRER_POLICY = "same-origin"
```

### 5. Upload validatsiyasi
```python
def validate_cover_image(self, file):
    allowed = {"image/jpeg", "image/png", "image/webp"}
    if getattr(file, "content_type", None) not in allowed:
        raise serializers.ValidationError("Only JPEG/PNG/WEBP allowed.")
    if file.size > 5 * 1024 * 1024:
        raise serializers.ValidationError("Max size is 5MB.")
    return file
```

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq (Oson): JWT qismlarini aniqlash
`eyJ...AAA.eyJ...BBB.CCC` ko'rinishidagi tokenda 3 ta qism nima deyiladi va qaysi biri shifrlanmagan?

**Yechim:** Header, Payload, Signature. Payload shifrlanmagan (istalgan odam o'qiy oladi), shuning uchun unga parol yozilmaydi.

### 2-topshiriq (O'rta): SimpleJWT ni sozlash
Access token 10 daqiqa, refresh 7 kun yashasin, refresh har yangilanganda aylansin (rotate) va eskisi blacklist ga tushsin.

**Yechim:**
```python
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=10),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}
```
`INSTALLED_APPS` ga `rest_framework_simplejwt.token_blacklist` ni qo'shib, `migrate` qilinadi.

### 3-topshiriq (Qiyin): Security checklist audit
O'z loyihangizni qo'llanmadagi checklist bo'yicha tekshiring va 3 ta kamchilikni tuzating (masalan `DEBUG`, `.env`, login throttling).

**Yechim (namuna):** `DEBUG=True` ni `False` qilish va `ALLOWED_HOSTS` yozish; `SECRET_KEY` ni `.env` ga ko'chirib `.env` ni `.gitignore` ga qo'shish; `login_anon: 5/min` throttling ni ulash. Tekshiruv: noto'g'ri parol bilan 6 marta login urinilsa 6-urinishda `429` chiqadi.

---

## Tezkor nazorat savollari

1. Authentication va Authorization farqi nima?
   - **Javob:** Authentication «siz kimsiz?», Authorization (Permissions) «nima qila olasiz?».
2. Nima uchun Basic Authentication productionda yaroqsiz?
   - **Javob:** Base64 shifrlash emas, parol oson o'qiladi.
3. JWT ning uch qismi va Signature vazifasi?
   - **Javob:** Header, Payload, Signature; imzo Payload o'zgartirilganini aniqlaydi.
4. Nega Access token qisqa yashaydi?
   - **Javob:** O'g'irlansa ham tez yaroqsiz bo'ladi.
5. Throttling limiti oshsa qaysi status qaytadi?
   - **Javob:** `429 Too Many Requests`.
6. Productionda nega `CORS_ALLOW_ALL_ORIGINS = True` qo'yilmaydi?
   - **Javob:** Istalgan domen API ga brauzer orqali murojaat qila oladi; faqat aniq originlar ruxsat etiladi.

---

## Uyga vazifa

`uyga-vazifa.md` ga qarang.
