# 4-hafta: Baholash shabloni (mentor uchun)

**Fan:** BI (Ma'lumotlar muhandisligi va ML)  
**Sinf:** 10-sinf  
**Hafta:** 4-hafta  
**Darslar:** 10, 11, 12 (global); 1, 2, 3 (hafta ichida)

---

## O'quvchilar ro'yxati

| O'quvchi ismi | D-10 | D-11 | D-12 | Uyga vazifa | Jami | Izoh |
|---|:---:|:---:|:---:|:---:|:---:|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

---

## Dars baholari (har bir dars uchun: 0–5 ball)

### Dars-10 (GROUP BY, HAVING)

| Mezon | Maks | Izoh |
|---|:---:|---|
| Darsda ishtirok (savollarga javob) | 1 | |
| Agregat funksiyalar va `GROUP BY` so'rovlari | 2 | |
| `WHERE` va `HAVING` farqini tushunish | 1 | |
| Xatoni topish / dublikat tekshiruvi | 1 | |
| **Jami** | **5** | |

### Dars-11 (JOIN turlari)

| Mezon | Maks | Izoh |
|---|:---:|---|
| Darsda ishtirok | 1 | |
| `INNER` / `LEFT JOIN` so'rovlari to'g'riligi | 2 | |
| Anti-join (`IS NULL`) va `ON` / `WHERE` farqi | 1 | |
| 3 jadval yoki `JOIN + GROUP BY` | 1 | |
| **Jami** | **5** | |

### Dars-12 (Subquery, CTE, CASE WHEN)

| Mezon | Maks | Izoh |
|---|:---:|---|
| Darsda ishtirok | 1 | |
| Subquery to'g'ri yozilgan | 1 | |
| CTE ishlatilgan (o'qiladigan struktura) | 1 | |
| `CASE WHEN` (toifa yoki pivot) | 1 | |
| Tezkor nazorat javoblari | 1 | |
| **Jami** | **5** | |

---

## Uyga vazifa baholari (0–10 ball)

| Mezon | Maks |
|---|:---:|
| Topshiriq 1: GROUP BY / HAVING | 3 |
| Topshiriq 2: JOIN, COALESCE, anti-join | 3 |
| Topshiriq 3: CTE + CASE WHEN | 3 |
| Kod izohlangan, natija tartibli | 1 |
| **Jami** | **10** |
| Bonus: o'z savol + izoh.txt | +2 |

---

## 4-hafta yakun bahosi

Formulasi: `(D-10 + D-11 + D-12) / 3 + uyga_vazifa / 2`

**Maksimal jami ball:** `5 + 5 = 10`; ya'ni dars o'rtachasi (5) + uyga vazifa / 2 (5) (+ 1 bonus).

Haftalik test (`hafta-test`) natijalari joriy nazorat (40 ball) hisobiga mentor ixtiyori bilan qo'shilishi mumkin.

---

## Dars kuzatishlari (mentor uchun bo'sh joy)

**10-dars (GROUP BY / HAVING):**
> ...

**11-dars (JOIN):**
> ...

**12-dars (Subquery / CTE / CASE WHEN):**
> ...

---

## Keng tarqalgan xatolar: 4-hafta

- `WHERE` ichida agregat funksiya (10-dars)
- `GROUP BY` da bo'lmagan ustunni `SELECT` ga yozish (10-dars)
- `ON` ni unutib Cartesian product hosil qilish (11-dars)
- `LEFT JOIN` da o'ng jadval shartini `WHERE` ga qo'yish (11-dars)
- `COUNT(*)` va `COUNT(ustun)` ni aralashtirish (10–11-dars)
- `CASE` ni `END` bilan yopmaslik, shartlar tartibi noto'g'ri (12-dars)
- Integer bo'linma: `* 1.0` unutish (10–12-dars)
