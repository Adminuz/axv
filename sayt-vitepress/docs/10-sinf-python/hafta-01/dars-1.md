---
title: "1-dars. Django REST Framework. Server side rendering va user side rendering tushunchalari"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (Python)", "link": "/10-sinf-python/"}, "week": {"n": 1, "link": "/10-sinf-python/hafta-01/"}, "g": 1, "title": "Django REST Framework. Server side rendering va user side rendering tushunchalari", "lead": "Veb-dasturlashda frontend va backend o'rtasidagi aloqa qanday o'rnatiladi? Ushbu darsda biz serverda HTML tayyorlash (SSR) va brauzerda ma'lumotlarni dinamik chizish (CSR/USR) modellarini tahlil qilamiz hamda Django REST Framework dunyosiga ilk qadamni qo'yamiz.", "slide": "/slaydlar/10-sinf-python/hafta-01/dars-1.html", "tabs": [{"g": 1, "link": "/10-sinf-python/hafta-01/dars-1", "current": true}, {"g": 2, "link": "/10-sinf-python/hafta-01/dars-2", "current": false}, {"g": 3, "link": "/10-sinf-python/hafta-01/dars-3", "current": false}], "prev": null, "next": {"g": 2, "title": "DRF loyiha qurish: MBni loyihalash. Loyihani yaratish, dastlabki sozlamalar", "link": "/10-sinf-python/hafta-01/dars-2"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- Veb-ilovalar foydalanuvchi ko'radigan **Frontend** va barcha mantiq hamda ma'lumotlar saqlanadigan **Backend** qismlariga bo'linadi.
- **Server-Side Rendering (SSR)** arxitekturasida sahifaning to'liq HTML kodi serverda tayyorlanib, brauzerga yuboriladi (klassik Django MTV modeli).
- SSR ning asosiy yutug'i — mukammal SEO (qidiruv tizimlari indekslashi oson) va birinchi sahifaning bir zumda ochilishidir.
- **User-Side Rendering (USR / CSR)** modelida server faqat toza ma'lumotni (JSON formatida) uzatadi, HTML interfeys esa foydalanuvchi brauzerida JavaScript orqali yig'iladi.
- USR yondashuvi yordamida zamonaviy **Single Page Application (SPA)** va qulay mobil ilovalar yaratiladi; sahifa qayta yuklanmasdan ishlaydi.
- **REST (Representational State Transfer)** — bu tarmoqda resurslarni HTTP metodlari (GET, POST, PUT, PATCH, DELETE) orqali boshqaruvchi holatsiz (stateless) arxitektura tamoyilidir.
- **Django REST Framework (DRF)** — Django asosida tezkor, xavfsiz va qulay RESTful API ishlab chiqish uchun eng kuchli backend kutubxonasi hisoblanadi.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Restoran analogiyasi: Tayyor taom (SSR) yoki Yarim tayyor masalliqlar (CSR)

Veb rendering modellarini yaxshiroq tushunish uchun restoranni tasavvur qiling:
- **SSR bu — to'liq tayyorlangan va laganda keltirilgan issiq taom.** Oshpaz (server) oshxonada hamma narsani pishiradi, bezatadi va sizga tayyor ovqatni beradi. Siz hech narsa qilmaysiz, darhol yeyishni boshlaysiz (tezkor birinchi ko'rinish). Agar taomga bir dona sous qo'shmoqchi bo'lsangiz, ofitsiant butun laganni oshxonaga qaytarib olib ketib, yangidan keltirishi kerak (sahifaning to'liq refresh bo'lishi).
- **CSR bu — o'zingiz tayyorlaydigan maxsus stol (masalan, koreyscha barbekyu).** Oshxona (backend API) sizga toza go'sht, ziravorlar va sabzavotlarni (JSON ma'lumotlarni) olib keladi. Sizning stolingizdagi plita (brauzerdagi JavaScript) esa ularni xohlaganingizcha pishiradi. Biror qo'shimcha kerak bo'lsa, butun stolni almashtirmasdan, faqat bitta sousni buyurtma qilasiz (sahifa yangilanmasdan kichik qismning o'zgarishi).

