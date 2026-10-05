# 12-dars. SQL asoslari: SELECT, ustunlar va sodda ifodalar

> Minglab qatorli jadvaldan kerakli ma'lumotni bir qator kod bilan olish — BI analitigining super kuchi. Bugun SQL ning eng muhim so'zi — `SELECT` bilan ishlaymiz.

## Dars xulosasi

- **SQL** — relatsion bazalar uchun standart, **deklarativ** til: «nimani olish» yoziladi, «qanday» ni DBMS hal qiladi.
- **Buyruq toifalari:** DDL (`CREATE`, `ALTER`, `DROP`), DML (`INSERT`, `UPDATE`, `DELETE`), **DQL (`SELECT`)**, DCL (`GRANT`, `REVOKE`), TCL (`COMMIT`, `ROLLBACK`).
- `SELECT * FROM Jadval;` — barcha ustunlar.
- `SELECT Ustun1, Ustun2 FROM Jadval;` — faqat kerakli ustunlar, yozilgan tartibda.
- `AS` — natijadagi ustunga taxallus: `Narx AS [Narx (so'm)]`.
- **Ifodalar:** `Narx * Soni AS Summa`, `Narx * 1.12 AS QQS_bilan`; matnni birlashtirish: `Nomi + N' ' + Kategoriya` yoki `CONCAT(...)`.
- `DISTINCT` — takrorsiz qiymatlar; `TOP N` — birinchi N qator (SQL Server; boshqalarda `LIMIT N`).
- **NULL** — «qiymat yo'q»; NULL qatnashgan arifmetika natijasi ham NULL.

---

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

### 2. So'rovlar va natijalar

```sql
SELECT Nomi, Narx * Soni AS OmborQiymati
FROM Mahsulotlar;
-- Sichqoncha 2000000, Klaviatura 1800000, Monitor 7600000, ...

SELECT DISTINCT Kategoriya FROM Mahsulotlar;
-- Aksessuar, Ekran, Kompyuter
```

### 3. Uchta tuzoq

1. **Butun bo'linma:** SQL Server da `7 / 2 = 3`, lekin `7 / 2.0 = 3.5`.
2. **Taxallussiz ifoda:** ustun nomi `(No column name)` bo'lib qoladi — doim `AS` yozing.
3. **Tartibsiz TOP:** `TOP 3` qaysi 3 qatorni berishi kafolatlanmaydi; «eng qimmat 3 ta» uchun keyinroq `ORDER BY` o'rganamiz.

### 4. Yozilish va bajarilish tartibi

Yozamiz: `SELECT ... FROM ...`. DBMS bajaradi: avval `FROM` (jadvalni topadi), keyin `SELECT` (ustunlarni hisoblaydi).

---

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **SQL** | Structured Query Language — tuzilmali so'rovlar tili |
| **Deklarativ til** | Natija tasvirlanadigan, bajarish yo'li ko'rsatilmaydigan til |
| **So'rov (query)** | Bazadan ma'lumot olish uchun yozilgan SQL buyrug'i |
| **DQL** | Ma'lumotni so'rash tili — `SELECT` |
| **SELECT** | Qaysi ustunlarni olishni ko'rsatadi |
| **FROM** | Qaysi jadvaldan olishni ko'rsatadi |
| **Taxallus (alias)** | `AS` bilan berilgan vaqtinchalik ustun nomi |
| **Hisoblangan ustun** | Ifoda (`Narx * Soni`) natijasida hosil bo'lgan ustun |
| **DISTINCT** | Takrorlanuvchi qiymatlarni olib tashlash |
| **TOP / LIMIT** | Natijadagi qatorlar sonini cheklash |
| **NULL** | Qiymat yo'qligi (0 ham, bo'sh matn ham emas) |
| **Natijalar to'plami (result set)** | So'rov qaytargan jadval ko'rinishidagi natija |

---

## Bilasizmi?

- SQL dastlab **SEQUEL** (Structured English Query Language) deb atalgan, shuning uchun ko'pchilik hozir ham uni «sikvel» deb o'qiydi.
- SQL 1986-yilda ANSI, 1987-yilda ISO standarti sifatida qabul qilingan.
- `SELECT` ma'lumotni o'zgartirmaydi — shuning uchun yangi boshlovchilar uchun eng xavfsiz buyruq.
- Power BI ham ichkarida ma'lumot manbasiga SQL so'rovlarini yuborishi mumkin.

---

