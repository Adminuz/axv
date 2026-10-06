# 14-dars: Fakt (Fact) va O'lcham (Dimension) jadvallarini loyihalash

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Hafta:** 5-hafta, 2-dars (umumiy 14-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

Fakt va o'lcham jadvallarini grain asosida loyihalash, o'lchovlar turlarini (additive, semi-additive, non-additive), surrogate kalitning ahamiyatini, dimension va fact jadvallarini `INSERT ... SELECT` bilan yuklash hamda yaxlitlikni tekshirishni o'rgatish. Manba: rasmiy dastur («Fact table va Dimension table tushunchalari; Granularity; Surrogate Keys; Fact Table turlari»), uslubiy ko'rsatma (Dimension va Fact jadvallarni yaratish, `DISTINCT` asosida to'ldirish), Kimball & Ross, *The Data Warehouse Toolkit* (2013).

---

## Kutilayotgan natijalar

- Grain ni aniqlab, fakt jadval ustunlarini tanlaydi;
- Additive, semi-additive va non-additive o'lchovlarni farqlaydi;
- Surrogate kalit bilan dimension jadval yaratadi;
- Dimension va fact jadvallarini yuklab, qatorlar sonini va yetim kalitlarni tekshiradi.

---

## Kerakli jihozlar

- Python 3.10+ (`sqlite3`);
- `data/maktab.db` (3–4-haftalardagi jadvallar: `hududlar`, `maktablar`, `yillik_kpi`).

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10** | Takrorlash | 13-dars: OLTP va OLAP, Kimball, Star va Snowflake |
| **10–28** | Dimension | Dimension jadvallari: atributlar, surrogate kalit |
| **28–40** | Fact | Fakt jadvali: grain va o'lchov turlari |
| **40–45** | Tanaffus | |
| **45–58** | Yuklash va tekshirish | Yuklash tartibi va yaxlitlikni tekshirish |
| **58–75** | Amaliyot | Fakt va dimension jadvallarini loyihalash, yuklash va tekshirish |
| **75–80** | Xulosa | Tezkor nazorat, hafta yakuni, uyga vazifa |

---

## Nazariy qism (konspekt)

### 1. Dimension jadvallari va surrogate kalit

Dimension jadval fakt qatorini «kim, qayerda, qachon» deb tavsiflaydi. Unda: **surrogate key** (sun'iy butun kalit, masalan, `hudud_key`) — manba tizimidan mustaqil; **natural key** (manbadagi `hudud_id`) — manba bilan bog'lash uchun; tavsiflovchi atributlar (`nomi`, `markaz`). Surrogate kalit manba kodlari o'zgarganda ham modelni barqaror tutadi. `dim_sana` da yil bilan birga foydali atributlar (`oquv_yili`, `davr`) bo'ladi.

```sql
CREATE TABLE dim_hudud (
    hudud_key INTEGER PRIMARY KEY AUTOINCREMENT,
    hudud_id  INTEGER UNIQUE,
    nomi      TEXT NOT NULL,
    markaz    TEXT
);
CREATE TABLE dim_sana (
    sana_key  INTEGER PRIMARY KEY AUTOINCREMENT,
    yil       INTEGER UNIQUE,
    oquv_yili TEXT
);
```

`hudud_key` — sun'iy kalit, `hudud_id` — manbadagi natural kalit. Fakt jadval faqat surrogate kalitga tayanadi.

### 2. Fakt jadvali: grain va o'lchov turlari

Fakt jadval: grain aniqlanadi, dimension surrogate kalitlari (FK) va raqamli o'lchovlar saqlanadi. O'lchovlar: **additive** — barcha dimension lar bo'yicha jamlash mumkin (`maktablar_soni` hududlar bo'yicha); **semi-additive** — ba'zi dimension lar bo'yicha jamlash mumkin, vaqt bo'yicha mumkin emas (`oquvchilar_soni` — yillik holat: hududlar bo'yicha jamlanadi, yillar bo'yicha jamlanmaydi, uning o'rniga o'rtacha yoki oxirgi yil olinadi); **non-additive** — jamlab bo'lmaydi (nisbat), shuning uchun nisbatni emas, uning tarkibiy qismlarini saqlang.

```sql
-- NOTO'G'RI: 3 yilni qo'shish
SELECT SUM(oquvchilar_soni) FROM fact_kpi;   -- 7 434 000 ?

-- TO'G'RI: bitta yil ichida hududlar bo'yicha jamlash
SELECT SUM(oquvchilar_soni) FROM fact_kpi f
JOIN dim_sana s ON s.sana_key = f.sana_key
WHERE s.yil = 2024;                           -- 2 526 000
```

Yillar bo'yicha qo'shilgan 7 434 000 — mazmunsiz (bir o'quvchi 3 marta sanalgan). O'rtacha olish yoki bitta yil tanlash kerak.

### 3. Yuklash tartibi va yaxlitlikni tekshirish

Yuklash tartibi: avval dimension lar (`INSERT ... SELECT` bilan manbadan), keyin fakt (manba qatorlarini dimension lar bilan natural kalit orqali `JOIN` qilib surrogate kalitlarni olish). Tekshiruvlar: (1) qatorlar soni manba bilan mos; (2) yetim kalit yo'q (`LEFT JOIN ... IS NULL`); (3) grain bo'yicha dublikat yo'q (`GROUP BY ... HAVING COUNT(*) > 1`).

```sql
INSERT INTO fact_kpi (hudud_key, sana_key, oquvchilar_soni, oqituvchilar_soni, maktablar_soni)
SELECT h.hudud_key, s.sana_key, k.oquvchilar_soni, k.oqituvchilar_soni, k.maktablar_soni
FROM yillik_kpi k
JOIN dim_hudud h ON h.hudud_id = k.hudud_id
JOIN dim_sana  s ON s.yil = k.yil;

-- yetim kalit tekshiruvi
SELECT COUNT(*) FROM fact_kpi f
LEFT JOIN dim_hudud h ON h.hudud_key = f.hudud_key
WHERE h.hudud_key IS NULL;   -- 0 bo'lishi kerak
```

Tekshiruv natijalari: qatorlar 15, yetim kalit 0, grain dublikati yo'q.

### Odatiy xatolar

1. Surrogate kalit o'rniga manba kodini fakt jadvalga FK qilish.
2. Yillik holat qiymatini yillar bo'yicha `SUM` qilish.
3. Nisbatni fakt jadvalda saqlab, keyin `SUM`/`AVG` qilish.
4. Dimension dan oldin fakt ni yuklashga urinish.
5. Yetim kalitni tekshirmaslik.

---

## Kod namunalari

### 1-namuna: Dimension va fakt ni yuklash (Python)

```python
import sqlite3
conn = sqlite3.connect("data/maktab.db")
c = conn.cursor()
c.executescript('''
DROP TABLE IF EXISTS fact_kpi; DROP TABLE IF EXISTS dim_sana; DROP TABLE IF EXISTS dim_hudud;
CREATE TABLE dim_hudud (hudud_key INTEGER PRIMARY KEY AUTOINCREMENT, hudud_id INTEGER UNIQUE, nomi TEXT NOT NULL, markaz TEXT);
CREATE TABLE dim_sana (sana_key INTEGER PRIMARY KEY AUTOINCREMENT, yil INTEGER UNIQUE, oquv_yili TEXT);
CREATE TABLE fact_kpi (
    hudud_key INTEGER REFERENCES dim_hudud(hudud_key),
    sana_key INTEGER REFERENCES dim_sana(sana_key),
    oquvchilar_soni INTEGER, oqituvchilar_soni INTEGER, maktablar_soni INTEGER,
    PRIMARY KEY (hudud_key, sana_key));
INSERT INTO dim_hudud (hudud_id, nomi, markaz) SELECT hudud_id, nomi, markaz FROM hududlar WHERE hudud_id <= 5;
INSERT INTO dim_sana (yil, oquv_yili) SELECT DISTINCT yil, (yil - 1) || '/' || yil FROM yillik_kpi;
INSERT INTO fact_kpi SELECT h.hudud_key, s.sana_key, k.oquvchilar_soni, k.oqituvchilar_soni, k.maktablar_soni
FROM yillik_kpi k JOIN dim_hudud h ON h.hudud_id = k.hudud_id JOIN dim_sana s ON s.yil = k.yil;
''')
print(c.execute("SELECT COUNT(*) FROM fact_kpi").fetchone())  # (15,)
conn.commit(); conn.close()
```

### 2-namuna: Yaxlitlik tekshiruvi (Python)

```python
import sqlite3
c = sqlite3.connect("data/maktab.db").cursor()
print(c.execute("SELECT COUNT(*) FROM fact_kpi").fetchone())             # (15,)
print(c.execute('''SELECT COUNT(*) FROM fact_kpi f
    LEFT JOIN dim_hudud h ON h.hudud_key = f.hudud_key
    WHERE h.hudud_key IS NULL''').fetchone())                             # (0,)
print(c.execute('''SELECT hudud_key, sana_key, COUNT(*) FROM fact_kpi
    GROUP BY hudud_key, sana_key HAVING COUNT(*) > 1''').fetchall())      # []
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson): Grain va ustunlar
`yillik_kpi` uchun fakt jadvalni loyihalang: grain, FK lar va o'lchovlar.

**Kutiladigan natija:** Grain: hudud x yil; FK: hudud_key, sana_key; o'lchovlar: o'quvchilar, o'qituvchilar, maktablar soni.  
**Yechim:**
```sql
CREATE TABLE fact_kpi (
    hudud_key INTEGER REFERENCES dim_hudud(hudud_key),
    sana_key  INTEGER REFERENCES dim_sana(sana_key),
    oquvchilar_soni INTEGER,
    oqituvchilar_soni INTEGER,
    maktablar_soni INTEGER,
    PRIMARY KEY (hudud_key, sana_key)
);
```

### 2-topshiriq (o'rta): Dimension yaratish
`dim_hudud` va `dim_sana` ni surrogate kalit bilan yarating va manbadan to'ldiring.

**Kutiladigan natija:** 5 va 3 qator.  
**Yechim:**
```sql
INSERT INTO dim_hudud (hudud_id, nomi, markaz)
SELECT hudud_id, nomi, markaz FROM hududlar WHERE hudud_id <= 5;
INSERT INTO dim_sana (yil, oquv_yili)
SELECT DISTINCT yil, (yil - 1) || '/' || yil FROM yillik_kpi;
```

### 3-topshiriq (o'rta): Fakt yuklash
`fact_kpi` ni `yillik_kpi` dan dimension lar bilan JOIN qilib yuklang.

**Kutiladigan natija:** 15 qator.  
**Yechim:**
```sql
INSERT INTO fact_kpi
SELECT h.hudud_key, s.sana_key, k.oquvchilar_soni, k.oqituvchilar_soni, k.maktablar_soni
FROM yillik_kpi k
JOIN dim_hudud h ON h.hudud_id = k.hudud_id
JOIN dim_sana s ON s.yil = k.yil;
```

### 4-topshiriq (qiyin): Yaxlitlik tekshiruvi
Qatorlar sonini, yetim kalitni va dublikatni tekshiring.

**Kutiladigan natija:** 15, 0 va bo'sh natija.  
**Yechim:**
```sql
SELECT COUNT(*) FROM fact_kpi;
SELECT COUNT(*) FROM fact_kpi f LEFT JOIN dim_hudud h ON h.hudud_key = f.hudud_key WHERE h.hudud_key IS NULL;
SELECT hudud_key, sana_key, COUNT(*) FROM fact_kpi GROUP BY hudud_key, sana_key HAVING COUNT(*) > 1;
```

### 5-topshiriq (bonus): Semi-additive tahlil
Hududlar bo'yicha 2022–2024 o'rtacha o'quvchilar sonini toping.

**Kutiladigan natija:** Toshkent 477667, Samarqand 610000, Farg'ona 572333, Andijon 512000, Buxoro 306000.  
**Yechim:**
```sql
SELECT h.nomi, ROUND(AVG(f.oquvchilar_soni)) AS ortacha
FROM fact_kpi f JOIN dim_hudud h ON h.hudud_key = f.hudud_key
GROUP BY h.nomi;
```

---

## Tezkor nazorat savollari

1. Surrogate kalit nima uchun kerak?  
   *Javob:* Manba kodlaridan mustaqil, barqaror kalit olish uchun.
2. Additive va semi-additive farqi?  
   *Javob:* Additive barcha o'lchamlar bo'yicha jamlanadi; semi-additive vaqt bo'yicha jamlanmaydi.
3. `oquvchilar_soni` qaysi turdagi o'lchov?  
   *Javob:* Semi-additive (yillik holat).
4. Yuklash tartibi qanday?  
   *Javob:* Avval dimension lar, keyin fakt.
5. Yetim kalitni qanday topamiz?  
   *Javob:* `LEFT JOIN ... WHERE dim_key IS NULL` bilan.

---

## Hafta yakuni va keyingi haftaga ko'prik

14-darsda fakt va dimension jadvallari loyihalandi va yuklandi. 15-darsda shu modeldan ma'lum bo'lim yoki soha uchun mo'ljallangan Data Mart (`VIEW`) yaratiladi.

---

## Uyga vazifa

`uyga-vazifa.md` ning 2-topshirig'i: o'z fakt va dimension jadvallaringizni yuklash va tekshirish (20–30 daqiqa).
