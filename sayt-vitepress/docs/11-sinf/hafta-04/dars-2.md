---
title: "11-dars. REST API va JSON asoslari: REST tamoyillari va HTTP"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "11-sinf", "link": "/11-sinf/"}, "week": {"n": 4, "link": "/11-sinf/hafta-04/"}, "g": 11, "title": "REST API va JSON asoslari: REST tamoyillari va HTTP", "lead": "Har bir ilova serverdan ma'lumotni bir xil tilda so'raydi: HTTP. Bugun kutubxona uchun o'z REST API'ngizni yozib, curl bilan chaqirasiz.", "slide": "/slaydlar/11-sinf/hafta-04/dars-2.html", "test": null, "tabs": [{"g": 10, "link": "/11-sinf/hafta-04/dars-1", "current": false}, {"g": 11, "link": "/11-sinf/hafta-04/dars-2", "current": true}, {"g": 12, "link": "/11-sinf/hafta-04/dars-3", "current": false}], "prev": {"g": 10, "title": "Loyihalash andozalari: Observer va hodisalar arxitekturasi", "link": "/11-sinf/hafta-04/dars-1"}, "next": {"g": 12, "title": "REST API va JSON asoslari: JSON formati, kontrakt va xavfsizlik", "link": "/11-sinf/hafta-04/dars-3"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **REST** (Representational State Transfer) — veb-xizmatlarni resurslar atrofida quruvchi yondashuv.
- **Resurs** (kitob, buyurtma, foydalanuvchi) o'z manzili — **URI** — orqali ifodalanadi.
- **«Nima?» — URI, «qanday?» — HTTP metodi.**
- **URI qoidasi:** ko'plikdagi otlar (`/books`), ierarxiya (`/orders/ORD-001/items`), filtr va saralash query'da (`?status=paid&sort=-created_at`).
- **Metodlar:** GET (o'qish), POST (yaratish), PUT (to'liq yangilash), PATCH (qisman), DELETE (o'chirish).
- **Idempotentlik:** bir necha marta yuborganda holat o'zgarmasligi (GET, PUT, DELETE shunday; POST odatda yo'q).
- **Stateless:** server seans holatini saqlamaydi, har so'rov o'zi hammasini olib keladi.
- **Status kodlari:** 200, 201, 204, 400, 401, 403, 404, 409, 500.
- **Sarlavhalar:** `Content-Type`, `Accept`; keshlash uchun `ETag`/`304`.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Kutubxona o'xshatishi

Har bir kitobning javon raqami bor: bu URI. Kutubxonachiga aytadigan amallar: «ko'rsat» (GET), «yangi kitob qo'sh» (POST), «butunlay almashtir» (PUT), «faqat muqovasini yangila» (PATCH), «chiqarib tashla» (DELETE). Javon raqami o'zgarmaydi, amal o'zgaradi.

### 2. Nega URL'da fe'l bo'lmasligi kerak?

`/getBooks`, `/createBook`, `/deleteBook` ko'rinishida har amal uchun yangi manzil o'ylab topasiz. REST'da esa manzil bitta (`/api/books`), amalni HTTP metodi bildiradi. Natijada API bashoratli: bitta qoidani bilsangiz, hamma resursni tushunasiz.

### 3. Idempotentlik misoli

- `DELETE /api/books/5` ni besh marta yuborsangiz: kitob yo'q bo'lib qoladi. Ikkinchi marta 404 kelishi mumkin, lekin tizim holati o'zgarmaydi.
- `POST /api/books` ni besh marta yuborsangiz: besh dona kitob yaratiladi.

To'lov kabi xavfli POST uchun `Idempotency-Key` sarlavhasi ishlatiladi: bir xil kalit bilan takror so'rov bir xil natija beradi (pul ikki marta yechilmaydi).

### 4. 401 va 403 ni qanday eslab qolish mumkin?

401 — «Siz kimsiz? Tanishtiring» (token yo'q). 403 — «Sizni taniyman, lekin kirish mumkin emas». Binoga kirishda: karta ko'rsatmadingiz (401) va karta bor, lekin bu xonaga ruxsat yo'q (403).

### 5. Odatiy xatolar

- Xatoni ham `200` bilan qaytarish: mijoz hammasi joyida deb o'ylaydi.
- `GET` bilan ma'lumotni o'zgartirish.
- Birlik va ko'plikni aralashtirish: `/book` va `/books`.
- Maxfiy ma'lumotni URL'ga yozish: loglarda qoladi.

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **REST** | Resursga yo'naltirilgan, HTTP ustida ishlovchi API yondashuvi |
| **Resurs** | API orqali boshqariladigan narsa: kitob, buyurtma, foydalanuvchi |
| **URI** | Resursning tarmoqdagi manzili, masalan `/api/books/5` |
| **Endpoint** | Metod + URI birikmasi, masalan `GET /api/books` |
| **Idempotentlik** | Takror so'rov holatni o'zgartirmasligi |
| **Stateless** | Serverda seans holati saqlanmasligi |
| **Status kod** | Javobning natijasini bildiruvchi raqam (200, 404...) |
| **Content-Type** | Yuborilayotgan ma'lumot formati sarlavhasi |
| **Accept** | Mijoz kutayotgan javob formati sarlavhasi |
| **ETag** | Javob versiyasini bildiruvchi hash; keshlashda ishlatiladi |
| **CRUD** | Create, Read, Update, Delete: to'rt asosiy amal |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Barcha brauzer so'rovlari HTTP metodlari bilan ishlaydi: sayt ochish odatda `GET`, formani yuborish ko'pincha `POST`.
- `404` kodi shu darajada mashhur bo'lib ketganki, internetda «404» deyilganda hamma «topilmadi» ni tushunadi.
- REST atamasi 2000-yilda Roy Fielding doktorlik dissertatsiyasida taklif etilgan (ochiq manbalardagi umumiy ma'lumot).
- Postman va `curl` — API'larni sinash uchun eng ko'p ishlatiladigan vositalar qatoriga kiradi.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Metod tanlash <Badge type="tip" text="oson" />
Har bir amal uchun metod tanlang: (a) kitoblar ro'yxatini olish; (b) yangi kitob qo'shish; (c) kitobni butunlay yangilash; (d) faqat `available` ni o'zgartirish; (e) kitobni o'chirish.

**Kutiladigan natija:** 5 ta metod nomi.

### 2. URL'ni tuzating <Badge type="tip" text="oson" />
Qayta yozing: `/getUsers`, `/api/order/delete?id=3`, `/api/createBook`, `/api/books/7/getReviews`.

**Kutiladigan natija:** 4 ta `metod + URI` juftligi.

### 3. Status kodlarini moslang <Badge type="tip" text="oson" />
Moslang: 200, 201, 204, 404 — (a) yangi kitob yaratildi; (b) javob tanasi bo'sh, o'chirish bajarildi; (c) kitob topilmadi; (d) kitob muvaffaqiyatli olindi.

**Kutiladigan natija:** to'g'ri juftliklar.

### 4. Idempotent yoki yo'q? <Badge type="tip" text="oson" />
GET, POST, PUT, PATCH, DELETE: har birining idempotentligini yozing. PATCH nega «ba'zan» deyiladi?

**Kutiladigan natija:** jadval va 1–2 jumlali izoh.

### 5. API'ni ishga tushiring <Badge type="warning" text="o'rta" />
Darsdagi `library-api/app.py` ni yozing, ishga tushiring va `curl -i` bilan `GET /api/books`, `GET /api/books/1`, `GET /api/books/99` ni chaqiring.

**Kutiladigan natija:** 3 ta status kodi (200, 200, 404) va skrinshot yoki terminal matni.

### 6. POST va PUT'ni solishtiring <Badge type="warning" text="o'rta" />
Bir xil tana bilan `PUT` ni 2 marta, `POST` ni 2 marta yuboring. `GET /api/books` natijasini ko'rib, farqni yozing.

**Kutiladigan natija:** qaysi metod yangi yozuv yaratgani va qaysi biri bermagani haqida xulosa.

### 7. Bashorat qiling <Badge type="warning" text="o'rta" />
`curl -i -X POST http://127.0.0.1:8000/api/books -H "Content-Type: application/json" -d '{}'` qanday status qaytaradi? Javob tanasida nima bo'ladi? Avval taxmin qiling, keyin sinang.

**Kutiladigan natija:** taxmin va haqiqiy natija taqqoslanadi.

### 8. Xatoni toping <Badge type="warning" text="o'rta" />
Quyidagi API dizaynida nechta xato bor? `GET /api/deleteBook/5` kitobni o'chiradi va `200` qaytaradi, kitob topilmasa ham `200 {"ok": false}` qaytaradi.

**Kutiladigan natija:** kamida 3 ta xato va ularning to'g'ri varianti.

### 9. PATCH qo'shing <Badge type="danger" text="qiyin" />
`app.py` ga `PATCH /api/books/<id>` qo'shing: faqat yuborilgan maydonlarni yangilasin. Yo'q kitobga 404, noto'g'ri JSON'ga 400 qaytarsin.

**Kutiladigan natija:** `{"available": false}` yuborilganda faqat shu maydon o'zgaradi.

### 10. Yangi resurs: mualliflar <Badge type="danger" text="qiyin" />
`/api/authors` va `/api/authors/<id>` uchun GET va POST endpointlarini qo'shing. Ierarxik URL ham o'ylab toping: muallifning kitoblari.

**Kutiladigan natija:** ishlaydigan endpointlar va ierarxik URL taklifi (masalan, `GET /api/authors/1/books`).

### 11. Dizayn hujjati <Badge type="danger" text="qiyin" />
Kutubxona API'ning to'liq endpointlar jadvalini yozing (metod, URI, status kodlar, qisqa izoh). Kamida 8 endpoint.

**Kutiladigan natija:** `library-api/README.md` da jadval.

### 12. ETag tadqiqoti <Badge type="info" text="bonus" />
`GET /api/books/1` javobiga `ETag` qo'shing; `If-None-Match` mos kelsa `304` qaytaring. `curl -i` bilan ko'rsating.

**Kutiladigan natija:** ikkinchi so'rov 304 qaytaradi, tana bo'sh.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. REST'da «resurs» va «URI» nima?
2. PUT va PATCH farqi nima?
3. Qaysi metodlar idempotent va nega bu retry uchun muhim?
4. 401 va 403 qanday farq qiladi?
5. Stateless nima beradi?
6. `Content-Type` va `Accept` nima uchun kerak?
7. 304 kodi qachon qaytariladi?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

`library-api/` ga kamida 3 ta endpoint qo'shing (masalan, PATCH, mualliflar), har biri to'g'ri status kod qaytarsin, `README.md` da endpointlar jadvalini yozing. Natijani Pull Request qiling (20–30 daqiqa). Shartlar `uyga-vazifa.md` da.

</div>

