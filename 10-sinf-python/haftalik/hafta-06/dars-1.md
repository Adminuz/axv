# 16-dars. Fayllar bilan ishlash

## Dars rejasi (80 daqiqa)

**Maqsad:** `python-multipart`, `UploadFile` va `File` yordamida fayl qabul qilishni, fayl turi va hajmini tekshirishni, xavfsiz nom (`uuid4`) bilan saqlashni va `FileResponse` orqali yuklab olish endpointini (path traversal dan himoya bilan) o'rgatish.

**Manba:** `oquv-dasturi.txt` (Fayllar bilan ishlash: UploadFile va File, saqlash, validatsiya, yuklab olish, xavfsizlik). Kod namunalari `Book` loyihasi uchun yozilgan va FastAPI + TestClient bilan sinab ko'rilgan.

**Kutiladigan natija:** o'quvchi (1) `UploadFile = File(...)` bilan fayl qabul qiluvchi endpoint yozadi; (2) `content_type` va hajm bo'yicha validatsiya qiladi (415, 413 xatolari); (3) Faylni foydalanuvchi bergan nom bilan emas, `uuid4` bilan saqlaydi; (4) `FileResponse` bilan yuklab olish endpointini yozadi; (5) Path traversal xavfini tushuntiradi va oldini oladi.

| Vaqt | Bosqich |
|---|---|
| 10 daq | Takrorlash: 15-dars: filtrlash, qidiruv, pagination |
| 30 daq | Yangi mavzu: `UploadFile` va `File`: fayl qabul qilish; Validatsiya: tur, hajm, xavfsiz nom |
| 5 daq | Tanaffus |
| 20 daq | Amaliyot: Saqlash va yuklab olish; Swagger da sinov |
| 10 daq | Xavfsizlik va xulosa: Xavfsizlik: path traversal, hajm chegarasi |
| 5 daq | Xulosa, tezkor nazorat, uyga vazifa |

---

## Mentor konspekti

### 1. UploadFile va File bilan fayl qabul qilish
Fayl (rasm, PDF) JSON emas, **multipart/form-data** ko'rinishida yuboriladi, buning uchun `python-multipart` paketi kerak (`pip install python-multipart`). Endpoint da `file: UploadFile = File(...)` yoziladi. `UploadFile` da `filename` (mijoz bergan nom), `content_type` (masalan `image/png`) va `await file.read()` bor. Katta fayl xotirada emas, vaqtinchalik faylda turadi, shuning uchun `UploadFile` oddiy `bytes` dan yaxshiroq. Swagger da endpoint yonida «Choose File» tugmasi paydo bo'ladi.

Fayl yuboruvchi endpoint da `Body` (JSON) bilan `File` ni aralashtirib bo'lmaydi: qo'shimcha maydonlar `Form(...)` bilan beriladi.

### 2. Fayl validatsiyasi va xavfsiz saqlash
Foydalanuvchi faylga ishonib bo'lmaydi. 1) **Tur**: `content_type` ni ruxsat etilgan ro'yxat (`image/jpeg`, `image/png`) bilan solishtiring, bo'lmasa **415**. 2) **Hajm**: `await file.read(MAX + 1)` o'qing; `MAX` dan oshsa **413**. 3) **Nom**: mijoz bergan `filename` ni ishlatmang (`../../x.py` kabi nom xavfli, fayl ustiga yozilishi mumkin); `uuid4().hex` va tekshirilgan kengaytma bilan o'z nomingizni yarating. 4) **Joy**: `UPLOAD_DIR` ni sozlamadan oling, loyiha kodidan alohida papkada saqlang.

`content_type` ni mijoz yuboradi, uni soxtalashtirish mumkin: jiddiy loyihada fayl sarlavhasi (magic bytes) ham tekshiriladi.

### 3. Yuklab olish va path traversal dan himoya
Saqlangan faylni qaytarish uchun `FileResponse(path)` ishlatiladi: u fayl turini o'zi aniqlaydi va oqim bilan yuboradi. Eng katta xavf — **path traversal**: foydalanuvchi `../.env` kabi nom yuborib, tizim fayllarini o'qishga urinadi. Himoya: yo'lni `resolve()` qiling va u haqiqatan `UPLOAD_DIR` ichida ekanini tekshiring, aks holda **404**. Ochiq statik fayllar (rasmlar) uchun `app.mount("/media", StaticFiles(directory="uploads"))` ham bor, lekin maxfiy fayllarni faqat tekshiruvli endpoint orqali bering. Fayl nomi bazada (`Book.cover`) saqlanadi, faylning o'zi emas.

