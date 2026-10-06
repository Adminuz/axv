# 17-dars. GROUP BY operatori va guruhlash mexanizmi

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga `GROUP BY` yordamida qatorlarni guruhlash va har bir guruh uchun aggregatsiya hisoblashni, `SELECT` ro'yxati qoidasini, bir nechta ustun bo'yicha guruhlashni hamda `WHERE` va `ORDER BY` bilan birga qo'llashni o'rgatish.
- **Kutiladigan natija:** O'quvchilar `GROUP BY` ning vazifasini va ishlash mexanizmini tushuntiradi; har bir shahar/toifa uchun `COUNT`, `SUM`, `AVG` hisoblaydi; `SELECT` dagi aggregatsiyasiz ustun `GROUP BY` da bo'lishi shartligini biladi; ikki ustun bo'yicha guruhlaydi; `WHERE` va `ORDER BY` ni `GROUP BY` bilan to'g'ri birga ishlatadi.
- **Vaqt taqsimoti:**
  - 16-dars: COUNT, SUM, AVG, NULL: 10 daqiqa
  - GROUP BY g'oyasi: guruh = bitta qator: 10 daqiqa
  - SELECT qoidasi va xatolar: 20 daqiqa
  - Ikki ustun, WHERE, ORDER BY: 15 daqiqa
  - Amaliyot, xatolar, xulosa: 25 daqiqa

> Manba: o'quv dasturi — «GROUP BY: bir va bir nechta ustun bo'yicha guruhlash», «WHERE + GROUP BY birga» va «GROUP BY + ORDER BY» mavzulari; 16-darsdagi `Sotuvlar` jadvali. So'rovlar SQL Server (T-SQL) sintaksisida, natijalar SQLite'da tekshirilgan.

---

## Mentor konspekti

### 1. GROUP BY: ma'lumotlarni guruhlash

Aggregatsiya o'z-o'zidan butun jadval uchun bitta natija beradi. Lekin biznesga ko'pincha «**har bir** shahar bo'yicha», «**har bir** toifa bo'yicha» kerak. `GROUP BY ustun` qatorlarni ustun qiymati bo'yicha guruhlarga ajratadi, aggregatsiya esa **har bir guruh uchun alohida** hisoblanadi, natijada har guruh bitta qator bo'ladi. `Sotuvlar` jadvalida 3 ta shahar bor: Toshkent (4 sotuv, 5 380 000), Samarqand (3 sotuv, 9 640 000), Buxoro (3 sotuv, 3 360 000). Ular yig'indisi umumiy 18 380 000 ga teng. Guruhlash mexanizmi: SQL qatorlarni shahar bo'yicha «savatlarga» soladi, har savat ichida funksiyani hisoblaydi va savat boshiga bitta qator chiqaradi. `GROUP BY` natijada tartib kafolatlamaydi: tartib kerak bo'lsa `ORDER BY` qo'shing.

```sql
SELECT Shahar,
       COUNT(*)   AS SotuvSoni,
       SUM(Summa) AS Jami
FROM Sotuvlar
GROUP BY Shahar;
-- Toshkent  | 4 | 5380000
-- Samarqand | 3 | 9640000
-- Buxoro    | 3 | 3360000
```

> Professional maslahat: Natijada 10 emas, 3 qator chiqadi — shaharlar soni qancha bo'lsa, shuncha qator. Qatorlar tartibi har xil bo'lishi mumkin.

### 2. GROUP BY qoidasi: SELECT dagi ustunlar

Asosiy qoida: `SELECT` ro'yxatidagi har bir ustun yoki **aggregatsiya ichida**, yoki **`GROUP BY` da** bo'lishi shart. Chunki guruhdagi bir nechta qatordan bitta qiymat ko'rsatish kerak: shahar nomi guruhda bitta, lekin `Summa` har xil — qaysi birini ko'rsatish noma'lum. Shuning uchun `SELECT Shahar, Summa ... GROUP BY Shahar` SQL Server'da xato beradi: «Column 'Sotuvlar.Summa' is invalid in the select list because it is not contained in either an aggregate function or the GROUP BY clause». To'g'ri: `SELECT Shahar, SUM(Summa) ... GROUP BY Shahar`. Teskarisi esa kerak emas: `GROUP BY` da bo'lgan ustunni `SELECT` da yozmaslik mumkin, lekin natijada qaysi guruh qaysi ekanini bilib bo'lmaydi. Guruhlash `NULL` qiymatlarni ham **bitta guruh** qilib birlashtiradi.

```sql
-- XATO: Summa guruhlanmagan va funksiyada emas
SELECT Shahar, Summa
FROM Sotuvlar
GROUP BY Shahar;

-- TO'G'RI
SELECT Shahar, SUM(Summa) AS Jami
FROM Sotuvlar
GROUP BY Shahar;
```

> Professional maslahat: Xato xabaridagi ustun nomiga qarang: aynan o'sha ustunni aggregatsiyaga o'rang yoki `GROUP BY` ga qo'shing.

### 3. Bir nechta ustun, WHERE va ORDER BY

