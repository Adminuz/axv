# 7-dars. Pagination va throttling

> Millionlab foydalanuvchilar bir vaqtda kirganda serveringiz bardosh bera oladimi? Ushbu darsda biz katta ma'lumotlarni sahifalab uzatish (Pagination) va tizimni ortiqcha yuklama hamda bot hujumlaridan himoyalash (Throttling / Rate limiting) texnologiyalarini o'rganamiz.

## Dars xulosasi

- **Pagination (Sahifalash)** — ma'lumotlar bazasidagi minglab yozuvlarni bir vaqtda emas, balki qismlarga bo'lib (masalan, 10 tadan) mijozga taqdim etish usulidir.
- Pagination bo'lmasa, server operativ xotirasi (RAM) to'lib qoladi, ma'lumotlar uzatish sekinlashadi va mobil qurilmalarda ilovalar qotib qoladi.
- DRF da **PageNumberPagination** (sahifa raqami bo'yicha), **LimitOffsetPagination** va **CursorPagination** (kursor asosida, cheksiz tasmalar uchun) turlari mavjud.
- Sahifalangan javob har doim 4 ta asosiy maydondan iborat bo'ladi: `count` (umumiy soni), `next` (keyingi sahifa), `previous` (oldingi sahifa) va `results` (joriy ma'lumotlar).
- **Throttling (Rate Limiting)** — bir foydalanuvchi yoki IP manzilning ma'lum vaqt birligida (masalan, 1 daqiqada) yuborishi mumkin bo'lgan so'rovlari sonini cheklovchi xavfsizlik qalqonidir.
- Limitdan oshganda server darhol **`429 Too Many Requests`** xatosini beradi va tizimni DoS hamda brute-force hujumlaridan himoya qiladi.

## Qo'shimcha ma'lumot

### 1. Kitob va Sahifalar analogiyasi: Pagination

Tasavvur qiling, 1000 sahifalik qalin ensiklopediya bor:
- **Pagination bo'lmaganda:** Siz kitob javonidan 1000 ta sahifaning barchasini birdaniga bitta ulkan rulon qilib chiqarib, o'quvchining ustiga tashlaysiz. O'quvchi bu qog'ozlar tagida qolib ketadi va hech narsani o'qiy olmaydi.
- **Pagination bilan:** Siz o'quvchiga: "Mana 1-sahifa (10 ta maqola), o'qib bo'lgach, pastdagi 'Keyingi' tugmasini bosing", deysiz. Bu ham o'quvchi uchun, ham kitobxona uchun o'ta qulay va yengil!

### 2. Nima uchun CursorPagination ijtimoiy tarmoqlar uchun eng yaxshisi?

Ko'p yangilik qo'shiladigan tizimlarda (Instagram, Twitter / X) oddiy `PageNumberPagination` muammo keltirib chiqarishi mumkin:
- Siz 1-sahifada 10 ta postni ko'ryapsiz.
- Ayni shu soniyada boshqa foydalanuvchilar bazaga 3 ta yangi post qo'shishdi.
- Siz 2-sahifaga o'tganingizda, 1-sahifadagi oxirgi 3 ta post pastga siljib, 2-sahifaning boshida yana qaytadan chiqadi (dublikat ma'lumot)!
**CursorPagination** esa sahifa raqamiga emas, aynan oxirgi ko'rilgan postning vaqt belgisi yoki kursoriga tayanadi. Yangi postlar qo'shilsa ham, foydalanuvchi hech qachon dublikat ko'rmaydi.

### 3. Throttling qanday qilib pul va serverni tejaydi?

Ko'plab kompaniyalar (OpenAI, Google Maps, SMS xizmatlari) o'z API laridan foydalanganlik uchun har bir so'rovga pul oladi.
Agar sizning serveringizda Throttling bo'lmasa:
- Bitta xakerlik boti sizning SMS yuborish endpointingizga 1 daqiqa ichida 50 000 ta so'rov yuborishi va kompaniyangizni bir zumda millionlab so'm qarzga kiritishi mumkin!
- Throttling qo'yilganda esa: bitta IP dan minutiga 5 tadan ortiq SMS so'rovi kelsa, server darhol `429 Too Many Requests` bilan botni to'xtatadi.

### 4. Dasturchilar ko'p yo'l qo'yadigan xatolar

