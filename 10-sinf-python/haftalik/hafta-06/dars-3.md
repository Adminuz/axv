# 18-dars. Docker orqali deploy qilish

## Dars rejasi (80 daqiqa)

**Maqsad:** Docker tushunchalarini (image, konteyner), FastAPI uchun `Dockerfile` va `.dockerignore` yozishni, `docker-compose.yml` bilan API va PostgreSQL ni birlashtirishni, portlar, `environment`, `volumes` va `depends_on` ni, hamda konteynerni boshqarish va deploy qilish (VPS, Render, Railway) tartibini o'rgatish.

**Manba:** `oquv-qollanma.txt` (Konteynerlashtirish asoslari: Docker, Dockerfile, image, konteyner, docker-compose; «mening kompyuterimda ishlagandi» muammosi; deploy uchun VPS va PaaS), `oquv-dasturi.txt` (Dockerfile, docker-compose, portlar, env va volume'lar). Qo'llanmadagi misol Django (`python:3.10-slim`, gunicorn) uchun; FastAPI uchun `uvicorn` va `python:3.12-slim` ishlatildi.

**Kutiladigan natija:** o'quvchi (1) Image va konteyner farqini, Docker nima muammoni hal qilishini tushuntiradi; (2) FastAPI uchun `Dockerfile` va `.dockerignore` yozadi; (3) `docker build` va `docker run -p` bilan ilovani ishga tushiradi; (4) `docker-compose.yml` da `api` va `db` xizmatlarini bog'laydi (`DATABASE_URL` da host `db`); (5) `docker compose up/logs/down` buyruqlarini ishlatadi.

| Vaqt | Bosqich |
|---|---|
| 10 daq | Takrorlash: 17-dars: sozlamalar, xatolar, testlar |
| 30 daq | Yangi mavzu: Docker tushunchasi, `Dockerfile`; `docker build` va `run`; `.dockerignore` |
| 5 daq | Tanaffus |
| 20 daq | Amaliyot: `docker-compose.yml`: api + PostgreSQL, volume |
| 10 daq | Xavfsizlik va xulosa: Deploy: VPS yoki PaaS, xavfsizlik |
| 5 daq | Xulosa, tezkor nazorat, uyga vazifa |

---

## Mentor konspekti

### 1. Docker, image va konteyner
«Mening kompyuterimda ishlagan-ku!» — muammo turli muhitdan keladi: boshqa Python versiyasi, boshqa kutubxona, boshqa OT. **Docker** bu muammoni konteynerlash bilan hal qiladi. **Image** — tayyor «quti» shabloni: OT, Python, kutubxonalar va kodingiz. **Konteyner** — image dan ishga tushirilgan jonli nusxa. **Dockerfile** — image qanday yasalishi haqida retsept. Qo'llanmadagi tamoyil: qutini bir marta yasaysiz, uni qaysi serverga qo'ysangiz ham (Docker o'rnatilgan bo'lsa), ilova bir xil ishlaydi.

`requirements.txt` ni kodan oldin nusxalash qatlam keshidan foydalanishni ta'minlaydi: kod o'zgarsa kutubxonalar qayta o'rnatilmaydi. `--host 0.0.0.0` bo'lmasa, konteyner tashqarisidan ulanib bo'lmaydi.

### 2. Image yasash va konteyner ishga tushirish
`docker build -t book-api .` joriy papkadagi `Dockerfile` dan `book-api` nomli image yasaydi. `docker run -p 8000:8000 --env-file .env book-api` konteynerni ishga tushiradi: `-p tashqi:ichki` port ulaydi (brauzerda `localhost:8000`), `--env-file` sozlamalarni `.env` dan oladi (maxfiy qiymatlar image ichiga **kiritilmaydi**). **`.dockerignore`** keraksiz va maxfiy narsalarni image ga tushirmaydi: `.env`, `.git`, `__pycache__`, `venv`. Tekshiruv: `docker ps` (ishlayotgan konteynerlar), `docker logs <nom>`, `docker stop <nom>`.

`.dockerignore` ga `.env` ni yozish xavfsizlik uchun muhim: aks holda parollar image ichida qoladi va image ni ulashsangiz ham sizib chiqadi.

### 3. docker-compose bilan xizmatlarni birlashtirish
Loyihada API va PostgreSQL bo'lsa, ularni bitta fayl bilan ko'taramiz: **`docker-compose.yml`**. Har xizmat (`api`, `db`) o'z konteynerida. Muhim qoidalar: 1) xizmatlar bir-biriga **xizmat nomi** bilan murojaat qiladi, shuning uchun `DATABASE_URL` da host `localhost` emas, **`db`** bo'ladi; 2) bazaning ma'lumoti **volume** da saqlanadi, aks holda konteyner o'chganda yo'qoladi; 3) `depends_on` va `healthcheck` baza tayyor bo'lgach API ni ishga tushiradi; 4) parollar `.env` dan `${DB_PASSWORD}` orqali olinadi. Ishga tushirish: `docker compose up -d --build`.

