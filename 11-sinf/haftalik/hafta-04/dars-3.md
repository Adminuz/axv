# 12-dars. REST API va JSON asoslari: JSON formati, kontrakt va xavfsizlik

**Hafta:** 4 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + kod amaliyoti · **I-bob**, 12-dars (umumiy 1–51)

**Manba:** o'quv qo'llanma, «REST API va JSON asoslari» ma'ruzasi, «JSON formati va kontrakt dizayni» (1.14 va 1.15-jadvallar) hamda «Amaliyot va xavfsizlik» (1.16 va 1.17-jadvallar) bo'limlari; o'quv dasturi, shu mavzu natijalari.

## 1. Dars rejasi

**Maqsad:** o'quvchi JSON tuzilmalari va turlarini, serializatsiya/deserializatsiyani biladi; JSON kontrakti, yagona xato formati (error envelope), paginatsiya/filtrlash/saralash, versiyalash va moslik (backward compatibility) tamoyillarini qo'llaydi; autentifikatsiya (Bearer/JWT), CORS, tezlikni cheklash va sirlar bilan ishlashning asosiy qoidalarini biladi.

**Kutiladigan natija:**
- JSON'ning 6 ta tuzilmasini (obyekt, massiv, string, number, boolean, null) farqlaydi va to'g'ri JSON yozadi.
- Python `json.dumps` / `json.loads` bilan serializatsiya va deserializatsiyani bajaradi.
- `snake_case` / `camelCase`, ISO-8601 UTC sana, pulni butun son bilan saqlash qoidalarini qo'llaydi.
- Yagona `error` konvertini (`code`, `message`, `details`) loyihalaydi.
- `limit`/`offset`, `status=...`, `sort=-created_at` parametrlarini ishlatadi.
- Xavfli maydonni (`password_hash`) javobdan chiqarib tashlaydi.
- 401 va 403, Bearer token, CORS va 429 ni to'g'ri ishlatadi.
- «Kutubxona boshqaruvi» API'ga kontrakt qatlamini qo'shadi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va kirish | 11-dars: metodlar, status kodlari. Savol: «Server `400` qaytardi, lekin sababi nima? Mijoz buni qanday biladi?» |
| 10–35 daq | Yangi mavzu | JSON tuzilmalari va turlari; kontrakt; error envelope; paginatsiya/filtrlash/saralash; versiyalash; xavfsizlik (Bearer/JWT, CORS, rate limit, sirlar) |
| 35–40 daq | Tanaffus | Harakatli tanaffus |
| 40–65 daq | Amaliyot | `json` moduli; xato konverti; so'rov parametrlari; `password_hash`; 401/403 |
| 65–75 daq | Tezkor nazorat | 5 ta savol |
| 75–80 daq | Xulosa va uyga vazifa | 5-haftaga ko'prik: jamoada muloqot |

---

## 2. Dars konspekti

### 2.1. JSON nima?

**JSON (JavaScript Object Notation)** — veb-xizmatlar o'rtasida ma'lumot almashishning eng ommabop, yengil va o'qilishi oson formati; tilga bog'liq emas va HTTP bilan tabiiy ishlaydi (RESTda de-fakto standart).

| Tuzilma | Belgisi | Izohi | Misol |
|---|---|---|---|
| Obyekt | `{}` | kalit–qiymat juftliklari | `{"id":1,"name":"Ali"}` |
| Array | `[]` | tartibli ro'yxat | `["new","paid","shipped"]` |
| String | `"..."` | matn | `"hello"` |
| Number | `123` | butun yoki o'nlik | `125000` |
| Boolean | `true/false` | mantiqiy | `false` |
| Null | `null` | ma'lum, lekin bo'sh | `{"middle_name":null}` |

Qoidalar: kalitlar va matnlar **qo'sh tirnoqda**, oxirgi elementdan keyin vergul yo'q, izoh yo'q.

**Serializatsiya** — Python obyektini JSON matniga aylantirish; **deserializatsiya** — teskarisi.

```python
import json

text = json.dumps({"id": 1, "middle_name": None, "paid": False, "tags": ["new"]})
print(text)
back = json.loads(text)
print(type(back), back["middle_name"], back["paid"])
```

Tekshirilgan natija:

```text
{"id": 1, "middle_name": null, "paid": false, "tags": ["new"]}
<class 'dict'> None False
```

