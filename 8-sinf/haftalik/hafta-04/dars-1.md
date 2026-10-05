# 10-dars. CSS asoslari: ulash va selektorlar

**Hafta:** 4 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliyot · **II-bob**, 10-dars

## 1. Dars rejasi

**Maqsad:** o'quvchilar CSS nima ekanini va veb-sahifadagi rolini tushunadi, CSS ni HTML ga ulashning uch usulini (style atributi, `<style>` tegi, `<link>` tegi) o'rganadi, elementlarni tanlashning asosiy selektorlarini (element, class, id, universal, guruh, descendant) amalda qo'llaydi va ikki qoida to'qnashganda qaysi biri yutishini (CSS priority, specificity) tushunadi.

**Kutiladigan natija:**
- CSS qoidasining tuzilishini (`selektor { xususiyat: qiymat; }`) tushuntira oladi.
- `inline`, `internal`, `external` CSS farqini biladi va `style.css` faylini `<link>` bilan ulay oladi.
- 6 xil selektorni yoza oladi va ularning farqini aytadi.
- Class va id ning farqini biladi.
- Ustuvorlik tartibini (element < class < id < inline) hisoblab, natijani oldindan taxmin qila oladi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–8 daq | Takrorlash | O'tgan hafta: HTML5 semantik teglar. Savol: «Nega sahifa oq-qora va zerikarli?» |
| 8–35 daq | Yangi mavzu | CSS nima, ulash usullari, selektorlar, ustuvorlik |
| 35–40 daq | Tanaffus | Ko'z va qo'l mashqlari |
| 40–70 daq | Amaliyot | `index.html` + `style.css`: 3 darajali topshiriq |
| 70–76 daq | Tezkor nazorat | 5 ta savol |
| 76–80 daq | Xulosa | Uyga vazifa, keyingi dars: rang va shrift |

---

## 2. Konspekt

### 2.1. Takrorlash (8 daqiqa)
- `<header>`, `<main>`, `<footer>` ning vazifasini ayting.
- Nega `<main>` sahifada faqat bitta bo'ladi?
- Muammo: shu semantik sahifani brauzerda ochsak, u qanday ko'rinadi? (Oq fon, qora matn: dizayn yo'q.)

### 2.2. CSS nima?
**CSS (Cascading Style Sheets)** — veb-sahifaning tashqi ko'rinishini (rang, shrift, joylashuv) belgilaydigan stil tili. HTML mazmun va tuzilmani beradi («nima?»), CSS esa ko'rinishni («qanday?»).

O'xshatish: HTML — uyning devori va tomi, CSS — bo'yoq, parda va mebel. Bir skeletga turli CSS berib, butunlay boshqa sayt hosil qilish mumkin.

CSS qoidasining tuzilishi:
```css
h1 {
  color: blue;
  text-align: center;
}
```
- `h1` — **selektor** (qaysi elementni tanlaymiz);
- `color` — **xususiyat (property)**;
- `blue` — **qiymat (value)**;
- har bir e'lon `;` bilan tugaydi, qoidalar `{ }` ichida yoziladi.

