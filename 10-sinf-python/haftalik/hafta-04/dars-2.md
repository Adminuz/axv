# 11-dars. Tayyor loyihani hostingga joylash (deploy)

## Dars rejasi (80 daqiqa)

**Maqsad:** o'quvchi deploy tushunchasini, Local va Production muhit farqini, `prod.py` sozlamalarini, Gunicorn, Nginx va Docker rolini tushunadi hamda NewsPortal ni Docker + Nginx + Gunicorn + PostgreSQL arxitekturasida ishga tushirishning qadamlarini bajaradi.

**Kutiladigan natija:** o'quvchi (1) Local va Production farqini ayta oladi; (2) `DEBUG`, `ALLOWED_HOSTS`, `.env`, `collectstatic` ning vazifasini tushuntiradi; (3) Dockerfile va `docker-compose.prod.yml` ni o'qiy oladi; (4) deploy checklistini tekshiradi; (5) hosting turlarini (Shared, PaaS, VPS) taqqoslaydi.

| Vaqt | Bosqich |
|---|---|
| 10 daq | Takrorlash: 10-dars (API xavfsizligi). Savol: `DEBUG=True` productionda nega xavfli? |
| 30 daq | Yangi mavzu: deploy, Local va Production, `settings`, static/media, WSGI/Gunicorn, Nginx |
| 5 daq | Tanaffus |
| 20 daq | Docker, `docker-compose.prod.yml`, hosting turlari, VPS qadamlari, CI/CD |
| 10 daq | Amaliyot: `prod.py`, Dockerfile, compose, checklist |
| 5 daq | Xulosa, tezkor nazorat, uyga vazifa |

Eslatma: dasturda bu mavzu «oraliq nazorat» bilan bog'langan. Mentor shu haftada deploy bo'yicha amaliy topshiriqni oraliq nazorat elementi sifatida baholashi mumkin (`baholash.md` ga qarang).

---

## Mentor konspekti

### 1. Deploy va muhitlar
**Deploy** — tayyor loyihani serverga joylab, foydalanuvchilarga ochiq qilish. Qo'llanma o'xshatishi: mashina ustaxonada (Local) kapoti ochiq yig'iladi; trassaga (Production) chiqqanda kapot yopiq, xavfsiz va har qanday ob-havoga chidamli bo'lishi shart.

| | Local (Development) | Production |
|---|---|---|
| Xato ko'rsatish | `DEBUG=True` qizil oyna | Oddiy 404/500 sahifa |
| Baza | SQLite (yengil) | PostgreSQL/MySQL |
| Server | `manage.py runserver` | Gunicorn + Nginx |
| Ustuvorlik | Qulaylik va tezlik | Xavfsizlik va barqarorlik |

### 2. `settings.py` ni tayyorlash
- **`DEBUG = False`**: aks holda xato sahifasi sirlarni (parol, kalit) ko'rsatib qo'yishi mumkin.
- **`ALLOWED_HOSTS`**: ruxsat etilgan domenlar ro'yxati (HTTP Host Header Injection dan himoya).
- **`SECRET_KEY` va parollar** `.env` da (Environment Variables), `.env` esa `.gitignore` da. `os.environ` orqali o'qiladi.
- **Baza:** SQLite o'rniga PostgreSQL (SQLite da yozish bloklanishi, database lock).

### 3. Static va Media
- Productionda (`DEBUG=False`) Django statik fayllarni tarqatmaydi: Python qimmat resurs, buni Nginx 10 barobar tezroq qiladi.
- `STATIC_ROOT` ko'rsatiladi, serverda `python manage.py collectstatic` fayllarni bitta `staticfiles` papkasiga yig'adi. Muqobil: WhiteNoise.
- Media (foydalanuvchi yuklagan fayllar): oddiy VPS da `MEDIA_ROOT`; bulutda (ephemeral storage) esa Object Storage (AWS S3, DigitalOcean Spaces) va `django-storages`.

