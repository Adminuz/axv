# 8-dars. Statik fayllar bilan ishlash. Fayllarni yuklash va koʻchirib olish

## Dars rejasi (80 daqiqa)

1. **O'tgan darsni takrorlash (10 daqiqa):** Pagination (sahifalash), `PageNumberPagination`, Throttling va `429 Too Many Requests` status kodi bo'yicha savol-javob.
2. **Yangi mavzu: Statik va Media fayllar farqi (20 daqiqa):**
   - Statik fayllar nima? (Dasturchi yozgan CSS, JS, admin panel uslublari). `STATIC_URL`, `STATIC_ROOT` va `collectstatic`.
   - Media fayllar nima? (Foydalanuvchilar yuklagan dinamik fayllar: muqova rasmi, avatar, PDF). `MEDIA_URL` va `MEDIA_ROOT`.
   - `.gitignore` qoidasi: nega yuklangan fayllar va to'plangan statika Git-ga kiritilmaydi?
   - `DEBUG=True` paytida media fayllarni `urls.py` orqali serve qilish.
3. **Yangi mavzu: DRF da Multipart fayl yuklash (Upload) (25 daqiqa):**
   - JSON formati nega katta ikkilik (binary) fayllarni uzatishga to'g'ri kelmaydi?
   - `multipart/form-data` kontent turi.
   - DRF parserlari: `MultiPartParser` va `FormParser`.
   - `PostCoverUploadSerializer` va rasm hajmini (maksimal 5 MB) hamda formatini (JPEG, PNG, WEBP) tekshiruvchi validatsiya.
   - `@action(detail=True, methods=["post"], url_path="upload-cover")` orqali alohida upload endpoint yaratish.
4. **Yangi mavzu: Fayllarni ko'chirib olish (Download) (15 daqiqa):**
   - Django `FileResponse` sinfi va uning oqimli (streaming) ishlash xususiyati.
   - `as_attachment=True` parametri orqali brauzerda yuklab olishni majburlash.
   - Muqovani yuklab olish actioni: `GET /api/v1/posts/{slug}/download-cover/`.
5. **Dars xulosasi va tezkor nazorat (10 daqiqa):** Savol-javob, o'quvchilarni baholash, uyga vazifa.

---

## Mentor konspekti

### 1. Statik va Media fayllarning tub farqi

