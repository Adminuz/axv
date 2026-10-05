# 10-dars. CSS asoslari: ulash va selektorlar

> HTML sahifangiz hozircha oq-qora ko'ylakda. Bugun unga CSS bilan rang, uslub va xarakter beramiz va kerakli elementni aniq tanlashni o'rganamiz.

## Dars xulosasi

- **CSS** (Cascading Style Sheets) sahifaning tashqi ko'rinishini belgilaydi, HTML esa mazmun va tuzilmani beradi.
- CSS qoidasi: `selektor { xususiyat: qiymat; }`. Har bir e'lon `;` bilan tugaydi.
- CSS ulashning 3 usuli: **inline** (`style` atributi), **internal** (`<style>` tegi), **external** (`<link>` bilan `.css` fayl).
- Selektorlar: element (`p`), class (`.karta`), id (`#logo`), universal (`*`), guruh (`h1, h2`), descendant (`nav a`).
- Class ko'p elementda takrorlanadi, id sahifada faqat bitta bo'ladi.
- Ustuvorlik: element < class < id < inline. Kuch teng bo'lsa, oxirgi yozilgan yutadi.

## Qo'shimcha ma'lumot

### 1. Nega aynan external CSS?
Tasavvur qiling, saytingizda 50 ta sahifa bor va siz sarlavha rangini o'zgartirmoqchisiz. Inline usulda 50 ta faylni ochib chiqasiz. External usulda esa `style.css` ichidagi bitta qatorni o'zgartirasiz va butun sayt yangilanadi. Shuning uchun real loyihalarda asosan external usul ishlatiladi.

### 2. Class vs id: o'xshatish
Class sinfdagi «a'lochilar guruhi» kabi: unga ko'pchilik kirishi mumkin. Id esa pasportdagi noyob raqam: u faqat bitta odamga tegishli. Shu sababli bir sahifada ikkita bir xil id yozish xato hisoblanadi.
```html
<div class="karta katta">Bir elementda ikkita class</div>
<h1 id="logo">Sahifada bitta</h1>
```

### 3. Descendant selektor «ichidagi» degani
`nav a` — bo'sh joy «ichidagi» ma'nosini beradi. Bu `nav` ichidagi barcha havolalarni tanlaydi, `nav` tashqaridagi havolalar esa tegmaydi.
```css
nav a {
  text-decoration: none;
}
```

### 4. Ustuvorlik hisobi
Eslab qolish uchun soddalashtirilgan ballar: element 1, class 10, id 100, inline 1000.
```css
p { color: red; }          /* 1 */
.xabar { color: green; }   /* 10 */
#asosiy { color: blue; }   /* 100 */
```
`<p id="asosiy" class="xabar">` ning rangi ko'k bo'ladi. «Oxirgi yozilgan yutadi» qoidasi faqat ballar teng bo'lganda ishlaydi.

### 5. Odatiy xatolar
- `karta { }` deb yozish: nuqta unutilgan, brauzer `<karta>` tegini qidiradi.
- `color: red` dan keyin `;` yo'q: keyingi e'lon ishlamay qoladi.
- `<link>` da `href` yo'li noto'g'ri yoki `rel="stylesheet"` yo'q: stil umuman chiqmaydi.
- Stil ishlamasa: F12 oynasini oching va qoida ustiga chizilganmi yoki yo'qmi qarang.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| CSS | Cascading Style Sheets: sahifa ko'rinishini belgilovchi stil tili |
| Selektor | CSS qaysi elementga tegishli ekanini tanlovchi qism |
| Property (xususiyat) | Nimani o'zgartirish kerak, masalan `color` |
| Value (qiymat) | Xususiyatga beriladigan qiymat, masalan `blue` |
| Inline CSS | Teg ichidagi `style` atributi |
| Internal CSS | `<head>` ichidagi `<style>` tegi |
| External CSS | Alohida `.css` fayl, `<link>` bilan ulanadi |
| Class selektor | Nuqta bilan yoziladi: `.karta` |
| Id selektor | Panjara bilan yoziladi: `#logo` |
| Specificity | Qoidaning kuchi (ustuvorlik) |

## Bilasizmi?

- CSS ni 1994-yilda norveg olimi Hokon Vium Li (Håkon Wium Lie) taklif qilgan.
- Hozirgi kunda deyarli har bir sayt CSS ishlatadi: usiz internet 1990-yillardagi oddiy matn sahifalariga o'xshab qolardi.
- «Cascading» so'zi «sharshara» ma'nosini beradi: qoidalar yuqoridan pastga «oqib tushadi», kuchlisi yutadi.
- CSS Zen Garden degan mashhur loyihada bitta HTML ga yuzlab turli CSS berilgan va har safar sayt butunlay boshqacha ko'rinadi.

