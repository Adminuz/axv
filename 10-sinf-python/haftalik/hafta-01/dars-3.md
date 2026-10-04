# 3-dars. Model, View va Serializer. Routerlar

## Dars rejasi (80 daqiqa)

1. **O'tgan mavzuni takrorlash (10 daqiqa):** NewsPortal ERD sxemasi, virtual muhit, Clean Architecture sozlamalari bo'yicha qisqa so'rov.
2. **Yangi mavzu: Django ORM va Modellar (20 daqiqa):**
   - `apps/common/models.py`: `TimeStampedModel` abstrakt modeli (`created_at`, `updated_at`).
   - `apps/news/models.py`: `Category`, `Tag`, `PostStatus`, `Post` (slug auto-to'ldirish, indexes).
   - `apps/comments/models.py`: `Comment` (daraxtsimon `parent` bog'lanish).
   - Migratsiyalarni amalga oshirish: `makemigrations` va `migrate`.
3. **Yangi mavzu: Serializers va ViewSets (25 daqiqa):**
   - Serializer vazifasi: Serialization va Deserialization.
   - Read va Write uchun serializerlarni ajratish: `PostListSerializer`, `PostDetailSerializer`, `PostWriteSerializer`.
   - N+1 muammosi va uni yechish: `select_related` va `prefetch_related`.
   - `ModelViewSet` va unda `get_serializer_class()` orqali mos serializer tanlash.
4. **Yangi mavzu: Routerlar va URL endpointlar (15 daqiqa):**
   - `rest_framework.routers.DefaultRouter` qulayliklari.
   - Endpointlarni `config/urls.py` ga ulash.
   - Browsable API orqali test qilish (`/api/v1/posts/`, `/api/v1/categories/`).
5. **Dars xulosasi va tezkor nazorat (10 daqiqa):** Savol-javob, o'quvchilarni baholash, 1-hafta umumiy xulosasi va uyga vazifa.

---

## Mentor konspekti

### 1. Django ORM: Modellar va Abstrakt modellar

Katta loyihalarda har bir modelda `created_at` (yaratilgan vaqt) va `updated_at` (yangilangan vaqt) maydonlari kerak bo'ladi. Har safar ularni qayta yozmaslik uchun `apps/common/models.py` ichida abstrakt model yaratamiz:

```python
# src/apps/common/models.py
from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Bazada alohida jadval ochilmaydi, faqat meros beradi
```

### 2. NewsPortal modellari

- **Category va Tag:** `name` va `slug` maydonlariga ega. `save()` metodi ichida agar `slug` kiritilmagan bo'lsa, `slugify(self.name)` orqali avtomatik to'ldiriladi.
- **Post (Maqola):**
  - `status`: `PostStatus.choices` (`draft`, `published`, `archived`);
  - `category`: `models.ForeignKey(Category, on_delete=models.PROTECT, related_name="posts")`;
  - `tags`: `models.ManyToManyField(Tag, blank=True, related_name="posts")`;
  - `indexes`: Tezkor qidiruv uchun `slug` va `['status', 'published_at']` bo'yicha indekslar qo'yiladi.

### 3. Serializer nima va nima uchun u muhim?

Serializer — bu Django ORM QuerySet obyektlari va JSON formatdagi ma'lumotlar o'rtasidagi "tarjimon" va "filtr"dir.
U ikkita asosiy vazifani bajaradi:
1. **Serialization (Serializatsiya):** Python/Django obyektini JSON-ga o'giradi (mijozga yuborish uchun).
2. **Deserialization & Validation (Qabul qilish va tekshirish):** Mijozdan kelgan JSON ma'lumotlarini qabul qilib, ularning to'g'riligini tekshiradi (validatsiya qiladi) va Django modeliga saqlaydi.

**Read va Write uchun serializerlarni ajratish:**
- O'qish (Read/GET) paytida mijozga chiroyli va to'liq ma'lumot kerak: kategoriya nomi, teglarning to'liq ro'yxati (nested serializer).
- Yozish (Write/POST/PUT) paytida esa mijozdan ortiqcha narsa emas, faqat kategoriya ID raqami kerak (`category: 2`). Shuning uchun `PostWriteSerializer` alohida yoziladi.

### 4. N+1 muammosi (Query Optimization)

Agar biz 100 ta postni chiqarsak va har bir postning kategoriyasi nomini so'rasak:
- Dastlab 1 ta so'rov: hamma postlarni oladi.
- Keyin har bir post uchun alohida 1 tadan so'rov kategoriya jadvaliga yuboriladi (jami 1 + 100 = 101 ta so'rov!).
Bu **N+1 muammosi** deyiladi va serverni juda sekinlashtiradi.

**Yechim:**
- `select_related('category')` &mdash; SQL `JOIN` orqali ForeignKey ma'lumotlarini 1 ta so'rovda qo'shib oladi.
- `prefetch_related('tags')` &mdash; ManyToMany munosabatlarini alohida bitta optimallashtirilgan so'rov bilan birlashtiradi.

### 5. Routerlar (DefaultRouter)

DRF da har bir URL ni qo'lda alohida yozib o'tirish shart emas:
`router.register(r'posts', PostViewSet, basename='post')`
Bu bitta qator kod orqali quyidagi barcha standart REST yo'nalishlari avtomatik ochiladi:
- `GET /posts/` &rarr; `list`
- `POST /posts/` &rarr; `create`
- `GET /posts/{slug}/` &rarr; `retrieve`
- `PUT /posts/{slug}/` &rarr; `update`
- `PATCH /posts/{slug}/` &rarr; `partial_update`
- `DELETE /posts/{slug}/` &rarr; `destroy`

---

## Kod namunalari

### 1. `src/apps/news/serializers.py`

```python
from rest_framework import serializers
from apps.news.models import Category, Post, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "slug", "created_at")

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name", "slug", "created_at")

class PostListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            "id", "title", "slug", "excerpt", "status",
            "published_at", "category", "tags", "created_at",
        )

class PostDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            "id", "title", "slug", "excerpt", "body",
            "cover_image", "status", "published_at",
            "category", "tags", "created_at", "updated_at",
        )

class PostWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "title", "slug", "excerpt", "body",
            "cover_image", "status", "published_at",
            "category", "tags",
        )
```

### 2. `src/apps/news/views.py`

```python
from rest_framework import viewsets
from apps.news.models import Category, Post, Tag
from apps.news.serializers import (
    CategorySerializer, TagSerializer,
    PostListSerializer, PostDetailSerializer, PostWriteSerializer
)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "slug"

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "slug"

class PostViewSet(viewsets.ModelViewSet):
    # N+1 muammosini oldini olish
    queryset = Post.objects.select_related("category").prefetch_related("tags").all()
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update"):
            return PostWriteSerializer
        if self.action == "retrieve":
            return PostDetailSerializer
        return PostListSerializer
```

### 3. `src/apps/news/urls.py` va `src/config/urls.py`

```python
# src/apps/news/urls.py
from rest_framework.routers import DefaultRouter
from apps.news.views import CategoryViewSet, PostViewSet, TagViewSet

router = DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"tags", TagViewSet, basename="tag")
router.register(r"posts", PostViewSet, basename="post")

urlpatterns = router.urls
```

```python
# src/config/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("apps.news.urls")),
]
```

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq (Oson): ModelSerializer yaratish
`Tag` modeli uchun `TagSerializer` klassini yozing. Unda `id`, `name`, `slug` maydonlari bo'lsin.

**Yechim:**
```python
from rest_framework import serializers
from apps.news.models import Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name", "slug")
```

### 2-topshiriq (O'rta): N+1 muammosini tuzatish
Quyidagi xato ViewSet kodini tahlil qiling va undagi N+1 muammosini bartaraf etish uchun `queryset` qatorini to'g'rilang:
```python
# Xato kod:
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all() # Har bir maqola uchun muallif va bo'lim alohida so'raladi!
```

**Yechim:**
```python
class ArticleViewSet(viewsets.ModelViewSet):
    # select_related ForeignKey bog'lanishlarini bitta SQL JOIN bilan olib keladi
    queryset = Article.objects.select_related("author", "category").prefetch_related("tags").all()
```

### 3-topshiriq (Qiyin): Izohlar (Comment) ViewSet filtri
`apps/comments/views.py` modulida `CommentViewSet` yarating. Unda faqat ma'lum bir maqolaning izohlarini olish uchun `GET /api/v1/comments/?post=3` so'rovi bo'yicha filtrlash mantiqini yozing.

**Yechim:**
```python
from rest_framework import viewsets
from apps.comments.models import Comment
from apps.comments.serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.select_related("post", "parent").all()
        post_id = self.request.query_params.get("post")
        if post_id:
            queryset = queryset.filter(post_id=post_id)
        return queryset
```

---

## Tezkor nazorat savollari

1. `TimeStampedModel` da `abstract = True` nima maqsadda yoziladi?
   - **Javob:** Bazada uning o'zi uchun alohida jadval ochilmasligi, faqat boshqa modellarga meros bo'lib xizmat qilishi uchun.
2. Serializerning asosiy 2 ta vazifasi nimadan iborat?
   - **Javob:** Python obyektlarini JSON-ga o'girish (serialization) va kelgan JSON-ni tekshirib modelga saqlash (deserialization).
3. Nima sababdan `PostListSerializer` va `PostWriteSerializer` alohida qilib yoziladi?
   - **Javob:** O'qishda kategoriya va teglarning to'liq ma'lumoti kerak, yozishda esa faqat ularning ID raqamlari qabul qilinishi yetarli.
4. `select_related` bilan `prefetch_related` qaysi bog'lanish turlarida ishlatiladi?
   - **Javob:** `select_related` — One-to-One va One-to-Many (ForeignKey) uchun; `prefetch_related` — Many-to-Many va teskari munosabatlar uchun.
5. `DefaultRouter` orqali bitta `PostViewSet` ro'yxatdan o'tkazilganda qanday HTTP amallar avtomatik paydo bo'ladi?
   - **Javob:** GET (list, retrieve), POST (create), PUT (update), PATCH (partial_update), DELETE (destroy).

---

## Uyga vazifa

1. `src/apps/news/models.py` da `Category`, `Tag` va `Post` modellarini yozib, `makemigrations` va `migrate` qiling.
2. `src/apps/news/serializers.py` va `src/apps/news/views.py` fayllarini konspektdagi namuna bo'yicha to'ldiring.
3. Brauzerda `http://127.0.0.1:8000/api/v1/posts/` manzilini oching va Browsable API orqali dastlabki test kategoriyasi va maqolasini yarating.
