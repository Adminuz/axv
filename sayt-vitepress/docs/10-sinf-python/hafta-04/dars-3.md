---
title: "12-dars. FastAPI loyiha yaratish. Loyiha uchun MB ni loyihalash va yaratish, dastlabki sozlamalar"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (Python)", "link": "/10-sinf-python/"}, "week": {"n": 4, "link": "/10-sinf-python/hafta-04/"}, "g": 12, "title": "FastAPI loyiha yaratish. Loyiha uchun MB ni loyihalash va yaratish, dastlabki sozlamalar", "lead": "Django dan keyin yangi sarguzasht: FastAPI! Bugun noldan E-Library loyihasining poydevorini quramiz: papkalar, baza dizayni, sozlamalar va birinchi ishlaydigan /health endpoint.", "slide": "/slaydlar/10-sinf-python/hafta-04/dars-3.html", "test": "/slaydlar/10-sinf-python/hafta-04/dars-3-test.html", "tabs": [{"g": 10, "link": "/10-sinf-python/hafta-04/dars-1", "current": false}, {"g": 11, "link": "/10-sinf-python/hafta-04/dars-2", "current": false}, {"g": 12, "link": "/10-sinf-python/hafta-04/dars-3", "current": true}], "prev": {"g": 11, "title": "Tayyor loyihani hostingga joylash (deploy)", "link": "/10-sinf-python/hafta-04/dars-2"}, "next": null}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **FastAPI** — zamonaviy, yuqori unumdor, asinxron (async/await) Python freymvorki.
- Uni **Uvicorn** (ASGI server) ishga tushiradi.
- Har bir loyiha **virtual muhit (venv)** da boshlanadi.
- Kod yozishdan oldin **mini texnik topshiriq (TT)** yoziladi: maqsad, rollar, funksiyalar, talablar.
- Loyiha qatlamlarga bo'linadi: `routes`, `schemas`, `services`, `models`, `core`.
- Baza avval «qog'ozda» loyihalanadi: jadvallar, PK/FK va bog'lanishlar (1:1, 1:N, M:N).
- Sozlamalar `.env` va Pydantic `Settings` orqali o'qiladi; migratsiyalarni **Alembic** boshqaradi.
- Tekshiruv: `uvicorn app.main:app --reload`, `/health` va Swagger (`/docs`).

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Nega TT dan boshlaymiz?
Uy qurishdan oldin chizma chiziladi. TT ham shunday chizma: nima quramiz (maqsad), kim foydalanadi (rollar), nimalar bo'ladi (MVP funksiyalar), qanday sifatda (nofunksional talablar). MVP — eng kichik ishlaydigan variant.

### 2. Kitob javonidagi tartib: qatlamlar
Kutubxonani tasavvur qiling: qabul stoli (routes) so'rovni oladi, kartochka shakli (schemas) ma'lumot qanday ko'rinishini belgilaydi, kutubxonachi (services) qoidalarni tekshiradi, javon (models) kitoblarni saqlaydi, ombor sozlamalari (core) umumiy narsalarni boshqaradi. Hammasini bitta odam qilsa (monolit `main.py`), chalkashlik boshlanadi.

### 3. Bog'lanish: 1:N
Bitta foydalanuvchi ko'p kitob qo'shadi, lekin kitobning egasi bitta. Shuning uchun `books` jadvalida `owner_id` (Foreign Key) bo'ladi.

```python
# books jadvali (soddalashtirilgan)
# id           PK
# title        NOT NULL
# owner_id     FK -> users.id
# category_id  FK -> categories.id
```

### 4. `engine` va `session` farqi
`engine` — bazaga doimiy aloqa kanali (yo'l). `AsyncSessionLocal` — har bir so'rov uchun ochiladigan vaqtincha muloqot sessiyasi (yo'lda yuruvchi mashina). `get_db()` har so'rovga sessiya beradi.

### 5. Odatiy xatolar
- `.env` yaratishni unutish: `Settings()` xato beradi.
- Venv faollashtirilmasdan `pip install` qilish (kutubxonalar global tizimga tushadi).
- `.env` ni GitHub ga yuklash.
- `alembic.ini` ga baza URL ni yozib qo'yish (to'g'risi: `settings` dan o'qish).
- Modellarni `app/models/__init__.py` da import qilmaslik: `--autogenerate` ularni ko'rmaydi.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| FastAPI | Asinxron Python veb-freymvork |
| Uvicorn | FastAPI uchun ASGI server |
| venv | Loyiha uchun izolyatsiyalangan Python muhiti |
| TT | Texnik topshiriq: loyiha talablari hujjati |
| MVP | Minimal ishlaydigan birinchi variant |
| Primary Key (PK) | Qatorni yagona aniqlovchi kalit |
| Foreign Key (FK) | Boshqa jadvalga ishora qiluvchi kalit |
| ORM | Obyekt-relyatsion moslashtirish: SQL o'rniga Python klasslari |
| Alembic | Baza migratsiyalarini boshqarish vositasi |
| Pydantic | Ma'lumotni tekshiruvchi va sozlamalarni o'qiydigan kutubxona |
| Swagger | `/docs` dagi avtomatik interaktiv API hujjati |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Qo'llanma bo'yicha FastAPI Pydantic yordamida `.env` o'zgaruvchilarini avtomatik Python obyektiga o'giradi va tekshiradi.
- Ruff bitta vosita ichida flake8, isort va format vazifalarini bajaradi.
- UUID identifikatorini taxmin qilish integer ID ga qaraganda ancha qiyin; shuning uchun API larda qulay.
- Maxfiy ma'lumotni kodga yozmaslik «12-Factor App» metodologiyasining talabi.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Qatlamlarni tushuntiring <Badge type="tip" text="oson" />
`routes`, `schemas`, `services`, `models`, `core` papkalari nima uchun xizmat qiladi? Har biriga bir jumla yozing.

**Kutiladigan natija:** 5 ta to'g'ri jumla.

### 2. Atamalarni juftlang <Badge type="tip" text="oson" />
PK, FK, ORM, Alembic va ularning ma'nolarini («yagona kalit», «boshqa jadvalga ishora», «migratsiya», «SQL o'rniga klasslar») juftlang.

