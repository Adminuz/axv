# 12-dars: Subquery, CTE (WITH) va CASE WHEN operatorlari

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Hafta:** 4-hafta, 3-dars (umumiy 12-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

Murakkab tahliliy so'rovlarni **bosqichlarga bo'lib** yozishni o'rgatish: ichki so'rovlar (**Subquery**), nomlangan vaqtinchalik natija (**CTE, `WITH`**) va shartli ustun (**`CASE WHEN`**). Rasmiy dastur "Subquery (ichki so'rovlar) orqali qo'shma tahlil, CTE (WITH) yaratish, CASE WHEN bilan shartli ustun" ni talab qiladi; uslubiy ko'rsatmada `WITH t AS (...) SELECT ... LAG(...)` (yillik o'sish, YoY) misoli va `CASE WHEN` orqali pivot/KPI hisoblash tilga olingan.

---

## Kutilayotgan natijalar

- Subquery turlarini (skalyar, ro'yxat `IN`, `FROM` dagi) ajratadi va to'g'ri joyda yozadi;
- `WITH nom AS (...)` bilan CTE yozib, so'rovni o'qiladigan qismlarga bo'ladi;
- Bir nechta CTE ni vergul bilan ketma-ket yoza oladi;
- `CASE WHEN ... THEN ... ELSE ... END` bilan toifa (kategoriya) ustuni yaratadi;
- `SUM(CASE WHEN ...)` bilan pivot (yillar ustunlarga) va shartli sanash bajaradi;
- Yillik o'sishni (YoY) CTE + `LAG` bilan hisoblashni tushunadi (uslubiy ko'rsatmadagi misol).

---

## Kerakli jihozlar

- Python 3.10+ (`sqlite3`, oyna funksiyasi `LAG` uchun SQLite 3.25+);
- `data/maktab.db` (10-darsdagi ma'lumot bilan).

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10** | Takrorlash | `GROUP BY`, `HAVING`, `JOIN`; tezkor savollar |
| **10–28** | Subquery | Skalyar, `IN` / `NOT IN`, `FROM` dagi ichki so'rov |
| **28–40** | CTE (`WITH`) | Sintaksis, bir nechta CTE, YoY misoli |
| **40–45** | Tanaffus | |
| **45–58** | `CASE WHEN` | Toifalash, pivot, shartli sanash |
| **58–75** | Amaliyot | 3 darajali topshiriqlar, mini-hisobot |
| **75–80** | Xulosa | Tezkor nazorat, hafta yakuni, uyga vazifa |

---

## Nazariy qism (konspekt)

### 1. Subquery (ichki so'rov)

**Subquery** — boshqa so'rov ichiga qavs bilan yozilgan `SELECT`. Avval ichki so'rov bajariladi, uning natijasi tashqi so'rovda ishlatiladi. Savol: "o'rtachadan katta hududlar qaysi?" — avval o'rtachani bilish kerak.

**a) Skalyar subquery** (bitta qiymat qaytaradi):

```sql
SELECT hudud_id, oquvchilar_soni
FROM yillik_kpi
WHERE yil = 2024
  AND oquvchilar_soni > (SELECT AVG(oquvchilar_soni) FROM yillik_kpi WHERE yil = 2024);
-- hudud 2, 3, 4
```

**b) `IN` bilan (ro'yxat qaytaradi):**

```sql
SELECT nomi FROM hududlar
WHERE hudud_id IN (SELECT hudud_id FROM yillik_kpi
                   WHERE yil = 2024 AND oquvchilar_soni > 500000);
-- Samarqand, Farg'ona, Andijon
```

`NOT IN` — ro'yxatda yo'qlar (Xorazm). Ehtiyot bo'ling: ichki ro'yxatda `NULL` bo'lsa, `NOT IN` hech narsa qaytarmasligi mumkin; `LEFT JOIN ... IS NULL` xavfsizroq.

**c) `FROM` dagi subquery** (taxallus majburiy):

```sql
SELECT t.hudud_id, t.ortacha
FROM (SELECT hudud_id, AVG(oquvchilar_soni) AS ortacha
      FROM yillik_kpi GROUP BY hudud_id) AS t
WHERE t.ortacha > 500000;
```

Bu yerda agregat natijasi ustida `WHERE` ishlatildi (`HAVING` o'rniga ham bo'lardi).

### 2. CTE: `WITH`

**CTE (Common Table Expression)** — so'rov oldidan nom berilgan vaqtinchalik natija. Subquery bilan bir xil ish qiladi, lekin **o'qish osonroq**: tepadan pastga, qadam-baqadam.

Uslubiy ko'rsatmadagi yillik o'sish (YoY) misoli (bizning jadvalga moslangan):

```sql
WITH t AS (
    SELECT yil, SUM(oquvchilar_soni) AS jami
    FROM yillik_kpi
    GROUP BY yil
)
SELECT yil, jami,
       jami - LAG(jami) OVER (ORDER BY yil) AS yoy_change
FROM t
ORDER BY yil;
-- 2022 | 2430000 | None
-- 2023 | 2478000 | 48000
-- 2024 | 2526000 | 48000
```

