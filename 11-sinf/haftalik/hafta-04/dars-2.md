# 11-dars. REST API va JSON asoslari: REST tamoyillari va HTTP

**Hafta:** 4 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + kod amaliyoti (curl / Postman) · **I-bob**, 11-dars (umumiy 1–51)

**Manba:** o'quv qo'llanma, «REST API va JSON asoslari» ma'ruzasi, «REST tamoyillari va HTTP asoslari» bo'limi (1.13-jadval: status kodlari); o'quv dasturi, «REST API va JSON asoslari» bayoni va natijalari.

## 1. Dars rejasi

**Maqsad:** o'quvchi REST (Representational State Transfer) g'oyasini, «resurs» va URI tushunchasini, HTTP metodlari (GET/POST/PUT/PATCH/DELETE) semantikasini, idempotentlik va xavfsiz metod farqini, holatsizlik (stateless) va status kodlarini biladi; resursga yo'naltirilgan URL loyihalaydi; minimal REST xizmatini yozib, `curl` yoki Postman bilan sinaydi.

**Kutiladigan natija:**
- «Nima?» = resurs nomi (URI), «qanday?» = HTTP metodi ekanini tushuntiradi.
- Ko'plik, ierarxiya (`/orders/ORD-001/items`) va query parametrlari qoidalari bo'yicha URL loyihalaydi.
- Beshta metodni ma'nosi va idempotentligi bo'yicha farqlaydi.
- 200/201/204/400/401/403/404/409/500 kodlarini to'g'ri vaziyatda tanlaydi.
- `Content-Type` va `Accept` sarlavhalarining vazifasini biladi; ETag va 304 mohiyatini tushuntiradi.
- «Kutubxona boshqaruvi» API'sining CRUD endpointlarini ishga tushiradi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va kirish | Observer (10-dars) uyga vazifasini ko'rish. Savol: «Telegram ilovasi serverdan ma'lumotni qanday so'raydi?» |
| 10–35 daq | Yangi mavzu | REST, resurs, URI dizayni; metodlar va idempotentlik; stateless; status kodlari; keshlash (ETag/304) |
| 35–40 daq | Tanaffus | Harakatli tanaffus |
| 40–65 daq | Amaliyot | `curl` bilan tayyor API'ni sinash; endpoint qo'shish; URL dizaynini tuzatish; status kodlarini tanlash |
| 65–75 daq | Tezkor nazorat | 5 ta savol |
| 75–80 daq | Xulosa va uyga vazifa | 12-darsga ko'prik: JSON kontrakt, xato formati |

---

## 2. Dars konspekti

### 2.1. REST nima?

**REST (Representational State Transfer)** — veb-xizmatlarni loyihalash uchun internet arxitekturasiga mos, soddaligi va izchilligi bilan ajralib turadigan yondashuv. Markazida **resurs** turadi: foydalanuvchi, buyurtma, mahsulot, to'lov, kitob. Har bir resurs tarmoqda o'z manzili (**URI**) orqali ifodalanadi. Mijoz resursning tasvirini HTTP yordamida o'qiydi, yangilaydi yoki o'chiradi.

Qoida: **«nima?» — resursning nomi (URI), «qanday?» — HTTP metodi.**

```text
GET  /api/users       -> foydalanuvchilar ro'yxati
POST /api/users       -> yangi foydalanuvchi yaratish
GET  /api/users/42    -> 42-ID foydalanuvchi
```

Hayotiy o'xshatish (yordamchi): kutubxona kartotekasi. Har bir kitobning o'z javon raqami (URI) bor; kutubxonachiga «ko'rsat», «yangi qo'sh», «chiqarib tashla» (metod) deysiz.

### 2.2. URI dizayni

Qo'llanmaga ko'ra URI **semantik, barqaror va izchil** bo'lishi kerak:
- ko'plikdagi otlar: `/orders`, `/books`;
- ierarxik bog'lanish: `/orders/ORD-001/items`;
- filtrlash va saralash — query parametrlarida: `/orders?status=paid&limit=20&sort=-created_at`.

