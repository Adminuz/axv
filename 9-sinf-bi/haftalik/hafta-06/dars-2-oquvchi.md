# 17-dars. GROUP BY operatori va guruhlash mexanizmi

> Jami raqam yaxshi, lekin qaysi shahar yoki toifa qancha beryapti? Bugun GROUP BY bilan hisobotni qismlarga ajratishni o'rganamiz.

## Dars xulosasi

- `GROUP BY` qatorlarni guruhlarga ajratadi.
- Har guruh uchun aggregatsiya alohida hisoblanadi.
- `SELECT` ustuni funksiyada yoki `GROUP BY` da bo'lishi shart.
- Ikki ustun bo'yicha guruhlash kombinatsiyalarni beradi.
- `WHERE` guruhlashdan oldin filtrlaydi.
- Tartib uchun `ORDER BY` ishlating.

## Qo'shimcha ma'lumot

### Pivot jadval
Excel'dagi Pivot jadval GROUP BY ga o'xshash ishlaydi.

### Guruh va indeks
Katta jadvalda guruhlash indeks bilan tezlashadi.

### COUNT(*) va guruh
Har guruhdagi qatorlar sonini beradi.

### NULL guruhi
NULL qiymatlar alohida guruh bo'ladi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| GROUP BY | Guruhlash operatori |
| Guruh | Bir xil qiymatli qatorlar |
| Aggregatsiya | Qatorlarni jamlash |
| Alias | AS bilan nom |
| ORDER BY | Saralash |
| WHERE | Qator filtri |
| Kombinatsiya | Ikki ustun juftligi |
| Reyting | Kamayish tartibida jadval |

## Bilasizmi?

- `GROUP BY` natijasi kafolatlangan tartibda chiqmaydi — tartib uchun doim `ORDER BY` yozing.
- Guruhlash ichida NULL qiymatlar bitta alohida guruh bo'ladi.
- Power BI va Excel'dagi Pivot jadval aslida GROUP BY ning vizual ko'rinishi.

## Topshiriqlar

### 1. Shaharlar soni · oson

Har bir shahar uchun sotuvlar sonini chiqaring.

**Kutiladigan natija:** Toshkent 4; Samarqand 3; Buxoro 3

### 2. Toifa yig'indisi · oson

Har bir toifa bo'yicha jami summani hisoblang.

**Kutiladigan natija:** Aksessuar 680 000; Ekran 3 800 000; Kompyuter 13 900 000

### 3. Sana bo'yicha · oson

Har kunlik sotuvlar sonini chiqaring.

**Kutiladigan natija:** Har kunga 2 ta

### 4. Nom berish · oson

Natija ustunlariga `AS` bilan nom bering.

**Kutiladigan natija:** Soni, Jami

### 5. Saralash · o'rta

Shaharlarni jami summa bo'yicha kamayish tartibida chiqaring.

**Kutiladigan natija:** Samarqand birinchi

### 6. O'rtacha chek · o'rta

Har bir shahar bo'yicha o'rtacha summani toping.

**Kutiladigan natija:** Toshkent 1 345 000; Samarqand ≈ 3 213 333,33; Buxoro 1 120 000

### 7. Faqat aksessuar · o'rta

Aksessuar sotuvlarini shaharlar bo'yicha jamlang.

**Kutiladigan natija:** Toshkent 280 000; Samarqand 240 000; Buxoro 160 000

### 8. Ikki ustun · o'rta

Shahar va toifa bo'yicha sotuvlar sonini chiqaring.

**Kutiladigan natija:** 8 qator

### 9. Eng katta chek · qiyin

Har bir shahar uchun eng katta va eng kichik summani toping.

**Kutiladigan natija:** Samarqand 7 500 000 / 240 000

### 10. Xatoni toping · qiyin

`SELECT Shahar, Summa FROM Sotuvlar GROUP BY Shahar` xatosini tuzating.

**Kutiladigan natija:** `SUM(Summa)` bilan

### 11. Chegirma · qiyin

Har shahar bo'yicha chegirma yig'indisini va soni chiqaring.

**Kutiladigan natija:** Buxoro 328 000; Samarqand 24 000; Toshkent 206 000

### 12. Mahsulot toifalari · bonus

`Mahsulotlar` bo'yicha har toifaning ombor qiymatini (Narx × Soni) toping.

**Kutiladigan natija:** Aksessuar 5 960 000; Ekran 7 600 000; Kompyuter 41 700 000

## O'zingizni tekshiring

1. GROUP BY nima qiladi?
2. SELECT qoidasi qanday?
3. WHERE qachon ishlaydi?
4. Ikki ustun bo'yicha qanday guruhlanadi?
5. Alias qayerda ishlaydi?
6. Guruhlar soni nimaga teng?

## Uyga vazifa

Sotuvlar bo'yicha 6 ta guruhlash so'rovini yozing (30–40 daqiqa). To'liq shart: `uyga-vazifa.md`.
