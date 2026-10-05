---
title: "2-dars. DRF loyiha qurish: MBni loyihalash. Loyihani yaratish, dastlabki sozlamalar"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (Python)", "link": "/10-sinf-python/"}, "week": {"n": 1, "link": "/10-sinf-python/hafta-01/"}, "g": 2, "title": "DRF loyiha qurish: MBni loyihalash. Loyihani yaratish, dastlabki sozlamalar", "lead": "Yirik va jiddiy backend loyihalari mustahkam poydevordan boshlanadi. Ushbu darsda biz real NewsPortal (yangiliklar portali) loyihasi uchun ma'lumotlar bazasini loyihalashtiramiz, Python virtual muhitini sozlaymiz va xalqaro clean architecture standartlariga mos Django loyihasini noldan quramiz.", "slide": "/slaydlar/10-sinf-python/hafta-01/dars-2.html", "test": "/slaydlar/10-sinf-python/hafta-01/dars-2-test.html", "tabs": [{"g": 1, "link": "/10-sinf-python/hafta-01/dars-1", "current": false}, {"g": 2, "link": "/10-sinf-python/hafta-01/dars-2", "current": true}, {"g": 3, "link": "/10-sinf-python/hafta-01/dars-3", "current": false}], "prev": {"g": 1, "title": "Django REST Framework. Server side rendering va user side rendering tushunchalari", "link": "/10-sinf-python/hafta-01/dars-1"}, "next": {"g": 3, "title": "Model, View va Serializer. Routerlar", "link": "/10-sinf-python/hafta-01/dars-3"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- Har qanday professional dasturiy ta'minot minimal **Texnik topshiriq (TT)** va tizimdagi rollarni (Guest, User, Admin) aniqlashdan boshlanadi.
- **Relyatsion ma'lumotlar bazasini loyihalash (ERD)** — jadvallar va ular orasidagi bog'lanishlarni (1-N, N-N) to'g'ri belgilash dasturning kelajakdagi xavfsizligi va tezligini kafolatlaydi.
- `Category` va `Post` o'rtasidagi bog'lanishda `models.PROTECT` ishlatiladi, bu esa maqolalari bor kategoriyaning tasodifan o'chib ketishini oldini oladi.
- **Virtual muhit (`venv`)** — Python kutubxonalarining global operatsion tizimdan ajratilgan, mustaqil muhitidir.
- Maxfiy ma'lumotlar (`SECRET_KEY`, baza parollari, API kalitlari) hech qachon kod ichiga yozilmaydi, faqat `.env` faylida saqlanadi.
- Loyihani **feature-based apps** uslubida (`apps/news`, `apps/comments`, `apps/accounts`, `apps/common`) tuzish kodning o'qilishi va kengayishini osonlashtiradi.
- `settings/base.py` faylida `INSTALLED_APPS` ro'yxatiga `'rest_framework'` qo'shilishi orqali Django REST Framework imkoniyatlari faollashadi.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Nega `pip install` buyrug'ini virtual muhitsiz ishlatmaslik kerak?

Tasavvur qiling, siz kompyuteringizda ikkita loyiha ustida ishlayapsiz:
1. Birinchi loyiha — eski tizim bo'lib, `Django 3.2` versiyasida yozilgan.
2. Ikkinchi loyiha — eng yangi loyiha bo'lib, `Django 5.1` versiyasini talab qiladi.

Agar siz virtual muhit yaratmasdan, global terminalda `pip install django` qilsangiz, yangi o'rnatilgan Django eski loyihangizning barcha fayllarini buzib qo'yadi!
Virtual muhit esa har bir loyiha uchun alohida "xona" ajratadi: 1-loyiha o'zining eski kutubxonalari bilan, 2-loyiha esa o'zining yangi kutubxonalari bilan tinch va mustaqil ishlaydi.

### 2. .env fayli xavfsizlik madaniyati

Dasturlash tarixida minglab dasturchilar xatosi sababli kompaniyalar millionlab dollar zarar ko'rgan: dasturchi tasodifan maxfiy ma'lumotlar bazasi paroli yoki karta to'lov kaliti yozilgan faylni GitHub-ga `git push` qilib yuboradi.
Maxsus xakerlik botlari GitHub-ni har soniyada tekshirib turadi va parollarni 1 daqiqa ichida o'g'irlab oladi.

