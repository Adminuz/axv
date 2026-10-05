# 11-dars. SQL JOIN turlari (INNER, LEFT, RIGHT, FULL) va amaliy tahlil

> Ma'lumot bitta jadvalda emas, bo'laklarga bo'lib saqlanadi. JOIN esa ularni kalit orqali bir joyga yig'adigan "yelim". Bugun to'rt xil yelimni va ularning qachon qo'llanishini o'rganasiz.

---

## Dars xulosasi

- Relatsion bazada ma'lumotlar bir nechta jadvalga bo'linadi; **`JOIN`** ularni kalit (PK = FK) orqali birlashtiradi.
- **`ON`** sharti jadvallar qanday bog'lanishini aytadi: `k.hudud_id = h.hudud_id`.
- **`INNER JOIN`** faqat ikkala tomonda mos kelganlarni qoldiradi.
- **`LEFT JOIN`** chap jadvalning barcha satrlarini saqlaydi; mosi yo'qlarga `NULL`.
- **`RIGHT JOIN`** o'ng jadvalning barcha satrlarini saqlaydi; **`FULL JOIN`** ikkala tomonni to'liq saqlaydi.
- `LEFT JOIN ... WHERE o'ng_PK IS NULL` bog'lanmaganlarni topadi.
- Taxalluslar (`h`, `k`, `m`) so'rovni qisqa va o'qiladigan qiladi.
- `JOIN` ni `GROUP BY` / `HAVING` bilan birga qo'llab, tayyor hisobot olinadi.

---

## Qo'shimcha ma'lumot

### 1. Nega ma'lumotni bo'lib saqlaymiz?
Agar har KPI satrida hudud nomi yozilsa, "Samarqand viloyati" matni yuzlab marta takrorlanadi; nom o'zgarsa, hammasini tahrirlash kerak. Shuning uchun nom `hududlar` da bir marta turadi, `yillik_kpi` esa faqat `hudud_id` ni saqlaydi. Hisobotda ikkalasini `JOIN` birlashtiradi.

### 2. Jadval raqsi: Venn diagrammasi
- `INNER JOIN` — ikki doiraning **kesishmasi**.
- `LEFT JOIN` — butun chap doira (+ kesishma).
- `RIGHT JOIN` — butun o'ng doira.
- `FULL JOIN` — ikkala doira birga.

### 3. LEFT JOIN da `ON` va `WHERE`
```sql
-- To'g'ri: Xorazm ham ro'yxatda qoladi (o'quvchilar soni NULL)
SELECT h.nomi, k.oquvchilar_soni
FROM hududlar h
LEFT JOIN yillik_kpi k ON k.hudud_id = h.hudud_id AND k.yil = 2024;

-- Qopqon: WHERE da shart bersangiz, NULL satrlar tushib qoladi
... LEFT JOIN yillik_kpi k ON k.hudud_id = h.hudud_id
WHERE k.yil = 2024;
```

### 4. COUNT va LEFT JOIN
`COUNT(*)` bo'sh hududni ham "1" deb sanaydi (chunki `NULL` li satr bor). To'g'risi: `COUNT(m.maktab_id)`, u `NULL` larni sanamaydi va 0 beradi.

### 5. COALESCE
`COALESCE(x, 0)` — `x` bo'sh bo'lsa `0` ni qaytaradi. Hisobotda `None` o'rniga `0` ko'rsatish uchun qulay.

### 6. RIGHT va FULL JOIN eslatmasi
SQLite 3.39 versiyadan boshlab `RIGHT` va `FULL JOIN` ni qo'llaydi. Tekshirish: `print(sqlite3.sqlite_version)`. Eski versiyada `LEFT JOIN` da jadvallar o'rnini almashtiring.

### 7. Odatiy xatolar
- `ON` ni unutish: har satr har satr bilan juftlanadi (Cartesian product).
- `hudud_id` ni jadval nomisiz yozish: ikkala jadvalda bor, noaniq.
- `LEFT JOIN` da o'ng jadval shartini `WHERE` ga qo'yish.

---

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **JOIN** | Jadvallarni kalit orqali birlashtirish |
| **ON** | Birlashtirish sharti |
| **INNER JOIN** | Faqat ikkala tomonda mos kelgan satrlar |
| **LEFT JOIN** | Chap jadvalning barcha satrlari + mosi |
| **RIGHT JOIN** | O'ng jadvalning barcha satrlari + mosi |
| **FULL JOIN** | Ikkala jadvalning barcha satrlari |
| **Primary Key (PK)** | Jadvaldagi satrni noyob aniqlovchi ustun |
| **Foreign Key (FK)** | Boshqa jadval PK siga havola qiluvchi ustun |
| **Anti-join** | `LEFT JOIN` + `IS NULL` bilan mosi yo'qlarni topish |
| **COALESCE** | `NULL` o'rniga boshqa qiymat beruvchi funksiya |

---

## Bilasizmi?

- Amalda ko'pincha `INNER JOIN` va `LEFT JOIN` yoziladi; `RIGHT JOIN` ni odatda jadval o'rinlarini almashtirib `LEFT JOIN` ga aylantirishadi.
- Onlayn do'konda buyurtma, mijoz va mahsulot ma'lumotlari odatda alohida jadvallarda; "Kim nima sotib oldi?" hisoboti 3 jadvalni `JOIN` qiladi.
- `JOIN` so'zi ingliz tilida "qo'shilmoq", Venn diagrammalarini esa XIX asr mantiqchisi John Venn nomi bilan atashadi.

---

## Topshiriqlar

> Jadvallar: `hududlar(hudud_id, nomi, markaz)`, `maktablar(maktab_id, hudud_id, raqam, sigim, turi)`, `yillik_kpi(kpi_id, hudud_id, yil, oquvchilar_soni, oqituvchilar_soni, maktablar_soni)`.

