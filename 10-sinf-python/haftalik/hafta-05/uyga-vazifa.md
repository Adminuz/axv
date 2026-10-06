# 5-hafta: Uyga vazifalar to'plami (Advanced Python Back-end)

Ushbu haftada o'tilgan darslar bo'yicha uyga vazifalar ro'yxati:

---

## 13-dars. Foydalanuvchilarni boshqarish: Identifikatsiya, autentifikatsiya va avtorizatsiya
1. `User` modeli, `UserCreate` va `UserRead` sxemalarini yozing va `alembic revision --autogenerate -m "users"` bilan migratsiya yarating.
2. `/auth/register`, `/auth/login` va `/auth/me` endpointlarini yozing; Swagger da Authorize bilan sinab, skrinshot oling.
3. `get_current_admin` dependency sini yozing va admin bo'lmagan foydalanuvchi uchun 403 qaytishini tekshiring.

---

## 14-dars. CRUD amallarni bajarish (model, forma, validatsiya)
1. `Book` modeli, `BookCreate`, `BookUpdate`, `BookRead` sxemalarini yozing va migratsiya yarating.
2. `POST`, `GET` (ro'yxat va bitta), `PATCH`, `DELETE` endpointlarini yozing; boshqa foydalanuvchi uchun 403 va yo'q id uchun 404 qaytishini tekshiring.
3. Swagger da barcha endpointlarni sinab skrinshot oling; `pages=-5` yuborib 422 javobini izohlang.

---

## 15-dars. Filtrlash, qidiruv va tartiblash
1. `GET /books` ga `author`, `min_pages` va `published_year` filtrlarini qo'shing; Swagger da 3 ta kombinatsiyani sinang.
2. `q` qidiruvini (sarlavha yoki muallif) va ruxsat etilgan `sort` ni qo'shing; noto'g'ri `sort` uchun 400 qaytishini tekshiring.
3. `limit`/`offset` va `BookPage` (items, total, limit, offset) ni qo'shing; 3 sahifani ketma-ket oling va natijani izohlang.

---

## Mentor uchun

### Baholash mezonlari (100 ballik tizim)

1. **Autentifikatsiya va JWT (35 ball):**
   - `User` modeli, bcrypt xeshlash va `/auth/register` (15 ball);
   - `/auth/login`, JWT va `get_current_user` (10 ball);
   - `/auth/me`, `get_current_admin` va 401/403 sinovi (10 ball).

2. **CRUD (35 ball):**
   - `Book` modeli va sxemalar, `Field` cheklovlari (10 ball);
   - POST, GET (ro'yxat, bitta), PATCH, DELETE ishlashi (15 ball);
   - 404 va 403 xatolari, Swagger skrinshotlari (10 ball).

3. **Filtrlash, qidiruv, tartiblash (30 ball):**
   - Filtrlar va `q` qidiruvi (10 ball);
   - Ruxsat etilgan `sort` va 400 xatosi (10 ball);
   - `limit`/`offset`, `total` va `BookPage` (10 ball).

### Kutiladigan namunaviy natijalar
- Bir xil email bilan ikkinchi `register` `409` qaytaradi.
- Yaroqsiz token bilan `/auth/me` `401`, admin bo'lmagan foydalanuvchi admin yo'lida `403` oladi.
- `pages=-5` bilan `POST /books` `422` qaytaradi; boshqa egasining kitobini `PATCH` qilish `403`.
- `GET /books?q=python&sort=-pages&limit=5&offset=0` javobida `items`, `total`, `limit`, `offset` bor.
