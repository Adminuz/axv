---
title: "12-dars. REST API va JSON asoslari: JSON formati, kontrakt va xavfsizlik"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "11-sinf", "link": "/11-sinf/"}, "week": {"n": 4, "link": "/11-sinf/hafta-04/"}, "g": 12, "title": "REST API va JSON asoslari: JSON formati, kontrakt va xavfsizlik", "lead": "API ning yuragi: JSON kontrakti. Maydonlar nomi, xato formati va xavfsizlik qoidalari bo'yicha mijoz va server o'rtasida «kelishuv» tuzamiz.", "slide": "/slaydlar/11-sinf/hafta-04/dars-3.html", "test": null, "tabs": [{"g": 10, "link": "/11-sinf/hafta-04/dars-1", "current": false}, {"g": 11, "link": "/11-sinf/hafta-04/dars-2", "current": false}, {"g": 12, "link": "/11-sinf/hafta-04/dars-3", "current": true}], "prev": {"g": 11, "title": "REST API va JSON asoslari: REST tamoyillari va HTTP", "link": "/11-sinf/hafta-04/dars-2"}, "next": null}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **JSON** — yengil, tilga bog'liq bo'lmagan ma'lumot formati. Tuzilmalari: obyekt `{}`, array `[]`, string, number, boolean, null.
- **Serializatsiya** (obyekt → JSON matni) va **deserializatsiya** (JSON → obyekt): Python'da `json.dumps` va `json.loads`.
- **Kontrakt:** maydon nomlari, turlari, ma'nosi va xato ko'rinishi bo'yicha kelishuv. Nomlash izchil (`snake_case` yoki `camelCase`), `id` formati yagona.
- **Sana va pul:** sana ISO-8601 UTC; pul butun son (tiyin) yoki decimal satr.
- **Error envelope:** barcha xatolar `{"error": {"code", "message", "details"}}` formatida.
- **Paginatsiya/filtr/saralash:** `limit`, `offset`, `status=paid`, `sort=-created_at`.
- **Versiyalash:** `/api/v1/` → `/api/v2/`; maydonni olib tashlash — breaking change.
- **Xavfsizlik:** HTTPS, Bearer/JWT, 401/403, CORS, rate limit (429), sirlarni kodga yozmaslik, `password_hash` javobda bo'lmasligi.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. JSON va Python o'rtasidagi moslik