| Yomon | Yaxshi | Nega |
|---|---|---|
| `/getAllBooks` | `GET /api/books` | fe'l metodda bo'ladi, URI'da emas |
| `/api/book/create` | `POST /api/books` | «yaratish» — POST ning ma'nosi |
| `/api/deleteBook?id=5` | `DELETE /api/books/5` | resurs manzili yo'lda, amal — metodda |
| `/api/books/5/getAuthor` | `GET /api/books/5/author` | ierarxiya, fe'lsiz |

### 2.3. HTTP metodlari va idempotentlik

| Metod | Vazifasi | Idempotent? | Xavfsiz (holatni o'zgartirmaydi)? |
|---|---|---|---|
| GET | faqat o'qish | ha (shart) | ha |
| POST | yangi resurs yaratish / holatni o'zgartiruvchi amal | odatda yo'q | yo'q |
| PUT | resursni **to'liq** yangilash | ha (talab) | yo'q |
| PATCH | resursni **qisman** yangilash | ba'zan ha, ba'zan yo'q | yo'q |
| DELETE | o'chirish | ha (maqsadga muvofiq) | yo'q |

**Idempotentlik** — so'rovni bir marta yoki ko'p marta yuborganda tizim holati bir xil bo'ladi. Misol: DELETE ni besh marta yuborsak ham, kitob «o'chirilgan» bo'lib qoladi (ikkinchi javob 404 bo'lishi mumkin, lekin tizim holati o'zgarmaydi). POST ni ikki marta yuborsak — ikkita kitob yaratiladi.

Retry (qayta urinish) uchun muhim: to'lov kabi POST so'rovlarda `Idempotency-Key` sarlavhasi bilan bir xil so'rov bir xil natija qaytaradi (qo'llanma namunasi):

```bash
curl -X POST https://api.example.com/v1/payments \
  -H "Authorization: Bearer <jwt>" \
  -H "Idempotency-Key: 3b1e-...-9c77" \
  -H "Content-Type: application/json" \
  -d '{"amount":125000,"currency":"UZS"}'
```

### 2.4. Holatsizlik va bir xil interfeys

- **Stateless:** har bir so'rov o'zida autentifikatsiya ma'lumoti (`Authorization: Bearer <jwt>`) va kerakli parametrlarni olib keladi; server seans holatini saqlamaydi. Natija: load balancer ortida bir nechta nusxa qo'yish oson (gorizontal masshtablash).
- **Uniform interface:** mijoz va server HTTP sarlavhalari va status kodlari orqali muloqot qiladi.
- `Content-Type: application/json` — yuborilayotgan format; `Accept: application/json` — mijoz kutayotgan javob formati.

### 2.5. Status kodlari (1.13-jadval)

