---
title: "9-dars. APIni testlash. APIni hujjatlashtirish. (Swagger, Redoc)"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (Python)", "link": "/10-sinf-python/"}, "week": {"n": 3, "link": "/10-sinf-python/hafta-03/"}, "g": 9, "title": "APIni testlash. APIni hujjatlashtirish. (Swagger, Redoc)", "lead": "Haqiqiy professional dasturchi kodni nafaqat yozadi, balki uning mukammal ishlashini avtomatlashtirilgan testlar bilan isbotlaydi va hamkasblari uchun tushunarli interaktiv hujjat (Swagger) taqdim etadi. Ushbu darsda biz 1-bobning yakuniy cho'qqisiga chiqamiz!", "slide": "/slaydlar/10-sinf-python/hafta-03/dars-3.html", "test": "/slaydlar/10-sinf-python/hafta-03/dars-3-test.html", "tabs": [{"g": 7, "link": "/10-sinf-python/hafta-03/dars-1", "current": false}, {"g": 8, "link": "/10-sinf-python/hafta-03/dars-2", "current": false}, {"g": 9, "link": "/10-sinf-python/hafta-03/dars-3", "current": true}], "prev": {"g": 8, "title": "Statik fayllar bilan ishlash. Fayllarni yuklash va koʻchirib olish", "link": "/10-sinf-python/hafta-03/dars-2"}, "next": null}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Avtomatlashtirilgan testlash** &mdash; dasturning to'g'ri ishlashini inson omilisiz, kompyuterning o'zi soniyalar ichida tekshirib beruvchi mexanizmdir.
- **Regressiya xatosi** &mdash; yangi kod qo'shilganda eski ishlayotgan qismlarning kutilmaganda buzilib qolishi; testlar aynan regressiyani oldini oladi.
- DRF da API larni testlash uchun **`APITestCase`** va **`APIClient`** klasslari ishlatiladi; testlar alohida vaqtinchalik xotira bazasida yurgaziladi.
- `self.client.force_authenticate(user)` orqali testlarda parolni kiritib o'tirmasdan, foydalanuvchini zudlik bilan autentifikatsiya qilish mumkin.
- **OpenAPI 3.0** &mdash; RESTful API larning barcha yo'llari, parametrlari va modellarini tavsiflovchi xalqaro standartdir.
- **`drf-spectacular`** kutubxonasi yordamida loyiha kodidan avtomatik ravishda **Swagger UI** (`/api/docs/`) va **ReDoc** (`/api/redoc/`) interfeyslari yaratiladi.
- Swagger UI brauzer orqali har bir endpointni "Try it out" tugmasi bilan to'g'ridan-to'g'ri sinash imkonini beradi va frontend hamda mobil jamoaga beqiyos qulaylik yaratadi.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Avtomobil zavodi analogiyasi: Crash Test

Tasavvur qiling, avtomobil zavodi yangi mashina ishlab chiqardi:
- **Testlarsiz (Havaskorlik):** Zavod mashinani to'g'ridan-to'g'ri xaridorga sotadi: "Haydab ko'ring-chi, tormozi ishlayaptimi?". Agar tormoz ishlamasa, fojia yuz beradi!
- **Avtomatlashtirilgan testlar bilan (Professionallik):** Zavod mashinani xaridorga berishdan oldin maxsus laboratoriyada sinovdan o'tkazadi: tormoz tizimi 10 000 marta bosib ko'riladi, xavfsizlik yostiqchalari tekshiriladi.
Dasturlashda ham xuddi shunday: foydalanuvchilar xatoga duch kelmasligi uchun, kodni avval testlar orqali sinovdan o'tkazamiz.

### 2. Swagger UI nima uchun jamoaviy dasturlashda inqilob qildi?

Ilgari backend dasturchi API yozgach, frontend dasturchiga Telegram orqali xabar yozardi:
"Falona URL ga mana bu ma'lumotni jo'nat, javobi mana bunday chiqadi...".
Keyin backendda bitta maydon o'zgarsa, yana tushunmovchiliklar, bahslar boshlanardi.

**Swagger UI bu muammoni butunlay yo'q qildi:**
- Backend dasturchi bitta qator kod o'zgartirsa, Swagger hujjatida bu o'zgarish **avtomatik** yangilanadi;
- Frontend dasturchi `/api/docs/` manzilini ochib, qaysi parametr majburiy, qaysi biri ixtiyoriy ekanligini, xatolikda qanday status chiqishini aniq ko'radi;
- "Try it out" tugmasi orqali API ga Postmansiz so'rov yuborib ko'radi.

### 3. TDD (Test-Driven Development) tushunchasi

Dunyoning yetakchi kompaniyalarida (Google, Microsoft, Amazon) ko'pincha **TDD (Testlar orqali ishlab chiqish)** uslubi qo'llaniladi:
1. **Red (Qizil):** Avval kod emas, balki kutilayotgan natijaning testi yoziladi. Kod hali yo'qligi sababli test yiqiladi (qizil rangda).
2. **Green (Yashil):** Testdan o'tish uchun minimal kod yoziladi. Test muvaffaqiyatli o'tadi (yashil rang).
3. **Refactor (Tozalash):** Kod tozalanadi, optimallashadi, ammo test yashilligicha qolishi shart.

