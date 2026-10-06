# 13-dars. Ma'lumotlar modellashtirish: Kimball metodologiyasi, Star Schema va Snowflake Schema

> Hisobotlar qancha tez va sodda bo'lsa, tahlilchi shuncha samarali. Bugun ma'lumotni tahlil uchun qanday tashkil qilishni — Kimball va Star Schema ni o'rganamiz.

## Dars xulosasi

- **OLTP** — kundalik amallar (normallashgan); **OLAP** — tahlil (star/snowflake).
- **Kimball 4 qadami:** biznes jarayon, grain, dimension, fact.
- **Star Schema:** markazda fact, atrofida dimension jadvallar; fact va dimension FK orqali bog'lanadi.
- **Snowflake Schema:** dimension lar normallashgan; joy tejaladi, JOIN lar ko'payadi.
- **Tanlov:** BI uchun odatda Star; shubha bo'lsa — Star.

## Qo'shimcha ma'lumot

### 1. Namuna ma'lumot
`yillik_kpi`: 5 hudud (Toshkent shahri, Samarqand, Farg'ona, Andijon, Buxoro) x 3 yil (2022–2024) = 15 qator. Jami o'quvchilar: 2022 — 2 430 000, 2023 — 2 478 000, 2024 — 2 526 000. Ma'lumotlar o'quv uchun o'ylab topilgan.

### 2. Kimball qadamlari bir misolda
Biznes jarayon: yillik ta'lim statistikasi. Grain: hudud x yil. Dimension: hudud, yil. Fact: o'quvchilar, o'qituvchilar, maktablar soni.

### 3. Odatiy xatolar
Fakt jadvalda matn saqlash; grain ni aniqlamaslik; hamma narsani snowflake qilish.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| OLTP | Operatsion tranzaksiyalar tizimi |
| OLAP | Tahliliy ishlov berish tizimi |
| Kimball | Dimensional modeling metodologiyasi |
| Fact table | Raqamli o'lchovlar jadvali |
| Dimension table | Tavsiflovchi atributlar jadvali |
| Grain | Fakt jadval qatorining aniqlik darajasi |
| Star Schema | Fact markazda, dimension lar atrofda |
| Snowflake Schema | Normallashtirilgan dimension lar bilan sxema |
| Surrogate key | Sun'iy butun kalit |

## Bilasizmi?

- Ralph Kimball 1996-yilda mashhur «The Data Warehouse Toolkit» kitobini chiqargan; yondashuv hali ham BI ning asosi.
- Star Schema nomi diagrammaning yulduzga o'xshashligidan kelib chiqqan.
- Power BI ning data modeli ham aslida star schema ga asoslangan.

## Topshiriqlar

### 1. OLTP yoki OLAP · oson

4 ta amalni OLTP yoki OLAP deb toifalang: yangi qator qo'shish, yillik jami, qiymatni yangilash, trend.

**Kutiladigan natija:** 4 ta to'g'ri toifa.

### 2. Grain jumlasi · oson

`yillik_kpi` asosidagi fakt uchun grain ni 1 jumlada yozing.

**Kutiladigan natija:** «Bitta qator = bitta hudud, bitta yil».

### 3. Fakt yoki dimension · oson

`hudud nomi`, `oquvchilar_soni`, `yil`, `maktablar_soni` ni fakt yoki dimension ga ajrating.

**Kutiladigan natija:** 2 fakt, 2 dimension atributi.

### 4. Kimball qadamlari · oson

Kimball ning 4 qadamini `maktab.db` misolida yozing.

**Kutiladigan natija:** 4 ta qadam to'g'ri.

### 5. dim_hudud · o'rta

`dim_hudud` jadvalini yarating va `hududlar` dan to'ldiring.

**Kutiladigan natija:** 5 qator.

### 6. dim_sana · o'rta

`dim_sana` ni `yillik_kpi` dagi yillardan to'ldiring.

**Kutiladigan natija:** 3 qator: 2022, 2023, 2024.

### 7. fact_kpi · o'rta

`fact_kpi` ni yarating va 15 qator bilan to'ldiring.

**Kutiladigan natija:** `COUNT(*) = 15`.

### 8. Natijani bashorat qiling · o'rta

`SELECT COUNT(*) FROM fact_kpi` va `SELECT COUNT(*) FROM dim_hudud` natijalarini ayting.

**Kutiladigan natija:** 15 va 5.

### 9. Yillik jami · qiyin

Har yil uchun jami o'quvchilarni JOIN bilan toping.

**Kutiladigan natija:** 2 430 000 / 2 478 000 / 2 526 000.

### 10. Hududlar bo'yicha 2024 · qiyin

2024-yil uchun hududlar bo'yicha o'quvchilarni kamayish tartibida chiqaring.

**Kutiladigan natija:** Samarqand 620000, Farg'ona 585000, Andijon 524000, Toshkent 485000, Buxoro 312000.

### 11. Star yoki Snowflake · qiyin

`dim_hudud` ni Snowflake ga aylantirish foydasi va zararini 3 jumlada yozing.

**Kutiladigan natija:** Joy tejaladi, JOIN ko'payadi.

### 12. Star Schema diagrammasi · bonus

`dim_hudud`, `dim_sana`, `fact_kpi` diagrammasini chizing: PK, FK, 1:N.

**Kutiladigan natija:** To'g'ri diagramma.

## O'zingizni tekshiring

1. OLTP va OLAP farqi nima?
2. Kimball ning 4 qadami qaysilar?
3. Grain nima?
4. Star Schema qanday tuzilgan?
5. Fact va Dimension farqi nima?
6. Snowflake Schema nimasi bilan farq qiladi?
7. BI uchun odatda qaysi sxema tanlanadi?

## Uyga vazifa

`maktab.db` da Star Schema qurib, 3 ta so'rov yozing (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
