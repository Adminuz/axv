# 16-dars. Fayllar bilan ishlash

> Kitobga muqova rasmini qanday yuklaymiz? Bugun FastAPI da fayl qabul qilish, tekshirish va yuklab olishni o'rganamiz.

## Dars xulosasi

- Fayl `UploadFile = File(...)` bilan qabul qilinadi (`python-multipart` kerak).
- Tur noto'g'ri bo'lsa 415, hajm katta bo'lsa 413.
- Mijoz bergan nomga ishonmang: `uuid4` nomi ishlating.
- `FileResponse` faylni yuklab olish uchun qaytaradi.
- Path traversal dan `resolve()` va papka tekshiruvi himoya qiladi.
- Bazada fayl nomi saqlanadi, faylning o'zi emas.

## Qo'shimcha ma'lumot

### Form
Fayl bilan birga oddiy maydonlar `Form(...)` bilan yuboriladi.

### StaticFiles
`app.mount` bilan ochiq statik fayllarni berish.

### Magic bytes
Fayl boshidagi baytlar haqiqiy turni ko'rsatadi.

### Chunk
Katta faylni bo'laklab o'qish.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| UploadFile | Yuklangan fayl obyekti |
| multipart | Fayl yuborish formati |
| content_type | Fayl turi |
| uuid4 | Tasodifiy noyob nom |
| FileResponse | Fayl qaytaruvchi javob |
| 413 | Fayl katta |
| 415 | Tur mos emas |
| Path traversal | Papkadan chiqish hujumi |

## Bilasizmi?

- FastAPI `UploadFile` Starlette ning `SpooledTemporaryFile` ustiga qurilgan: kichik fayl xotirada, katta fayl diskda turadi.
- Katta fayllar ko'pincha to'g'ridan-to'g'ri bulutli saqlashga (S3 va boshqalar) yuklanadi.
- Rasmni qayta ishlash (siqish, o'lcham) uchun Pillow kutubxonasi ishlatiladi.

## Topshiriqlar

### 1. Fayl qabul qilish · oson

Fayl nomini qaytaruvchi endpoint yozing.

**Kutiladigan natija:** `UploadFile = File(...)`.

### 2. Paket · oson

Fayl yuklash uchun qaysi paket o'rnatiladi?

**Kutiladigan natija:** `python-multipart`.

### 3. Xato kodlari · oson

413 va 415 ni tushuntiring.

**Kutiladigan natija:** Katta fayl; noto'g'ri tur.

### 4. Atributlar · oson

UploadFile ning 2 atributini yozing.

**Kutiladigan natija:** `filename`, `content_type`.

### 5. Tur tekshiruvi · o'rta

Faqat PDF ni qabul qiling.

**Kutiladigan natija:** `application/pdf` tekshiruvi.

### 6. Hajm · o'rta

5 MB chegarasini qo'shing.

**Kutiladigan natija:** `read(MAX+1)` va 413.

### 7. Nom · o'rta

Nega `uuid4` nomi ishlatiladi?

**Kutiladigan natija:** Xavfsizlik va takrorlanmaslik.

### 8. Kengaytma · o'rta

Ruxsat etilgan kengaytmalarni lug'at orqali tanlang.

**Kutiladigan natija:** `ALLOWED.get(content_type)`.

### 9. Yuklab olish · qiyin

`/files/{name}` ni xavfsiz yozing.

**Kutiladigan natija:** `resolve()` va papka tekshiruvi.

### 10. Hujum testi · qiyin

`../main.py` nomi bilan so'rov yuboring va 404 ni tekshiring.

**Kutiladigan natija:** 404 qaytadi.

### 11. Egasi · qiyin

Faqat fayl egasi yuklab olsin.

**Kutiladigan natija:** `user.id == book.owner_id`.

### 12. Bazaga bog'lash · bonus

`Book.cover` maydonini qo'shib, migratsiya yarating.

**Kutiladigan natija:** Alembic migratsiya va endpoint.

## O'zingizni tekshiring

1. Fayl uchun qaysi tur?
2. 413 va 415 farqi?
3. Nega `filename` ga ishonmaymiz?
4. Path traversal nima?
5. `FileResponse` nima?
6. Bazada nima saqlanadi?

## Uyga vazifa

Book loyihasiga fayl yuklashni qo'shing (30–40 daqiqa). To'liq shart: `uyga-vazifa.md`.
