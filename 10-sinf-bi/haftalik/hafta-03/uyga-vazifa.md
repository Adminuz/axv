# 3-hafta: Uyga vazifa

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Hafta:** 3-hafta  
**Topshirish muddati:** Keyingi darsga qadar (4-hafta, 1-dars)

---

## Topshiriq 1: Ma'lumotlar bazasini boyitish · o'rta

`maktab.db` bazasiga `hududlar` jadvalida kamida 5 ta viloyat qayd etilgan bo'lishi kerak. `yillik_kpi` jadvaliga shu 5 ta viloyat uchun **2022, 2023 va 2024** yillar bo'yicha quyidagi ustunlar bilan ma'lumotlar kiriting:

- `hudud_id` — viloyat identifikatori
- `yil` — yil
- `oquvchilar_soni` — talabalar soni (maqsadga muvofiq raqamlar, masalan, 300 000 — 900 000 oralig'ida)
- `maktablar_soni` — maktablar soni (masalan, 500 — 2000 oralig'ida)
- `oquvchilar_soni / maktablar_soni` ni hisoblash uchun ikkala ustun ham to'ldirilishi shart

**Eslatma:** `INSERT INTO` SQL buyrug'i yordamida. Qiymatlarni o'ylab topmasdan, o'zingiz yashayotgan yoki o'qiyotgan viloyatlar statistikasini taxminiy kiriting.

---

## Topshiriq 2: Maktab yuklamasi tahlili · qiyin

Python skripti (`uyga_vazifa.py`) yozing. Skript quyidagilarni bajarsin:

1. `maktab.db` ga ulaning, `PRAGMA foreign_keys = ON` qo'ying.
2. **SQL 1 — Barcha hududlar uchun o'rtacha yuklama:** Har bir hudud uchun 2022–2024 yillar bo'yicha o'rtacha bitta maktabga to'g'ri keladigan o'quvchilar sonini hisoblang.
   - `ROUND(... / ..., 1)` va `AS` taxallusidan foydalaning.
   - Natijani hudud nomi bilan chiqaring (JOIN bilan).
3. **SQL 2 — Yuklamasi 700 dan oshgan hududlar:** 2-so'rovda faqat 2024-yilgi yuklamasi 700 nafardan oshgan hududlarni `WHERE` orqali filtrlang.
4. **SQL 3 — TOP-3 hudud:** Yuqori yuklamalidan pastiga `ORDER BY ... DESC` saralang va `LIMIT 3` bilan faqat eng yuqori 3 ta hududni chiqaring.
5. Har uchala so'rov natijasini `print` bilan konsolga tartibli — chiroyli jadval ko'rinishida — chiqaring.

```python
# Kutilayotgan natija ko'rinishi:
# ============================================
# TOP-3: Maktab yuklamasi (2024-yil)
# ============================================
# Hudud                    Yuklama (o'quvchi/maktab)
# ----------------------------------------
# Toshkent viloyati              842.3
# Samarqand viloyati             791.0
# Qashqadaryo viloyati           735.8
```

---

## Topshiriq 3: Mustaqil tadqiqot · bonus

Internetdan O'zbekistonning haqiqiy ta'lim statistikasini toping (stat.uz yoki xalqaro ma'lumotlar). Kamida 3 ta viloyat uchun haqiqiy ma'lumotlarni `maktab.db` ga kiriting va SQL tahlil natijalari bilan taqqoslang. Taqqoslash natijasini qisqa (5–7 jumladan iborat) matn ko'rinishida `izoh.txt` faylida yozing.

---

## Baholash mezoni

| Mezon | Ball |
|---|---|
| Topshiriq 1 (ma'lumotlar kiritilgan, 3 yil × 5 hudud) | 3 |
| Topshiriq 2 (SQL 1: o'rtacha yuklama bilan JOIN) | 2 |
| Topshiriq 2 (SQL 2: WHERE filtri to'g'ri ishlaydi) | 2 |
| Topshiriq 2 (SQL 3: TOP-3 ORDER BY + LIMIT) | 2 |
| Kod izohlangan, `print` natijasi tartibli | 1 |
| **Jami** | **10** |
| Bonus (haqiqiy statistika + izoh.txt) | +2 |

---

## Mentor uchun

**Tekshirish bo'yicha eslatmalar:**

- `maktab.db` ga `SELECT COUNT(*) FROM yillik_kpi` orqali 15+ yozuv borligini tekshiring.
- `uyga_vazifa.py` ni ishga tushiring: `python uyga_vazifa.py` — xatosiz ishlashi kerak.
- SQL 2 da `WHERE maktab_yuklamasi > 700` alias ni WHERE ichida ishlatgan bo'lsa, bu noto'g'ri (ijro tartibi xatosi). To'g'ri yo'l: `WHERE ROUND(oquvchilar_soni * 1.0 / maktablar_soni, 1) > 700` yoki `HAVING` + `GROUP BY` qo'llanilishi kerak.
- Bonus topshiriq stat.uz yoki UNESCO ma'lumotlaridan olinganligini tekshiring.

**Keng tarqalgan xatolar:**
1. `= NULL` o'rniga `IS NULL` yozmaslik
2. `ORDERBY` yaxlit yozish (bo'sh joy yo'q)
3. LIMIT dan oldin `ORDER BY` qo'ymaslik
4. SQLite da integer bo'linmasi (`5 / 2 = 2`), `* 1.0` yoki `CAST AS REAL` esdan chiqarish