### 4. Dasturchilar ko'p yo'l qo'yadigan xatolar

- **Xato 1: Testlarda real ma'lumotlar bazasini tozalashdan qo'rqish.** Dasturchilar: "Test yozsam, bazamdagi ma'lumotlar o'chib ketadimi?" deb qo'rqishadi. Yo'q! `APITestCase` har doim vaqtinchalik test bazasini ochadi va sizning asosiy `db.sqlite3` yoki PostgreSQL bazangizga zarracha tegmaydi.
- **Xato 2: Swagger sxemasiga mos bo'lmagan Serializer yozish.** Agar serializerda maydonlar noto'g'ri ta'riflansa, Swagger ularni noto'g'ri ko'rsatishi mumkin. `drf-spectacular` dan foydalanganda aniq serializer klasslaridan foydalanish maqsadga muvofiq.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Avtomatlashtirilgan test** | Kodning to'g'ri ishlashini kompyuter tomonidan avtomatik tekshiruvchi maxsus dastur kodi. |
| **APITestCase** | DRF da REST API endpointlarini testlash uchun mo'ljallangan sinov sinfi. |
| **APIClient** | Test jarayonida brauzer yoki Postman kabi HTTP so'rovlarini simulyatsiya qiluvchi virtual mijoz. |
| **force_authenticate** | Test paytida foydalanuvchini login/parolsiz zudlik bilan tizimga kiritilgan deb e'lon qilish metodi. |
| **OpenAPI 3.0** | RESTful API interfeyslarini kompyuter va inson tushunadigan formatda tavsiflash standarti. |
| **drf-spectacular** | Django REST Framework uchun zamonaviy OpenAPI 3.0 sxemalarini generatsiya qiluvchi kutubxona. |
| **Swagger UI** | OpenAPI spetsifikatsiyasini interaktiv, testlash imkoniyatiga ega chiroyli veb-sahifaga aylantiruvchi vosita. |
| **ReDoc** | API hujjatlarini uch ustunli, o'qish uchun juda qulay kitob shaklida namoyish etuvchi interfeys. |
| **Regressiya** | Dasturga yangi o'zgartirish kiritilganda eski funksiyalarning kutilmaganda buzilib qolishi. |
| **CI/CD** | Kodni avtomatik testlash, yig'ish va serverga joylashtirishning uzluksiz muhandislik jarayoni. |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- NASA kosmik kemalari va samolyotlarni boshqaruvchi dasturiy ta'minotlarda har 1 qator dastur kodi uchun kamida 10 qator avtomatlashtirilgan sinov testlari yoziladi!
- Swagger 2011-yilda yaratilgan bo'lib, keyinchalik u xalqaro Linux Foundation konsorsiumiga topshirilgan va bugungi kunda "OpenAPI Initiative" deb ataluvchi global standartga aylangan.
- Django-ning `python manage.py test` buyrug'i barcha ilovalardagi `test_*.py` fayllarini avtomatik qidirib topadi va ularni alifbo tartibida birma-bir xavfsiz muhitda yurgazadi.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Test tushunchalarini aniqlash <Badge type="tip" text="oson" />
Quyidagi atamalarning ma'nosini qisqacha tushuntiring:
- `APITestCase`
- `force_authenticate`
- `self.assertEqual`
**Kutiladigan natija:** 3 ta test mexanizmining aniq tavsifi.

### 2. Swagger va ReDoc manzillari <Badge type="tip" text="oson" />
Loyiha sozlangach, brauzerda:
1. Interaktiv Swagger UI interfeysini ochish uchun qaysi URL ga kiriladi?
2. Toza texnik hujjat (ReDoc) qaysi URL da joylashadi?
**Kutiladigan natija:** Ikkala URL yo'li (`/api/docs/` va `/api/redoc/`).

### 3. Test terminal buyrug'i <Badge type="tip" text="oson" />
Faqat `apps/news` papkasidagi testlarni ishga tushirish uchun terminalda qanday buyruq beriladi?
**Kutiladigan natija:** To'g'ri `python manage.py test ...` buyrug'i.

### 4. Regressiya xatosi tushunchasi <Badge type="tip" text="oson" />
Dasturlashda "Regressiya" nima va avtomatlashtirilgan testlar uning oldini olishga qanday yordam beradi?
**Kutiladigan natija:** Regressiya tushunchasi va testlarning o'rni.

### 5. Oddiy GET so'rovi testini yozish <Badge type="warning" text="o'rta" />
`apps/news/tests/test_categories.py` faylida kategoriyalar ro'yxatini (`GET /api/v1/categories/`) tekshiruvchi va HTTP status `200 OK` qaytishini tasdiqlovchi test metodini yozing.
**Kutiladigan natija:** To'liq `APITestCase` klassi va metodi.