**Kutiladigan natija:** 4 ta to'g'ri juftlik.

### 3. Bog'lanish turi <Badge type="tip" text="oson" />
Quyidagilar qaysi turga kiradi: foydalanuvchi va pasport, foydalanuvchi va postlar, talabalar va fanlar.

**Kutiladigan natija:** 1:1, 1:N, M:N (bog'lovchi jadval bilan).

### 4. Venv buyruqlari <Badge type="tip" text="oson" />
Venv yarating, faollashtiring va FastAPI bilan Uvicorn ni o'rnating. Buyruqlarni ketma-ket yozing.

**Kutiladigan natija:** `python -m venv .venv`, faollashtirish, `pip install fastapi "uvicorn[standard]"`.

### 5. Mini TT yozing <Badge type="warning" text="o'rta" />
O'zingiz tanlagan loyiha (masalan, «Maktab olimpiadalari») uchun mini TT: maqsad, rollar, MVP funksiyalar, nofunksional talablar.

**Kutiladigan natija:** Kamida 4 bo'limli bir betlik TT.

### 6. ER dizayn chizing <Badge type="warning" text="o'rta" />
O'z loyihangiz uchun kamida 2 ta jadvalni PK, FK va maydon turlari bilan chizing (qog'ozda yoki draw.io da).

**Kutiladigan natija:** Diagramma 1:N bog'lanishi bilan.

### 7. Bu kod nima qaytaradi? <Badge type="warning" text="o'rta" />
```python
@app.get("/health", tags=["system"])
async def healthcheck() -> dict:
    return {"status": "ok"}
```
`GET /health` qanday javob beradi va `tags=["system"]` Swagger da nimani o'zgartiradi?

**Kutiladigan natija:** `{"status": "ok"}`; Swagger da endpoint «system» guruhida ko'rinadi.

### 8. Xatoni toping <Badge type="warning" text="o'rta" />
`Settings()` ishga tushganda `field required` xatosi chiqdi. Sabablarni va yechimni yozing.

**Kutiladigan natija:** `.env` fayli yo'q yoki o'zgaruvchi yetishmaydi (masalan `DB_NAME`); `.env.example` dan nusxa olib to'ldirish.

### 9. `.env` va config <Badge type="danger" text="qiyin" />
`.env.example` va `Settings` klassini o'z loyihangiz uchun yozing, `database_url` property sini qo'shing.

**Kutiladigan natija:** `settings.database_url` `postgresql+asyncpg://...` ko'rinishida chiqadi.

### 10. Skeleton ni ishga tushiring <Badge type="danger" text="qiyin" />
`app/core/config.py`, `app/core/database.py`, `app/main.py` ni yozing va `uvicorn app.main:app --reload` ni ishga tushiring.

**Kutiladigan natija:** `http://127.0.0.1:8000/health` va `/docs` ochiladi.

### 11. PostgreSQL ni ulash <Badge type="danger" text="qiyin" />
PostgreSQL ni Docker yoki lokal usulda ishga tushiring va `.env` orqali ulanish ma'lumotlarini kiriting.

**Kutiladigan natija:** `docker ps` da konteyner ko'rinadi; ilova xatosiz ishga tushadi.

### 12. Alembic ni tayyorlash <Badge type="info" text="bonus" />
`alembic init alembic` ni bajaring va `env.py` ni async engine hamda `target_metadata = Base.metadata` bilan moslang.

**Kutiladigan natija:** `alembic.ini` da baza URL yo'q, `env.py` `settings.database_url` dan foydalanadi.

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. FastAPI ga nega ASGI server kerak?
2. Venv yaratmasdan boshlash qanday muammolarga olib keladi?
3. `.env` fayli nima uchun kerak?
4. `models` va `schemas` farqi nimada?
5. One-to-Many bog'lanish bazada qanday amalga oshadi?
6. ORM ning xavfsizlik jihatidan ustunligi nima?
7. Nega jadvalga ustun qo'shishda Alembic ishlatiladi?
8. `engine` va `AsyncSessionLocal` farqini ayting.

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

(20-30 daqiqa) O'z FastAPI loyihangizni tanlang, mini TT yozing, MB ni loyihalang va skeleton (`/health`) ni yarating. To'liq ro'yxat: `uyga-vazifa.md`.

</div>

