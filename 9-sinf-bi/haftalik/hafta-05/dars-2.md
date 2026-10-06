# 14-dars. SQL asoslari: ORDER BY saralash (ASC, DESC), LIMIT va OFFSET

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarni `ORDER BY` bilan natijani o'sish (`ASC`) va kamayish (`DESC`) tartibida saralash, bir necha ustun bo'yicha tartiblash, `TOP` ni `ORDER BY` bilan birga ishlatish hamda sahifalash (`OFFSET ... FETCH`, boshqa DBMS larda `LIMIT ... OFFSET`) bilan tanishtirish.
- **Kutiladigan natija:** O'quvchilar `ORDER BY` bilan bir va bir necha ustun bo'yicha saralaydi; `ASC` va `DESC` ni to'g'ri tanlaydi; «eng qimmat N ta» so'rovini `TOP` va `ORDER BY` bilan yozadi; `OFFSET ... FETCH` bilan sahifalaydi.
- **Vaqt taqsimoti:**
  - O'tgan darsni takrorlash (`WHERE`, `AND`, `OR`, `IN`, `LIKE`): 10 daqiqa
  - Yangi mavzu: `ORDER BY`, `ASC`, `DESC`: 10 daqiqa
  - Bir nechta ustun va `WHERE` bilan saralash: 20 daqiqa
  - `TOP`, `OFFSET–FETCH` va `LIMIT`: 15 daqiqa
  - Amaliyot (namuna bazada 8–10 ta so'rov), nazorat va xulosa: 25 daqiqa

> Manba: o'quv dasturi — «SQL asoslari: SELECT, WHERE, ORDER BY» moduli; o'quv qo'llanma — «Ma'lumotni saralash (ORDER BY)», «Natijani cheklash va sahifalash», «TOP va OFFSET–FETCH yordamida natijalarni boshqarish» bo'limlari; uslubiy ko'rsatma.

---

## Mentor konspekti

### 1. `ORDER BY`: `ASC` va `DESC`

Jadvaldagi qatorlar tartibi kafolatlanmagan: tartib faqat `ORDER BY` bilan beriladi. `ASC` — o'sish (standart), `DESC` — kamayish tartibi. `ORDER BY` so'rovning oxirida yoziladi. Saralash son, matn (alifbo) va sana bo'yicha ishlaydi, shuningdek hisoblangan ustun yoki taxallus bo'yicha ham.

```sql
SELECT Nomi, Narx
FROM Mahsulotlar
ORDER BY Narx ASC;

SELECT Nomi, Narx
FROM Mahsulotlar
ORDER BY Narx DESC;
```

> Professional maslahat: `ASC` yozilmasa ham o'sish tartibi bo'ladi. `DESC` da avval Noutbuk (7 500 000), oxirida Sichqoncha (80 000).

### 2. Bir nechta ustun bo'yicha va `WHERE` bilan saralash

`ORDER BY` da ustunlar vergul bilan yoziladi. Avval birinchi ustun bo'yicha tartiblanadi, qiymatlar teng bo'lsa — keyingisi bo'yicha. Har bir ustunga alohida `ASC`/`DESC` beriladi. `WHERE` bilan birga: avval filtr, keyin tartib. `ORDER BY` da `SELECT` dagi taxallusni ishlatish mumkin.

```sql
SELECT Kategoriya, Nomi, Narx
FROM Mahsulotlar
ORDER BY Kategoriya ASC, Narx DESC;

SELECT Nomi, Narx * Soni AS Qiymat
FROM Mahsulotlar
WHERE Kategoriya <> N'Ekran'
ORDER BY Qiymat DESC;
```

> Professional maslahat: Birinchi so'rovda Aksessuar ichida: Klaviatura, Quloqchin, Sichqoncha (narxi kamayish tartibida); Kompyuter ichida: Noutbuk, Planshet.

### 3. `TOP`, `OFFSET ... FETCH` va `LIMIT`

`TOP N` natijadan birinchi N qatorni oladi; «eng ... N ta» uchun uni albatta `ORDER BY` bilan ishlatish kerak. Sahifalash uchun SQL Server da `OFFSET n ROWS FETCH NEXT m ROWS ONLY` (faqat `ORDER BY` bilan) ishlatiladi: `n` ta qatorni o'tkazib, keyingi `m` tasini oladi. PostgreSQL, MySQL, SQLite da shu vazifani `LIMIT m OFFSET n` bajaradi.

```sql
SELECT TOP 3 Nomi, Narx
FROM Mahsulotlar
ORDER BY Narx DESC;

SELECT Nomi, Narx
FROM Mahsulotlar
ORDER BY Narx DESC
OFFSET 2 ROWS
FETCH NEXT 2 ROWS ONLY;

-- PostgreSQL / MySQL / SQLite:
-- ... ORDER BY Narx DESC LIMIT 2 OFFSET 2;
```

> Professional maslahat: Birinchi so'rov: Noutbuk, Planshet, Monitor. Ikkinchi so'rov 2 ta qatorni o'tkazib: Monitor, Klaviatura (2-sahifa, hajmi 2).

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Narx bo'yicha saralash (oson)
Mahsulotlarni narxi bo'yicha o'sish tartibida, so'ng kamayish tartibida chiqaring.

**Yechim:**
```sql
SELECT Nomi, Narx FROM Mahsulotlar ORDER BY Narx ASC;
SELECT Nomi, Narx FROM Mahsulotlar ORDER BY Narx DESC;
```

### 2-topshiriq. Eng qimmat 3 ta (oson)
Eng qimmat 3 ta mahsulot nomi va narxini chiqaring.

**Yechim:**
```sql
SELECT TOP 3 Nomi, Narx
FROM Mahsulotlar
ORDER BY Narx DESC;
-- Noutbuk, Planshet, Monitor
```

### 3-topshiriq. Ko'p ustunli saralash (o'rta)
Avval kategoriya bo'yicha alifbo tartibida, kategoriya ichida narx bo'yicha kamayish tartibida chiqaring.

**Yechim:**
```sql
SELECT Kategoriya, Nomi, Narx
FROM Mahsulotlar
ORDER BY Kategoriya ASC, Narx DESC;
```

### 4-topshiriq. 2-sahifa (qiyin)
Mahsulotlarni narxi kamayish tartibida sahifalang (sahifa hajmi 2). 2-sahifani chiqaring.

**Yechim:**
```sql
SELECT Nomi, Narx
FROM Mahsulotlar
ORDER BY Narx DESC
OFFSET 2 ROWS
FETCH NEXT 2 ROWS ONLY;
-- Monitor 1900000, Klaviatura 150000
```

### 5-topshiriq. Ombor qiymati reytingi (bonus)
Aksessuar bo'lmagan mahsulotlardan ombor qiymati (`Narx * Soni`) bo'yicha eng yuqori 2 tasini taxallus bilan chiqaring.

**Yechim:**
```sql
SELECT TOP 2 Nomi, Narx * Soni AS Qiymat
FROM Mahsulotlar
WHERE Kategoriya <> N'Aksessuar'
ORDER BY Qiymat DESC;
-- Noutbuk 22500000, Planshet 19200000
```

---

## Tezkor nazorat savollari

1. `ORDER BY` ning standart tartibi qanday?
   - *Javob:* `ASC` — o'sish tartibi.
2. `DESC` nimani anglatadi?
   - *Javob:* Kamayish tartibini: eng katta qiymat birinchi.
3. Nima uchun `TOP` ni `ORDER BY` siz ishlatish xavfli?
   - *Javob:* Tartib bo'lmasa, qaysi qatorlar «birinchi» ekani kafolatlanmaydi.
4. `OFFSET ... FETCH` qachon ishlaydi?
   - *Javob:* Faqat `ORDER BY` bilan birga.
5. PostgreSQL/MySQL da `OFFSET–FETCH` o'rniga nima?
   - *Javob:* `LIMIT m OFFSET n`.

---

## Uyga vazifa

`Mahsulotlar` jadvalida (10 ta mahsulot) 8 ta so'rov yozing: `ASC`, `DESC`, ikki ustunli saralash, `WHERE` + `ORDER BY`, `TOP 3` + `ORDER BY`, hisoblangan ustun bo'yicha saralash, 1-sahifa va 2-sahifa (hajmi 3). Har bir natijada birinchi qatorni yozing.
