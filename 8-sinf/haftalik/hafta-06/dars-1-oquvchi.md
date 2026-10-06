# 16-dars. Responsiv maket amaliyoti: mobil, planshet va desktop uchun sahifa

> 15-darsda nazariyani o'rgandik. Bugun amalda: bitta sahifani telefon, planshet va kompyuter uchun moslashtiramiz va DevTools'da sinab ko'ramiz.

## Dars xulosasi

- Mobile-first: avval telefon, keyin `min-width`.
- Matn va masofalar uchun `rem`, sarlavhaga `clamp()`.
- Rasm: `max-width: 100%`, `aspect-ratio`, `object-fit`.
- `srcset` va `<picture>` mos rasm tanlashga yordam beradi.
- Breakpoint — sahifa buzilgan joyda qo'shiladi.
- Hamma kengliklarda tekshiring, gorizontal skroll bo'lmasin.

## Qo'shimcha ma'lumot

### Fluid grid
`%` va `fr` bilan moslashuvchan to'r.

### Container query
Ota element o'lchamiga qarab stil.

### `dvh`
Mobil brauzerdagi haqiqiy balandlik birligi.

### Dark mode
`prefers-color-scheme` qoidasi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Mobile-first | Avval telefon uchun CSS |
| Breakpoint | Maket o'zgaradigan kenglik |
| rem | Asosiy shriftga nisbatan birlik |
| clamp() | Chegaralangan moslashuvchan qiymat |
| aspect-ratio | Eni va bo'yi nisbati |
| object-fit | Rasmni maydonga joylash usuli |
| srcset | Rasm variantlari ro'yxati |
| viewport | Ko'rinish oynasi |

## Bilasizmi?

- `<picture>` teg turli ekranlar uchun turli rasmni ko'rsata oladi (masalan, telefonda kvadrat, kompyuterda keng).
- `@media (orientation: landscape)` telefon yotiq holatini aniqlaydi.
- Yangi CSS da `container queries` komponentni ekranga emas, ota elementga qarab moslashtiradi.

## Topshiriqlar

### 1. Mobile-first · oson

Mobile-first yondashuvini bir jumlada yozing.

**Kutiladigan natija:** Avval telefon, keyin kengroq.

### 2. Viewport · oson

Viewport meta tegini yozing.

**Kutiladigan natija:** `width=device-width, initial-scale=1.0`.

### 3. rem birligi · oson

1rem odatda necha piksel?

**Kutiladigan natija:** 16px.

### 4. Rasm qoidasi · oson

Rasm toshmasligi uchun 2 xossa yozing.

**Kutiladigan natija:** `max-width: 100%; height: auto;`.

### 5. Clamp · o'rta

`h1` uchun `clamp` yozing: 1.5rem–2.5rem.

**Kutiladigan natija:** `clamp(1.5rem, 5vw, 2.5rem)`.

### 6. Menyu · o'rta

Menyuni ≥768px da qatorga o'tkazing.

**Kutiladigan natija:** `flex-direction: row`.

### 7. Karta nisbati · o'rta

Karta rasmi 16:9 bo'lsin.

**Kutiladigan natija:** `aspect-ratio: 16 / 9`.

### 8. object-fit · o'rta

`cover` va `contain` farqini yozing.

**Kutiladigan natija:** cover kesadi, contain sig'diradi.

### 9. Ustunlar · qiyin

1/2/3 ustunli Grid yozing.

**Kutiladigan natija:** `repeat(2, 1fr)`, `repeat(3, 1fr)`.

### 10. Skroll sababi · qiyin

Gorizontal skroll sababini toping.

**Kutiladigan natija:** Qotirilgan kenglik yoki katta rasm.

### 11. DevTools · qiyin

Qurilma rejimini qanday ochasiz?

**Kutiladigan natija:** Ctrl+Shift+M.

### 12. Sahifa loyihasi · bonus

O'z sahifangizga 4-bo'lim qo'shib, moslashtiring.

**Kutiladigan natija:** Hamma kenglikda ishlaydi.

## O'zingizni tekshiring

1. Mobile-first nima?
2. `rem` nimaga nisbatan?
3. `clamp()` nima beradi?
4. Rasm qanday moslashtiriladi?
5. Breakpoint qanday tanlanadi?
6. DevTools da qanday tekshiriladi?

## Uyga vazifa

«Maktab sayti» sahifasini tugating va 3 kenglikda tekshiring (30–40 daqiqa). To'liq shart: `uyga-vazifa.md`.
