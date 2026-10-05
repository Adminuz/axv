# 12-dars. SQL asoslari: SELECT, ustunlar va sodda ifodalar

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarni SQL tilining vazifasi, qisqa tarixi va buyruq toifalari (DDL, DML, DQL, DCL, TCL) bilan tanishtirish; `SELECT ... FROM` yordamida barcha yoki tanlangan ustunlarni olish, `AS` taxalluslari (alias), arifmetik va matnli ifodalar, `DISTINCT` va `TOP` ni amalda qo'llashni o'rgatish.
- **Kutiladigan natija:** O'quvchilar SQL ning deklarativ til ekanini tushuntiradi; buyruqni to'g'ri toifaga ajratadi; SSMS da `SELECT *` va ustunli `SELECT` so'rovlarini yozadi; hisoblangan ustun (masalan, `Narx * Soni AS Summa`) va takrorsiz ro'yxat (`DISTINCT`) oladi; so'rov natijasini oldindan bashorat qila oladi.
- **Vaqt taqsimoti:**
  - O'tgan darsni takrorlash (RDBMS, cheklovlar): 10 daqiqa
  - Yangi mavzu: SQL tarixi va buyruq toifalari: 10 daqiqa
  - SELECT, FROM, ustunlar, AS: 20 daqiqa
  - Sodda ifodalar, DISTINCT, TOP: 15 daqiqa
  - Amaliyot (namuna bazada 8–10 ta so'rov), nazorat va xulosa: 25 daqiqa

> Manba: o'quv dasturi — «SQL asoslari: SELECT, WHERE, ORDER BY» moduli («SQL tilining vazifasi va qo'llanilish sohasi. SELECT operatori orqali ma'lumot tanlash...»); o'quv qo'llanma — SQL tarixi (1970 Codd, 1974 SEQUEL, 1986 ANSI), buyruq toifalari, «Ma'lumotni tanlash (SELECT)», DISTINCT, NULL, SELECT TOP bo'limlari. Modul 3 darsga bo'lingan: bu darsda SELECT va ifodalar, 13-darsda WHERE va mantiqiy operatorlar, keyin ORDER BY.

---

## Mentor konspekti

### 1. SQL nima?

**SQL (Structured Query Language — tuzilmali so'rovlar tili)** — relatsion ma'lumotlar bazalari bilan ishlash uchun standart til. SQL **deklarativ**: siz «**nimani** olish kerak» deb aytasiz, «**qanday** topish kerak» ni DBMS o'zi hal qiladi.

Qisqa tarix (o'quv qo'llanma bo'yicha):
- 1970 — Edgar F. Codd relatsion modelni e'lon qildi;
- 1974 — IBM da D. Chamberlin va R. Boyce SEQUEL tilini yaratdi (keyin nomi SQL ga o'zgardi);
- 1979 — Oracle birinchi tijoriy SQL tizimini chiqardi;
- 1986–1987 — ANSI va ISO standarti;
- hozir — dialektlar: T-SQL (SQL Server), PL/SQL (Oracle), PostgreSQL SQL.

### 2. SQL buyruq toifalari

| Toifa | To'liq nomi | Buyruqlar | Vazifasi |
|---|---|---|---|
| **DDL** | Data Definition Language | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` | Tuzilmani yaratadi/o'zgartiradi (11-darsdagi `CREATE TABLE`) |
| **DML** | Data Manipulation Language | `INSERT`, `UPDATE`, `DELETE` | Jadval ichidagi ma'lumotni o'zgartiradi |
| **DQL** | Data Query Language | `SELECT` | Ma'lumotni **o'qiydi** — o'zgartirmaydi |
| **DCL** | Data Control Language | `GRANT`, `REVOKE` | Foydalanuvchi huquqlari |
| **TCL** | Transaction Control Language | `COMMIT`, `ROLLBACK` | Tranzaksiyalarni boshqarish |

BI analitigi kunining ko'p qismini **DQL** — `SELECT` bilan o'tkazadi. `SELECT` ma'lumotni o'zgartirmaydi, shuning uchun uni o'rganish xavfsiz.

### 3. Namuna jadval

Dars davomida `Dokon` bazasidagi `Mahsulotlar` jadvalidan foydalanamiz (mentor oldindan yaratib qo'yadi):

```sql
CREATE TABLE Mahsulotlar (
    MahsulotID INT PRIMARY KEY,
    Nomi       NVARCHAR(50) NOT NULL,
    Kategoriya NVARCHAR(30),
    Narx       DECIMAL(12,2),
    Soni       INT
);
INSERT INTO Mahsulotlar VALUES
 (1, N'Sichqoncha', N'Aksessuar', 80000,  25),
 (2, N'Klaviatura', N'Aksessuar', 150000, 12),
 (3, N'Monitor',    N'Ekran',     1900000, 4),
 (4, N'Noutbuk',    N'Kompyuter', 7500000, 3),
 (5, N'Quloqchin',  N'Aksessuar', 120000, 18),
 (6, N'Planshet',   N'Kompyuter', 3200000, 6);
```

### 4. SELECT * — barcha ustunlar

```sql
SELECT *
FROM Mahsulotlar;
```

- `SELECT` — **nimani** olamiz; `*` — barcha ustunlar.
- `FROM` — **qayerdan** (qaysi jadvaldan).
- `;` — buyruq oxiri (SQL Server da ko'pincha ixtiyoriy, lekin yozish odati yaxshi).
- SQL kalit so'zlari katta-kichik harfni farqlamaydi (`select` = `SELECT`), lekin kalit so'zlarni KATTA harfda yozish — umumiy odat.

> Professional maslahat: katta jadvallarda `SELECT *` sekin va ortiqcha; hisobotlarda faqat kerakli ustunlarni tanlang.

### 5. Kerakli ustunlarni tanlash

```sql
SELECT Nomi, Narx
FROM Mahsulotlar;
```

Natija — faqat 2 ta ustun, 6 ta qator. Ustunlar **siz yozgan tartibda** chiqadi: `SELECT Narx, Nomi` yozsangiz, avval narx.

### 6. AS — taxallus (alias)

```sql
SELECT Nomi AS Mahsulot,
       Narx AS [Narx (so'm)]
FROM Mahsulotlar;
```

- `AS` natijadagi ustun nomini o'zgartiradi (jadvaldagi asl nom o'zgarmaydi).
- Bo'sh joy yoki maxsus belgi bo'lsa, SQL Server da nom `[...]` ichida yoziladi (standart SQL da `"..."`).

### 7. Sodda ifodalar: hisoblangan ustunlar

`SELECT` ichida arifmetik amallar (`+ - * /`) ishlatish mumkin:

```sql
SELECT Nomi,
       Narx,
       Soni,
       Narx * Soni         AS OmborQiymati,
       Narx * 1.12         AS QQS_bilan,
       Narx - Narx * 0.10  AS Chegirma10
FROM Mahsulotlar;
```

| Nomi | Narx | Soni | OmborQiymati | QQS_bilan | Chegirma10 |
|---|---|---|---|---|---|
| Sichqoncha | 80000 | 25 | 2000000 | 89600 | 72000 |
| Klaviatura | 150000 | 12 | 1800000 | 168000 | 135000 |
| Monitor | 1900000 | 4 | 7600000 | 2128000 | 1710000 |
| … | | | | | |

(QQS — 12%, O'zbekiston uchun amaldagi stavka; natijada ko'proq kasr xonalar ko'rinishi mumkin.)

Butun sonlarni bo'lishda ehtiyot bo'ling: SQL Server da `7 / 2 = 3` (butun bo'linma), `7 / 2.0 = 3.5`.

**Matnli ifoda** (birlashtirish):

```sql
SELECT Nomi + N' (' + Kategoriya + N')' AS ToliqNom
FROM Mahsulotlar;
-- Sichqoncha (Aksessuar)
```

Universal variant: `CONCAT(Nomi, N' (', Kategoriya, N')')` — NULL qiymatlarda ham xato bermaydi.

### 8. DISTINCT — takrorsiz qiymatlar

```sql
SELECT DISTINCT Kategoriya
FROM Mahsulotlar;
-- Aksessuar, Ekran, Kompyuter (3 ta qator, 6 ta emas)
```

BI da `DISTINCT` kategoriyalar, shaharlar, mijoz segmentlari ro'yxatini olishda ishlatiladi.

### 9. TOP — birinchi N qator

```sql
SELECT TOP 3 Nomi, Narx
FROM Mahsulotlar;
```

SQL Server da `TOP`; PostgreSQL/MySQL/SQLite da: `SELECT Nomi, Narx FROM Mahsulotlar LIMIT 3;`. Tartibsiz `TOP` qaysi 3 qatorni berishi kafolatlanmaydi — «eng qimmat 3 ta» uchun keyingi darslarda `ORDER BY` qo'shamiz.

### 10. NULL haqida qisqacha

**NULL** — «qiymat yo'q / noma'lum». U `0` ham, bo'sh matn `''` ham emas. Har qanday arifmetik amalda NULL qatnashsa, natija ham NULL: `NULL * 5 = NULL`. (NULL ni filtrlash — `IS NULL` — 13-darsda.)

### 11. So'rovning mantiqiy tartibi

Yozilish tartibi: `SELECT ... FROM ...`. Bajarilish tartibi: avval `FROM` (jadval topiladi), keyin `SELECT` (ustunlar va ifodalar hisoblanadi). Shu sababli keyingi darslarda `WHERE` `FROM` dan keyin qo'shiladi.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Buyruq toifasi (oson)
Toifasini aniqlang: `SELECT`, `CREATE TABLE`, `INSERT`, `GRANT`, `ROLLBACK`, `DROP`, `UPDATE`.

**Yechim:**
`SELECT` — DQL; `CREATE TABLE`, `DROP` — DDL; `INSERT`, `UPDATE` — DML; `GRANT` — DCL; `ROLLBACK` — TCL.

### 2-topshiriq. Ustunlarni tanlash va taxallus (oson)
`Mahsulotlar` jadvalidan mahsulot nomi va kategoriyasini `Mahsulot` va `Turi` sarlavhalari bilan chiqaring.

**Yechim:**
```sql
SELECT Nomi AS Mahsulot,
       Kategoriya AS Turi
FROM Mahsulotlar;
```

### 3-topshiriq. Hisoblangan ustunlar (o'rta)
Har bir mahsulot uchun: nomi, ombordagi umumiy qiymati (`Narx * Soni`) va 15% chegirmali narxini chiqaring. Ustunlarga ma'noli nom bering.

**Yechim:**
```sql
SELECT Nomi,
       Narx * Soni        AS OmborQiymati,
       Narx * 0.85        AS Chegirma15
FROM Mahsulotlar;
```
Tekshirish: Sichqoncha uchun 2000000 va 68000; Noutbuk uchun 22500000 va 6375000.

### 4-topshiriq. Natijani bashorat qiling (qiyin)
So'rovlarni bajarmasdan natijani yozing, so'ng SSMS da tekshiring:
```sql
SELECT DISTINCT Kategoriya FROM Mahsulotlar;   -- (a) nechta qator?
SELECT TOP 2 Nomi FROM Mahsulotlar;            -- (b) nechta ustun, nechta qator?
SELECT 7 / 2 AS A, 7 / 2.0 AS B;               -- (c) A va B?
SELECT Nomi + N' - ' + Kategoriya FROM Mahsulotlar;  -- (d) ustun nomi qanday?
```

**Yechim:**
(a) 3 qator (Aksessuar, Ekran, Kompyuter); (b) 1 ustun, 2 qator (qaysi ikkitasi — kafolatlanmagan, odatda PK tartibida); (c) A = 3, B = 3.5 (aniqrog'i `3.500000`); (d) taxallus berilmagani uchun ustun nomi `(No column name)` — shuning uchun hisoblangan ustunlarga doim `AS` bering.

### 5-topshiriq. BI savoliga javob (bonus)
Rahbar so'radi: «Har bir mahsulot ombordagi qiymati bilan, mahsulot nomi va kategoriyasi bitta ustunda bo'lsin.» Bitta so'rov yozing.

**Yechim:**
```sql
SELECT CONCAT(Nomi, N' (', Kategoriya, N')') AS Mahsulot,
       Narx * Soni AS [Ombor qiymati]
FROM Mahsulotlar;
```

---

## Tezkor nazorat savollari

1. SQL nega deklarativ til deyiladi?
   - *Javob:* Unda «qanday» emas, «nimani olish kerak» yoziladi; bajarish yo'lini DBMS tanlaydi.
2. `SELECT` qaysi toifaga kiradi va ma'lumotni o'zgartiradimi?
   - *Javob:* DQL; yo'q, faqat o'qiydi.
3. `SELECT *` va `SELECT Nomi, Narx` farqi nima?
   - *Javob:* Birinchisi barcha ustunlarni, ikkinchisi faqat ko'rsatilgan ustunlarni shu tartibda qaytaradi.
4. `AS` nima qiladi?
   - *Javob:* Natijadagi ustunga vaqtinchalik nom (taxallus) beradi; jadvaldagi asl nom o'zgarmaydi.
5. `DISTINCT` nima uchun kerak?
   - *Javob:* Takrorlanuvchi qiymatlarni olib tashlab, noyob qiymatlar ro'yxatini olish uchun.

---

## Uyga vazifa

`Dokon` bazasidagi `Mahsulotlar` jadvaliga kamida 4 ta yangi mahsulot qo'shing (jami 10 ta) va 6 ta `SELECT` so'rovini yozing: barcha ustunlar; 2 ta ustun taxallus bilan; ombor qiymati; QQS bilan narx; takrorsiz kategoriyalar; birinchi 3 ta mahsulot. Har bir so'rov ostiga natijaning qisqa tavsifini yozing. Batafsil: `uyga-vazifa.md`.