Moslik: Python `None` ↔ JSON `null`, `True/False` ↔ `true/false`, `dict` ↔ obyekt, `list` ↔ array.

### 2.2. JSON kontrakti

REST'da JSON — «kontrakt» tashuvchisi: mijoz va server maydonlar tuzilmasi, ma'nosi, turlari, cheklovlari, xato ko'rinishi va versiyalash qoidalari haqida kelishadi. Kontrakt — shunchaki javob namunasi emas, u API barqarorligini belgilaydi.

Dizayn qoidalari (qo'llanma):
- **Izchil nomlash:** butun API bo'ylab yoki `snake_case` (`created_at`), yoki `camelCase` (`createdAt`); aralashtirmang.
- **Yagona `id` formati:** hammasida butun son, yoki hammasida UUID, yoki domen identifikatori (`"ORD-001"`).
- **Sana-vaqt:** ISO-8601, UTC: `"2025-11-24T15:00:00Z"`.
- **Pul:** butun son (tiyin) yoki decimal satr; `float` tavsiya etilmaydi (yaxlitlash xatolari).
- **Katta sonlar** (64-bitli ID, karta raqami) ba'zi tillarda aniqlikni yo'qotadi, shuning uchun satr sifatida beriladi.
- **`null` ≠ maydon yo'q:** `null` — «ma'lum, lekin bo'sh»; maydonning yo'qligi — «qo'llanmaydi yoki noma'lum».
- Sarlavhalar: `Content-Type: application/json; charset=utf-8`, mijoz `Accept: application/json`.

Katta jamoalarda kontrakt **JSON Schema** yoki **OpenAPI (Swagger)** bilan rasmiylashtiriladi (turlar, `required`, min/max, enum, regex); undan validatsiya kodi, SDK va hujjat avtomatik hosil bo'ladi. Rollar: Product Owner, backend, frontend/mobile, QA, DevOps — hammasi bitta kontraktga tayanadi.

### 2.3. Barqaror evolyutsiya va versiyalash

- Mavjud maydonning ma'nosini o'zgartirmang.
- **Yangi maydon qo'shish** — odatda orqaga mos (backward compatible).
- **Maydonni olib tashlash yoki ma'nosini o'zgartirish** — buzuvchi o'zgarish (**breaking change**).
- Buzuvchi o'zgarish bo'lsa, yangi versiya: `/api/v1/...` → `/api/v2/...`; eski mijozlarga ko'chish uchun vaqt beriladi, v1 uchun «deprecation» e'lon qilinadi.

### 2.4. Yagona xato formati (error envelope)

Har servis xatoni o'zicha yuborsa, mijozda birlashtirish qiyin. Shuning uchun bitta konvert:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Some fields are invalid",
    "details": [
      { "field": "email", "error": "invalid_format" }
    ]
  }
}
```

- `code` — mashinaga qulay (enum kabi);
- `message` — odamga tushunarli;
- `details` — maydonlar bo'yicha batafsil ro'yxat (`field`, `error`).

Frontend shu formatga tayanib mos inputni qizil qilishi mumkin. Muhim: **stack trace hech qachon mijozga chiqmaydi**; prodda loglarga yoziladi, mijoz `500` + umumiy xabar oladi.

### 2.5. Paginatsiya, filtrlash, saralash

| Maqsad | Misol |
|---|---|
| Paginatsiya (limit/offset) | `GET /api/v1/orders?limit=20&offset=40` |
| Paginatsiya (cursor) | javobda `next_cursor`; keyingi sahifa `?cursor=...` |
| Filtr | `status=paid`, `from=2024-01-01&to=2024-01-31`, `status=paid,shipped` |
| Saralash | `sort=-created_at` (minus — teskari tartib) |

Kichik hajmda `limit/offset` yetadi; katta oqimlarda cursor barqarorroq.

### 2.6. Kontrakt kodi (Python)

Kod `library-api/contract.py` fayliga yoziladi.

```python
import json
from urllib.parse import urlparse, parse_qs


def error(code, message, details=None):
    """Yagona xato konverti (error envelope)."""
    return {"error": {"code": code, "message": message, "details": details or []}}


def validate_book(data):
    """Xatolar ro'yxatini qaytaradi (bo'sh ro'yxat = hammasi joyida)."""
    details = []
    if not isinstance(data.get("title"), str) or not data["title"].strip():
        details.append({"field": "title", "error": "required"})
    if "year" in data and not isinstance(data["year"], int):
        details.append({"field": "year", "error": "invalid_type"})
    return details


