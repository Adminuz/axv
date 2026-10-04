# 2-dars. DRF loyiha qurish: MBni loyihalash. Loyihani yaratish, dastlabki sozlamalar

## Dars rejasi (80 daqiqa)

1. **O'tgan mavzuni takrorlash (10 daqiqa):** SSR va USR/CSR farqlari, RESTful API tamoyillari, JSON formati bo'yicha tezkor savol-javob.
2. **Yangi mavzu: Mini-TT va Ma'lumotlar bazasini loyihalash (20 daqiqa):**
   - NewsPortal loyihasi maqsadi va vazifalari.
   - Foydalanuvchi rollari: Guest, User, Admin.
   - Relyatsion MB modeli (ERD): Category, Tag, Post, Comment jadvallari, 1-N (One-to-Many) va N-N (Many-to-Many) bog'lanishlar.
3. **Yangi mavzu: Professional loyiha arxitekturasi va muhit (25 daqiqa):**
   - Virtual muhit (venv) yaratish va faollashtirish (Windows, Mac/Linux).
   - Kerakli kutubxonalar: `django`, `djangorestframework`, `python-dotenv`, `psycopg2-binary`.
   - Modulli clean arxitektura: `src/`, `config/settings/base.py`, `local.py`, `prod.py`, `apps/` papkalari.
   - `.env` faylida maxfiy o'zgaruvchilarni saqlash (xavfsizlik qoidalari).
4. **Amaliyot: Loyihani noldan yaratish va sozlash (15 daqiqa):**
   - Terminalda buyruqlarni bajarish, `manage.py` ishga tushirish, `INSTALLED_APPS` ga `'rest_framework'` qo'shish.
   - `python manage.py migrate` va `runserver` orqali tizimni tekshirish.
5. **Dars xulosasi va tezkor nazorat (10 daqiqa):** O'quvchilar loyihasini tekshirish, savol-javob, uyga vazifa.

---

## Mentor konspekti

### 1. Loyiha konsepsiyasi: NewsPortal (Yangiliklar portali)

Ushbu bob davomida biz real kompaniyalar darajasidagi **NewsPortal** veb-servisi uchun to'liq backend API quramiz.
Loyiha mini-texnik topshirig'i (mini-TT):
- **Maqsad:** Ro'yxatdan o'tgan foydalanuvchilar va mehmonlar uchun yangiliklar, kategoriyalar, teglar va muhokamalar (izohlar) taqdim etuvchi xavfsiz REST API.
- **Rollar:**
  - `Guest (Mehmon):` yangiliklar ro'yxatini va maqola matnini ko'rish.
  - `User (Foydalanuvchi):` tizimga kirish, profil boshqaruvi, maqolalarga izoh yozish.
  - `Admin / Staff:` barcha yangiliklarni yaratish, tahrirlash, o'chirish (CRUD) va izohlarni moderatsiya qilish (`is_approved`).

### 2. Ma'lumotlar bazasi loyihasi (ERD - Entity Relationship Diagram)

