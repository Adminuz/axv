---
title: "1-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "10-sinf (Python)", "link": "/10-sinf-python/"}, "n": 1, "bob": "I-bob · Django REST freymvork", "lessons": [{"g": 1, "title": "Django REST Framework. Server side rendering va user side rendering tushunchalari", "lead": "Veb-dasturlashda frontend va backend o'rtasidagi aloqa qanday o'rnatiladi? Ushbu darsda biz serverda HTML tayyorlash (SSR) va brauzerda ma'lumotlarni dinamik chizish (CSR/USR) modellarini tahlil qilamiz hamda Django REST Framework dunyosiga ilk qadamni qo'yamiz.", "link": "/10-sinf-python/hafta-01/dars-1", "slide": "/slaydlar/10-sinf-python/hafta-01/dars-1.html"}, {"g": 2, "title": "DRF loyiha qurish: MBni loyihalash. Loyihani yaratish, dastlabki sozlamalar", "lead": "Yirik va jiddiy backend loyihalari mustahkam poydevordan boshlanadi. Ushbu darsda biz real NewsPortal (yangiliklar portali) loyihasi uchun ma'lumotlar bazasini loyihalashtiramiz, Python virtual muhitini sozlaymiz va xalqaro clean architecture standartlariga mos Django loyihasini noldan quramiz.", "link": "/10-sinf-python/hafta-01/dars-2", "slide": "/slaydlar/10-sinf-python/hafta-01/dars-2.html"}, {"g": 3, "title": "Model, View va Serializer. Routerlar", "lead": "Django REST Framework ning yuragi — bu Model, Serializer, View va Router komponentlarining o'zaro mukammal uyg'unligidir. Ushbu darsda biz NewsPortal tizimining to'liq ishlaydigan dastlabki REST API endpointlarini quramiz va N+1 muammosini hal etishni o'rganamiz.", "link": "/10-sinf-python/hafta-01/dars-3", "slide": "/slaydlar/10-sinf-python/hafta-01/dars-3.html"}]}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Ushbu haftada o'tilgan darslar bo'yicha uyga vazifalar ro'yxati:

---

### 1-dars. Django REST Framework. SSR va USR tushunchalari
1. Konspektdagi SSR va USR taqqoslash jadvalini daftaringizga ko'chirib, har bir mezonni o'z so'zlaringiz bilan izohlang.
2. Internetdagi o'zingiz yoqtirgan bitta veb-saytni tanlang (masalan, yangiliklar yoki ijtimoiy tarmoq), brauzerda `F12` (Dasturchi asboblari) tugmasini bosing, `Network` (Tarmoq) bo'limini oching va sahifa yuklanishida qanday `.html` va qanday `.json` so'rovlar o'tayotganini kuzating. Natijalarni daftarga 3-4 jumla bilan qayd eting.
3. Keyingi darsda o'rnatiladigan Django va DRF paketlari uchun kompyuteringizda Python versiyasini terminalda `python --version` orqali tekshirib qo'ying.

---

### 2-dars. DRF loyiha qurish: MBni loyihalash. Loyihani yaratish, dastlabki sozlamalar
1. Konspektdagi terminal buyruqlarini kompyuteringizda ketma-ket bajarib, `newsportal` loyihasini yarating.
2. `src/config/settings/base.py` faylini konspektdagi namuna asosida shakllantiring va `INSTALLED_APPS` ga `'rest_framework'` qo'shing.
3. Loyiha ildizida `.env` faylini yarating va unga `SECRET_KEY` kiriting.
4. Terminalda `python manage.py migrate` buyrug'ini bering va barcha dastlabki jadvallar bazaga yozilganligini tekshiring.

---

### 3-dars. Model, View va Serializer. Routerlar
1. Konspektdagi `CategorySerializer`, `TagSerializer` va `PostListSerializer` kodlarini o'z loyihangizda yozing.
2. `apps/news/views.py` da `CategoryViewSet` va `PostViewSet` ni yarating, ularni `DefaultRouter` orqali `config/urls.py` ga ulang.
3. Serverni ishga tushirib, brauzer orqali `http://127.0.0.1:8000/api/v1/posts/` manzilini oching va Browsable API yordamida kamida 2 ta kategoriya va 3 ta yangilik yarating.

---

</div>
