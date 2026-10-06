# 10-sinf (Advanced Python Back-end): 5-hafta baholash qaydnomasi

**Mavzular:**
13. Foydalanuvchilarni boshqarish: Identifikatsiya, autentifikatsiya va avtorizatsiya. Token, session va JWT
14. CRUD amallarni bajarish (model, forma, validatsiya)
15. Filtrlash, qidiruv va tartiblash

---

## Baholash mezonlari

| Mezon | Tavsif | Maks. ball |
|---|---|---|
| **Autentifikatsiya va JWT** | `User` modeli, bcrypt xeshlash, `/auth/register`, `/auth/login`, `get_current_user`, 401/403 | 35 ball |
| **CRUD** | `Book` modeli, Pydantic sxemalar, `Field` validatsiya, POST/GET/PATCH/DELETE, 404 va 403 | 35 ball |
| **Filtrlash, qidiruv, tartiblash** | `Query`, `where`, `ilike`, `or_`, `order_by`, `limit`/`offset`, `total` | 30 ball |
| **JAMI** | | **100 ball** |

---

## O'quvchilar natijalari jadvali

| № | O'quvchi F.I.Sh. | Autentifikatsiya (35) | CRUD (35) | Filtr va qidiruv (30) | Jami ball (100) | Izoh |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |
| 9 | | | | | | |
| 10 | | | | | | |
| 11 | | | | | | |
| 12 | | | | | | |

---

## Mentor qaydlari va tahlil

- **Mumkin qiyinchiliklar:** `await` ni unutish, `commit` yozmaslik, 401 va 403 ni aralashtirish, `response_model` siz parol xeshini qaytarish, `sort` ni tekshirmaslik.
- **Iqtidorli o'quvchilar uchun:** refresh token va `get_current_admin`; cursor pagination; `pg_trgm` bilan tez qidiruv.
- **Keyingi haftaga ko'prik:** 6-haftada fayllar bilan ishlash (`UploadFile`) va loyihani yakunlash: bugungi `Book`, `User` va `get_current_user` kerak bo'ladi.
- **Oraliq nazorat:** dasturda CRUD mavzusi oraliq nazorat bilan birga ko'rsatilgan; qaror mentorda.
