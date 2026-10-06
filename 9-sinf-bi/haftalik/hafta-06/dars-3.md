# 18-dars. HAVING filtrlash operatori (WHERE vs HAVING)

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga `HAVING` yordamida guruhlangan natijalarni aggregatsiya bo'yicha filtrlashni, `WHERE` va `HAVING` farqini, so'rovning mantiqiy bajarilish tartibini (`FROM` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY`) hamda ikkala filtrni bitta so'rovda birga qo'llashni o'rgatish.
- **Kutiladigan natija:** O'quvchilar `WHERE` va `HAVING` farqini tushuntiradi; `HAVING SUM(...)`, `HAVING COUNT(*)` bilan guruhlarni filtrlaydi; so'rovning mantiqiy bajarilish tartibini aytadi; `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY` ni bitta so'rovda to'g'ri tartibda yozadi; qaysi shartni `WHERE` ga, qaysini `HAVING` ga yozishni asoslaydi.
- **Vaqt taqsimoti:**
  - 17-dars: GROUP BY, SELECT qoidasi: 10 daqiqa
  - HAVING g'oyasi: guruhlarni filtrlash: 10 daqiqa
  - WHERE va HAVING farqi, bajarilish tartibi: 20 daqiqa
  - Birga qo'llash, samaradorlik: 15 daqiqa
  - Amaliyot, xatolar, xulosa: 25 daqiqa

> Manba: o'quv dasturi — «HAVING: guruhlangan natijalarni filtrlash», «WHERE va HAVING farqi» va «WHERE + GROUP BY + HAVING birga» mavzulari; 16–17-darslardagi `Sotuvlar` jadvali. So'rovlar SQL Server (T-SQL) sintaksisida, natijalar SQLite'da tekshirilgan.

---

## Mentor konspekti

### 1. HAVING: guruhlangan natijani filtrlash

`WHERE` aggregatsiya funksiyasini ishlata olmaydi, chunki u guruhlar hosil bo'lishidan **oldin** ishlaydi. Guruhlar tayyor bo'lgandan keyin ularni filtrlash uchun `HAVING` bor. `HAVING` shartida aggregatsiya funksiyasi yoziladi: `HAVING SUM(Summa) > 4000000` — «jami summasi 4 mln dan katta guruhlar». Joyi: `GROUP BY` dan **keyin**, `ORDER BY` dan oldin. Misol: shaharlar jami summasi — Samarqand 9 640 000, Toshkent 5 380 000, Buxoro 3 360 000. `HAVING SUM(Summa) > 4000000` Buxoroni olib tashlaydi, 2 qator qoladi. `HAVING COUNT(*) >= 4` esa faqat Toshkentni qoldiradi (4 ta sotuv). Xato misol: `WHERE SUM(Summa) > 4000000` — SQL Server «An aggregate may not appear in the WHERE clause» xatosini beradi.

```sql
SELECT Shahar, SUM(Summa) AS Jami
FROM Sotuvlar
GROUP BY Shahar
HAVING SUM(Summa) > 4000000;
-- Samarqand | 9640000
-- Toshkent  | 5380000

SELECT Shahar, COUNT(*) AS SotuvSoni
FROM Sotuvlar
GROUP BY Shahar
HAVING COUNT(*) >= 4;
-- Toshkent | 4
```

> Professional maslahat: `HAVING` da `SELECT` dagi alias ishlamaydi (T-SQL'da): `HAVING Jami > 4000000` xato, funksiyani qayta yozing.

### 2. WHERE va HAVING farqi, bajarilish tartibi

**WHERE** — alohida **qatorlarni** guruhlashdan oldin filtrlaydi, aggregatsiya funksiyasini ishlata olmaydi. **HAVING** — **guruhlarni** guruhlashdan keyin filtrlaydi, aggregatsiya funksiyasini ishlatadi. Mantiqiy bajarilish tartibi: 1) `FROM`, 2) `WHERE`, 3) `GROUP BY`, 4) `HAVING`, 5) `SELECT`, 6) `ORDER BY`. Shuning uchun `WHERE` va `HAVING` bir so'rovda birga yashaydi: `WHERE Kategoriya <> N'Ekran'` avval ekran sotuvlarini olib tashlaydi, `GROUP BY Shahar` guruhlaydi, `HAVING SUM(Summa) > 3500000` esa kichik guruhlarni tashlaydi. Natija: Samarqand 7 740 000 (Ekran sotuvi olingach 9 640 000 − 1 900 000). Qoida: **qator shartini** (`Shahar = ...`, `Sana >= ...`) iloji boricha `WHERE` ga yozing — kamroq qator guruhlanadi va so'rov tezroq ishlaydi; **guruh shartini** (`SUM`, `COUNT`, `AVG`) `HAVING` ga yozing.

```sql
SELECT Shahar, SUM(Summa) AS Jami
FROM Sotuvlar
WHERE Kategoriya <> N'Ekran'
GROUP BY Shahar
HAVING SUM(Summa) > 3500000
ORDER BY SUM(Summa) DESC;
-- Samarqand | 7740000

-- Qator sharti WHERE ga:
SELECT Shahar, SUM(Summa) AS Jami
FROM Sotuvlar
WHERE Shahar = N'Toshkent'
GROUP BY Shahar;
```

> Professional maslahat: Eslab qoling: WHERE — «qaysi qatorlar?», HAVING — «qaysi guruhlar?».

### 3. HAVING bilan amaliy hisobotlar

`HAVING` ko'pincha biznes savollarida uchraydi: «kamida 2 ta sotuvi bo'lgan shahar+toifa juftliklari», «o'rtacha chegi 2 mln dan oshgan toifalar». `HAVING` ichida bir nechta shart `AND`/`OR` bilan birlashadi: `HAVING COUNT(*) >= 2 AND SUM(Summa) > 200000`. Ikki ustun bo'yicha guruhlab `HAVING COUNT(*) > 1` qilsak, ikki yoki undan ko'p sotuvi bor juftliklar qoladi: Buxoro–Aksessuar (2) va Toshkent–Aksessuar (2). O'rtacha bo'yicha: `HAVING AVG(Summa) > 2000000` faqat Kompyuter toifasini qoldiradi (≈ 4 633 333,33). `HAVING` guruhlanmagan so'rovda ham yozilishi mumkin, lekin amalda deyarli doim `GROUP BY` bilan birga ishlatiladi. Xato: `HAVING` ga qator ustunini (guruhlanmagan) yozish, masalan `HAVING Summa > 100000`: `Summa` guruhlanmagan va aggregatsiyada emas.

```sql
SELECT Shahar, Kategoriya, COUNT(*) AS Soni
FROM Sotuvlar
GROUP BY Shahar, Kategoriya
HAVING COUNT(*) > 1;
-- Buxoro  | Aksessuar | 2
-- Toshkent| Aksessuar | 2

SELECT Kategoriya, AVG(Summa) AS Ortacha
FROM Sotuvlar
GROUP BY Kategoriya
HAVING AVG(Summa) > 2000000;
-- Kompyuter | 4633333.33
```

> Professional maslahat: Savol so'zlariga e'tibor bering: «har bir qator ...» → WHERE; «jami / o'rtacha / soni ... bo'lgan guruhlar» → HAVING.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Katta shaharlar (oson)
Jami summasi 4 000 000 dan oshgan shaharlarni chiqaring.

**Yechim:**
```sql
SELECT Shahar, SUM(Summa) AS Jami
FROM Sotuvlar
GROUP BY Shahar
HAVING SUM(Summa) > 4000000;
```

### 2-topshiriq. Ko'p sotuvli shaharlar (oson)
Kamida 4 ta sotuvi bo'lgan shaharni toping.

**Yechim:**
```sql
SELECT Shahar, COUNT(*) AS SotuvSoni
FROM Sotuvlar
GROUP BY Shahar
HAVING COUNT(*) >= 4;
```

### 3-topshiriq. Qimmat toifa (o'rta)
O'rtacha summasi 2 000 000 dan oshgan toifalarni chiqaring.

**Yechim:**
```sql
SELECT Kategoriya, AVG(Summa) AS Ortacha
FROM Sotuvlar
GROUP BY Kategoriya
HAVING AVG(Summa) > 2000000;
```

### 4-topshiriq. Takroriy juftliklar (o'rta)
Shahar va toifa juftligi bo'yicha 1 dan ko'p sotuvi bor guruhlarni toping.

**Yechim:**
```sql
SELECT Shahar, Kategoriya, COUNT(*) AS Soni
FROM Sotuvlar
GROUP BY Shahar, Kategoriya
HAVING COUNT(*) > 1;
```

### 5-topshiriq. WHERE va HAVING birga (qiyin)
Ekran sotuvlarisiz, jami 3 500 000 dan oshgan shaharlarni jami bo'yicha kamayish tartibida chiqaring.

**Yechim:**
```sql
SELECT Shahar, SUM(Summa) AS Jami
FROM Sotuvlar
WHERE Kategoriya <> N'Ekran'
GROUP BY Shahar
HAVING SUM(Summa) > 3500000
ORDER BY Jami DESC;
```

### 6-topshiriq. Xatoni tuzating (bonus)
`WHERE SUM(Summa) > 4000000` so'rovini to'g'rilab, nima uchun xato ekanini yozing.

**Yechim:**
```sql
-- Aggregatsiya `WHERE` da yozilmaydi — u guruhlashdan oldin ishlaydi. Shart `GROUP BY` dan keyin `HAVING SUM(Summa) > 4000000` ko'rinishida yoziladi.
```

---

## Tezkor nazorat savollari

1. `WHERE` va `HAVING` farqi?
   - *Javob:* `WHERE` qatorlarni guruhlashdan oldin, `HAVING` guruhlarni guruhlashdan keyin filtrlaydi.
2. Aggregatsiya sharti qayerda yoziladi?
   - *Javob:* `HAVING` da.
3. Mantiqiy bajarilish tartibi?
   - *Javob:* FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY.
4. Qator shartini qayerga yozish yaxshi?
   - *Javob:* `WHERE` ga — kamroq qator guruhlanadi.
5. `HAVING` qayerga yoziladi?
   - *Javob:* `GROUP BY` dan keyin, `ORDER BY` dan oldin.

---

## Uyga vazifa

1. Jami summasi 5 000 000 dan oshgan shaharlarni toping (Samarqand va Toshkent chiqishi kerak).
2. Kamida 3 ta sotuvi bo'lgan toifalarni toping va sotuvlar sonini chiqaring.
3. Aksessuar sotuvlari bo'yicha shaharlar jamini hisoblab, 200 000 dan oshganlarini qoldiring (Toshkent 280 000, Samarqand 240 000).
4. So'rovning mantiqiy bajarilish tartibini o'z so'zlaringiz bilan 6 qadamda yozing.
5. `WHERE SUM(Summa) > 4000000` so'rovidagi xatoni tushuntiring va to'g'rilang.
