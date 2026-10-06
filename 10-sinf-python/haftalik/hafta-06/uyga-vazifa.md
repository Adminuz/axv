# 6-hafta: Uyga vazifa

**Fan:** Advanced Python Back-end  
**Sinf:** 10-sinf  
**Hafta:** 6-hafta  
**Topshirish muddati:** Keyingi darsga qadar (7-hafta, 1-dars)

---

## Topshiriq 1: Fayllar (UploadFile) · qiyin

1. `POST /books/{id}/cover` ni yozing: JPEG/PNG, 2 MB, `uuid4` nomi; Swagger da sinab, skrinshot oling.
2. `GET /files/{name}` ni path traversal dan himoyalab yozing va `../` bilan so'rov yuborib 404 ni tekshiring.
3. TestClient bilan 3 ta test yozing: muvaffaqiyat (201), noto'g'ri tur (415), katta fayl (413).

---

## Topshiriq 2: Loyihani yakunlash · o'rta

1. `Settings` va `.env`/`.env.example` yarating; `.env` `.gitignore` da ekanini tekshiring.
2. Xato formatini (HTTPException va 422) bir xil qiling va 2 ta test yozing.
3. `alembic upgrade head` va `pytest -q` natijalarini skrinshot qiling; README ga ishga tushirish bo'limini qo'shing.

---

## Topshiriq 3: Docker deploy · oson

1. Book loyihasi uchun `Dockerfile` va `.dockerignore` yozing; `docker build` va `docker run` natijasini skrinshot qiling.
2. `docker-compose.yml` (api + db + volume) yozing; `docker compose up -d --build` va `/docs` ning skrinshotini oling.
3. `localhost` va `db` host farqini 3 jumlada tushuntiring.

---

## Baholash mezoni

| Mezon | Ball |
|---|---|
| 16-dars: Fayl yuklash va yuklab olish | 3 |
| 17-dars: Loyihani yakunlash | 3 |
| 18-dars: Dockerfile va docker-compose | 2 |
| Toza, o'z vaqtida va mustaqil bajarilgan | 2 |
| **Jami** | **10** |
| Bonus: bonus darajadagi topshiriq | +2 |

---

## Mentor uchun

**Tekshirish:**
- 16-dars: Faylning o'zi qayerda saqlanadi?? Javobi: Diskda yoki obyekt saqlashda; bazada faqat nomi.
- 17-dars: alembic upgrade head?? Javobi: Bazani oxirgi migratsiyaga ko'taradi.
- 18-dars: Volume nima uchun?? Javobi: Ma'lumot konteyner o'chganda yo'qolmasligi uchun.

**Keng tarqalgan xatolar:**
- 16-dars: file.filename ni to'g'ridan-to'g'ri yo'lga qo'shish.
- 17-dars: .env ni GitHub ga yuborish.
- 18-dars: DATABASE_URL da localhost yozish (compose da db kerak).