### 6. Ruxsatlarni testlash (401 Unauthorized) <Badge type="warning" text="o'rta" />
Tizimga kirmagan (anonim) foydalanuvchi `POST /api/v1/posts/` manziliga yangi post yaratish so'rovini yuborganda server unga `401 UNAUTHORIZED` qaytarishini tekshiruvchi test metodini yozing.
**Kutiladigan natija:** `test_create_post_unauthenticated` testi kodi.

### 7. IDOR himoyasini testlash (403 Forbidden) <Badge type="warning" text="o'rta" />
2-foydalanuvchi 1-foydalanuvchining maqolasini o'chirishga (`DELETE /api/v1/posts/{slug}/`) uringanda server `403 FORBIDDEN` qaytarishini tekshiruvchi test kodini yozing.
**Kutiladigan natija:** Obyekt darajasidagi ruxsatni tekshiruvchi to'liq test.

### 8. Kod tahlili: Xatoni topish <Badge type="warning" text="o'rta" />
Boshlovchi dasturchi quyidagi testni yozdi:
```python
def test_create_post(self):
    self.client.force_authenticate(user=self.user)
    response = self.client.post("/api/v1/posts/", data={"title": "Salom"})
    # Xato taqqoslash:
    self.assertEqual(response.status_code, 200)
```
Nima uchun bu test yiqiladi? Yangi obyekt yaratilganda qaysi HTTP status kodi (200 emas!) kutiladi?
**Kutiladigan natija:** Xato sababi va `201 CREATED` ga to'g'rilangan kod.

### 9. Mini-loyiha: Swagger sozlamalarini to'liq sozlash <Badge type="danger" text="qiyin" />
`src/config/settings/base.py` fayliga `drf-spectacular` ni ulang va quyidagi sozlamalarni kiriting:
- Loyiha nomi: `Muhammad al-Xorazmiy vorislari NewsPortal API`;
- Versiya: `1.0.0`;
- Tavsif: `10-sinf uchun professional REST API portali`;
- Swagger UI da tokenni kiritish uchun `Authorize` (Bearer) tugmasi ko'rinishini ta'minlang.
**Kutiladigan natija:** `SPECTACULAR_SETTINGS` konfiguratsiyasi.

### 10. Test Factory yondashuvi <Badge type="danger" text="qiyin" />
Testlarda har safar qo'lda obyekt yaratmaslik uchun `apps/common/tests/factories.py` modulida `create_user` va `create_post` yordamchi funksiyalarini yozing (standart qiymatlar va `**kwargs` bilan).
**Kutiladigan natija:** Qayta ishlatiluvchi Factory funksiyalari kodi.

### 11. Test Coverage (Test qamrovi) tahlili <Badge type="danger" text="qiyin" />
`coverage` kutubxonasi yordamida loyiha kodining necha foizi testlar bilan qamrab olinganligini tekshirish mumkin.
1. `coverage run --source='.' manage.py test` buyrug'i qanday ishlaydi?
2. `coverage report` va `coverage html` hisobotlari dasturchiga qaysi qatorlar test qilinmaganligini qanday ko'rsatadi?
**Kutiladigan natija:** Test qamrovi tahlili va buyruqlar tushuntirilishi.

### 12. Bonus tadqiqot: Postman Collection va Newman orqali testlash <Badge type="info" text="bonus" />
Ko'pgina kompaniyalar API larni nafaqat Python testlari orqali, balki Postman to'plamlari (Collections) orqali ham testlaydilar.
1. Postman-da test ssenariylarini (Assertions) qanday yozish mumkin?
2. `newman` CLI vositasi yordamida terminalda Postman to'plamlarini avtomatik ishga tushirish qanday amalga oshiriladi?
**Kutiladigan natija:** Postman va Newman orqali API testlash bo'yicha mustaqil tadqiqot.

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Nima sababdan avtomatlashtirilgan testlar jamoaviy dasturlashda muhim o'rin tutadi?
2. `APITestCase` vaqtinchalik ma'lumotlar bazasini qanday boshqaradi?
3. `force_authenticate` metodi qachon va nima maqsadda ishlatiladi?
4. OpenAPI 3.0 spetsifikatsiyasining maqsadi nima?
5. Swagger UI ning ReDoc dan qanday asosiy farqi va ustunligi bor?
6. Bitta yangi post muvaffaqiyatli saqlanganda qanday HTTP status kodi qaytishi kerak?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. `src/apps/news/tests/test_posts_api.py` faylini konspektdagi namuna asosida to'ldiring va terminalda `python manage.py test` qiling.
2. `drf-spectacular` kutubxonasini o'rnatib, `urls.py` ga `/api/docs/` va `/api/redoc/` yo'llarini ulang.
3. Brauzerda `http://127.0.0.1:8000/api/docs/` manzilini oching va Swagger interfeysidagi "Try it out" orqali yangiliklar ro'yxatini olib, natijani kuzating.

</div>

