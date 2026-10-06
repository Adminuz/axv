# 15-dars. SQL asoslari: NULL qiymatlar bilan ishlash va ma'lumot turlari

> Ma'lumotlar hamma vaqt to'liq bo'lmaydi: telefon yozilmagan, sana noma'lum. Bugun `NULL` bilan to'g'ri ishlashni va ustun turlarini o'rganamiz.

## Dars xulosasi

- **`NULL`** — qiymat yo'q yoki noma'lum; `0` va `''` emas.
- **Tekshirish:** `IS NULL`, `IS NOT NULL`; `= NULL` ishlamaydi.
- **Almashtirish:** `ISNULL(a, b)` (SQL Server), `COALESCE(a, b, c, ...)` (standart).
- **Tuzoq:** `NULL` qatnashgan arifmetika va `<>` taqqoslash qatorni yo'qotishi mumkin.
- **Turlar:** `INT`, `DECIMAL`, `NVARCHAR`, `DATE`, `BIT`; `CAST(ifoda AS tur)` turni o'zgartiradi.

## Qo'shimcha ma'lumot

### 1. Mijozlar jadvali
| MijozID | Ism | Telefon | Email | RoyxatSana | Faol |
|---|---|---|---|---|---|
| 1 | Ali | 901234567 | ali@mail.uz | 2024-09-01 | 1 |
| 2 | Vali | NULL | vali@gmail.com | 2024-10-15 | 1 |
| 3 | Sana | 935551122 | NULL | 2025-01-10 | 0 |
| 4 | Dilnoza | NULL | NULL | 2025-02-20 | 1 |
| 5 | Jasur | 977778899 | jasur@gmail.com | 2025-03-05 | 0 |

### 2. Uchta tuzoq
1. **`= NULL`:** hech qachon `TRUE` emas — `IS NULL` yozing.
2. **`<>` va NULL:** `Telefon <> N'9...'` NULL qatorlarni chiqarmaydi.
3. **Butun bo'linma:** `7 / 2 = 3`; kasr kerak bo'lsa `DECIMAL` yoki `CAST`.

### 3. Ustun cheklovi
`NOT NULL` ustunga `NULL` kiritishni taqiqlaydi; `NULL` ruxsat etilgan ustunlarda esa qiymat ixtiyoriy.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| NULL | Qiymat yo'qligi yoki noma'lumligi |
| IS NULL | NULL ni tekshiruvchi shart |
| IS NOT NULL | Qiymati borligini tekshiruvchi shart |
| ISNULL | SQL Server da NULL ni almashtirish funksiyasi |
| COALESCE | Birinchi NULL bo'lmagan qiymatni qaytaradi |
| Ma'lumot turi | Ustunda saqlanadigan qiymat turi |
| DECIMAL | Aniq o'nlik son turi |
| NVARCHAR | Unicode matn turi |
| BIT | Mantiqiy (0/1) tur |
| CAST | Ma'lumot turini o'zgartirish |

## Bilasizmi?

- Kompyuter fanida `NULL` ni «milliard dollarlik xato» deb atashgan: u ko'plab dastur xatolariga sabab bo'lgan.
- SQL da `NULL = NULL` ham `TRUE` bermaydi: ikkita noma'lum qiymat teng ekani noma'lum.
- Power BI da bo'sh (`blank`) qiymatlar ham aslida `NULL` ga mos keladi.

## Topshiriqlar

### 1. NULL nima? · oson

`NULL`, `0` va `''` farqini 3 jumlada yozing.

**Kutiladigan natija:** Qiymat yo'q, nol qiymat, bo'sh matn farqlari.

### 2. IS NULL · oson

Emaili kiritilmagan mijozlarni toping.

**Kutiladigan natija:** Sana va Dilnoza.

### 3. IS NOT NULL · oson

Ham telefoni, ham emaili bor mijozlarni toping.

**Kutiladigan natija:** Ali va Jasur.

### 4. = NULL ni sinang · oson

`WHERE Telefon = NULL` ni bajaring va natijani tushuntiring.

**Kutiladigan natija:** 0 qator: `= NULL` ishlamaydi.

### 5. ISNULL · o'rta

`Telefon` NULL bo'lsa «Yo'q» chiqaring (`ISNULL`).

**Kutiladigan natija:** Vali va Dilnoza uchun «Yo'q».

### 6. COALESCE · o'rta

Telefon, bo'lmasa Email, bo'lmasa «Aloqa yo'q» chiqaring.

**Kutiladigan natija:** Dilnoza uchun «Aloqa yo'q».

### 7. Sana filtri · o'rta

2025-yilda ro'yxatdan o'tgan mijozlarni toping.

**Kutiladigan natija:** Sana, Dilnoza, Jasur.

### 8. BIT filtri · o'rta

Faol (`Faol = 1`) mijozlarni toping.

**Kutiladigan natija:** Ali, Vali, Dilnoza.

### 9. Natijani bashorat qiling · qiyin

Qiymatni ayting: `SELECT 5 + NULL, COALESCE(NULL, 7);`

**Kutiladigan natija:** `NULL` va `7`.

### 10. <> tuzog'i · qiyin

`WHERE Telefon <> N'901234567'` nechta qator beradi? NULL qatorlarini ham qaytaring.

**Kutiladigan natija:** 2 qator; `OR Telefon IS NULL` bilan 4 qator.

### 11. Tur tanlash · qiyin

Narx, tug'ilgan sana, faolligi, ism va yosh uchun mos ma'lumot turini tanlang.

**Kutiladigan natija:** `DECIMAL`, `DATE`, `BIT`, `NVARCHAR`, `INT`.

### 12. CAST bilan bo'lish · bonus

`7 / 2` va `CAST(7 AS DECIMAL(5,2)) / 2` natijalarini solishtiring va xulosa yozing.

**Kutiladigan natija:** 3 va 3.50; butun bo'linma farqi.

## O'zingizni tekshiring

1. `NULL` nima?
2. `= NULL` nega ishlamaydi?
3. `IS NULL` va `IS NOT NULL` nima qiladi?
4. `ISNULL` va `COALESCE` farqi nima?
5. `<>` taqqoslashda NULL qanday ta'sir qiladi?
6. Pul uchun qaysi tur mos?
7. `CAST` nima uchun kerak?

## Uyga vazifa

Mijozlar jadvalini yarating va 8 ta so'rov yozing (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
