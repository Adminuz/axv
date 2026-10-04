# 2-hafta: Uyga vazifalar to'plami (Advanced Python Back-end)

Ushbu haftada o'tilgan darslar bo'yicha uyga vazifalar ro'yxati:

---

## 4-dars. Foydalanuvchilarni boshqarish: Identifikatsiya, autentifikatsiya va avtorizatsiya. Token, session va JWT
1. Konspektdagi `User` va `UserManager` modellarini `src/apps/accounts/models.py` da yozing.
2. `settings/base.py` fayliga `AUTH_USER_MODEL = "accounts.User"` sozlamasini kiriting.
3. `rest_framework_simplejwt` paketini o'rnatib, `SIMPLE_JWT` sozlamalarini qo'shing.
4. Terminalda `makemigrations` va `migrate` qilib, `createsuperuser` orqali yangi admin hisobini oching.

---

## 5-dars. Ruxsatlar bilan ishlash
1. `src/apps/common/permissions.py` faylida `IsStaffOrReadOnly` va `IsOwnerOrStaff` klasslarini to'liq yozing.
2. `CategoryViewSet` va `TagViewSet` ga `permission_classes = (IsStaffOrReadOnly,)` sozlamasini ulang.
3. `PostViewSet` ga `permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrStaff)` ni qo'ying va `perform_create` metodini yozing.
4. Tizimda 2 ta foydalanuvchi ochib, 1-foydalanuvchining maqolasini 2-foydalanuvchi tahrirlay olmasligini (`403 Forbidden`) amalda sinab ko'ring.

---

## 6-dars. Filtrlash, qidiruv va tartiblash
1. `src/apps/news/filters.py` faylini konspektdagi namuna asosida shakllantiring.
2. `PostViewSet` ga `filterset_class`, `search_fields` va `ordering_fields` ni bog'lang.
3. Postman yoki brauzer orqali quyidagi so'rovlarni amalda sinab ko'ring va natijalar to'g'ri qaytayotganiga ishonch hosil qiling:
   - `GET /api/v1/posts/?status=published`
   - `GET /api/v1/posts/?search=texnologiya`
   - `GET /api/v1/posts/?ordering=-published_at`

---

## Mentor uchun

### Baholash mezonlari (100 ballik tizim)

1. **Xavfsizlik va Autentifikatsiya (35 ball):**
   - Custom User modeli (`AbstractBaseUser`, `UserManager`) to'g'ri loyihalashtirilgani (15 ball);
   - JWT tokenlar (Access va Refresh) mexanizmining to'g'ri sozlanganligi va tushunilishi (10 ball);
   - Postman yoki HTTP mijozda `Bearer <token>` bilan so'rov yubora olishi (10 ball).

2. **Ruxsatlar va IDOR himoyasi (35 ball):**
   - `IsStaffOrReadOnly` va `IsOwnerOrStaff` ruxsat klasslarining to'g'ri ishlashi (15 ball);
   - `perform_create` orqali muallif avtomatik biriktirilgani (10 ball);
   - Boshqa foydalanuvchi ma'lumotlarini o'zgartirishda `403 Forbidden` himoyasi tekshirilgani (10 ball).

3. **Filtrlash, Qidiruv va Tartiblash (30 ball):**
   - `django-filter` va `PostFilter` ning to'g'ri sozlanganligi (15 ball);
   - `search_fields` va `ordering_fields` orqali URL da turli xil query-parametrlarni muvaffaqiyatli sinashi (15 ball).

### Kutiladigan namunaviy natijalar
- Tizimda `http://127.0.0.1:8000/api/v1/posts/?search=...` so'rovi to'g'ri qidiruv natijalarini qaytarishi kerak;
- Tizimga kirmasdan `POST /api/v1/posts/` qilganda `401 Unauthorized`, boshqa birovning maqolasiga `PUT` qilganda `403 Forbidden` qaytishi shart.
