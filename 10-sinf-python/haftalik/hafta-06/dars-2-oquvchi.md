# 17-dars. Loyihani yakunlash

> Loyiha ishlaydi, lekin tayyormi? Bugun uni tartibga solamiz: sozlamalar, xato formati, CORS, testlar va migratsiya.

## Dars xulosasi

- Loyiha mantiqiy papkalarga bo'linadi.
- Sozlamalar `.env` da, `Settings` orqali o'qiladi.
- `.env` GitHub ga yuborilmaydi; `.env.example` qo'yiladi.
- Xatolar `exception_handler` bilan bir xil JSON qaytadi.
- CORS faqat kerakli manzillarga ruxsat beradi.
- `pytest` va `alembic upgrade head` — yakuniy tekshiruv.

## Qo'shimcha ma'lumot

### Middleware
Har so'rov va javob orasidagi umumiy qatlam.

### OpenAPI
Swagger va ReDoc manbai bo'lgan hujjat standarti.

### dev/test/prod
Uch muhit: faqat `.env` qiymatlari farq qiladi.

### Health check
Ilova tirikligini tekshiruvchi endpoint.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Settings | Sozlamalar sinfi |
| .env | Muhit o'zgaruvchilari fayli |
| CORS | Origin lar siyosati |
| Middleware | Oraliq qatlam |
| Exception handler | Xato ishlovchi |
| pytest | Test kutubxonasi |
| alembic | Migratsiya vositasi |
| OpenAPI | API hujjat standarti |

## Bilasizmi?

- Ko'p loyihalarda `Settings` ni `lru_cache` bilan bir marta yaratishadi.
- `.env.example` yangi dasturchiga qaysi sozlamalar kerakligini ko'rsatadi.
- Swagger va ReDoc bitta OpenAPI hujjatidan avtomatik yasaladi.

## Topshiriqlar

### 1. Settings · oson

`Settings` sinfida 2 ta maydon yozing.

**Kutiladigan natija:** `app_name`, `debug`.

### 2. `.env` · oson

`.env` da qaysi 2 ma'lumot saqlanadi?

**Kutiladigan natija:** `DATABASE_URL`, `SECRET_KEY`.

### 3. `.gitignore` · oson

`.env` ni nega `.gitignore` ga qo'shamiz?

**Kutiladigan natija:** Maxfiy qiymatlar sizib chiqmasligi uchun.

### 4. Hujjat · oson

Swagger va ReDoc manzillarini yozing.

**Kutiladigan natija:** `/docs`, `/redoc`.

### 5. Handler · o'rta

404 uchun bir xil formatli handler yozing.

**Kutiladigan natija:** `exception_handler(HTTPException)`.

### 6. CORS · o'rta

CORS ga bitta manzil qo'shing.

**Kutiladigan natija:** `allow_origins=[...]`.

### 7. Test · o'rta

`/health` testini yozing.

**Kutiladigan natija:** 200 va `{"status": "ok"}`.

### 8. Struktura · o'rta

Papka strukturasini chizing.

**Kutiladigan natija:** app/, core/, models/, schemas/, routers/, tests/.

### 9. Xato formati · qiyin

422 xatosini `fields` ro'yxati bilan qaytaring.

**Kutiladigan natija:** `RequestValidationError` handler.

### 10. Env farqi · qiyin

Dev va prod uchun `.env` farqini tushuntiring.

**Kutiladigan natija:** Faqat qiymatlar farq qiladi.

### 11. Migratsiya · qiyin

`alembic upgrade head` va `current` farqi?

**Kutiladigan natija:** Birinchisi qo'llaydi, ikkinchisi joriyni ko'rsatadi.

### 12. Checklist · bonus

Loyiha uchun 8 bandli checklist tuzing.

**Kutiladigan natija:** To'liq checklist.

## O'zingizni tekshiring

1. Sozlamalar qayerda?
2. `.env` GitHub da bo'ladimi?
3. Exception handler nima?
4. CORS nima?
5. `pytest` nima uchun?
6. `alembic upgrade head`?

## Uyga vazifa

Book loyihasini yakunlang (40 daqiqa). To'liq shart: `uyga-vazifa.md`.
