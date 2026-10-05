---
title: "3-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "8-sinf", "link": "/8-sinf/"}, "n": 3, "bob": "I-bob · HTML tili va veb-sahifa tuzishning asoslari", "lessons": [{"g": 7, "title": "HTML5 semantik teglari: <header>, <nav>, <main>, <section>, <article>, <aside>, <footer>", "lead": "Veb-sahifalarni «div sho'rvasi»dan qutqarish, brauzerlar va qidiruv tizimlari uchun tushunarli toza arxitektura hamda HTML5 semantika san'ati.", "link": "/8-sinf/hafta-03/dars-1", "slide": "/slaydlar/8-sinf/hafta-03/dars-1.html", "test": "/slaydlar/8-sinf/hafta-03/dars-1-test.html"}, {"g": 8, "title": "HTML5 multimedia va interaktiv elementlar: <video>, <audio>, <figure>, <details>, <progress>", "lead": "Veb-sahifani video va audio bilan jonlantirish, rasmlarni ilmiy izohlash hamda JavaScriptsiz sof HTML da interaktiv bloklar yaratish sirlari.", "link": "/8-sinf/hafta-03/dars-2", "slide": "/slaydlar/8-sinf/hafta-03/dars-2.html", "test": "/slaydlar/8-sinf/hafta-03/dars-2-test.html"}, {"g": 9, "title": "HTML5 global atributlari va zamonaviy forma imkoniyatlari. I bob yakuni", "lead": "Barcha teglar uchun universal global atributlar, data-* sirlari, yangi kiritish vositalari hamda I bob bo'yicha to'liq mustaqil veb-loyiha.", "link": "/8-sinf/hafta-03/dars-3", "slide": "/slaydlar/8-sinf/hafta-03/dars-3.html", "test": "/slaydlar/8-sinf/hafta-03/dars-3-test.html"}], "test": "/slaydlar/8-sinf/hafta-03/hafta-test.html"}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Har bir vazifa 20–30 daqiqa. Fayllar alohida `hafta-03` papkasida saqlanadi.

### 7-dars uchun (HTML5 semantik teglari)
**1-topshiriq: «Toza semantik yangiliklar sahifasi»**
- `yangiliklar.html` faylini yarating.
- Unda `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>` va `<footer>` elementlaridan to'liq foydalaning.
- `<main>` ichida kamida 2 ta yangilik maqolasi (`<article>`) bo'lsin.
- Har bir maqola ichida o'zining kichik `<header>`i (sarlavha va sana) hamda `<footer>`i (manba va teglar) bo'lsin.
- **Tekshirish:** butun sahifada faqat bitta `<main>` ishlatilgan, hech qanday `<div>` ishlatilmagan (sof semantika).

### 8-dars uchun (HTML5 multimedia va interaktiv elementlar)
**2-topshiriq: «Media-galereya va savol-javoblar»**
- `media.html` faylini yarating.
- Unda kamida 1 ta video (`<video controls width="480" poster="...">`) va 1 ta audio (`<audio controls>`) pleer joylashtiring.
- Rasm va uning ostidagi ilmiy izohni `<figure>` va `<figcaption>` bilan o'rab chiqing.
- Sayt so'ngida `<details>` va `<summary>` yordamida 3 ta savoldan iborat FAQ akkordeoni hosil qiling.
- O'rganish foizini ko'rsatish uchun bitta `<progress value="85" max="100"></progress>` chizig'i qo'shing.
- **Tekshirish:** video va audio boshqaruv tugmalari ishlaydi, akkordeon bosilganda silliq ochilib-yopiladi.

### 9-dars uchun (HTML5 global atributlari va I bob yakuniy loyihasi)
**3-topshiriq: «Interaktiv shaxsiy portfolio» katta loyihasi**
- `index.html` faylini yarating.
- I bobda o'tilgan barcha bilimlarni bitta loyihaga birlashtiring:
  1. To'liq semantik tuzilma (`header`, `nav`, `main`, `footer`);
  2. Shaxsiy ma'lumotlar va surat (`figure` va `figcaption`);
  3. Texnologiyalar jadvali (`table`, `thead`, `tbody`);
  4. Muloqot formasi (`type="color"`, `type="date"`, `type="range"`, `textarea`, `required`);
  5. Sarlavhalardan biriga `contenteditable="true"` qo'shing;
  6. Ma'lumotlarga `data-*` atributlarini biriktiring.
- **Tekshirish:** xatosiz HTML5 standarti, W3C qoidalariga moslik, formaning barcha maydonlari to'g'ri ishlashi.

</div>
