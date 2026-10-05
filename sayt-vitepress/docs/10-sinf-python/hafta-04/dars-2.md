---
title: "11-dars. Tayyor loyihani hostingga joylash (deploy)"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (Python)", "link": "/10-sinf-python/"}, "week": {"n": 4, "link": "/10-sinf-python/hafta-04/"}, "g": 11, "title": "Tayyor loyihani hostingga joylash (deploy)", "lead": "Loyihangiz kompyuteringizda ishlayapti, lekin butun dunyo uni ko'ra oladimi? Bu darsda Gunicorn, Nginx va Docker yordamida API ni serverga chiqarishni o'rganasiz.", "slide": "/slaydlar/10-sinf-python/hafta-04/dars-2.html", "test": "/slaydlar/10-sinf-python/hafta-04/dars-2-test.html", "tabs": [{"g": 10, "link": "/10-sinf-python/hafta-04/dars-1", "current": false}, {"g": 11, "link": "/10-sinf-python/hafta-04/dars-2", "current": true}, {"g": 12, "link": "/10-sinf-python/hafta-04/dars-3", "current": false}], "prev": {"g": 10, "title": "API havfsizligini ta'minlash", "link": "/10-sinf-python/hafta-04/dars-1"}, "next": {"g": 12, "title": "FastAPI loyiha yaratish. Loyiha uchun MB ni loyihalash va yaratish, dastlabki sozlamalar", "link": "/10-sinf-python/hafta-04/dars-3"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Deploy** — tayyor loyihani serverga joylab, foydalanuvchilarga ochiq qilish.
- Local (Development) muhitda qulaylik, Production da xavfsizlik va barqarorlik muhim.
- Production sozlamalari: `DEBUG = False`, `ALLOWED_HOSTS`, sirlar `.env` da, PostgreSQL.
- Statik fayllar `collectstatic` bilan yig'ilib, Nginx orqali beriladi.
- `runserver` o'rniga **Gunicorn** (WSGI), uning oldida **Nginx** (Reverse Proxy) turadi.
- **Docker** loyihani konteynerga joylab, muhit farqi muammosini hal qiladi.
- Hosting turlari: Shared, PaaS, VPS; **CI/CD** deploy jarayonini avtomatlashtiradi.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Ustaxona va trassa
Mashinani ustaxonada (Local) yig'asiz: kapot ochiq, har qismga ko'zingiz tushadi. Trassaga (Production) chiqqanda esa kapot yopiq va mashina yo'lovchilar uchun xavfsiz bo'lishi kerak. Shu sababli productionda xato sahifalari yashiriladi, kuchli baza va tezkor server qo'yiladi.

### 2. Gunicorn va Nginx: ofis va qabulxona
Nginx — binoning qabulxona xodimi: kelgan mehmonni kutib oladi, oddiy so'rov (rasm, CSS) bo'lsa o'zi javob beradi. Murakkab savol bo'lsa (`/api/users/`) ichkaridagi mutaxassisga, ya'ni Gunicorn ga uzatadi. Gunicorn Django kodini ishlatib, javobni Nginx ga qaytaradi.

```text
Client -> Nginx (:80/:443) -> Gunicorn (:8000) -> Django -> PostgreSQL
```

### 3. Nega `DEBUG = False` bo'lsa Django ALLOWED_HOSTS so'raydi?
Agar kimdir soxta domen nomidan serveringizga so'rov yuborsa, Django uni ro'yxatda yo'qligi uchun rad etadi. Bu HTTP Host Header Injection hujumidan himoya.

```python
ALLOWED_HOSTS = ["api.meningloyiham.uz"]
```

### 4. Dockerfile — qutining retsepti
```dockerfile
FROM python:3.12-slim      # asos: toza Python
WORKDIR /app               # ichida papka
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY src /app/src
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
```
Retseptdan **Image** (tayyor quti) yasaladi, image dan **Container** (ishlayotgan quti) ishga tushadi.

### 5. Odatiy xatolar
- `DEBUG = True` ni serverda qoldirish.
- `.env` yoki `SECRET_KEY` ni GitHub ga yuklash.
- `collectstatic` ni unutib, `/static/` dan fayl topilmasligi.
- Compose da `DB_HOST` ga `localhost` yozish (to'g'risi: servis nomi, `db`).
- Baza uchun volume qo'ymaslik: konteyner o'chsa ma'lumot yo'qoladi.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Deploy | Loyihani serverga joylash va ishga tushirish |
| Production | Haqiqiy foydalanuvchilar ishlatadigan jonli muhit |
| Environment Variables (.env) | Sirlar va sozlamalar saqlanadigan muhit o'zgaruvchilari |
| WSGI | Veb-server va Python ilova orasidagi standart |
| Gunicorn | Production uchun WSGI server |
| Nginx | Reverse Proxy va tezkor veb-server |
| Reverse Proxy | So'rovni qabul qilib, ichki serverga uzatuvchi vositachi |
| Docker | Ilovani konteynerga joylash texnologiyasi |
| Dockerfile | Image yaratish retsepti |
| VPS | Virtual Private Server: o'zingiz sozlaydigan virtual server |
| CI/CD | Test va deploy ni avtomatlashtirish |
| Volume | Konteyner qayta ishga tushsa ham saqlanadigan ma'lumot joyi |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Django hujjatlarida `runserver` haqida: «Hech qachon uni production muhitida ishlatmang».
- Gunicorn bir necha `workers` (jarayon) yaratadi: bittasi «o'lsa», Gunicorn avtomatik yangisini ishga tushiradi.
- Docker davridan oldin dasturchilar «bu kod mening noutbukimda ishlayapti-ku!» muammosiga soatlab vaqt yo'qotardi.
- VPS ni oyiga taxminan 4-5 dollarga olish mumkin (qo'llanma bo'yicha); unda ekran ham, sichqoncha ham yo'q, hammasi buyruq qatori orqali.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Muhitlarni taqqoslang <Badge type="tip" text="oson" />
Local va Production muhitlarining kamida 4 ta farqini jadvalga yozing.

