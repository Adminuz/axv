# 16-dars. Responsiv maket amaliyoti: mobil, planshet va desktop uchun sahifa

**Fan:** Web Full-stack dasturlash
**Sinf:** 8-sinf
**Hafta:** 6-hafta, 1-dars (umumiy 16-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** O'quv dasturi, 7-mavzu «Moslashuvchan (responsiv) dizayn va media so'rovlar va Figma»: «mobil-first va desktop-first yondashuvlar, rasm va kontentni moslashtirish (responsive images, max-width, height: auto, object-fit)». `clamp()`, `aspect-ratio`, `srcset` va `<picture>` standart MDN hujjatlariga ko'ra qo'shildi.

---

## Darsning maqsadi

O'quvchilarga 15-darsdagi nazariyani amalda qo'llab, to'liq bir sahifani (header-menyu, hero, kartalar, footer) mobile-first usulida yaratishni, nisbiy o'lchamlar (`rem`, `%`, `clamp()`), moslashuvchan rasmlar (`max-width`, `object-fit`, `aspect-ratio`, `srcset`) va uch breakpoint (telefon, planshet, kompyuter) bilan ishlashni o'rgatish.

## Kutiladigan natija

- Mobile-first CSS yozadi: asosiy qoidalar telefon uchun, kengroq ekran uchun `min-width`;
- `rem`, `%` va `clamp()` bilan matn va masofalarni moslashtiradi;
- Rasmni `max-width: 100%`, `object-fit` va `aspect-ratio` bilan toshirmasdan joylaydi;
- Menyuni telefonda ustun, kompyuterda qator qilib o'zgartiradi;
- Sahifani DevTools'ning qurilma rejimida 3 xil kenglikda tekshiradi.

## Kerakli jihozlar

- Kompyuter, brauzer va VS Code
- Brauzer DevTools (Ctrl+Shift+M — qurilma rejimi)
- Bir nechta rasm (kamida 3 ta) va 14-darsdagi maket

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 00–08 | Takrorlash | 15-dars: viewport, @media, breakpoint |
| 08–22 | Yangi mavzu 1 | Mobile-first asos: nisbiy o'lchamlar va menyu |
| 22–32 | Yangi mavzu 2 | Moslashuvchan rasmlar va kartalar |
| 32–38 | Tanaffus + mini-quiz | Slayddagi `.quiz` |
| 38–50 | Yangi mavzu 3 | Loyiha: «Maktab sayti» sahifasi uch breakpointda |
| 50–75 | Amaliyot | Tekshirish, xatolar, xulosa |
| 75–80 | Xulosa | Tezkor nazorat, uyga vazifa |

---

## Konspekt (mentor aytadigan matn)

### 1. Mobile-first asos: nisbiy o'lchamlar va menyu

Mobile-first — avval **telefon** uchun yoziladi, keyin `min-width` bilan kengaytiriladi. Telefon uchun asos: `* { box-sizing: border-box; }`, konteyner `width: 90%; max-width: 1100px; margin: 0 auto`. Matn va masofalar uchun piksel o'rniga **`rem`** (1rem = brauzerdagi asosiy shrift, odatda 16px) ishlatiladi: foydalanuvchi shriftni kattalashtirsa, sahifa ham moslashadi. Sarlavha o'lchami uchun **`clamp(min, ideal, max)`**: `font-size: clamp(1.5rem, 5vw, 2.5rem)` — ekran bilan o'sadi, lekin 1.5rem dan kichik va 2.5rem dan katta bo'lmaydi. Menyu telefonda **ustun** (`flex-direction: column`), 768px dan boshlab **qator** bo'ladi.

Brauzerda matn o'lchamini piksel bilan qotirib qo'ymang: `rem` foydalanuvchi sozlamasini hurmat qiladi. Tugmalar telefonda barmoq bilan bosishga qulay bo'lishi uchun kamida 44×44px bo'lsin.

### 2. Moslashuvchan rasmlar va kartalar

Rasm konteynerdan toshib ketmasligi uchun: `img { max-width: 100%; height: auto; display: block; }`. Kartalardagi rasmlar bir xil ko'rinishda bo'lishi uchun **`aspect-ratio: 16 / 9`** (nisbat) va **`object-fit: cover`** (rasm kesilib, butun maydonni to'ldiradi) ishlatiladi. HTML tomondan: **`srcset`** va **`sizes`** brauzerga turli o'lchamdagi fayllardan mosini tanlash imkonini beradi (telefonga kichik, kompyuterga katta rasm yuklanadi, trafik tejaladi), **`<picture>`** esa turli ekranlar uchun turli rasm ko'rsatadi. Kartalar uchun Grid: telefonda 1 ustun, planshetda 2, kompyuterda 3 ustun (`repeat(3, 1fr)`).

`object-fit: cover` rasmni kesishi mumkin: muhim qismi (masalan, yuz) chetga tushmasligi uchun rasmni tekshiring. Har rasmda `alt` matnini yozing.

### 3. Loyiha: uch breakpointli sahifa

Endi hammasini birlashtiramiz. Sahifa: **header** (logo va menyu), **hero** (sarlavha va tugma), **kartalar** (3–6 ta) va **footer**. Ishlash tartibi: 1) HTML ni semantik teglar bilan yozing (`header`, `nav`, `main`, `section`, `footer`); 2) telefon uchun CSS (breakpointsiz); 3) DevTools da kenglikni asta kengaytirib, sahifa «buzilgan» joyda breakpoint qo'shing (kontentga qarab, qurilmaga emas); 4) 768px va 992px da tekshiring; 5) Ctrl+Shift+M bilan qurilma rejimida 375px, 768px va 1280px kenglikni ko'ring. Gorizontal skroll chiqmasligi shart.

