# 15-dars. SQL asoslari: NULL qiymatlar bilan ishlash va ma'lumot turlari

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarni `NULL` ning ma'nosi (qiymat yo'q), `IS NULL` / `IS NOT NULL` bilan tekshirish, `ISNULL` va `COALESCE` bilan almashtirish, uch qiymatli mantiq tuzoqlari hamda asosiy SQL Server ma'lumot turlari (`INT`, `DECIMAL`, `NVARCHAR`, `DATE`, `BIT`) va `CAST` bilan tanishtirish.
- **Kutiladigan natija:** O'quvchilar `NULL` ni `0` va bo'sh matndan farqlaydi; `IS NULL` va `IS NOT NULL` bilan to'g'ri filtrlaydi; `ISNULL` va `COALESCE` bilan NULL ni almashtiradi; ustun uchun mos ma'lumot turini tanlaydi va `CAST` ni qo'llaydi.
- **Vaqt taqsimoti:**
  - O'tgan darsni takrorlash (`ORDER BY`, `TOP`, `OFFSET–FETCH`): 10 daqiqa
  - Yangi mavzu: `NULL` va `IS NULL`: 10 daqiqa
  - `ISNULL`, `COALESCE` va NULL tuzoqlari: 20 daqiqa
  - Ma'lumot turlari va `CAST`: 15 daqiqa
  - Amaliyot (`Mijozlar` jadvalida 8–10 ta so'rov), nazorat va xulosa: 25 daqiqa

> Manba: o'quv dasturi — «SQL asoslari: SELECT, WHERE, ORDER BY» moduli; o'quv qo'llanma — «NULL qiymatlarni boshqarish (ISNULL, COALESCE)» va «Cheklovlar» bo'limlari; uslubiy ko'rsatma.

---

## Mentor konspekti

### 1. `NULL` va `IS NULL`

`NULL` — «qiymat yo'q yoki noma'lum». U `0` ham, bo'sh matn `''` ham, `false` ham emas. `NULL` ni `=` bilan tekshirib bo'lmaydi: `Telefon = NULL` hech qachon `TRUE` bo'lmaydi. Buning uchun `IS NULL` va `IS NOT NULL` ishlatiladi. Quyida `Mijozlar` jadvali: Ali, Sana, Jasur telefoni bor; Vali va Dilnozada `NULL`.

```sql
SELECT Ism FROM Mijozlar
WHERE Telefon IS NULL;

SELECT Ism FROM Mijozlar
WHERE Telefon IS NOT NULL;

SELECT Ism FROM Mijozlar
WHERE Telefon = NULL;
```

`Mijozlar` jadvali: `MijozID INT`, `Ism NVARCHAR(30)`, `Telefon NVARCHAR(15) NULL`, `Email NVARCHAR(50) NULL`, `RoyxatSana DATE`, `Faol BIT`. Qatorlar: Ali (901234567, ali@mail.uz), Vali (NULL, vali@gmail.com), Sana (935551122, NULL), Dilnoza (NULL, NULL), Jasur (977778899, jasur@gmail.com).

> Professional maslahat: `IS NULL` — Vali, Dilnoza (2 qator). `IS NOT NULL` — Ali, Sana, Jasur (3 qator). `= NULL` — 0 qator!

### 2. `ISNULL`, `COALESCE` va NULL tuzoqlari

`ISNULL(ifoda, almashtiruvchi)` SQL Server ga xos, ikki parametrli. `COALESCE(a, b, c, ...)` SQL standarti: birinchi `NULL` bo'lmagan qiymatni qaytaradi, istalgancha parametr qabul qiladi. Tuzoqlar: `NULL` qatnashgan arifmetika natijasi `NULL` (`5 + NULL`); `NULL` bilan `<>` taqqoslash ham qatorni olib tashlaydi, chunki natija `TRUE` emas.

```sql
SELECT Ism,
       ISNULL(Telefon, N'Yo''q') AS Tel,
       COALESCE(Telefon, Email, N'Aloqa yo''q') AS Aloqa
FROM Mijozlar;

SELECT Ism FROM Mijozlar
WHERE Telefon <> N'901234567';
```

> Professional maslahat: Ikkinchi so'rov faqat Sana va Jasur ni qaytaradi: `NULL` telefonli Vali va Dilnoza ham chiqmaydi. Ularni ham olish uchun `OR Telefon IS NULL` qo'shing.

### 3. Ma'lumot turlari va `CAST`

Har bir ustun ma'lumot turiga ega. Asosiylari (SQL Server): `INT` / `BIGINT` — butun son; `DECIMAL(p, s)` — aniq o'nlik son (pul uchun); `FLOAT` — taxminiy son; `NVARCHAR(n)` — unicode matn; `DATE` / `DATETIME2` — sana va vaqt; `BIT` — mantiqiy (0/1). Turni o'zgartirish uchun `CAST(ifoda AS tur)`. Butun sonlarni bo'lishda `7 / 2 = 3`: kasr kerak bo'lsa `DECIMAL` yoki `CAST` ishlating.

```sql
SELECT Ism, RoyxatSana
FROM Mijozlar
WHERE RoyxatSana >= '2025-01-01';

SELECT Ism FROM Mijozlar
WHERE Faol = 1;

SELECT CAST(7 AS DECIMAL(5,2)) / 2 AS Natija,
       CAST(Narx AS INT) AS ButunNarx
FROM Mahsulotlar;
```

> Professional maslahat: Sana `YYYY-MM-DD` formatida yoziladi. `RoyxatSana >= '2025-01-01'` — Sana, Dilnoza, Jasur. `Faol = 1` — Ali, Vali, Dilnoza. `CAST(7 AS DECIMAL(5,2)) / 2` natijasi 3.50.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. NULL telefonlar (oson)
Telefoni kiritilmagan mijozlarni toping.

**Yechim:**
```sql
SELECT Ism
FROM Mijozlar
WHERE Telefon IS NULL;
-- Vali, Dilnoza
```

### 2-topshiriq. Aloqa bor mijozlar (oson)
Telefoni bor mijozlarni `IS NOT NULL` bilan chiqaring.

**Yechim:**
```sql
SELECT Ism, Telefon
FROM Mijozlar
WHERE Telefon IS NOT NULL;
-- Ali, Sana, Jasur
```

### 3-topshiriq. Almashtirish (o'rta)
Har bir mijoz uchun telefonni, telefon yo'q bo'lsa emailni, ikkalasi ham yo'q bo'lsa «Aloqa yo'q» matnini chiqaring.

**Yechim:**
```sql
SELECT Ism,
       COALESCE(Telefon, Email, N'Aloqa yo''q') AS Aloqa
FROM Mijozlar;
```

### 4-topshiriq. Tuzoqni toping (qiyin)
`WHERE Telefon <> N'901234567'` nechta qator beradi? Nega Vali va Dilnoza chiqmaydi? Ularni ham olish uchun so'rovni tuzating.

**Yechim:**
```sql
-- 2 qator: Sana, Jasur (NULL bilan <> natijasi TRUE emas)
SELECT Ism FROM Mijozlar
WHERE Telefon <> N'901234567' OR Telefon IS NULL;
-- 4 qator: Vali, Sana, Dilnoza, Jasur
```

### 5-topshiriq. Turlar va CAST (bonus)
2025-yildan keyin ro'yxatdan o'tgan faol mijozlar ismini chiqaring va `Mahsulotlar` narxini `CAST` bilan butun songa aylantiring.

**Yechim:**
```sql
SELECT Ism FROM Mijozlar
WHERE RoyxatSana >= '2025-01-01' AND Faol = 1;
-- Dilnoza

SELECT Nomi, CAST(Narx AS INT) AS ButunNarx
FROM Mahsulotlar;
```

---

## Tezkor nazorat savollari

1. `NULL` nimani anglatadi?
   - *Javob:* Qiymat yo'qligi yoki noma'lumligini; u `0` ham, bo'sh matn ham emas.
2. `Telefon = NULL` nega ishlamaydi?
   - *Javob:* `NULL` bilan taqqoslash `TRUE` bermaydi; `IS NULL` ishlatiladi.
3. `ISNULL` va `COALESCE` farqi?
   - *Javob:* `ISNULL` SQL Server ga xos va ikki parametrli; `COALESCE` standart va ko'p parametrli.
4. `5 + NULL` nimaga teng?
   - *Javob:* `NULL`.
5. Pul miqdori uchun qaysi tur mos?
   - *Javob:* `DECIMAL(p, s)`.

---

## Uyga vazifa

`Dokon` bazasiga `Mijozlar` jadvalini (`MijozID`, `Ism`, `Telefon`, `Email`, `RoyxatSana`, `Faol`) yarating, 8 ta mijoz kiriting (kamida 3 tasida `NULL`). 8 ta so'rov yozing: `IS NULL`, `IS NOT NULL`, `ISNULL`, `COALESCE`, sana bo'yicha filtr, `BIT` bo'yicha filtr, `CAST`, hamda `<>` tuzog'ini ko'rsatuvchi so'rov.
