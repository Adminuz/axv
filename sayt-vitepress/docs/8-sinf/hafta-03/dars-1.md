---
title: "7-dars. HTML5 semantik teglari: <header>, <nav>, <main>, <section>, <article>, <aside>, <footer>"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "8-sinf", "link": "/8-sinf/"}, "week": {"n": 3, "link": "/8-sinf/hafta-03/"}, "g": 7, "title": "HTML5 semantik teglari: <header>, <nav>, <main>, <section>, <article>, <aside>, <footer>", "lead": "Veb-sahifalarni «div sho'rvasi»dan qutqarish, brauzerlar va qidiruv tizimlari uchun tushunarli toza arxitektura hamda HTML5 semantika san'ati.", "slide": "/slaydlar/8-sinf/hafta-03/dars-1.html", "tabs": [{"g": 7, "link": "/8-sinf/hafta-03/dars-1", "current": true}, {"g": 8, "link": "/8-sinf/hafta-03/dars-2", "current": false}, {"g": 9, "link": "/8-sinf/hafta-03/dars-3", "current": false}], "prev": null, "next": {"g": 8, "title": "HTML5 multimedia va interaktiv elementlar: <video>, <audio>, <figure>, <details>, <progress>", "link": "/8-sinf/hafta-03/dars-2"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **HTML5 inqilobi:** HTML4 dagi cheksiz `<div>` lar o'rniga har bir blokning aniq mazmunini ifodalovchi maxsus semantik teglar joriy etildi.
- **Semantika nima:** Tegning shunchaki ko'rinishi emas, balki uning inson, brauzer va qidiruv botlari uchun anglatadigan ma'nosi (ma'nodoshlik).
- **Asosiy semantik karkas:** Har qanday zamonaviy sahifa `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>` va `<footer>` orqali mantiqiy bloklarga ajratiladi.
- **`<main>` tegi qoidasi:** Sahifaning asosiy va takrorlanmas qismi bo'lib, har bir sahifada qat'iy ravishda faqat **bitta** bo'lishi shart.
- **`<article>` vs `<section>`:** `<article>` mustaqil ko'chirilishi mumkin bo'lgan alohida post yoki yangilik; `<section>` esa bitta umumiy mavzuni ifodalovchi bo'limdir.
- **Foydasi (SEO va Accessibility):** Google qidiruvida saytning yuqori o'ringa chiqishi va ekrandan o'qish dasturlari (Screen Readers) orqali imkoniyati cheklangan insonlar saytdan bemalol foydalanishi uchun semantika hal qiluvchi rol o'ynaydi.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. «Div sho'rvasi» (Div Soup) kasalligi va uning davosi

2014-yilgacha deyarli barcha veb-saytlar mana bunday ko'rinishda yozilar edi:
```html
<div class="header">
  <div class="navigation-bar">
    <div class="menu-item"><a href="#">Bosh sahifa</a></div>
  </div>
</div>
<div class="content-wrapper">
  <div class="left-column">
    <div class="blog-entry">
      <div class="entry-title">Dasturlash asoslari</div>
    </div>
  </div>
  <div class="right-column">
    <div class="sidebar">...</div>
  </div>
</div>
<div class="footer">...</div>
```
Bunday kodda nima muammo bor?
Tashqaridan qaraganda sahifa chiroyli ko'rinishi mumkin, lekin kod jihatidan u bir qozon «div sho'rvasi»ga o'xshaydi. Google yoki Yandex qidiruv boti bu sahifaga kirganda, qayerda asosiy matn borligini, qayerda shunchaki reklama ekanini ajrata olmaydi. Natijada sayt qidiruv reytingida pastga tushadi.

HTML5 buni bir zumda hal qildi:
`<div>` lar o'rniga `<header>`, `<nav>`, `<main>`, `<article>`, `<aside>`, `<footer>` qo'yilishi bilan kod 3 barobar ixchamlashadi va professional arxitekturaga aylanadi!

### 2. `<article>` va `<section>` farqini qanday eslab qolish mumkin?

Dasturchilar ko'pincha bu ikki tegni adashtiradilar. Ularni eslab qolishning oltin qoidasi:
- **Tasavvur qiling — gazeta:** 
  - Gazetada «Sport xabarlari» degan butun bir sahifa yoki bo'lim bor — bu **`<section>`** (bo'lim).
  - Shu bo'lim ichida «O'zbekiston terma jamoasi g'alaba qozondi» degan alohida bitta maqola bor — bu **`<article>`** (maqola).
  - Agar siz ushbu maqolani gazetadan qirqib olib, boshqa jurnalga yoki devoriy gazetaga yopishtirsangiz ham u o'z ma'nosini yo'qotmaydi. Shuning uchun mustaqil narsalar — `<article>`, ularni jamlovchi bo'lim esa — `<section>` hisoblanadi.

### 3. Screen Reader (Ekran o'quvchi) va raqamli qulaylik (Accessibility)

Dunyoda millionlab ko'rish qobiliyati cheklangan insonlar internetdan maxsus dasturlar (NVDA, JAWS, VoiceOver) orqali foydalanishadi.
- Bu dasturlar ekrandagi matnlarni ovoz chiqarib o'qib beradi.
- Agar siz semantik teglardan foydalansangiz, foydalanuvchi klaviaturadagi bitta tugma bilan birdaniga `<main>` ga (asosiy matnga) sakrashi yoki `<nav>` orqali menyuni tinglashi mumkin.
- Agar hamma narsa `<div>` bo'lsa, ekran o'quvchi butun sayt boshidagi menyularni har bir sahifada qayta-qayta zerikarli o'qishga majbur bo'ladi.

### 4. Qachon `<div>` ishlatish joiz?

HTML5 semantikasi chiqdi degani, `<div>` ni butunlay unutish kerak degani emas!
`<div>` (Division — bo'linish) — bu hech qanday semantik ma'noga ega bo'lmagan toza konteynerdir. Uni faqat **CSS dizayni va joylashuvi (styling / layout)** uchun ishlatish kerak:
- Flexbox yoki Grid konteynerlari yasashda;
- Chiroyli ramka, soya yoki fon berishda;
- Elementlarni bir qatorga terishda (`<div class="row">`, `<div class="card-grid">`).

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **HTML5** | 2014-yilda qabul qilingan, zamonaviy multimedia va semantikani qo'llab-quvvatlovchi HTML standarti |
| **Semantika** | So'z yoki kod elementining o'z mazmuni va vazifasiga mos ma'no kasb etishi |
| **`<header>`** | Sahifa yoki bo'limning kirish (bosh) qismi: logotip, sarlavha va asosiy menyu joylashadi |
| **`<nav>`** | Saytning asosiy navigatsiya va menyu havolalari joylashadigan maxsus blok |
| **`<main>`** | Sahifadagi eng muhim, takrorlanmas asosiy kontent (sahifada faqat 1 marta keladi) |
| **`<section>`** | Sahifaning alohida mavzuli bo'limi (odatda o'z `<h2>` sarlavhasiga ega bo'ladi) |
| **`<article>`** | Saytning boshqa joyiga ko'chirilsa ham ma'nosini yo'qotmaydigan mustaqil maqola yoki post |
| **`<aside>`** | Asosiy mavzuga bevosita aloqador bo'lmagan qo'shimcha yon blok (sidebar, reklama, muallif) |
| **`<footer>`** | Sahifa yoki bo'limning quyi qismi: mualliflik huquqi, bog'lanish, ijtimoiy tarmoqlar |
| **SEO (Search Engine Optimization)** | Saytni Google va boshqa qidiruv tizimlarida yuqori o'ringa ko'tarish usullari |
| **Accessibility (a11y)** | Saytning imkoniyati cheklangan barcha insonlar uchun qulay va to'siqsiz bo'lishi |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

1. **HTML5 ning tug'ilishi:** HTML5 standarti 2004-yilda WHATWG (Apple, Mozilla, Opera mutaxassislari) tomonidan boshlangan va 2014-yil 28-oktyabrda W3C tomonidan rasman tavsiya qilingan.
2. **Google algoritmi:** Google qidiruv tizimi botlari `<header>` va `<nav>` ichidagi takrorlanuvchi so'zlarga kamroq, `<main>` va `<article>` ichidagi matnlarga esa eng yuqori baho beradi.
3. **Semantikaning mashhurligi:** Bugungi kunda dunyodagi eng yetakchi saytlarning 95 foizdan ortig'i HTML5 semantik teglari asosida yaratilgan.
4. **DOCTYPE soddaligi:** Eski HTML4 da `<!DOCTYPE ...>` yozuvi 3 qatordan iborat murakkab havola edi. HTML5 da u oddiygina `<!DOCTYPE html>` bo'lib qoldi!

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Sayt bosh qismini (`<header>` va `<nav>`) yaratish <Badge type="tip" text="oson" />
Shaxsiy saytingiz uchun `<header>` blokini tuzing. Unda `<h1>` bilan saytingiz nomi, `<p>` bilan shioringiz va `<nav>` tegi ichida 3 ta havola (`Bosh sahifa`, `Loyihalar`, `Bog'lanish`) joylashsin.
**Kutiladigan natija:** To'g'ri iyerarxiyada yozilgan semantik header bloki.

### 2. Sayt quyi qismini (`<footer>`) yaratish <Badge type="tip" text="oson" />
Sahifa so'ngi uchun `<footer>` bloki yozing. Unda mualliflik belgisi (`&copy; 2026 Ism Familiya`), maktabingiz nomi hamda Telegram va GitHub profilingizga olib boruvchi 2 ta havola bo'lsin.
**Kutiladigan natija:** Valid semantik footer kodi.

### 3. `<main>` tegini to'g'ri joylashtirish <Badge type="tip" text="oson" />
Berilgan chala kodni to'g'rilang:
```html
<header><h1>Saytim</h1></header>
<main>
  <p>Asosiy matn...</p>
</main>
<main>
  <p>Ikkinchi matn...</p>
</main>
<footer>...</footer>
```
Bitta sahifada faqat bitta `<main>` bo'lishi qoidasiga ko'ra ikkinchi `<main>` o'rniga qaysi semantik teg ishlatilishi kerakligini aniqlang va kodni to'g'rilang.
**Kutiladigan natija:** Ikki matn bitta `<main>` ichidagi alohida `<section>` larda joylashtiriladi.

### 4. Yangiliklar xabari uchun `<article>` yasash <Badge type="tip" text="oson" />
Maktabingizdagi tadbir haqida bitta yangilik `<article>`i tuzing. Unda kichik `<header>` (yangilik sarlavhasi va sanasi), asosiy matn paragrafi va oxirida teglar (masalan: `#maktab #tadbir`) joylashsin.
**Kutiladigan natija:** Mustaqil va to'liq shakllangan `<article>` kodi.

### 5. Bo'limlar (`<section>`) bilan ishlash <Badge type="warning" text="o'rta" />
Bitta `<main>` ichida 3 ta turli `<section>` yarating:
1. «Biz haqimizda» (`<h2>` sarlavha va qisqa matn).
2. «Xizmatlarimiz» (`<h2>` sarlavha va 3 ta ro'yxat bandi).
3. «Bizning jamoa» (`<h2>` sarlavha va 2 nafar o'quvchi ma'lumoti).
**Kutiladigan natija:** Mantiqiy jihatdan aniq ajratilgan 3 ta semantik section kodi.

### 6. Yon panel (`<aside>`) yaratish <Badge type="warning" text="o'rta" />
Blog sahifasi uchun `<aside>` bloki tayyorlang. Unda:
- Qidiruv formasi (`<form>` va `<input type="search">`);
- «Eng o'qilgan mavzular» ro'yxati (3 ta havola);
- Sayt muallifining qisqa biografiyasi va surati uchun joy bo'lsin.
**Kutiladigan natija:** To'g'ri shakllantirilgan va asosiy kontentga bog'liq bo'lmagan sidebar kodi.

### 7. «Div soup» kodini semantik tozalash <Badge type="warning" text="o'rta" />
Quyidagi tartibsiz eski kodni olib, uni to'liq HTML5 semantik teglari (`header`, `nav`, `main`, `section`, `footer`) bilan qayta yozing:
```html
<div id="top">
  <h2>IT Darsliklari</h2>
  <div class="links"><a href="#">Bosh</a> <a href="#">Darslar</a></div>
</div>
<div id="body">
  <div class="chapter">
    <h3>1-dars</h3>
    <p>HTML asoslari...</p>
  </div>
</div>
<div id="bottom"><p>Muallif: Ahmad</p></div>
```
**Kutiladigan natija:** Barcha `div` lar o'rniga mos semantik teglar qo'llangan toza kod.

### 8. Maqola ichida alohida `header` va `footer` qo'llash <Badge type="warning" text="o'rta" />
Bilamizki, `<header>` va `<footer>` nafaqat butun sahifa uchun, balki alohida `<article>` ichida ham ishlatilishi mumkin. Bitta ilmiy maqola (`<article>`) tuzing: uning o'z `header`ida maqola nomi va yozilgan vaqti, `footer`ida esa manbalar ro'yxati joylashsin.
**Kutiladigan natija:** Ichki semantik header/footer imkoniyatlarini to'g'ri ko'rsatuvchi kod.

### 9. Screen reader uchun semantik tahlil (Keys tahlili) <Badge type="danger" text="qiyin" />
Ko'zi ojiz inson sizning saytingizga kirdi. Agar saytda `<nav>`, `<main>`, `<aside>` teglaridan to'g'ri foydalanilgan bo'lsa, u qanday qilib darhol maqolani o'qishga o'ta oladi? Agar hamma narsa `<div>` bo'lsa, qanday qiyinchilikka duch keladi? 4-5 jumlada tushuntirib bering.
**Kutiladigan natija:** O'quvchi raqamli qulaylik (a11y) va screen reader dasturlarining semantik teglarga tayanishini amaliy tushuntiradi.

### 10. To'liq veb-portal skeletini loyihalash <Badge type="danger" text="qiyin" />
O'zbekistonning diqqatga sazovor joylariga bag'ishlangan sayt skeletini yarating:
- Umumiy `<header>` (sayt nomi va `<nav>`).
- `<main>` ichida:
  - 1-`<section>`: Kirish va O'zbekiston xaritasi haqida matn.
  - 2-`<section>`: 3 ta qadimiy shahar (Samarqand, Buxoro, Xiva) haqida 3 ta alohida `<article>`.
  - `<aside>`: Sayohat qilish bo'yicha maslahatlar va ob-havo ma'lumoti.
- Umumiy `<footer>`.
**Kutiladigan natija:** Barcha 7 ta semantik elementni qamrab olgan mukammal HTML5 sahifa hujjati.

### 11. HTML5 Validator orqali kod tozaligini tekshirish <Badge type="info" text="bonus" />
Tuzgan kodingizni rasmiy W3C HTML Validator (`validator.w3.org`) qoidalari bo'yicha tahlil qiling: hujjatingizda `lang="uz"`, `charset="UTF-8"`, to'g'ri sarlavhalar ketma-ketligi (`h1 -> h2 -> h3`) va barcha teglarning to'g'ri yopilishi talablariga 100% javob berishini ta'minlang.
**Kutiladigan natija:** Xatosiz, standartlarga to'liq mos keluvchi professional HTML5 kodi.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. HTML5 semantik teglari nima maqsadda yaratilgan?
2. `<header>` va `<head>` teglari orasidagi farq nima?
3. Nima uchun bitta sahifada bir nechta `<main>` tegi bo'lishi mumkin emas?
4. `<article>` va `<section>` teglarini qanday hollarda tanlash kerak?
5. `<aside>` tegi qanday ma'lumotlarni o'z ichiga oladi?
6. Qidiruv tizimlari (Google bot) semantik teglardan qanday foydalanadi?
7. Zamonaviy veb-ishlanmalarda `<div>` tegi qachon ishlatilishi mumkin?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. **Nazariy takrorlash:** Semantik teglar vazifasini va atamalar lug'atini yod oling.
2. **Kodni tekshirish:** 2-haftada yozgan formali sahifangizni oching va uning strukturasini `<header>`, `<main>`, `<section>`, `<footer>` teglari bilan qayta tartiblang.
3. **Amaliy vazifa:** O'zingiz yoqtirgan mavzuda (futbol, kosmos, robototexnika) 1 sahifalik to'liq semantik veb-maqola skeletini yarating.

</div>