### 2. Nima uchun zamonaviy IT kompaniyalar API ga o'tmoqda?

Avvallari barcha veb-saytlar faqat kompyuter brauzerlari uchun yaratilgan. Hozirgi kunda bitta xizmat bir vaqtning o'zida:
- Veb-saytda (React/Vue),
- Android ilovada (Kotlin),
- iOS ilovada (Swift),
- Telegram botda (Aiogram),
- Aqlli soatlarda va televizorlarda ishlashi kerak.

Agar siz an'anaviy SSR ishlatsangiz, har bir platforma uchun alohida backend yozishingizga to'g'ri kelardi. REST API yordamida esa **bitta yagona backend** yoziladi va u barcha qurilmalarga universal JSON formatida ma'lumot uzatadi!

### 3. RESTful API ning oltin tamoyillari

REST arxitekturasining asosiy qoidalari:
1. **Stateless (Holatsiz):** Server har bir so'rovni alohida ko'rib chiqadi. Foydalanuvchi kimligini bilish uchun har bir so'rovda maxsus xavfsizlik belgisi (Token yoki JWT) yuboriladi.
2. **Resurslarga asoslangan nomlash:** URL manzillar fe'l emas, ot so'z turkumidan iborat bo'lishi kerak.
   - Noto'g'ri: `/api/get-all-news/` yoki `/api/create_post/`
   - To'g'ri: `GET /api/v1/posts/` yoki `POST /api/v1/posts/`
3. **Standart HTTP status kodlari:**
   - `200 OK` — so'rov muvaffaqiyatli bajarildi;
   - `201 Created` — yangi ma'lumot muvaffaqiyatli saqlandi;
   - `400 Bad Request` — yuborilgan ma'lumotda xatolik bor (validatsiya xatosi);
   - `401 Unauthorized` — tizimga kirmagan foydalanuvchi;
   - `403 Forbidden` — bu amalni bajarishga ruxsatingiz yetmaydi;
   - `404 Not Found` — so'ralgan ma'lumot topilmadi;
   - `500 Internal Server Error` — server kodida ichki xatolik yuz berdi.

### 4. Dasturchilar ko'p yo'l qo'yadigan xatolar

