# 12-dars. FastAPI loyiha yaratish. Loyiha uchun MB ni loyihalash va yaratish, dastlabki sozlamalar

## Dars rejasi (80 daqiqa)

**Maqsad:** o'quvchi FastAPI loyihasini texnik topshiriq (TT) asosida rejalashtiradi, papkalar tuzilmasini quradi, ER konsepti bo'yicha MB ni loyihalaydi, PostgreSQL, `.env`, config, async DB session va Alembic ni sozlaydi hamda `/health` va Swagger orqali tekshiradi.

**Kutiladigan natija:** o'quvchi (1) mini TT yozadi; (2) `app/` qatlamlarini (routes, schemas, services, models, core) ajratadi; (3) 1:N bog'lanishli jadvallarni loyihalaydi; (4) venv, kutubxonalar, `.env`, `Settings`, `get_db`, `main.py` ni yaratadi; (5) `uvicorn app.main:app --reload` bilan loyihani ishga tushiradi.

| Vaqt | Bosqich |
|---|---|
| 10 daq | Takrorlash: DRF dan FastAPI ga ko'prik, Django `settings` va `.env` |
| 30 daq | Yangi mavzu: FastAPI, Uvicorn/ASGI, TT, arxitektura, ER dizayn |
| 5 daq | Tanaffus |
| 20 daq | Amaliyot: venv, kutubxonalar, `.env`, config, DB session, `main.py` |
| 10 daq | Alembic init, ishga tushirish va Swagger tekshiruvi |
| 5 daq | Xulosa, tezkor nazorat, uyga vazifa |

---

## Mentor konspekti

### 1. FastAPI va ishchi muhit
- FastAPI — zamonaviy, yuqori unumdor, asinxron (async/await) Python freymvorki. REST API yaratish uchun.
- **Uvicorn** — ASGI server. Asinxron FastAPI ga an'anaviy WSGI emas, tezkor ASGI server kerak.
- **Virtual muhit (venv):** loyiha uchun alohida izolyatsiyalangan papka; turli loyihalar kutubxona versiyalari to'qnashmasligi uchun.

```bash
mkdir e_library && cd e_library
python -m venv .venv
source .venv/bin/activate        # Windows: .\.venv\Scripts\activate
python -m pip install -U pip
pip install fastapi "uvicorn[standard]" sqlalchemy asyncpg alembic pydantic-settings
pip install "python-jose[cryptography]" "passlib[bcrypt]" python-multipart
pip install ruff mypy            # dev tools
```

### 2. Mini texnik topshiriq (TT): «E-Library API» (MVP)
- **Maqsad:** ro'yxatdan o'tgan foydalanuvchilar elektron kitoblarni joylashtiradi, ko'radi va boshqaradi (CRUD).
- **Rollar:** Guest (faqat `is_published=True` kitoblarni ko'radi), User (kitob qo'shadi, o'zinikini tahrirlaydi/o'chiradi, fayl yuklaydi), Admin (keyingi iteratsiya, modelda `is_admin`).
- **Funksiyalar:** Auth (register, login (JWT), me), Category CRUD, Book (list/detail, create/update/delete faqat owner, file upload/download, search/filter/pagination keyingi mavzularda).
- **Nofunksional talablar:** yengil Clean Architecture (router -> service -> repository/db), PEP8 va typed hints, `.env` orqali config, Alembic migratsiya, Async SQLAlchemy.

### 3. Loyiha arxitekturasi (qatlamlar)
| Papka | Vazifasi |
|---|---|
| `routes/` | HTTP qatlami (request/response, status code) |
| `schemas/` | Pydantic DTO (kirish/chiqish) |
| `services/` | Biznes mantiq (ruxsat, validatsiya) |
| `models/` | SQLAlchemy ORM (baza) |
| `core/` | config, DB session, security, umumiy yordamchilar |

Tamoyil: **Separation of Concerns**. Monolit `main.py` (hammasi bitta faylda) — yomon; modulli tuzilma — yaxshi.

### 4. MB dizayni (ER konsept)
- Asosiy tushunchalar: Table, Column, Primary Key (PK), Foreign Key (FK).
- Bog'lanishlar: One-to-One (1:1), One-to-Many (1:N), Many-to-Many (M:N, bog'lovchi jadval orqali).
- Loyiha: `users (1) - (N) books`, `categories (1) - (N) books`.

| Jadval | Asosiy maydonlar |
|---|---|
| `users` | id UUID PK, full_name, email UNIQUE NOT NULL, hashed_password, is_active, is_admin, created_at |
| `categories` | id UUID PK, name UNIQUE NOT NULL, description, created_at |
| `books` | id UUID PK, title NOT NULL, description, author, language, published_year, pages, file_path, cover_path, is_published, owner_id FK -> users (CASCADE), category_id FK -> categories (RESTRICT), created_at, updated_at |

Indekslar (keyinroq): `books(title)`, `books(owner_id)`, `books(category_id)`.

### 5. PostgreSQL ni yaratish
Variant A (tavsiya): Docker orqali. Variant B: lokal Postgres (psql/pgAdmin). Qaysi variant bo'lmasin, `.env` orqali ulanamiz.