`LAG(x) OVER (ORDER BY yil)` — oldingi satr qiymatini oladi (oyna funksiyasi, Window Function: rasmiy dasturda analitik operatorlar qatorida tilga olingan; bu yerda faqat ko'rinish uchun, batafsil o'rganilmaydi). Bir nechta CTE vergul bilan:

```sql
WITH jami AS (
    SELECT hudud_id, SUM(oquvchilar_soni) AS s FROM yillik_kpi GROUP BY hudud_id
), ort AS (
    SELECT AVG(s) AS a FROM jami
)
SELECT j.hudud_id, j.s FROM jami j, ort WHERE j.s > ort.a;
-- hudud 2, 3, 4
```

**Qachon nima?** Bir marta ishlatiladigan oddiy shart: subquery. Murakkab, ko'p bosqichli yoki bir necha marta kerak bo'lgan hisob: CTE.

### 3. CASE WHEN: shartli ustun

`CASE WHEN` — SQL ning `if / elif / else` i. Natija — yangi ustun.

```sql
SELECT h.nomi, k.oquvchilar_soni,
       CASE WHEN k.oquvchilar_soni >= 600000 THEN 'Katta'
            WHEN k.oquvchilar_soni >= 400000 THEN 'O''rta'
            ELSE 'Kichik'
       END AS toifa
FROM yillik_kpi k
JOIN hududlar h ON h.hudud_id = k.hudud_id
WHERE k.yil = 2024
ORDER BY k.oquvchilar_soni DESC;
```

Shartlar yuqoridan pastga tekshiriladi, birinchi to'g'risi ishlaydi. `ELSE` yo'q bo'lsa va hech biri mos kelmasa, natija `NULL`. (SQL da matn ichidagi apostrof ikkilanadi: `'O''rta'`.)

**Pivot** (yillar ustunlarga): `SUM(CASE WHEN ...)` + `GROUP BY`. Uslubiy ko'rsatmadagi dbt misolida ham `CASE WHEN` orqali pivot bajarilib, Student/Teacher ratio kabi ko'rsatkichlar hisoblanadi.

```sql
SELECT hudud_id,
       SUM(CASE WHEN yil = 2022 THEN oquvchilar_soni END) AS y2022,
       SUM(CASE WHEN yil = 2023 THEN oquvchilar_soni END) AS y2023,
       SUM(CASE WHEN yil = 2024 THEN oquvchilar_soni END) AS y2024
FROM yillik_kpi
GROUP BY hudud_id;
```

**Shartli sanash:** `SUM(CASE WHEN shart THEN 1 ELSE 0 END)`. Toifalar bo'yicha guruhlash: `GROUP BY toifa` (SQLite alias ni `GROUP BY` da qabul qiladi; boshqa bazalarda CASE ifodasini takrorlash kerak bo'lishi mumkin).

### Odatiy xatolar
1. Subquery qavsini yoki `FROM` dagi subquery taxallusini unutish.
2. Skalyar subquery bittadan ko'p qiymat qaytarishi.
3. `CASE` ni `END` bilan yopmaslik.
4. CTE dan keyin vergulsiz ikkinchi CTE yozish yoki oxirida ortiqcha vergul qoldirish.
5. `CASE` shartlarini noto'g'ri tartibda yozish (katta shart oldin turmasa, kichigi hamma narsani "yutib" yuboradi).

---

## Kod namunalari

### 1-namuna: Subquery (Python)

```python
import sqlite3
conn = sqlite3.connect("data/maktab.db")
c = conn.cursor()
c.execute("""
SELECT h.nomi, k.oquvchilar_soni
FROM yillik_kpi k
JOIN hududlar h ON h.hudud_id = k.hudud_id
WHERE k.yil = 2024
  AND k.oquvchilar_soni > (SELECT AVG(oquvchilar_soni) FROM yillik_kpi WHERE yil = 2024)
ORDER BY k.oquvchilar_soni DESC;
""")
print(c.fetchall())  # Samarqand 620000, Farg'ona 585000, Andijon 524000
```

### 2-namuna: CTE bilan yuklama hisoboti

```python
c.execute("""
WITH yuklama AS (
    SELECT hudud_id, yil,
           ROUND(oquvchilar_soni * 1.0 / maktablar_soni, 1) AS yuk
    FROM yillik_kpi
)
SELECT h.nomi, y.yuk
FROM yuklama y
JOIN hududlar h ON h.hudud_id = y.hudud_id
WHERE y.yil = 2024 AND y.yuk > 600
ORDER BY y.yuk DESC;
""")
print(c.fetchall())  # Toshkent 1426.5, Andijon 623.8
```

Eslatma: bu o'quv ma'lumotida Toshkent shahri uchun maktablar soni ataylab kichik berilgan; sonlar haqiqiy statistika emas.

