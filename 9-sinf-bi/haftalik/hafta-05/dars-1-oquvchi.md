# 13-dars. SQL asoslari: WHERE shartli filtrlash, taqqoslash va mantiqiy operatorlar (AND, OR, NOT)

> Minglab qatordan kerakligini topish — haqiqiy tahlilning boshlanishi. Bugun `WHERE` bilan jadvalni «elakdan o'tkazamiz».

## Dars xulosasi

- **`WHERE`** — qatorlarni shart bo'yicha filtrlaydi; `FROM` dan keyin yoziladi.
- **Taqqoslash:** `=`, `<>`, `>`, `<`, `>=`, `<=`; matn va sana bir tirnoqda, unicode uchun `N'...'`.
- **`AND`** — ikkala shart, **`OR`** — kamida bittasi, **`NOT`** — teskari.
- **Tartib:** `NOT`, keyin `AND`, keyin `OR`; shubha bo'lsa — qavs.
- **`IN`** — ro'yxat, **`BETWEEN`** — oraliq (chegaralar kiradi), **`LIKE`** — namuna (`%`, `_`).

## Qo'shimcha ma'lumot

### 1. Namuna jadval
| MahsulotID | Nomi | Kategoriya | Narx | Soni |
|---|---|---|---|---|
| 1 | Sichqoncha | Aksessuar | 80000 | 25 |
| 2 | Klaviatura | Aksessuar | 150000 | 12 |
| 3 | Monitor | Ekran | 1900000 | 4 |
| 4 | Noutbuk | Kompyuter | 7500000 | 3 |
| 5 | Quloqchin | Aksessuar | 120000 | 18 |
| 6 | Planshet | Kompyuter | 3200000 | 6 |

### 2. Uchta tuzoq
1. **Bitta `=`:** SQL Server da tenglik `=` bilan yoziladi, `==` emas.
2. **Tirnoqsiz matn:** `Kategoriya = Aksessuar` xato; matn tirnoqda: `N'Aksessuar'`.
3. **Qavssiz `OR`:** `AND` avval bajarilgani uchun natija kutilganidan farq qilishi mumkin.

### 3. Bajarilish tartibi
Yozamiz: `SELECT ... FROM ... WHERE ...`. DBMS bajaradi: `FROM`, so'ng `WHERE` (qatorlar filtrlanadi), keyin `SELECT`.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| WHERE | Qatorlarni shart bo'yicha filtrlash bandi |
| Shart (condition) | `TRUE` yoki `FALSE` beruvchi ifoda |
| Taqqoslash operatori | `=`, `<>`, `>`, `<`, `>=`, `<=` |
| AND | Ikkala shart bajarilishi kerak |
| OR | Kamida bitta shart bajarilishi kerak |
| NOT | Shartni teskarisiga o'giradi |
| IN | Qiymat ro'yxatdagilardan biriga tengmi |
| BETWEEN | Qiymat oraliqda (chegaralar bilan) |
| LIKE | Namuna bo'yicha matn qidiruvi |
| Wildcard | `%` va `_` o'rinbosar belgilar |

## Bilasizmi?

- `WHERE` ni birinchi marta SQL ning 1970-yillardagi nashrlarida «filtr qatlami» deb atashgan; hozir ham u har bir tahlilchi so'rovining asosi.
- Power BI da filtrlar ham orqada `WHERE` ga aylanib, ma'lumot manbasiga yuboriladi.
- `LIKE '%abc'` kabi namunalar indeksdan foydalana olmaydi, shuning uchun juda katta jadvallarda sekin.

## Topshiriqlar

### 1. Narx bo'yicha filtr · oson

Narxi 1 000 000 dan yuqori mahsulotlar nomini chiqaring.

**Kutiladigan natija:** `SELECT Nomi FROM Mahsulotlar WHERE Narx > 1000000;` — 3 qator.

### 2. Kategoriya bo'yicha · oson

Faqat `Kompyuter` kategoriyasidagi mahsulotlarni chiqaring.

**Kutiladigan natija:** `WHERE Kategoriya = N'Kompyuter'` — 2 qator.

### 3. Teng emas · oson

Aksessuar bo'lmagan mahsulotlarni `<>` bilan toping.

**Kutiladigan natija:** `<>` bilan yozilgan so'rov, 3 qator.

### 4. Soni kam · oson

Soni 5 dan kam mahsulotlar nomi va sonini chiqaring.

**Kutiladigan natija:** Monitor (4) va Noutbuk (3).

### 5. AND bilan · o'rta

Aksessuar va narxi 100 000 dan past mahsulotlarni toping.

**Kutiladigan natija:** 1 qator: Sichqoncha.

### 6. OR bilan · o'rta

Ekran kategoriyasi yoki soni 5 dan kam mahsulotlarni toping.

**Kutiladigan natija:** 2 qator: Monitor va Noutbuk.

### 7. BETWEEN · o'rta

Narxi 100 000 dan 2 000 000 gacha mahsulotlarni `BETWEEN` bilan toping.

**Kutiladigan natija:** 3 qator: Klaviatura, Monitor, Quloqchin.

### 8. IN va LIKE · o'rta

Kategoriyasi Ekran yoki Kompyuter bo'lganlarni `IN` bilan, nomi `K` bilan boshlanganlarni `LIKE` bilan toping.

**Kutiladigan natija:** 3 qator (`IN`) va 1 qator: Klaviatura (`LIKE`).

### 9. Natijani bashorat qiling · qiyin

Bajarmasdan qatorlar sonini ayting: `WHERE Kategoriya = N'Aksessuar' OR Kategoriya = N'Ekran' AND Narx > 1000000`.

**Kutiladigan natija:** 4 qator (3 aksessuar + Monitor): `AND` avval bajariladi.

### 10. Xatoni toping · qiyin

3 ta xatoni toping: `SELECT Nomi FROM Mahsulotlar WHERE Kategoriya == Aksessuar AND Narx > ;`

**Kutiladigan natija:** `=` (bitta), matn tirnoqda (`N'Aksessuar'`), `Narx > 100000` kabi qiymat yozilgan.

### 11. Qavsli shart · qiyin

(Aksessuar yoki Ekran) va narxi 1 000 000 dan yuqori mahsulotlarni qavs bilan toping.

**Kutiladigan natija:** 1 qator: Monitor.

### 12. Rahbar uchun filtr · bonus

Narxi 100 000 – 2 000 000 oralig'ida, nomi `K` yoki `Q` bilan boshlanadigan mahsulotlarni toping va bir jumlali izoh yozing.

**Kutiladigan natija:** Klaviatura va Quloqchin; izoh bilan.

## O'zingizni tekshiring

1. `WHERE` nima qiladi?
2. `=` va `<>` farqi nima?
3. `AND`, `OR`, `NOT` qanday ishlaydi?
4. Qavs nima uchun kerak?
5. `IN` va `BETWEEN` farqi?
6. `%` va `_` wildcardlari nimani bildiradi?
7. SQL Server da matn qiymati qanday yoziladi?

## Uyga vazifa

Mahsulotlar jadvalida 10 ta `WHERE` so'rovini yozing (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