### 6. ORM va Alembic
- **ORM** (SQLAlchemy) SQL yozmasdan Python klasslari bilan baza bilan ishlash imkonini beradi; xavfsizroq (SQL Injection dan himoya).
- **Alembic** — MB versiyalarini boshqarish: ustun qo'shilsa eski ma'lumot o'chmaydi. `alembic init alembic`, `env.py` da `target_metadata = Base.metadata`.
- Nega `.env` va `pydantic-settings`: unutilgan o'zgaruvchi bo'lsa dastur ishga tushmaydi va xato beradi.

---

## Kod namunalari

### 1. PostgreSQL (Docker)
```bash
docker run --name e_library_db \
  -e POSTGRES_USER=elib_user \
  -e POSTGRES_PASSWORD=elib_pass \
  -e POSTGRES_DB=e_library \
  -p 5432:5432 -d postgres:16
docker ps
```

### 2. `.env.example`
```text
APP_NAME=E-Library API
DEBUG=true
DB_HOST=localhost
DB_PORT=5432
DB_NAME=e_library
DB_USER=elib_user
DB_PASSWORD=elib_pass
JWT_SECRET_KEY=change_me_please
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
MEDIA_ROOT=media
```

### 3. `app/core/config.py`
```python
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "E-Library API"
    debug: bool = False
    db_host: str
    db_port: int = 5432
    db_name: str
    db_user: str
    db_password: str
    jwt_secret_key: str
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60
    media_root: str = "media"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )


settings = Settings()
```

### 4. `app/core/database.py`
```python
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from app.core.config import settings

engine = create_async_engine(settings.database_url, echo=settings.debug)
AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
```
`engine` — baza bilan aloqa kanali; `AsyncSessionLocal` — har so'rov uchun alohida sessiya.

### 5. `app/main.py` (healthcheck)
```python
from fastapi import FastAPI
from app.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name, debug=settings.debug)

    @app.get("/health", tags=["system"])
    async def healthcheck() -> dict:
        return {"status": "ok"}

    return app


app = create_app()
```

### 6. `app/models/base.py` va Alembic
```python
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
```
```bash
alembic init alembic
# alembic/env.py: target_metadata = Base.metadata, URL settings.database_url dan
uvicorn app.main:app --reload
```
Tekshirish: `http://127.0.0.1:8000/docs` (Swagger) va `http://127.0.0.1:8000/health` (`{"status": "ok"}`).

### 7. `pyproject.toml` (ruff)
```toml
[tool.ruff]
line-length = 88
target-version = "py311"
select = ["E", "F", "I", "B", "UP"]
ignore = ["B008"]
```

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq (Oson): Qatlamlarni juftlash
`routes`, `schemas`, `services`, `models`, `core` papkalari nima uchun ekanini yozing.

**Yechim:** routes: HTTP qatlami; schemas: Pydantic kirish/chiqish; services: biznes mantiq; models: SQLAlchemy ORM; core: config, DB session, security.

### 2-topshiriq (O'rta): Skeleton ni ishga tushirish
Venv, kutubxonalar, `.env`, `config.py`, `database.py` va `main.py` ni yarating va `/health` ni tekshiring.

**Yechim:** Kod namunalari 2-5. `uvicorn app.main:app --reload` dan keyin `/health` javobi `{"status": "ok"}`, `/docs` da Swagger ochiladi.

### 3-topshiriq (Qiyin): O'z loyihangiz uchun TT va MB
O'z FastAPI loyihangizni tanlang (masalan, «Maktab kutubxonasi»), mini TT yozing, 2-3 jadvalli ER dizayn chizing va skeleton yarating.

**Yechim (namuna):** TT: maqsad, rollar, MVP funksiyalar, nofunksional talablar. ER: `users (1) - (N) books`, PK/FK belgilangan. Skeleton: E-Library kabi tuzilma, `GET /health` ishlaydi, `alembic init` bajarilgan.

---

## Tezkor nazorat savollari

1. FastAPI ga nega ASGI server (Uvicorn) kerak?
   - **Javob:** FastAPI asinxron (async/await) ishlaydi; an'anaviy WSGI emas, ASGI server kerak.
2. Virtual muhit nima uchun kerak?
   - **Javob:** Kutubxona versiyalari ziddiyatini (dependency conflicts) oldini oladi.
3. `app/models` va `app/schemas` farqi?
   - **Javob:** models: baza jadvallari (ORM); schemas: foydalanuvchiga qaytadigan va kiradigan ma'lumot shakli (Pydantic).
4. One-to-Many bog'lanish qanday amalga oshadi?
   - **Javob:** «Ko'p» tomondagi jadvalda boshqa jadvalga Foreign Key bo'ladi (`books.owner_id -> users.id`).
5. Nega Alembic ishlatiladi?
   - **Javob:** MB versiyalarini boshqaradi, jadvalga o'zgarish kiritilganda ma'lumot o'chmaydi.
6. `.env` va `BaseSettings` afzalligi?
   - **Javob:** Sirlar kodda emas; unutilgan o'zgaruvchi bo'lsa dastur ishga tushmay xato beradi.

---

## Uyga vazifa

`uyga-vazifa.md` ga qarang.
