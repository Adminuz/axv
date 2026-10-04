# 6-dars. Filtrlash, qidiruv va tartiblash

## Dars rejasi (80 daqiqa)

1. **O'tgan darsni takrorlash (10 daqiqa):** DRF Permissions tizimi, `IsOwnerOrStaff`, `perform_create` va xavfsizlik qoidalari bo'yicha tezkor savol-javob.
2. **Yangi mavzu: Filtrlash, qidiruv va tartiblash zarurati (20 daqiqa):**
   - Muammo: Ma'lumotlar bazasida 100 000 ta maqola bo'lsa, ularni saralash va qidirish qanday tashkil etiladi?
   - Uch vosita: Filtrlash (Filtering), Matnli qidiruv (Search) va Tartiblash (Ordering).
   - Global konfiguratsiya: `django-filter` o'rnatish va `settings/base.py` da `DEFAULT_FILTER_BACKENDS`.
3. **Yangi mavzu: PostFilter va sana oraliqlari (25 daqiqa):**
   - `apps/news/filters.py`: `django_filters.FilterSet` sinfi.
   - Aniq qiymat bo'yicha: `status`, `category`, `author`, `tags`.
   - Sana oraliqlari: `IsoDateTimeFilter` bilan `lookup_expr="gte"` va `lookup_expr="lte"` (`published_from`, `published_to`).
   - `search_fields` (Sarlavha va matn bo'yicha to'liq qidiruv) va `ordering_fields` (Sana, sarlavha bo'yicha saralash).
4. **Amaliyot: Endpointlarni qidiruv va filtrlar bilan sinash (15 daqiqa):**
   - `PostViewSet` va `CommentViewSet` ga filtrlarni ulash.
   - URL parametrlar orqali murakkab so'rovlar yuborish: `?status=published&category=2&search=python&ordering=-published_at`.
   - Browsable API da avtomatik "Filters" tugmasi hosil bo'lishini ko'rish.
5. **Dars xulosasi va tezkor nazorat (10 daqiqa):** Savol-javob, o'quvchilarni baholash, 2-hafta umumiy xulosasi va uyga vazifa.

---

## Mentor konspekti

### 1. Filtrlash, Qidiruv va Tartiblash: Farqlar

- **Filtrlash (Filtering):** Muayyan aniq shartlarga mos ma'lumotlarni saralab olish. Masalan: faqat "Texnologiya" kategoriyasidagi, faqat "e'lon qilingan" (`status='published'`) maqolalar.
- **Qidiruv (Search):** Foydalanuvchi kiritgan matnni bir nechta maydonlar ichidan (sarlavha, qisqacha mazmun, asosiy matn) qidirish. Masalan: `?search=sun'iy intellekt`.
- **Tartiblash (Ordering):** Natijalarni ma'lum bir ustun bo'yicha o'sish yoki kamayish tartibida joylashtirish. Masalan: eng yangilari tepada (`?ordering=-published_at`).

### 2. `django-filter` kutubxonasi va sozlamalar

DRF da qulay va keng qamrovli filtrlash uchun `django-filter` kutubxonasi o'rnatiladi:
```bash
pip install django-filter
pip freeze > requirements.txt
```

`src/config/settings/base.py` fayliga ulanadi:
```python
INSTALLED_APPS += ["django_filters"]

REST_FRAMEWORK = {
    # ... avvalgi sozlamalar
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ),
}
```

### 3. Custom FilterSet: `apps/news/filters.py`

Django-filter imkoniyatlari juda keng. Oddiy maydonlardan tashqari sanalar oralig'ini qidirish uchun `IsoDateTimeFilter` qo'llaymiz:
- `lookup_expr="gte"` &mdash; "Greater Than or Equal" (katta yoki teng, berilgan sanadan keyingi);
- `lookup_expr="lte"` &mdash; "Less Than or Equal" (kichik yoki teng, berilgan sanagacha bo'lgan).

### 4. SearchFilter simvollari

DRF `SearchFilter` da maydonlar oldiga maxsus belgilar qo'yish orqali qidiruv turini o'zgartirish mumkin:
- `'^title'` &mdash; Sarlavha berilgan so'z bilan boshlansa (Starts-with);
- `'=status'` &mdash; Aniq teng bo'lsa (Exact match);
- `'@body'` &mdash; To'liq matnli qidiruv (Full-text search, PostgreSQL uchun);
- `'title'` (belgisiz) &mdash; Ichida shu so'z qatnashgan bo'lsa (Case-insensitive contains / `icontains`).

---

## Kod namunalari

### 1. `src/apps/news/filters.py`

```python
import django_filters
from apps.news.models import Post

class PostFilter(django_filters.FilterSet):
    """
    Post filterlari:
    - status
    - category (id)
    - author (id)
    - tags (id) -> tags=1&tags=2
    - published_at oralig'i: published_from, published_to
    """
    published_from = django_filters.IsoDateTimeFilter(
        field_name="published_at", lookup_expr="gte"
    )
    published_to = django_filters.IsoDateTimeFilter(
        field_name="published_at", lookup_expr="lte"
    )

    class Meta:
        model = Post
        fields = {
            "status": ["exact"],
            "category": ["exact"],
            "author": ["exact"],
            "tags": ["exact"],
        }
```

### 2. ViewSetga filtrlarni ulash (`src/apps/news/views.py`)

```python
from apps.news.filters import PostFilter

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related("category", "author").prefetch_related("tags").all()
    lookup_field = "slug"

    # Maxsus filter klassi
    filterset_class = PostFilter

    # Qidiruv maydonlari
    search_fields = ("title", "excerpt", "body")

    # Saralash maydonlari
    ordering_fields = ("published_at", "created_at", "title", "status")
    ordering = ("-published_at", "-created_at")  # Standart tartib
```

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq (Oson): URL parametrlarini tahlil qilish
Quyidagi so'rov qanday maqolalarni qaytarishini tahlil qiling:
`GET /api/v1/posts/?status=published&category=3&ordering=-published_at`

**Yechim:**
Ushbu so'rov:
1. Faqat e'lon qilingan (`status='published'`);
2. 3-raqamli kategoriyaga tegishli bo'lgan;
3. E'lon qilingan vaqti bo'yicha eng yangilaridan boshlab kamayish tartibida saralangan (`ordering=-published_at`) maqolalar ro'yxatini qaytaradi.

### 2-topshiriq (O'rta): Izohlar (Comment) filtri
`apps/comments/filters.py` faylida `CommentFilter` klassini yozing. Unda:
- Aniq post bo'yicha (`post`);
- Moderatsiyadan o'tganligi bo'yicha (`is_approved`);
- Yaratilgan vaqti bo'yicha `created_from` (sanadan keyin) filtrlash bo'lsin.

**Yechim:**
```python
import django_filters
from apps.comments.models import Comment

class CommentFilter(django_filters.FilterSet):
    created_from = django_filters.IsoDateTimeFilter(
        field_name="created_at", lookup_expr="gte"
    )

    class Meta:
        model = Comment
        fields = {
            "post": ["exact"],
            "is_approved": ["exact"],
        }
```

### 3-topshiriq (Qiyin): Narx oralig'i bo'yicha filtrlash
Onlayn do'kon API tizimida `Product` modeli mavjud bo'lib, uning `price` (narx) maydoni bor.
Foydalanuvchi `GET /api/v1/products/?min_price=10000&max_price=50000` deb so'rov yuborganda narx oralig'ini to'g'ri filtrlovchi `ProductFilter(django_filters.FilterSet)` klassini yozing.

**Yechim:**
```python
import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = Product
        fields = ["category", "in_stock"]
```

---

## Tezkor nazorat savollari

1. `filterset_class` bilan `search_fields` ning asosiy farqi nimada?
   - **Javob:** `filterset_class` aniq maydonlar (kategoriya, holat, sana) bo'yicha qat'iy tekshiradi; `search_fields` esa matn ichidan kalit so'zlarni qidiradi.
2. `ordering` da maydon oldidagi minus (`-`) belgisi nimani anglatadi?
   - **Javob:** Kamayish (descending) tartibida saralashni (masalan: `-created_at` eng yangilarni birinchi chiqaradi).
3. `django-filter` da `lookup_expr="gte"` nimani bildiradi?
   - **Javob:** "Greater Than or Equal" &mdash; kiritilgan qiymatdan katta yoki teng bo'lgan yozuvlarni tanlashni.
4. Qidiruv so'rovi URL da qaysi standart parametr orqali yuboriladi?
   - **Javob:** `?search=so'z` parametri orqali.
5. Nima sababdan filtrlash frontendda emas, aynan backend ma'lumotlar bazasida bajarilishi kerak?
   - **Javob:** Agar millionta ma'lumot bo'lsa, ularning barchasini frontendga yuklab olib keyin saralash internet trafigi va kompyuter xotirasini to'ldirib tashlaydi. Baza buni bir zumda optimallashtirib beradi.

---

## Uyga vazifa

1. `pip install django-filter` qilib, `src/config/settings/base.py` ga `django_filters` ni ulang.
2. `src/apps/news/filters.py` faylini yarating va `PostFilter` klassini yozing.
3. `PostViewSet` ga `filterset_class`, `search_fields` va `ordering_fields` ni qo'shing.
4. Brauzer orqali `http://127.0.0.1:8000/api/v1/posts/` ni ochib, "Filters" tugmasi orqali kategoriya va qidiruv bo'yicha amaliy sinov o'tkazing.