- **Xato 1: URL ichida amal nomini yozish.** Masalan, `/api/posts/delete/5/`. REST standartida bu xato hisoblanadi. O'chirish amali HTTP metodi orqali bildirilishi kerak: `DELETE /api/posts/5/`.
- **Xato 2: Xatolik yuz berganda ham 200 OK qaytarish.** Ba'zi boshlovchilar JSON ichida `{"status": "error"}` deb yozib, HTTP statusni 200 qoldirishadi. Bu frontend uchun juda noqulay. Xatolik bo'lsa, 4xx yoki 5xx status kodi qaytarilishi shart.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Frontend** | Foydalanuvchi ko'radigan va o'zaro ta'sir o'tkazadigan veb-saytning vizual qismi (HTML/CSS/JS). |
| **Backend** | Tizimning server tomoni: ma'lumotlar bazasi, biznes mantiq va xavfsizlikni boshqaruvchi qatlam. |
| **SSR (Server-Side Rendering)** | HTML sahifani serverda to'liq render qilib, tayyor holda brauzerga yuborish texnologiyasi. |
| **CSR / USR (Client-Side Rendering)** | Sahifani foydalanuvchi brauzerida JavaScript orqali dinamik qurish texnologiyasi. |
| **SPA (Single Page Application)** | Sahifani to'liq qayta yuklamasdan ishlaydigan bir sahifali zamonaviy veb-ilova. |
| **API (Application Programming Interface)** | Dasturlar va xizmatlarning o'zaro ma'lumot almashishi uchun maxsus interfeys. |
| **REST (Representational State Transfer)** | Taqsimlangan tarmoq tizimlari uchun me'moriy uslub va qoidalar to'plami. |
| **DRF (Django REST Framework)** | Python Django freymvorkida qulay va qudratli REST API lar yaratish kutubxonasi. |
| **JSON (JavaScript Object Notation)** | Odam o'qishi uchun ham, kompyuter tahlil qilishi uchun ham oson bo'lgan matnli ma'lumotlar almashish formati. |
| **Stateless** | Server o'zida har bir mijozning oldingi so'rovlari tarixini saqlamasligi holati. |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Google qidiruv tizimi botlari kuniga milliardlab veb-sahifalarni skanerlaydi. SSR saytlar HTML shaklida kelgani sababli, Google ularni CSR saytlarga qaraganda 10 barobar kamroq kompyuter resursi sarflab indekslaydi!
- Roy Fielding 2000-yilda o'zining doktorlik dissertatsiyasida ilk bor REST tushunchasini ilmiy asoslab bergan. Bugungi kunda Internetdagi barcha ommaviy API larning 80% dan ortig'i REST tamoyillariga asoslanadi.
- Django REST Framework (DRF) dunyo bo'ylab har oy millionlab marta yuklab olinadi va Mozilla, Red Hat, Instagram kabi gigant kompaniyalar infratuzilmasida keng qo'llaniladi.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Veb rendering modellarini ajratish <Badge type="tip" text="oson" />
Quyidagi 4 ta loyihani SSR va USR toifalariga ajrating va har bir tanlovingizni 1 ta jumla bilan asoslang:
a) Onlayn ensiklopediya (Vikipediya).
b) Onlayn musiqa pleyeri (Spotify Web).
c) Kunlik ob-havo yangiliklari sayti.
d) Onlayn rasm tahrirlash muharriri (Figma / Canva Web).
**Kutiladigan natija:** Har bir loyiha uchun SSR yoki USR tanlanib, uning sababi yozilgan qisqa tahlil.

### 2. HTTP metodlarini tahlil qilish <Badge type="tip" text="oson" />
Elektron kundalik tizimida quyidagi amallar uchun qaysi HTTP metodi (`GET`, `POST`, `PUT`, `DELETE`) ishlatilishini ko'rsating:
1. O'quvchining choraklik baholarini ekranda ko'rish.
2. Yangi o'quvchini tizim ro'yxatiga qo'shish.
3. O'quvchining telefon raqamini yangilash.
4. Xato kiritilgan o'quvchi profilini bazadan butunlay o'chirish.
**Kutiladigan natija:** 4 ta amalga mos keluvchi HTTP metodlari ro'yxati.

### 3. HTTP status kodlari ma'nosini topish <Badge type="tip" text="oson" />
Quyidagi vaziyatlarda API qanday HTTP status kodini (masalan: 200, 201, 400, 401, 404, 500) qaytarishi kerakligini aniqlang:
a) Foydalanuvchi ro'yxatdan o'tmagan holda shaxsiy profilini ochmoqchi bo'ldi.
b) Foydalanuvchi mavjud bo'lmagan maqola havolasiga kirdi (masalan `/api/posts/9999/`).
c) Yangi maqola muvaffaqiyatli saqlandi.
d) Maqola sarlavhasi kiritilishi shart bo'lsa-da, foydalanuvchi uni bo'sh qoldirdi.
**Kutiladigan natija:** Har bir holat uchun to'g'ri 3 xonali HTTP status kodi.

### 4. RESTful URL dizayni tekshiruvi <Badge type="tip" text="oson" />
Quyidagi URL larning qaysilari REST tamoyillariga mos va qaysilari xato ekanligini aniqlang. Xatolarini to'g'rilab yozing:
1. `GET /api/v1/get_all_users/`
2. `POST /api/v1/users/`
3. `POST /api/v1/delete_user/12/`
4. `GET /api/v1/users/12/`
**Kutiladigan natija:** Noto'g'ri URL lar topilib, REST standartiga muvofiq qayta yozilgan ko'rinishi.