| Kod | Nomi | Qachon |
|---|---|---|
| 200 | OK | muvaffaqiyatli, javobda resurs bor |
| 201 | Created | yangi resurs yaratildi |
| 204 | No Content | bajarildi, javob tanasi yo'q (masalan, DELETE) |
| 400 | Bad Request | so'rov noto'g'ri yoki validatsiyadan o'tmadi |
| 401 | Unauthorized | autentifikatsiya kerak (token yo'q) |
| 403 | Forbidden | kim ekanligi ma'lum, lekin ruxsat yo'q |
| 404 | Not Found | resurs yo'q |
| 409 | Conflict | mavjud resurs bilan zid holat |
| 500 | Server Error | serverning ichki xatosi |

O'quv dasturi yana 3xx, 422 va 429 ni eslatadi: 304 (Not Modified) keshlashda, 429 (Too Many Requests) tezlik cheklanganda ishlatiladi. Sinflar: 2xx — muvaffaqiyat, 3xx — yo'naltirish, 4xx — mijoz xatosi, 5xx — server xatosi.

### 2.6. Keshlash (qisqa)

Server javobga `ETag` (hash) yoki `Last-Modified` qo'shadi. Mijoz keyingi so'rovda `If-None-Match` / `If-Modified-Since` yuboradi; resurs o'zgarmagan bo'lsa **304 Not Modified** keladi va tarmoq tejaladi. `Cache-Control: public, max-age=60` brauzer/proksiga yo'l-yo'riq beradi. `If-Match` bilan PUT eski versiyani bosib yozib yuborish (lost update) oldini oladi.

### 2.7. Minimal REST xizmati (Python, faqat standart kutubxona)

Dars uchun hech narsa o'rnatish shart emas: `http.server` yetarli. (Real loyihada freymvork ishlatiladi; qo'llanma Python'da `pytest` bilan CRUD testlarini eslatadi.) Kod `library-api/app.py` fayliga yoziladi.

```python
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

BOOKS = {
    1: {"id": 1, "title": "O'tkan kunlar", "author": "Abdulla Qodiriy", "available": True},
    2: {"id": 2, "title": "Mehrobdan chayon", "author": "Abdulla Qodiriy", "available": True},
}
NEXT_ID = 3


class Handler(BaseHTTPRequestHandler):
    def send_json(self, status, body=None, headers=None):
        data = b"" if body is None else json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        for k, v in (headers or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(data)

    def read_json(self):
        size = int(self.headers.get("Content-Length", 0))
        try:
            return json.loads(self.rfile.read(size) or b"{}")
        except json.JSONDecodeError:
            return None

    def book_id(self):
        parts = self.path.strip("/").split("/")
        if len(parts) == 3 and parts[:2] == ["api", "books"] and parts[2].isdigit():
            return int(parts[2])
        return None

    def do_GET(self):
        if self.path == "/api/books":
            return self.send_json(200, list(BOOKS.values()))
        bid = self.book_id()
        if bid in BOOKS:
            return self.send_json(200, BOOKS[bid])
        self.send_json(404, {"message": "Kitob topilmadi"})

    def do_POST(self):
        global NEXT_ID
        body = self.read_json()
        if self.path != "/api/books":
            return self.send_json(404, {"message": "Manzil topilmadi"})
        if not body or not body.get("title"):
            return self.send_json(400, {"message": "title majburiy"})
        book = {"id": NEXT_ID, "title": body["title"], "author": body.get("author", ""), "available": True}
        BOOKS[NEXT_ID] = book
        NEXT_ID += 1
        self.send_json(201, book, {"Location": f"/api/books/{book['id']}"})

    def do_PUT(self):
        bid = self.book_id()
        body = self.read_json()
        if bid not in BOOKS:
            return self.send_json(404, {"message": "Kitob topilmadi"})
        if not body or not body.get("title"):
            return self.send_json(400, {"message": "title majburiy"})
        BOOKS[bid] = {"id": bid, "title": body["title"], "author": body.get("author", ""),
                      "available": body.get("available", True)}
        self.send_json(200, BOOKS[bid])

    def do_DELETE(self):
        bid = self.book_id()
        if bid not in BOOKS:
            return self.send_json(404, {"message": "Kitob topilmadi"})
        del BOOKS[bid]
        self.send_response(204)
        self.end_headers()


if __name__ == "__main__":
    HTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
```

(Mentor: kodni ekranda bo'laklab ko'rsating, to'liq faylni o'quvchi o'zi yozadi. Dars oldidan ishga tushirib tekshirilgan.)

Sinash (ikkinchi terminalda):

```bash
curl -i http://127.0.0.1:8000/api/books/1
curl -i -X POST http://127.0.0.1:8000/api/books \
  -H "Content-Type: application/json" -d '{"title":"Sarob","author":"Abdulla Qodiriy"}'
curl -i -X DELETE http://127.0.0.1:8000/api/books/2
```

Tekshirilgan natijalar: `GET /api/books/99` — 404; `POST` to'g'ri tana — 201 + `Location: /api/books/3`; `POST` `{}` — 400; `PUT` ikki marta — ikkalasi 200 va bir xil tana (idempotent); `DELETE` birinchi marta 204, ikkinchi marta 404.

Postman: yangi so'rov → metodni tanlang → URL → Body → raw → JSON → Send. Postman bo'lmasa `curl` yetarli (mentor ixtiyori).

### 2.8. Umumiy xatolar

- URI'da fe'l (`/getBooks`), birlikdagi ot bilan aralashtirish (`/book` va `/books`).
- Hamma narsaga 200 qaytarish (xatoni ham): mijoz xatoni sezmaydi.
- `GET` bilan ma'lumotni o'zgartirish.
- 401 va 403 ni aralashtirish.
- Parol/token kabi sirlarni URL query'ga yozish (loglarda qoladi).

---

## 3. Amaliy mashg'ulot (mini-loyiha: «Kutubxona boshqaruvi», 2-bosqich)

### 1-mashq (oson). API'ni ishga tushirish va sinash
**Vazifa:** 2.7-bo'limdagi `app.py` ni yozing, ishga tushiring. `curl -i` bilan `GET /api/books`, `GET /api/books/1`, `GET /api/books/99` ni chaqiring va har birining status kodini yozing.

**Kutiladigan natija:** 200, 200, 404.

**Yechim:** `python3 app.py`, boshqa terminalda `curl -i http://127.0.0.1:8000/api/books/99` → `HTTP/1.0 404 Not Found` va `{"message": "Kitob topilmadi"}`. Asosiy nuqta: mavjud bo'lmagan resurs uchun 200 emas, 404.

### 2-mashq (oson). URL dizaynini tuzatish
**Vazifa:** bu URL'larni REST qoidalariga moslab qayta yozing: `/getUsers`, `/api/order/delete?id=3`, `/api/createBook`, `/api/books/7/getReviews`.

**Kutiladigan natija:** to'rtta to'g'ri `metod + URI` juftligi.

**Yechim:**
- `GET /api/users`
- `DELETE /api/orders/3`
- `POST /api/books`
- `GET /api/books/7/reviews`

### 3-mashq (o'rta). Metod va idempotentlikni isbotlash
**Vazifa:** `PUT /api/books/1` ni bir xil tana bilan ikki marta chaqiring, javoblarni solishtiring. So'ng `POST /api/books` ni bir xil tana bilan ikki marta chaqiring va `GET /api/books` da nechta yozuv paydo bo'lganini sanang. Xulosani bir jumlada yozing.

**Kutiladigan natija:** PUT: ikkalasi 200, bir xil tana. POST: ikkita yangi yozuv (ID lar har xil).

**Yechim:**
```bash
curl -s -X PUT http://127.0.0.1:8000/api/books/1 -H "Content-Type: application/json" \
  -d '{"title":"O'"'"'tkan kunlar","author":"Qodiriy"}'
# ikkinchi marta ham xuddi shu javob (idempotent)
curl -s -X POST http://127.0.0.1:8000/api/books -H "Content-Type: application/json" -d '{"title":"Sarob"}'
curl -s -X POST http://127.0.0.1:8000/api/books -H "Content-Type: application/json" -d '{"title":"Sarob"}'
# GET /api/books da "Sarob" ikki marta, id 3 va 4
```
Xulosa: PUT idempotent (holat bir xil), POST — yo'q (har chaqiruv yangi resurs yaratadi).

### 4-mashq (o'rta). Status kodlarini tanlash
**Vazifa:** har bir vaziyatga kod tanlang: (a) yangi kitob yaratildi; (b) kitob o'chirildi, javob tanasi yo'q; (c) so'rovda `title` yo'q; (d) token yo'q; (e) token bor, lekin foydalanuvchi kitob o'chirishga ruxsatsiz; (f) shu ISBN li kitob allaqachon bor; (g) server bazaga ulana olmadi.

**Kutiladigan natija:** 7 ta kod.

**Yechim:** (a) 201; (b) 204; (c) 400; (d) 401; (e) 403; (f) 409; (g) 500.

### 5-mashq (qiyin). PATCH va yangi endpoint
**Vazifa:** `app.py` ga `PATCH /api/books/<id>` qo'shing: faqat yuborilgan maydonlarni yangilasin (masalan, `{"available": false}`). Mavjud bo'lmagan kitobga 404, noto'g'ri JSON'ga 400 qaytarsin.

**Kutiladigan natija:** `PATCH ... {"available": false}` → 200, qolgan maydonlar o'zgarmagan.

**Yechim:**
```python
    def do_PATCH(self):
        bid = self.book_id()
        body = self.read_json()
        if bid not in BOOKS:
            return self.send_json(404, {"message": "Kitob topilmadi"})
        if body is None:
            return self.send_json(400, {"message": "JSON noto'g'ri"})
        for key in ("title", "author", "available"):
            if key in body:
                BOOKS[bid][key] = body[key]
        self.send_json(200, BOOKS[bid])
```
Farq: PUT — to'liq almashtirish (yuborilmagan maydon yo'qoladi/standartga qaytadi), PATCH — faqat yuborilganlar.

### 6-mashq (qiyin). Holatsizlik va sarlavhalar
**Vazifa:** `curl -i -H "Accept: application/json" ...` bilan so'rov yuboring va javob sarlavhalarida `Content-Type` ni toping. So'ng qisqa yozing: nega server «avvalgi so'rovni eslab qolmasligi» (stateless) masshtablashga yordam beradi?

**Kutiladigan natija:** `Content-Type: application/json; charset=utf-8` topiladi; 2–3 jumlali tushuntirish.

**Yechim:** Har so'rov o'zi kerakli ma'lumotni (masalan, `Authorization`) olib keladi, shuning uchun mijoz qaysi nusxaga tushishi farqsiz: load balancer ortida bir nechta nusxa qo'yib, yukni bo'lish mumkin.

### 7-mashq (bonus). ETag
**Vazifa:** `GET /api/books/1` javobiga `ETag` (masalan, tana hash'i) qo'shing; `If-None-Match` mos kelsa 304 qaytaring.

**Yechim:** (ixtiyoriy)
```python
import hashlib

    def do_GET(self):
        ...
        if bid in BOOKS:
            body = json.dumps(BOOKS[bid], ensure_ascii=False)
            etag = '"' + hashlib.md5(body.encode()).hexdigest() + '"'
            if self.headers.get("If-None-Match") == etag:
                self.send_response(304)
                self.end_headers()
                return
            return self.send_json(200, BOOKS[bid], {"ETag": etag})
```
Ikkinchi so'rovda `curl -i -H 'If-None-Match: "<etag>"'` → 304.

---

## 4. Tezkor savollar

1. REST da «resurs» va URI nima?
   - **Javob:** Resurs — tizimdagi narsa (kitob, buyurtma); URI — uning tarmoqdagi manzili (`/api/books/5`). «Nima?» URI, «qanday?» metod bilan beriladi.
2. PUT va PATCH farqi?
   - **Javob:** PUT resursni to'liq almashtiradi va idempotent; PATCH faqat yuborilgan maydonlarni yangilaydi.
3. Idempotentlik nima? Qaysi metodlar idempotent?
   - **Javob:** Bir marta yoki ko'p marta yuborilganda tizim holati bir xil. GET, PUT, DELETE; POST odatda emas.
4. 401 va 403 farqi?
   - **Javob:** 401 — autentifikatsiya yo'q (kim ekanligi noma'lum); 403 — kim ekanligi ma'lum, lekin ruxsat yo'q.
5. Stateless nimani anglatadi va nima beradi?
   - **Javob:** Server seans holatini saqlamaydi, har so'rov o'zi hamma narsani olib keladi; gorizontal masshtablash osonlashadi.

## 5. Mentor uchun eslatmalar

- 10-dars uyga vazifasini (Observer mini-loyiha) dars boshida 3–4 daqiqada ko'ring.
- Kodni dars oldidan o'zingiz ishga tushirib ko'ring (port 8000 band bo'lsa 8001 ni tanlang).
- `http.server` ni qo'llanma talab qilmaydi; u faqat o'rnatishsiz ishlashi uchun tanlandi. Freymvork (FastAPI/Flask) qo'llanmada alohida yoritilmagan, kerak bo'lsa nom sifatida eslatish mumkin.
- Idempotency-Key, ETag va 304 qo'llanmada bor; amaliy server kodi (ETag misoli) — mentorning ilovasi.
- Postman o'rnatilmagan bo'lsa, `curl` bilan davom eting; natija bir xil.
- Kutubxona o'xshatishi yordamchi analogiya, rasmiy hujjatdan emas.
