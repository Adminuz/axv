---
title: "3-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "10-sinf (Python)", "link": "/10-sinf-python/"}, "n": 3, "bob": "", "lessons": [{"g": 7, "title": "Pagination va throttling", "lead": "Millionlab foydalanuvchilar bir vaqtda kirganda serveringiz bardosh bera oladimi? Ushbu darsda biz katta ma'lumotlarni sahifalab uzatish (Pagination) va tizimni ortiqcha yuklama hamda bot hujumlaridan himoyalash (Throttling / Rate limiting) texnologiyalarini o'rganamiz.", "link": "/10-sinf-python/hafta-03/dars-1", "slide": "/slaydlar/10-sinf-python/hafta-03/dars-1.html"}, {"g": 8, "title": "Statik fayllar bilan ishlash. Fayllarni yuklash va koʻchirib olish", "lead": "Har qanday zamonaviy yangiliklar portali jozibali muqova rasmlari, foydalanuvchilarning fotosuratlari va yuklab olinuvchi hujjatlarsiz to'liq bo'lmaydi. Ushbu darsda biz Django loyihasida statik va media fayllarni to'g'ri tashkil etishni, multipart fayllarni qabul qilish va xavfsiz yuklab olish endpointlarini quramiz.", "link": "/10-sinf-python/hafta-03/dars-2", "slide": "/slaydlar/10-sinf-python/hafta-03/dars-2.html"}, {"g": 9, "title": "APIni testlash. APIni hujjatlashtirish. (Swagger, Redoc)", "lead": "Haqiqiy professional dasturchi kodni nafaqat yozadi, balki uning mukammal ishlashini avtomatlashtirilgan testlar bilan isbotlaydi va hamkasblari uchun tushunarli interaktiv hujjat (Swagger) taqdim etadi. Ushbu darsda biz 1-bobning yakuniy cho'qqisiga chiqamiz!", "link": "/10-sinf-python/hafta-03/dars-3", "slide": "/slaydlar/10-sinf-python/hafta-03/dars-3.html"}]}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Ushbu haftada o'tilgan darslar bo'yicha uyga vazifalar ro'yxati:

---

### 7-dars. Pagination va throttling
1. `src/apps/common/pagination.py` da `DefaultPageNumberPagination` klassini yarating va `settings/base.py` ga global pagination sozlamasini qo'shing.
2. `settings/base.py` faylida `DEFAULT_THROTTLE_CLASSES` va `DEFAULT_THROTTLE_RATES` ni sozlang (`anon: 60/min`, `user: 300/min`).
3. Brauzerda `http://127.0.0.1:8000/api/v1/posts/?page=1` manzilini oching va JSON javobida pagination tuzilishi to'g'ri chiqqanligini tekshiring.

---

### 8-dars. Statik fayllar bilan ishlash. Fayllarni yuklash va koʻchirib olish
1. Kompyuteringizda `pip install pillow` buyrug'ini bering va `Post` modelida `cover_image` maydoni borligiga ishonch hosil qiling.
2. `src/apps/news/serializers.py` faylida `PostCoverUploadSerializer` klassini yozing.
3. `PostViewSet` da `upload_cover` va `download_cover` actionlarini yozib, Postman orqali kompyuterdan rasm yuklash va uni yuklab olishni sinovdan o'tkazing.

---

### 9-dars. APIni testlash. APIni hujjatlashtirish. (Swagger, Redoc)
1. `src/apps/news/tests/test_posts_api.py` faylini konspektdagi namuna asosida to'ldiring va terminalda `python manage.py test` qiling.
2. `drf-spectacular` kutubxonasini o'rnatib, `urls.py` ga `/api/docs/` va `/api/redoc/` yo'llarini ulang.
3. Brauzerda `http://127.0.0.1:8000/api/docs/` manzilini oching va Swagger interfeysidagi "Try it out" orqali yangiliklar ro'yxatini olib, natijani kuzating.

---

</div>
