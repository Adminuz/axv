# 9-dars: SQL analitik operatorlari: SELECT, WHERE, ORDER BY, LIMIT asoslari

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Hafta:** 3-hafta, 3-dars (umumiy 9-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga ma'lumotlar tahlilining asosiy quroli bo'lgan **SQL (Structured Query Language)** tilining DQL (Data Query Language) qatlamini o'rgatish; ma'lumotlarni tanlab olish (**SELECT**), hisob-kitoblar va ustunlarni qayta nomlash (**AS alias**); murakkab mantiqiy va arifmetik shartlar bilan filtrlash (**WHERE: AND, OR, NOT, BETWEEN, IN, LIKE, IS NULL**); natijalarni ko'p darajali saralash (**ORDER BY ASC/DESC**) hamda yozuvlarni chegaralash va sahifalash (**LIMIT va OFFSET**); rasmiy o'quv qo'llanmasidagi "Maktab KPI" dataseti bo'yicha TOP-N tahlillarni (masalan, 2024-yilda O'zbekistonning eng ko'p o'quvchisi bo'lgan TOP-10 hududini aniqlash) mustaqil yoza olish ko'nikmalarini shakllantirish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- SQL buyruqlarining asosiy guruhlarini (DDL, DML, DQL) farqlash va `SELECT` ning o'rnini bilish;
- `SELECT` operatori yordamida aniq ustunlarni tanlash, ustunlar ustida arifmetik amallar bajarish va ularga `AS` orqali yangi nom berish;
- `WHERE` bandida solishtirish (`=, !=, >, <, >=, <=`) va mantiqiy (`AND`, `OR`, `NOT`) operatorlarni to'g'ri birlashtira olish;
- Diapazonli qidiruv (`BETWEEN`), to'plamdan izlash (`IN`) va shablonli qidiruv (`LIKE` bilan `%` va `_`) dan foydalanish;
- `NULL` qiymatlarni tekshirishda `IS NULL` va `IS NOT NULL` sintaksisini qo'llash;
- `ORDER BY` yordamida natijalarni o'sish (`ASC`) va kamayish (`DESC`) tartibida bir nechta ustunlar kesimida saralash;
- `LIMIT` va `OFFSET` orqali TOP-N tahlillarni bajarish va veb-tizimlardagi sahifalash (Pagination) mexanizmini tushunish;
- Python `sqlite3` yordamida tahliliy SQL so'rovlarini ishga tushirish va natijalarni konsolga tartibli chiqarish.

---

## Kerakli jihozlar va vositalar

- O'qituvchi va o'quvchilar uchun shaxsiy kompyuter;
- Python 3.10+ (o'rnatilgan `sqlite3` moduli bilan);
- `data/maktab.db` ma'lumotlar bazasi (o'tgan darsda yaratilgan);
- DBeaver yoki SQLite Viewer (VS Code).

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va takrorlash | ERD modeli, 1:N va M:N bog'lanishlar, Junction table bo'yicha savol-javob |
| **10–30 min** | Yangi mavzu bayoni (Nazariya) | SQL tili tuzilishi, SELECT va arifmetik amallar, WHERE filtr shartlari (BETWEEN, IN, LIKE) |
| **30–50 min** | Saralash va Chegaralash (Nazariya) | ORDER BY ASC/DESC, bir nechta ustunli saralash, LIMIT va OFFSET (Pagination, TOP-N) |
| **50–70 min** | Amaliyot: O'zbekiston Ta'lim KPI tahlili | Python sqlite3 da TOP-10 hududlarni aniqlash, murakkab filtrlash so'rovlarini yozish |
| **70–80 min** | Dars xulosasi va 3-hafta yakuni | Dars natijalari, tezkor savol-javob va uyga vazifani tushuntirish |

---

## Nazariy qism (Batafsil konspekt)

### 1. SQL so'rovining mantiqiy tuzilishi

SQL (Structured Query Language) — bu deklarativ til. Biz kompyuterga "qanday qilib qidirishni" emas, "aynan qanday natija kerakligini" aytamiz.

Boshlang'ich analitik so'rov skeleti:
```sql
SELECT ustun1, ustun2, (ustun1 / ustun2) AS yangi_nom
FROM jadval_nomi
WHERE shartlar
ORDER BY saralash_ustuni DESC
LIMIT soni OFFSET boshlangich_orin;
```

**Mantiqiy bajarilish tartibi (SQL Order of Execution):**
Dasturchi `SELECT` dan boshlab yozsa ham, ma'lumotlar bazasi so'rovni boshqacha ketma-ketlikda bajaradi:
1. `FROM` (Jadval topiladi);
2. `WHERE` (Keraksiz satrlar filtrlanadi);
3. `SELECT` (Kerakli ustunlar hisoblanadi va olinadi);
4. `ORDER BY` (Natija saralanadi);
5. `LIMIT / OFFSET` (Kerakli qism kesib olinadi).

---

### 2. `WHERE` filtrlash operatorlari

Ma'lumotlar omboridan faqat kerakli satrlarni ajratib olish uchun `WHERE` qo'llaniladi:

1. **Solishtirish operatorlari:** `=`, `!=` (yoki `<>`), `>`, `<`, `>=`, `<=`.
2. **Mantiqiy bog'lovchilar:**
   - `AND`: Har ikkala shart to'g'ri bo'lishi shart;
   - `OR`: Hech bo'lmaganda bitta shart to'g'ri bo'lsa yetarli;
   - `NOT`: Shartni teskarisiga aylantiradi.
3. **Maxsus analitik operatorlar:**
   - `BETWEEN a AND b`: Qiymat `[a, b]` oraliqda ekanini tekshiradi (chegaralar kiradi);
   - `IN (qiymat1, qiymat2, ...)`: Ro'yxatdagi qiymatlardan biriga teng bo'lishini tekshiradi;
   - `LIKE 'shablon'`: Matnli qidiruv:
     - `%` — ixtiyoriy sondagi belgilar (masalan, `nomi LIKE 'Toshkent%'`);
     - `_` — aniq bitta belgi (masalan, `sinf_nomi LIKE '1_-A'`);
   - `IS NULL` va `IS NOT NULL`: Bo'sh qiymatlarni aniqlash (`= NULL` ishlamaydi!).

---

### 3. `ORDER BY` va `LIMIT / OFFSET`

1. **ORDER BY:**
   - `ASC` (Ascending): Kichikdan kattaga (o'sish tartibi, sukut bo'yicha);
   - `DESC` (Descending): Kattadan kichikka (kamayish tartibi).
   - *Ko'p ustunli saralash:* Avval yil bo'yicha kamayish, keyin o'quvchilar soni bo'yicha kamayish:
     ```sql
     ORDER BY yil DESC, oquvchilar_soni DESC
     ```

2. **LIMIT va OFFSET (TOP-N va Pagination):**
   - `LIMIT N`: Faqat eng yuqoridagi N ta yozuvni oladi.
   - `OFFSET K`: Dastlabki K ta yozuvni tashlab yuboradi.
   - *Veb-sahifalash formulasi:*
     - 1-sahifa (1–10): `LIMIT 10 OFFSET 0`
     - 2-sahifa (11–20): `LIMIT 10 OFFSET 10`
     - 3-sahifa (21–30): `LIMIT 10 OFFSET 20`

---

## Kod namunalari

### 1-namuna: Asosiy SELECT, Arifmetika va Alias

```python
import sqlite3

conn = sqlite3.connect('data/maktab.db')
cursor = conn.cursor()

# Maktablar sig'imi va o'rtacha xona yuklamasini hisoblash
cursor.execute("""
SELECT 
    raqam AS maktab_raqami,
    sigim AS umumiy_sigim,
    ROUND(sigim / 30.0, 1) AS taxminiy_xonalar_soni
FROM maktablar;
""")

for row in cursor.fetchall():
    print(f"Maktab #{row[0]} | Sig'im: {row[1]} | Taxminiy sinfxonalar: {row[2]}")
```

### 2-namuna: WHERE filtrining barcha turlari

```python
# 1. BETWEEN va IN misoli
cursor.execute("""
SELECT hudud_id, yil, oquvchilar_soni, maktablar_soni
FROM yillik_kpi
WHERE yil BETWEEN 2020 AND 2024
  AND hudud_id IN (1, 2, 3);
""")

print("\n--- 2020-2024 yillar filtri ---")
for r in cursor.fetchall():
    print(r)

# 2. LIKE bilan matn qidirish
cursor.execute("""
SELECT hudud_id, nomi, markaz
FROM hududlar
WHERE nomi LIKE '%viloyati';
""")

print("\n--- Faqat viloyatlar ro'yxati ---")
for r in cursor.fetchall():
    print(f"ID: {r[0]} | Nomi: {r[1]} | Markazi: {r[2]}")
```

### 3-namuna: TOP-10 tahlili (ORDER BY + LIMIT) — Rasmiy uslubiy ssenariy

```python
# 2024-yil uchun eng ko'p o'quvchisi bo'lgan TOP-5 hududni aniqlash
cursor.execute("""
SELECT 
    h.nomi,
    k.oquvchilar_soni,
    k.oqituvchilar_soni,
    k.maktablar_soni
FROM yillik_kpi k
JOIN hududlar h ON k.hudud_id = h.hudud_id
WHERE k.yil = 2024
ORDER BY k.oquvchilar_soni DESC
LIMIT 5;
""")

print("\n=== 2024-yil: O'zbekiston TOP-5 Hudud (O'quvchilar soni) ===")
rank = 1
for row in cursor.fetchall():
    print(f"{rank}. {row[0]:<22} | O'quvchilar: {row[1]:,} | O'qituvchilar: {row[2]:,} | Maktablar: {row[3]}")
    rank += 1

conn.close()
```

---

## Amaliy topshiriqlar

### 1-topshiriq: Mantiqiy shartlar bilan filtrlash (Oson)
`yillik_kpi` jadvalidan:
- Yili 2023 yoki 2024 bo'lgan;
- Maktablar soni kamida 500 ta bo'lgan barcha yozuvlarni ajratib oluvchi SQL so'rovini yozing.

**Kutiladigan natija:** `WHERE yil IN (2023, 2024) AND maktablar_soni >= 500` sharti qo'llaniladi.  
**Yechim:**  
```sql
SELECT hudud_id, yil, maktablar_soni, oquvchilar_soni
FROM yillik_kpi
WHERE yil IN (2023, 2024) AND maktablar_soni >= 500;
```

---

### 2-topshiriq: Matnli qidiruv va LIKE (O'rta)
O'zbekiston viloyatlari ichida nomida "shahar" so'zi qatnashgan barcha hududlarni yoki nomi "B" harfi bilan boshlanuvchi viloyatlarni topuvchi bitta SQL so'rovini yozing.

**Kutiladigan natija:** `LIKE '%shahar%' OR nomi LIKE 'B%'` operatori to'g'ri ishlatiladi.  
**Yechim:**  
```sql
SELECT hudud_id, nomi, markaz
FROM hududlar
WHERE nomi LIKE '%shahar%' OR nomi LIKE 'B%';
```

---

### 3-topshiriq: Sahifalash (Pagination) va Resurs yuklamasi (Qiyin)
Katta ta'lim monitoringi platformasi uchun sahifalash mexanizmini yarating:
Har bir sahifada 3 tadan hudud ko'rsatilishi kerak.
1. 1-sahifani chiqaruvchi so'rovni yozing (1–3 o'rinlar);
2. 2-sahifani chiqaruvchi so'rovni yozing (4–6 o'rinlar).
Barcha natijalar 1 o'qituvchiga to'g'ri kelgan o'quvchilar nisbati (`oquvchilar_soni / oqituvchilar_soni`) kamayish tartibida saralansin.

