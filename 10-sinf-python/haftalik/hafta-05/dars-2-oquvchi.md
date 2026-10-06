# 14-dars. CRUD amallarni bajarish (model, forma, validatsiya)

> Kitob qo'shish, ko'rish, tuzatish, o'chirish: har bir ilovaning yuragi shu to'rt amal. Bugun E-Library ga to'liq kitoblar CRUD sini qo'shamiz.

## Dars xulosasi

- CRUD: Create (POST/INSERT), Read (GET/SELECT), Update (PUT-PATCH/UPDATE), Delete (DELETE/DELETE).
- SQLAlchemy modeli bazadagi jadval, Pydantic sxemasi kiruvchi/chiquvchi ma'lumot filtri.
- `Field(min_length, max_length, gt, le)` bilan validatsiya; xato bo'lsa 422.
- Create: `db.add`, `commit`, `refresh`, status 201.
- Update/Delete avval kitobni topadi (404) va egaligini tekshiradi (403).
- `PATCH` da `model_dump(exclude_unset=True)`; HTML forma uchun `Form`.

## Qo'shimcha ma'lumot

### 1. Nega avval topamiz?
O'chirishdan oldin topmasak, «yo'q» holatni 404 bilan aytib bo'lmaydi va egalikni tekshirib bo'lmaydi.

### 2. Service qatlami
Katta loyihada endpoint ichidagi baza kodi `services/` ga ko'chiriladi: router faqat HTTP bilan, service biznes mantiq bilan shug'ullanadi.

### 3. Odatiy xatolar
`commit` ni unutish; `await` ni unutish; modelni to'g'ridan-to'g'ri javobda qaytarib, `response_model` bermaslik; egalikni tekshirmaslik.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **CRUD** | Ma'lumot ustida to'rt amal |
| **ORM** | Obyektlar orqali bazadan foydalanish |
| **Pydantic** | Ma'lumotni tekshiruvchi kutubxona |
| **response_model** | Javob shakli sxemasi |
| **HTTPException** | Xato javobini qaytarish |
| **Form** | HTML forma ma'lumotini qabul qilish |
| **model_dump** | Pydantic obyektini lug'atga aylantirish |
| **422** | Validatsiya xatosi |

## Bilasizmi?

- `exclude_unset=True` PATCH ni xavfsiz qiladi: yuborilmagan maydon `None` bilan o'chib ketmaydi.
- `204 No Content` javobda tana bo'lmaydi.
- UUID bilan resurs manzili taxmin qilishga qiyin.

## Topshiriqlar

### 1. CRUD juftlash · oson
C, R, U, D uchun HTTP metodlarini yozing.

**Kutiladigan natija:** POST, GET, PUT/PATCH, DELETE.

### 2. SQL juftlash · oson
CRUD uchun SQL buyruqlarini yozing.

**Kutiladigan natija:** INSERT, SELECT, UPDATE, DELETE.

### 3. Model va schema · oson
SQLAlchemy modeli va Pydantic sxemasi farqini 2 jumlada yozing.

**Kutiladigan natija:** Model — baza; sxema — kirish/chiqish.

### 4. Status kodlar · oson
201, 204, 404, 422 kodlari qachon qaytishini yozing.

**Kutiladigan natija:** 4 ta holat.

### 5. Book modeli · o'rta
`Book` modelini yozing (id UUID, title, author, pages, owner_id FK).

**Kutiladigan natija:** Migratsiyada `books` jadvali.

### 6. Field cheklovlari · o'rta
`pages` uchun 1 dan 5000 gacha cheklov yozing va `-5` yuborib natijani ko'ring.

**Kutiladigan natija:** 422 xatosi.

### 7. Create · o'rta
`POST /books` ni yozing va `201` oling.

**Kutiladigan natija:** Javobda `id` bor.

### 8. Read · o'rta
`GET /books/{id}` ni yozing; mavjud bo'lmagan `id` uchun 404 oling.

**Kutiladigan natija:** 404 va xabar.

### 9. Update · qiyin
`PATCH /books/{id}` ni yozing; faqat `title` yuborganda boshqa maydonlar saqlansin.

**Kutiladigan natija:** Faqat `title` o'zgardi.

### 10. Delete · qiyin
`DELETE /books/{id}` ni egalik tekshiruvi bilan yozing.

**Kutiladigan natija:** Egasiga 204, boshqasiga 403.

### 11. Xatoni toping · qiyin
`db.add(book)` dan keyin `commit` yozilmagan. Nima bo'ladi?

**Kutiladigan natija:** O'zgarish bazaga yozilmaydi; `await db.commit()` kerak.

### 12. Category CRUD · bonus
`categories` jadvali uchun xuddi shunday CRUD yozing (faqat admin yaratsin).

**Kutiladigan natija:** Kategoriya endpointlari ishlaydi.

## O'zingizni tekshiring

1. CRUD nima?
2. Nega ikkita model kerak?
3. `db.refresh()` nima qiladi?
4. PUT va PATCH farqi?
5. 404 va 403 qachon qaytadi?
6. `Field(gt=0)` nima qiladi?
7. `Form` qachon ishlatiladi?

## Uyga vazifa

Book CRUD endpointlarini yozing va Swagger da sinang (25 daqiqa). To'liq shart: `uyga-vazifa.md`.
