# 17-dars. Loyihani yakunlash

## Dars rejasi (80 daqiqa)

**Maqsad:** Loyihani yakuniy holatga keltirishni o'rgatish: papka strukturasi, `.env` va `Settings` (pydantic-settings), xato javoblarini bir xil formatga keltiruvchi `exception_handler`, `CORS` sozlamasi, Swagger/ReDoc hujjatlari, `pytest` bilan testlar va `alembic upgrade head`.

**Manba:** `oquv-dasturi.txt` (Loyihani yakunlash: kodni tozalash, `.env` va `settings.py`, xatoliklar va javob formatlari, Swagger va ReDoc, alembic upgrade; CORS, middleware, exception handler; dev/test/prod konfiguratsiya). Kod namunalari FastAPI, pydantic-settings va pytest bilan sinab ko'rilgan.

**Kutiladigan natija:** o'quvchi (1) Loyiha papkalarini mantiqiy tuzilmaga keltiradi; (2) `.env` va `Settings` sinfi orqali sozlamalarni o'qiydi; (3) `HTTPException` va validatsiya xatolarini bir xil JSON formatda qaytaradi; (4) CORS ni ruxsat etilgan manzillar bilan sozlaydi; (5) `pytest` bilan 3 ta test yozadi va `alembic upgrade head` ni ishga tushiradi.

| Vaqt | Bosqich |
|---|---|
| 10 daq | Takrorlash: 16-dars: fayl yuklash va yuklab olish |
| 30 daq | Yangi mavzu: Struktura va `Settings` (`.env`); Xatolar standarti va CORS |
| 5 daq | Tanaffus |
| 20 daq | Amaliyot: Hujjat (Swagger), testlar va migratsiya |
| 10 daq | Xavfsizlik va xulosa: Yakuniy tekshiruv ro'yxati (checklist) |
| 5 daq | Xulosa, tezkor nazorat, uyga vazifa |

---

## Mentor konspekti

### 1. Loyiha strukturasi va sozlamalar
Loyiha tayyor bo'lganda kod tartibli bo'lishi kerak: `app/` ichida `main.py` (ilova), `core/` (sozlamalar), `models/`, `schemas/`, `routers/`, `services/` yoki `crud/`, `tests/`. Sozlamalar (`DATABASE_URL`, maxfiy kalit, CORS) kod ichida emas, **`.env`** faylida turadi va **`Settings`** sinfi orqali o'qiladi (`pydantic-settings`). `.env` ni `.gitignore` ga qo'shing, GitHub ga hech qachon yubormang; o'rniga `.env.example` (qiymatlarsiz) qo'ying. Dev, test va prod muhitlar uchun faqat `.env` qiymatlari farq qiladi.

`.env` da `DEBUG=true` yoki `CORS_ORIGINS=["https://sayt.uz"]` kabi yoziladi. Maxfiy qiymatlar kodda va GitHub da bo'lmasin.

### 2. Xatoliklarni standartlash va CORS
Mijoz (frontend) har xil xato shaklini kutmaydi: hamma xato bir xil JSON bo'lsa, ishlash oson. `@app.exception_handler(HTTPException)` va `RequestValidationError` uchun handler yozib, javobni `{"error": {"status": ..., "message": ...}}` ko'rinishiga keltiramiz. **CORS** — brauzer boshqa manzildagi (masalan frontend `localhost:3000`) saytning API ga so'rov yuborishiga ruxsat. `CORSMiddleware` da `allow_origins` ga faqat kerakli manzillarni yozing; ishlab chiqarishda `["*"]` ishlatmang.

Validatsiya xatosi uchun ham (`RequestValidationError`) shunday handler yozing va `422` qaytaring.

### 3. Swagger hujjati, testlar va alembic
`FastAPI(title=..., version=..., description=...)` va `tags=[...]` Swagger (`/docs`) va ReDoc (`/redoc`) ni tushunarli qiladi: endpointlar guruhlanadi, tavsif yoziladi. Keyin testlar: `TestClient` va `pytest` bilan kamida sog'liq tekshiruvi (`/health`), xato formati va asosiy CRUD. Bazaga kelsak, hamma migratsiyalar tekshiriladi va yakunda **`alembic upgrade head`** bajariladi: baza modellar bilan bir xil bo'ladi. Oxirida checklist: testlar yashil, `.env` yo'q GitHub da, README da ishga tushirish yo'riqnomasi bor.

Terminalda `pytest -q` va `alembic upgrade head`. `alembic current` joriy migratsiyani ko'rsatadi.

---

## Kod namunalari

### 1. Yakuniy main.py (sinab ko'rilgan)
```python
from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core import settings

app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    description="Kitoblar API: CRUD, qidiruv, fayllar.",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(HTTPException)
async def http_error(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": {"status": exc.status_code, "message": exc.detail}},
    )


@app.exception_handler(RequestValidationError)
async def validation_error(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"error": {"status": 422, "message": "Noto'g'ri ma'lumot",
                           "fields": [e["loc"][-1] for e in exc.errors()]}},
    )


@app.get("/health", tags=["system"])
async def health():
    return {"status": "ok"}
```

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq (Oson): Settings
`app_name` va `debug` maydonli `Settings` yozing.

**Yechim:** 
```python
class Settings(BaseSettings):
    app_name: str = "Book API"
    debug: bool = False
```

### 2-topshiriq (Oson): `.env.example`
Maxfiy qiymatsiz `.env.example` namunasini yozing.

**Yechim:** 
```python
DATABASE_URL=
SECRET_KEY=
DEBUG=false
```

### 3-topshiriq (O'rta): Handler
404 xatosini `{"error": ...}` formatida qaytaring.

**Yechim:** 
```python
@app.exception_handler(HTTPException)
async def http_error(request, exc):
    return JSONResponse(status_code=exc.status_code,
        content={"error": {"status": exc.status_code, "message": exc.detail}})
```

### 4-topshiriq (O'rta): CORS
Faqat `http://localhost:3000` ga ruxsat bering.

**Yechim:** 
```python
app.add_middleware(CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"], allow_headers=["*"])
```

### 5-topshiriq (Qiyin): Test
`/health` uchun test yozing.

**Yechim:** 
```python
def test_health():
    r = client.get("/health")
    assert r.status_code == 200
```

### 6-topshiriq (Qo'shimcha): Hujjat
Swagger da endpointlarni `tags` bilan guruhlang.

**Yechim:** `@app.get("/health", tags=["system"])`; `FastAPI(title=..., version=...)`.

---

## Tezkor nazorat savollari

1. Sozlamalar qayerda saqlanadi?
   - **Javob:** `.env` faylida, `Settings` orqali o'qiladi.
2. `.env` GitHub ga yuboriladimi?
   - **Javob:** Yo'q; `.gitignore` ga qo'shiladi.
3. Exception handler nima uchun?
   - **Javob:** Xatolarni bir xil formatda qaytarish uchun.
4. CORS nima?
   - **Javob:** Boshqa manzildan so'rovga ruxsat siyosati.
5. `alembic upgrade head`?
   - **Javob:** Bazani oxirgi migratsiyaga ko'taradi.

---

## Uyga vazifa

`uyga-vazifa.md` ga qarang.
