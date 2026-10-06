# 15-dars. Filtrlash, qidiruv va tartiblash

> Kutubxonada 10 000 kitob bo'lsa, foydalanuvchi bittasini topishi kerak. Bugun ro'yxatni filtrlash, qidirish, tartiblash va sahifalashni o'rganamiz.

## Dars xulosasi

- Query parametrlar URL da `?kalit=qiymat` ko'rinishida; `Query(ge, le)` bilan validatsiya qilinadi.
- `where(...)` filtrlari ketma-ket AND bilan birikadi.
- `ilike` registrni farqlamay qidiradi; bir nechta maydon uchun `or_`.
- `order_by` bilan tartiblash; `sort` faqat ruxsat etilgan maydonlar ro'yxatidan tanlanadi.
- Pagination: `limit` (chegara bilan), `offset`; javobda `total` qaytariladi.
- Tartib: filtr, qidiruv, `count`, `order_by`, `limit/offset`.

## Qo'shimcha ma'lumot

### 1. AND va OR
Bir nechta `where` — AND. OR kerak bo'lsa `or_(...)`, ichma-ich mantiq uchun `and_(...)`. SQL dagi `AND`/`OR` bilan bir xil.

### 2. Sahifa raqami yoki offset
Ba'zi API lar `page` va `size` ishlatadi. Ichida baribir `offset = (page - 1) * size` hisoblanadi.

### 3. Odatiy xatolar
`limit` ga chegara qo'ymaslik; `sort` ni tekshirmasdan `getattr` ga berish; `count` ni `limit` dan keyin hisoblash; `ilike` da `%` ni qo'shishni unutish.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Filtrlash** | Ro'yxatni shartga ko'ra cheklash |
| **Qidiruv** | Matn bo'yicha qisman moslik izlash |
| **ilike** | PostgreSQL da registrni farqlamaydigan LIKE |
| **order_by** | Tartiblash |
| **limit** | Sahifadagi yozuvlar soni |
| **offset** | O'tkazib yuboriladigan yozuvlar soni |
| **Pagination** | Natijani sahifalarga bo'lish |
| **total** | Jami mos yozuvlar soni |

## Bilasizmi?

- PostgreSQL da `ILIKE` mavjud, SQLite da `LIKE` registrni odatda farqlamaydi.
- Katta offset (masalan, 1 000 000) sekin ishlaydi; shuning uchun keyingi bosqichda cursor pagination ishlatiladi.
- SQLAlchemy `where` ni zanjir qilib yozish mumkin, har chaqiruv yangi so'rov obyektini qaytaradi.

## Topshiriqlar

### 1. Query parametr · oson
`GET /books?author=Navoiy&min_pages=100` dagi parametrlarni sanang.

**Kutiladigan natija:** 2 ta parametr.

### 2. AND yoki OR · oson
Ketma-ket ikkita `where` AND mi yoki OR mi?

**Kutiladigan natija:** AND.

### 3. ilike · oson
`ilike` va `like` farqini yozing.

**Kutiladigan natija:** `ilike` registrni farqlamaydi.

### 4. limit va offset · oson
`limit=5&offset=10` qaysi yozuvlarni qaytaradi?

**Kutiladigan natija:** 11 dan 15 gacha.

### 5. Filtr · o'rta
`min_pages` filtrini `list_books` ga qo'shing.

**Kutiladigan natija:** `pages >= min_pages` bo'yicha natija.

### 6. Qidiruv · o'rta
Sarlavha yoki muallifda `q` bo'yicha qidiruv yozing.

**Kutiladigan natija:** Registrdan qat'i nazar topadi.

### 7. Sort · o'rta
`ALLOWED_SORT` lug'atini yozing (title, pages, created_at).

**Kutiladigan natija:** 3 ta ruxsat etilgan maydon.

### 8. `sort=-pages` · o'rta
`-` belgisini qanday qayta ishlaysiz?

**Kutiladigan natija:** `startswith("-")` va `desc()`.

### 9. Pagination · qiyin
`limit` (1..100) va `offset` parametrlarini `Query` bilan yozing.

**Kutiladigan natija:** `limit=0` va `limit=500` uchun 422.

### 10. total · qiyin
Filtrga mos jami sonni `func.count()` bilan hisoblang.

**Kutiladigan natija:** `total` chiqadi.

### 11. Xatoni toping · qiyin
`getattr(Book, sort)` ishlatilgan. Qanday xavf bor va qanday tuzatasiz?

**Kutiladigan natija:** Ixtiyoriy atribut; `ALLOWED_SORT` ro'yxati.

### 12. Mini-loyiha · bonus
O'z kitoblaringiz uchun `/books/mine` yozing va unga qidiruv hamda sahifalash qo'shing.

**Kutiladigan natija:** Faqat o'zingizning kitoblaringiz.

## O'zingizni tekshiring

1. Query parametr nima?
2. `where` larning birikishi?
3. `ilike` nima?
4. `or_` nima uchun?
5. `sort` ni nima uchun tekshiramiz?
6. `limit` va `offset` nima?
7. `total` nima uchun kerak?

## Uyga vazifa

Filtr, qidiruv, sort va pagination bilan `GET /books` ni yozing (25 daqiqa). To'liq shart: `uyga-vazifa.md`.
