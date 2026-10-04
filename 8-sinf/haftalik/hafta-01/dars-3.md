# 3-dars. Matn teglari, `<a>` tegi, block va inline elementlar

**Hafta:** 1 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliyot · **I-bob**, 3-dars

## 1. Dars rejasi

**Maqsad:** o'quvchi matnni semantik jihatdan to'g'ri formatlaydi, havola (`<a>`) yaratadi, block va inline elementlar farqini tushunadi.

**Kutiladigan natija:**
- `<strong>`, `<em>`, `<mark>`, `<small>`, `<sub>`, `<sup>`, `<abbr>`, `<code>`, `<q>`, `<cite>`, `<span>` va boshqalarni ishlatadi.
- `<b>`/`<strong>` va `<i>`/`<em>` farqini biladi.
- `<a>` ning `href`, `target`, `rel`, `title`, `download` atributlarini biladi.
- Block va inline elementlarni ajratadi; odatiy xatolardan qochadi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 | Takrorlash | Skelet, `head`, sarlavhalar; uyga vazifa |
| 10–30 | Yangi mavzu 1 | Matn teglari |
| 30–40 | Yangi mavzu 2 | `<a>` va atributlari |
| 40–45 | Tanaffus | |
| 45–55 | Yangi mavzu 3 | Block/inline, odatiy xatolar |
| 55–75 | Amaliyot | Maqola sahifasi |
| 75–80 | Tezkor nazorat va xulosa | |

## 2. Konspekt

### 2.1. Takrorlash (10 daqiqa)
O'quvchilardan doskada (yoki og'zaki) skelet tuzilishini aytishni so'rang. Uyga vazifani ko'ring. Savol: «`<head>` ichida nima bo'ladi?»

### 2.2. Matn teglari
**Mazmunli (semantik) teglar** — matnning ma'nosini bildiradi:

| Teg | Vazifasi | Misol |
|---|---|---|
| `<strong>` | Muhim matn (odatda qalin) | `<strong>Diqqat!</strong>` |
| `<em>` | Ta'kidlangan (odatda qiyshiq) | `Men <em>haqiqatan</em> ham yoqtiraman` |
| `<mark>` | Belgilab ko'rsatilgan (sariq) | `<mark>muhim joy</mark>` |
| `<small>` | Mayda yozuv | `<small>© 2026</small>` |
| `<abbr title="...">` | Qisqartma, kursor bosilganda izoh | `<abbr title="HyperText Markup Language">HTML</abbr>` |
| `<cite>` | Asar nomi / manba | `<cite>O'tkan kunlar</cite>` |
| `<q>` | Qisqa sitata (qo'shtirnoq o'zi chiqadi) | `<q>Bilim — kuch</q>` |
| `<code>` | Dastur kodi | `<code>console.log()</code>` |
| `<kbd>` | Klaviatura tugmasi | `<kbd>Ctrl</kbd> + <kbd>S</kbd>` |
| `<samp>` | Dastur chiqargan natija | `<samp>Xato: 404</samp>` |
| `<var>` | O'zgaruvchi (matematika/dasturda) | `<var>x</var> = 5` |
| `<sub>` / `<sup>` | Pastki / yuqori indeks | `H<sub>2</sub>O`, `x<sup>2</sup>` |
| `<br>` | Qator uzish | `Salom<br>dunyo` |
| `<wbr>` | Uzun so'zni uzish mumkin bo'lgan joy | `uzun<wbr>so'z` |
| `<span>` | Ma'nosiz konteyner (CSS bilan keyin bezaladi) | `<span>matn</span>` |

**Ko'rinish uchun teglar:** `<b>` (qalin), `<i>` (qiyshiq), `<u>` (tagiga chizilgan). Ular faqat ko'rinishni o'zgartiradi, ma'no bermaydi. Qoida: ma'no uchun — `<strong>`, `<em>`; keyinchalik ko'rinishni **CSS** boshqaradi. Shuning uchun imkon qadar `strong`/`em` ishlating.

Eslatma: `<u>` ni havola bilan adashtirishadi (havola ham tagiga chizilgan), shuning uchun kamdan-kam ishlating.

### 2.3. `<a>` — havola
```html
<a href="https://uz.wikipedia.org">Vikipediya</a>
```
Atributlar:
- `href` — manzil (**h**ypertext **ref**erence). Majburiy.
- `target="_blank"` — yangi tabda ochadi.
- `rel="noopener noreferrer"` — `target="_blank"` bilan birga yozish tavsiya etiladi (xavfsizlik).
- `title="..."` — kursor ustida chiqadigan izoh.
- `download` — havola faylni yuklab oladi.

Havola turlari:
```html
<!-- Boshqa sayt (to'liq manzil) -->
<a href="https://google.com">Google</a>
<!-- O'z saytingizdagi boshqa sahifa (nisbiy yo'l) -->
<a href="aloqa.html">Aloqa</a>
<!-- Sahifa ichidagi joyga (id orqali) -->
<a href="#pastki">Pastga</a>
...
<h2 id="pastki">Pastki qism</h2>
<!-- Elektron pochta va telefon -->
<a href="mailto:test@example.com">Yozing</a>
<a href="tel:+998901234567">Qo'ng'iroq</a>
```
(`id` atributi 7–9 darslarda va CSS'da ko'proq o'tiladi; bu yerda faqat «yorliq» sifatida ko'rsating.)

