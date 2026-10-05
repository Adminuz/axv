# 11-dars. Relatsion ma'lumotlar bazalari va model tushunchasi (3-qism): RDBMS muhitlari va ma'lumotlar yaxlitligi

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarni mashhur RDBMS platformalari (Microsoft SQL Server, PostgreSQL, MySQL, Oracle, SQLite) va ularning ish muhiti (SQL Server Management Studio — SSMS) bilan tanishtirish; ma'lumotlar yaxlitligi (Data Integrity) turlarini — Entity, Referential, Domain — va ularni ta'minlovchi cheklovlarni (PRIMARY KEY, FOREIGN KEY, NOT NULL, UNIQUE, CHECK, DEFAULT) o'rgatish; ACID tamoyillari haqida dastlabki tushuncha berish.
- **Kutiladigan natija:** O'quvchilar RDBMS larni farqlaydi va qaysi biri qayerda ishlatilishini aytadi; SSMS da baza va jadval yaratadi; `CREATE TABLE` ichida cheklovlarni to'g'ri qo'yadi; cheklov buzilganda DBMS qanday xato berishini va nima uchun bu foydali ekanini tushuntiradi.
- **Vaqt taqsimoti:**
  - O'tgan darsni takrorlash (anomaliyalar, 1NF–3NF): 10 daqiqa
  - Yangi mavzu: RDBMS platformalari va SSMS muhiti: 15 daqiqa
  - Ma'lumotlar yaxlitligi turlari va cheklovlar: 25 daqiqa
  - Amaliyot: jadval yaratish va cheklovlarni sinash: 20 daqiqa
  - ACID, nazorat savollari va xulosa: 10 daqiqa

