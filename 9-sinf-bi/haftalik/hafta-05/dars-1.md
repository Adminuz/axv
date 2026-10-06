# 13-dars. SQL asoslari: WHERE shartli filtrlash, taqqoslash va mantiqiy operatorlar (AND, OR, NOT)

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarni `WHERE` yordamida qatorlarni shart bo'yicha filtrlash, taqqoslash operatorlari (`=`, `<>`, `>`, `<`, `>=`, `<=`), mantiqiy operatorlar (`AND`, `OR`, `NOT`), qavslar bilan tartibni boshqarish hamda `IN`, `BETWEEN` va `LIKE` operatorlari bilan tanishtirish.
- **Kutiladigan natija:** O'quvchilar `WHERE` bilan bir va bir necha shartli so'rovlar yozadi; `AND`, `OR`, `NOT` ning ishlashini tushuntiradi; qavslar bilan `AND` va `OR` tartibini to'g'ri boshqaradi; `IN`, `BETWEEN`, `LIKE` bilan oddiy filtrlarni tuzadi.
- **Vaqt taqsimoti:**
  - O'tgan darsni takrorlash (`SELECT`, `AS`, `DISTINCT`, `TOP`): 10 daqiqa
  - Yangi mavzu: `WHERE` va taqqoslash operatorlari: 10 daqiqa
  - `AND`, `OR`, `NOT` va qavslar: 20 daqiqa
  - `IN`, `BETWEEN`, `LIKE`: 15 daqiqa
  - Amaliyot (namuna bazada 8–10 ta so'rov), nazorat va xulosa: 25 daqiqa

> Manba: o'quv dasturi — «SQL asoslari: SELECT, WHERE, ORDER BY» moduli; o'quv qo'llanma — «WHERE operatorining mohiyati», «Mantiqiy operatorlardan foydalanish: AND, OR, NOT», «IN va BETWEEN», «LIKE va wildcardlar» bo'limlari; uslubiy ko'rsatma.

---

## Mentor konspekti

### 1. `WHERE` va taqqoslash operatorlari

`WHERE` jadvaldan qaytariladigan qatorlarni shart bo'yicha cheklaydi: u so'rovning «filtr qatlami». Shart `FROM` dan keyin yoziladi va faqat `TRUE` bo'lgan qatorlar natijaga o'tadi. Taqqoslash operatorlari: `=` (teng), `<>` (teng emas), `>`, `<`, `>=`, `<=`. Matn va sana qiymatlari bir tirnoqda yoziladi, unicode matn uchun `N'...'` ishlatiladi; SQL Server da tenglik uchun bitta `=` yoziladi.

```sql
SELECT Nomi, Narx
FROM Mahsulotlar
WHERE Narx > 1000000;

SELECT *
FROM Mahsulotlar
WHERE Kategoriya = N'Aksessuar';
```

| Operator | Ma'nosi | Misol |
|---|---|---|
| `=` | teng | `Soni = 4` |
| `<>` | teng emas | `Kategoriya <> N'Ekran'` |
| `>` / `<` | katta / kichik | `Narx > 100000` |
| `>=` / `<=` | katta yoki teng / kichik yoki teng | `Soni <= 5` |

> Professional maslahat: `Narx > 1000000` Monitor, Noutbuk va Planshet (3 qator) ni, `Kategoriya = N'Aksessuar'` esa Sichqoncha, Klaviatura, Quloqchin ni qaytaradi.

### 2. Mantiqiy operatorlar: `AND`, `OR`, `NOT`

`AND` — ikkala shart ham bajarilishi kerak; `OR` — kamida bittasi yetarli; `NOT` — shartni teskarisiga o'giradi. Bir so'rovda `AND` va `OR` aralashsa, avval `AND` bajariladi. Tartibni aniq ko'rsatish va xatodan qochish uchun qavslardan foydalaning.

```sql
SELECT Nomi FROM Mahsulotlar
WHERE Kategoriya = N'Aksessuar' AND Narx < 100000;

SELECT Nomi FROM Mahsulotlar
WHERE Kategoriya = N'Ekran' OR Soni < 5;

SELECT Nomi FROM Mahsulotlar
WHERE NOT Kategoriya = N'Aksessuar';

SELECT Nomi FROM Mahsulotlar
WHERE (Kategoriya = N'Aksessuar' OR Kategoriya = N'Ekran')
  AND Narx > 1000000;
```

Qavs ahamiyati: `Kategoriya = N'Aksessuar' OR Kategoriya = N'Ekran' AND Narx > 1000000` — 4 qator (3 aksessuar + Monitor), qavsli variant esa 1 qator (Monitor) qaytaradi.

> Professional maslahat: Qavssiz `A OR B AND C` bu `A OR (B AND C)` demak. Birinchi so'rov faqat Sichqoncha ni, qavsli oxirgi so'rov esa faqat Monitor ni qaytaradi.

### 3. `IN`, `BETWEEN` va `LIKE`

`IN` bir nechta qiymatdan biriga tengligini tekshiradi (`OR` zanjiri o'rniga). `BETWEEN a AND b` qiymat oraliqda ekanini tekshiradi, chegaralar kiradi. `LIKE` matnni namuna bo'yicha qidiradi: `%` — nol yoki undan ko'p belgi, `_` — aynan bitta belgi.

```sql
SELECT Nomi FROM Mahsulotlar
WHERE Kategoriya IN (N'Ekran', N'Kompyuter');

SELECT Nomi, Narx FROM Mahsulotlar
WHERE Narx BETWEEN 100000 AND 2000000;

SELECT Nomi FROM Mahsulotlar
WHERE Nomi LIKE N'K%';

SELECT Nomi FROM Mahsulotlar
WHERE Nomi LIKE N'%ch%';
```

> Professional maslahat: `LIKE N'%ch%'` Sichqoncha va Quloqchin ni topadi. `%` bilan boshlangan namuna katta jadvalda sekin ishlashi mumkin.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Qimmat mahsulotlar (oson)
`Mahsulotlar` dan narxi 1 000 000 dan yuqori mahsulotlar nomi va narxini chiqaring.

**Yechim:**
```sql
SELECT Nomi, Narx
FROM Mahsulotlar
WHERE Narx > 1000000;
```

### 2-topshiriq. Aksessuarlar (oson)
Faqat `Aksessuar` kategoriyasidagi mahsulotlarning barcha ustunlarini chiqaring.

**Yechim:**
```sql
SELECT *
FROM Mahsulotlar
WHERE Kategoriya = N'Aksessuar';
```

### 3-topshiriq. Arzon va ko'p (o'rta)
Narxi 200 000 dan past va soni 10 dan ko'p mahsulotlarni toping.

**Yechim:**
```sql
SELECT Nomi, Narx, Soni
FROM Mahsulotlar
WHERE Narx < 200000 AND Soni > 10;
```

### 4-topshiriq. Qavs ahamiyati (qiyin)
Ikki so'rovni yozing va natijalarini solishtiring: (a) `Kategoriya = N'Aksessuar' OR Kategoriya = N'Ekran' AND Narx > 1000000`; (b) xuddi shu shart qavs bilan: `(Aksessuar OR Ekran) AND Narx > 1000000`. Nega natija farq qiladi?

**Yechim:**
```sql
-- (a) AND avval bajariladi: 3 aksessuar + Monitor = 4 qator
SELECT Nomi FROM Mahsulotlar
WHERE Kategoriya = N'Aksessuar'
   OR Kategoriya = N'Ekran' AND Narx > 1000000;

-- (b) qavs bilan: faqat Monitor = 1 qator
SELECT Nomi FROM Mahsulotlar
WHERE (Kategoriya = N'Aksessuar' OR Kategoriya = N'Ekran')
  AND Narx > 1000000;
```

### 5-topshiriq. Rahbar uchun filtr (bonus)
Rahbar so'radi: «Narxi 100 000 va 2 000 000 oralig'ida, nomi 'K' yoki 'Q' bilan boshlanadigan, Aksessuar bo'lmagan mahsulotlar». Bitta so'rov yozing.

**Yechim:**
```sql
SELECT Nomi, Narx
FROM Mahsulotlar
WHERE Narx BETWEEN 100000 AND 2000000
  AND (Nomi LIKE N'K%' OR Nomi LIKE N'Q%')
  AND Kategoriya <> N'Aksessuar';
-- Aksessuarlar chiqarilgani uchun natija bo'sh: bu to'g'ri javob.
```

---

## Tezkor nazorat savollari

1. `WHERE` nima uchun kerak?
   - *Javob:* Qatorlarni shart bo'yicha filtrlash uchun: faqat shartga mos qatorlar natijaga o'tadi.
2. `=` va `<>` farqi nima?
   - *Javob:* `=` teng, `<>` teng emas degani.
3. `AND` va `OR` farqi?
   - *Javob:* `AND` da ikkala shart ham, `OR` da kamida bittasi bajarilishi kerak.
4. Qavs nima uchun muhim?
   - *Javob:* `AND` `OR` dan oldin bajariladi; qavs tartibni aniq belgilaydi.
5. `BETWEEN` chegaralarni o'z ichiga oladimi?
   - *Javob:* Ha, ikkala chegara ham kiradi.

---

## Uyga vazifa

`Dokon` bazasidagi `Mahsulotlar` jadvalida (10 ta mahsulot bilan) kamida 10 ta `WHERE` so'rovi yozing: tenglik, taqqoslash, `AND`, `OR`, `NOT`, qavs bilan aralash shart, `IN`, `BETWEEN`, 2 ta `LIKE`. Har bir so'rov ostiga natijada nechta qator chiqqanini yozing.