def query_books(books, url):
    """GET /api/v1/books?available=true&sort=-title&limit=2&offset=0"""
    q = {k: v[0] for k, v in parse_qs(urlparse(url).query).items()}
    items = list(books)
    if "available" in q:
        items = [b for b in items if b["available"] == (q["available"] == "true")]
    if "sort" in q:
        field = q["sort"].lstrip("-")
        items.sort(key=lambda b: b[field], reverse=q["sort"].startswith("-"))
    total = len(items)
    limit, offset = int(q.get("limit", 20)), int(q.get("offset", 0))
    return {"items": items[offset:offset + limit], "total": total, "limit": limit, "offset": offset}


def public_user(user):
    """Javobga ichki maydonlarni chiqarmaymiz."""
    return {k: v for k, v in user.items() if k != "password_hash"}
```

Sinash:

```python
books = [
    {"id": 1, "title": "Sarob", "available": True},
    {"id": 2, "title": "O'tkan kunlar", "available": False},
    {"id": 3, "title": "Mehrobdan chayon", "available": True},
]
print(json.dumps(error("VALIDATION_ERROR", "Some fields are invalid", validate_book({"year": "1926"})), ensure_ascii=False))
print(json.dumps(query_books(books, "/api/v1/books?available=true&sort=-title&limit=1"), ensure_ascii=False))
print(public_user({"id": 1, "email": "a@b.uz", "password_hash": "x9f"}))
```

Tekshirilgan natija:

```text
{"error": {"code": "VALIDATION_ERROR", "message": "Some fields are invalid", "details": [{"field": "title", "error": "required"}, {"field": "year", "error": "invalid_type"}]}}
{"items": [{"id": 1, "title": "Sarob", "available": true}], "total": 2, "limit": 1, "offset": 0}
{'id': 1, 'email': 'a@b.uz'}
```

### 2.7. Xavfsizlik (1.17-jadval)

| Komponent | Daraja | Vazifasi |
|---|---|---|
| TLS (HTTPS) | transport | trafikni shifrlash, sniffing va MITM'dan himoya |
| Autentifikatsiya (JWT/OAuth2/API key) | ilova | foydalanuvchini aniqlash |
| Avtorizatsiya (RBAC/ABAC) | ilova | kim nimaga ruxsatli |
| CORS/CSRF | brauzer | cross-origin va soxta so'rovlardan himoya |
| Rate limiting / Throttling | API gateway | haddan tashqari so'rovlar, botlar |
| WAF va input validatsiya | perimetr/ilova | injeksiya va xavfli naqshlarni bloklash |
| Secrets management | infratuzilma | token, kalit, parolni xavfsiz saqlash |

Asosiy qoidalar:
- **HTTPS (TLS) — qat'iy talab.**
- **Bearer/JWT:** `Authorization: Bearer <jwt>`. JWT'da qisqa umrli access token va uzoq umrli refresh token; `scope`/rol orqali ruxsat (RBAC).
- **Resurs darajasidagi ruxsat API'da tekshiriladi:** `GET /users/{id}` da server token ichidagi foydalanuvchi shu `id` ga tengligini tekshiradi. Buni faqat UI'ga topshirib bo'lmaydi.
- **CORS:** `Access-Control-Allow-Origin` aniq domenlar bilan cheklanadi, `*` tavsiya etilmaydi; brauzer ba'zan oldin `OPTIONS` (preflight) so'rov yuboradi.
- **Rate limiting:** `429 Too Many Requests` + `RateLimit-Limit`, `RateLimit-Remaining`, `RateLimit-Reset` sarlavhalari.
- **Javobda sir yo'q:** `password_hash`, token, ichki identifikator chiqmasin.
- **Kiruvchi JSON qat'iy validatsiya** qilinadi (tur, majburiy maydon, uzunlik, naqsh, enum).
- **Sirlar kodda emas:** `.env` yoki secrets manager'da; hech qachon gitda.

Muhitlar (1.16-jadval): **Dev** (dasturchi), **Stage** (prodga yaqin sinov), **Prod** (real foydalanuvchilar). Kod bir xil, konfiguratsiya (URL, DB, sirlar) farq qiladi.

### 2.8. 401/403 mantig'i (Python)

O'quv uchun soxta tokenlar (haqiqiy JWT emas; JWT imzosini tekshirish keyingi mavzularda kutubxona bilan qilinadi):

```python
TOKENS = {"tok-ali": "reader", "tok-admin": "admin"}


