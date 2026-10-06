# 15-dars. Filtrlash, qidiruv va tartiblash

## Dars rejasi (80 daqiqa)

**Maqsad:** Query parametrlar orqali filtrlashni (`Query` bilan validatsiya), SQLAlchemy da `where`, `ilike`, `or_`, `in_` qidiruvini, `order_by` bilan xavfsiz tartiblashni (ruxsat etilgan maydonlar ro'yxati), `limit`/`offset` pagination va umumiy sonni (`total`) qaytarishni o'rgatish.

**Kutiladigan natija:** o'quvchi (1) `Query(ge=..., le=...)` bilan validatsiyalangan query parametrlarni yozadi; (2) `where`, `ilike` va `or_` bilan filtrlash va qidiruv so'rovini quradi; (3) `order_by` bilan ruxsat etilgan maydonlar bo'yicha tartiblaydi; (4) `limit`/`offset` pagination va `total` bilan sahifalangan javob qaytaradi.

| Vaqt | Bosqich |
|---|---|
| 10 daq | Takrorlash: 14-dars: Book CRUD, `HTTPException` |
| 30 daq | Yangi mavzu: Query parametrlar, filtrlash (`where`) va qidiruv (`ilike`, `or_`); Tartiblash (`order_by`) va ruxsat etilgan maydonlar |
| 5 daq | Tanaffus |
| 20 daq | Amaliyot: Pagination: `limit`, `offset`, `total`; Swagger da sinov |
| 10 daq | Xavfsizlik: `sort` ni tekshirish, `limit` chegarasi; xulosa |
| 5 daq | Xulosa, tezkor nazorat, uyga vazifa |

---

## Mentor konspekti

### 1. Query parametrlar orqali filtrlash
Ro'yxatni cheklash uchun **query parametrlar** ishlatiladi: `GET /books?author=Navoiy&min_pages=100`. FastAPI da ular endpoint funksiyasining oddiy argumentlari (`author: str | None = None`), cheklovlar `Query(...)` bilan beriladi. SQLAlchemy da filtr `where(...)` bilan qo'shiladi: bir nechta `where` ketma-ket `AND` ga aylanadi. Parametr berilmasa, filtr qo'llanmaydi. Chop etilgan (`is_published`) kitoblarni ko'rsatish oddiy foydalanuvchi uchun majburiy filtr bo'lishi mumkin.

`GET /books?min_pages=100&published_year=2020` ikkala shartni birga (AND) qo'llaydi. `min_pages=0` bo'lsa `if min_pages:` shart o'tmaydi: aniq tekshiruv uchun `is not None` ishlating.

### 2. Qidiruv (ilike, or_) va tartiblash (order_by)
**Qidiruv**: `Book.title.ilike(f"%{q}%")` registrni farqlamasdan qismini topadi (PostgreSQL `ILIKE`). Bir nechta maydonda izlash uchun `or_(...)`. **Tartiblash**: `order_by(Book.created_at.desc())`. Foydalanuvchidan kelgan `sort` nomini `getattr(Book, sort)` bilan to'g'ridan-to'g'ri ishlatmang: faqat **ruxsat etilgan maydonlar ro'yxati** (`ALLOWED_SORT`) dan tanlang. Odatda `-created_at` kamayish, `title` o'sish tartibini bildiradi.

Qidiruvda `%` va `_` belgilari LIKE da maxsus. Katta jadvalda boshida `%` bo'lgan `ilike` indeksdan foydalanmaydi (keyingi bosqich: `pg_trgm`).

### 3. Pagination va sahifalangan javob
Minglab yozuvni bir marta qaytarish serverni sekinlashtiradi. **Pagination** natijani sahifalarga bo'ladi: `limit` (sahifada nechta) va `offset` (nechtasini o'tkazib yuborish). `Query(10, ge=1, le=100)` bilan `limit` chegaralanadi. Javobda sahifa elementlari (`items`) bilan birga umumiy son (`total`) ham qaytadi, shunda frontend sahifalar sonini hisoblaydi. Umumiy son: `select(func.count()).select_from(stmt.subquery())` (limit qo'llashdan oldin). Sahifa: `offset = (page - 1) * limit`.

`limit` ga yuqori chegara (masalan, 100) qo'yish shart: aks holda `limit=1000000` bilan serverni yuklash mumkin. `GET /books?q=python&sort=title&limit=5&offset=10`.

---

## Kod namunalari

### 1. To'liq `GET /books`
```python
@router.get("/", response_model=BookPage)
async def list_books(
    q: str | None = None,
    author: str | None = None,
    min_pages: int | None = Query(None, ge=1),
    published_year: int | None = None,
    sort: str = "-created_at",
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: AsyncSession = Depends(get_db),
):
    stmt = select(Book).where(Book.is_published.is_(True))
    if author:
        stmt = stmt.where(Book.author == author)
    if min_pages is not None:
        stmt = stmt.where(Book.pages >= min_pages)
    if published_year is not None:
        stmt = stmt.where(Book.published_year == published_year)
    stmt = apply_search(stmt, q)
    total = await db.scalar(select(func.count()).select_from(stmt.subquery()))
    stmt = apply_sort(stmt, sort).limit(limit).offset(offset)
    items = (await db.scalars(stmt)).all()
    return BookPage(items=items, total=total, limit=limit, offset=offset)
```

### 2. `in_` bilan bir nechta qiymat
```python
years = [2020, 2021, 2022]
stmt = select(Book).where(Book.published_year.in_(years))
```

### 3. Foydalanuvchining o'z kitoblari
```python
@router.get("/mine", response_model=list[BookRead])
async def my_books(db: AsyncSession = Depends(get_db),
                   user: User = Depends(get_current_user)):
    stmt = select(Book).where(Book.owner_id == user.id).order_by(Book.created_at.desc())
    return (await db.scalars(stmt)).all()
```

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq (Oson): Filtr
`published_year` bo'yicha filtrni `list_books` ga qo'shing.

**Yechim:** 
```python
if published_year is not None:
    stmt = stmt.where(Book.published_year == published_year)
```

### 2-topshiriq (O'rta): Qidiruv
`q` parametri sarlavha va muallifda registrni farqlamay qidirsin.

**Yechim:** 
```python
if q:
    like = f"%{q}%"
    stmt = stmt.where(or_(Book.title.ilike(like), Book.author.ilike(like)))
```

### 3-topshiriq (Qiyin): Sort va sahifa
`sort` (ruxsat etilgan maydonlar) va `limit`/`offset` ni yozing, `total` qaytaring.

**Yechim:** 
```python
column = ALLOWED_SORT.get(sort.lstrip("-"))
if column is None:
    raise HTTPException(400, "Noto'g'ri sort maydoni")
stmt = stmt.order_by(column.desc() if sort.startswith("-") else column.asc())
total = await db.scalar(select(func.count()).select_from(stmt.subquery()))
stmt = stmt.limit(limit).offset(offset)
```

---

## Tezkor nazorat savollari

1. Query parametr nima?
   - **Javob:** URL dagi `?kalit=qiymat` ko'rinishidagi parametr.
2. Qaysi operator katta-kichik harfni farqlamaydi?
   - **Javob:** `ilike`.
3. Nega `sort` ni ruxsat etilgan ro'yxatdan tekshiramiz?
   - **Javob:** Foydalanuvchi ixtiyoriy maydon nomini yubormasligi va xato yoki ma'lumot ochilmasligi uchun.
4. `limit` va `offset` nima?
   - **Javob:** Sahifa hajmi va o'tkazib yuboriladigan yozuvlar soni.
5. `total` nima uchun kerak?
   - **Javob:** Filtrga mos jami yozuvlar soni; frontend sahifalar sonini hisoblaydi.

---

## Uyga vazifa

`uyga-vazifa.md` ga qarang.
