# 5-dars. Ruxsatlar bilan ishlash

## Dars rejasi (80 daqiqa)

1. **O'tgan darsni takrorlash (10 daqiqa):** Identifikatsiya, autentifikatsiya, JWT tokenlar (Access va Refresh), Custom User modeli bo'yicha savol-javob.
2. **Yangi mavzu: DRF Ruxsatlar (Permissions) tizimi (20 daqiqa):**
   - Permission nima va nima uchun u biznes mantiqning asosi?
   - Standart DRF ruxsatlari: `AllowAny`, `IsAuthenticated`, `IsAdminUser`, `IsAuthenticatedOrReadOnly`.
   - Global sozlamalar (`DEFAULT_PERMISSION_CLASSES`) va View-darajasidagi nazorat.
3. **Yangi mavzu: Custom Permission klasslar yaratish (25 daqiqa):**
   - `rest_framework.permissions.BasePermission` sinfi.
   - `has_permission(request, view)` &mdash; umumiy endpoint darajasida tekshirish (masalan: `IsStaffOrReadOnly`).
   - `has_object_permission(request, view, obj)` &mdash; aniq bitta obyekt darajasida tekshirish (masalan: `IsOwnerOrStaff`).
   - Xavfsiz HTTP metodlar (`SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')`).
4. **Amaliyot: ViewSetlarga ruxsatlarni ulash va perform_create (15 daqiqa):**
   - `CategoryViewSet` va `TagViewSet` ga `IsStaffOrReadOnly` ulash.
   - `PostViewSet` ga `IsOwnerOrStaff` ulash.
   - `perform_create(self, serializer)` orqali joriy foydalanuvchini avtomatik `author` qilib saqlash.
   - Brauzer va token bilan testlash (boshqa birovning maqolasini tahrirlashga 403 Forbidden olish).
5. **Dars xulosasi va tezkor nazorat (10 daqiqa):** Savol-javob, o'quvchilarni baholash, uyga vazifa.

---

## Mentor konspekti

### 1. Permission (Ruxsat) nima?

Autentifikatsiya foydalanuvchining **kimligini** aniqlaydi (`request.user`).
Permission esa uning **nimalarni o'zgartira olishini** hal qiladi.
Agar ruxsatlar tizimi bo'lmasa, istalgan ro'yxatdan o'tgan foydalanuvchi butun saytdagi boshqa odamlarning maqolalarini o'chirib yuborishi yoki tahrirlab qo'yishi mumkin!

### 2. Standart DRF ruxsat klasslari

DRF da eng ko'p ishlatiladigan tayyor klasslar:
1. `AllowAny` &mdash; Hammaga ruxsat beradi (mehmonlarga ham, tizimga kirganlarga ham). Odatda ommaviy yangiliklarni o'qish uchun ishlatiladi.
2. `IsAuthenticated` &mdash; Faqat tizimga kirgan (yaroqli token yoki sessiyaga ega) foydalanuvchilarga ruxsat beradi.
3. `IsAdminUser` &mdash; Faqat `is_staff=True` bo'lgan xodimlar va adminlarga ruxsat beradi.
4. `IsAuthenticatedOrReadOnly` &mdash; O'qish (GET, HEAD, OPTIONS) amallariga hammaga ruxsat beradi, ammo yangi qo'shish yoki o'zgartirish (POST, PUT, DELETE) uchun tizimga kirgan bo'lish shart.

### 3. Custom Permission yaratish metodikasi

Standart klasslar hamma biznes talablarni qoplay olmaydi. Masalan: "Maqolani hamma o'qiy olsin, lekin faqat uning muallifi yoki bosh admin tahrirlay olsin".
Buning uchun `BasePermission` dan voris olib, 2 ta metoddan birini (yoki ikkalasini) yozamiz:

1. **`has_permission(self, request, view)`:**
   - Butun ro'yxat yoki endpointga kirishdan oldin tekshiriladi.
   - Agar `False` qaytsa, so'rov darhol to'xtatiladi (`403 Forbidden`).

2. **`has_object_permission(self, request, view, obj)`:**
   - Muayyan bitta obyekt (masalan, 15-raqamli Post) ustida amal bajarilayotganda ishlaydi.
   - `obj` &mdash; aynan shu obyekt (Post yoki Comment).
   - Biz `obj.author == request.user` deb solishtiramiz.

### 4. `perform_create` orqali avtomatik muallif biriktirish