### 3-namuna: CASE WHEN + guruhlash

```python
c.execute("""
SELECT CASE WHEN oquvchilar_soni >= 600000 THEN 'Katta'
            WHEN oquvchilar_soni >= 400000 THEN 'O''rta'
            ELSE 'Kichik' END AS toifa,
       COUNT(*) AS soni
FROM yillik_kpi WHERE yil = 2024
GROUP BY toifa;
""")
print(c.fetchall())  # Katta 1, Kichik 1, O'rta 3
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson): Skalyar subquery
2024-yilda eng ko'p o'quvchisi bo'lgan hududning `hudud_id` sini subquery (`MAX`) yordamida toping.

**Kutiladigan natija:** `2` (620000).  
**Yechim:**
```sql
SELECT hudud_id, oquvchilar_soni
FROM yillik_kpi
WHERE yil = 2024
  AND oquvchilar_soni = (SELECT MAX(oquvchilar_soni) FROM yillik_kpi WHERE yil = 2024);
```

### 2-topshiriq (o'rta): CASE WHEN toifalash
2024-yil uchun har bir hududga o'quvchi/o'qituvchi nisbati bo'yicha toifa bering: `> 14` — `Yuqori`, `> 13` — `O'rta`, aks holda `Normal`. Hudud nomi, nisbat (2 xona) va toifani chiqaring.

**Kutiladigan natija:** Toshkent 15.16 Yuqori; Andijon 13.58 O'rta; Farg'ona 13.15 O'rta; Buxoro 13.05 O'rta; Samarqand 12.92 Normal.  
**Yechim:**
```sql
SELECT h.nomi,
       ROUND(k.oquvchilar_soni * 1.0 / k.oqituvchilar_soni, 2) AS nisbat,
       CASE WHEN k.oquvchilar_soni * 1.0 / k.oqituvchilar_soni > 14 THEN 'Yuqori'
            WHEN k.oquvchilar_soni * 1.0 / k.oqituvchilar_soni > 13 THEN 'O''rta'
            ELSE 'Normal' END AS toifa
FROM yillik_kpi k
JOIN hududlar h ON h.hudud_id = k.hudud_id
WHERE k.yil = 2024;
```

### 3-topshiriq (qiyin): CTE + pivot + o'sish
CTE yordamida har bir hudud uchun 2022 va 2024-yil o'quvchilar sonini ustunlarga ajrating (pivot), keyin hudud nomi bilan birlashtirib 2 yillik o'sishni (`y2024 - y2022`) hisoblang va o'sish kamayish tartibida chiqaring.

**Kutiladigan natija:** Farg'ona 25000, Andijon 24000, Samarqand 20000, Toshkent 15000, Buxoro 12000.  
**Yechim:**
```sql
WITH p AS (
    SELECT hudud_id,
           SUM(CASE WHEN yil = 2022 THEN oquvchilar_soni END) AS y2022,
           SUM(CASE WHEN yil = 2024 THEN oquvchilar_soni END) AS y2024
    FROM yillik_kpi
    GROUP BY hudud_id
)
SELECT h.nomi, p.y2022, p.y2024, p.y2024 - p.y2022 AS osish
FROM p
JOIN hududlar h ON h.hudud_id = p.hudud_id
ORDER BY osish DESC;
```

---

## Tezkor nazorat savollari

1. Subquery nima va qaysi tartibda bajariladi?  
   *Javob:* Boshqa so'rov ichidagi `SELECT`; avval ichki, keyin tashqi so'rov bajariladi.
2. CTE ning subquerydan afzalligi?  
   *Javob:* Nom beriladi, so'rov tepadan pastga o'qiladi, bir necha marta ishlatish mumkin.
3. `CASE WHEN` da shartlar qaysi tartibda tekshiriladi?  
   *Javob:* Yuqoridan pastga; birinchi to'g'ri shart natijani beradi.
4. `ELSE` yozilmasa va shart mos kelmasa nima chiqadi?  
   *Javob:* `NULL`.
5. `SUM(CASE WHEN ... THEN 1 ELSE 0 END)` nima qiladi?  
   *Javob:* Shartga mos satrlarni sanaydi.

---

## Hafta yakuni va keyingi haftaga ko'prik

4-haftada: `GROUP BY`/`HAVING` (agregatsiya), `JOIN` (jadvallarni bog'lash), Subquery/CTE/`CASE WHEN` (murakkab so'rovlarni qurish). 5-haftadan **ma'lumotlar modellashtirish** boshlanadi: Kimball metodologiyasi, Star Schema va Snowflake Schema, fakt va o'lcham jadvallari. Bugungi `JOIN` ko'nikmasi shu mavzuda asosiy qurol bo'ladi.

---

## Uyga vazifa

`uyga-vazifa.md` ning 3-topshirig'i: CTE va `CASE WHEN` hisoboti (20–30 daqiqa).
