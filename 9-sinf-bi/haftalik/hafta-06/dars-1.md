# 16-dars. Aggregatsiya funksiyalari: COUNT, SUM, AVG, MIN, MAX

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga aggregatsiya funksiyalarining mohiyatini (ko'p qatordan bitta natija), `COUNT(*)`, `COUNT(ustun)`, `SUM`, `AVG`, `MIN`, `MAX` funksiyalarini, ularning `NULL` bilan ishlash qoidasini, `WHERE` bilan birga qo'llanishini hamda `AVG` da butun son bo'linishi tuzog'ini o'rgatish.
- **Kutiladigan natija:** O'quvchilar aggregatsiya funksiyasi nima ekanini va nima uchun kerakligini aytadi; `COUNT(*)` va `COUNT(ustun)` farqini tushuntiradi; `SUM`, `AVG`, `MIN`, `MAX` bilan hisobot so'rovlarini yozadi; aggregatsiya `NULL` qiymatlarni o'tkazib yuborishini misolda ko'rsatadi; `AS` bilan natija ustuniga nom beradi va `WHERE` bilan filtrlaydi.
- **Vaqt taqsimoti:**
  - 15-dars: NULL, ISNULL, COALESCE: 10 daqiqa
  - Aggregatsiya g'oyasi: COUNT, SUM, AVG, MIN, MAX: 10 daqiqa
  - Sotuvlar jadvali va NULL qoidasi: 20 daqiqa
  - AVG tuzog'i, AS, WHERE bilan birga: 15 daqiqa
  - Amaliyot, xatolar, xulosa: 25 daqiqa

> Manba: o'quv dasturi — «Aggregatsiya funksiyalari: SUM, AVG, MIN, MAX, COUNT» va «NULL qiymatlar aggregatsiyada» mavzulari; 13–15-darslardagi `Mahsulotlar` jadvali. `Sotuvlar` jadvali shu dars uchun tuzilgan namuna. SQL so'rovlari SQL Server (T-SQL) sintaksisida yozilgan, hisob-kitoblar SQLite'da tekshirilgan.

---

## Mentor konspekti

### 1. Aggregatsiya funksiyalari: COUNT, SUM, AVG, MIN, MAX

Oddiy `SELECT` har bir qator uchun bitta natija qaytaradi. **Aggregatsiya funksiyasi** esa ko'p qatorni **bitta qiymatga** jamlaydi: nechta qator bor (`COUNT`), jami nechta (`SUM`), o'rtacha qancha (`AVG`), eng kichik (`MIN`) va eng katta (`MAX`). BI hisobotlarining asosi shu: «jami sotuv», «o'rtacha chek», «eng qimmat mahsulot». Namuna: `Mahsulotlar` jadvali (6 ta mahsulot). Funksiyaga ustun beriladi, natija esa bitta qatorda chiqadi. Ustun nomi chiqmasligi uchun `AS` bilan nom bering. `COUNT(*)` — barcha qatorlar soni, `SUM(Soni)` — ombordagi jami dona, `AVG(Narx)` — o'rtacha narx, `MIN`/`MAX` — eng arzon va eng qimmat narx. `MIN` va `MAX` matn va sana ustunlarida ham ishlaydi (alifbo va vaqt bo'yicha).

```sql
SELECT COUNT(*)  AS MahsulotSoni,
       SUM(Soni) AS JamiDona,
       AVG(Narx) AS OrtachaNarx,
       MIN(Narx) AS EngArzon,
       MAX(Narx) AS EngQimmat
FROM Mahsulotlar;
-- 6 | 68 | 2158333.33 | 80000 | 7500000

SELECT COUNT(*) AS AksessuarSoni
FROM Mahsulotlar
WHERE Kategoriya = N'Aksessuar';
-- 3
```

> Professional maslahat: Natijada 6 qator emas, bitta qator chiqadi. `WHERE` avval qatorlarni filtrlaydi, aggregatsiya esa faqat qolgan qatorlarni hisoblaydi.

### 2. Sotuvlar jadvali va NULL qoidasi

Keyingi darslar uchun `Sotuvlar` jadvalini ishlatamiz: 10 ta sotuv, shahar, toifa, summa, miqdor va `Chegirma` (chegirma bo'lmasa `NULL`). **Muhim qoida:** aggregatsiya funksiyalari `NULL` qiymatlarni **o'tkazib yuboradi**. Istisno — `COUNT(*)`: u qatorlarni sanaydi, ustun qiymatiga qaramaydi. `COUNT(ustun)` esa faqat `NULL` bo'lmagan qiymatlarni sanaydi. Demak 10 ta sotuvdan faqat 5 tasida chegirma bor: `COUNT(*)` = 10, `COUNT(Chegirma)` = 5. `AVG(Chegirma)` ham 5 ta qiymat bo'yicha hisoblanadi: 558 000 / 5 = 111 600. Agar `NULL` ni 0 deb hisoblasak, o'rtacha 55 800 chiqardi — bu boshqa ma'no. Qaysi variant kerakligini biznes savoliga qarab tanlang: `AVG(ISNULL(Chegirma, 0))` — barcha sotuvlar bo'yicha o'rtacha chegirma.

```sql
CREATE TABLE Sotuvlar (
    SotuvID    INT PRIMARY KEY,
    Sana       DATE,
    Shahar     NVARCHAR(20),
    Kategoriya NVARCHAR(30),
    Summa      DECIMAL(12,2),
    Miqdor     INT,
    Chegirma   DECIMAL(12,2) NULL
);
INSERT INTO Sotuvlar VALUES
 (1,  '2024-03-01', N'Toshkent',   N'Aksessuar', 160000,  2, 16000),
 (2,  '2024-03-01', N'Samarqand',  N'Kompyuter', 7500000, 1, NULL),
 (3,  '2024-03-02', N'Toshkent',   N'Ekran',     1900000, 1, 190000),
 (4,  '2024-03-02', N'Buxoro',     N'Aksessuar', 80000,   1, NULL),
 (5,  '2024-03-03', N'Samarqand',  N'Aksessuar', 240000,  2, 24000),
 (6,  '2024-03-03', N'Toshkent',   N'Kompyuter', 3200000, 1, NULL),
 (7,  '2024-03-04', N'Buxoro',     N'Kompyuter', 3200000, 1, 320000),
 (8,  '2024-03-04', N'Toshkent',   N'Aksessuar', 120000,  1, NULL),
 (9,  '2024-03-05', N'Samarqand',  N'Ekran',     1900000, 1, NULL),
 (10, '2024-03-05', N'Buxoro',     N'Aksessuar', 80000,   1, 8000);

SELECT COUNT(*)        AS Hammasi,      -- 10
       COUNT(Chegirma) AS ChegirmaBor,  -- 5
       SUM(Chegirma)   AS JamiChegirma, -- 558000
       AVG(Chegirma)   AS OrtachaChegirma  -- 111600
FROM Sotuvlar;
```

> Professional maslahat: Bu skriptni mentor darsdan oldin ishga tushirib qo'yadi. Yuqoridagi natijalarni o'quvchilar o'z ekranida solishtirsin.

### 3. AVG tuzog'i, AS va WHERE bilan birga

SQL Server'da `AVG` butun son (`INT`) ustuniga qo'llansa, natija ham **butun son** bo'ladi — kasr qismi tashlanadi. `Miqdor` ustuni `INT`: jami 12 dona, 10 sotuv, haqiqiy o'rtacha 1,2, lekin `AVG(Miqdor)` = 1 chiqadi. To'g'ri hisob uchun qiymatni `DECIMAL` ga o'tkazing: `AVG(CAST(Miqdor AS DECIMAL(10,2)))` yoki `AVG(Miqdor * 1.0)`. Narx va summa ustunlari `DECIMAL` bo'lgani uchun ularda bu muammo yo'q. Ikkinchi tuzoq: aggregatsiya funksiyasini `WHERE` ichida yozib bo'lmaydi (`WHERE SUM(Summa) > 100` — xato). Shart bilan filtrlash uchun `WHERE` ni qatorlarga qo'llang va aggregatsiyani `SELECT` da yozing: `SELECT SUM(Summa) FROM Sotuvlar WHERE Shahar = N'Toshkent'` — 5 380 000. Uchinchi tuzoq: `SELECT Shahar, SUM(Summa)` kabi aggregatsiyasiz ustunni funksiya bilan aralashtirib yozib bo'lmaydi — buning uchun keyingi darsda `GROUP BY` o'rganiladi.

```sql
SELECT AVG(Miqdor)                       AS ButunOrtacha,  -- 1
       AVG(CAST(Miqdor AS DECIMAL(10,2))) AS HaqiqiyOrtacha -- 1.200000
FROM Sotuvlar;

SELECT COUNT(*)   AS Soni,   -- 4
       SUM(Summa) AS Jami    -- 5380000
FROM Sotuvlar
WHERE Shahar = N'Toshkent';

SELECT MIN(Sana) AS Birinchi, MAX(Sana) AS Oxirgi
FROM Sotuvlar;              -- 2024-03-01 | 2024-03-05
```

> Professional maslahat: Sana va matn ustunlarida `MIN`/`MAX` ham ishlaydi, `SUM` va `AVG` esa faqat sonli ustunlarda.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Sotuvlar soni (oson)
Sotuvlar jadvalidagi barcha qatorlar sonini toping.

**Yechim:**
```sql
SELECT COUNT(*) AS SotuvSoni
FROM Sotuvlar;
```

### 2-topshiriq. Jami summa (oson)
Barcha sotuvlarning jami summasini hisoblang.

**Yechim:**
```sql
SELECT SUM(Summa) AS JamiSumma
FROM Sotuvlar;
```

### 3-topshiriq. Narx chegaralari (o'rta)
Mahsulotlardagi eng arzon va eng qimmat narxni bitta so'rovda chiqaring.

**Yechim:**
```sql
SELECT MIN(Narx) AS EngArzon,
       MAX(Narx) AS EngQimmat
FROM Mahsulotlar;
```

### 4-topshiriq. Toshkent hisoboti (o'rta)
Toshkentdagi sotuvlar soni va yig'indisini chiqaring.

**Yechim:**
```sql
SELECT COUNT(*)   AS Soni,
       SUM(Summa) AS Jami
FROM Sotuvlar
WHERE Shahar = N'Toshkent';
```

### 5-topshiriq. Chegirma tahlili (qiyin)
Nechta sotuvda chegirma borligini va o'rtacha chegirmani toping; so'ng NULL ni 0 deb hisoblab, barcha sotuvlar bo'yicha o'rtachani hisoblang.

**Yechim:**
```sql
SELECT COUNT(Chegirma)             AS ChegirmaBor,
       AVG(Chegirma)               AS OrtachaBor,
       AVG(ISNULL(Chegirma, 0))    AS OrtachaHammasi
FROM Sotuvlar;
```

### 6-topshiriq. Ombor qiymati (bonus)
Ombordagi barcha mahsulotlar qiymatini (Narx × Soni yig'indisi) hisoblang.

**Yechim:**
```sql
SELECT SUM(Narx * Soni) AS OmborQiymati
FROM Mahsulotlar;
```

---

## Tezkor nazorat savollari

1. Aggregatsiya funksiyasi nima qiladi?
   - *Javob:* Ko'p qatorni bitta qiymatga jamlaydi.
2. `COUNT(*)` va `COUNT(ustun)` farqi?
   - *Javob:* `COUNT(*)` barcha qatorni, `COUNT(ustun)` esa faqat NULL bo'lmagan qiymatlarni sanaydi.
3. Aggregatsiya NULL qiymatlarni qanday qabul qiladi?
   - *Javob:* O'tkazib yuboradi (`COUNT(*)` dan tashqari).
4. `MIN` va `MAX` qaysi turlarda ishlaydi?
   - *Javob:* Son, matn va sana ustunlarida.
5. `INT` ustunida `AVG` nima uchun butun chiqadi?
   - *Javob:* SQL Server butun turdagi natija qaytaradi; `CAST AS DECIMAL` kerak.

---

## Uyga vazifa

1. `Mahsulotlar` bo'yicha: mahsulotlar soni, jami dona, eng arzon va eng qimmat narx, o'rtacha narx — bitta so'rovda, har bir ustunga nom bering.
2. `Sotuvlar` bo'yicha Buxorodagi sotuvlar soni va yig'indisini toping.
3. `COUNT(*)` va `COUNT(Chegirma)` ni bitta so'rovda chiqaring; farqini yozma izohlang.
4. `AVG(Miqdor)` va `AVG(CAST(Miqdor AS DECIMAL(10,2)))` natijalarini solishtiring va nima uchun farq qilishini tushuntiring.
