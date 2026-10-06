# 15-dars: Data Mart tushunchasi va sohaga oid martlar yaratish

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Hafta:** 5-hafta, 3-dars (umumiy 15-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

Data Mart tushunchasini (ma'lum soha yoki foydalanuvchi uchun mo'ljallangan analitik qism), uning ombor (DWH) bilan munosabatini, `VIEW` va jadval ko'rinishidagi martlarni, sohaga oid martlarni (`mart_oquvchilar`, `mart_yuklama`) va mart hujjatlashtirishni o'rgatish. Manba: rasmiy dastur («Data Mart nima va qanday yaratiladi; Conformed Dimensions»), uslubiy ko'rsatma («7-bosqich. Data Mart (VIEW) yaratish»; mart ta'rifi, 5 ta analitik so'rov), Kimball & Ross, *The Data Warehouse Toolkit* (2013).

---

## Kutilayotgan natijalar

- Data Mart ni ta'riflaydi va DWH dan farqini aytadi;
- Star Schema ustida `VIEW` ko'rinishida mart yaratadi;
- `CASE WHEN` bilan toifalar qo'shib, soha uchun mart quradi;
- Mart ni hujjatlashtiradi: nomi, maqsadi, foydalanuvchisi, ustunlari.

---

## Kerakli jihozlar

- Python 3.10+ (`sqlite3`);
- `data/maktab.db` (3–4-haftalardagi jadvallar: `hududlar`, `maktablar`, `yillik_kpi`).

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10** | Takrorlash | 14-dars: fakt va dimension, surrogate kalit, yaxlitlik |
| **10–28** | Data Mart | Data Mart nima va nega kerak |
| **28–40** | VIEW mart | `VIEW` bilan mart yaratish |
| **40–45** | Tanaffus | |
| **45–58** | Sohaga oid martlar | Sohaga oid martlar va `CASE WHEN` toifalar |
| **58–75** | Amaliyot | `mart_oquvchilar` va `mart_yuklama` ni qurish, hujjatlashtirish |
| **75–80** | Xulosa | Tezkor nazorat, hafta yakuni, uyga vazifa |

---

## Nazariy qism (konspekt)

### 1. Data Mart tushunchasi

**Data Mart** — ma'lumotlar omborining (DWH) muayyan soha, bo'lim yoki foydalanuvchi guruhi (masalan, ta'lim, moliya, kadrlar) uchun mo'ljallangan kichik, mavzuga yo'naltirilgan qismi. Mart faqat shu sohaga kerakli ustun va qatorlarni, tushunarli nomlar bilan, tayyor holda beradi: tahlilchi 5 ta JOIN yozmaydi. Dimension lar mart lar o'rtasida umumiy bo'lsa (**conformed dimension**), turli mart natijalari bir-biri bilan mos keladi.

```text
Mart nomi:   mart_oquvchilar
Maqsadi:     hududlar va yillar bo'yicha o'quvchilar soni
Foydalanuvchi: rahbariyat, BI tahlilchi
Manba:       fact_kpi, dim_hudud, dim_sana
Yangilanish: har yilgi yuklashdan keyin
```

Har mart uchun hujjat: nomi, maqsadi, foydalanuvchi, manba va yangilanish davri.

### 2. `VIEW` bilan mart yaratish

Eng sodda mart — `VIEW`: saqlangan `SELECT` so'rovi. U jadval kabi o'qiladi, lekin ma'lumotni nusxalamaydi, har safar so'rov ishga tushadi (doim yangi ma'lumot). Alternativ — `CREATE TABLE ... AS SELECT` (jadval mart): tez, lekin yangilab turish kerak. `VIEW` murakkab JOIN larni yashiradi, ustunlarga tushunarli nom beradi va faqat kerakli ustunlarni ochadi.

```sql
CREATE VIEW mart_oquvchilar AS
SELECT h.nomi   AS hudud,
       s.yil    AS yil,
       f.oquvchilar_soni AS oquvchilar
FROM fact_kpi f
JOIN dim_hudud h ON h.hudud_key = f.hudud_key
JOIN dim_sana  s ON s.sana_key  = f.sana_key;

SELECT * FROM mart_oquvchilar WHERE yil = 2024 ORDER BY oquvchilar DESC;
```

Tahlilchi endi bitta oddiy `SELECT` yozadi. 2024-yil: Samarqand 620000, Farg'ona 585000, Andijon 524000, Toshkent 485000, Buxoro 312000.

### 3. Sohaga oid martlar: `mart_yuklama`

Har soha o'z martini oladi: rahbariyat — `mart_oquvchilar`, kadrlar bo'limi — `mart_yuklama` (o'quvchi/o'qituvchi nisbati va toifa). Mart ichida hisoblangan ustunlar va `CASE WHEN` toifalar (`> 14` — Yuqori, `> 13` — O'rta, aks holda Normal) tayyor beriladi, shunda BI vositasi (Power BI) faqat o'qiydi. `1.0 *` butun bo'linmadan saqlaydi.

```sql
CREATE VIEW mart_yuklama AS
SELECT h.nomi AS hudud,
       s.yil  AS yil,
       ROUND(1.0 * f.oquvchilar_soni / f.oqituvchilar_soni, 2) AS nisbat,
       CASE WHEN 1.0 * f.oquvchilar_soni / f.oqituvchilar_soni > 14 THEN 'Yuqori'
            WHEN 1.0 * f.oquvchilar_soni / f.oqituvchilar_soni > 13 THEN 'O''rta'
            ELSE 'Normal' END AS toifa
FROM fact_kpi f
JOIN dim_hudud h ON h.hudud_key = f.hudud_key
JOIN dim_sana  s ON s.sana_key  = f.sana_key;
```

2024: Toshkent 15.16 (Yuqori); Andijon 13.58, Farg'ona 13.15, Buxoro 13.05 (O'rta); Samarqand 12.92 (Normal).

### Odatiy xatolar

1. Martni butun omborning nusxasi sifatida yaratish: faqat kerakli ustunlar ochiladi.
2. Ustunlarga tushunarsiz nomlar berish.
3. Mart ni hujjatlashtirmaslik.
4. VIEW ni jadval deb o'ylash: u ma'lumot saqlamaydi.
5. Bir xil dimension ni har mart uchun alohida (mos kelmaydigan) qilish.

---

## Kod namunalari

### 1-namuna: Martlarni yaratish (Python)

```python
import sqlite3
conn = sqlite3.connect("data/maktab.db")
c = conn.cursor()
c.executescript('''
DROP VIEW IF EXISTS mart_oquvchilar;
CREATE VIEW mart_oquvchilar AS
SELECT h.nomi AS hudud, s.yil AS yil, f.oquvchilar_soni AS oquvchilar
FROM fact_kpi f
JOIN dim_hudud h ON h.hudud_key = f.hudud_key
JOIN dim_sana  s ON s.sana_key  = f.sana_key;
''')
print(c.execute("SELECT * FROM mart_oquvchilar WHERE yil = 2024 ORDER BY oquvchilar DESC").fetchall())
conn.commit(); conn.close()
```

### 2-namuna: Yuklama marti va toifalar (Python)

```python
import sqlite3
c = sqlite3.connect("data/maktab.db").cursor()
c.executescript('''
DROP VIEW IF EXISTS mart_yuklama;
CREATE VIEW mart_yuklama AS
SELECT h.nomi AS hudud, s.yil AS yil,
       ROUND(1.0 * f.oquvchilar_soni / f.oqituvchilar_soni, 2) AS nisbat,
       CASE WHEN 1.0 * f.oquvchilar_soni / f.oqituvchilar_soni > 14 THEN 'Yuqori'
            WHEN 1.0 * f.oquvchilar_soni / f.oqituvchilar_soni > 13 THEN "O'rta"
            ELSE 'Normal' END AS toifa
FROM fact_kpi f
JOIN dim_hudud h ON h.hudud_key = f.hudud_key
JOIN dim_sana s ON s.sana_key = f.sana_key;
''')
print(c.execute("SELECT toifa, COUNT(*) FROM mart_yuklama WHERE yil = 2024 GROUP BY toifa").fetchall())
# [('Normal', 1), ("O'rta", 3), ('Yuqori', 1)]
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson): Mart ta'rifi
`mart_oquvchilar` uchun 1 paragrafli ta'rif yozing: nomi, maqsadi, foydalanuvchi, manba.

**Kutiladigan natija:** Ta'rif to'liq: 4 ta band.  
**Yechim:**
```sql
Mart nomi: mart_oquvchilar
Maqsadi: hududlar va yillar bo'yicha o'quvchilar soni
Foydalanuvchi: rahbariyat, BI tahlilchi
Manba: fact_kpi, dim_hudud, dim_sana
```

### 2-topshiriq (o'rta): mart_oquvchilar
`VIEW` yarating va 2024-yil o'quvchilarini kamayish tartibida chiqaring.

**Kutiladigan natija:** Samarqand 620000, Farg'ona 585000, Andijon 524000, Toshkent 485000, Buxoro 312000.  
**Yechim:**
```sql
CREATE VIEW mart_oquvchilar AS
SELECT h.nomi AS hudud, s.yil AS yil, f.oquvchilar_soni AS oquvchilar
FROM fact_kpi f
JOIN dim_hudud h ON h.hudud_key = f.hudud_key
JOIN dim_sana s ON s.sana_key = f.sana_key;

SELECT * FROM mart_oquvchilar WHERE yil = 2024 ORDER BY oquvchilar DESC;
```

### 3-topshiriq (qiyin): mart_yuklama
Nisbat va `CASE WHEN` toifali `mart_yuklama` yarating; 2024-yil uchun toifalar bo'yicha hududlar sonini toping.

**Kutiladigan natija:** Yuqori 1, O'rta 3, Normal 1.  
**Yechim:**
```sql
SELECT toifa, COUNT(*) AS hududlar
FROM mart_yuklama
WHERE yil = 2024
GROUP BY toifa;
```

### 4-topshiriq (bonus): 5 ta analitik so'rov
Martlardan 5 ta so'rov yozing, kamida 2 tasi `GROUP BY` bilan.

**Kutiladigan natija:** 5 ta so'rov va natijalar.  
**Yechim:**
```sql
SELECT yil, SUM(oquvchilar) FROM mart_oquvchilar GROUP BY yil;
SELECT hudud, MAX(oquvchilar) FROM mart_oquvchilar GROUP BY hudud;
SELECT * FROM mart_yuklama WHERE toifa = 'Yuqori';
SELECT hudud, ROUND(AVG(nisbat), 2) FROM mart_yuklama GROUP BY hudud;
SELECT * FROM mart_oquvchilar WHERE yil = 2022 ORDER BY oquvchilar DESC LIMIT 3;
```

---

## Tezkor nazorat savollari

1. Data Mart nima?  
   *Javob:* Soha yoki foydalanuvchi guruhi uchun mo'ljallangan analitik qism.
2. DWH va mart farqi?  
   *Javob:* DWH — butun tashkilot uchun, mart — bitta soha uchun kichikroq qism.
3. `VIEW` nima?  
   *Javob:* Saqlangan `SELECT` so'rovi; ma'lumotni saqlamaydi.
4. Conformed dimension nima?  
   *Javob:* Bir nechta martda umumiy ishlatiladigan dimension.
5. Mart hujjatida nimalar bo'ladi?  
   *Javob:* Nomi, maqsadi, foydalanuvchi, manba va yangilanish.

---

## Hafta yakuni va keyingi haftaga ko'prik

5-haftada: Kimball, Star va Snowflake (13), fakt va dimension (14), Data Mart (15). 6-haftada dimension larning o'zgarishi — SCD Type 1 va Type 2 hamda surrogate kalitlar chuqur ko'riladi; Data Warehouse va Data Lake ham boshlanadi.

---

## Uyga vazifa

`uyga-vazifa.md` ning 3-topshirig'i: o'z soha martingizni yaratish va 5 ta so'rov yozish (20–30 daqiqa).
