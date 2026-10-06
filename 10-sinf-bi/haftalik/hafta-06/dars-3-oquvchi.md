# 18-dars. Data Lake konsepsiyasi, Bronze / Silver / Gold zonalari

> Hamma ma'lumot ham darrov hisobotga tayyor emas. Bugun Data Lake va uning Bronze, Silver, Gold qatlamlarini o'rganamiz.

## Dars xulosasi

- Data Lake — ma'lumotni xom, har xil formatda arzon saqlash joyi (schema-on-read).
- Bronze — minimal ishlov; Silver — tozalangan; Gold — biznes uchun tayyor.
- Raw qatlam o'zgartirilmaydi.
- DWH — tuzilmali va tez SQL; Lake — xom va moslashuvchan.
- Lakehouse ikkalasini bitta tizimda birlashtiradi.
- Tartibsiz Lake «data swamp» ga aylanadi: qatlamlar va hujjatlar kerak.

## Qo'shimcha ma'lumot

### Medallion arxitekturasi
Bronze, Silver, Gold bo'linishi ko'pincha shunday ataladi. Dasturda uchta qatlam alohida nomlangan.

### Data swamp
Tartibsiz, hujjatsiz lake: ma'lumot bor, lekin hech kim ishlata olmaydi.

### Parquet
Ustunli siqilgan format; katta ma'lumotda CSV dan tez va ixcham. Uslubiy ko'rsatmada Silver Parquet ko'rinishida yaratiladi.

### E-commerce misoli
Loglar va rasmlar — Lake; tozalangan sotuv fakti — DWH; dashboard — BI.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Data Lake | Xom ma'lumot ombori |
| Bronze | Minimal ishlov qatlami |
| Silver | Tozalangan qatlam |
| Gold | Biznes qatlami |
| Schema-on-read | Tuzilma o'qishda |
| Lakehouse | Lake + DWH |
| Data swamp | Tartibsiz lake |
| Parquet | Ustunli fayl formati |
| Raw | Asl fayllar qatlami |

## Bilasizmi?

- Medallion nomi medal ranglaridan (bronza, kumush, oltin) olingan.
- Parquet ustunli format bo'lgani uchun tahlil so'rovlarida faqat kerakli ustun o'qiladi.
- Ko'p kompaniyalar Lake va DWH ni bir vaqtda ishlatadi.

## Topshiriqlar

### 1. Lake ta'rifi · oson

Data Lake ni 2 jumlada ta'riflang.

**Kutiladigan natija:** To'g'ri ta'rif.

### 2. Qatlamlar · oson

Bronze, Silver, Gold vazifasini yozing.

**Kutiladigan natija:** 3 ta vazifa.

### 3. Schema-on-read · oson

Schema-on-read nima?

**Kutiladigan natija:** O'qishda tuzilma.

### 4. DWH yoki Lake · oson

3 xil ma'lumot uchun saqlash joyini tanlang.

**Kutiladigan natija:** Asosli tanlov.

### 5. Qatlamni toping · o'rta

Dublikatni olib tashlash qaysi qatlamda?

**Kutiladigan natija:** Silver.

### 6. Papkalar · o'rta

4 ta data papkasini va vazifasini yozing.

**Kutiladigan natija:** raw, bronze, silver, gold.

### 7. Silver kodi · o'rta

`drop_duplicates` va `dropna` bilan Silver yozing.

**Kutiladigan natija:** Silver DataFrame.

### 8. Raw qoidasi · o'rta

Nima uchun Raw tahrirlanmaydi?

**Kutiladigan natija:** Qayta ishlash uchun asl.

### 9. Gold kodi · qiyin

Yillik jamlama yozing.

**Kutiladigan natija:** `groupby` + `sum`.

### 10. Oqim · qiyin

Raw dan Gold gacha to'liq oqim yozing.

**Kutiladigan natija:** 3 qatlam CSV.

### 11. Hujjat · qiyin

Silver da nima tashlangani haqida qisqa hujjat yozing.

**Kutiladigan natija:** Qoidalar ro'yxati.

### 12. Lakehouse · bonus

Lakehouse ni misol bilan tushuntiring.

**Kutiladigan natija:** Lake + DWH.

## O'zingizni tekshiring

1. Data Lake nima?
2. Bronze, Silver, Gold farqi?
3. Schema-on-read nima?
4. DWH va Lake farqi?
5. Lakehouse nima?
6. Nega Raw tahrirlanmaydi?

## Uyga vazifa

Raw dan Gold gacha oqim yozing (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