Foydalanuvchining o'z fayli bo'lsa, `get_current_user` bilan egasini ham tekshiring.

---

## Kod namunalari

### 1. To'liq endpoint (sinab ko'rilgan)
```python
from pathlib import Path
from uuid import uuid4

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import FileResponse

app = FastAPI()
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)
ALLOWED = {"image/jpeg": ".jpg", "image/png": ".png"}
MAX_SIZE = 2 * 1024 * 1024


@app.post("/books/{book_id}/cover", status_code=201)
async def upload_cover(book_id: int, file: UploadFile = File(...)):
    ext = ALLOWED.get(file.content_type)
    if ext is None:
        raise HTTPException(415, "Faqat JPEG yoki PNG")
    data = await file.read(MAX_SIZE + 1)
    if len(data) > MAX_SIZE:
        raise HTTPException(413, "Fayl 2 MB dan katta")
    name = f"{book_id}_{uuid4().hex}{ext}"
    (UPLOAD_DIR / name).write_bytes(data)
    return {"filename": name, "size": len(data)}


@app.get("/files/{name}")
async def download(name: str):
    path = (UPLOAD_DIR / name).resolve()
    if path.parent != UPLOAD_DIR.resolve() or not path.is_file():
        raise HTTPException(404, "Fayl topilmadi")
    return FileResponse(path)
```

### 2. TestClient bilan tekshiruv
```python
from fastapi.testclient import TestClient

client = TestClient(app)
r = client.post("/books/1/cover", files={"file": ("a.png", b"x" * 10, "image/png")})
assert r.status_code == 201
r = client.post("/books/1/cover", files={"file": ("a.txt", b"x", "text/plain")})
assert r.status_code == 415
```

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq (Oson): Fayl qabul qiling
`/upload` endpointi yozing: fayl nomi va hajmini qaytarsin.

**Yechim:** 
```python
@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    data = await file.read()
    return {"filename": file.filename, "size": len(data)}
```

### 2-topshiriq (Oson): Tur tekshiruvi
Faqat PNG va JPEG ga ruxsat bering, boshqasida 415.

**Yechim:** 
```python
if file.content_type not in ("image/png", "image/jpeg"):
    raise HTTPException(415, "Faqat PNG yoki JPEG")
```

### 3-topshiriq (O'rta): Hajm chegarasi
2 MB dan katta faylga 413 qaytaring.

**Yechim:** 
```python
data = await file.read(MAX_SIZE + 1)
if len(data) > MAX_SIZE:
    raise HTTPException(413, "Fayl katta")
```

### 4-topshiriq (O'rta): Xavfsiz nom
Faylni `uuid4` nomi bilan saqlang.

**Yechim:** 
```python
name = f"{uuid4().hex}.png"
(UPLOAD_DIR / name).write_bytes(data)
```

### 5-topshiriq (Qiyin): Yuklab olish
`/files/{name}` endpointini path traversal dan himoyalab yozing.

**Yechim:** 
```python
path = (UPLOAD_DIR / name).resolve()
if path.parent != UPLOAD_DIR.resolve() or not path.is_file():
    raise HTTPException(404, "Fayl topilmadi")
return FileResponse(path)
```

### 6-topshiriq (Qo'shimcha): Bazaga bog'lash
`Book.cover` maydoniga fayl nomini yozing.

**Yechim:** Saqlangach `book.cover = name`, `await db.commit()`.

---

## Tezkor nazorat savollari

1. Fayl uchun qaysi tur ishlatiladi?
   - **Javob:** `UploadFile = File(...)`.
2. 413 va 415 farqi?
   - **Javob:** 413 — fayl katta; 415 — tur mos emas.
3. Nega `file.filename` ga ishonmaymiz?
   - **Javob:** Zararli nom (`../`) fayllarni ustiga yozishi mumkin.
4. Path traversal nima?
   - **Javob:** `../` bilan papkadan chiqib, tizim fayllarini o'qish urinishi.
5. Faylning o'zi qayerda saqlanadi?
   - **Javob:** Diskda yoki obyekt saqlashda; bazada faqat nomi.

---

## Uyga vazifa

`uyga-vazifa.md` ga qarang.