def check_access(auth_header, need_role):
    """401 = kim ekanligi noma'lum; 403 = kim ekanligi ma'lum, lekin ruxsat yo'q."""
    if not auth_header or not auth_header.startswith("Bearer "):
        return 401
    role = TOKENS.get(auth_header[len("Bearer "):])
    if role is None:
        return 401
    if need_role == "admin" and role != "admin":
        return 403
    return 200


print(check_access(None, "admin"))                 # 401
print(check_access("Bearer tok-ali", "admin"))     # 403
print(check_access("Bearer tok-admin", "admin"))   # 200
```

### 2.9. Sinash va hujjatlash

Postman (yoki Insomnia) bilan CRUD oqimi, paginatsiya, filtr, xatolik javoblari qo'lda tekshiriladi; keyin unit va integratsion testlar yoziladi va CI'ga ulanadi. Testlar faqat «to'g'ri yo'l»ni emas, xatolarni ham qamrab olsin: noto'g'ri `Content-Type`, majburiy maydon yo'q, noto'g'ri enum, ruxsatsiz so'rovda 401/403, yo'q resursda 404, kolliziyada 409. Loglarda har so'rovga `trace-id` / `X-Request-ID` biriktiriladi.

---

## 3. Amaliy mashg'ulot (mini-loyiha: «Kutubxona boshqaruvi», 3-bosqich)

### 1-mashq (oson). To'g'ri JSON yozish
**Vazifa:** kitobni JSON obyekti sifatida yozing: `id` (son), `title`, `author`, `available` (boolean), `tags` (massiv, 2 ta element), `isbn` (hozircha noma'lum, `null`).

**Kutiladigan natija:** to'g'ri sintaksisli JSON.

**Yechim:**
```json
{
  "id": 7,
  "title": "O'tkan kunlar",
  "author": "Abdulla Qodiriy",
  "available": true,
  "tags": ["roman", "klassika"],
  "isbn": null
}
```

### 2-mashq (oson). Xatoni topish
**Vazifa:** bu JSON'da 3 ta sintaksis xatosi bor. Toping: `{'id': 1, "title": "Sarob", "tags": ["a", "b",], available: true}`.

**Kutiladigan natija:** 3 ta xato va tuzatilgan variant.

**Yechim:** (1) `'id'` bir tirnoqda: JSON'da faqat qo'sh tirnoq; (2) massivda oxirgi vergul `"b",`; (3) `available` kaliti tirnoqsiz. To'g'ri: `{"id": 1, "title": "Sarob", "tags": ["a", "b"], "available": true}`.

### 3-mashq (o'rta). Serializatsiya
**Vazifa:** Python lug'ati `{"id": 1, "middle_name": None, "paid": False}` ni `json.dumps` bilan matnga, keyin `json.loads` bilan qaytaring. `None` va `False` JSON'da qanday yozilishini ko'rsating.

**Kutiladigan natija:** `{"id": 1, "middle_name": null, "paid": false}`.

**Yechim:** 2.1-bo'limdagi kod. `None` → `null`, `False` → `false`.

### 4-mashq (o'rta). Xato konverti
**Vazifa:** `contract.py` ni yozing. `validate_book({"title": "", "year": "1926"})` ni chaqirib, natijani `error("VALIDATION_ERROR", ...)` ichiga o'rang. Qaysi HTTP status mos?

**Kutiladigan natija:** `details` da 2 ta element; status 400 (dasturda 422 ham tilga olingan).

**Yechim:**
```python
d = validate_book({"title": "", "year": "1926"})
print(error("VALIDATION_ERROR", "Some fields are invalid", d))
# details: title required, year invalid_type -> status 400
```

### 5-mashq (o'rta). Filtr, saralash, paginatsiya
**Vazifa:** 2.6-bo'limdagi `books` ro'yxati bilan `query_books(books, "/api/v1/books?sort=title&limit=2&offset=1")` ni chaqiring va natijani oldindan bashorat qiling.

**Kutiladigan natija:** nomi bo'yicha o'sish tartibi: Mehrobdan chayon, O'tkan kunlar, Sarob; `offset=1` — birinchisi o'tkazib yuboriladi, `limit=2` — ikkitasi: O'tkan kunlar va Sarob; `total` = 3.

**Yechim:** `{"items": [{"id": 2, ...O'tkan kunlar}, {"id": 1, ...Sarob}], "total": 3, "limit": 2, "offset": 1}`.

### 6-mashq (qiyin). Sirni yashirish va 401/403
**Vazifa:** (a) `public_user` yordamida foydalanuvchini qaytaring va `password_hash` chiqmasligini isbotlang. (b) `check_access` ni 4 ta holatda sinang: token yo'q, noto'g'ri token, `reader` admin amalida, `admin` admin amalida. Kutilgan kodlarni oldindan yozing.

**Kutiladigan natija:** 401, 401, 403, 200.

**Yechim:** 2.6 va 2.8 bo'limlari kodi. Noto'g'ri token — 401 (kim ekanligi noma'lum); `reader` — 403 (ruxsat yo'q).

### 7-mashq (qiyin). Kontraktni buzmay o'zgartirish
**Vazifa:** API javobida `author` (satr) maydoni bor. Endi muallifni obyekt qilish kerak: `{"name": "...", "born": 1894}`. Eski mijozlarni buzmaslik uchun nima qilasiz? Yangi JSON namunasini va URL'ni yozing.

**Kutiladigan natija:** buzuvchi o'zgarish aniqlanadi; `v2` yoki yangi maydon taklif etiladi.

**Yechim:** `author` ning turini satrdan obyektga o'zgartirish — breaking change. Variant 1: `/api/v2/books` da `author` obyekt, `/api/v1/books` o'zgarishsiz (deprecation e'lon qilinadi). Variant 2 (orqaga mos): `author` satr bo'lib qoladi, yangi maydon `author_details: {"name": "...", "born": 1894}` qo'shiladi.

### 8-mashq (bonus). Bearer bilan haqiqiy so'rov
**Vazifa:** `app.py` (11-dars) da `DELETE` uchun `check_access(self.headers.get("Authorization"), "admin")` ni chaqiring: 401/403 bo'lsa error konvertida javob bering. `curl -H "Authorization: Bearer tok-admin"` bilan sinang.

**Yechim:** (ixtiyoriy)
```python
    def do_DELETE(self):
        status = check_access(self.headers.get("Authorization"), "admin")
        if status != 200:
            code = "UNAUTHORIZED" if status == 401 else "FORBIDDEN"
            return self.send_json(status, error(code, "Ruxsat yo'q"))
        ...
```

---

## 4. Tezkor savollar

1. JSON'ning 6 ta tuzilmasini ayting.
   - **Javob:** obyekt `{}`, array `[]`, string, number, boolean, null.
2. Error envelope nima uchun kerak?
   - **Javob:** Barcha endpointlar xatoni bir xil formatda (`code`, `message`, `details`) qaytarsin: mijoz xatoni birxil qayta ishlaydi.
3. Qaysi o'zgarish «breaking change»?
   - **Javob:** Mavjud maydonni olib tashlash yoki ma'nosini/turini o'zgartirish. Yangi maydon qo'shish odatda orqaga mos.
4. Nega `password_hash` javobda bo'lmasligi kerak?
   - **Javob:** Ichki/maxfiy ma'lumot; javobda sizib chiqishi xavfsizlik zaifligi.
5. CORS da nega `*` tavsiya etilmaydi?
   - **Javob:** Har qanday domendan brauzer so'roviga ruxsat beradi; aniq ishonchli domenlar ro'yxati xavfsizroq.

## 5. Mentor uchun eslatmalar

- 11-dars uyga vazifasini (kutubxona API endpointlari) dars boshida ko'ring.
- Qo'llanma JWT, OAuth2, CORS, rate limit'ni nazariy bayon qiladi; imzo tekshirish kodi yo'q. Shuning uchun amaliyotda soxta token lug'ati ishlatildi: buni o'quvchiga ochiq ayting.
- Postman dasturi mavjud bo'lmasa, `curl` yoki Python `urllib` bilan davom eting.
- Qo'llanmadagi 1.16-jadval (Dev/Stage/Prod) 28–30-darslarda (CD, env/secrets) chuqurlashadi: bu yerda faqat tanishtirish.
- 11 va 12-darslar kodi `library-api/` papkasida portfolio repozitoriyga commit qilinsin (semantik commit: `feat(api): add error envelope`).
- Python `json` va `urllib.parse` kodi dars oldidan tekshirilgan.