**Kutiladigan natija:** Jadval: DEBUG, baza, server, ustuvorlik.

### 2. Atamalarni juftlang <Badge type="tip" text="oson" />
Gunicorn, Nginx, Docker, PostgreSQL va ularning vazifalari: «konteyner», «reverse proxy», «WSGI server», «baza» ni juftlang.

**Kutiladigan natija:** 4 ta to'g'ri juftlik.

### 3. Bu nima? <Badge type="tip" text="oson" />
`python manage.py collectstatic` buyrug'i nima qiladi va `STATIC_ROOT` nima uchun kerak?

**Kutiladigan natija:** Barcha statik fayllarni `STATIC_ROOT` papkasiga yig'adi; Nginx shu papkadan beradi.

### 4. Xavfli sozlamani toping <Badge type="tip" text="oson" />
`DEBUG = True`, `SECRET_KEY = "django-insecure-..."` kodda, `ALLOWED_HOSTS = []`: productionda bular nega xavfli?

**Kutiladigan natija:** Xato sahifasi sirlarni ochadi; kalit GitHub ga tushsa xavfsizlik buziladi; bo'sh ro'yxat bilan Django ishlamaydi.

### 5. `prod.py` yozing <Badge type="warning" text="o'rta" />
`DEBUG=False`, `SECRET_KEY` va `ALLOWED_HOSTS` ni `os.environ` dan o'qiydigan, `SESSION_COOKIE_SECURE` va `CSRF_COOKIE_SECURE` yoqilgan `prod.py` yozing.

**Kutiladigan natija:** `config.settings.prod` bilan loyiha ishga tushadi, `.env` dagi qiymatlar o'qiladi.

### 6. Dockerfile ni o'qing <Badge type="warning" text="o'rta" />
```dockerfile
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY src /app/src
```
Nega `requirements.txt` kod dan alohida nusxalanadi?

**Kutiladigan natija:** Kod o'zgarganda kutubxonalar qayta o'rnatilmaydi: build cache tezlashadi.

### 7. Nginx oqimi <Badge type="warning" text="o'rta" />
Foydalanuvchi `/static/logo.png` va `/api/v1/posts/` ni so'radi. Har birini kim qaytaradi?

**Kutiladigan natija:** `/static/logo.png` ni Nginx o'zi beradi; `/api/v1/posts/` Gunicorn ga uzatiladi.

### 8. Compose xatosini toping <Badge type="warning" text="o'rta" />
`.env.prod` da `DB_HOST=localhost` yozilgan va `web` konteyneri bazaga ulana olmayapti. Sabab nima?

**Kutiladigan natija:** Konteyner ichidagi `localhost` o'zi; bazaga compose servis nomi `db` orqali ulanish kerak (`DB_HOST=db`).

### 9. Docker Compose ni ishga tushirish <Badge type="danger" text="qiyin" />
`docker compose -f docker-compose.prod.yml --env-file .env.prod up -d --build` ni bajaring va `http://localhost/api/v1/posts/` ni oching.

**Kutiladigan natija:** Brauzerda API ro'yxati ochiladi; `docker logs -f newsportal_web` da xato yo'q.

### 10. Deploy checklist <Badge type="danger" text="qiyin" />
Qo'llanmadagi 8 bandli productionda tekshiriladigan checklistni o'z loyihangizda to'ldiring.

**Kutiladigan natija:** Har band uchun «bajarildi / bajarilmadi» va izoh.

### 11. Hosting tanlash <Badge type="danger" text="qiyin" />
Maktab klubi uchun kichik API ni qaysi hostingga joylagan bo'lardingiz: Shared, PaaS yoki VPS? Ikkita sabab keltiring.

**Kutiladigan natija:** Asoslangan tanlov (masalan PaaS: oson; VPS: arzon va to'liq nazorat) va kamchiliklari.

### 12. Mustaqil tadqiqot <Badge type="info" text="bonus" />
cPanel da Python App (Passenger) orqali Django ni joylash qadamlarini o'rganing va 5 qadamli qisqa yo'riqnoma yozing.

**Kutiladigan natija:** 5 qadamli yo'riqnoma va manbalar ro'yxati.

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Local va Production muhitning asosiy farqlari qanday?
2. `DEBUG = True` ni productionda qoldirish nega xavfli?
3. `.env` fayli nima uchun kerak va nega u `.gitignore` da bo'lishi shart?
4. `runserver` o'rniga Gunicorn nega ishlatiladi?
5. Nginx Gunicorn oldida nima uchun turadi?
6. Docker image va container farqi nima?
7. Shared, PaaS va VPS hostinglarning farqini ayting.
8. CI va CD nimani anglatadi?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

(20-30 daqiqa) `prod.py` ni yozing, Dockerfile va `docker-compose.prod.yml` ni loyihangizga qo'shing va deploy checklistni to'ldiring. To'liq ro'yxat: `uyga-vazifa.md`.

</div>