Shuning uchun oltin qoida:
- Loyiha ildizida `.gitignore` fayliga `.env` yoziladi!
- Git omboriga faqat `.env.example` namunasi (soxta kalitlar bilan) yuklanadi.
- Haqiqiy maxfiy kalitlar faqat serverning o'zidagi `.env` faylida qoladi.

### 3. Relyatsion bog'lanishlar: PROTECT, CASCADE va SET_NULL

Django ORM-da `ForeignKey` o'chirish harakatlari juda muhim:
- `on_delete=models.CASCADE` &mdash; Ota obyekt o'chsa, unga bog'langan barcha bola obyektlar ham avtomatik o'chadi. Masalan, Post o'chsa, uning ostidagi barcha Comment'lar o'chadi (bu to'g'ri).
- `on_delete=models.PROTECT` &mdash; Agar ota obyektga bog'langan kamida bitta bola obyekt bo'lsa, ota obyektni o'chirishga ruxsat bermaydi (`ProtectedError` chiqaradi). Masalan, "Iqtisodiyot" kategoriyasida 100 ta post bo'lsa, adashib bu kategoriyani o'chirib yuborishning oldini oladi.
- `on_delete=models.SET_NULL` &mdash; Ota obyekt o'chsa, bola obyektdagi havola bo'sh (`NULL`) holatga o'tadi. Masalan, maqola muallifi profili o'chsa, maqola saytda qoladi, muallifi esa "Noma'lum" bo'lib ko'rinadi.

### 4. Clean Architecture va sozlamalar bo'linishi

Biz `settings.py` faylini bitta qilib qoldirmasdan, `settings/` papkasi ichida 3 ga ajratdik:
1. `base.py` &mdash; Barcha muhitlar uchun bir xil bo'lgan sozlamalar (applar, middleware, tillar, vaqt zonasi).
2. `local.py` &mdash; Sizning noutbukingiz uchun (bu yerda `DEBUG = True`, oddiy SQLite ishlatiladi).
3. `prod.py` &mdash; Real ishlab chiqarish serveri uchun (bu yerda `DEBUG = False`, kuchli PostgreSQL, maxsus xavfsizlik filtrlari ishlatiladi).

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **ERD (Entity Relationship Diagram)** | Ma'lumotlar bazasi jadvallari, ularning maydonlari va o'zaro bog'lanishlarini ko'rsatuvchi arxitektura sxemasi. |
| **Virtual Environment (venv)** | Python loyihasi uchun kutubxonalar va bog'liqliklarni izolyatsiya qiluvchi alohida muhit. |
| **requirements.txt** | Loyihaga o'rnatilgan barcha Python paketlari va ularning versiyalari qayd etilgan matnli fayl. |
| **pip freeze** | O'rnatilgan paketlarni aniq versiyalari bilan terminalga chiqaruvchi Python buyrug'i. |
| **.env** | Tizim konfiguratsiyasi va maxfiy kalitlarini saqlash uchun mo'ljallangan muhit fayli. |
| **Clean Architecture** | Dastur kodini o'qilishi oson, sinovdan o'tuvchi va o'zaro bog'liqligi minimal qatlamlarga ajratuvchi loyihalash tamoyili. |
| **One-to-Many (1-N)** | Bir obyektga ko'plab boshqa obyektlar bog'lanishi mumkin bo'lgan munosabat (masalan: bitta Category &rarr; ko'p Post). |
| **Many-to-Many (N-N)** | Ikkala tomondan ham bir nechta bog'lanish mavjud bo'lgan munosabat (masalan: bitta Post &rarr; ko'p Tag, bitta Tag &rarr; ko'p Post). |
| **Slug** | URL manzillarda ishlatish uchun qulay, faqat lotin harflari, sonlar va chiziqchalardan iborat matnli identifikator. |
| **ForeignKey** | Boshqa jadvaldagi qatorga ishora qiluvchi maydon (relyatsion kalit). |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Django freymvorki 2003-yilda AQShning Kanzas shtatidagi "Lawrence Journal-World" yangiliklar gazetasi dasturchilari tomonidan yaratilgan. Shuning uchun ham Django arxitekturasi yangiliklar saytlarini tez va samarali yaratish uchun mukammal moslashgan!
- `pip freeze > requirements.txt` buyrug'i yordamida olingan fayl butun dunyo bo'ylab dasturiy ta'minotni tarqatish va Docker konteynerlariga joylashning universal standarti hisoblanadi.
- PostgreSQL — dunyodagi eng ilg'or ochiq kodli relyatsion ma'lumotlar bazasi bo'lib, u yirik korporatsiyalarda soniyasiga o'n minglab murakkab tranzaksiyalarni xatosiz bajarishga qodir.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Virtual muhit buyruqlari ketma-ketligi <Badge type="tip" text="oson" />
Kompyuterda `blog_api` nomli yangi loyiha papkasini ochish, unda virtual muhit yaratish va uni faollashtirish bo'yicha terminal buyruqlarini tartib bilan yozing (Windows va Linux/Mac uchun).
**Kutiladigan natija:** Ikkala operatsion tizim uchun to'liq buyruqlar ketma-ketligi.