### 4. WSGI, Gunicorn, Nginx
- `runserver` faqat development uchun. Productionda **WSGI** standarti va uning serveri **Gunicorn**: `gunicorn config.wsgi:application --workers 3`. Workers — mustaqil jarayonlar; bittasi band bo'lsa so'rov boshqasiga yo'naltiriladi, o'lsa Gunicorn yangisini yaratadi.
- WebSocket kerak bo'lsa WSGI o'rniga ASGI va Uvicorn.
- **Nginx (Reverse Proxy):** binoning qabulxona xodimi. `/static/` va `/media/` ni o'zi beradi, qolgan so'rovlarni Gunicorn ga uzatadi (Proxy Pass), sekin so'rovlarni (Slowloris) o'zi yig'adi, SSL (HTTPS) ni boshqaradi (SSL Termination).
- Oqim: `Client -> Nginx (:80/:443) -> Gunicorn (:8000) -> Django -> PostgreSQL`.

### 5. Docker
«Mening kompyuterimda ishlagandi» muammosi: Python/Windows/kutubxona versiyalari farqi. **Docker** konteyner ichiga OS, Python, kod va kutubxonalarni joylaydi. `Dockerfile` — quti retsepti, undan **Image**, image dan **Container** ishga tushadi. `docker-compose.yml` bir necha servisni (Django, Postgres, Nginx) bir tugma bilan ko'taradi. Volumes: konteyner qayta ishga tushsa ham `postgres_data`, `staticfiles`, `media` yo'qolmaydi.

### 6. Hosting turlari
| Tur | Xususiyati |
|---|---|
| Shared (cPanel) | Arzon, PHP uchun mo'ljallangan, root yo'q, Django uchun noqulay |
| PaaS (Heroku, Render, Railway, PythonAnywhere) | Eng oson, kodni GitHub bilan bog'laysiz; qimmat, sozlash cheklangan |
| VPS/VDS (DigitalOcean, Hetzner, AWS EC2) | Eng to'g'ri va professional: bo'sh Linux server, hammasini o'zingiz sozlaysiz |

### 7. VPS ga joylash xaritasi
1. `ssh` bilan ulanish; 2. `apt update` / `upgrade`; 3. Docker o'rnatish (`docker.io docker-compose-plugin`); 4. `git clone`; 5. `.env.prod` yaratish; 6. `docker compose ... up -d --build`; 7. domen (DNS) va SSL (Let's Encrypt, certbot yoki Nginx Proxy Manager/Traefik).

### 8. CI/CD
**CI:** `git push` bo'lganda robot (GitHub Actions) testlarni yurgizadi; test yiqilsa jarayon to'xtaydi. **CD:** testlar yashil bo'lsa robot serverga SSH orqali ulanib `git pull`, `migrate`, Gunicorn restart qiladi. Kod: `.github/workflows/deploy.yml`.

---

## Kod namunalari

### 1. `config/settings/prod.py`
```python
import os
from .base import *  # noqa

DEBUG = False
SECRET_KEY = os.environ["SECRET_KEY"]
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR.parent / "staticfiles"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR.parent / "media"
```

### 2. `Dockerfile`
```dockerfile
FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY src /app/src
WORKDIR /app/src
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
```
`requirements.txt` alohida nusxalanadi: build cache tezlashadi.

### 3. `docker-compose.prod.yml` (qisqartirilgan)
```yaml
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_DB: ${DB_NAME}
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: always
  web:
    build: .
    env_file: [.env.prod]
    depends_on: [db]
    volumes: [staticfiles:/app/staticfiles, media:/app/media]
    command: >
      sh -c "python manage.py migrate &&
      python manage.py collectstatic --noinput &&
      gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 60"
    restart: always
  nginx:
    image: nginx:1.27
    ports: ["80:80"]
    volumes:
      - ./deploy/nginx.conf:/etc/nginx/conf.d/default.conf:ro
      - staticfiles:/staticfiles:ro
      - media:/media:ro
    depends_on: [web]
    restart: always
volumes:
  postgres_data:
  staticfiles:
  media:
```

