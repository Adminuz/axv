# 4-hafta: Uyga vazifalar to'plami (Advanced Python Back-end)

Ushbu haftada o'tilgan darslar bo'yicha uyga vazifalar ro'yxati:

---

## 10-dars. API havfsizligini ta'minlash
1. `settings/base.py` ga `SIMPLE_JWT` ni sozlang: Access 10 daqiqa, Refresh 7 kun, rotate va blacklist yoqilgan. `token_blacklist` ilovasini qo'shib, `migrate` qiling.
2. `IsAuthor` permissionini yozib PostViewSet ga ulang. Boshqa foydalanuvchi PATCH qilganda `403` qaytishini tekshiring.
3. Qo'llanmadagi security checklist bo'yicha loyihangizni tekshiring va kamida 3 ta kamchilikni tuzating.

---

## 11-dars. Tayyor loyihani hostingga joylash (deploy)
1. `config/settings/prod.py` ni yozing: `DEBUG=False`, `SECRET_KEY` va `ALLOWED_HOSTS` env dan o'qilsin.
2. Loyihangizga `Dockerfile`, `docker-compose.prod.yml` va `deploy/nginx.conf` qo'shing.
3. Mahalliy kompyuterda `docker compose -f docker-compose.prod.yml --env-file .env.prod up -d --build` ni ishga tushirib, deploy checklistni to'ldiring.

---

## 12-dars. FastAPI loyiha yaratish. MB ni loyihalash
1. O'z FastAPI loyihangizni tanlang va mini texnik topshiriq (TT) tuzing.
2. TT asosida MB ni loyihalang (kamida 2-3 jadval, PK/FK, bog'lanish turlari).
3. Venv, kutubxonalar, `.env`, `config.py`, `database.py` va `main.py` ni yaratib, `/health` va `/docs` ni tekshiring.

---

## Mentor uchun

### Baholash mezonlari (100 ballik tizim)

1. **API xavfsizligi (35 ball):**
   - SimpleJWT to'g'ri sozlangani, rotate va blacklist (15 ball);
   - Custom permission va `403` sinovi (10 ball);
   - Security checklist bo'yicha tuzatilgan kamchiliklar (10 ball).

2. **Deploy (35 ball):**
   - `prod.py` va `.env` da sirlarning ajratilgani (10 ball);
   - Dockerfile va compose faylining to'g'riligi (15 ball);
   - Deploy checklist to'ldirilgani va ishga tushirish natijasi (10 ball).

3. **FastAPI loyiha va MB dizayni (30 ball):**
   - Mini TT va ER dizayn (15 ball);
   - Skeleton ishga tushishi: `/health` va Swagger (15 ball).

### Kutiladigan namunaviy natijalar
- Noto'g'ri parol bilan ketma-ket urinishda login endpoint `429` qaytaradi.
- `docker compose ... up -d --build` dan so'ng `http://localhost/api/v1/posts/` ochiladi.
- `uvicorn app.main:app --reload` dan so'ng `/health` `{"status": "ok"}` qaytaradi.