### 2. Kutubxona o'rnatish va tekshirish <Badge type="tip" text="oson" />
Virtual muhit ichiga `django` va `djangorestframework` paketlarini o'rnatish hamda `requirements.txt` faylini yaratish uchun qaysi 2 ta buyruq ishga tushiriladi?
**Kutiladigan natija:** Kutubxonalarni o'rnatish va eksport qilish buyruqlari.

### 3. .env xavfsizligini ta'minlash <Badge type="tip" text="oson" />
Dasturchi o'z loyihasini GitHub-ga yuklashdan oldin `.env` fayli tarmoqqa chiqib ketmasligi uchun nima qilishi kerak? Ushbu qoidani aniq fayl nomi bilan ko'rsating.
**Kutiladigan natija:** `.gitignore` fayliga kiritilishi kerak bo'lgan yozuv va uning sababi.

### 4. Relyatsiyalarni tahlil qilish <Badge type="tip" text="oson" />
NewsPortal loyihasidagi quyidagi juftliklar orasida qanday bog'lanish turi (1-to-1, 1-to-Many yoki Many-to-Many) mavjudligini aniqlang:
1. `Category` va `Post`
2. `Post` va `Tag`
3. `Post` va `Comment`
**Kutiladigan natija:** Har bir juftlik uchun to'g'ri relyatsiya turi.

### 5. .env.example shablonini tuzish <Badge type="warning" text="o'rta" />
NewsPortal loyihasida PostgreSQL bazasiga ulanish uchun `.env.example` shablonini yarating. Unda `SECRET_KEY`, `DEBUG`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` maydonlari bo'lsin.
**Kutiladigan natija:** Xavfsiz, namunaviy konfiguratsiya matni.

### 6. on_delete harakatlarini taqqoslash <Badge type="warning" text="o'rta" />
Tasavvur qiling, "Texnologiya" nomli kategoriya ichida 15 ta yangilik maqolasi bor.
1. Agar `on_delete=models.CASCADE` bo'lsa va admin ushbu kategoriyani o'chirib yuborsa, 15 ta maqolaga nima bo'ladi?
2. Agar `on_delete=models.PROTECT` bo'lsa va admin ushbu kategoriyani o'chirishga harakat qilsa, Django qanday javob qaytaradi?
3. Nima uchun yirik yangiliklar saytida `models.PROTECT` tanlanishi maqsadga muvofiq?
**Kutiladigan natija:** Har ikki holat tahlili va sababi.

### 7. Daraxtsimon (Threaded) izohlar mantiqi <Badge type="warning" text="o'rta" />
Ijtimoiy tarmoqlar va yangiliklar saytlarida bir foydalanuvchining izohiga boshqa foydalanuvchi javob yoza oladi.
Ushbu mantiqni bitta `Comment` jadvali orqali amalga oshirish uchun modelda qanday maydon qo'shilishi kerak? Nega ushbu maydonda `parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)` deb yoziladi?
**Kutiladigan natija:** `self` bog'lanishining vazifasi va uning qanday ishlashi bo'yicha tushuntirish.

### 8. Loyiha arxitekturasidagi xatoni topish <Badge type="warning" text="o'rta" />
Boshlovchi dasturchi o'z loyihasining `settings.py` fayliga quyidagi kodni yozdi:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'rest_framework',
    'news',
]
```
Biroq u ilovalarni `src/apps/news` papkasida yaratgan edi. Nima uchun `python manage.py runserver` qilganda `ModuleNotFoundError: No module named 'news'` xatosi yuz beradi? Xatoni qanday to'g'rilash kerak?
**Kutiladigan natija:** Xato sababi va to'g'ri `apps.news` yozuvi.