## Topshiriqlar

### 1. Toifani aniqlang · oson
Har bir buyruq toifasini yozing: `SELECT`, `CREATE TABLE`, `INSERT`, `GRANT`, `ROLLBACK`, `DROP`, `UPDATE`.

**Kutiladigan natija:** 7 ta to'g'ri javob (DQL, DDL, DML, DCL, TCL).

### 2. Barcha ustunlar · oson
`Mahsulotlar` jadvalidagi barcha ma'lumotni chiqaruvchi so'rov yozing va natijada nechta qator, nechta ustun bo'lishini ayting.

**Kutiladigan natija:** `SELECT * FROM Mahsulotlar;` — 6 qator, 5 ustun.

### 3. Ikki ustun · oson
Faqat mahsulot nomi va narxini chiqaring.

**Kutiladigan natija:** to'g'ri so'rov va 2 ustunli natija.

### 4. Taxalluslar · oson
Nomi va kategoriyani `Mahsulot` va `Turi` sarlavhalari bilan chiqaring.

**Kutiladigan natija:** `AS` bilan yozilgan so'rov.

### 5. Ombor qiymati · o'rta
Har bir mahsulotning ombordagi umumiy qiymatini (`Narx * Soni`) hisoblang.

**Kutiladigan natija:** hisoblangan ustunli so'rov; Sichqoncha uchun 2000000.

### 6. QQS va chegirma · o'rta
Narxni QQS bilan (12%) va 15% chegirma bilan ikkita alohida ustunda chiqaring.

**Kutiladigan natija:** `Narx * 1.12` va `Narx * 0.85` ustunlari.

### 7. Takrorsiz ro'yxat · o'rta
Do'konda qaysi kategoriyalar borligini takrorsiz chiqaring.

**Kutiladigan natija:** `DISTINCT` li so'rov, 3 qator.

### 8. Matnni birlashtiring · o'rta
`Sichqoncha (Aksessuar)` ko'rinishidagi `ToliqNom` ustunini hosil qiling.

**Kutiladigan natija:** `+` yoki `CONCAT` bilan yozilgan so'rov.

### 9. Natijani bashorat qiling · qiyin
Bajarmasdan javob bering, keyin tekshiring: `SELECT 7 / 2 AS A, 7 / 2.0 AS B;` va `SELECT TOP 2 Nomi FROM Mahsulotlar;`.

**Kutiladigan natija:** A = 3, B = 3.5; 1 ustun, 2 qator va «tartib kafolatlanmagan» izohi.

### 10. Xatoni toping · qiyin
So'rovdagi 3 ta xatoni toping va tuzating: `SELEC Nomi Narx FORM Mahsulotlar`.

**Kutiladigan natija:** `SELECT Nomi, Narx FROM Mahsulotlar;` va xatolar ro'yxati.

### 11. 10 ta mahsulotli baza · qiyin
Jadvalga yana 4 ta mahsulot qo'shing (`INSERT`) va 2–8-topshiriqlardagi so'rovlarni qayta bajaring. Natijalar qanday o'zgardi?

**Kutiladigan natija:** yangilangan natijalar va 3–4 jumlali xulosa.

### 12. Rahbar uchun hisobot · bonus
Bitta so'rovda chiqaring: `Mahsulot (Kategoriya)` ko'rinishidagi nom, narx, QQS bilan narx va ombor qiymati — barcha ustunlar ma'noli taxalluslar bilan.

**Kutiladigan natija:** 4 ustunli, o'qilishi oson hisobot so'rovi.

---

## O'zingizni tekshiring

1. SQL nima va nega u deklarativ deyiladi?
2. Beshta buyruq toifasini va har biridan bittadan buyruqni ayting.
3. `SELECT *` qachon ishlatiladi va nega hisobotlarda undan qochish kerak?
4. `AS` nima qiladi?
5. Hisoblangan ustunga misol keltiring.
6. `DISTINCT` va `TOP` nima uchun kerak?
7. NULL bilan `0` ning farqi nima?

---

## Uyga vazifa

`Mahsulotlar` jadvalini 10 ta mahsulotgacha to'ldiring va 6 ta `SELECT` so'rovini yozing (barcha ustunlar; 2 ustun taxallus bilan; ombor qiymati; QQS bilan narx; takrorsiz kategoriyalar; birinchi 3 ta mahsulot), har birining natijasini qisqa tavsiflang. Batafsil: `uyga-vazifa.md`.
