---
title: "2-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "10-sinf (Python)", "link": "/10-sinf-python/"}, "n": 2, "bob": "I-bob · Django REST freymvork", "lessons": [{"g": 4, "title": "Foydalanuvchilarni boshqarish: Identifikatsiya, autentifikatsiya va avtorizatsiya. Token, session va JWT", "lead": "Foydalanuvchilarni tanish va himoya qilish — har qanday backend tizimning eng muhim ustunidir. Ushbu darsda biz login, parol, sessiya va zamonaviy JSON Web Token (JWT) mexanizmlari bilan tanishamiz hamda NewsPortal uchun Custom User modelini quramiz.", "link": "/10-sinf-python/hafta-02/dars-1", "slide": "/slaydlar/10-sinf-python/hafta-02/dars-1.html", "test": "/slaydlar/10-sinf-python/hafta-02/dars-1-test.html"}, {"g": 5, "title": "Ruxsatlar bilan ishlash", "lead": "Tizimga kirish yetarli emas — har bir foydalanuvchining o'z chegarasi va vakolati bo'lishi shart! Ushbu darsda biz Django REST Framework ning ruxsatlar (Permissions) mexanizmi bilan tanishamiz va o'z maqolasini faqat uning muallifigina tahrirlay oladigan xavfsiz tizim quramiz.", "link": "/10-sinf-python/hafta-02/dars-2", "slide": "/slaydlar/10-sinf-python/hafta-02/dars-2.html", "test": "/slaydlar/10-sinf-python/hafta-02/dars-2-test.html"}, {"g": 6, "title": "Filtrlash, qidiruv va tartiblash", "lead": "Yuz minglab ma'lumotlar ichidan foydalanuvchiga aynan kerakli bitta yangilikni 10 millisoniyada topib berish — haqiqiy backend ustasining mahoratidir! Ushbu darsda biz django-filter kutubxonasini o'rganamiz, to'liq matnli qidiruv va moslashuvchan saralash tizimini NewsPortal ga ulaymiz.", "link": "/10-sinf-python/hafta-02/dars-3", "slide": "/slaydlar/10-sinf-python/hafta-02/dars-3.html", "test": "/slaydlar/10-sinf-python/hafta-02/dars-3-test.html"}], "test": "/slaydlar/10-sinf-python/hafta-02/hafta-test.html"}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Ushbu haftada o'tilgan darslar bo'yicha uyga vazifalar ro'yxati:

---

### 4-dars. Foydalanuvchilarni boshqarish: Identifikatsiya, autentifikatsiya va avtorizatsiya. Token, session va JWT
1. Konspektdagi `User` va `UserManager` modellarini `src/apps/accounts/models.py` da yozing.
2. `settings/base.py` fayliga `AUTH_USER_MODEL = "accounts.User"` sozlamasini kiriting.
3. `rest_framework_simplejwt` paketini o'rnatib, `SIMPLE_JWT` sozlamalarini qo'shing.
4. Terminalda `makemigrations` va `migrate` qilib, `createsuperuser` orqali yangi admin hisobini oching.

---

### 5-dars. Ruxsatlar bilan ishlash
1. `src/apps/common/permissions.py` faylida `IsStaffOrReadOnly` va `IsOwnerOrStaff` klasslarini to'liq yozing.
2. `CategoryViewSet` va `TagViewSet` ga `permission_classes = (IsStaffOrReadOnly,)` sozlamasini ulang.
3. `PostViewSet` ga `permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrStaff)` ni qo'ying va `perform_create` metodini yozing.
4. Tizimda 2 ta foydalanuvchi ochib, 1-foydalanuvchining maqolasini 2-foydalanuvchi tahrirlay olmasligini (`403 Forbidden`) amalda sinab ko'ring.

---

### 6-dars. Filtrlash, qidiruv va tartiblash
1. `src/apps/news/filters.py` faylini konspektdagi namuna asosida shakllantiring.
2. `PostViewSet` ga `filterset_class`, `search_fields` va `ordering_fields` ni bog'lang.
3. Postman yoki brauzer orqali quyidagi so'rovlarni amalda sinab ko'ring va natijalar to'g'ri qaytayotganiga ishonch hosil qiling:
   - `GET /api/v1/posts/?status=published`
   - `GET /api/v1/posts/?search=texnologiya`
   - `GET /api/v1/posts/?ordering=-published_at`

---

</div>
