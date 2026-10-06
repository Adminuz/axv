# 18-dars. HAVING filtrlash operatori (WHERE vs HAVING)

> Ba'zan hisobotda faqat muhim guruhlar kerak: katta shaharlar, ko'p sotuvli toifalar. Bugun HAVING bilan guruhlarni filtrlaymiz va WHERE bilan farqini aniq bilib olamiz.

## Dars xulosasi

- `HAVING` guruhlangan natijani filtrlaydi.
- `WHERE` qatorlarni guruhlashdan oldin filtrlaydi.
- Aggregatsiya sharti faqat `HAVING` da yoziladi.
- Tartib: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY.
- Qator shartini `WHERE` ga, guruh shartini `HAVING` ga yozing.
- Ikkala filtr bir so'rovda birga ishlaydi.

## Qo'shimcha ma'lumot

### Alias va HAVING
T-SQL'da HAVING da alias ishlamaydi.

### HAVING COUNT(*)
Eng ko'p ishlatiladigan shakl.

### Samaradorlik
WHERE kamroq qatorni guruhlaydi.

### Bir nechta shart
HAVING da AND/OR ishlatiladi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| HAVING | Guruh filtri |
| WHERE | Qator filtri |
| Aggregatsiya | Qatorlarni jamlash |
| Guruh | GROUP BY natijasi |
| Bajarilish tartibi | Mantiqiy ketma-ketlik |
| Alias | AS bilan nom |
| COUNT | Sanash |
| SUM | Yig'indi |

## Bilasizmi?

- `HAVING` so'zi ingliz tilida «ega bo'lgan» degani: «... ga ega bo'lgan guruhlar».
- Ko'p bazalar optimizatori ba'zi qator shartlarini `HAVING` dan `WHERE` ga o'zi ko'chiradi, lekin buni kutmasdan to'g'ri yozing.
- MySQL'da `HAVING` da alias ishlaydi, SQL Server'da esa yo'q.

## Topshiriqlar

### 1. Katta shaharlar · oson

Jami summasi 4 000 000 dan katta shaharlarni toping.

**Kutiladigan natija:** Samarqand; Toshkent

### 2. Ko'p sotuv · oson

Kamida 3 ta sotuvi bor shaharlarni toping.

**Kutiladigan natija:** Toshkent; Samarqand; Buxoro

### 3. Toifa soni · oson

2 tadan ko'p sotuvi bor toifalarni toping.

**Kutiladigan natija:** Aksessuar 5; Kompyuter 3

### 4. HAVING joyi · oson

`HAVING` qayerga yoziladi?

**Kutiladigan natija:** GROUP BY dan keyin

### 5. Qimmat toifa · o'rta

O'rtacha summasi 2 000 000 dan katta toifa.

**Kutiladigan natija:** Kompyuter

### 6. Kichik shahar · o'rta

Jami summasi 4 000 000 dan kam shaharni toping.

**Kutiladigan natija:** Buxoro 3 360 000

### 7. WHERE yoki HAVING · o'rta

`Shahar = N'Toshkent'` shartini qayerga yozasiz? Asoslang.

**Kutiladigan natija:** WHERE: qator sharti

### 8. Juftliklar · o'rta

Shahar+toifa bo'yicha 1 dan ko'p sotuvli juftliklar.

**Kutiladigan natija:** Buxoro–Aksessuar; Toshkent–Aksessuar

### 9. Birga · qiyin

Ekransiz, jami 3 500 000 dan katta shaharlar, jami bo'yicha kamayish.

**Kutiladigan natija:** Samarqand 7 740 000

### 10. Eng katta chek · qiyin

Eng katta summasi 3 000 000 dan oshgan shaharlar.

**Kutiladigan natija:** Samarqand; Toshkent; Buxoro

### 11. Xatoni toping · qiyin

`WHERE SUM(Summa) > 100` ni tuzating.

**Kutiladigan natija:** HAVING

### 12. O'z hisoboti · bonus

Biznes savol o'ylab toping va WHERE + GROUP BY + HAVING bilan yeching.

**Kutiladigan natija:** Mustaqil so'rov

## O'zingizni tekshiring

1. HAVING nimani filtrlaydi?
2. WHERE nimani filtrlaydi?
3. Bajarilish tartibi qanday?
4. Aggregatsiya sharti qayerda?
5. Qator shartini qayerga yozamiz?
6. HAVING qayerga yoziladi?

## Uyga vazifa

HAVING bilan 6 ta hisobot so'rovini yozing (30–40 daqiqa). To'liq shart: `uyga-vazifa.md`.
