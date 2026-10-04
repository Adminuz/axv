# 1-hafta: Uyga vazifalar to'plami (Advanced Python Back-end)

Ushbu haftada o'tilgan darslar bo'yicha uyga vazifalar ro'yxati:

---

## 1-dars. Django REST Framework. SSR va USR tushunchalari
1. Konspektdagi SSR va USR taqqoslash jadvalini daftaringizga ko'chirib, har bir mezonni o'z so'zlaringiz bilan izohlang.
2. Internetdagi o'zingiz yoqtirgan bitta veb-saytni tanlang (masalan, yangiliklar yoki ijtimoiy tarmoq), brauzerda `F12` (Dasturchi asboblari) tugmasini bosing, `Network` (Tarmoq) bo'limini oching va sahifa yuklanishida qanday `.html` va qanday `.json` so'rovlar o'tayotganini kuzating. Natijalarni daftarga 3-4 jumla bilan qayd eting.
3. Keyingi darsda o'rnatiladigan Django va DRF paketlari uchun kompyuteringizda Python versiyasini terminalda `python --version` orqali tekshirib qo'ying.

---

## 2-dars. DRF loyiha qurish: MBni loyihalash. Loyihani yaratish, dastlabki sozlamalar
1. Konspektdagi terminal buyruqlarini kompyuteringizda ketma-ket bajarib, `newsportal` loyihasini yarating.
2. `src/config/settings/base.py` faylini konspektdagi namuna asosida shakllantiring va `INSTALLED_APPS` ga `'rest_framework'` qo'shing.
3. Loyiha ildizida `.env` faylini yarating va unga `SECRET_KEY` kiriting.
4. Terminalda `python manage.py migrate` buyrug'ini bering va barcha dastlabki jadvallar bazaga yozilganligini tekshiring.

---

## 3-dars. Model, View va Serializer. Routerlar
1. Konspektdagi `CategorySerializer`, `TagSerializer` va `PostListSerializer` kodlarini o'z loyihangizda yozing.
2. `apps/news/views.py` da `CategoryViewSet` va `PostViewSet` ni yarating, ularni `DefaultRouter` orqali `config/urls.py` ga ulang.
3. Serverni ishga tushirib, brauzer orqali `http://127.0.0.1:8000/api/v1/posts/` manzilini oching va Browsable API yordamida kamida 2 ta kategoriya va 3 ta yangilik yarating.

---

## Mentor uchun

### Baholash mezonlari (100 ballik tizim)

1. **Nazariy tushunchalar va arxitektura (30 ball):**
   - SSR va USR/CSR farqlarini to'g'ri tushuntira olishi (10 ball);
   - REST tamoyillari va HTTP metodlari (GET, POST, PUT, DELETE) mosligini bilishi (10 ball);
   - ERD diagrammasidagi munosabatlar (1-N, N-N, PROTECT/CASCADE) mohiyatini anglaganligi (10 ball).

2. **Loyiha muhiti va sozlamalar (30 ball):**
   - Virtual muhit (`venv`) to'g'ri yaratilgani va faollashtirilgani (10 ball);
   - Kutubxonalar `requirements.txt` da to'g'ri qayd etilganligi (10 ball);
   - `.env` faylida maxfiy o'zgaruvchilar sozlangani va `.gitignore` ga kiritilganligi (10 ball).

3. **Amaliy kod va API ishlashi (40 ball):**
   - Modellar (`TimeStampedModel`, `Category`, `Tag`, `Post`) to'g'ri yozilgani va migratsiya o'tgani (15 ball);
   - Serializerlar (`CategorySerializer`, `PostListSerializer`, `PostWriteSerializer`) to'g'ri ajratilgani (15 ball);
   - `DefaultRouter` orqali endpointlar ochilgani va Browsable API da yangilik qo'shilgani (10 ball).

### Kutiladigan namunaviy natijalar
- O'quvchi terminalida `python manage.py runserver` xatosiz ishga tushishi kerak;
- `http://127.0.0.1:8000/api/v1/posts/` manzilida JSON ro'yxati va pastda yangi post kiritish formasi (Browsable API) ko'rinishi shart.
