# 4-dars. Foydalanuvchilarni boshqarish: Identifikatsiya, autentifikatsiya va avtorizatsiya. Token, session va JWT

## Dars rejasi (80 daqiqa)

1. **O'tgan haftani takrorlash va kirish (10 daqiqa):** DRF arxitekturasi, ModelSerializer, ModelViewSet va DefaultRouter bo'yicha savol-javob. Foydalanuvchi tushunchasi bilan darsni boshlash.
2. **Yangi mavzu: Xavfsizlikning 3 ustuni (20 daqiqa):**
   - Identifikatsiya (Identification) &mdash; "Siz kimsiz?" (Login/Email).
   - Autentifikatsiya (Authentication) &mdash; "Haqiqatan ham sizmisiz?" (Parol, SMS kod, Biometrika).
   - Avtorizatsiya (Authorization) &mdash; "Sizga nimalar qilishga ruxsat bor?" (Rollar, huquqlar).
3. **Yangi mavzu: Session vs Token vs JWT (25 daqiqa):**
   - Session-based auth: Cookielar, stateful arxitektura, xotira sarfi, mobil ilovalardagi qiyinchiliklar.
   - Token-based auth: DRF built-in TokenAuthentication, stateless afzalligi.
   - JSON Web Token (JWT): Uch qism (Header, Payload, Signature), Access va Refresh token ishlash mexanizmi, `rest_framework_simplejwt`.
4. **Amaliyot: Custom User modeli va JWT sozlash (15 daqiqa):**
   - Nega standart Django User emas, Custom User kerak? (`apps/accounts/models.py`).
   - `AUTH_USER_MODEL = "accounts.User"` sozlash.
   - Post va Comment modellariga `author` va `user` ForeignKey maydonlarini qo'shish.
   - Postman / Browsable API da token olish (`/api/v1/auth/jwt/create/`).
5. **Dars xulosasi va tezkor nazorat (10 daqiqa):** Savol-javob, o'quvchilarni baholash, uyga vazifa.

---

## Mentor konspekti

### 1. Identifikatsiya, Autentifikatsiya va Avtorizatsiya

Ko'pincha dasturchilar bu 3 tushunchani chalkashtirib yuborishadi:
- **Identifikatsiya:** Tizimga o'zini tanishtirish. Masalan, "Mening emailim `ali@mail.uz`".
- **Autentifikatsiya:** Shaxsning haqiqiyligini tekshirish. Masalan, kiritilgan parolni bazadagi shifrlangan hesh (`bcrypt` / `pbkdf2`) bilan solishtirish.
- **Avtorizatsiya:** Foydalanuvchining ma'lum bir amalni bajarishga huquqi bor-yo'qligini tekshirish. Masalan: "Ali oddiy foydalanuvchi, u boshqa birovning maqolasini o'chira olmaydi, faqat admin o'chira oladi".

### 2. Autentifikatsiya usullari: Session, Token va JWT

| Usul | Qayerda saqlanadi? | Afzalligi | Kamchiligi |
|---|---|---|---|
| **Session** | Server bazasida yoki xotirasida | Tokenni bekor qilish oson | Server xotirasini band qiladi, mobil ilovalar uchun noqulay |
| **Oddiy Token** | DB da bitta jadvalda | Oddiy va tushunarli | Har bir so'rovda DB ga token tekshirish uchun qo'shimcha so'rov boradi |
| **JWT** | Faqat foydalanuvchida (stateless) | DB ga so'rov yubormaydi, mikroservislar va mobil ilovalar uchun ideal | Muddati tugamaguncha to'xtatish murakkabroq |

### 3. JWT (JSON Web Token) anatomiyasi