## Topshiriqlar

### 1. Birinchi style.css · oson
`index.html` va `style.css` fayllarini yarating. `<head>` ichida `<link rel="stylesheet" href="style.css">` yozing. `h1` matnini ko'k rangga bo'yang.
**Kutiladigan natija:** sarlavha ko'k rangda ko'rinadi.

### 2. Uchta usul · oson
Bitta `<h1>` ni avval inline, keyin internal, keyin external usulda qizilga bo'yang. Har safar boshqa usulni sinab ko'ring.
**Kutiladigan natija:** uchala usulda ham bir xil natija, lekin kod joylashuvi har xil.

### 3. Bo'sh joy kerakmi? · oson
Quyidagi qoidani to'g'rilang, `h1` ham qizil va markazda bo'lishi kerak:
```css
h1 {
  color: red
  text-align: center;
}
```
**Kutiladigan natija:** yetishmayotgan belgi topilgan va ikkala e'lon ishlaydi.

### 4. Nuqta yoki panjara · oson
Sahifada `<div class="karta">` va `<h1 id="logo">` bor. Ikkala elementga alohida qoida yozing.
**Kutiladigan natija:** `.karta` ga fon, `#logo` ga katta shrift berilgan.

### 5. Qaysi elementlar tanlandi? · o'rta
Quyidagi kodda `nav a` qoidasi qaysi havolalarga ta'sir qiladi? Oldindan taxmin qiling, keyin brauzerda tekshiring.
```html
<nav><a href="#">1</a><a href="#">2</a></nav>
<a href="#">3</a>
```
```css
nav a { color: green; }
```
**Kutiladigan natija:** faqat 1 va 2 yashil, 3 o'zgarmaydi.

### 6. Guruh selektor · o'rta
Uchta qoidani bitta guruh selektorga birlashtiring:
```css
h1 { color: navy; }
h2 { color: navy; }
h3 { color: navy; }
```
**Kutiladigan natija:** bitta qisqa qoida, natija o'zgarmaydi.

### 7. Bu kod nima chiqaradi? · o'rta
Matn qaysi rangda ko'rinadi?
```css
p { color: red; }
.xabar { color: green; }
```
```html
<p class="xabar">Salom</p>
```
**Kutiladigan natija:** yashil rangni tushuntiring: class element dan kuchli.

### 8. Ikki class · o'rta
Bitta `<div>` ga ikkita class bering: `karta` va `katta`. `.karta` ga fon, `.katta` ga katta shrift yozing.
**Kutiladigan natija:** div ikkala stilni ham oladi.

### 9. Ustuvorlik jangi · qiyin
Bitta `<p>` ga element, class va id selektori orqali uchta turli rang bering. Natijani oldindan taxmin qiling. Keyin qoidalar tartibini almashtirib, yana tekshiring.
**Kutiladigan natija:** qaysi rang yutganini va tartib nega ahamiyatsiz bo'lganini tushuntirib bera olasiz.

### 10. Xatoni toping · qiyin
`style.css` yozildi, lekin sahifada o'zgarish yo'q. Kamida 4 ta mumkin bo'lgan sababni ro'yxat qilib yozing va har birini tekshirib ko'ring.
**Kutiladigan natija:** sabablar: fayl nomi/yo'li, `rel="stylesheet"`, figurali qavs, boshqa kuchliroq qoida.

### 11. Mening sinfim sahifasi · qiyin
Kamida 5 ta turli selektordan (element, class, id, guruh, descendant) foydalanib, «Mening sinfim» sahifasini bezang.
**Kutiladigan natija:** hammasi bitta `style.css` da, sahifa toza va tartibli.

### 12. Tadqiqot: universal selektor · bonus
`* { border: 1px solid red; }` qoidasini sahifangizga yozing. Nima bo'ldi? Bu usul nima uchun xato topishda qo'l keladi?
**Kutiladigan natija:** barcha elementlar atrofida chiziq paydo bo'ladi, tuzilma ko'rinadi.

## O'zingizni tekshiring

1. CSS qoidasi qanday qismlardan iborat?
2. CSS ulashning uch usulini va ularning farqini ayting.
3. External CSS qaysi teg bilan va qaysi atributlar bilan ulanadi?
4. Class va id selektorlari qanday yoziladi, farqi nimada?
5. `h1, h2` va `nav a` selektorlari nimani anglatadi?
6. `p`, `.xabar`, `#asosiy` to'qnashsa, qaysi biri yutadi va nega?
7. Kuch teng bo'lsa, qaysi qoida yutadi?

## Uyga vazifa

«Mening sinfim» sahifasiga `style.css` ulang. Unda kamida 4 xil selektor ishlating: element, class, id va guruh yoki descendant. 20–30 daqiqa.