### 4. `deploy/nginx.conf`
```nginx
server {
    listen 80;
    client_max_body_size 20M;
    location /static/ { alias /staticfiles/; expires 7d; }
    location /media/  { alias /media/;       expires 7d; }
    location / {
        proxy_pass http://web:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 5. `.env.prod` va ishga tushirish
```bash
# .env.prod (namuna, haqiqiy qiymatlarni GitHub ga yuklamang)
DJANGO_SETTINGS_MODULE=config.settings.prod
SECRET_KEY=REPLACE_WITH_LONG_RANDOM_SECRET
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
DB_NAME=newsportal_db
DB_USER=newsportal_user
DB_PASSWORD=STRONG_PASSWORD
DB_HOST=db
DB_PORT=5432

docker compose -f docker-compose.prod.yml --env-file .env.prod up -d --build
docker logs -f newsportal_web
```
`DB_HOST=db` — compose dagi servis nomi.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq (Oson): Local va Production
Beshta farqni jadvalga yozing: xato ko'rsatish, baza, server, statik fayl, sirlar.

**Yechim:** Local: `DEBUG=True`, SQLite, `runserver`, Django beradi, sirlar kodda bo'lishi mumkin. Production: `DEBUG=False`, PostgreSQL, Gunicorn+Nginx, Nginx beradi, sirlar `.env` da.

### 2-topshiriq (O'rta): `prod.py` yozish
`DEBUG`, `SECRET_KEY` va `ALLOWED_HOSTS` ni env dan o'qiydigan, cookie larni secure qiladigan `prod.py` yozing.

**Yechim:** Kod namunasi 1 dagi `prod.py`. Tekshiruv: `ALLOWED_HOSTS` bo'sh bo'lsa so'rov `400 Bad Request` qaytaradi.

### 3-topshiriq (Qiyin): Compose ni ishga tushirish va checklist
`docker-compose.prod.yml` ni mahalliy ishga tushiring: `http://localhost/api/v1/posts/` va `/admin/` ochilishini, `/static/` va `/media/` ishlashini tekshiring.

**Yechim:** Buyruq: `docker compose -f docker-compose.prod.yml --env-file .env.prod up -d --build`. Checklist: `DEBUG=False` ishlayaptimi, `/admin/` ochiladimi, `collectstatic` natijasi `/static/` dan keladimi, upload fayl `/media/` dan ochiladimi, `migrate` xatosiz o'tdimi, `ALLOWED_HOSTS` to'g'rimi, DB paroli kuchlimi, backup reja (Postgres volume) bormi.

---

## Tezkor nazorat savollari

1. Deploy nima?
   - **Javob:** Tayyor loyihani serverga joylab, foydalanuvchilarga ochiq qilish.
2. Nega productionda `runserver` ishlatilmaydi?
   - **Javob:** U faqat development uchun; xavfsizlik auditidan o'tmagan va yuklamaga mo'ljallanmagan. Gunicorn ishlatiladi.
3. Nginx ning vazifasi?
   - **Javob:** Reverse proxy: statik/media ni o'zi beradi, qolganini Gunicorn ga uzatadi, SSL ni boshqaradi.
4. `collectstatic` nima qiladi?
   - **Javob:** Barcha statik fayllarni `STATIC_ROOT` papkasiga yig'adi.
5. Docker qanday muammoni hal qiladi?
   - **Javob:** «Mening kompyuterimda ishlagandi» muammosini: muhit konteyner ichida bir xil bo'ladi.
6. Eng professional hosting turi qaysi (qo'llanma bo'yicha)?
   - **Javob:** VPS/VDS.

---

## Uyga vazifa

`uyga-vazifa.md` ga qarang.