- **Xato 1: `max_page_size` parametrini bermaslik.** Agar siz `page_size_query_param = "page_size"` qilib, lekin `max_page_size` ni cheklamasangiz, xaker ataylab `?page_size=1000000` deb so'rov yuborishi va baribir serverni to'xtatib qo'yishi mumkin! Har doim maksimal chegarani (masalan 100) belgilang.
- **Xato 2: Cache sozlamalarini unutish.** DRF Throttling hisob-kitobni keshda saqlaydi. Agar loyihangizda Redis yoki to'g'ri kesh sozlanmagan bo'lsa, har bir so'rovda rate limitni tekshirish uchun bazaga ortiqcha yuk tushishi mumkin.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Pagination** | Ma'lumotlar to'plamini kichik va boshqariladigan sahifalarga bo'lib chiqarish jarayoni. |
| **PageNumberPagination** | Aniq sahifa raqami (`?page=1`) va sahifa hajmi (`?page_size=10`) orqali sahifalash. |
| **CursorPagination** | Yuqori tezlikdagi dinamik oqimlar uchun kursor va vaqt belgisi orqali sahifalash. |
| **Throttling (Rate Limiting)** | Vaqt birligi ichida bitta foydalanuvchi yoki IP manzil yubora oladigan so'rovlar chegarasi. |
| **429 Too Many Requests** | So'rovlar soni belgilangan me'yordan oshib ketganligini bildiruvchi HTTP status kodi. |
| **Brute-Force** | Parol yoki maxfiy kalitlarni bittalab ketma-ket taxmin qilish orqali tizimni buzishga urinish. |
| **DoS (Denial of Service)** | Serverni son-sanoqsiz so'rovlar bilan to'ldirib, uni oddiy foydalanuvchilar uchun ishdan chiqarish hujumi. |
| **AnonRateThrottle** | Tizimga kirmagan anonim mehmonlar uchun so'rovlar tezligini cheklovchi klass. |
| **UserRateThrottle** | Ro'yxatdan o'tgan foydalanuvchilar uchun so'rovlar tezligini cheklovchi klass. |
| **Retry-After** | 429 xatosi bilan birga qaytariladigan, mijoz qancha soniyadan so'ng qayta so'rov yuborishi mumkinligini bildiruvchi sarlavha. |

## Bilasizmi?

- Telegram, Instagram va TikTok kabi gigant tarmoqlarda siz lentani pastga aylantirganingizda (Infinite Scroll), orqa fonda aynan Pagination so'rovlari ishlaydi: har safar ekran oxiriga yetganingizda, serverdan keyingi 10-15 ta video yoki post yuklanadi.
- GitHub API bepul foydalanuvchilar uchun soatiga 60 ta, token bilan kirganlar uchun esa soatiga 5 000 ta so'rov bilan Throttling o'rnatgan. Agar chegaradan oshsangiz, GitHub ham `429` xatosini chiqaradi.
- Agar ma'lumotlar bazasida 1 millionta post bo'lsa, `SELECT * FROM posts LIMIT 10 OFFSET 0` so'rovi 1 millisoniyada bajariladi, ammo pagination bo'lmasa 1 millionta qatorni olish bir necha daqiqa vaqt oladi!

## Topshiriqlar

### 1. Pagination JSON maydonlarini aniqlash · oson
Quyidagi javobda berilgan maydonlarning vazifasini yozing:
- `count`
- `next`
- `previous`
- `results`
**Kutiladigan natija:** 4 ta maydonning aniq ma'nosi.

### 2. URL sahifa so'rovi tuzish · oson
Maqolalar ro'yxatining 4-sahifasini va har bir sahifada 15 tadan maqola bo'lishini so'rash uchun `posts` endpointiga qanday URL query parametrlari yuboriladi?
**Kutiladigan natija:** To'g'ri URL havolasi (`?page=...&page_size=...`).

### 3. Throttling limitlarini o'qish · oson
`settings/base.py` faylida quyidagi yozuv berilgan:
```python
"DEFAULT_THROTTLE_RATES": {
    "anon": "30/minute",
    "user": "500/day",
}
```
1. Ro'yxatdan o'tmagan anonim foydalanuvchi minutiga ko'pi bilan nechta so'rov yubora oladi?
2. Tizimga kirgan foydalanuvchi bir kunda nechta so'rov yuborishi mumkin?
**Kutiladigan natija:** Ikkala savolga aniq raqamli javoblar.

### 4. 429 xatosi va Retry-After · oson
Foydalanuvchi juda ko'p so'rov yuborib limitdan oshib ketdi.
Server unga qanday HTTP status kodi qaytaradi va qachon qayta so'rov yuborish mumkinligini qaysi sarlavha (header) orqali bilib olish mumkin?
**Kutiladigan natija:** 3 xonali status kodi va sarlavha nomi.

### 5. DefaultPageNumberPagination sozlash · o'rta
`apps/common/pagination.py` modulida standart sahifa o'lchami 12 ta, maksimal ruxsat etilgan hajm 60 ta bo'lgan `CatalogPagination` klassini yozing.
**Kutiladigan natija:** `PageNumberPagination` dan voris olgan to'g'ri Python klassi.

### 6. Throttling hisob-kitobi · o'rta
Tizimda `anon: 60/min` limiti o'rnatilgan.
Avtomatlashtirilgan test dasturi 1 daqiqada 100 ta so'rov yubordi.
1. Nechta so'rov muvaffaqiyatli bajariladi (200 OK)?
2. Nechta so'rov rad etiladi (429 Too Many Requests)?
3. Ushbu rad etilgan so'rovlar server bazasiga yuklama beradimi?
**Kutiladigan natija:** Raqamlar va yuklama bo'yicha tahlil.

