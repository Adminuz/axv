# 14-dars. SQL asoslari: ORDER BY saralash (ASC, DESC), LIMIT va OFFSET

> Reyting, «eng yaxshi 10 ta», sahifalangan katalog — barchasi saralashga tayanadi. Bugun natijani tartibga solamiz.

## Dars xulosasi

- **`ORDER BY`** — natijani tartiblaydi; `ASC` (standart) va `DESC`.
- **Bir nechta ustun:** `ORDER BY Kategoriya, Narx DESC` — avval birinchi, teng bo'lsa ikkinchi ustun.
- **`TOP N` + `ORDER BY`** — «eng ... N ta» so'rovi (SQL Server).
- **`OFFSET n ROWS FETCH NEXT m ROWS ONLY`** — sahifalash; faqat `ORDER BY` bilan.
- **Boshqa DBMS:** `LIMIT m OFFSET n`.

## Qo'shimcha ma'lumot

### 1. Sahifa formulasi
`OFFSET = (sahifa - 1) * sahifa hajmi`. Hajmi 5 bo'lsa: 1-sahifa `OFFSET 0`, 2-sahifa `OFFSET 5`, 3-sahifa `OFFSET 10`.

### 2. Uchta tuzoq
1. **Tartibsiz `TOP`:** qaysi qatorlar kelishi kafolatlanmaydi.
2. **`ORDER BY` jadvaldagi tartib emas:** u faqat natija tartibini beradi.
3. **`OFFSET` `ORDER BY` siz xato beradi** (SQL Server).

### 3. Bajarilish tartibi
`FROM`, `WHERE`, `SELECT`, `ORDER BY`, so'ng `TOP` / `OFFSET-FETCH`. Shuning uchun `ORDER BY` da `SELECT` dagi taxallusni ishlatish mumkin, `WHERE` da esa mumkin emas.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| ORDER BY | Natijani saralash bandi |
| ASC | O'sish tartibi (standart) |
| DESC | Kamayish tartibi |
| TOP N | Birinchi N qatorni olish (SQL Server) |
| OFFSET | O'tkazib yuboriladigan qatorlar soni |
| FETCH NEXT | Qaytariladigan qatorlar soni |
| LIMIT | TOP/FETCH ning PostgreSQL, MySQL, SQLite analogi |
| Pagination (sahifalash) | Natijani bo'laklab ko'rsatish |

## Bilasizmi?

- Onlayn do'konlarda «Keyingi sahifa» tugmasi aynan `OFFSET ... FETCH` ga o'xshash so'rovni yuboradi.
- `TOP 10 PERCENT` natijaning faqat 10 foizini qaytaradi.
- Power BI jadvallaridagi «Tartiblash» ham ichkarida saralashga aylanadi.

## Topshiriqlar

### 1. O'sish tartibi · oson

Mahsulotlarni narxi bo'yicha o'sish tartibida chiqaring.

**Kutiladigan natija:** Birinchi Sichqoncha (80 000), oxirgi Noutbuk (7 500 000).

### 2. Kamayish tartibi · oson

Mahsulotlarni narxi bo'yicha kamayish tartibida chiqaring.

**Kutiladigan natija:** Birinchi Noutbuk, oxirgi Sichqoncha.

### 3. Alifbo tartibi · oson

Mahsulotlarni nomi bo'yicha alifbo tartibida chiqaring.

**Kutiladigan natija:** Klaviatura, Monitor, Noutbuk, Planshet, Quloqchin, Sichqoncha.

### 4. Eng arzon 2 ta · oson

Eng arzon 2 ta mahsulotni toping.

**Kutiladigan natija:** Sichqoncha va Quloqchin (`TOP 2` + `ORDER BY Narx`).

### 5. Ikki ustun · o'rta

Kategoriya bo'yicha A-Z, kategoriya ichida narx bo'yicha kamayish tartibida chiqaring.

**Kutiladigan natija:** Aksessuar: Klaviatura, Quloqchin, Sichqoncha; Ekran: Monitor; Kompyuter: Noutbuk, Planshet.

### 6. WHERE va ORDER BY · o'rta

Faqat aksessuarlarni narxi bo'yicha kamayish tartibida chiqaring.

**Kutiladigan natija:** Klaviatura, Quloqchin, Sichqoncha.

### 7. Ombor qiymati · o'rta

`Narx * Soni` ni `Qiymat` taxallusi bilan hisoblab, qiymati bo'yicha kamayish tartibida chiqaring.

**Kutiladigan natija:** Birinchi Noutbuk (22 500 000), oxirgi Klaviatura (1 800 000).

### 8. 2-sahifa · o'rta

Narx kamayish tartibida, sahifa hajmi 2 bilan 2-sahifani chiqaring.

**Kutiladigan natija:** Monitor va Klaviatura.

### 9. Natijani bashorat qiling · qiyin

Bajarmasdan javob bering: `SELECT TOP 2 Nomi FROM Mahsulotlar ORDER BY Narx ASC;`

**Kutiladigan natija:** Sichqoncha va Quloqchin (2 qator, 1 ustun).

### 10. Xatoni toping · qiyin

Nega xato? `SELECT Nomi FROM Mahsulotlar OFFSET 2 ROWS FETCH NEXT 2 ROWS ONLY;`

**Kutiladigan natija:** `ORDER BY` yo'q; `ORDER BY Narx DESC` qo'shilgan.

### 11. 3-sahifa formulasi · qiyin

Sahifa hajmi 4 bo'lsa, 3-sahifa uchun `OFFSET` qancha? Formulani yozing va so'rovni tuzing.

**Kutiladigan natija:** `OFFSET 8 ROWS FETCH NEXT 4 ROWS ONLY`.

### 12. PostgreSQL varianti · bonus

11-topshiriqni `LIMIT ... OFFSET` bilan qayta yozing.

**Kutiladigan natija:** `... ORDER BY Narx DESC LIMIT 4 OFFSET 8;`

## O'zingizni tekshiring

1. `ORDER BY` nima qiladi?
2. `ASC` va `DESC` farqi nima?
3. Ikki ustun bo'yicha saralash qanday ishlaydi?
4. `TOP` ni nega `ORDER BY` bilan ishlatish kerak?
5. `OFFSET ... FETCH` qanday ishlaydi?
6. Sahifalash formulasi nima?
7. `LIMIT` qaysi DBMS larda ishlaydi?

## Uyga vazifa

8 ta saralash va sahifalash so'rovini yozing (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
