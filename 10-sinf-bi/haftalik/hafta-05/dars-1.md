# 13-dars: Ma'lumotlar modellashtirish: Kimball metodologiyasi, Star Schema va Snowflake Schema

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Hafta:** 5-hafta, 1-dars (umumiy 13-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

Operatsion (OLTP) va tahliliy (OLAP) modellashtirish farqini, Kimball (dimensional modeling) metodologiyasining 4 qadamini, Star Schema va Snowflake Schema tuzilmasini hamda ularni SQLite da `maktab.db` ma'lumotlari ustida qurishni o'rgatish. Manba: rasmiy dastur («Ma'lumotlar modellashtirish: OLTP va OLAP farqi, Star schema va Snowflake schema»), uslubiy ko'rsatma («Star Schema tuzilmasini amalda yaratish»), Kimball & Ross, *The Data Warehouse Toolkit* (2013).

---

## Kutilayotgan natijalar

- OLTP va OLAP farqini misol bilan tushuntiradi;
- Kimball ning 4 qadamini (biznes jarayon, grain, dimension, fact) ketma-ket aytadi;
- Star Schema ni chizadi va SQLite da `dim_` va `fact_` jadvallarini yaratadi;
- Star va Snowflake ni solishtirib, JOIN soni va soddalik bo'yicha tanlov qiladi.

---

## Kerakli jihozlar

- Python 3.10+ (`sqlite3`);
- `data/maktab.db` (3–4-haftalardagi jadvallar: `hududlar`, `maktablar`, `yillik_kpi`).

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10** | Takrorlash | 12-dars: Subquery, CTE, `CASE WHEN`; tezkor savollar |
| **10–28** | OLTP va OLAP | OLTP va OLAP, nega alohida model kerak |
| **28–40** | Kimball va Star | Kimball metodologiyasi va Star Schema |
| **40–45** | Tanaffus | |
| **45–58** | Snowflake | Snowflake Schema va ikki modelni solishtirish |
| **58–75** | Amaliyot | `maktab.db` ustida Star Schema qurish va so'rov yozish |
| **75–80** | Xulosa | Tezkor nazorat, hafta yakuni, uyga vazifa |

---

## Nazariy qism (konspekt)

### 1. OLTP va OLAP: nega alohida model kerak

**OLTP** (Online Transaction Processing) — kundalik amallar (yozish, o'zgartirish): tez, normallashgan (3NF) ko'p jadvalli model, har qatorda kichik o'zgarish. **OLAP** (Online Analytical Processing) — tahlil: ko'p qatorni o'qib jamlash, guruhlash; model sodda va o'qishga qulay bo'lishi kerak. `maktab.db` dagi `hududlar`, `maktablar`, `yillik_kpi` — OLTP uslubida; hisobot uchun esa alohida analitik model quriladi.

```sql
-- OLTP: bitta yozuvni yangilash
UPDATE yillik_kpi SET oquvchilar_soni = 486000
WHERE hudud_id = 1 AND yil = 2024;

-- OLAP: ko'p qatorni jamlash
SELECT yil, SUM(oquvchilar_soni) AS jami
FROM yillik_kpi
GROUP BY yil;
```

OLTP — «bitta qator, tez yozish»; OLAP — «ko'p qator, tez o'qish va jamlash».

### 2. Kimball metodologiyasi va Star Schema

Ralph Kimball yondashuvi (dimensional modeling) 4 qadamdan iborat: (1) biznes jarayonni tanlash (masalan, yillik ta'lim statistikasi), (2) **grain** — fakt jadvalning bitta qatori nimani anglatishini aniqlash (masalan, «hudud x yil»), (3) o'lchamlarni (**dimension**) aniqlash (hudud, yil), (4) faktlarni (**fact**, raqamli o'lchovlar) aniqlash (o'quvchilar, o'qituvchilar, maktablar soni). Star Schema: markazda fact jadval, atrofida dimension jadvallar; fact har dimension bilan FK orqali bog'lanadi.

```sql
CREATE TABLE dim_hudud (
    hudud_key INTEGER PRIMARY KEY,
    nomi TEXT, markaz TEXT
);
CREATE TABLE dim_sana (
    sana_key INTEGER PRIMARY KEY,
    yil INTEGER
);
CREATE TABLE fact_kpi (
    hudud_key INTEGER REFERENCES dim_hudud(hudud_key),
    sana_key  INTEGER REFERENCES dim_sana(sana_key),
    oquvchilar_soni INTEGER,
    oqituvchilar_soni INTEGER,
    maktablar_soni INTEGER
);
```

Grain: `hudud x yil`. 5 hudud va 3 yil bo'lsa, `fact_kpi` da 15 qator bo'ladi.

### 3. Snowflake Schema va ikki modelni solishtirish

Snowflake Schema da dimension jadvallar ham normallashtiriladi: bir dimension bir necha bog'langan jadvalga bo'linadi (masalan, `dim_hudud` dan `dim_markaz` ajratiladi). Ustunlari kam takrorlanadi, joy tejaladi, lekin so'rovda JOIN lar ko'payadi va murakkablashadi. Star — sodda va tez o'qiladi (BI uchun odatiy tanlov), Snowflake — takrorni kamaytiradi.

```sql
-- Star: 1 ta JOIN
SELECT h.nomi, SUM(f.oquvchilar_soni)
FROM fact_kpi f JOIN dim_hudud h ON h.hudud_key = f.hudud_key
GROUP BY h.nomi;

-- Snowflake: 2 ta JOIN
SELECT m.markaz_nomi, SUM(f.oquvchilar_soni)
FROM fact_kpi f
JOIN dim_hudud h ON h.hudud_key = f.hudud_key
JOIN dim_markaz m ON m.markaz_id = h.markaz_id
GROUP BY m.markaz_nomi;
```

Star ni birinchi tanlang: BI uchun sodda va tez. Snowflake faqat dimension juda katta va takrorli bo'lsa kerak.

### Odatiy xatolar

1. Fakt jadvalda tavsiflovchi matn (hudud nomi) saqlash: u dimension da turishi kerak.
2. Grain ni aniqlamasdan jadvallarni loyihalash.
3. Star Schema da dimension lar o'rtasida to'g'ridan-to'g'ri FK qo'yish.
4. Snowflake ni «har doim yaxshiroq» deb o'ylash: u so'rovni murakkablashtiradi.
5. OLTP jadvallarida to'g'ridan-to'g'ri murakkab hisobotlar yozish.

---

## Kod namunalari

### 1-namuna: Star Schema yaratish va to'ldirish (Python)

```python
import sqlite3
conn = sqlite3.connect("data/maktab.db")
c = conn.cursor()
c.executescript('''
DROP TABLE IF EXISTS fact_kpi; DROP TABLE IF EXISTS dim_sana; DROP TABLE IF EXISTS dim_hudud;
CREATE TABLE dim_hudud (hudud_key INTEGER PRIMARY KEY, nomi TEXT, markaz TEXT);
CREATE TABLE dim_sana (sana_key INTEGER PRIMARY KEY, yil INTEGER);
CREATE TABLE fact_kpi (
    hudud_key INTEGER REFERENCES dim_hudud(hudud_key),
    sana_key INTEGER REFERENCES dim_sana(sana_key),
    oquvchilar_soni INTEGER, oqituvchilar_soni INTEGER, maktablar_soni INTEGER);
INSERT INTO dim_hudud SELECT hudud_id, nomi, markaz FROM hududlar;
INSERT INTO dim_sana SELECT DISTINCT yil, yil FROM yillik_kpi;
INSERT INTO fact_kpi SELECT hudud_id, yil, oquvchilar_soni, oqituvchilar_soni, maktablar_soni FROM yillik_kpi;
''')
print(c.execute("SELECT COUNT(*) FROM fact_kpi").fetchone())  # (15,)
conn.commit(); conn.close()
```

### 2-namuna: Star so'rovi (Python)

```python
import sqlite3
c = sqlite3.connect("data/maktab.db").cursor()
c.execute('''
SELECT s.yil, SUM(f.oquvchilar_soni)
FROM fact_kpi f JOIN dim_sana s ON s.sana_key = f.sana_key
GROUP BY s.yil ORDER BY s.yil
''')
print(c.fetchall())  # [(2022, 2430000), (2023, 2478000), (2024, 2526000)]
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson): OLTP yoki OLAP?
Har bir amalni toifalang: (a) yangi o'quvchi qo'shish, (b) hududlar bo'yicha yillik jami, (c) maktab sig'imini yangilash, (d) 3 yillik o'sish trendi.

**Kutiladigan natija:** (a) OLTP, (b) OLAP, (c) OLTP, (d) OLAP  
**Yechim:**
```sql
-- OLTP
INSERT INTO oquvchilar ...;
UPDATE maktablar SET sigim = 1250 WHERE maktab_id = 1;
-- OLAP
SELECT yil, SUM(oquvchilar_soni) FROM yillik_kpi GROUP BY yil;
```

### 2-topshiriq (oson): Grain ni yozing
`maktab.db` asosidagi fakt jadval uchun grain jumlasini yozing va nechta qator bo'lishini ayting.

**Kutiladigan natija:** Grain: bitta qator = bitta hudud, bitta yil. 5 x 3 = 15 qator.  
**Yechim:**
```sql
SELECT COUNT(*) FROM yillik_kpi;  -- 15
```

### 3-topshiriq (o'rta): Star Schema yaratish
`dim_hudud`, `dim_sana` va `fact_kpi` jadvallarini yarating, `yillik_kpi` dan to'ldiring.

**Kutiladigan natija:** `fact_kpi` da 15 qator.  
**Yechim:**
```sql
INSERT INTO dim_hudud (hudud_key, nomi, markaz)
SELECT hudud_id, nomi, markaz FROM hududlar;

INSERT INTO dim_sana (sana_key, yil)
SELECT DISTINCT yil, yil FROM yillik_kpi;

INSERT INTO fact_kpi
SELECT hudud_id, yil, oquvchilar_soni, oqituvchilar_soni, maktablar_soni
FROM yillik_kpi;
```

### 4-topshiriq (qiyin): Yillik jami
Star Schema dan foydalanib, har yil uchun jami o'quvchilar sonini toping.

**Kutiladigan natija:** 2022: 2430000, 2023: 2478000, 2024: 2526000.  
**Yechim:**
```sql
SELECT s.yil, SUM(f.oquvchilar_soni) AS jami
FROM fact_kpi f
JOIN dim_sana s ON s.sana_key = f.sana_key
GROUP BY s.yil
ORDER BY s.yil;
```

### 5-topshiriq (bonus): Snowflake varianti
`dim_hudud` dan `dim_markaz` ni ajrating va markazlar bo'yicha 2024-yil jami o'quvchilarni toping.

**Kutiladigan natija:** Toshkent 485000, Samarqand 620000, Farg'ona 585000, Andijon 524000, Buxoro 312000 (markazlar bo'yicha).  
**Yechim:**
```sql
CREATE TABLE dim_markaz (markaz_id INTEGER PRIMARY KEY, markaz_nomi TEXT UNIQUE);
INSERT INTO dim_markaz (markaz_nomi) SELECT DISTINCT markaz FROM dim_hudud;
-- dim_hudud ga markaz_id ustuni qo'shiladi, so'ng 2 ta JOIN bilan so'rov yoziladi
```

---

## Tezkor nazorat savollari

1. OLTP va OLAP farqi nima?  
   *Javob:* OLTP — kundalik amallar uchun normallashgan model; OLAP — tahlil uchun ko'p qatorni jamlaydigan model.
2. Kimball ning 4 qadami qaysilar?  
   *Javob:* Biznes jarayon, grain, dimension, fact.
3. Grain nima?  
   *Javob:* Fakt jadvalning bitta qatori nimani anglatishi.
4. Star Schema qanday tuzilgan?  
   *Javob:* Markazda fact jadval, atrofida dimension jadvallar.
5. Snowflake Star dan nimasi bilan farq qiladi?  
   *Javob:* Dimension jadvallar normallashtirilgan, JOIN lar ko'p.

---

## Hafta yakuni va keyingi haftaga ko'prik

Kimball metodologiyasi va Star/Snowflake sxemalari 14-darsda fakt va o'lcham jadvallarini batafsil loyihalash uchun asos bo'ladi: grain, additive o'lchovlar va surrogate kalitlar.

---

## Uyga vazifa

`uyga-vazifa.md` ning 1-topshirig'i: `maktab.db` da Star Schema qurish va 3 ta so'rov yozish (20–30 daqiqa).