Migratsiya: `docker compose exec api alembic upgrade head`. To'xtatish: `docker compose down` (volume saqlanadi); `down -v` esa bazani ham o'chiradi.

---

## Kod namunalari

### 1. Dockerfile
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 2. .dockerignore
```text
.env
.git
__pycache__/
venv/
uploads/
```

### 3. docker-compose.yml va .env
```yaml
# docker-compose.yml
services:
  api:
    build: .
    ports: ["8000:8000"]
    environment:
      DATABASE_URL: postgresql+asyncpg://book:${DB_PASSWORD}@db:5432/books
    depends_on:
      db:
        condition: service_healthy
    volumes: ["uploads:/app/uploads"]
  db:
    image: postgres:16
    environment:
      POSTGRES_USER: book
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: books
    volumes: ["pgdata:/var/lib/postgresql/data"]
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U book -d books"]
      interval: 5s
      retries: 5
volumes:
  pgdata:
  uploads:
# .env (GitHub ga yubormang):
# DB_PASSWORD=o'zingizning-parolingiz
```

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq (Oson): Dockerfile
`python:3.12-slim` asosida FastAPI uchun Dockerfile yozing.

**Yechim:** 
```bash
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 2-topshiriq (Oson): .dockerignore
Image ga tushmasligi kerak bo'lgan 4 ta narsani yozing.

**Yechim:** 
```bash
.env
.git
__pycache__
venv
```

### 3-topshiriq (O'rta): Build va run
Image yasang va 8000-portda ishga tushiring.

**Yechim:** 
```bash
docker build -t book-api .
docker run -d --name api -p 8000:8000 --env-file .env book-api
```

### 4-topshiriq (O'rta): DB hosti
Compose da `DATABASE_URL` hostini nima uchun `db` qilamiz?

**Yechim:** Konteynerlar bir-biriga xizmat nomi bilan murojaat qiladi; `localhost` — konteynerning o'zi.

### 5-topshiriq (Qiyin): Volume
PostgreSQL ma'lumoti o'chmasligi uchun volume qo'shing.

**Yechim:** 
```bash
services:
  db:
    volumes: ["pgdata:/var/lib/postgresql/data"]
volumes:
  pgdata:
```

### 6-topshiriq (Qo'shimcha): Migratsiya
Compose ichida alembic migratsiyasini bajaring.

**Yechim:** `docker compose exec api alembic upgrade head`.

---

## Tezkor nazorat savollari

1. Image va konteyner farqi?
   - **Javob:** Image — shablon; konteyner — ishlayotgan nusxa.
2. Dockerfile nima?
   - **Javob:** Image qanday yasalishi haqida retsept.
3. `-p 8000:8000` nima?
   - **Javob:** Kompyuter va konteyner portlarini ulaydi.
4. Compose da baza hosti?
   - **Javob:** Xizmat nomi (`db`), `localhost` emas.
5. Volume nima uchun?
   - **Javob:** Ma'lumot konteyner o'chganda yo'qolmasligi uchun.

---

## Uyga vazifa

`uyga-vazifa.md` ga qarang.