### 9. Mini-loyiha: Elektron kutubxona ER diagrammasi <Badge type="danger" text="qiyin" />
Elektron kutubxona tizimi uchun relyatsion ma'lumotlar bazasi sxemasini (ERD) loyihalashtiring:
- Jadvallar: `Author`, `Publisher`, `Book`, `Review`.
- Har bir jadval uchun kamida 4 tadan maydon yozing (maydon nomi va toifasi: masalan `title: CharField`).
- Jadvallar orasidagi bog'lanishlarni (1-N, N-N) va `on_delete` turlarini aniq ko'rsating.
**Kutiladigan natija:** To'liq ma'lumotlar bazasi arxitekturasi loyihasi.

### 10. PostgreSQL va SQLite farqlari tadqiqoti <Badge type="danger" text="qiyin" />
Dastlabki ishlab chiqishda (local development) ko'pincha `SQLite` ishlatiladi, ammo ishlab chiqarishda (production) `PostgreSQL` talab qilinadi.
1. SQLite ning qanday cheklovlari bor (bir vaqtning o'zida yozish, ma'lumotlar hajmi)?
2. PostgreSQL ning qanday kuchli xususiyatlari yirik tizimlar uchun muhim (JSONB maydonlar, to'liq matnli qidiruv, yuqori konkurentlik)?
3. Qanday qilib Django ORM orqali bitta kod bilan ikkala bazada ham bir xil ishlash mumkin?
**Kutiladigan natija:** Ikki ma'lumotlar bazasini chuqur texnik tahlil qiluvchi hisobot.

### 11. Slug yaratish va URL optimizatsiyasi <Badge type="danger" text="qiyin" />
Maqola sarlavhasi: `"Sun'iy intellekt va O'zbekiston yoshlari: 2026-yil istiqbollari!"`.
1. Ushbu sarlavha uchun ideal `slug` qanday ko'rinishda bo'lishi kerak?
2. Nima sababdan URL larda `id` (masalan `/posts/145/`) o'rniga `slug` (masalan `/posts/suniy-intellekt-istiqbollari/`) ishlatish qidiruv tizimlari (SEO) va foydalanuvchilar uchun foydali?
3. Agar ikkita muallif aynan bir xil sarlavhali maqola yozsa, `unique=True` qoidasi qanday muammo keltirib chiqarishi mumkin va uni qanday yechish mumkin?
**Kutiladigan natija:** Slug mexanizmi, SEO ahamiyati va unikallik muammosining texnik yechimi.

### 12. Bonus tadqiqot: Django ORM migrations mexanizmi <Badge type="info" text="bonus" />
`python manage.py makemigrations` va `python manage.py migrate` buyruqlari qanday ishlaydi?
- `makemigrations` buyrug'i qanday fayl hosil qiladi va bu fayl ichida nima saqlanadi?
- `migrate` buyrug'i ma'lumotlar bazasida qaysi maxsus jadval (`django_migrations`) orqali qaysi migratsiyalar bajarilganini kuzatib boradi?
- Agar migratsiya faylini qo'lda o'chirib yuborsak, qanday xavf yuzaga keladi?
**Kutiladigan natija:** Django migratsiya mexanizmini to'liq ochib beruvchi mustaqil tadqiqot.

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Virtual muhit nima uchun kerak va u tizimni qanday himoya qiladi?
2. `pip freeze > requirements.txt` buyrug'i jamoaviy dasturlashda qanday yordam beradi?
3. Maxfiy o'zgaruvchilarni `.env` faylida saqlashning asosiy sababi nima?
4. `models.PROTECT` bilan `models.CASCADE` orasidagi asosiy farqni bitta misol bilan tushuntiring.
5. Django loyihasida ilovalarni alohida `apps/` papkasiga ajratishning qanday ustunliklari bor?
6. `INSTALLED_APPS` ro'yxatida Django REST Framework qanday nom bilan qayd etiladi?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. Konspektdagi terminal buyruqlarini kompyuteringizda ketma-ket bajarib, `newsportal` loyihasini yarating.
2. `src/config/settings/base.py` faylini konspektdagi namuna asosida shakllantiring va `INSTALLED_APPS` ga `'rest_framework'` qo'shing.
3. Loyiha ildizida `.env` faylini yarating va unga `SECRET_KEY` kiriting.
4. Terminalda `python manage.py migrate` buyrug'ini bering va barcha dastlabki jadvallar bazaga yozilganligini tekshiring.

</div>