Loyiha uchun 4 ta asosiy biznes jadvali loyihalashtiriladi:
1. **Category (Kategoriya):** `id`, `name`, `slug`, `created_at`.
2. **Tag (Teg):** `id`, `name`, `slug`, `created_at`.
3. **Post (Yangilik / Maqola):**
   - `id`, `title`, `slug`, `excerpt` (qisqa mazmun), `body` (matn);
   - `cover_image` (muqova rasmi);
   - `status` (`draft` - qoralama, `published` - e'lon qilingan, `archived` - arxivlangan);
   - `published_at` (chop etilgan vaqt);
   - `category_id` (ForeignKey &rarr; Category, `on_delete=models.PROTECT`);
   - `tags` (ManyToManyField &rarr; Tag);
   - `created_at`, `updated_at`.
4. **Comment (Izoh):**
   - `id`, `post_id` (ForeignKey &rarr; Post, `CASCADE`);
   - `parent_id` (ForeignKey &rarr; self, zanjirli/daraxtsimon javob izohlar uchun);
   - `name`, `email`, `body`, `is_approved`.

**Muhim qoidalar:**
- `slug` maydonlari har bir jadvalda noyob (`unique=True`) bo'lishi shart;
- Kategoriya o'chirilganda undagi maqolalar tasodifan o'chib ketmasligi uchun `PROTECT` cheklovi qo'yiladi.

### 3. Professional loyiha strukturasi (Clean Modular Architecture)

Barcha fayllarni bitta papkaga tashlash o'rniga, yirik ishlab chiqarish standartlariga mos **feature-based apps** strukturasidan foydalanamiz:

```text
newsportal/
├── .env                  # Maxfiy kalitlar va muhit o'zgaruvchilari
├── .gitignore            # Git-ga kiritilmaydigan fayllar (venv, .env, media)
├── requirements.txt      # Loyiha kutubxonalari ro'yxati
└── src/
    ├── manage.py
    ├── config/           # Asosiy loyiha sozlamalari
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── settings/
    │       ├── base.py   # Barcha muhitlar uchun umumiy sozlamalar
    │       ├── local.py  # Dasturchining kompyuteri uchun (DEBUG=True)
    │       └── prod.py   # Real server uchun (DEBUG=False, PostgreSQL)
    └── apps/             # Alohida domen ilovalari
        ├── common/       # Umumiy mixinlar, modellar, yordamchilar
        ├── news/         # Yangiliklar, kategoriyalar, teglar
        ├── comments/     # Izohlar tizimi
        └── accounts/     # Foydalanuvchilar va autentifikatsiya
```

### 4. Virtual muhit va kutubxonalarni o'rnatish

Nima uchun virtual muhit kerak?
Har bir Python loyihasi alohida izolyatsiyalangan muhitda ishlashi zarur, aks holda tizimdagi turli kutubxona versiyalari to'qnashadi.

**Terminal buyruqlari:**
```bash
# 1. Loyiha papkasini yaratish va unga o'tish
mkdir newsportal && cd newsportal

# 2. Virtual muhit yaratish
python3 -m venv venv

# 3. Virtual muhitni faollashtirish
# Linux / macOS:
source venv/bin/activate
# Windows (cmd/PowerShell):
# venv\Scripts\activate

# 4. Asosiy kutubxonalarni o'rnatish
pip install django djangorestframework python-dotenv psycopg2-binary

# 5. O'rnatilgan paketlarni qayd qilish
pip freeze > requirements.txt
```

### 5. .env fayli va xavfsizlik

Maxfiy kalitlarni (masalan, `SECRET_KEY`, baza parollari) to'g'ridan-to'g'ri `settings.py` fayliga yozish o'ta xavflidir! Ular GitHub-ga chiqib ketmasligi uchun `.env` faylida saqlanadi:

```bash
# .env fayli namunasi
SECRET_KEY=django-insecure-axv-newsportal-super-secret-key-2026
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

---

## Kod namunalari

### 1. `src/config/settings/base.py` (Asosiy konfiguratsiya)

```python
"""
Django REST Framework asosiy sozlamalari (base.py)
"""
from pathlib import Path
import os
from dotenv import load_dotenv

# src/ papkasiga yo'l
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# .env faylini yuklaymiz
load_dotenv(BASE_DIR.parent / ".env")

SECRET_KEY = os.getenv("SECRET_KEY", "default-fallback-key")
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

# Tizim ilovalari
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",  # Django REST Framework
]

