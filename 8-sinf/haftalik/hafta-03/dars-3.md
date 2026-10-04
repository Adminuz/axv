# 9-dars. HTML5 global atributlari va zamonaviy forma imkoniyatlari. I bob yakuni

**Hafta:** 3 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliy loyiha · **I-bob**, 9-dars

## 1. Dars rejasi

**Maqsad:** o'quvchilarga barcha HTML elementlari uchun umumiy bo'lgan global atributlarni (`id`, `class`, `title`, `style`, `data-*`, `hidden`, `tabindex`, `contenteditable`), HTML5 ning yangi forma input turlari (`color`, `date`, `range`, `number`) va validatsiya qoidalarini amaliy o'rgatish hamda I bob bo'yicha to'liq semantik, multimediaviy va formali veb-sahifa loyihasini yaratish.

**Kutiladigan natija:**
- Global atributlar tushunchasini va ularning har qanday tegda ishlashini biladi.
- `data-*` (foydalanuvchi ma'lumotlari) atributi orqali HTML elementlariga maxsus ma'lumotlar biriktirishni tushunadi.
- `hidden` (elementni yashirish), `contenteditable` (matnni brauzerda to'g'ridan-to'g'ri tahrirlash) va `tabindex` (klaviaturadan Tab bilan yurish tartibi) atributlarini amalda qo'llay oladi.
- Zamonaviy input turlari (`type="color"`, `type="range"`, `type="date"`) orqali interaktiv boshqaruv elementlarini hosil qiladi.
- I bobda o'rganilgan barcha teglarni (matn, ro'yxat, rasm, jadval, forma, semantika, video/audio) birlashtirib, mukammal yakuniy veb-sahifa loyihasini yarata oladi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash | 8-dars (multimedia, details, progress). Muammo: «Brauzerda sahifadagi matnni Word kabi to'g'ridan-to'g'ri yozib tahrirlab ko'rganmisiz?» |
| 10–30 daq | Yangi mavzu: Global atributlar | `id`, `class`, `title`, `data-*`, `hidden`, `contenteditable`, `tabindex` va yangi inputlar |
| 30–35 daq | Tanaffus | Ko'z va bilak mashqlari |
| 35–65 daq | Amaliy loyiha: I bob yakuni | «Mening interaktiv shaxsiy portfoliom» to'liq HTML5 sahifasi loyihasini yaratish |
| 65–75 daq | Tezkor nazorat va himoya | Mini-loyihalarni o'zaro ko'rib chiqish va 5 ta savol |
| 75–80 daq | Xulosa va II bobga ko'prik | I bob natijalari va keyingi hafta boshlanadigan CSS texnologiyasi anonsi |

---

## 2. Konspekt

### 2.1. Takrorlash (10 daqiqa)
- `<details>` va `<summary>` teglari nima vazifani bajaradi?
- Videoga `controls` va `poster` nima uchun qo'yiladi?

### 2.2. HTML5 Global atributlari nima?

Ba'zi atributlar faqat bitta tegda ishlaydi (masalan, `href` faqat `<a>` da, `src` faqat `<img>` da).
Lekin **Global atributlar** istisnosiz barcha HTML teglari bilan birgalikda ishlatilishi mumkin!

Eng muhim global atributlar:
1. **`id` (Yagona identifikator):**
   - Sahifadagi bitta elementga beriladigan takrorlanmas nom. Bir sahifada bitta `id` faqat 1 marta kelishi shart. CSS stillash va JavaScript orqali elementni topishda ishlatiladi.
2. **`class` (Sinf nomi):**
   - Bir nechta elementni umumiy guruhga birlashtirish uchun ishlatiladi. Bitta elementda bir nechta class bo'lishi mumkin (bo'sh joy bilan ajratiladi: `class="btn btn-primary"`).
3. **`title` (Qalqib chiquvchi eslatma / Tooltip):**
   - Sichqoncha kursori element ustiga olib borilganda kichik yordamchi matn chiqadi.
   ```html
   <abbr title="World Wide Web">WWW</abbr>
   ```
