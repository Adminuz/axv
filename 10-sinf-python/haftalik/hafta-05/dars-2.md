# 14-dars. CRUD amallarni bajarish (model, forma, validatsiya)

## Dars rejasi (80 daqiqa)

**Maqsad:** CRUD tushunchasini (POST/GET/PUT-PATCH/DELETE ↔ INSERT/SELECT/UPDATE/DELETE) tushuntirish, `Book` SQLAlchemy modeli va Pydantic sxemalarini (`BookCreate`, `BookUpdate`, `BookRead`) yozish, `Field` cheklovlari bilan validatsiya qilish, to'liq CRUD endpointlarni xatoliklarni boshqarish (404, 403) bilan qurish va Swagger orqali sinash.

**Kutiladigan natija:** o'quvchi (1) CRUD harflarini HTTP metodlari va SQL buyruqlari bilan juftlaydi; (2) `Book` modeli va `BookCreate`/`BookRead` sxemalarini `Field` cheklovlari bilan yozadi; (3) Create, Read (ro'yxat va bitta), Update va Delete endpointlarini yozadi; (4) 404 va 403 xatolarini `HTTPException` bilan qaytaradi, Swagger da sinaydi.

| Vaqt | Bosqich |
|---|---|
| 10 daq | Takrorlash: 13-dars: register, login, `get_current_user` |
| 30 daq | Yangi mavzu: CRUD jadvali, `Book` modeli va Pydantic sxemalar; `POST /books` va `GET /books`, `GET /books/{id}` |
| 5 daq | Tanaffus |
| 20 daq | Amaliyot: `PATCH`, `DELETE`, egalik tekshiruvi va xatolar |
| 10 daq | Xatolar, Form va Swagger orqali test; xulosa |
| 5 daq | Xulosa, tezkor nazorat, uyga vazifa |

---

## Mentor konspekti

### 1. CRUD, SQLAlchemy model va Pydantic sxemalar
CRUD — Create, Read, Update, Delete: ma'lumotlar hayot sikli. REST da ular **POST, GET, PUT/PATCH, DELETE** ga, SQL da **INSERT, SELECT, UPDATE, DELETE** ga mos keladi. Jadval `SQLAlchemy` modelida (`Book`), kiruvchi va chiquvchi ma'lumot shakli esa `Pydantic` sxemalarida yoziladi. Nega ikkita? Model — bazadagi fizik ko'rinish, sxema — foydalanuvchi yuboradigan va oladigan ma'lumot «filtri». Masalan, `BookCreate` da `id` yo'q (uni baza beradi), `BookRead` da `owner_id` bor. `Field(min_length=..., gt=..., le=...)` cheklovlari avtomatik validatsiya beradi.

`gt` — kattaroq, `le` — kichik yoki teng. `pages=-5` yuborilsa FastAPI avtomatik `422 Unprocessable Entity` qaytaradi, bazaga bormaydi.

### 2. Create va Read endpointlari
**Create** (`POST`): JSON `BookCreate` sxemasi bilan tekshiriladi, modelga o'tkaziladi, `db.add`, `await db.commit()`, `await db.refresh()` (bazadagi `id` va `created_at` ni qaytarish uchun), status `201`. Egasi — joriy foydalanuvchi. **Read** (`GET`): ro'yxat (`select(Book)`) va bitta kitob (`db.get(Book, id)`); topilmasa `404 Not Found`. Muvaffaqiyatli yaratishda `201 Created` standart hisoblanadi.

`db.refresh(book)` bo'lmasa, `commit` dan keyin bazada yaratilgan maydonlar (`created_at`) javobda eskirgan bo'lishi mumkin.

### 3. Update, Delete va xatolarni boshqarish
**Update** avval kitobni o'qishni, so'ng o'zgartirishni talab qiladi. To'liq almashtirish uchun `PUT`, qisman o'zgartirish uchun `PATCH`: `data.model_dump(exclude_unset=True)` faqat yuborilgan maydonlarni beradi. **Delete** ham avval topadi: yo'q bo'lsa `404`. Ikkalasida **egalik tekshiruvi**: kitob egasi boshqa bo'lsa `403 Forbidden`. Xatolar `HTTPException` bilan qaytariladi: 400 (mantiqiy xato), 401, 403, 404. Frontend HTML forma yuborsa, JSON sxema o'rniga `Form(...)` ishlatiladi.