**Kutiladigan natija:** `LIMIT 3 OFFSET 0` va `LIMIT 3 OFFSET 3` yordamida sahifalash amalga oshiriladi.  
**Yechim:**  
```sql
-- 1-sahifa:
SELECT h.nomi, ROUND(CAST(k.oquvchilar_soni AS REAL) / k.oqituvchilar_soni, 2) AS yuklama
FROM yillik_kpi k
JOIN hududlar h ON k.hudud_id = h.hudud_id
WHERE k.yil = 2024
ORDER BY yuklama DESC
LIMIT 3 OFFSET 0;

-- 2-sahifa:
SELECT h.nomi, ROUND(CAST(k.oquvchilar_soni AS REAL) / k.oqituvchilar_soni, 2) AS yuklama
FROM yillik_kpi k
JOIN hududlar h ON k.hudud_id = h.hudud_id
WHERE k.yil = 2024
ORDER BY yuklama DESC
LIMIT 3 OFFSET 3;
```

---

## Tezkor nazorat savollari

1. SQL so'rovida `WHERE` va `SELECT` ning mantiqiy bajarilish ketma-ketligi qanday?  
   *Javob:* Avval `WHERE` bajarilib, keraksiz satrlar filtrlanadi, shundan so'ng qolgan satrlar ustida `SELECT` ustunlarni hisoblaydi.
