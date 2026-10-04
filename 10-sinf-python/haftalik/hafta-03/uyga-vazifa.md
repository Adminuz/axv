# 3-hafta: Uyga vazifalar to'plami (Advanced Python Back-end)

Ushbu haftada o'tilgan darslar bo'yicha uyga vazifalar ro'yxati:

---

## 7-dars. Pagination va throttling
1. `src/apps/common/pagination.py` da `DefaultPageNumberPagination` klassini yarating va `settings/base.py` ga global pagination sozlamasini qo'shing.
2. `settings/base.py` faylida `DEFAULT_THROTTLE_CLASSES` va `DEFAULT_THROTTLE_RATES` ni sozlang (`anon: 60/min`, `user: 300/min`).
3. Brauzerda `http://127.0.0.1:8000/api/v1/posts/?page=1` manzilini oching va JSON javobida pagination tuzilishi to'g'ri chiqqanligini tekshiring.

---

## 8-dars. Statik fayllar bilan ishlash. Fayllarni yuklash va koʻchirib olish
1. Kompyuteringizda `pip install pillow` buyrug'ini bering va `Post` modelida `cover_image` maydoni borligiga ishonch hosil qiling.
2. `src/apps/news/serializers.py` faylida `PostCoverUploadSerializer` klassini yozing.
3. `PostViewSet` da `upload_cover` va `download_cover` actionlarini yozib, Postman orqali kompyuterdan rasm yuklash va uni yuklab olishni sinovdan o'tkazing.

---

## 9-dars. APIni testlash. APIni hujjatlashtirish. (Swagger, Redoc)
1. `src/apps/news/tests/test_posts_api.py` faylini konspektdagi namuna asosida to'ldiring va terminalda `python manage.py test` qiling.
2. `drf-spectacular` kutubxonasini o'rnatib, `urls.py` ga `/api/docs/` va `/api/redoc/` yo'llarini ulang.
3. Brauzerda `http://127.0.0.1:8000/api/docs/` manzilini oching va Swagger interfeysidagi "Try it out" orqali yangiliklar ro'yxatini olib, natijani kuzating.

---

## Mentor uchun

### Baholash mezonlari (100 ballik tizim)

1. **Unumdorlik va Himoya (Pagination & Throttling) (30 ball):**
   - `DefaultPageNumberPagination` to'g'ri sozlanganligi va `max_page_size` chegarasi (15 ball);
   - Throttling (Anon va User limitlari) to'g'ri ishlayotgani va `429` xatosi sinovi (15 ball).

2. **Fayllar bilan ishlash (Upload & Download) (35 ball):**
   - `STATIC_ROOT` va `MEDIA_ROOT` sozlamalari, `.gitignore` ga kiritilganligi (10 ball);
   - `MultiPartParser` orqali rasm yuklash va uning formati hamda hajmi tekshirilishi (15 ball);
   - `FileResponse` yordamida `download_cover` xavfsiz yuklab olish actioni (10 ball).

3. **Testlash va Hujjatlashtirish (Swagger) (35 ball):**
   - `APITestCase` orqali asosiy endpointlar (CRUD, Auth, Permissions) avtomatik sinovdan o'tgani (`OK`) (20 ball);
   - `drf-spectacular` orqali `/api/docs/` va `/api/redoc/` sahifalari xatosiz ochilishi (15 ball).

### Kutiladigan namunaviy natijalar
- Terminalda `python manage.py test` buyrug'i barcha testlarni yashil (`OK`) ko'rsatishi kerak;
- Brauzerda `http://127.0.0.1:8000/api/docs/` manzilida to'liq va interaktiv Swagger UI hujjati ochilishi shart.
