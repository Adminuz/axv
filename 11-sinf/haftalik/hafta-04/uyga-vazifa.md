# 4-hafta. Uyga vazifalar

Har bir vazifa 20–30 daqiqa. Parol, shaxsiy token, maxfiy kalit va shaxsiy ma'lumotlarni repozitoriyga yozmang: topshirishda faqat ochiq GitHub repo yoki Pull Request havolasi kerak.

## 10-dars uchun (Observer va EventBus)
**1-topshiriq: «Kutubxona EventBus tizimi»**
1. O'z GitHub portfolio repozitoriyangizda `feature/observer-eventbus` tarmog'ini oching.
2. `library_events.py` faylida markaziy `EventBus` sinfini e'lon qiling (`subscribe`, `unsubscribe`, `publish`).
3. `book:borrowed` hodisasi uchun ikkita kuzatuvchi yarating:
   - `AuditLogger` &mdash; berilgan kitob va o'quvchi ma'lumotlarini `logs/library.log` fayliga qo'shadi;
   - `StudentNotifier` &mdash; qaytarish muddatini hisoblab terminalga xabar chiqaradi.
4. `test_events.py` faylida `unittest.mock.MagicMock` yordamida `publish` chaqirilganda barcha kuzatuvchilar ishga tushishini tekshiruvchi 2 ta unit test yozing.
5. Semantik commitlar bilan GitHub'ga yuboring.

**Kutiladigan natija:** bo'sh bog'langan, OCP talablariga mos, testlangan EventBus kodi.  
**Topshirish:** GitHub commit yoki fayl havolasi.

---

## 11-dars uchun (REST tamoyillari va HTTP metodlari)
**2-topshiriq: «REST API URI loyihasi va curl sinovlari»**
1. `docs/api_design.md` faylida «Kutubxona boshqaruvi» tizimi uchun RESTful endpointlar jadvalini tuzing:
   - Kitoblarni olish (`GET /api/v1/books`), yangi kitob qo'shish (`POST`), ID bo'yicha olish (`GET /api/v1/books/{id}`), o'chirish (`DELETE`);
   - Ko'plik otlar, ierarxiya va to'g'ri HTTP metodlari qo'llansin.
2. Har bir amal uchun qaytishi kerak bo'lgan kutilayotgan HTTP status kodlarini (200, 201, 204, 400, 404) yozing.
3. `test_api.sh` nomli skript fayl tuzib, unga ushbu endpointlarni sinovdan o'tkazuvchi kamida 4 ta `curl` buyrug'ini yozing (`-X`, `-H "Content-Type: application/json"`, `-d`, `-v` bayroqlari bilan).

**Kutiladigan natija:** to'g'ri loyihalangan RESTful URI hujjati va terminalda ishlovchi curl sinov skripti.  
**Topshirish:** `docs/api_design.md` va `test_api.sh` havolasi.

---

## 12-dars uchun (JSON formati, Kontrakt va Xavfsizlik)
**3-topshiriq: «JSON Kontrakt, Error Envelope va DTO xavfsizligi»**
1. `contracts.py` faylida quyidagi qoidalarga mos keluvchi JSON serializatsiya funksiyalarini yozing:
   - Yagona xatolik formati (`Error Envelope`): `{"error": {"code": "...", "message": "...", "details": [...]}}` qaytaruvchi `make_error_response()` funksiyasi;
   - Paginatsiya javobini shakllantiruvchi `make_paginated_response(data, limit, offset, total)` funksiyasi (`data` va `meta` bo'limlari bilan);
   - Xavfsiz DTO filtri: Foydalanuvchi obyektidan `password_hash`, `token`, `secret_key` maydonlarini olib tashlab, sanalarni ISO-8601 UTC formatiga o'tkazuvchi `sanitize_user()` funksiyasi.
2. `test_contracts.py` faylida har uchala funksiyani `pytest` yoki `assert` bilan tekshiruvchi testlar yozing.
3. Barcha ishlarni `main` tarmog'iga Pull Request qilib yuboring.

**Kutiladigan natija:** xalqaro standartlarga mos, xavfsiz JSON kontrakt moduli va yashil unit testlar.  
**Topshirish:** GitHub Pull Request havolasi.

---

## Mentor uchun
Dars boshida 10-dars bo'yicha kuzatuvchilardan biri xato bersa boshqalari to'xtab qolmasligi tekshirilganini ko'ring (`try/except` mavjudligi). 11-darsda URI ichida fe'llar (`/getBooks`, `/delete_book`) ishlatilmaganiga, resurslar ko'plikda nomlanganiga ishonch hosil qiling. 12-darsda `sanitize_user` funksiyasida `password_hash` mijozga chiqib ketmasligi va xato javoblarida yagona `error` kaliti ishlatilganini tahlil qiling.
