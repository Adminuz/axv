# 16-dars. CSS3 selektorlari, kaskadlik va Box Model arxitekturasi

> Sahifaning HTML qismi tayyor, endi uni bezash vaqti keldi. Bugun CSS ning 3 asosiy qoidasini o'rganamiz: selektor, kaskad va Box Model.

## Dars xulosasi

- CSS qoidasi: selektor, xossa va qiymat.
- Eng ko'p class selektori ishlatiladi.
- Kaskad: avval kuchlilik, keyin yozilish tartibi.
- Kuchlilik: inline 1000, id 100, class 10, teg 1.
- Box Model: content, padding, border, margin.
- `box-sizing: border-box` o'lchamni oson hisoblaydi.

## Qo'shimcha ma'lumot

### Pseudo-element
`::before`, `::after` — elementga qo'shimcha bezak.

### Margin collapse
Vertikal margin lar birlashadi.

### `:where()`
Specificity ni 0 qiladi.

### Reset
`* { margin: 0; }` kabi boshlang'ich tozalash.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Selektor | Elementni tanlash qoidasi |
| Class | Qayta ishlatiladigan nom |
| Specificity | Qoida kuchi |
| Kaskad | Qoidalar g'olibini aniqlash |
| Meros | Ota xossasi bolaga o'tishi |
| Padding | Ichki masofa |
| Margin | Tashqi masofa |
| border-box | Padding va border ni o'z ichiga oluvchi o'lcham |

## Bilasizmi?

- Brauzerdagi `Computed` bo'limi elementning yakuniy qiymatlarini ko'rsatadi.
- `:where()` selektorning specificity sini 0 qiladi.
- Yangi CSS da `@layer` bilan kaskad tartibini boshqarish mumkin.

## Topshiriqlar

### 1. Qoida tuzilishi · oson

CSS qoidasining 3 qismini yozing.

**Kutiladigan natija:** Selektor, xossa, qiymat.

### 2. Selektor yozing · oson

Barcha `p` va `.note` uchun rang bering.

**Kutiladigan natija:** 2 ta to'g'ri qoida.

### 3. Class va id · oson

Class va id farqini yozing.

**Kutiladigan natija:** Class takrorlanadi, id bitta.

### 4. Quti qatlamlari · oson

Box Model ning 4 qatlamini sanang.

**Kutiladigan natija:** Content, padding, border, margin.

### 5. Avlod va bola · o'rta

`ul li` va `ul > li` farqini yozing.

**Kutiladigan natija:** Avlod — hammasi, bola — bevosita.

### 6. Kuchni hisoblang · o'rta

`#a .b p` ning kuchini hisoblang.

**Kutiladigan natija:** 100 + 10 + 1 = 111.

### 7. Tartib · o'rta

Kuchi teng ikki qoida: qaysi biri g'olib?

**Kutiladigan natija:** Keyin yozilgani.

### 8. O'lcham hisobi · o'rta

`content-box`: 300px, padding 10px, border 1px. Umumiy kenglik?

**Kutiladigan natija:** 322px.

### 9. Hover · qiyin

Havola ustiga kelganda rangi o'zgarsin.

**Kutiladigan natija:** `a:hover` qoidasi.

### 10. Nth-child · qiyin

Jadvalning juft qatorlarini ranglang.

**Kutiladigan natija:** `tr:nth-child(even)`.

### 11. Muammo topish · qiyin

Qoida ishlamayapti: sababini DevTools da toping.

**Kutiladigan natija:** Bosib o'tayotgan qoida topildi.

### 12. Maktab kartasi · bonus

Maktab saytiga 3 ta karta (hover bilan) yarating.

**Kutiladigan natija:** Chiroyli, hoverli kartalar.

## O'zingizni tekshiring

1. CSS qoidasi tuzilishi?
2. Id va class farqi?
3. Specificity qanday hisoblanadi?
4. Box Model qatlamlari?
5. `border-box` nima?
6. Meros nima?

## Uyga vazifa

Maktab saytiga CSS qo'shing: kartalar, havolalar va `border-box` (30–40 daqiqa). To'liq shart: `uyga-vazifa.md`.