2. `BETWEEN 10 AND 20` shartiga 10 va 20 sonlarining o'zi kiradimi?  
   *Javob:* Ha, SQL da `BETWEEN` oraliqning har ikkala chegarasini o'z ichiga oladi (`>= 10 AND <= 20`).
3. Matnli qidiruvda `%` va `_` belgilarining farqi nimada?  
   *Javob:* `%` har qanday sondagi (0 yoki undan ortiq) belgilarni, `_` esa qat'iy ravishda faqat 1 ta belgini bildiradi.
4. `LIMIT 5 OFFSET 10` nimani anglatadi?  
   *Javob:* Dastlabki 10 ta satrni tashlab yuborib, 11-qatordan boshlab keyingi 5 ta satrni natijaga chiqaradi.

---

## Uyga vazifa

1. `maktab.db` bazasidagi barcha hududlar bo'yicha o'rtacha bitta maktabga to'g'ri kelgan o'quvchilar sonini hisoblang.
2. Yuklama 800 nafardan oshgan maktablar mavjud bo'lgan hududlarni `WHERE` orqali filtrlang.
3. Natijalarni yuklama bo'yicha kamayish tartibida saralab, eng yuqori 3 ta hududni `LIMIT` orqali ekranga chiqaruvchi Python skriptini yozing.
