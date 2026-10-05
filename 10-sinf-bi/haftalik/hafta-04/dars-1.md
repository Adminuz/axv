# 10-dars: SQL analitik operatorlari: GROUP BY va HAVING bilan ma'lumotlarni guruhlash

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Hafta:** 4-hafta, 1-dars (umumiy 10-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga SQL da ma'lumotlarni **agregatsiya** qilishni o'rgatish: agregat funksiyalar (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`), `GROUP BY` bilan guruhlash, `HAVING` bilan guruhlarni filtrlash, `WHERE` va `HAVING` farqini tushunish. Rasmiy uslubiy ko'rsatmadagi "Maktab tahliliy platformasi" ssenariysi (yillar bo'yicha jami o'quvchilar va o'qituvchilar, o'quvchi/o'qituvchi nisbati KPI, `NULLIF`, dublikatni `GROUP BY ... HAVING COUNT(*) > 1` bilan tekshirish) `maktab.db` ustida amalga oshiriladi.

---

## Kutilayotgan natijalar

- Agregat funksiyalarning vazifasini aytib, `SELECT` da qo'llay oladi;
- `GROUP BY` yordamida yil, hudud, tur kesimida hisobot tuza oladi;
- `WHERE` (guruhlashdan oldin, satrlarni) va `HAVING` (guruhlashdan keyin, guruhlarni) farqini tushuntiradi;
- SQL so'rovining mantiqiy ijro tartibini (`FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT`) biladi;
- `NULLIF` bilan nolga bo'lishdan saqlanadi va KPI nisbatini hisoblaydi;
- Dublikatlarni `GROUP BY ... HAVING COUNT(*) > 1` bilan topadi.

---

## Kerakli jihozlar

- Python 3.10+ (`sqlite3`), DBeaver yoki SQLite Viewer;
- 3-haftada yaratilgan `data/maktab.db` (jadvallar: `hududlar`, `maktablar`, `yillik_kpi`).

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10** | Takrorlash | 3-hafta: `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`; ma'lumotni dars uchun to'ldirish skripti |
| **10–25** | Agregat funksiyalar | `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`, `NULL` va `COUNT(*)` / `COUNT(ustun)` farqi |
| **25–40** | `GROUP BY` | Yillar bo'yicha jami, bir nechta ustun bo'yicha guruhlash, KPI nisbati va `NULLIF` |
| **40–45** | Tanaffus | |
| **45–55** | `HAVING` | `WHERE` vs `HAVING`, ijro tartibi, dublikat tekshirish |
| **55–75** | Amaliyot | 3 darajali topshiriqlar |
| **75–80** | Xulosa | Tezkor nazorat, uyga vazifa |

---

## Nazariy qism (konspekt)

### 1. Agregatsiya nima?

Shu paytgacha `SELECT` har bir satr uchun bitta natija qaytardi. **Agregat funksiya** ko'p satrni **bitta qiymatga** aylantiradi. BI da bu "hisobot" degani: jami, o'rtacha, eng katta.

| Funksiya | Nima qiladi |
|---|---|
| `COUNT(*)` | Satrlar sonini sanaydi |
| `COUNT(ustun)` | `NULL` bo'lmagan qiymatlar sonini sanaydi |
| `SUM(ustun)` | Yig'indi |
| `AVG(ustun)` | O'rtacha (`NULL` lar hisobga olinmaydi) |
| `MIN` / `MAX` | Eng kichik / eng katta |

```sql
SELECT COUNT(*) AS yozuvlar, SUM(oquvchilar_soni) AS jami,
       ROUND(AVG(oquvchilar_soni), 0) AS ortacha,
       MIN(oquvchilar_soni) AS eng_kam, MAX(oquvchilar_soni) AS eng_kop
FROM yillik_kpi;
```

**Muhim:** agregat funksiya `WHERE` ichida ishlamaydi (`WHERE SUM(x) > 5` xato), chunki `WHERE` guruhlardan oldin bajariladi.

### 2. GROUP BY: guruhlab hisoblash

`GROUP BY` satrlarni bir xil qiymatli guruhlarga bo'ladi, agregat funksiya har guruh uchun alohida hisoblanadi. Rasmiy uslubiy ko'rsatmadagi 3-bosqich (yillar bo'yicha jami):

```sql
SELECT yil, SUM(oquvchilar_soni) AS jami_oquvchi
FROM yillik_kpi
GROUP BY yil
ORDER BY yil;
```

**Qoida:** `SELECT` dagi har bir ustun yoki `GROUP BY` da bo'lishi, yoki agregat funksiya ichida bo'lishi kerak. Bir nechta ustun bo'yicha guruhlash mumkin: `GROUP BY hudud_id, yil`.

**KPI: o'quvchi/o'qituvchi nisbati** (uslubiy ko'rsatmadagi 5-bosqich; u yerda PostgreSQL `::numeric` ishlatilgan, SQLite da `* 1.0`):

```sql
SELECT yil,
       ROUND(SUM(oquvchilar_soni) * 1.0 / NULLIF(SUM(oqituvchilar_soni), 0), 2) AS nisbat
FROM yillik_kpi
GROUP BY yil ORDER BY yil;
```

`NULLIF(a, 0)` — `a` nolga teng bo'lsa `NULL` qaytaradi, shunda nolga bo'lish xatosi chiqmaydi.

### 3. HAVING: guruhlarni filtrlash

| | `WHERE` | `HAVING` |
|---|---|---|
| Nimani filtrlaydi | Satrlarni | Guruhlarni |
| Qachon bajariladi | Guruhlashdan **oldin** | Guruhlashdan **keyin** |
| Agregat funksiya | Mumkin emas | Mumkin |

**Mantiqiy ijro tartibi:** `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT`.

```sql
-- o'rtacha o'quvchilari 500 000 dan ko'p hududlar
SELECT hudud_id, ROUND(AVG(oquvchilar_soni), 0) AS ortacha
FROM yillik_kpi
GROUP BY hudud_id
HAVING AVG(oquvchilar_soni) > 500000
ORDER BY ortacha DESC;
```

**Dublikat tekshirish** (uslubiy ko'rsatmadagi "C) Dublikat tekshirish" usuli): kalit bo'yicha guruhlab, soni 1 dan ko'p bo'lganlarni ko'rsatamiz. Natija bo'sh bo'lsa, dublikat yo'q.

```sql
SELECT hudud_id, yil, COUNT(*) AS soni
FROM yillik_kpi
GROUP BY hudud_id, yil
HAVING COUNT(*) > 1;
```

---

## Kod namunalari

### 0-namuna: Dars uchun ma'lumot (hamma o'quvchida bir xil bo'lishi uchun)

> Diqqat: bu o'quv uchun **o'ylab topilgan** sonlar, haqiqiy statistika emas.

```python
import sqlite3

conn = sqlite3.connect("data/maktab.db")
conn.execute("PRAGMA foreign_keys = ON")
c = conn.cursor()

hududlar = [(1, "Toshkent shahri", "Toshkent"), (2, "Samarqand viloyati", "Samarqand"),
            (3, "Farg'ona viloyati", "Farg'ona"), (4, "Andijon viloyati", "Andijon"),
            (5, "Buxoro viloyati", "Buxoro"), (6, "Xorazm viloyati", "Urganch")]
c.executemany("INSERT OR IGNORE INTO hududlar (hudud_id, nomi, markaz) VALUES (?, ?, ?)", hududlar)

kpi = [(1,2022,470000,31000,335),(1,2023,478000,31500,338),(1,2024,485000,32000,340),
       (2,2022,600000,46500,1240),(2,2023,610000,47200,1250),(2,2024,620000,48000,1260),
       (3,2022,560000,43000,1010),(3,2023,572000,43800,1015),(3,2024,585000,44500,1020),
       (4,2022,500000,37000,830),(4,2023,512000,37800,835),(4,2024,524000,38600,840),
       (5,2022,300000,23000,640),(5,2023,306000,23400,642),(5,2024,312000,23900,645)]
c.executemany("""INSERT OR IGNORE INTO yillik_kpi
    (hudud_id, yil, oquvchilar_soni, oqituvchilar_soni, maktablar_soni) VALUES (?, ?, ?, ?, ?)""", kpi)

maktablar = [(1,14,1200,"Umumiy o'rta"),(1,28,850,"Ixtisoslashgan"),(1,45,1000,"Umumiy o'rta"),
             (2,1,1500,"Umumiy o'rta"),(2,7,900,"Umumiy o'rta"),(2,12,1100,"Ixtisoslashgan"),
             (3,3,1300,"Umumiy o'rta"),(3,9,700,"Umumiy o'rta"),
             (4,5,1400,"Umumiy o'rta"),(5,2,600,"Umumiy o'rta")]
c.executemany("INSERT OR IGNORE INTO maktablar (hudud_id, raqam, sigim, turi) VALUES (?, ?, ?, ?)", maktablar)

conn.commit()
print(c.execute("SELECT COUNT(*) FROM yillik_kpi").fetchone())   # (15,) yoki ko'proq (uyga vazifa yozuvlari)
conn.close()
```

Eslatma: 3-hafta uyga vazifasida o'quvchilar o'z yozuvlarini kiritgan bo'lishi mumkin; shuning uchun natijalar farq qilsa, yangi `maktab_dars.db` yarating (fayl nomini o'zgartiring), jadvallarni 3-hafta 2-dars skripti bilan qayta yarating.

### 1-namuna: Agregat funksiyalar (natija: `15 | 7434000 | 495600.0 | 300000 | 620000`)

```python
import sqlite3
conn = sqlite3.connect("data/maktab.db")
c = conn.cursor()
c.execute("""
SELECT COUNT(*), SUM(oquvchilar_soni), ROUND(AVG(oquvchilar_soni), 0),
       MIN(oquvchilar_soni), MAX(oquvchilar_soni)
FROM yillik_kpi;
""")
print(c.fetchone())
```

### 2-namuna: Yillar bo'yicha jami va KPI

```python
c.execute("""
SELECT yil,
       SUM(oquvchilar_soni)  AS jami_oquvchi,
       SUM(oqituvchilar_soni) AS jami_oqituvchi,
       ROUND(SUM(oquvchilar_soni) * 1.0 / NULLIF(SUM(oqituvchilar_soni), 0), 2) AS nisbat
FROM yillik_kpi
GROUP BY yil
ORDER BY yil;
""")
for yil, a, b, n in c.fetchall():
    print(f"{yil} | o'quvchi {a:>9,} | o'qituvchi {b:>8,} | nisbat {n}")
# 2022 | o'quvchi 2,430,000 | o'qituvchi  180,500 | nisbat 13.46
# 2023 | o'quvchi 2,478,000 | o'qituvchi  183,700 | nisbat 13.49
# 2024 | o'quvchi 2,526,000 | o'qituvchi  187,000 | nisbat 13.51
```

### 3-namuna: `WHERE` + `GROUP BY` + `HAVING` birga

```python
c.execute("""
SELECT hudud_id, COUNT(*) AS maktab_soni, SUM(sigim) AS umumiy_sigim
FROM maktablar
WHERE sigim >= 600
GROUP BY hudud_id
HAVING COUNT(*) >= 2
ORDER BY umumiy_sigim DESC;
""")
print(c.fetchall())
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson): Maktab turlari bo'yicha hisobot
`maktablar` jadvalidan har bir `turi` bo'yicha maktablar soni va o'rtacha sig'imni chiqaring.

**Kutiladigan natija:** 2 qator: `Ixtisoslashgan | 2 | 975.0`, `Umumiy o'rta | 8 | 1075.0`.  
**Yechim:**
```sql
SELECT turi, COUNT(*) AS soni, ROUND(AVG(sigim), 1) AS ortacha_sigim
FROM maktablar
GROUP BY turi;
```

### 2-topshiriq (o'rta): HAVING bilan filtr
2023 va 2024-yillar uchun yillik jami o'quvchilar sonini toping va faqat jami 2 500 000 dan oshgan yillarni qoldiring.

**Kutiladigan natija:** faqat 2024 (`2526000`); 2023 (`2478000`) chiqmaydi.  
**Yechim:**
```sql
SELECT yil, SUM(oquvchilar_soni) AS jami
FROM yillik_kpi
WHERE yil IN (2023, 2024)
GROUP BY yil
HAVING SUM(oquvchilar_soni) > 2500000;
```

### 3-topshiriq (qiyin): Hudud reytingi va xatoni topish
(a) Har bir hudud uchun 3 yillik jami o'quvchilar sonini hisoblab, eng kattasi birinchi bo'lsin va faqat 1 500 000 dan ko'p bo'lganlar chiqsin. (b) Quyidagi so'rovdagi xatoni toping: `SELECT yil, SUM(oquvchilar_soni) FROM yillik_kpi WHERE SUM(oquvchilar_soni) > 1000000 GROUP BY yil;`

**Kutiladigan natija:** (a) `hudud_id` 2 (1 830 000), 3 (1 717 000), 4 (1 536 000). (b) `WHERE` ichida agregat funksiya ishlatilgan.  
**Yechim:**
```sql
-- (a)
SELECT hudud_id, SUM(oquvchilar_soni) AS jami
FROM yillik_kpi
GROUP BY hudud_id
HAVING SUM(oquvchilar_soni) > 1500000
ORDER BY jami DESC;

-- (b) to'g'ri variant: agregat shart HAVING ga ko'chiriladi
SELECT yil, SUM(oquvchilar_soni)
FROM yillik_kpi
GROUP BY yil
HAVING SUM(oquvchilar_soni) > 1000000;
```

---

## Tezkor nazorat savollari

1. `COUNT(*)` va `COUNT(ustun)` farqi nima?  
   *Javob:* `COUNT(*)` barcha satrlarni, `COUNT(ustun)` esa shu ustunda `NULL` bo'lmagan satrlarni sanaydi.
2. `WHERE` va `HAVING` qaysi biri guruhlashdan oldin bajariladi?  
   *Javob:* `WHERE` oldin (satrlarni filtrlaydi), `HAVING` keyin (guruhlarni filtrlaydi).
3. Nega `WHERE SUM(x) > 5` xato?  
   *Javob:* `WHERE` bajarilayotganda guruhlar hali yo'q, agregat hisoblanmagan.
4. `NULLIF(a, 0)` nima uchun kerak?  
   *Javob:* Maxraj nol bo'lsa `NULL` qaytarib, nolga bo'lish xatosining oldini oladi.
5. Dublikatni qanday topamiz?  
   *Javob:* Kalit ustunlar bo'yicha `GROUP BY ... HAVING COUNT(*) > 1`.

---

## Uyga vazifa

`uyga-vazifa.md` ning 1-topshirig'i: `GROUP BY` / `HAVING` hisoboti (20–30 daqiqa).