### 2.4. Block va inline elementlar
- **Block** elementlar yangi qatordan boshlanadi va butun kenglikni egallaydi: `<h1>–<h6>`, `<p>`, `<div>`.
- **Inline** elementlar qator ichida, faqat o'z mazmuni kengligicha turadi: `<span>`, `<a>`, `<strong>`, `<em>`, `<code>`.

Qoida: inline element block elementning ichida turadi (`<p>` ichida `<a>`), `<p>` ichiga boshqa `<p>` yoki `<h1>` qo'yib bo'lmaydi.

### 2.5. Odatiy xatolar va to'g'ri yozish qoidalari
1. Yopuvchi tegni unutish.
2. Teglarni noto'g'ri tartibda yopish.
3. Atribut qiymatini qo'shtirnoqsiz yozish.
4. `<p>` ichiga `<p>` yoki `<h1>` qo'yish.
5. Sarlavhani matnni kattalashtirish uchun ishlatish.
6. Fayl nomida bo'sh joy va katta harf (`Mening Sahifam.HTML`) — `index.html`, `aloqa.html` kabi kichik harf va tire ishlating.
7. Kodni surmaslik (indent) — o'qish qiyin.

## 3. Kod namunalari

**Namuna 1 — matn teglari aralash:**
```html
<p>
  Suv formulasi: H<sub>2</sub>O. Kvadrat: x<sup>2</sup>.<br>
  Saqlash uchun <kbd>Ctrl</kbd> + <kbd>S</kbd> bosing.
</p>
<p><abbr title="Domain Name System">DNS</abbr> — domen nomini <mark>IP manzilga</mark> aylantiradi.</p>
<p>Alisher Navoiy: <q>Odami ersang, demagil odami</q>.</p>
```

**Namuna 2 — havolalar:**
```html
<p><a href="https://uz.wikipedia.org" target="_blank" rel="noopener noreferrer" title="Erkin ensiklopediya">Vikipediya</a></p>
<p><a href="mailto:test@example.com">Pochta yozish</a></p>
<p><a href="#oxiri">Sahifa oxiriga</a></p>
```

**Namuna 3 — block va inline farqi (brauzerda sinab ko'ring):**
```html
<p>Birinchi abzats</p>
<p>Ikkinchi abzats</p>
<span>Birinchi span</span>
<span>Ikkinchi span (bir qatorda!)</span>
```

## 4. Amaliy topshiriqlar

### Oson — Matn formatlash
Quyidagini HTML da yozing:
> Muhim: ertaga dars soat 15:00 da. Suv formulasi H2O, kvadrat esa x2. Saqlash: Ctrl + S.

«Muhim» — `<strong>`; «15:00» — `<mark>`; H2O va x2 indekslari; Ctrl va S — `<kbd>`.
**Yechim:**
```html
<p><strong>Muhim:</strong> ertaga dars soat <mark>15:00</mark> da.</p>
<p>Suv formulasi H<sub>2</sub>O, kvadrat esa x<sup>2</sup>.</p>
<p>Saqlash: <kbd>Ctrl</kbd> + <kbd>S</kbd></p>
```

### O'rta — Havolali sahifa
`havolalar.html` yarating: sarlavha, qisqa tanishtiruv `<p>`, kamida 3 ta havola (biri yangi tabda `target="_blank"` va `rel` bilan, biri `title` bilan, biri `mailto:`). Sahifa oxirida `<small>` bilan «© 2026» yozuvi.
**Kutiladigan natija:** havolalar bosilganda ishlaydi; tab to'g'ri ochiladi.
**Yechim:** Namuna 2 asosida.

### Qiyin (kuchli o'quvchi uchun) — Ikki sahifali mini-sayt
`index.html` va `haqida.html` yarating. Har birida to'liq skelet, `<title>`, `<meta description>`. `index.html` dan `haqida.html` ga va aksincha havola bering. `index.html` da sahifa ichidagi havola (`#oxiri`) ham bo'lsin: pastda `id="oxiri"` li `<h2>`; unga yetish uchun yetarlicha matn yozing.
**Kutiladigan natija:** ikkala sahifa o'rtasida o'tish ishlaydi (ikkala fayl bir papkada).
**Yechim:**
```html
<!-- index.html -->
<a href="haqida.html">Men haqimda</a>
<!-- haqida.html -->
<a href="index.html">Bosh sahifa</a>
```

### Yakuniy — Maqola
Sevimli mavzuda (o'yin, hayvon, shahar) kichik maqola: `<h1>`, ikkita `<h2>`, abzatslar; kamida bitta `<strong>`, `<em>`, `<abbr>`, `<q>` va bitta tashqi havola.

## 5. Tezkor nazorat
1. `<strong>` va `<b>` farqi nima? *(Birinchisi ma'noni — muhimlikni bildiradi, ikkinchisi faqat ko'rinish.)*
2. `href` atributi nima uchun? *(Havola manzilini ko'rsatadi.)*
3. Havolani yangi tabda ochish uchun qanday atribut kerak? *(`target="_blank"`, yoniga `rel="noopener noreferrer"`.)*
4. `<p>` block yoki inline? `<span>`-chi? *(Block; inline.)*
5. `H₂O` dagi 2 ni qaysi teg bilan yozamiz? *(`<sub>`)*

## 6. Uyga vazifa
`uyga-vazifa.md` dagi 3-topshiriq.