| Xususiyat | Statik fayllar (Static) | Media fayllar (Media / Upload) |
|---|---|---|
| **Kim yaratadi?** | Dasturchi (kod yozish jarayonida) | Foydalanuvchilar (sayt ishlash jarayonida) |
| **Fayl turlari** | `style.css`, `app.js`, logo, piktogrammalar | Maqola rasmlari, foydalanuvchi avatari, PDF kitoblar |
| **Qayerda saqlanadi?** | Loyiha ichidagi `static/` papkalarida | Serverning `media/` papkasida (bazada faqat yo'li saqlanadi) |
| **Deployda nima qilinadi?** | `collectstatic` orqali bitta papkaga yig'ilib, Nginx orqali uzatiladi | S3 bulutli xotirasida yoki Nginx alohida papkasida saqlanadi |

### 2. Sozlamalar: STATIC va MEDIA

`src/config/settings/base.py` faylida:
```python
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR.parent / "staticfiles"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR.parent / "media"
```

**Development muhitda serve qilish:**
Klassik Django-da `DEBUG=True` bo'lganda statik fayllar avtomatik ochiladi, lekin media fayllarni `urls.py` ga qo'shish shart:
```python
# src/config/urls.py
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 3. DRF da Fayl yuklash (Upload) arxitekturasi

Oddiy JSON so'rovlarida rasm yuborib bo'lmaydi. Buning uchun mijoz `Content-Type: multipart/form-data` yuboradi.
DRF ViewSet da ushbu ma'lumotni o'qish uchun `parser_classes` ko'rsatilishi shart:
- `MultiPartParser` &mdash; fayl obyektlarini (`request.FILES`) o'qish uchun;
- `FormParser` &mdash; shakl matnli maydonlarini o'qish uchun.

**Alohida endpoint afzalligi:**
Maqola yaratish (`POST /posts/`) bilan uning rasmini yuklashni (`POST /posts/{slug}/upload-cover/`) alohida endpointga ajratish clean architecture tamoyili hisoblanadi. Bu tarmoq xatolarida xatolikni oson aniqlash va rasmni alohida qayta yuklash imkonini beradi.

### 4. Faylni ko'chirib olish (FileResponse)

Faylni to'g'ridan-to'g'ri `http://site.uz/media/covers/photo.jpg` deb ochish mumkin, ammo:
1. Agar bu fayl faqat pullik obunachilar uchun bo'lsa-chi?
2. Agar brauzerda ochilmasdan, majburiy kompyuterga yuklab olinishi (`as_attachment=True`) kerak bo'lsa-chi?

Buning uchun biz `FileResponse` dan foydalanamiz:
```python
from django.http import FileResponse, Http404

@action(methods=["get"], detail=True, url_path="download-cover")
def download_cover(self, request, slug=None):
    post = self.get_object()
    if not post.cover_image:
        raise Http404("Muqova rasmi topilmadi")
    return FileResponse(
        post.cover_image.open("rb"),
        as_attachment=True,
        filename=post.cover_image.name.split("/")[-1]
    )
```

---

## Kod namunalari

### 1. Serializer va Validatsiya (`src/apps/news/serializers.py`)

```python
from rest_framework import serializers
from apps.news.models import Post

class PostCoverUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("cover_image",)

    def validate_cover_image(self, file):
        # 1. MIME formatini tekshirish
        allowed_types = ("image/jpeg", "image/png", "image/webp")
        if file.content_type not in allowed_types:
            raise serializers.ValidationError("Faqat JPEG, PNG yoki WEBP formatdagi rasmlar ruxsat etiladi.")

        # 2. Fayl hajmini tekshirish (maksimal 5 MB)
        max_size = 5 * 1024 * 1024  # 5 MB
        if file.size > max_size:
            raise serializers.ValidationError("Rasm hajmi 5 MB dan oshmasligi kerak.")

        return file
```

### 2. ViewSet Actionlari (`src/apps/news/views.py`)

```python
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.http import FileResponse, Http404
from apps.news.serializers import PostCoverUploadSerializer

class PostViewSet(viewsets.ModelViewSet):
    # ... avvalgi sozlamalar

    @action(
        methods=["post"],
        detail=True,
        url_path="upload-cover",
        parser_classes=[MultiPartParser, FormParser],
    )
    def upload_cover(self, request, slug=None):
        post = self.get_object()
        serializer = PostCoverUploadSerializer(post, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=["get"], detail=True, url_path="download-cover")
    def download_cover(self, request, slug=None):
        post = self.get_object()
        if not post.cover_image:
            raise Http404("Rasm mavjud emas")
        return FileResponse(
            post.cover_image.open("rb"),
            as_attachment=True,
            filename=post.cover_image.name.split("/")[-1]
        )
```

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq (Oson): STATIC va MEDIA sozlamalarini ajratish
Quyidagi sozlamalarning qaysi biri dasturchi yozgan CSS/JS uchun, qaysi biri foydalanuvchi yuklagan rasmlar uchun ekanligini belgilang:
`STATIC_ROOT`, `MEDIA_ROOT`, `STATIC_URL`, `MEDIA_URL`.

**Yechim:**
- `STATIC_URL` va `STATIC_ROOT` &mdash; dasturchining statik fayllari (CSS, JS, ikonlar) uchun.
- `MEDIA_URL` va `MEDIA_ROOT` &mdash; foydalanuvchilar tomonidan yuklangan dinamik fayllar (avarlar, muqovalar) uchun.

### 2-topshiriq (O'rta): Fayl hajmini tekshiruvchi validatsiya
O'quvchilar onlayn kitoblar tizimida PDF fayllarni qabul qilmoqda.
Faylning formati `application/pdf` bo'lishini va hajmi ko'pi bilan 20 MB bo'lishini tekshiruvchi `validate_file` metodini yozing.

**Yechim:**
```python
def validate_file(self, file):
    if file.content_type != "application/pdf":
        raise serializers.ValidationError("Faqat PDF formatdagi kitoblar qabul qilinadi.")
    if file.size > 20 * 1024 * 1024:
        raise serializers.ValidationError("Fayl hajmi 20 MB dan oshmasligi kerak.")
    return file
```

### 3-topshiriq (Qiyin): curl orqali fayl yuklash
Foydalanuvchi kompyuteridagi `C:\covers\django.jpg` rasmini `news-ai` nomli postga yuklash uchun `curl` buyrug'ini qanday formatda yozishi kerak? (Autentifikatsiya tokeni bilan birga).

**Yechim:**
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/posts/news-ai/upload-cover/" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -F "cover_image=@C:\covers\django.jpg"
```

---

## Tezkor nazorat savollari

1. Statik va Media fayllarning asosiy farqi nimada?
   - **Javob:** Statik fayllarni dasturchi kod bilan birga yozadi; Media fayllarni esa foydalanuvchilar sayt ishlash davomida yuklaydi.
2. Nima sababdan `media/` va `staticfiles/` papkalari `.gitignore` ga qo'shilishi shart?
   - **Javob:** Git faqat kodni saqlashi kerak; yuzlab megabaytli rasmlar va yig'ilgan statik fayllar omborni behuda og'irlashtiradi.
3. Oddiy JSON o'rniga fayl yuklashda qaysi kontent turi (`Content-Type`) ishlatiladi?
   - **Javob:** `multipart/form-data`.
4. DRF ViewSet da rasmni o'qiy olish uchun qaysi parser klassi zarur?
   - **Javob:** `MultiPartParser` (va `FormParser`).
5. `FileResponse` dagi `as_attachment=True` parametri nima vazifani bajaradi?
   - **Javob:** Faylni brauzer oynasida ochib yubormasdan, kompyuterga yuklab olish oynasini (Download) chiqarishni majburlaydi.

---

## Uyga vazifa

1. `src/config/settings/base.py` fayliga `STATIC_ROOT`, `STATIC_URL`, `MEDIA_ROOT` va `MEDIA_URL` sozlamalarini kiriting.
2. `src/apps/news/serializers.py` faylida `PostCoverUploadSerializer` klassini yozing (5 MB va MIME tekshiruvi bilan).
3. `PostViewSet` ichiga `upload_cover` va `download_cover` actionlarini qo'shing va Postman orqali rasm yuklab, yuklab olishni sinab ko'ring.