LOCAL_APPS = [
    "apps.common",
    "apps.news",
    "apps.comments",
    "apps.accounts",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

WSGI_APPLICATION = "config.wsgi.application"

# Ma'lumotlar bazasi (Dastlabki ishlab chiqish uchun SQLite)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

LANGUAGE_CODE = "uz-uz"
TIME_ZONE = "Asia/Tashkent"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
```

### 2. Dastlabki `src/config/urls.py`

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
```

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq (Oson): Virtual muhitni tekshirish
Terminalda virtual muhit faollashtirilgach, `pip list` buyrug'i orqali `Django` va `djangorestframework` kutubxonalari o'rnatilganligini tekshiring. Kutubxonalar o'rnatilganligini ko'rsatuvchi konsol yozuvini keltiring.

**Yechim:**
```bash
(venv) $ pip list
Package             Version
------------------- -------
asgiref             3.8.1
Django              5.1.2
djangorestframework 3.15.2
pip                 24.2
psycopg2-binary     2.9.10
python-dotenv       1.0.1
sqlparse            0.5.1
```

### 2-topshiriq (O'rta): .env konfiguratsiyasini sozlash
Loyiha ildizida `.env.example` faylini yarating. Unda boshqa dasturchilar loyihani yuklab olganda qanday muhit o'zgaruvchilarini kiritishi kerakligi bo'yicha namunaviy shablon yozing.

**Yechim:**
```bash
# .env.example
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_NAME=newsportal_db
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres_password
DATABASE_HOST=127.0.0.1
DATABASE_PORT=5432
```

### 3-topshiriq (Qiyin): NewsPortal ER diagrammasi relyatsiyalarini tahlil qilish
Quyidagi 3 ta relyatsiya turining NewsPortal loyihasidagi o'rnini tushuntiring:
1. `Category` va `Post` o'rtasidagi bog'lanish turi va `on_delete=models.PROTECT` mantiqi;
2. `Tag` va `Post` o'rtasidagi bog'lanish turi;
3. `Comment` ning o'z-o'ziga bog'lanishi (`parent = models.ForeignKey('self', ...)`).

**Yechim:**
1. **Category va Post (One-to-Many):** Bitta kategoriyaga ko'plab postlar tegishli bo'lishi mumkin, ammo har bir post bitta asosiy kategoriyaga ega. `on_delete=models.PROTECT` — agar admin ichida 50 ta maqola bo'lgan kategoriyani tasodifan o'chirib yubormoqchi bo'lsa, baza xatolik beradi va postlar "egasi yo'q" holatga tushib qolishidan saqlaydi.
2. **Tag va Post (Many-to-Many):** Bitta postda bir nechta teg (masalan, "Python", "AI", "Ta'lim") bo'lishi mumkin va ayni shu teg boshqa ko'plab postlarda ham qayta ishlatiladi.
3. **Comment ning self-referential parent bog'lanishi:** Bu daraxtsimon (threaded comments) izohlar uchun kerak. Agar foydalanuvchi to'g'ridan-to'g'ri maqolaga izoh yozsa, `parent=None` bo'ladi. Agar boshqa bir foydalanuvchining izohiga javob qaytarsa, `parent` ushbu boshlang'ich izohning `id` sini ko'rsatadi.

---

## Tezkor nazorat savollari

1. Nima uchun Django loyihalarida har doim `venv` (virtual environment) dan foydalanish shart?
   - **Javob:** Turli loyihalarning kutubxona va versiyalari tizim darajasida to'qnashmasligi uchun.
2. `requirements.txt` faylining qanday amaliy vazifasi bor?
   - **Javob:** Loyiha ishga tushishi uchun kerak bo'lgan barcha kutubxonalar va ularning aniq versiyalarini saqlaydi (`pip install -r requirements.txt`).
3. Nima sababdan `SECRET_KEY` va baza parollarini to'g'ridan-to'g'ri kod ichiga yozish taqiqlanadi?
   - **Javob:** Agar kod GitHub yoki ochiq manbaga chiqsa, xakerlar tizimga to'liq egalik qilib olishi mumkin. Ular faqat `.env` da saqlanadi.
4. Django REST Framework-ni faollashtirish uchun `settings.py` dagi qaysi ro'yxatga nima qo'shiladi?
   - **Javob:** `INSTALLED_APPS` ro'yxatiga `'rest_framework'` qo'shiladi.
5. `ForeignKey` da `models.PROTECT` bilan `models.CASCADE` ning asosiy farqi nimada?
   - **Javob:** `CASCADE` asosiy obyekt o'chganda unga bog'liq barcha ma'lumotlarni ham o'chiradi; `PROTECT` esa bog'langan ma'lumotlar bor bo'lsa o'chirishni taqiqlaydi.

---

## Uyga vazifa

1. O'z kompyuteringizda `newsportal` loyihasini yarating, virtual muhit oching va `django` hamda `djangorestframework` paketlarini o'rnating.
2. `.env` faylini yaratib, `SECRET_KEY` va `DEBUG=True` o'zgaruvchilarini sozlang.
3. Loyiha papkasida `python manage.py migrate` va `python manage.py runserver` buyruqlarini berib, brauzerda `http://127.0.0.1:8000/` sahifasi ochilishini ta'minlang.
