# 7-dars. HTML5 semantik teglari: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`

**Hafta:** 3 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliyot · **I-bob**, 7-dars

## 1. Dars rejasi

**Maqsad:** o'quvchilarga HTML5 ning paydo bo'lish sabablari, «div sho'rvasi» (div soup) muammosi, semantik teglarning mazmuniy ahamiyati (SEO, screen readerlar, toza kod) hamda sahifaning to'liq semantik skeletini (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`) to'g'ri loyihalashni amaliy o'rgatish.

**Kutiladigan natija:**
- Semantik va nosemantik elementlar o'rtasidagi farqni tushuntira oladi (`<div class="header">` vs `<header>`).
- `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>` teglarining har birining o'z o'rni va vazifasini to'g'ri belgilaydi.
- `<article>` va `<section>` ning nozik farqini (mustaqil kontent vs mavzuli bo'lim) amalda ajrata oladi.
- Bir sahifada faqat bitta `<main>` bo'lishi shartligini biladi.
- Yangiliklar sayti yoki shaxsiy blog uchun to'liq semantik HTML5 karkasini qura oladi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va muammo qo'yish | O'tgan hafta mavzusi (formalar). Muammo: «Nega hamma joyda faqat `<div>` ishlatish yomon odat hisoblanadi?» |
| 10–30 daq | Yangi mavzu: Nazariya | HTML5 nima? Semantika tushunchasi. 7 ta asosiy semantik element anatomiyasi |
| 30–35 daq | Tanaffus | Ko'z va harakat mashqlari |
| 35–65 daq | Amaliy mashg'ulot | Veb-sahifa maketini `<div>` lardan semantik teglarga qayta yozish (refactoring) |
| 65–75 daq | Tezkor nazorat | 5 ta savol va xatolarni topish mashqi |
| 75–80 daq | Xulosa va vazifa | Mavzuni yakunlash va uyga vazifani berish |

---

## 2. Konspekt

### 2.1. Takrorlash (10 daqiqa)
- `<form>` ning `method="POST"` va `method="GET"` parametrlari bir-biridan nima bilan farq qiladi?
- `<label for="...">` va `<input id="...">` nima uchun bir xil nomga ega bo'lishi shart?

### 2.2. HTML5 nima va «Semantika» so'zi nimani anglatadi?

HTML 1990-yillardan boshlab rivojlanib kelgan. HTML4 davrida veb-sahifaning barcha bloklari faqat bitta teg — `<div>` bilan yasalgan:
```html
<!-- Eski HTML4 uslubi ("Div soup") -->
<div class="header">...</div>
<div class="nav">...</div>
<div class="main-content">
  <div class="post">...</div>
</div>
<div class="footer">...</div>
```
Bu usulning kamchiliklari:
1. Qidiruv botlari (Google, Yandex) sahifaning qaysi qismi muhim maqola, qaysi qismi menyu yoki mualliflik huquqi ekanini tushunishga qiynaladi.
2. Ko'zi ojiz insonlar foydalanadigan ovozli o'quvchi dasturlar (Screen Readers) sahifada to'g'ri navigatsiya qila olmaydi.
3. Dasturchi uchun yuzlab `<div>` lar ichida adashib ketish xavfi yuqori.

**Semantika (Semantics)** — bu teglarning shunchaki ko'rinishiga emas, balki ularning **mazmuni va vazifasiga** qarab ishlatilishidir. HTML5 da brauzer va robotlarga har bir blok nima ekanini ochiq aytuvchi maxsus teglar joriy etildi.

### 2.3. Asosiy HTML5 semantik teglari

1. **`<header>` (Sahifa yoki bo'lim bosh qismi):**
   - Sayt logotipi, asosiy sarlavha (`<h1>`), shior va navigatsiya menyusini o'z ichiga oladi.
   - Har bir `<article>` yoki `<section>` ichida ham o'zining alohida kichik `<header>`i bo'lishi mumkin.

2. **`<nav>` (Navigatsiya havolalari):**
   - Saytning asosiy menyu havolalari to'plami. Barcha havolalar emas, aynan asosiy sahifalarga olib boruvchi menyular `<nav>` ichiga olinadi.

3. **`<main>` (Sahifaning asosiy mazmuni):**
   - Sahifadagi eng muhim va takrorlanmas kontent.
   - Qat'iy qoida: bir HTML hujjatida **faqat 1 ta** `<main>` bo'lishi kerak! U `<header>`, `<footer>` yoki `<aside>` ichida joylashishi mumkin emas.

4. **`<section>` (Mavzuli bo'lim):**
   - Sahifani mantiqiy boblarga yoki bloklarga ajratish uchun ishlatiladi (Masalan: «Biz haqimizda», «Xizmatlarimiz», «Aloqa»).
   - Odatda har bir `<section>` o'zining `<h2>` yoki `<h3>` sarlavhasiga ega bo'lishi tavsiya etiladi.

5. **`<article>` (Mustaqil maqola / post):**
   - O'zicha to'liq mustaqil mazmunga ega bo'lgan, saytning boshqa qismiga yoki boshqa saytga ko'chirilganda ham ma'nosini yo'qotmaydigan blok.
   - Misollar: blog posti, yangilik xabari, mahsulot kartochkasi, foydalanuvchi sharhi.

6. **`<aside>` (Qo'shimcha yon panel / Sidebar):**
   - Asosiy mazmunga bevosita bog'liq bo'lmagan qo'shimcha ma'lumotlar: sayt bo'ylab qidiruv oynasi, o'xshash maqolalar ro'yxati, reklama bannerlari, muallif haqida qisqa ma'lumot.

7. **`<footer>` (Sahifa yoki bo'lim quyi qismi):**
   - Mualliflik huquqi (Copyright ©), ijtimoiy tarmoqlar havolalari, bog'lanish ma'lumotlari, maxfiylik siyosati.

---

## 3. Amaliy topshiriqlar va yechimlari

### 1-topshiriq. «Div soup»ni tozalash (Refactoring)
**Vazifa:** Quyidagi eski HTML4 kodini to'g'ri HTML5 semantik teglari bilan almashtiring:
```html
<div class="top-bar">
  <h1>IT Yangiliklari</h1>
  <div class="menu">
    <a href="#">Bosh sahifa</a> | <a href="#">Aloqa</a>
  </div>
</div>
```
**Yechim:**
```html
<header>
  <h1>IT Yangiliklari</h1>
  <nav>
    <a href="#">Bosh sahifa</a> | <a href="#">Aloqa</a>
  </nav>
</header>
```

### 2-topshiriq. To'liq blog sahifasi skeletini qurish
**Vazifa:** Bitta shaxsiy blog sahifasining semantik strukturasini yarating. Tarkibi:
- Sahifa `header`ida blog nomi va `nav` menyusi.
- `main` ichida 2 ta alohida yangilik `article`i (har birida sarlavha va matn) va 1 ta yon panel `aside`.
- Sahifa so'ngida `footer`.
**Yechim:**
```html
<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <title>Mening IT Blogim</title>
</head>
<body>
  <header>
    <h1>Dasturchi Kundaligi</h1>
    <nav>
      <a href="#bosh">Bosh sahifa</a>
      <a href="#maqolalar">Maqolalar</a>
      <a href="#aloqa">Aloqa</a>
    </nav>
  </header>

  <main>
    <section id="maqolalar">
      <h2>So'nggi postlar</h2>
      
      <article>
        <header>
          <h3>Nega HTML5 semantikasi muhim?</h3>
          <p>Sana: 2026-10-04 | Muallif: Sardor</p>
        </header>
        <p>Semantik teglar veb-saytning Google qidiruvida yuqori o'ringa chiqishiga yordam beradi...</p>
      </article>

      <article>
        <header>
          <h3>CSS Flexbox sirlari</h3>
          <p>Sana: 2026-10-02 | Muallif: Sardor</p>
        </header>
        <p>Flexbox yordamida elementlarni bir tekisda yonma-yon joylashtirish juda oson...</p>
      </article>
    </section>

    <aside>
      <h3>Muallif haqida</h3>
      <p>Sardor — 8-sinf o'quvchisi, Full-stack yo'nalishi qiziquvchisi.</p>
    </aside>
  </main>

  <footer>
    <p>&copy; 2026 Barcha huquqlar himoyalangan.</p>
  </footer>
</body>
</html>
```

---

## 4. Tezkor nazorat savollari (javoblari bilan)

1. **Savol:** Nima uchun sahifada 100 ta `<div>` ishlatish o'rniga semantik teglardan foydalanish kerak?
   **Javob:** Semantik teglar kodni o'qishni osonlashtiradi, qidiruv tizimlariga (SEO) sahifa tuzilishini to'g'ri tushuntiradi va screen readerlar orqali imkoniyati cheklangan foydalanuvchilarga qulaylik yaratadi.
2. **Savol:** `<article>` va `<section>` ning asosiy farqi nimada?
   **Javob:** `<article>` — o'zicha mustaqil mazmunga ega (masalan, alohida maqola yoki sharh). `<section>` esa bitta umumiy mavzuni birlashtiruvchi bo'limdir.
3. **Savol:** Bitta sahifada nechta `<main>` tegi bo'lishi mumkin?
   **Javob:** Faqat 1 ta `<main>` tegi bo'lishi mumkin.
4. **Savol:** `<nav>` tegi ichiga qanday havolalar qo'yiladi?
   **Javob:** Saytning asosiy navigatsiya menyulari (bosh sahifa, xizmatlar, bog'lanish va h.k.).
5. **Savol:** `<aside>` tegi qanday kontent uchun mo'ljallangan?
   **Javob:** Asosiy maqolaga qo'shimcha bo'lgan yon bloklar (sidebar), reklamalar yoki muallif ma'lumoti uchun.