### 1. Kalitni toping · oson
`hududlar` va `yillik_kpi` orasida qaysi ustun PK, qaysisi FK? `ON` sharti qanday yoziladi?  
**Kutiladigan natija:** `hududlar.hudud_id` (PK), `yillik_kpi.hudud_id` (FK) va to'liq `ON` ifodasi.

### 2. Birinchi JOIN · oson
2024-yil uchun hudud nomi va o'quvchilar sonini chiqaring (`INNER JOIN`).  
**Kutiladigan natija:** bitta hudud uchun bitta qator, hamma nom matn ko'rinishida.

### 3. Taxalluslar · oson
Oldingi so'rovni taxalluslarsiz (to'liq jadval nomlari bilan) va taxalluslar bilan yozing. Qaysi biri o'qishga qulay?  
**Kutiladigan natija:** ikkita ekvivalent so'rov va xulosa.

### 4. JOIN turini toping · oson
Har vaziyat uchun JOIN turini tanlang: (a) faqat KPI si bor hududlar; (b) KPI bor-yo'qligidan qat'i nazar barcha hududlar; (c) ikki ro'yxatdagi hamma yozuv, bir-biriga mos kelmaganlari bilan.  
**Kutiladigan natija:** `INNER`, `LEFT`, `FULL` (yoki `RIGHT`) ga to'g'ri moslashtirilgan javoblar.

### 5. Nechta qator? · o'rta
`hududlar` da 6 qator, `yillik_kpi` da (har hududga 3 yil, bitta hududda ma'lumot yo'q) 15 qator bor. Quyidagi so'rovlar necha qator qaytaradi? Avval bashorat qiling, keyin tekshiring: (a) `INNER JOIN`; (b) `LEFT JOIN` (shartsiz).  
**Kutiladigan natija:** bashorat va tajriba natijasi.

### 6. Bo'sh hududni toping · o'rta
Hech qanday KPI kiritilmagan hududlarni topuvchi so'rov yozing (`LEFT JOIN ... IS NULL`).  
**Kutiladigan natija:** bitta hudud nomi (ma'lumotsiz hudud).

### 7. Maktablar hisoboti · o'rta
Har bir hudud uchun maktablar soni va umumiy sig'imni chiqaring. Maktabi yo'q hudud ham ko'rinsin, sig'im `0` bo'lsin (`COALESCE`).  
**Kutiladigan natija:** barcha hududlar, maktabsiz hudud uchun `0 | 0`.

### 8. Qopqonni toping · o'rta
Nima uchun quyidagi so'rov `LEFT JOIN` ning afzalligini yo'qotadi? Tuzating.
```sql
SELECT h.nomi, k.oquvchilar_soni
FROM hududlar h
LEFT JOIN yillik_kpi k ON k.hudud_id = h.hudud_id
WHERE k.yil = 2024;
```
**Kutiladigan natija:** `WHERE` sharti `NULL` satrlarni olib tashlashi tushuntiriladi, shart `ON` ga ko'chiriladi.

### 9. Uch jadval · qiyin
Har bir maktab uchun: hudud nomi, maktab raqami, sig'imi va shu hududning 2024-yildagi o'quvchilar soni chiqsin.  
**Kutiladigan natija:** `maktablar` qatorlari soniga teng natija, ikkita `JOIN` bilan.

### 10. FULL JOIN tadqiqoti · qiyin
`qabul_reja(hudud_nomi, reja)` jadvalini yarating (4 qator, ulardan 3 tasi `hududlar` dagi nomlar, 1 tasi yo'q nom) va `FULL JOIN` bilan ikkala tomonda mos kelmaganlarni toping.  
**Kutiladigan natija:** chap yoki o'ng tomoni `NULL` bo'lgan qatorlar ajratib ko'rsatiladi.

### 11. Hisobot + HAVING · qiyin
Har bir hudud uchun 3 yillik jami o'quvchilarni hisoblab, faqat 1 500 000 dan ko'p bo'lganlarni ko'rsating, hudud nomi bilan, kamayish tartibida.  
**Kutiladigan natija:** `JOIN`, `GROUP BY`, `HAVING`, `ORDER BY` uyg'unlashgan so'rov, uchta hudud.

### 12. Mini-loyiha: Python hisobot · bonus
Yuqoridagi 9- yoki 11-topshiriq natijasini Python skriptda olib, `f-string` bilan chiroyli jadval ko'rinishida chiqaring, `None` ni "ma'lumot yo'q" deb almashtiring.  
**Kutiladigan natija:** ustunlari tekislangan, `None` qiymatsiz chiroyli chop etish.

---

## O'zingizni tekshiring

1. JOIN nima uchun kerak?
2. `ON` ni yozmasak nima bo'ladi?
3. `INNER` va `LEFT JOIN` farqini bitta jumlada ayting.
4. Bog'lanmagan yozuvlarni topishda `IS NULL` qaysi jadval ustuniga qo'llanadi?
5. `LEFT JOIN` da o'ng jadval shartini nega `ON` ga yozamiz?
6. `COUNT(*)` va `COUNT(m.maktab_id)` farqi `LEFT JOIN` da nimada?
7. `FULL JOIN` natijasida kimdir `NULL` ga ega bo'lsa, bu nimani bildiradi?

---

## Uyga vazifa

Har bir hudud uchun nomi, 2024-yil o'quvchilar soni va `qabul_reja` dagi rejani bitta jadvalda chiqaring (`LEFT JOIN`; reja yo'q bo'lsa `0`, `COALESCE`). Keyin `qabul_reja` da rejasi kiritilmagan hududlarni anti-join bilan alohida chiqaring. (20–30 daqiqa)