Breakpoint qiymatini qurilma nomiga emas, sahifangiz «buzilgan» joyiga qarab tanlang. Odatda 768px va 992px ham yetarli.

---

## Kod namunasi

«Maktab sayti» sahifasi (HTML va CSS):

```html
<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Maktab sayti</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header class="konteyner">
    <h1>Mening maktabim</h1>
    <nav class="menyu"><a href="#">Bosh sahifa</a><a href="#">Yangiliklar</a><a href="#">Aloqa</a></nav>
  </header>
  <main class="konteyner">
    <section class="hero"><h2>Xush kelibsiz!</h2><a class="tugma" href="#">Batafsil</a></section>
    <section class="kartalar">
      <article class="karta"><img src="rasm1.jpg" alt="Sinf xonasi"><h3>Sinf</h3></article>
      <article class="karta"><img src="rasm2.jpg" alt="Kutubxona"><h3>Kutubxona</h3></article>
      <article class="karta"><img src="rasm3.jpg" alt="Sport zali"><h3>Sport</h3></article>
    </section>
  </main>
  <footer>© 2025 Maktab</footer>
</body>
</html>
```

style.css:

```css
* { box-sizing: border-box; }
body { font-family: Arial, sans-serif; margin: 0; }
.konteyner { width: 90%; max-width: 1100px; margin: 0 auto; }
h1 { font-size: clamp(1.5rem, 5vw, 2.5rem); }
.menyu { display: flex; flex-direction: column; gap: 8px; }
.hero { padding: 2rem 1rem; text-align: center; background: #eef; }
.tugma { display: inline-block; padding: 12px 24px; background: #17e; color: #fff; }
.kartalar { display: grid; grid-template-columns: 1fr; gap: 16px; margin: 16px 0; }
img { max-width: 100%; height: auto; display: block; }
.karta img { width: 100%; aspect-ratio: 16 / 9; object-fit: cover; }
footer { padding: 1rem; text-align: center; }

@media (min-width: 768px) {
  .menyu { flex-direction: row; gap: 24px; }
  .kartalar { grid-template-columns: repeat(2, 1fr); }
}
@media (min-width: 992px) {
  .hero { padding: 5rem 1rem; }
  .kartalar { grid-template-columns: repeat(3, 1fr); }
}
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Menyu yo'nalishi
Menyu telefonda ustun, 768px dan qator bo'lsin.

**Kutiladigan natija:** Moslashuvchan menyu.

**Yechim:** 
```css
.menyu { display: flex; flex-direction: column; gap: 8px; }
@media (min-width: 768px) {
  .menyu { flex-direction: row; gap: 24px; }
}
```

### 2-topshiriq (oson). Sarlavha o'lchami
`h1` o'lchami 1.5rem dan 2.5rem gacha ekranga qarab o'zgarsin.

**Kutiladigan natija:** Clamp bilan o'lcham.

**Yechim:** 
```css
h1 { font-size: clamp(1.5rem, 5vw, 2.5rem); }
```

### 3-topshiriq (o'rta). Rasm toshmasin
Barcha rasmlar konteynerga sig'sin va nisbati buzilmasin.

**Kutiladigan natija:** Rasm moslashdi.

**Yechim:** 
```css
img { max-width: 100%; height: auto; display: block; }
```

### 4-topshiriq (o'rta). Bir xil karta rasmi
Karta rasmlari 16:9 nisbatda bo'lib, maydonni to'ldirsin.

**Kutiladigan natija:** Bir xil rasmlar.

**Yechim:** 
```css
.karta img { width: 100%; aspect-ratio: 16 / 9; object-fit: cover; }
```

### 5-topshiriq (qiyin). 1 → 2 → 3 ustun
Kartalar telefonda 1, ≥768px da 2, ≥992px da 3 ustunda bo'lsin.

**Kutiladigan natija:** Uch breakpoint.

**Yechim:** 
```css
.kartalar { display: grid; grid-template-columns: 1fr; gap: 16px; }
@media (min-width: 768px) { .kartalar { grid-template-columns: repeat(2, 1fr); } }
@media (min-width: 992px) { .kartalar { grid-template-columns: repeat(3, 1fr); } }
```

### 6-topshiriq (qo'shimcha). Gorizontal skroll
Tor ekranda gorizontal skroll chiqdi. Qaysi 3 sababni tekshirasiz?

**Kutiladigan natija:** Sabablar topildi.

**Yechim:** Qotirilgan `width` (px), `max-width: 100%` yo'q rasm, uzun so'z yoki jadval; DevTools da toshib turgan elementni toping.

---

## Tezkor nazorat (dars oxirida)

1. Mobile-first nima? — Avval telefon CSS, keyin `min-width`.
2. `rem` nimaga nisbatan? — Asosiy shrift o'lchamiga.
3. `clamp()` nechta qiymat oladi? — Uchta: min, ideal, max.
4. Rasm toshmasligi uchun nima yoziladi? — `max-width: 100%; height: auto;`.
5. Breakpoint qanday tanlanadi? — Sahifa buzilgan kenglikka qarab.

## Keng tarqalgan xatolar

- `viewport` meta tegini unutish.
- Qotirilgan `width: 800px` ishlatish.
- Rasmga `alt` yozmaslik.
- Breakpoint ni faqat bitta telefon uchun tanlash.
- Faqat bitta kenglikda tekshirish.

## Bilasizmi? (qo'shimcha)

- `<picture>` teg turli ekranlar uchun turli rasmni ko'rsata oladi (masalan, telefonda kvadrat, kompyuterda keng).
- `@media (orientation: landscape)` telefon yotiq holatini aniqlaydi.
- Yangi CSS da `container queries` komponentni ekranga emas, ota elementga qarab moslashtiradi.
