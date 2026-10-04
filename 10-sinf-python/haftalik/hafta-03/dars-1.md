# 7-dars. Pagination va throttling

## Dars rejasi (80 daqiqa)

1. **O'tgan haftani takrorlash va kirish (10 daqiqa):** DRF Permissions, `IsOwnerOrStaff`, `django-filter` va qidiruv bo'yicha qisqa so'rov. Katta hajmdagi ma'lumotlar muammosi.
2. **Yangi mavzu: Pagination (Sahifalash) mexanizmi (25 daqiqa):**
   - Nima uchun barcha ma'lumotlarni birdaniga berish xato? (Server xotirasi, tarmoq tiqilishi, brauzer qotishi).
   - Pagination turlari: `PageNumberPagination`, `LimitOffsetPagination`, `CursorPagination`.
   - `apps/common/pagination.py`: `DefaultPageNumberPagination` (sahifa o'lchami 10 ta, maksimal 100 ta).
   - Standart JSON formati: `count`, `next`, `previous`, `results`.
3. **Yangi mavzu: Throttling (Rate Limiting) va API xavfsizligi (25 daqiqa):**
   - Throttling nima: DoS hujumi, botlar va parollarni topish (brute-force) xavfi.
   - Anonim va autentifikatsiyalangan foydalanuvchilar limitlari (`AnonRateThrottle`, `UserRateThrottle`).
   - `DEFAULT_THROTTLE_RATES`: `anon: "60/min"`, `user: "300/min"`.
   - Login uchun maxsus cheklov: `LoginAnonThrottle` (`10/min`).
   - `429 Too Many Requests` status kodi va kutish vaqti (`Retry-After`).
4. **Amaliyot: Pagination va Throttlingni sinash (10 daqiqa):**
   - Brauzer va curl orqali `?page=2&page_size=5` so'rovlarini yuborish.
   - Ketma-ket tezkor so'rovlar yuborib, `429 Too Many Requests` javobini olish.
5. **Dars xulosasi va tezkor nazorat (10 daqiqa):** Savol-javob, o'quvchilarni baholash, uyga vazifa.

---

## Mentor konspekti

### 1. Pagination: Nima va nega kerak?

**Muammo:** NewsPortal loyihasida 50 000 ta maqola va 200 000 ta izoh to'plandi.
Agar frontend ilova `GET /api/v1/posts/` so'rovini yuborsa va server barcha 50 000 ta postni bitta ulkan JSON qilib (masalan, 80 Megabayt) qaytarsa:
- Ma'lumotlar bazasi barcha qatorlarni o'qish uchun og'ir yuk ostida qoladi;
- Serverning operativ xotirasi (RAM) to'lib qoladi;
- Foydalanuvchining mobil internet trafigi bir zumda tugaydi;
- Brauzer bunday ulkan JSON-ni chizishga harakat qilib butunlay qotib qoladi (crash).

**Yechim:** Ma'lumotlarni qismlarga bo'lib (masalan, har safar 10 tadan) uzatish — bu **Pagination** deb ataladi.

### 2. Pagination turlari

1. **PageNumberPagination (Sahifa raqami bo'yicha):**
   - Eng ommabop va tushunarli usul: `?page=2&page_size=10`.
   - Mijozga umumiy soni (`count`), keyingi sahifa havolasi (`next`), oldingi sahifa havolasi (`previous`) va joriy ro'yxat (`results`) qaytariladi.
2. **LimitOffsetPagination:**
   - SQL `LIMIT` va `OFFSET` buyruqlariga asoslanadi: `?limit=10&offset=20` (20-yozuvdan boshlab 10 ta ma'lumot).
3. **CursorPagination:**
   - Sahifa raqami emas, maxsus shifrlangan kursor (token) orqali ishlaydi. Ma'lumotlar bazasida har soniyada yangi postlar qo'shilib turadigan ijtimoiy tarmoqlar tasmasi (Infinite Scroll) uchun eng barqaror va tezkor usul.

### 3. Throttling (Rate Limiting) nima?

**Throttling** — bu bir foydalanuvchi yoki IP manzilning ma'lum vaqt oralig'ida (masalan, 1 daqiqada) serverga yuborishi mumkin bo'lgan maksimal so'rovlar sonini cheklash mexanizmidir.

**Nima uchun kerak?**
- **DoS/DDoS hujumlaridan himoya:** Botlar soniyasiga yuzlab so'rovlar yuborib serverni ishdan chiqarishining oldini oladi.
- **Brute-Force hujumidan himoya:** Xakerlar login sahifasiga sekundiga minglab parollarni tekshirib ko'rishini to'xtatadi.
- **Server resurslarini adolatli taqsimlash:** Bitta mijoz barcha server quvvatini band qilib qo'ymasligi uchun.

Agar belgilangan limitdan oshib ketsa, server darhol `429 Too Many Requests` xatosini qaytaradi:
```json
{
  "detail": "Request was throttled. Expected available in 45 seconds."
}
```

---

## Kod namunalari

### 1. `src/apps/common/pagination.py`

```python
from rest_framework.pagination import PageNumberPagination

class DefaultPageNumberPagination(PageNumberPagination):
    """
    Standart sahifalash:
    - ?page=1
    - ?page_size=10
    Maksimal ruxsat etilgan hajm: 100
    """
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100
```

### 2. Sozlamalar: Pagination va Throttling (`src/config/settings/base.py`)

```python
REST_FRAMEWORK = {
    # ... avvalgi sozlamalar

    # Global Pagination
    "DEFAULT_PAGINATION_CLASS": "apps.common.pagination.DefaultPageNumberPagination",
    "PAGE_SIZE": 10,

    # Global Throttling
    "DEFAULT_THROTTLE_CLASSES": (
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ),
    "DEFAULT_THROTTLE_RATES": {
        "anon": "60/min",        # Ro'yxatdan o'tmaganlar: minutiga 60 ta
        "user": "300/min",       # Tizimga kirganlar: minutiga 300 ta
        "login_anon": "10/min",  # Login sahifasi: minutiga 10 ta
    },
}
```

### 3. Login uchun maxsus Throttling (`src/apps/accounts/throttles.py`)

```python
from rest_framework.throttling import AnonRateThrottle

class LoginAnonThrottle(AnonRateThrottle):
    scope = "login_anon"
```

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq (Oson): Pagination javob strukturasini tahlil qilish
Quyidagi JSON javobida qaysi maydonlar borligini va ular nimani anglatishini tushuntiring:
```json
{
  "count": 45,
  "next": "http://127.0.0.1:8000/api/v1/posts/?page=3",
  "previous": "http://127.0.0.1:8000/api/v1/posts/?page=1",
  "results": [...]
}
```

**Yechim:**
- `count: 45` &mdash; Bazadagi ushbu mezonlarga mos barcha maqolalarning umumiy soni (45 ta).
- `next` &mdash; Keyingi 3-sahifani olish uchun to'liq URL havolasi (agar oxirgi sahifa bo'lsa `null`).
- `previous` &mdash; Oldingi 1-sahifaga qaytish havolasi (agar 1-sahifa bo'lsa `null`).
- `results` &mdash; Joriy sahifaga tegishli bo'lgan 10 ta maqolaning to'liq ma'lumotlar massivi.

### 2-topshiriq (O'rta): Maxsus sahifalash klassi
Mobil ilovalar uchun bitta sahifada 20 tadan post chiqaradigan va mijoz xohlasa maksimal 50 tagacha so'ray oladigan `MobilePostPagination` klassini yozing.

**Yechim:**
```python
from rest_framework.pagination import PageNumberPagination

class MobilePostPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 50
```

### 3-topshiriq (Qiyin): Throttling so'rovini tekshirish
Foydalanuvchi `anon` cheklovi (60 ta so'rov/daqiqa) bo'lgan endpointga 1 daqiqa ichida ketma-ket 65 ta so'rov yubordi.
1. Dastlabki 60 ta so'rovda qanday status qaytadi?
2. 61-so'rovdan boshlab server qanday HTTP status kodi va qanday JSON xabar qaytaradi?
3. Server bu vaqtni qayerda (xotirada) hisoblab boradi?

**Yechim:**
1. Dastlabki 60 ta so'rovga `200 OK` (muvaffaqiyatli) qaytadi.
2. 61-so'rovdan boshlab server `429 Too Many Requests` status kodi bilan `{"detail": "Request was throttled. Expected available in X seconds."}` xabarini qaytaradi.
3. DRF throttling vaqt va so'rovlar sonini keshlash (Cache) tizimida (local developmentda `LocMemCache`, productionda esa `Redis`) saqlab hisoblaydi.

---

## Tezkor nazorat savollari

1. Nima uchun yirik tizimlarda Pagination ishlatilishi majburiydir?
   - **Javob:** Server xotirasini tejash, tarmoq trafigini kamaytirish va brauzer qotib qolmasligi uchun.
2. `PageNumberPagination` da mijoz keyingi sahifani qanday query parametri bilan so'raydi?
   - **Javob:** `?page=2` (yoki `?page=3`) parametri orqali.
3. Throttling nima va u serverni qanday tahdidlardan himoya qiladi?
   - **Javob:** Vaqt birligida keladigan so'rovlar sonini cheklash mexanizmi; DoS hujumlari va parollarni topish (brute-force) dan himoyalaydi.
4. Agar belgilangan so'rovlar chegarasidan oshib ketsa, qanday HTTP status qaytariladi?
   - **Javob:** `429 Too Many Requests`.
5. Nega login sahifasi uchun global limitdan ko'ra qattiqroq limit (`login_anon: 10/min`) qo'yiladi?
   - **Javob:** Xakerlar foydalanuvchilar hisobiga parollarni ketma-ket tanlash orqali buzib kirmasligi (brute-force) uchun.

---

## Uyga vazifa

1. `src/apps/common/pagination.py` modulida `DefaultPageNumberPagination` klassini yarating.
2. `settings/base.py` fayliga `DEFAULT_PAGINATION_CLASS` va `DEFAULT_THROTTLE_CLASSES` sozlamalarini qo'shing.
3. Brauzerda `http://127.0.0.1:8000/api/v1/posts/?page=1&page_size=3` so'rovini yuborib, JSON javobida `count`, `next`, `previous` maydonlari to'g'ri chiqayotganini tekshiring.
