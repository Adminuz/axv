# 13-dars. Semantik HTML5 teglari va accessibility (WCAG) asoslari

> Ekranda ikki sayt bir xil ko'rinishi mumkin, lekin ko'r foydalanuvchi uchun biri tushunarli, boshqasi esa «sho'rva». Bugun HTML ga ma'no berishni o'rganamiz.

## Dars xulosasi

- Semantik HTML kontent ma'nosini va rolini aniq ifodalovchi teglardan foydalanishdir.
- Semantik teglar: `h1`, `p`, `ul`, `table`, `figure`, `header`, `main`, `aside`, `nav`, `footer`; non-semantik: `div`, `span`, `br`.
- Foydalari: accessibility, usability, maintainability, SEO.
- Landmarklar: `header`, `nav`, `main` (bitta), `aside`, `footer`; sahifada bitta `h1`, iyerarxiya sakramaydi.
- ARIA: avval semantik HTML; `nav`, `main` kabilarga ortiqcha `role` kerak emas.
- WCAG: POUR; rasmga `alt`, matn kontrasti 4.5:1 (oddiy matn).

## Qo'shimcha ma'lumot

### Yo'l belgisiz haydash
Qo'llanmaga ko'ra, semantik elementlarsiz saytdan foydalanish yo'l belgilarisiz haydashga o'xshaydi: yetib borasiz, lekin sekin va chalkash.

### a va button farqi
Boshqa sahifaga olib boruvchi element uchun `a`, amal bajaruvchi (yuborish, ochish) element uchun `button`. Aralashtirish foydalanuvchini chalg'itadi.

### Kontrast
Matn va fon orasidagi kontrast WCAG da oddiy matn uchun 4.5:1 tavsiya etiladi (katta matn uchun 3:1). Oq fonda och kulrang matn ko'pincha yetmaydi.

### Odatiy xatolar
`div` dan hamma narsa yasash; `alt` yozmaslik; `h1` ni bir necha marta ishlatish; ARIA ni ortiqcha qo'shish.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Semantik HTML | Ma'noli teglardan foydalanish |
| Non-semantik | Ma'no bildirmaydigan teg (`div`, `span`) |
| Landmark | Sahifaning asosiy zonasi |
| Accessibility | Hamma uchun qulaylik |
| ARIA | Rol va holat atributlari |
| WCAG | Veb kontent qulayligi bo'yicha ko'rsatmalar |
| POUR | WCAG ning 4 tamoyili |
| alt | Rasm uchun matnli o'rnini bosuvchi tavsif |
| Kontrast | Matn va fon rangi orasidagi farq |

## Bilasizmi?

- Zamonaviy HTML da taxminan 30–40 semantik element bor.
- Ekran o'qiydigan qurilma foydalanuvchiga sarlavhalar ro'yxatini ko'rsata oladi: shuning uchun `h1`–`h6` tartibi muhim.
- Google Search Central ham ma'noli sarlavhalar va iyerarxik tuzilmani tavsiya qiladi.

## Topshiriqlar

### 1. Semantik yoki yo'q · oson

`div`, `nav`, `span`, `footer`, `main`, `br` ni semantik va non-semantik guruhlarga ajrating.

**Kutiladigan natija:** Semantik: nav, footer, main; non-semantik: div, span, br.

### 2. 4 ta foyda · oson

Semantik HTML ning 4 foydasini yozing.

**Kutiladigan natija:** Accessibility, usability, maintainability, SEO.

### 3. Landmark vazifalari · oson

`header`, `nav`, `main`, `aside`, `footer` vazifasini 1 jumlada yozing.

**Kutiladigan natija:** 5 ta to'g'ri jumla.

### 4. POUR · oson

POUR ning har harfi nimani bildiradi?

**Kutiladigan natija:** Perceivable, Operable, Understandable, Robust.

### 5. div ni almashtiring · o'rta

`<div id="nav"> <a>..</a> | <a>..</a> </div>` ni semantik menyuga o'tkazing.

**Kutiladigan natija:** `nav > ul > li > a`.

### 6. Sarlavhalar · o'rta

Sahifada `h1`, `h3`, `h2`, `h4` tartibi bor. Qanday tuzatasiz?

**Kutiladigan natija:** `h1`, `h2`, `h3`, `h4`.

### 7. alt matn · o'rta

Maktab binosi rasmi va bezak chizig'i uchun `alt` yozing.

**Kutiladigan natija:** Mazmunli `alt` va `alt=""`.

### 8. Bu kod nima uchun xato? · o'rta

`<button onclick="location='/qabul'">Qabul</button>` ni qanday yaxshilaysiz?

**Kutiladigan natija:** `<a href="/qabul">Qabul</a>`: sahifaga o'tish uchun `a`.

### 9. Bosh sahifa · qiyin

Maktab sayti uchun semantik `index.html` ni yozing (header, nav, main, 3 article, footer).

**Kutiladigan natija:** Bitta `h1`, to'g'ri landmarklar.

### 10. Lighthouse · qiyin

Sahifada Lighthouse Accessibility tekshiruvini bajaring va 2 ta tuzatish qiling.

**Kutiladigan natija:** Ball oshgan hisobot.

### 11. Xatoni toping · qiyin

`<main>` sahifada ikki marta ishlatilgan va `<nav role="navigation">` yozilgan. Nimalar xato?

**Kutiladigan natija:** Bitta `main` va ortiqcha `role`.

### 12. Tab komponent · bonus

`div` dan tab interfeysi yozing va `role="tablist"`, `role="tab"`, `aria-selected` qo'shing.

**Kutiladigan natija:** 3 atributli tab bloki.

## O'zingizni tekshiring

1. Semantik va non-semantik teg farqi?
2. Semantikaning 4 foydasi?
3. `main` nechta bo'ladi?
4. Sarlavhalar iyerarxiyasi qoidasi?
5. ARIA qachon ishlatiladi?
6. POUR nima?
7. `alt` nima uchun kerak?

## Uyga vazifa

Maktab sayti semantik sahifasini yozing va Lighthouse ni ishga tushiring (25 daqiqa). To'liq shart: `uyga-vazifa.md`.