### 2.3. HTML ga CSS ulash usullari (CSS turlari)
1. **Inline** — `style` atributi, faqat shu elementga ta'sir qiladi:
```html
<h1 style="color: red;">Salom</h1>
```
2. **Internal** — `<head>` ichidagi `<style>` tegi, butun sahifaga ta'sir qiladi:
```html
<head>
  <style>
    h1 { color: red; }
  </style>
</head>
```
3. **External** — alohida `.css` fayl, `<link>` tegi bilan ulanadi (ko'p sahifaga bitta fayl, asosiy usul):
```html
<head>
  <link rel="stylesheet" href="style.css">
</head>
```
`style.css` ichida `<style>` tegi yozilmaydi, faqat qoidalar bo'ladi.

### 2.4. Elementlarni tanlash: selektorlar
| Turi | Yozilishi | Nimani tanlaydi |
|---|---|---|
| Element | `p` | barcha `<p>` teglari |
| Class | `.karta` | `class="karta"` bor elementlar |
| Id | `#logo` | `id="logo"` bor yagona element |
| Universal | `*` | sahifadagi hamma element |
| Guruh | `h1, h2` | vergul bilan sanalgan selektorlar |
| Descendant | `nav a` | `nav` ichidagi barcha `a` |

```css
p { color: gray; }
.karta { background-color: lightyellow; }
#logo { font-size: 32px; }
h1, h2, h3 { color: navy; }
nav a { text-decoration: none; }
* { margin: 0; }
```
```html
<p>Oddiy matn</p>
<div class="karta">...</div>
<h1 id="logo">AXV</h1>
```
Class bir nechta elementda takrorlanadi va bitta elementda bir nechta class bo'lishi mumkin (`class="karta katta"`). Id sahifada faqat bir marta ishlatiladi.

### 2.5. CSS priority (ustuvorlik, specificity)
Bitta elementga bir nechta qoida to'g'ri kelsa, kuchlisi yutadi. O'rganish uchun soddalashtirilgan ballar: element — 1, class — 10, id — 100, inline — 1000. Kuch teng bo'lsa, **oxirgi yozilgan** qoida yutadi.
```css
p { color: red; }
.xabar { color: green; }
#asosiy { color: blue; }
```
```html
<p id="asosiy" class="xabar">Salom!</p>
```
Natija: matn **ko'k** (id = 100 > class = 10 > element = 1).

### 2.6. Odatiy xatolar
- Class oldiga nuqta qo'yishni unutish: `karta {}` — bu `<karta>` tegini qidiradi.
- `;` yoki `}` ni tushirib qoldirish.
- `<link>` da `rel="stylesheet"` yoki fayl yo'li noto'g'ri.
- «Oxirgi yozilgan yutadi» deb o'ylash: bu faqat kuch teng bo'lganda.

---

## 3. Amaliy topshiriqlar va yechimlari

### 1-topshiriq (oson). Birinchi `style.css`
**Vazifa:** `index.html` va `style.css` yarating, `<link>` bilan ulang, `h1` rangini o'zgartiring.
**Kutiladigan natija:** sarlavha ko'k rangda va markazda.
**Yechim:**
```html
<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <title>Mening sinfim</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Mening sinfim</h1>
  <p>8-sinf o'quvchilari</p>
</body>
</html>
```
```css
h1 {
  color: blue;
  text-align: center;
}
```

### 2-topshiriq (o'rta). Selektorlar to'plami
**Vazifa:** sahifada 3 ta `.karta`, `#logo`, `h2` va `h3`, `nav` ichida havolalar bo'lsin. CSS: `.karta` ga fon, `#logo` ga katta shrift, `h2, h3` ga bir xil rang, `nav a` dan tagchiziqni olib tashlang.
**Kutiladigan natija:** har bir selektor aynan o'z elementiga ta'sir qiladi.
**Yechim:**
```css
.karta { background-color: lightyellow; }
#logo { font-size: 32px; }
h2, h3 { color: navy; }
nav a { text-decoration: none; }
```
```html
<h1 id="logo">AXV</h1>
<nav><a href="#">Bosh sahifa</a> <a href="#">Aloqa</a></nav>
<div class="karta"><h2>Birinchi</h2></div>
<div class="karta"><h3>Ikkinchi</h3></div>
<div class="karta">Uchinchi</div>
```

### 3-topshiriq (qiyin). Ustuvorlik jangi
**Vazifa:** bitta `<p>` elementga element, class va id selektori orqali 3 ta turli rang bering. Avval natijani taxmin qiling, keyin tekshiring. Keyin qoidalar tartibini almashtiring.
**Kutiladigan natija:** tartib o'zgarsa ham id yutadi.
**Yechim:**
```css
#asosiy { color: blue; }
.xabar { color: green; }
p { color: red; }
```
```html
<p id="asosiy" class="xabar">Salom!</p>
```
Matn ko'k. Tartib almashganda ham ko'k: kuchli selektor tartibga qaramay yutadi.

---

## 4. Tezkor nazorat savollari (javoblari bilan)
1. **Savol:** CSS ning to'liq nomi va vazifasi?
   **Javob:** Cascading Style Sheets; sahifaning tashqi ko'rinishini belgilaydi.
2. **Savol:** CSS ulashning uch usulini ayting.
   **Javob:** inline (`style` atributi), internal (`<style>` tegi), external (`<link>` bilan `.css` fayl).
3. **Savol:** Class va id selektorlari qanday belgi bilan boshlanadi?
   **Javob:** class — nuqta (`.karta`), id — panjara (`#logo`).
4. **Savol:** `nav a` nimani tanlaydi?
   **Javob:** `nav` ichidagi barcha `a` teglarini (descendant selektor).
5. **Savol:** `p`, `.xabar`, `#asosiy` to'qnashsa, qaysi biri yutadi?
   **Javob:** `#asosiy` (id), chunki id 100 > class 10 > element 1.
