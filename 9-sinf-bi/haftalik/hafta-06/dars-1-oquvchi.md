# 16-dars. Aggregatsiya funksiyalari: COUNT, SUM, AVG, MIN, MAX

> Biznes savollari ko'pincha «nechta», «jami qancha», «o'rtacha qancha» bilan boshlanadi. Bugun SQL'da shu savollarga bitta so'rov bilan javob berishni o'rganamiz.

## Dars xulosasi

- Aggregatsiya ko'p qatorni bitta qiymatga jamlaydi.
- `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` — asosiy funksiyalar.
- `COUNT(*)` barcha qatorni, `COUNT(ustun)` NULL bo'lmaganlarni sanaydi.
- `SUM`, `AVG`, `MIN`, `MAX` NULL ni o'tkazib yuboradi.
- `INT` ustunida `AVG` uchun `CAST AS DECIMAL` ishlating.
- `AS` bilan natija ustuniga nom bering.

## Qo'shimcha ma'lumot

### COUNT(DISTINCT)
Takrorlanmas qiymatlar sonini sanaydi; 19-darsda o'rganiladi.

### ISNULL / COALESCE
NULL ni boshqa qiymatga almashtirib, aggregatsiyaga kiritish mumkin.

### Ish tezligi
Katta jadvalda aggregatsiya indeks yordamida tezlashadi.

### SUM(Narx * Soni)
Funksiya ichida ifoda yozish mumkin.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Aggregatsiya | Qatorlarni jamlash |
| COUNT | Sanash |
| SUM | Yig'indi |
| AVG | O'rtacha |
| MIN | Eng kichik |
| MAX | Eng katta |
| Alias | AS bilan berilgan nom |
| NULL | Noma'lum qiymat |

## Bilasizmi?

- `COUNT_BIG` funksiyasi 2 mlrd dan ko'p qatorni sanash uchun mo'ljallangan.
- Ko'pgina BI vositalari (Power BI, Tableau) hisobotdagi «jami» va «o'rtacha» ni aynan shu SQL funksiyalari orqali yoki ularga o'xshash mantiq bilan hisoblaydi.
- `STRING_AGG` funksiyasi matnlarni bitta qatorga yig'adi (SQL Server 2017+).

## Topshiriqlar

### 1. Mahsulotlar soni · oson

`Mahsulotlar` jadvalidagi qatorlar sonini toping.

**Kutiladigan natija:** 6

### 2. Jami dona · oson

Ombordagi jami dona (`Soni` yig'indisi) nechta?

**Kutiladigan natija:** 68

### 3. Eng arzon narx · oson

Eng arzon mahsulot narxini toping.

**Kutiladigan natija:** 80 000

### 4. Eng qimmat narx · oson

Eng qimmat mahsulot narxini toping.

**Kutiladigan natija:** 7 500 000

### 5. O'rtacha narx · o'rta

`Mahsulotlar` bo'yicha o'rtacha narxni AS bilan chiqaring.

**Kutiladigan natija:** ≈ 2 158 333,33

### 6. Aksessuarlar · o'rta

Aksessuar toifasidagi mahsulotlar sonini toping.

**Kutiladigan natija:** 3

### 7. Samarqand sotuvlari · o'rta

Samarqanddagi sotuvlar yig'indisini hisoblang.

**Kutiladigan natija:** 9 640 000

### 8. Sanalar oralig'i · o'rta

`Sotuvlar` dagi birinchi va oxirgi sanani toping.

**Kutiladigan natija:** 2024-03-01 va 2024-03-05

### 9. COUNT farqi · qiyin

`COUNT(*)` va `COUNT(Chegirma)` ni bitta so'rovda chiqaring va farqini tushuntiring.

**Kutiladigan natija:** 10 va 5

### 10. Chegirma o'rtachasi · qiyin

NULL ni o'tkazib va 0 deb hisoblab ikki xil o'rtachani toping.

**Kutiladigan natija:** 111 600 va 55 800

### 11. To'g'ri o'rtacha · qiyin

O'rtacha miqdorni (Miqdor) kasr bilan chiqaring.

**Kutiladigan natija:** 1.200000

### 12. Mini hisobot · bonus

Bitta so'rovda: sotuvlar soni, jami, o'rtacha, eng katta chek.

**Kutiladigan natija:** 10; 18 380 000; 1 838 000; 7 500 000

## O'zingizni tekshiring

1. Aggregatsiya nima?
2. COUNT(*) va COUNT(ustun) farqi?
3. NULL aggregatsiyada nima bo'ladi?
4. INT da AVG nega butun chiqadi?
5. WHERE aggregatsiyadan oldinmi yoki keyinmi?
6. AS nima uchun kerak?

## Uyga vazifa

Mahsulotlar va Sotuvlar bo'yicha 6 ta aggregatsiya so'rovi yozing (30–40 daqiqa). To'liq shart: `uyga-vazifa.md`.