### 5. Mahsulotlar uchun JSON strukturasi tuzish <Badge type="warning" text="o'rta" />
Onlayn kiyim-kechak do'koni uchun bitta mahsulot haqidagi ma'lumotni ifodalovchi to'liq JSON obyektini yarating. Unda quyidagi maydonlar bo'lishi shart:
- `id` (butun son);
- `name` (satr);
- `price` (o'nlik son);
- `sizes` (o'lchamlar massivi: masalan, S, M, L, XL);
- `in_stock` (mantiqiy qiymat: bor/yo'q);
- `category` (ichki obyekt: id va name maydonlari bilan).
**Kutiladigan natija:** Sintaktik jihatdan to'g'ri, barcha talab qilingan maydonlarga ega JSON kodi.

### 6. SSR va CSR trafigini taqqoslash hisobi <Badge type="warning" text="o'rta" />
Tasavvur qiling, yangiliklar saytining har bir sahifasi HTML ko'rinishida 120 Kilobayt (KB) hajmni tashkil qiladi.
Agar ushbu sahifaning faqat yangilik matni va sarlavhasi JSON shaklida olinsa, uning hajmi bor-yo'g'i 4 KB bo'ladi.
Foydalanuvchi kun davomida ushbu saytda 30 ta yangilikni o'qidi.
1. SSR modelida foydalanuvchi sarflagan umumiy internet trafigini hisoblang.
2. CSR modelida foydalanuvchi faqat 30 ta yangilikning JSON ma'lumotlarini yuklaganida qancha trafik sarflaydi?
3. Trafik tejamkorligi necha barobarni tashkil etadi?
**Kutiladigan natija:** Uchta savolga aniq raqamlar va tejamkorlik xulosasi.

### 7. Browsable API imkoniyatlarini tahlil qilish <Badge type="warning" text="o'rta" />
Django REST Framework-ning boshqa ko'plab freymvorklardan (masalan Express.js yoki FastAPI) eng katta qulayligi — bu o'rnatilgan "Browsable API" interfeysidir.
Dasturchi uchun ushbu interfeysning qanday 3 ta amaliy foydasi borligini yozing. Postman kabi dasturlar mavjud bo'lsa ham, nima uchun Browsable API qulay hisoblanadi?
**Kutiladigan natija:** Browsable API ning kamida 3 ta amaliy afzalligi yoritilgan tahlil.

### 8. Xatolikni toping: Noto'g'ri JSON sintaksisi <Badge type="warning" text="o'rta" />
Quyidagi JSON kodida 4 ta sintaktik xato mavjud. Xatolarni toping va kodni to'g'rilab yozing:
```json
{
  name: 'Alisher Navoiy',
  "year": 1441,
  "city": "Hirot",
  "is_author": True,
  "works": ["Xamsa", "Lison ut-tayr",],
}
```
**Kutiladigan natija:** Xatolar izohlanib, haqiqiy JSON standartiga keltirilgan kod.

### 9. Mini-loyiha: Maktab kutubxonasi API xaritasi <Badge type="danger" text="qiyin" />
Maktab kutubxonasi uchun REST API arxitekturasini loyihalashtiring. Quyidagi resurslar uchun barcha kerakli endpointlarni jadval ko'rinishida yozing:
- Kitoblar (`books`)
- Mualliflar (`authors`)
- Kitob ijaralari (`loans`)
Jadval ustunlari: `HTTP Metod`, `URL Manzil`, `Vazifasi`, `Kutiladigan HTTP Status`.
**Kutiladigan natija:** Kamida 8 ta to'liq ishlab chiqilgan endpointdan iborat API arxitektura jadvali.

### 10. Gibrid rendering (Next.js / SSR + CSR) tahlili <Badge type="danger" text="qiyin" />
Zamonaviy veb-ishlab chiqishda sof SSR yoki sof CSR o'rniga "Gibrid yondashuv" (masalan, Next.js yoki Nuxt.js) qo'llaniladi.
Ushbu gibrid yondashuv qanday ishlashini tadqiq qiling:
- Sahifaga birinchi kirganda nima sodir bo'ladi?
- Sahifa ichidagi keyingi havolalarga o'tganda nima sodir bo'ladi?
- Bu usul orqali dasturchilar qanday qilib SSR ning ham, CSR ning ham eng yaxshi tomonlarini birlashtirishadi?
**Kutiladigan natija:** Gibrid rendering arxitekturasining ishlash mexanizmi bo'yicha batafsil tushuntirish.

### 11. Tadqiqot va muammo yechimi: Katta hajmdagi ma'lumotlar <Badge type="danger" text="qiyin" />
Tasavvur qiling, ma'lumotlar bazasida 500 000 ta mahsulot bor.
Frontend ilova `GET /api/v1/products/` so'rovini yubordi va server bir vaqtning o'zida barcha 500 000 ta mahsulotni JSON qilib qaytarishga harakat qildi.
1. Serverda qanday muammo (xotira, vaqt) yuz berishi mumkin?
2. Brauzerda ushbu ulkan JSON qabul qilinganda nima bo'ladi?
3. Ushbu muammoni hal qilish uchun qanday backend mexanizmlari (Pagination) qo'llaniladi?
**Kutiladigan natija:** Muammoning texnik sabablari va uni yechish yo'llari ko'rsatilgan tahlil.

### 12. Bonus tadqiqot: GraphQL va REST API qarama-qarshiligi <Badge type="info" text="bonus" />
Bugungi kunda REST API ga muqobil sifatida Facebook tomonidan ishlab chiqilgan GraphQL texnologiyasi ham qo'llaniladi.
1. REST API dagi "Over-fetching" (keragidan ortiq ma'lumot kelishi) va "Under-fetching" (bitta ma'lumot uchun bir nechta so'rov yuborish) muammolari nima?
2. GraphQL ushbu muammolarni qanday hal qiladi?
3. Nima uchun aksariyat tizimlarda hali ham REST API eng ishonchli va ommabop tanlov bo'lib qolmoqda?
**Kutiladigan natija:** REST va GraphQL ni qiyosiy taqqoslagan qiziqarli mustaqil tahlil.

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Web-ilovaning frontend va backend qismlari orasidagi asosiy vazifalar taqsimotini aytib bering.
2. Server-Side Rendering (SSR) modelida veb-sahifa dastlab qayerda shakllanadi?
3. Client-Side Rendering (CSR) usulida nima sababdan dastlabki yuklanish biroz ko'proq vaqt olishi mumkin?
4. Qaysi loyihalarda SSR dan foydalanish eng to'g'ri yo'l hisoblanadi va nega?
5. REST me'moriy uslubining asosiy 3 ta tamoyilini sanab bering.
6. JSON formatining afzalliklari nimada va nima uchun u veb dasturlashda asosiy standartga aylandi?
7. Django REST Framework-da yaratilgan API klassik Django shablonlaridan qanday farq qiladi?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. Konspektdagi SSR va USR taqqoslash jadvalini daftaringizga ko'chirib, o'z so'zlaringiz bilan har bir mezonni izohlang.
2. Internetdagi o'zingiz yoqtirgan bitta veb-saytni tanlang (masalan, yangiliklar yoki ijtimoiy tarmoq), brauzerda `F12` (Dasturchi asboblari) tugmasini bosing, `Network` (Tarmoq) bo'limini oching va sahifa yuklanishida qanday `.html` va qanday `.json` so'rovlar o'tayotganini kuzating. Natijalarni daftarga 3-4 jumla bilan qayd eting.
3. Keyingi darsda o'rnatiladigan Django va DRF paketlari uchun kompyuteringizda Python versiyasini terminalda `python --version` orqali tekshirib qo'ying.

</div>

