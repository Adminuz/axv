# 16-dars. DRY prinsipi va Pythonda funksiyalar (def)

> Bir xil kodni ko'p joyga nusxalash tez, lekin xavfli. Bugun DRY prinsipini va funksiyalarni o'rganamiz: formulani bir marta yozib, hamma joyda ishlatamiz.

## Dars xulosasi

- DRY — kodni takrorlama, bitta joyga jamla.
- `def nom(parametr): ...` — funksiya e'loni.
- `return` natijani qaytaradi, `print` ekranga chiqaradi.
- Parametrga standart qiymat berish mumkin.
- Uzun `if/elif` o'rniga `dict` ishlating.
- Funksiya bitta ish qilsin va nomi uni aytsin.

## Qo'shimcha ma'lumot

### Docstring
Funksiyaning tavsifi.

### `*args`
Ixtiyoriy sondagi argument.

### Lokal o'zgaruvchi
Faqat funksiya ichida ishlaydi.

### `lambda`
Qisqa nomsiz funksiya.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| DRY | Don't Repeat Yourself |
| Funksiya | Qayta ishlatiladigan kod bloki |
| def | Funksiya e'loni |
| Parametr | E'londagi nom |
| Argument | Chaqirishdagi qiymat |
| return | Natijani qaytarish |
| None | Qiymat yo'qligi |
| Lug'at | dict: kalit–qiymat |

## Bilasizmi?

- Python'da funksiya ham qiymat: uni o'zgaruvchiga yoki boshqa funksiyaga berish mumkin.
- Funksiya birinchi qatoridagi uch qo'shtirnoqli matn — docstring: funksiyani tushuntiradi (`help(f)`).
- `*args` va `**kwargs` funksiyaga ixtiyoriy sondagi argument berishga imkon beradi.

## Topshiriqlar

### 1. DRY · oson

DRY ni o'z so'zlaringiz bilan tushuntiring.

**Kutiladigan natija:** Kodni takrorlamaslik.

### 2. def · oson

Funksiya e'loni qaysi so'z bilan boshlanadi?

**Kutiladigan natija:** `def`.

### 3. Chaqirish · oson

`salom_ber()` funksiyasini chaqiring.

**Kutiladigan natija:** `salom_ber()`.

### 4. Parametr · oson

Parametr va argument farqini yozing.

**Kutiladigan natija:** E'londagi nom / berilgan qiymat.

### 5. Kvadrat · o'rta

Sonning kvadratini qaytaring.

**Kutiladigan natija:** `return x * x`.

### 6. Standart qiymat · o'rta

`ism="Mehmon"` parametrli funksiya yozing.

**Kutiladigan natija:** Standart qiymatli salom.

### 7. return va print · o'rta

Farqini misol bilan yozing.

**Kutiladigan natija:** print ko'rsatadi, return qaytaradi.

### 8. Takrorni toping · o'rta

Berilgan kodda takrorni toping va funksiyaga aylantiring.

**Kutiladigan natija:** Funksiya yozildi.

### 9. dict bilan · qiyin

Hafta kunlari (1–7) nomini dict bilan qaytaring.

**Kutiladigan natija:** dict va get.

### 10. Ikki qiymat · qiyin

Ro'yxat min va maxini qaytaring.

**Kutiladigan natija:** `return min(s), max(s)`.

### 11. Do'kon · qiyin

Chegirma va soliq bilan jami narx funksiyasi.

**Kutiladigan natija:** To'g'ri hisob.

### 12. Mini kalkulyator · bonus

4 amalli funksiyalar to'plamini yozing.

**Kutiladigan natija:** qo'sh, ayir, ko'paytir, bo'l.

## O'zingizni tekshiring

1. DRY nima?
2. Funksiya qanday e'lon qilinadi?
3. Parametr va argument?
4. return va print farqi?
5. Standart qiymat nima?
6. dict bilan DRY qanday?

## Uyga vazifa

Do'kon hisobini funksiyalar bilan yozing (30–40 daqiqa). To'liq shart: `uyga-vazifa.md`.
