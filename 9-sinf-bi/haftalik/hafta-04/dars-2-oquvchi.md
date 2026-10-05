# 11-dars. RDBMS muhitlari va ma'lumotlar yaxlitligi

> Excel'da manfiy narx yoki ikki xil bir xil ID ni hech kim to'xtatmaydi. Haqiqiy ma'lumotlar bazasi esa bunday xatoni «yo'q!» deb rad etadi. Bugun bazani himoya qiluvchi qoidalar — cheklovlar bilan tanishamiz.

## Dars xulosasi

- **RDBMS** — relatsion modelga asoslangan va SQL bilan boshqariladigan DBMS.
- **Mashhur RDBMS lar:** Microsoft SQL Server (T-SQL), PostgreSQL, MySQL/MariaDB, Oracle (PL/SQL), SQLite (serversiz, bitta fayl).
- **SSMS** — SQL Server bilan ishlash dasturi: **Object Explorer** (bazalar daraxti), **New Query** (so'rov oynasi), **Execute / F5** (bajarish).
- **Ma'lumotlar yaxlitligi** — ma'lumotlarning aniq, to'liq va izchil bo'lishi.
- **Yaxlitlik turlari:**
  - **Entity** — har qator noyob: `PRIMARY KEY`;
  - **Referential** — FK faqat mavjud PK ga: `FOREIGN KEY ... REFERENCES`;
  - **Domain** — qiymat ruxsat etilgan doirada: ma'lumot turi, `NOT NULL`, `CHECK`, `DEFAULT`.
- `UNIQUE` — PK bo'lmagan ustunda ham takrorni taqiqlaydi (email, telefon).
- Cheklov buzilsa, DBMS **xato beradi va yozuvni qabul qilmaydi** — bu bazaning himoyasi.
- **ACID:** Atomicity, Consistency, Isolation, Durability — tranzaksiyalar ishonchliligi.

---

## Qo'shimcha ma'lumot

### 1. SQL — til, RDBMS — «davlatlar»

Barcha RDBMS lar SQL da «gapiradi», lekin shevalari farq qiladi. Masalan, birinchi 5 qatorni olish:
- SQL Server: `SELECT TOP 5 * FROM Mahsulotlar;`
- PostgreSQL, MySQL, SQLite: `SELECT * FROM Mahsulotlar LIMIT 5;`

### 2. Cheklovli jadval namunasi

```sql
CREATE TABLE Oquvchilar (
    OquvchiID INT PRIMARY KEY,
    Ism       NVARCHAR(50) NOT NULL,
    Email     VARCHAR(100) UNIQUE,
    Sinf      INT DEFAULT 9,
    Yosh      INT CHECK (Yosh BETWEEN 12 AND 18)
);
```

- `NVARCHAR` — o'zbek harflari uchun xavfsiz Unicode matn; qiymat `N'...'` ko'rinishida yoziladi.
- Matn ichidagi apostrof ikkilantiriladi: `N'O''g''iloy'`.

### 3. Xato — do'stingiz

```sql
INSERT INTO Oquvchilar (OquvchiID, Ism, Yosh) VALUES (4, N'Sardor', 21);
-- XATO: CHECK cheklovi buzildi (21 > 18)
```

Xato xabarini o'qishni o'rganing: unda **qaysi cheklov** buzilgani yoziladi.

### 4. ACID — bank misolida

Do'stingizga 100 000 so'm o'tkazyapsiz: (1) sizdan yechiladi, (2) unga qo'shiladi. Agar 2-qadamda xato chiqsa, **Atomicity** tufayli 1-qadam ham bekor qilinadi — pul «yo'qolib» qolmaydi.

---

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **RDBMS** | Relatsion ma'lumotlar bazasini boshqarish tizimi |
| **Dialekt** | SQL ning ma'lum bir RDBMS dagi o'ziga xos varianti (T-SQL, PL/SQL) |
| **SSMS** | SQL Server Management Studio — SQL Server uchun grafik muhit |
| **Object Explorer** | SSMS dagi bazalar va jadvallar daraxti |
| **Ma'lumotlar yaxlitligi** | Ma'lumotlarning aniq, to'liq va izchilligi |
| **Cheklov (constraint)** | Ustunga qo'yiladigan va noto'g'ri qiymatni rad etuvchi qoida |
| **NOT NULL** | Ustun bo'sh qolishi mumkin emas |
| **UNIQUE** | Ustunda takroriy qiymat bo'lishi mumkin emas |
| **CHECK** | Qiymat shartga mos bo'lishi kerak (`Narx > 0`) |
| **DEFAULT** | Qiymat berilmasa, avtomatik qo'yiladigan standart qiymat |
| **Tranzaksiya** | Birgalikda bajarilishi shart bo'lgan amallar guruhi |
| **ACID** | Tranzaksiyaning 4 ishonchlilik tamoyili |

---

## Bilasizmi?

- SQLite dunyodagi eng ko'p o'rnatilgan ma'lumotlar bazasi deb hisoblanadi: u deyarli har bir smartfon va brauzer ichida bor.
- PostgreSQL ning ildizlari 1980-yillarda Kaliforniya universitetida (Berkeley) boshlangan POSTGRES loyihasiga borib taqaladi.
- SQL Server ning bepul **Express** versiyasi o'quv va kichik loyihalar uchun yetarli.
- Banklarda har bir pul o'tkazmasi ACID tamoyillariga amal qiluvchi tranzaksiya sifatida bajariladi.

---

## Topshiriqlar

### 1. RDBMS ni moslang · oson
Moslashtiring: SQL Server, PostgreSQL, MySQL, Oracle, SQLite — «telefon ilovasi ichida», «Microsoft korporativ muhit», «bepul, veb-saytlar uchun mashhur», «PL/SQL dialekti», «ochiq kodli, analitika va startaplar».

**Kutiladigan natija:** 5 ta to'g'ri juftlik.

### 2. Yaxlitlik turi · oson
Qaysi tur buzilgan: (a) ikki o'quvchida bir xil ID; (b) yosh `-3`; (c) baholar jadvalida mavjud bo'lmagan fan ID si?

**Kutiladigan natija:** Entity, Domain, Referential.

### 3. Cheklovni tanlang · oson
Har bir talabga mos cheklovni yozing: ism bo'sh bo'lmasin; email takrorlanmasin; narx musbat bo'lsin; sinf ko'rsatilmasa 9 bo'lsin.

**Kutiladigan natija:** NOT NULL, UNIQUE, CHECK, DEFAULT.

### 4. SSMS qismlari · oson
SSMS da Object Explorer, New Query, Execute (F5), Results va Messages oynalari nima uchun kerakligini bir jumladan yozing.

**Kutiladigan natija:** 5 ta qisqa tavsif.

### 5. Baza va jadval yarating · o'rta
SSMS da (yoki SQLite da) `Maktab` bazasi va `Oquvchilar` jadvalini cheklovlar bilan yarating (PK, NOT NULL, UNIQUE, DEFAULT, CHECK).

**Kutiladigan natija:** ishlaydigan `CREATE TABLE` skripti va Object Explorer dagi jadval.

### 6. Xatoni bashorat qiling · o'rta
`Oquvchilar` jadvaliga 5 ta `INSERT` yozing: 2 tasi muvaffaqiyatli, 3 tasi turli cheklovlarni buzsin. Avval natijani bashorat qiling, keyin tekshiring.

**Kutiladigan natija:** 5 ta so'rov, bashorat va haqiqiy natija jadvali.

### 7. FK bilan ikki jadval · o'rta
`Sinflar(SinfID, Nomi)` va `Oquvchilar(..., SinfID FK)` jadvallarini yarating. Mavjud bo'lmagan `SinfID` bilan o'quvchi qo'shib ko'ring va xatoni yozing.

**Kutiladigan natija:** 2 ta jadval skripti va referential xato xabari.

### 8. Jadvallar tartibi · o'rta
Nima uchun `Buyurtmalar` jadvalini `Mijozlar` jadvalidan oldin yaratib bo'lmaydi? 2–3 jumla bilan tushuntiring.

**Kutiladigan natija:** FK mavjud jadvalga ishora qilishi haqida izoh.

### 9. Kutubxona skripti · qiyin
10-darsdagi 3NF kutubxona modeli uchun `CREATE TABLE` skriptlarini yozing: PK, FK, kamida bittadan NOT NULL, UNIQUE, CHECK, DEFAULT.

**Kutiladigan natija:** to'liq, xatosiz bajariladigan skript.

### 10. ACID misollari · qiyin
ACID ning har bir harfi uchun hayotiy misol (bank, chipta sotish, onlayn do'kon) yozing.

**Kutiladigan natija:** 4 ta misol, har biri 1–2 jumla.

### 11. Dialektlarni solishtiring · qiyin
Internetdan (rasmiy hujjatlardan) aniqlang: SQL Server, PostgreSQL va MySQL da avtomatik o'suvchi ID qanday yoziladi?

**Kutiladigan natija:** 3 qatorli jadval (`IDENTITY`, `SERIAL`/`GENERATED`, `AUTO_INCREMENT`).

### 12. «Iflos» ma'lumotdan himoya · bonus
7-darsdagi Data Cleaning muammolaridan 4 tasini (dublikat, bo'sh qiymat, noto'g'ri format, mantiqsiz qiymat) tanlang va har birini qaysi cheklov oldini olishini yozing.

**Kutiladigan natija:** 4 qatorli jadval: muammo → cheklov → misol.

---

## O'zingizni tekshiring

1. DBMS va RDBMS qanday farq qiladi?
2. Beshta RDBMS va ularning qo'llanish sohasini ayting.
3. SSMS da so'rov qanday yoziladi va bajariladi?
4. Uchta yaxlitlik turini cheklovlar bilan tushuntiring.
5. `UNIQUE` va `PRIMARY KEY` farqi nima?
6. Cheklov buzilganda DBMS nima qiladi va bu nega foydali?
7. ACID harflarini tushuntiring.

---

## Uyga vazifa

Kutubxona modelingiz uchun cheklovli `CREATE TABLE` skriptlarini yozing va har bir cheklovni buzadigan bitta `INSERT` misolini xato izohi bilan keltiring. Batafsil: `uyga-vazifa.md`.