| JSON | Python |
|---|---|
| obyekt `{}` | `dict` |
| array `[]` | `list` |
| string | `str` |
| number | `int` / `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

Eng ko'p uchraydigan sintaksis xatolari: bir tirnoq (`'id'`), oxirgi elementdan keyingi vergul, tirnoqsiz kalit.

### 2. `null` va «maydon yo'q» bir narsa emas

`{"middle_name": null}` — «otasining ismi ma'lum, lekin bo'sh». Maydonning umuman yo'qligi esa «qo'llanmaydi yoki noma'lum» degani. Mijoz kodi bu ikkisini farqlashi mumkin, shuning uchun aralashtirmang.

### 3. Pul nega `float` bo'lmasligi kerak?

Kasr sonlar kompyuterda taxminiy saqlanadi, yaxlitlash xatolari yig'ilib ketadi. Shuning uchun pul ko'pincha butun son (tiyin) yoki decimal satr sifatida yuboriladi: `"amount": 125000`.

### 4. Breaking change misoli

Javobda `"author": "Qodiriy"` (satr) bor edi. Uni `"author": {"name": "Qodiriy"}` (obyekt) qilsangiz, eski mijozlar to'xtab qoladi. Yangi maydon qo'shish (`author_details`) esa eski mijozlarga ta'sir qilmaydi. Shu sababli buzuvchi o'zgarishlar yangi versiyada (`v2`) chiqariladi.

### 5. Stack trace nega mijozga chiqmaydi?

Ichki istisno izlari server tuzilishi haqida ma'lumot beradi (hujumchiga foyda). Prodda ular logga yoziladi, mijoz esa `500` va umumiy xabar oladi.

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **JSON** | JavaScript Object Notation: yengil ma'lumot almashish formati |
| **Serializatsiya** | Obyektni JSON matniga aylantirish |
| **Deserializatsiya** | JSON matnini obyektga aylantirish |
| **Kontrakt** | Mijoz va server o'rtasidagi maydonlar va xatolar bo'yicha kelishuv |
| **Error envelope** | Barcha xatolar uchun yagona JSON konvert |
| **Paginatsiya** | Natijani sahifalarga bo'lish (`limit`/`offset`, cursor) |
| **Backward compatibility** | Orqaga moslik: eski mijozlar yangi API bilan ham ishlaydi |
| **Breaking change** | Eski mijozlarni buzadigan o'zgarish |
| **Bearer token** | `Authorization: Bearer <token>` bilan yuboriladigan kirish tokeni |
| **JWT** | JSON Web Token: autentifikatsiya uchun ishlatiladigan token |
| **CORS** | Brauzerdan boshqa domenga so'rovlarni boshqarish siyosati |
| **Rate limiting** | So'rovlar tezligini cheklash (429) |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- JSON nomida JavaScript bor, lekin u deyarli barcha dasturlash tillarida qo'llab-quvvatlanadi.
- Ba'zi tillarda juda katta butun sonlar (64-bitli ID) JSON number sifatida aniqligini yo'qotadi, shuning uchun ular satr sifatida beriladi (qo'llanmada eslatilgan).
- Standart xato formati bo'lgani uchun frontend dasturchi formadagi mos inputni avtomatik qizil qila oladi.
- OWASP tashkiloti API xavfsizligi bo'yicha «Top 10» ro'yxatini yuritadi; o'quv qo'llanmasi uni muntazam audit qilishni tavsiya etadi.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. JSON yozing <Badge type="tip" text="oson" />
Kitobni JSON obyekti qiling: `id`, `title`, `author`, `available` (boolean), `tags` (2 ta element), `isbn` (noma'lum).

**Kutiladigan natija:** to'g'ri sintaksisli JSON.

### 2. Xatolarni toping <Badge type="tip" text="oson" />
Bu JSON'da 3 ta xato bor: `{'id': 1, "title": "Sarob", "tags": ["a", "b",], available: true}`. Topib tuzating.

**Kutiladigan natija:** 3 ta xato va to'g'ri variant.

### 3. Turlarni moslang <Badge type="tip" text="oson" />
Python qiymatlari JSON'da qanday yoziladi: `None`, `True`, `{"a": 1}`, `[1, 2]`?

**Kutiladigan natija:** 4 ta juftlik.

### 4. Nomlashni tuzating <Badge type="tip" text="oson" />
Bu maydonlar aralash uslubda: `user_id`, `createdAt`, `Total_Amount`. Bir uslubni tanlab, hammasini qayta nomlang.

**Kutiladigan natija:** izchil nomlar va tanlov sababi.

### 5. Serializatsiya <Badge type="warning" text="o'rta" />
`json.dumps` va `json.loads` bilan lug'atni matnga va qaytib lug'atga aylantiring. `None` va `False` ning JSON ko'rinishini ko'rsating.

**Kutiladigan natija:** `null` va `false` ko'rinadigan chiqish.

### 6. Xato konverti <Badge type="warning" text="o'rta" />
`error()` va `validate_book()` funksiyalarini yozing. `{"title": "", "year": "1926"}` uchun xato konvertini hosil qiling.

**Kutiladigan natija:** `details` da 2 ta element.

### 7. Bashorat qiling <Badge type="warning" text="o'rta" />
`query_books(books, "/api/v1/books?sort=title&limit=2&offset=1")` nimani qaytaradi? (Darsdagi 3 ta kitob bilan.) Avval taxmin qiling, keyin ishga tushiring.

**Kutiladigan natija:** taxmin va natija taqqoslanadi; `total` qiymati to'g'ri tushuntiriladi.

### 8. Sanani va pulni to'g'ri yozing <Badge type="warning" text="o'rta" />
Buyurtma JSON'ida `created_at` (ISO-8601 UTC) va `total_amount` (125 000 so'm) maydonlarini yozing. Pul uchun qaysi turni tanladingiz va nega?

**Kutiladigan natija:** JSON va 1–2 jumlali asos.

### 9. Maxfiy maydonni yashiring <Badge type="danger" text="qiyin" />
`public_user()` funksiyasini yozing va foydalanuvchi lug'atidan `password_hash` chiqmasligini ko'rsating. Yana qaysi maydonlar javobda bo'lmasligi kerak (kamida 2 ta misol)?

**Kutiladigan natija:** ishlaydigan funksiya va ro'yxat.

### 10. 401 yoki 403? <Badge type="danger" text="qiyin" />
`check_access()` ni yozing va 4 ta holatni sinang: token yo'q; noto'g'ri token; `reader` admin amalida; `admin` admin amalida. Natijalarni oldindan taxmin qiling.

**Kutiladigan natija:** 401, 401, 403, 200.

### 11. Versiyalash qarori <Badge type="danger" text="qiyin" />
Kitob javobida `author` satr edi, endi obyekt bo'lishi kerak. Eski mijozlarni buzmaslik uchun ikki xil yechim taklif qiling (v2 yoki yangi maydon) va birini tanlab asoslang.

**Kutiladigan natija:** ikki variant, tanlov va yangi JSON namunasi.

### 12. To'liq kontrakt hujjati <Badge type="info" text="bonus" />
`library-api/CONTRACT.md` yozing: kitob JSON tuzilmasi (maydon, tur, majburiy yoki yo'q), xato konverti, paginatsiya parametrlari, versiyalash qoidasi.

**Kutiladigan natija:** bir sahifalik hujjat; boshqa dasturchi faqat shu hujjatga qarab mijoz yoza oladi.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. JSON'ning 6 ta tuzilmasini ayting.
2. `null` va maydonning yo'qligi qanday farq qiladi?
3. Error envelope ichida qaysi uch maydon bor?
4. Qaysi o'zgarish orqaga mos, qaysi biri buzuvchi?
5. `limit/offset` va cursor paginatsiyasi qachon ishlatiladi?
6. 401 va 403 farqi nima?
7. Nega sirlar (token, parol) kodga va gitga yozilmaydi?
8. Rate limiting qaysi status kodni qaytaradi?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

`library-api/` ga `contract.py` ni qo'shing, `validate_book`, `query_books`, `public_user` va `check_access` uchun testlar yozing, `CONTRACT.md` ni tayyorlang va Pull Request oching (20–30 daqiqa). Shartlar `uyga-vazifa.md` da.

</div>