JWT nuqta (`.`) bilan ajratilgan 3 qismdan iborat bo'ladi:
`xxxxx.yyyyy.zzzzz`
1. **Header (Sarlavha):** Token turi va shifrlash algoritmi (masalan, `HS256`).
2. **Payload (Yuk / Ma'lumot):** Foydalanuvchi ID si, emaili, tokenni berilgan vaqti va amal qilish muddati (`exp`).
3. **Signature (Raqamli imzo):** Serverning maxfiy kaliti (`SECRET_KEY`) orqali Header va Payload birlashtirilib hosil qilingan imzo. Birov payloadni o'zgartirsa, imzo buziladi va server so'rovni darhol rad etadi!

**Access va Refresh tokenlar juftligi:**
- **Access Token:** Qisqa muddat yashaydi (masalan, 15-30 daqiqa). Har bir API so'rovida `Authorization: Bearer <access_token>` shaklida yuboriladi.
- **Refresh Token:** Uzoq muddat yashaydi (masalan, 7-30 kun). Access token eskirganda, yangi access token olish uchun ishlatiladi (`/api/v1/auth/jwt/refresh/`).

### 4. Nega Custom User kerak?

Standart Django User modeli `username` (login) orqali ishlaydi. Zamonaviy tizimlarda esa ro'yxatdan o'tish va kirish **email** yoki **telefon raqam** orqali amalga oshiriladi.
Shuningdek, profilga avatar, telefon, tug'ilgan sana kabi qo'shimcha maydonlarni erkin qo'shish uchun loyihani boshidanoq `AbstractBaseUser` va `PermissionsMixin` asosida Custom User yaratish qat'iy tavsiya etiladi.

---

## Kod namunalari

### 1. `src/apps/accounts/models.py` (Custom User)

```python
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from apps.common.models import TimeStampedModel

class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str | None = None, **extra_fields):
        if not email:
            raise ValueError("Email kiritilishi shart")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email=email, password=password, **extra_fields)

class User(TimeStampedModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=160, blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list[str] = []

    def __str__(self) -> str:
        return self.email
```

### 2. Post va Comment modellariga muallifni ulash

```python
# src/apps/news/models.py (Post ichida)
from django.conf import settings

author = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.PROTECT,
    related_name="posts",
    blank=True,
    null=True,
)
```

### 3. JWT sozlamalari (`src/config/settings/base.py`)

```python
AUTH_USER_MODEL = "accounts.User"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
}

from datetime import timedelta
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "AUTH_HEADER_TYPES": ("Bearer",),
}
```

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq (Oson): Tushunchalarni ajratish
Quyidagi harakatlarning qaysi biri Identifikatsiya, qaysi biri Autentifikatsiya va qaysi biri Avtorizatsiya ekanligini aniqlang:
1. Foydalanuvchi saytga o'zining telefon raqamini kiritdi.
2. Foydalanuvchi telefoniga SMS orqali kelgan 6 xonali maxfiy kodni kiritdi.
3. Tizim foydalanuvchining o'qituvchi ekanligini bilib, unga jurnalga baho qo'yish imkoniyatini ochib berdi.

**Yechim:**
1. Identifikatsiya (o'z shaxsini e'lon qildi).
2. Autentifikatsiya (kod orqali haqiqatan telefon egasi ekanligini isbotladi).
3. Avtorizatsiya (huquq va vakolatlarini tekshirib ruxsat berdi).

### 2-topshiriq (O'rta): JWT Payload tarkibini tahlil qilish
Quyidagi dekodlangan JWT payloadida qanday ma'lumotlar borligini va `exp` maydoni nima maqsadda ishlatilishini tushuntiring:
```json
{
  "token_type": "access",
  "exp": 1791108000,
  "iat": 1791104400,
  "jti": "5a4f78c9d12345",
  "user_id": 42
}
```

**Yechim:**
- `token_type`: Token turi (qisqa muddatli access token).
- `user_id`: Tizimdagi 42-raqamli foydalanuvchining ID raqami.
- `iat` (issued at): Token qaysi Unix timestamp vaqtida berilganligi.
- `exp` (expiration time): Tokenning amal qilish muddati tugash vaqti. Ushbu vaqtdan so'ng token yaroqsiz bo'ladi va server uni qabul qilmaydi (`401 Unauthorized`).
- `jti`: Tokenning takrorlanmas noyob identifikatori.

### 3-topshiriq (Qiyin): So'rov sarlavhasida JWT yuborish
Foydalanuvchi yangi maqola chop etish uchun `POST /api/v1/posts/` manziliga so'rov yubormoqda. U o'zining JWT tokenini so'rov sarlavhasida (Headers) qanday formatda yuborishi kerak? Curl va Python Requests kutubxonasida ushbu so'rov sarlavhasini yozing.

**Yechim:**
HTTP Sarlavha formati:
`Authorization: Bearer <TOKEN_QIYMATI>`

Python Requests kodi:
```python
import requests

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}
data = {
    "title": "Yangi yangilik",
    "body": "Maqola matni",
    "category": 1
}
response = requests.post("http://127.0.0.1:8000/api/v1/posts/", json=data, headers=headers)
```

---

## Tezkor nazorat savollari

1. Autentifikatsiya va Avtorizatsiya orasidagi tub farq nima?
   - **Javob:** Autentifikatsiya — shaxsning kimligini tekshirish; Avtorizatsiya — unga qaysi amallarga ruxsat borligini aniqlash.
2. JWT tarkibidagi 3 ta qism nimalardan iborat?
   - **Javob:** Header (algoritm), Payload (ma'lumotlar), Signature (raqamli imzo).
3. Nima sababdan Access tokenning muddati qisqa (masalan 15-60 daqiqa) qilib belgilanadi?
   - **Javob:** Agar token xakerlar qo'liga tushib qolsa, zararni minimallashtirish uchun; muddati tezda tugab, yaroqsiz bo'ladi.
4. Refresh token nima uchun kerak?
   - **Javob:** Access token eskirganda, foydalanuvchini har 15 daqiqada qayta parol terishga majburlamasdan, yangi access token olish uchun.
5. `AUTH_USER_MODEL` sozlamasining vazifasi nima?
   - **Javob:** Djangoning standart User modeli o'rniga o'zimiz yaratgan Custom User modelini asosiy deb e'lon qilish.

---

## Uyga vazifa

1. `src/apps/accounts/models.py` da `User` va `UserManager` klasslarini yozing.
2. `settings/base.py` faylida `AUTH_USER_MODEL = "accounts.User"` ni belgilang va `rest_framework_simplejwt` kutubxonasini o'rnating.
3. Terminalda `makemigrations` va `migrate` buyruqlarini bering, so'ng `python manage.py createsuperuser` orqali yangi admin yarating.