Frontend dasturchi yangi post yaratganda:
`POST /api/v1/posts/`
U JSON ichida `author: 5` deb yubormaydi (va yubormasligi kerak, chunki boshqa birovning ID sini yozib qo'yishi mumkin!).
Muallif server tomonida, tokendan olingan `request.user` orqali avtomatik biriktiriladi:

```python
def perform_create(self, serializer):
    serializer.save(author=self.request.user)
```

---

## Kod namunalari

### 1. `src/apps/common/permissions.py`

```python
from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsStaffOrReadOnly(BasePermission):
    """
    GET, HEAD, OPTIONS -> hammaga ruxsat.
    POST, PUT, PATCH, DELETE -> faqat xodim/adminlarga ruxsat.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)

class IsOwnerOrStaff(BasePermission):
    """
    Obyekt darajasidagi ruxsat:
    O'qish -> hammaga ruxsat.
    O'zgartirish/O'chirish -> faqat obyekt egasi (author/user) yoki staff.
    """
    owner_field = "author"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        user = request.user
        if not (user and user.is_authenticated):
            return False

        if user.is_staff:
            return True

        owner_field = getattr(view, "owner_field", self.owner_field)
        owner = getattr(obj, owner_field, None)
        return owner == user
```

### 2. ViewSetlarga ulash (`src/apps/news/views.py`)

```python
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.common.permissions import IsStaffOrReadOnly, IsOwnerOrStaff
from apps.news.models import Category, Post
from apps.news.serializers import CategorySerializer, PostListSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "slug"
    permission_classes = (IsStaffOrReadOnly,)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related("category", "author").all()
    lookup_field = "slug"
    owner_field = "author"
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrStaff)

    def perform_create(self, serializer):
        # Maqola muallifini joriy user qilib saqlaymiz
        serializer.save(author=self.request.user)
```

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq (Oson): SAFE_METHODS ro'yxati
DRF dagi `SAFE_METHODS` o'zgarmas korteji (tuple) qaysi HTTP metodlarini o'z ichiga oladi va nima uchun ular "xavfsiz" (safe) deb ataladi?

**Yechim:**
`SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')`
Ular serverdagi ma'lumotlar bazasini o'zgartirmaydi, faqat o'qish va server imkoniyatlarini tekshirish uchun xizmat qilgani sababli "xavfsiz" deb ataladi.

### 2-topshiriq (O'rta): Izohlar (Comment) uchun IsOwnerOrStaff moslashuvi
`CommentViewSet` da maqolaga yozilgan izohni faqat o'sha izohni yozgan foydalanuvchi (`comment.user`) yoki admin o'chira olishi uchun `owner_field` qanday sozlanishi kerak? Kod namunasini yozing.

**Yechim:**
```python
from apps.common.permissions import IsOwnerOrStaff
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related("post", "user").all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrStaff)
    owner_field = "user"  # Comment modelida muallif "user" maydonida saqlanadi

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
```

### 3-topshiriq (Qiyin): Faqat VIP foydalanuvchilar uchun Custom Permission
Loyiha talabi: Platformada yangi "Premium" yangiliklar bor. Ushbu yangiliklarni faqat `user.is_premium == True` bo'lgan foydalanuvchilar to'liq o'qiy oladi, boshqalarga esa `403 Forbidden` xabari chiqishi kerak. `HasPremiumAccess` nomli maxsus permission klassini yozing.

**Yechim:**
```python
from rest_framework.permissions import BasePermission

class HasPremiumAccess(BasePermission):
    message = "Ushbu kontent faqat Premium obunachilar uchun ochiq."

    def has_object_permission(self, request, view, obj):
        # Agar maqola oddiy bo'lsa, hammaga ruxsat
        if not getattr(obj, "is_premium", False):
            return True

        # Agar maqola premium bo'lsa, user login qilgan va premium bo'lishi shart
        user = request.user
        return bool(user and user.is_authenticated and getattr(user, "is_premium", False))
```

---

## Tezkor nazorat savollari

1. `has_permission` bilan `has_object_permission` ning asosiy farqi nimada?
   - **Javob:** `has_permission` butun so'rov darajasida (ro'yxatni ochishdan oldin) tekshiradi; `has_object_permission` esa aynan bitta aniq obyektga murojaat qilinganda ishlaydi.
2. Agar ruxsat berilmasa, DRF qanday HTTP status kodi qaytaradi?
   - **Javob:** `403 Forbidden` (agar tizimga kirmagan bo'lsa `401 Unauthorized`).
3. `IsAuthenticatedOrReadOnly` klassi ro'yxatdan o'tmagan mehmonlarga qaysi amallarga ruxsat beradi?
   - **Javob:** Faqat xavfsiz o'qish amallariga (GET, HEAD, OPTIONS).
4. Nima uchun maqola muallifini (`author`) frontenddan JSON orqali qabul qilish xavfsizlikka ziddir?
   - **Javob:** Foydalanuvchi boshqa odamning ID raqamini yuborib, uning nomidan yolg'on maqola chop etishi mumkin.
5. `perform_create` metodi ViewSet ichida qachon chaqiriladi?
   - **Javob:** Serializer ma'lumotlarni to'g'ri deb tasdiqlaganidan keyin (`is_valid()`), yangi obyekt bazaga saqlanish arafasida chaqiriladi.

---

## Uyga vazifa

1. `src/apps/common/permissions.py` faylini yarating va `IsStaffOrReadOnly` hamda `IsOwnerOrStaff` klasslarini yozing.
2. `CategoryViewSet` va `PostViewSet` ga ushbu permissionlarni bog'lang.
3. Postmanda ikkita turli foydalanuvchi hisobidan token oling va 1-foydalanuvchi yozgan postni 2-foydalanuvchi o'zgartira olmasligini (`403 Forbidden`) amalda tekshiring.