`GROUP BY` da bir nechta ustunni vergul bilan yozish mumkin: guruh — ustunlar **kombinatsiyasi**. `GROUP BY Shahar, Kategoriya` — «shahar + toifa» juftlari bo'yicha guruhlar: Toshkent–Aksessuar, Toshkent–Ekran va hokazo (jami 8 guruh). `WHERE` guruhlashdan **oldin** qatorlarni filtrlaydi: `WHERE Kategoriya = N'Aksessuar' GROUP BY Shahar` faqat aksessuar sotuvlarini guruhlaydi. Tartib: `FROM` → `WHERE` → `GROUP BY` → `SELECT` → `ORDER BY`. `ORDER BY` natijani saralaydi va aggregatsiyani ham, nomni (alias) ham ishlata oladi: `ORDER BY Jami DESC`. Lekin `GROUP BY` da alias ishlamaydi: `GROUP BY Shahar` yoziladi, `GROUP BY Jami` emas. Bu `ORDER BY` `SELECT` dan keyin bajarilgani uchun mumkin.

```sql
SELECT Shahar, Kategoriya, SUM(Summa) AS Jami
FROM Sotuvlar
GROUP BY Shahar, Kategoriya
ORDER BY Shahar, Kategoriya;
-- 8 qator: Buxoro/Aksessuar 160000, Buxoro/Kompyuter 3200000, ...

SELECT Shahar, SUM(Summa) AS Jami
FROM Sotuvlar
WHERE Kategoriya = N'Aksessuar'
GROUP BY Shahar
ORDER BY Jami DESC;
-- Toshkent 280000 | Samarqand 240000 | Buxoro 160000
```

> Professional maslahat: `ORDER BY Jami DESC` — eng katta yig'indidan boshlab: «reyting» hosil qilishning eng oddiy usuli.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Shaharlar bo'yicha soni (oson)
Har bir shahar bo'yicha sotuvlar sonini chiqaring.

**Yechim:**
```sql
SELECT Shahar, COUNT(*) AS SotuvSoni
FROM Sotuvlar
GROUP BY Shahar;
```

### 2-topshiriq. Toifalar bo'yicha jami (oson)
Har bir toifa bo'yicha jami summani hisoblang.

**Yechim:**
```sql
SELECT Kategoriya, SUM(Summa) AS Jami
FROM Sotuvlar
GROUP BY Kategoriya;
```

### 3-topshiriq. Eng ko'p sotgan shahar (o'rta)
Shaharlarni jami summa bo'yicha kamayish tartibida chiqaring.

**Yechim:**
```sql
SELECT Shahar, SUM(Summa) AS Jami
FROM Sotuvlar
GROUP BY Shahar
ORDER BY Jami DESC;
```

### 4-topshiriq. Toifa statistikasi (o'rta)
Har bir toifa uchun sotuvlar soni, o'rtacha va eng katta summani chiqaring.

**Yechim:**
```sql
SELECT Kategoriya,
       COUNT(*)   AS Soni,
       AVG(Summa) AS Ortacha,
       MAX(Summa) AS EngKatta
FROM Sotuvlar
GROUP BY Kategoriya;
```

### 5-topshiriq. Shahar va toifa (qiyin)
Shahar va toifa juftligi bo'yicha jami summani chiqaring, shahar va toifa bo'yicha saralang.

**Yechim:**
```sql
SELECT Shahar, Kategoriya, SUM(Summa) AS Jami
FROM Sotuvlar
GROUP BY Shahar, Kategoriya
ORDER BY Shahar, Kategoriya;
```

### 6-topshiriq. Chegirmalar shaharlar bo'yicha (bonus)
Har bir shahar uchun nechta sotuvda chegirma borligini va chegirma yig'indisini toping.

**Yechim:**
```sql
SELECT Shahar,
       COUNT(Chegirma) AS ChegirmaBor,
       SUM(Chegirma)   AS JamiChegirma
FROM Sotuvlar
GROUP BY Shahar;
```

---

## Tezkor nazorat savollari

1. `GROUP BY` nima qiladi?
   - *Javob:* Qatorlarni ustun qiymati bo'yicha guruhlaydi, har guruh uchun bitta qator chiqaradi.
2. `SELECT` dagi ustunlar uchun qoida?
   - *Javob:* Har ustun aggregatsiya ichida yoki `GROUP BY` da bo'lishi shart.
3. `WHERE` qachon bajariladi?
   - *Javob:* Guruhlashdan oldin.
4. Ikki ustun bo'yicha guruhlash qanday yoziladi?
   - *Javob:* `GROUP BY A, B`.
5. `GROUP BY` da alias ishlaydimi?
   - *Javob:* Yo'q; alias faqat `ORDER BY` da ishlaydi.

---

## Uyga vazifa

1. Har bir shahar bo'yicha sotuvlar soni, jami summa va o'rtacha summani bitta so'rovda chiqaring; jami bo'yicha kamayish tartibida saralang.
2. Har bir toifa bo'yicha eng katta va eng kichik summani toping.
3. `Shahar, Kategoriya` bo'yicha guruhlab, sotuvlar sonini chiqaring.
4. `WHERE Sana >= '2024-03-03'` bilan shaharlar bo'yicha yig'indini hisoblang (Buxoro 3 280 000, Samarqand 2 140 000, Toshkent 3 320 000 chiqishi kerak).
5. `SELECT Shahar, Summa ... GROUP BY Shahar` xatosini yozing, xabarni o'qing va tuzating.