> Manba: o'quv qo'llanma — «RDBMS (Relational Database Management Systems)» bo'limi (SQL Server, PostgreSQL, MySQL/MariaDB, Oracle, SQLite; Primary Key, Foreign Key, Unique, Check cheklovlari, domain constraints; ACID tamoyillari) va SQL bo'limidagi SSMS bilan ishlash. Kurs SQL Server (T-SQL) dialektida olib boriladi; SSMS o'rnatib bo'lmasa, mentor SQLite yoki onlayn SQL muharriridan foydalanishi mumkin (sintaksis farqlari pastda ko'rsatilgan).

---

## Mentor konspekti

### 1. DBMS va RDBMS

**DBMS (Database Management System)** — ma'lumotlar bazasini yaratish, o'zgartirish, qidirish va himoya qilish dasturi. **RDBMS** — relatsion modelga (jadvallar, PK, FK) asoslangan DBMS. Barcha RDBMS lar **SQL** tilidan foydalanadi, lekin har birining o'z «shevasi» (dialekti) bor.

| RDBMS | Ishlab chiqaruvchi | Litsenziya | Qayerda ko'p ishlatiladi | SQL dialekti |
|---|---|---|---|---|
| **Microsoft SQL Server** | Microsoft | tijoriy (bepul Express/Developer versiyalari bor) | korporativ tizimlar, banklar, Power BI bilan | T-SQL |
| **PostgreSQL** | ochiq hamjamiyat | bepul, ochiq kodli | veb-ilovalar, analitika, startaplar | PostgreSQL SQL |
| **MySQL / MariaDB** | Oracle / MariaDB hamjamiyati | bepul (ochiq kodli) | veb-saytlar, internet-do'konlar | MySQL SQL |
| **Oracle Database** | Oracle | tijoriy | yirik korporatsiyalar, davlat tizimlari | PL/SQL |
| **SQLite** | ochiq hamjamiyat | bepul | telefon ilovalari, brauzerlar, kichik dasturlar (server kerak emas — bitta fayl) | SQLite SQL |

> Analogiya: SQL — «ingliz tili», RDBMS lar — turli davlatlar. Asosiy grammatika bir xil, lekin talaffuz va ba'zi so'zlar farq qiladi (masalan, birinchi 5 qatorni olish: SQL Server da `SELECT TOP 5`, PostgreSQL/MySQL/SQLite da `LIMIT 5`).

### 2. SSMS muhiti

**SQL Server Management Studio (SSMS)** — SQL Server bilan ishlash uchun Microsoft ning bepul grafik dasturi.

Asosiy qismlar:
- **Connect to Server** oynasi — server nomi (masalan, `localhost` yoki `.\SQLEXPRESS`), autentifikatsiya turi.
- **Object Explorer** (chapda) — serverdagi bazalar, jadvallar, ustunlar daraxti.
- **New Query** tugmasi — SQL yozish oynasi.
- **Execute** (`F5`) — so'rovni bajarish; natija pastdagi **Results** va **Messages** oynalarida.
- Baza tanlash: yuqoridagi ro'yxat yoki `USE BazaNomi;` buyrug'i.

Birinchi qadamlar:

```sql
CREATE DATABASE Dokon;
GO
USE Dokon;
GO
```

`GO` — SSMS uchun «paket tugadi» belgisi (SQL buyrug'i emas, SSMS ko'rsatmasi).

### 3. Ma'lumotlar yaxlitligi (Data Integrity)

**Ma'lumotlar yaxlitligi** — bazadagi ma'lumotlarning **aniq, to'liq va izchil** bo'lishi. RDBMS buni **cheklovlar (constraints)** yordamida avtomatik nazorat qiladi: noto'g'ri ma'lumot kiritilsa, DBMS uni rad etadi.

| Yaxlitlik turi | Ma'nosi | Cheklovlar |
|---|---|---|
| **Entity integrity** (obyekt yaxlitligi) | Har bir qator noyob aniqlanadi | `PRIMARY KEY` (takrorlanmaydi va NULL bo'lmaydi) |
| **Referential integrity** (havola yaxlitligi) | FK faqat mavjud PK qiymatiga ishora qiladi | `FOREIGN KEY ... REFERENCES` |
| **Domain integrity** (qiymatlar sohasi) | Ustun qiymati ruxsat etilgan doirada | ma'lumot turi (`INT`, `NVARCHAR`, `DATE`), `NOT NULL`, `CHECK`, `DEFAULT` |
| Qo'shimcha: noyoblik | PK bo'lmagan ustunda takror bo'lmasin | `UNIQUE` (masalan, telefon yoki email) |

### 4. Cheklovlar bilan jadval yaratish

10-darsdagi 3NF modelimizni SQL Server da quramiz:

```sql
CREATE TABLE Mijozlar (
    MijozID   INT PRIMARY KEY,
    Ism       NVARCHAR(50) NOT NULL,
    Telefon   VARCHAR(20)  UNIQUE,
    Shahar    NVARCHAR(30) DEFAULT N'Toshkent'
);

CREATE TABLE Mahsulotlar (
    MahsulotID INT PRIMARY KEY,
    Nomi       NVARCHAR(50) NOT NULL,
    Narx       DECIMAL(12,2) CHECK (Narx > 0)
);

CREATE TABLE Buyurtmalar (
    BuyurtmaID INT PRIMARY KEY,
    Sana       DATE NOT NULL,
    MijozID    INT NOT NULL FOREIGN KEY REFERENCES Mijozlar(MijozID)
);
```

Izohlar:
- `NVARCHAR` — Unicode matn (o'zbek harflari `o'`, `g'` va kirill uchun xavfsiz); `N'...'` — Unicode matn qiymati.
- `DECIMAL(12,2)` — 12 xonali son, shundan 2 tasi verguldan keyin (pul uchun).
- Jadvallar tartibi muhim: `Buyurtmalar` dan oldin `Mijozlar` yaratilishi kerak, chunki FK mavjud jadvalga ishora qiladi.

### 5. Cheklov buzilganda nima bo'ladi?

```sql
INSERT INTO Mijozlar (MijozID, Ism, Telefon) VALUES (1, N'Aziza', '901112233');
INSERT INTO Mijozlar (MijozID, Ism, Telefon) VALUES (1, N'Bekzod', '934445566');
-- XATO: Violation of PRIMARY KEY constraint (MijozID = 1 allaqachon bor)

INSERT INTO Mahsulotlar VALUES (10, N'Sichqoncha', -5000);
-- XATO: CHECK constraint (Narx > 0) buzildi

INSERT INTO Buyurtmalar VALUES (101, '2024-10-01', 99);
-- XATO: FOREIGN KEY constraint — MijozID = 99 Mijozlar jadvalida yo'q
```

Mentor uchun asosiy g'oya: **xato — bu himoya**. Cheklovlar «iflos» ma'lumot bazaga tushishining oldini oladi; 7-darsdagi Data Cleaning ishining katta qismi aynan cheklovsiz Excel jadvallar tufayli kerak bo'ladi.

> Matndagi apostrof: SQL da matn `'...'` ichida yoziladi, shuning uchun `O'g'iloy` ismini `N'O''g''iloy'` ko'rinishida (apostrofni ikkilantirib) yozish kerak.

### 6. ACID — tranzaksiya ishonchliligi

**Tranzaksiya** — birgalikda bajarilishi shart bo'lgan amallar guruhi (masalan, bir hisobdan pul yechish va boshqasiga qo'shish).

| Harf | Tamoyil | Ma'nosi |
|---|---|---|
| **A** | Atomicity (atomarlik) | Hammasi bajariladi yoki hech biri — «yarim» holat yo'q |
| **C** | Consistency (izchillik) | Tranzaksiyadan keyin barcha cheklovlar saqlanadi |
| **I** | Isolation (izolyatsiya) | Bir vaqtdagi tranzaksiyalar bir-biriga xalaqit bermaydi |
| **D** | Durability (barqarorlik) | Tasdiqlangan (COMMIT) o'zgarish elektr o'chsa ham saqlanib qoladi |

Bank misoli: 100 000 so'm o'tkazishda yechish bajarildi-yu, qo'shishda xato chiqdi — Atomicity tufayli yechish ham bekor qilinadi (ROLLBACK).

### 7. BI uchun ahamiyati

BI analitigi odatda bazani o'zi loyihalamaydi, lekin undan ma'lumot oladi. Cheklovlar bor bazadan olingan ma'lumot **ishonchli**: dublikat ID yo'q, «yetim» buyurtmalar (mijozi yo'q) yo'q, manfiy narxlar yo'q — hisobot raqamlari to'g'ri chiqadi.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. RDBMS ni tanlang (oson)
Har bir holat uchun mos RDBMS ni tanlang: (a) Android telefonidagi oflayn eslatmalar ilovasi; (b) bank korporativ tizimi va Power BI hisobotlari Microsoft muhitida; (c) bepul ochiq kodli bazada ishlaydigan internet-do'kon sayti.

**Yechim:**
(a) **SQLite** — server kerak emas, bitta faylda ishlaydi; (b) **Microsoft SQL Server** (yoki Oracle) — korporativ, Microsoft ekotizimi; (c) **MySQL** yoki **PostgreSQL** — bepul, veb uchun mashhur.

### 2-topshiriq. Yaxlitlik turini aniqlang (oson)
Qaysi yaxlitlik turi buzilgan? (a) Ikki o'quvchiga bir xil `OquvchiID = 7` berilgan; (b) Yoshi ustunida `-3`; (c) Baholar jadvalida mavjud bo'lmagan `FanID = 55`.

**Yechim:**
(a) **Entity integrity** (PK takrorlandi); (b) **Domain integrity** (`CHECK (Yosh > 0)` kerak); (c) **Referential integrity** (FK mavjud bo'lmagan PK ga ishora qilmoqda).

### 3-topshiriq. Cheklovli jadval yarating (o'rta)
SSMS da `Maktab` bazasi va `Oquvchilar` jadvalini yarating: `OquvchiID` (PK), `Ism` (bo'sh bo'lmasin), `Email` (takrorlanmasin), `Sinf` (standart qiymat `9`), `Yosh` (12 dan 18 gacha).

**Yechim:**
```sql
CREATE DATABASE Maktab;
GO
USE Maktab;
GO
CREATE TABLE Oquvchilar (
    OquvchiID INT PRIMARY KEY,
    Ism       NVARCHAR(50) NOT NULL,
    Email     VARCHAR(100) UNIQUE,
    Sinf      INT DEFAULT 9,
    Yosh      INT CHECK (Yosh BETWEEN 12 AND 18)
);
```
Tekshirish: Object Explorer da `Maktab → Tables → dbo.Oquvchilar` paydo bo'ladi (kerak bo'lsa, `F5` bilan yangilang).

### 4-topshiriq. Xatoni bashorat qiling (qiyin)
3-topshiriqdagi jadvalga quyidagilar kiritildi. Qaysilari muvaffaqiyatli, qaysilari xato beradi va nima uchun?
```sql
INSERT INTO Oquvchilar (OquvchiID, Ism, Email, Yosh) VALUES (1, N'Ali', 'ali@maktab.uz', 15);
INSERT INTO Oquvchilar (OquvchiID, Ism, Email, Yosh) VALUES (2, NULL, 'vali@maktab.uz', 14);
INSERT INTO Oquvchilar (OquvchiID, Ism, Email, Yosh) VALUES (3, N'Malika', 'ali@maktab.uz', 15);
INSERT INTO Oquvchilar (OquvchiID, Ism, Email, Yosh) VALUES (4, N'Sardor', 'sardor@maktab.uz', 21);
INSERT INTO Oquvchilar (OquvchiID, Ism, Email, Yosh) VALUES (5, N'Nodira', 'nodira@maktab.uz', 16);
```

**Yechim:**
1 — muvaffaqiyatli (Sinf avtomatik 9 bo'ladi, DEFAULT); 2 — xato: `Ism` NOT NULL; 3 — xato: `Email` UNIQUE (ali@maktab.uz bor); 4 — xato: CHECK (21 > 18); 5 — muvaffaqiyatli. Natijada jadvalda 2 ta qator (1 va 5).

---

## Tezkor nazorat savollari

1. DBMS va RDBMS farqi nima?
   - *Javob:* RDBMS — relatsion modelga (jadvallar, kalitlar, munosabatlar) asoslangan DBMS turi; SQL bilan boshqariladi.
2. 5 ta mashhur RDBMS ni ayting.
   - *Javob:* Microsoft SQL Server, PostgreSQL, MySQL, Oracle, SQLite.
3. Ma'lumotlar yaxlitligining 3 asosiy turi qaysilar?
   - *Javob:* Entity (PK), Referential (FK), Domain (tur, NOT NULL, CHECK, DEFAULT).
4. `UNIQUE` va `PRIMARY KEY` farqi nima?
   - *Javob:* Ikkalasi takrorni taqiqlaydi; PK jadvalda bitta va NULL bo'lmaydi, UNIQUE bir nechta ustunda bo'lishi mumkin (SQL Server da bitta NULL ga ruxsat beradi).
5. ACID dagi «A» nimani bildiradi?
   - *Javob:* Atomicity — tranzaksiya to'liq bajariladi yoki umuman bajarilmaydi.

---

## Uyga vazifa

10-darsda 3NF ga keltirilgan kutubxona modelingiz uchun `CREATE TABLE` skriptlarini yozing: har bir jadvalda PK, kerakli FK, kamida bitta `NOT NULL`, bitta `UNIQUE`, bitta `CHECK` va bitta `DEFAULT` cheklovi bo'lsin. Har bir cheklov uchun uni buzadigan bitta `INSERT` misolini yozib, qanday xato chiqishini izohlang. Batafsil: `uyga-vazifa.md`.