### 7. Login endpointi uchun maxsus Throttle · o'rta
Nima sababdan login endpointi (`/api/v1/auth/jwt/create/`) uchun global `anon` limitidan (masalan 60/min) ko'ra ancha qattiqroq limit (masalan `10/min`) qo'yilishi shart?
Ushbu cheklov qanday kiberhujumning oldini oladi?
**Kutiladigan natija:** Brute-force hujumi va login cheklovi tahlili.

### 8. Kod tahlili: Xatoni topish · o'rta
Boshlovchi dasturchi quyidagi pagination klassini yaratdi:
```python
class PostPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "size"
    # max_page_size ko'rsatilmagan!
```
Xaker ushbu endpointga `GET /api/v1/posts/?size=500000` deb so'rov yubordi.
Nima uchun bu serverning ishdan chiqishiga olib kelishi mumkin va kodni qanday to'g'rilash kerak?
**Kutiladigan natija:** Muammo tushuntirilib, `max_page_size = 100` qo'shilgan kod.

### 9. Mini-loyiha: Izohlar uchun CursorPagination · qiyin
Yangiliklar ostidagi izohlar har soniyada ko'plab yangilanadi.
1. `apps/common/pagination.py` faylida `CommentCursorPagination(CursorPagination)` klassini yarating (sahifa hajmi 20 ta, tartiblash `ordering = '-created_at'`).
2. `CommentViewSet` ga ushbu paginationni ulang.
3. Kursor orqali olinadigan JSON javobida `next` va `previous` havolalari qanday shifrlangan kursor bilan chiqishini ko'rsating.
**Kutiladigan natija:** To'liq klass kodi va namunaviy kursor URL lari.

### 10. ScopedRateThrottle tadqiqoti · qiyin
DRF dagi `ScopedRateThrottle` qanday ishlaydi?
Agar bitta loyihada:
- Maqolalar ro'yxati uchun `throttle_scope = "posts"` (1000/day);
- Izoh yozish uchun `throttle_scope = "comments"` (50/hour);
- To'lov qilish uchun `throttle_scope = "payments"` (5/minute)
bo'lsa, buni `settings.py` va ViewSetlar darajasida qanday sozlash mumkin?
**Kutiladigan natija:** `ScopedRateThrottle` mexanizmi va konfiguratsiya kodi.

### 11. Throttling uchun Redis keshlash · qiyin
Standart holatda DRF `LocMemCache` (server operativ xotirasi) dan foydalanadi.
Ammo agar bizda 3 ta server (Load Balancer ortida) ishlayotgan bo'lsa:
1. Nima uchun `LocMemCache` har bir serverda alohida hisoblab, umumiy limitni to'g'ri ushlay olmaydi?
2. Markazlashgan `Redis` xotirasi bu muammoni qanday hal etadi?
3. Django keshini Redis ga ulash uchun qanday sozlamalar (`CACHES`) kerak?
**Kutiladigan natija:** Taqsimlangan tizimlarda Redis kesh va Throttling tahlili.

### 12. Bonus tadqiqot: Cloudflare va Reverse Proxy Rate Limiting · bonus
Yirik IT kompaniyalar rate limitingni nafaqat Django kodi darajasida, balki serverga so'rov yetib kelmasidan oldin — Cloudflare yoki Nginx darajasida to'xtatadilar.
1. Cloudflare Rate Limiting qanday ishlaydi va uning Django Throttling dan qanday ustunligi bor?
2. Nima sababdan birinchi to'siqni Nginx/Cloudflare da, nozik biznes qoidalarini esa DRF da tekshirish eng mukammal xavfsizlik arxitekturasi hisoblanadi?
**Kutiladigan natija:** Veb-infratuzilma darajasidagi rate limiting bo'yicha mustaqil tadqiqot.

## O'zingizni tekshiring

1. Pagination qanday muammolarni hal qiladi va nega u barcha ochiq API larda majburiy?
2. `PageNumberPagination` qaytaradigan 4 ta asosiy JSON maydonini ayting.
3. Throttling nima va u serverni qanday DoS hujumlaridan saqlaydi?
4. `429 Too Many Requests` status kodi qachon qaytariladi?
5. Nima sababdan `max_page_size` parametrini belgilash xavfsizlik talabi hisoblanadi?
6. Nima uchun login sahifasi uchun qattiqroq limit qo'yiladi?

## Uyga vazifa

1. `src/apps/common/pagination.py` da `DefaultPageNumberPagination` klassini yarating va `settings/base.py` ga global pagination sozlamasini qo'shing.
2. `settings/base.py` faylida `DEFAULT_THROTTLE_CLASSES` va `DEFAULT_THROTTLE_RATES` ni sozlang (`anon: 60/min`, `user: 300/min`).
3. Brauzerda `http://127.0.0.1:8000/api/v1/posts/?page=1` manzilini oching va JSON javobida pagination tuzilishi to'g'ri chiqqanligini tekshiring.
