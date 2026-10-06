# 15-dars. Data Mart tushunchasi va sohaga oid martlar yaratish

> Tahlilchi har safar 5 ta jadvalni bog'lamasligi kerak. Bugun sohaga tayyor ma'lumot qismini — Data Mart ni yaratamiz.

## Dars xulosasi

- **Data Mart** — soha uchun mo'ljallangan, foydalanuvchiga tayyor analitik qism.
- **DWH** — butun tashkilot uchun; mart — undan olingan mavzuli qism.
- **VIEW** — saqlangan `SELECT`: murakkab JOIN larni yashiradi, ma'lumotni nusxalamaydi.
- **Sohaga oid martlar:** `mart_oquvchilar`, `mart_yuklama` (nisbat va `CASE WHEN` toifa).
- **Hujjat:** nomi, maqsadi, foydalanuvchi, manba, yangilanish; umumiy (conformed) dimension lar.

## Qo'shimcha ma'lumot

### 1. Mart ta'rifi namunasi
**Nomi:** `mart_yuklama`. **Maqsadi:** hududlar va yillar bo'yicha o'quvchi/o'qituvchi nisbati va toifasi. **Foydalanuvchi:** kadrlar bo'limi, BI tahlilchi. **Manba:** `fact_kpi`, `dim_hudud`, `dim_sana`.

### 2. 2024-yil toifalari
Toshkent 15.16 — Yuqori; Andijon 13.58, Farg'ona 13.15, Buxoro 13.05 — O'rta; Samarqand 12.92 — Normal. (Ma'lumotlar o'quv uchun o'ylab topilgan.)

### 3. Qachon jadval mart
Hajm katta bo'lsa va so'rov sekin ishlasa, `CREATE TABLE ... AS SELECT` bilan jadval mart yaratiladi; uni har yuklashdan keyin yangilash kerak.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Data Mart | Soha uchun mo'ljallangan analitik qism |
| DWH | Markaziy ma'lumotlar ombori |
| VIEW | Saqlangan SELECT so'rovi |
| Conformed dimension | Martlar o'rtasida umumiy dimension |
| Mart ta'rifi | Nomi, maqsadi, foydalanuvchi, manba hujjati |
| CTAS | `CREATE TABLE ... AS SELECT` |
| Toifa | `CASE WHEN` bilan berilgan kategoriya |

## Bilasizmi?

- Kimball yondashuvida ombor martlar yig'indisidan quriladi, Inmon yondashuvida esa avval markaziy ombor, keyin martlar yaratiladi.
- Power BI hisobotlari ko'pincha aynan martlardan (yoki ularga o'xshash modellardan) ma'lumot oladi.
- Mart nomlari uchun odatda `mart_` prefiksi ishlatiladi.

## Topshiriqlar

### 1. Mart nima · oson

Data Mart ni 2 jumlada ta'riflang.

**Kutiladigan natija:** To'g'ri ta'rif.

### 2. DWH yoki mart · oson

Quyidagilarni ajrating: butun tashkilot ombori, kadrlar bo'limi uchun qism.

**Kutiladigan natija:** DWH va mart.

### 3. VIEW sifatlari · oson

VIEW ning 2 ta afzalligini yozing.

**Kutiladigan natija:** Murakkablikni yashiradi, doim yangi.

### 4. Mart nomi · oson

Moliya bo'limi uchun mart nomi va maqsadini yozing.

**Kutiladigan natija:** `mart_moliya` va maqsad.

### 5. mart_oquvchilar · o'rta

`mart_oquvchilar` VIEW ini yarating.

**Kutiladigan natija:** 15 qator.

### 6. 2024 filtri · o'rta

Martdan 2024-yil ma'lumotini kamayish tartibida chiqaring.

**Kutiladigan natija:** Samarqand eng yuqorida.

### 7. Natijani bashorat qiling · o'rta

`SELECT COUNT(*) FROM mart_oquvchilar` nechta qator beradi?

**Kutiladigan natija:** 15.

### 8. mart_yuklama · o'rta

Nisbat va toifa bilan `mart_yuklama` ni yarating.

**Kutiladigan natija:** 15 qator va 3 toifa.

### 9. Toifalar soni · qiyin

2024-yil uchun toifalar bo'yicha hududlar sonini toping.

**Kutiladigan natija:** Yuqori 1, O'rta 3, Normal 1.

### 10. Xatoni toping · qiyin

`nisbat = oquvchilar / oqituvchilar` butun bo'linma beradi. Nega va qanday tuzatiladi?

**Kutiladigan natija:** Butun bo'linma; `1.0 *` qo'shiladi.

### 11. Hududlar bo'yicha o'rtacha · qiyin

`mart_yuklama` dan har hudud uchun o'rtacha nisbatni toping.

**Kutiladigan natija:** 5 qator.

### 12. O'z martingiz · bonus

`maktablar` jadvalidan `mart_maktablar` yarating va ta'rif yozing.

**Kutiladigan natija:** VIEW va ta'rif.

## O'zingizni tekshiring

1. Data Mart nima?
2. DWH va mart farqi nima?
3. `VIEW` nima va u ma'lumotni saqlaydimi?
4. Conformed dimension nima?
5. `1.0 *` nima uchun yoziladi?
6. Mart hujjatida nimalar bo'lishi kerak?
7. Qachon jadval mart yaratiladi?

## Uyga vazifa

O'z soha martingizni yarating va 5 ta so'rov yozing (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
