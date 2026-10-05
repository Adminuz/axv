---
title: "4-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "10-sinf (Python)", "link": "/10-sinf-python/"}, "n": 4, "bob": "I-bob · Django REST freymvork", "lessons": [{"g": 10, "title": "API havfsizligini ta'minlash", "lead": "Qalin devorli binoning ochiq eshigi: sizning API ingiz ham shunday bo'lmasin! Bu darsda JWT, ruxsatlar, throttling, CORS va production sozlamalari bilan API ni haker hujumlaridan himoyalashni o'rganasiz.", "link": "/10-sinf-python/hafta-04/dars-1", "slide": "/slaydlar/10-sinf-python/hafta-04/dars-1.html", "test": "/slaydlar/10-sinf-python/hafta-04/dars-1-test.html"}, {"g": 11, "title": "Tayyor loyihani hostingga joylash (deploy)", "lead": "Loyihangiz kompyuteringizda ishlayapti, lekin butun dunyo uni ko'ra oladimi? Bu darsda Gunicorn, Nginx va Docker yordamida API ni serverga chiqarishni o'rganasiz.", "link": "/10-sinf-python/hafta-04/dars-2", "slide": "/slaydlar/10-sinf-python/hafta-04/dars-2.html", "test": "/slaydlar/10-sinf-python/hafta-04/dars-2-test.html"}, {"g": 12, "title": "FastAPI loyiha yaratish. Loyiha uchun MB ni loyihalash va yaratish, dastlabki sozlamalar", "lead": "Django dan keyin yangi sarguzasht: FastAPI! Bugun noldan E-Library loyihasining poydevorini quramiz: papkalar, baza dizayni, sozlamalar va birinchi ishlaydigan /health endpoint.", "link": "/10-sinf-python/hafta-04/dars-3", "slide": "/slaydlar/10-sinf-python/hafta-04/dars-3.html", "test": "/slaydlar/10-sinf-python/hafta-04/dars-3-test.html"}], "test": "/slaydlar/10-sinf-python/hafta-04/hafta-test.html"}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Ushbu haftada o'tilgan darslar bo'yicha uyga vazifalar ro'yxati:

---

### 10-dars. API havfsizligini ta'minlash
1. `settings/base.py` ga `SIMPLE_JWT` ni sozlang: Access 10 daqiqa, Refresh 7 kun, rotate va blacklist yoqilgan. `token_blacklist` ilovasini qo'shib, `migrate` qiling.
2. `IsAuthor` permissionini yozib PostViewSet ga ulang. Boshqa foydalanuvchi PATCH qilganda `403` qaytishini tekshiring.
3. Qo'llanmadagi security checklist bo'yicha loyihangizni tekshiring va kamida 3 ta kamchilikni tuzating.

---

### 11-dars. Tayyor loyihani hostingga joylash (deploy)
1. `config/settings/prod.py` ni yozing: `DEBUG=False`, `SECRET_KEY` va `ALLOWED_HOSTS` env dan o'qilsin.
2. Loyihangizga `Dockerfile`, `docker-compose.prod.yml` va `deploy/nginx.conf` qo'shing.
3. Mahalliy kompyuterda `docker compose -f docker-compose.prod.yml --env-file .env.prod up -d --build` ni ishga tushirib, deploy checklistni to'ldiring.

---

### 12-dars. FastAPI loyiha yaratish. MB ni loyihalash
1. O'z FastAPI loyihangizni tanlang va mini texnik topshiriq (TT) tuzing.
2. TT asosida MB ni loyihalang (kamida 2-3 jadval, PK/FK, bog'lanish turlari).
3. Venv, kutubxonalar, `.env`, `config.py`, `database.py` va `main.py` ni yaratib, `/health` va `/docs` ni tekshiring.

---

</div>