4. **`data-*` (Maxsus ma'lumotlar atributi):**
   - Dasturchiga o'zining shaxsiy ma'lumotlarini HTML ichida saqlash imkonini beradi. Yulduzcha o'rniga istalgan so'z yoziladi:
   ```html
   <article data-id="101" data-category="frontend" data-author="Jasur">...</article>
   ```
5. **`hidden` (Yashirish):**
   - Mantiqiy (boolean) atribut. Agar elementga `hidden` yozilsa, brauzer uni sahifada ko'rsatmaydi (CSS dagi `display: none` ga teng):
   ```html
   <p hidden>Ushbu maxfiy xabar faqat tizimga kirgach ochiladi.</p>
   ```
6. **`contenteditable` (Matnni tahrirlash):**
   - Sehrli atribut! Agar uni `true` qilsangiz, foydalanuvchi oddiy paragraf yoki sarlavhani xuddi Word'dagi kabi brauzerda to'g'ridan-to'g'ri o'chirib, o'zgartirishi mumkin:
   ```html
   <h2 contenteditable="true">Ushbu sarlavhani o'zgartirib ko'ring!</h2>
   ```
7. **`tabindex` (Klaviaturadan o'tish tartibi):**
   - Foydalanuvchi `Tab` tugmasini bosganda kursor qaysi elementga navbat bilan sakrashini belgilaydi:
   ```html
   <input type="text" tabindex="1">
   <input type="text" tabindex="2">
   ```

### 2.3. Yangi HTML5 forma inputlari
HTML5 formalar uchun juda qulay yangi kiritish turlarini taqdim etdi:
- `type="color"`: Rang tanlash palitrasini ochadi.
- `type="range"`: O'ngga-chapga suriladigan slayder (slider) yaratadi (`min="0" max="100"`).
- `type="date"`: Kalendardan sana tanlash oynasini chiqaradi.
- `type="number"`: Faqat raqam kiritiladigan va yuqori-pastga strelkalari bor maydon.

---

## 3. Amaliy topshiriqlar va yechimlari

### 1-topshiriq. Global atributlar amaliyoti
**Vazifa:** Quyidagi talablarga mos elementlar tuzing:
1. `contenteditable="true"` bo'lgan bitta `<h3>` sarlavha;
2. `title="Ushbu tugma bosilganda yangilanadi"` bo'lgan bitta `<button>`;
3. `data-user-id="77"` va `data-status="active"` atributlariga ega bo'lgan bitta `<div class="user-card">`.
**Yechim:**
```html
<h3 contenteditable="true">Mening maqsadlarim ro'yxati (tahrirlash mumkin)</h3>
<button type="button" title="Ushbu tugma bosilganda yangilanadi">Yangilash</button>
<div class="user-card" id="user-77" data-user-id="77" data-status="active">
  <p>Foydalanuvchi: Jasur Karimov</p>
</div>
```

### 2-topshiriq. I bob yakuniy loyihasi: «Interaktiv shaxsiy portfolio»
**Vazifa:** I bobdagi barcha mavzularni o'z ichiga olgan 1 sahifalik to'liq veb-sahifa yarating:
1. `<header>` va `<nav>` menyusi.
2. `<main>` ichida:
   - Shaxsiy fotosurat `<figure>` va `<figcaption>` bilan.
   - Bilim darajasini ko'rsatuvchi `<progress>` indikatori.
   - «Mening ko'nikmalarim» jadvali (`<table>`, `<th>`, `<td>`).
   - Sevimli qo'shiq yoki audioyozuv (`<audio controls>`).
   - Bog'lanish formasi (`<form>`: ism, rang tanlash `type="color"`, sana `type="date"`, xabar `<textarea>`, yuborish tugmasi).
   - O'zingiz haqingizdagi qiziqarli savol-javoblar (`<details>` va `<summary>`).
3. `<footer>` mualliflik huquqi bilan.
**Yechim:**
```html
<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <title>Sardor - Shaxsiy Portfolio</title>
</head>
<body>
  <header>
    <h1>Sardor Alimov</h1>
    <p>8-sinf o'quvchisi · Bo'lajak Web Full-stack dasturchi</p>
    <nav>
      <a href="#haqimda">Haqimda</a> |
      <a href="#loyihalar">Loyihalar</a> |
      <a href="#boglanish">Bog'lanish</a>
    </nav>
  </header>

  <main>
    <section id="haqimda">
      <h2>Men haqimda</h2>
      <figure>
        <img src="profil.jpg" alt="Sardor fotosurati" width="200">
        <figcaption>Sardor Alimov — dasturlash to'garagi a'zosi</figcaption>
      </figure>
      <p>HTML5 o'zlashtirish darajam:</p>
      <progress value="90" max="100"></progress> 90%
    </section>

    <section id="loyihalar">
      <h2>O'rganilgan texnologiyalar</h2>
      <table border="1">
        <thead>
          <tr>
            <th>Texnologiya</th>
            <th>Daraja</th>
            <th>Holat</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>HTML Asoslari</td>
            <td>A'lo</td>
            <td>O'zlashtirildi</td>
          </tr>
          <tr>
            <td>HTML5 Semantika</td>
            <td>A'lo</td>
            <td>O'zlashtirildi</td>
          </tr>
        </tbody>
      </table>

      <h3>Sevimli tanaffus musiqam</h3>
      <audio controls>
        <source src="musiqa.mp3" type="audio/mpeg">
      </audio>

      <details>
        <summary>Nega men dasturlashni tanladim?</summary>
        <p>Kelajakda xalqaro IT kompaniyalarida ishlash va foydali ilovalar yaratish uchun.</p>
      </details>
    </section>

    <section id="boglanish">
      <h2>Men bilan bog'lanish</h2>
      <form action="#" method="POST">
        <label for="ism">Ismingiz:</label>
        <input type="text" id="ism" name="ism" required placeholder="Ismingizni yozing"><br><br>

        <label for="rang">Sevimli rangingiz:</label>
        <input type="color" id="rang" name="rang"><br><br>

        <label for="sana">Uchrashuv kuni:</label>
        <input type="date" id="sana" name="sana"><br><br>

        <label for="xabar">Xabaringiz:</label><br>
        <textarea id="xabar" name="xabar" rows="4" cols="30" placeholder="Xabaringizni yozing..."></textarea><br><br>

        <button type="submit">Yuborish</button>
      </form>
    </section>
  </main>

  <footer>
    <p>&copy; 2026 Sardor Alimov. Barcha huquqlar himoyalangan.</p>
  </footer>
</body>
</html>
```

---

## 4. Tezkor nazorat savollari (javoblari bilan)

1. **Savol:** Maxsus (spesifik) atributlar bilan global atributlarning farqi nimada?
   **Javob:** Maxsus atributlar faqat ma'lum bir tegda ishlaydi (masalan, `href` faqat `<a>` da). Global atributlar esa har qanday HTML elementiga qo'llanilishi mumkin.
2. **Savol:** `data-*` atributi dasturchiga qanday qulaylik beradi?
   **Javob:** Standart teglarga o'zimizning maxsus yashirin ma'lumotlarimizni (masalan, foydalanuvchi IDsi, mahsulot narxi, toifa) xavfsiz saqlash va keyinchalik JavaScript orqali o'qish imkonini beradi.
3. **Savol:** Elementni sahifadan butunlay yashirib qo'yish uchun qaysi global atribut ishlatiladi?
   **Javob:** `hidden` atributi ishlatiladi.
4. **Savol:** Brauzerda matnni Word kabi to'g'ridan-to'g'ri tahrirlash imkonini beruvchi atribut qaysi?
   **Javob:** `contenteditable="true"` atributi.
5. **Savol:** I bobda (HTML tili) qanday asosiy bo'limlarni o'rganib chiqdik?
   **Javob:** Internet va veb arxitekturasi, HTML hujjat tuzilishi, matnlar, ro'yxatlar, jadvallar, formalar, HTML5 semantikasi, multimedia va global atributlar.