`DELETE` uchun `status_code=204` qo'yish va `await db.delete(book)` dan keyin `commit` qilish odatiy. Avval topmasdan o'chirish noto'g'ri: 404 ni qaytara olmaysiz.

---

## Kod namunalari

### 1. `app/schemas/book.py`
```python
import uuid
from pydantic import BaseModel, ConfigDict, Field


class BookCreate(BaseModel):
    title: str = Field(min_length=2, max_length=200)
    author: str | None = Field(default=None, max_length=120)
    description: str | None = None
    pages: int | None = Field(default=None, gt=0, le=5000)
    published_year: int | None = Field(default=None, ge=1000, le=2100)
    is_published: bool = False


class BookUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=2, max_length=200)
    author: str | None = Field(default=None, max_length=120)
    description: str | None = None
    pages: int | None = Field(default=None, gt=0, le=5000)
    is_published: bool | None = None


class BookRead(BookCreate):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    owner_id: uuid.UUID
```

### 2. `app/models/book.py`
```python
import uuid
from datetime import datetime
from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base


class Book(Base):
    __tablename__ = "books"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(200), index=True)
    author: Mapped[str | None] = mapped_column(String(120))
    description: Mapped[str | None] = mapped_column(Text)
    pages: Mapped[int | None] = mapped_column(Integer)
    published_year: Mapped[int | None] = mapped_column(Integer)
    is_published: Mapped[bool] = mapped_column(Boolean, default=False)
    owner_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
```

### 3. Forma ma'lumoti (Form)
```python
from fastapi import Form

@router.post("/form")
async def create_from_form(title: str = Form(...), author: str = Form("")):
    return {"title": title, "author": author}
```

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq (Oson): CRUD juftlash
C, R, U, D harflarini HTTP metodi va SQL buyrug'i bilan juftlang.

**Yechim:** C — POST — INSERT; R — GET — SELECT; U — PUT/PATCH — UPDATE; D — DELETE — DELETE.

### 2-topshiriq (O'rta): Create
`POST /books` endpointini yozing (egasi joriy foydalanuvchi, status 201).

**Yechim:** 
```python
@router.post("/", response_model=BookRead, status_code=201)
async def create_book(data: BookCreate, db: AsyncSession = Depends(get_db),
                      user: User = Depends(get_current_user)):
    book = Book(**data.model_dump(), owner_id=user.id)
    db.add(book)
    await db.commit()
    await db.refresh(book)
    return book
```

### 3-topshiriq (Qiyin): Delete
`DELETE /books/{id}` ni yozing: 404, egasi bo'lmasa 403, muvaffaqiyatda 204.

**Yechim:** 
```python
@router.delete("/{book_id}", status_code=204)
async def delete_book(book_id: uuid.UUID, db: AsyncSession = Depends(get_db),
                      user: User = Depends(get_current_user)):
    book = await db.get(Book, book_id)
    if book is None:
        raise HTTPException(404, "Kitob topilmadi")
    if book.owner_id != user.id:
        raise HTTPException(403, "Bu kitob sizniki emas")
    await db.delete(book)
    await db.commit()
```

---

## Tezkor nazorat savollari

1. CRUD nima?
   - **Javob:** Create, Read, Update, Delete: ma'lumotlarning to'rt asosiy amali.
2. Nega ikkita model: SQLAlchemy va Pydantic?
   - **Javob:** SQLAlchemy — bazadagi jadval; Pydantic — foydalanuvchiga kiruvchi/chiquvchi ma'lumotni tekshiruvchi filtr.
3. `db.refresh()` nima qiladi?
   - **Javob:** Commit dan keyin obyektni bazadan yangilaydi (masalan, bazada yaratilgan `created_at`).
4. PUT va PATCH farqi?
   - **Javob:** PUT to'liq almashtiradi, PATCH qisman o'zgartiradi.
5. Topilmagan resurs uchun qaysi status?
   - **Javob:** 404 Not Found.

---

## Uyga vazifa

`uyga-vazifa.md` ga qarang.
