---
title: "9-dars. HTML5 global atributlari va zamonaviy forma imkoniyatlari. I bob yakuni"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "8-sinf", "link": "/8-sinf/"}, "week": {"n": 3, "link": "/8-sinf/hafta-03/"}, "g": 9, "title": "HTML5 global atributlari va zamonaviy forma imkoniyatlari. I bob yakuni", "lead": "Barcha teglar uchun universal global atributlar, data-* sirlari, yangi kiritish vositalari hamda I bob bo'yicha to'liq mustaqil veb-loyiha.", "slide": "/slaydlar/8-sinf/hafta-03/dars-3.html", "test": "/slaydlar/8-sinf/hafta-03/dars-3-test.html", "tabs": [{"g": 7, "link": "/8-sinf/hafta-03/dars-1", "current": false}, {"g": 8, "link": "/8-sinf/hafta-03/dars-2", "current": false}, {"g": 9, "link": "/8-sinf/hafta-03/dars-3", "current": true}], "prev": {"g": 8, "title": "HTML5 multimedia va interaktiv elementlar: <video>, <audio>, <figure>, <details>, <progress>", "link": "/8-sinf/hafta-03/dars-2"}, "next": null}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Global atributlar:** Istalgan HTML elementiga biriktirilishi mumkin bo'lgan universal parametrlar to'plami.
- **`id` va `class`:** `id` sahifada faqat bitta elementga beriladigan takrorlanmas nom bo'lsa, `class` bir nechta elementlarni bitta uslubiy guruhga birlashtirish vositasidir.
- **`data-*` xususiyati:** Dasturchiga element ichida o'zining maxsus shaxsiy ma'lumotlarini (masalan, narx, mahsulot kodi, status) saqlashga imkon beradi.
- **`contenteditable` va `hidden`:** `contenteditable="true"` oddiy matnni brauzerda to'g'ridan-to'g'ri tahrirlanadigan qiladi; `hidden` esa elementni sahifadan vaqtincha yashirib turadi.
- **Yangi forma boshqaruvlari:** `type="color"` (ranglar palitrasi), `type="range"` (slayder), `type="date"` (kalendar) orqali boyitilgan interfeys.
- **I bob yakuni:** HTML tili va veb-sahifa tuzishning barcha tamoyillari (teglardan tortib semantikagacha) to'liq o'zlashtirildi.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. `data-*` atributi nima uchun zamonaviy dasturlashda juda muhim?

HTML faqat ma'lumotni ko'rsatish uchun emas, balki uni JavaScript orqali boshqarish uchun ham xizmat qiladi.
Tasavvur qiling, internet-do'konda 50 ta telefon kartochkasi bor. Har bir telefonning narxi, ishlab chiqarilgan yili va qoldiq sonini qayerda saqlash mumkin?
HTML5 bunga eng toza yechim berdi — `data-*`:
```html
<div class="product" data-name="iPhone 15" data-price="950" data-stock="12">
  <h3>iPhone 15</h3>
  <p>Narxi: $950</p>
</div>
```
JavaScript orqali ushbu ma'lumotlarni bir qator kod bilan o'qib olish (`element.dataset.price`) va savatchaga qo'shish juda oson.

### 2. `tabindex` orqali klaviatura navigatsiyasini boshqarish

Kompyuterda sichqonchadan foydalanmaydigan dasturchilar yoki imkoniyati cheklangan foydalanuvchilar sahifada harakatlanish uchun `Tab` tugmasini bosishadi:
- `tabindex="0"`: Elementni klaviatura orqali diqqat markaziga (focus) tushadigan qiladi.
- `tabindex="-1"`: Elementni Tab ro'yxatidan chiqarib tashlaydi (unga Tab bilan borib bo'lmaydi).
- `tabindex="1"`, `tabindex="2"`: Tugma bosilganda o'tishning qat'iy tartibini belgilaydi.

### 3. Matnni joyida tahrirlash: `contenteditable` mo'jizasi

Agar siz saytda o'quvchiga matn kiritish yoki tahrirlash imkonini bermoqchi bo'lsangiz, albatta `<textarea>` ochishingiz shart emas.
Oddiygina:
```html
<div contenteditable="true" style="border: 1px dashed gray; padding: 10px;">
  Bu yerga xohlagan matningizni yozing yoki o'chiring!
</div>
```
deb yozsangiz, butun boshli blok matn muharririga aylanadi. Google Docs yoki Notion kabi mashhur dasturlarning asosida aynan shu mexanizm yotadi!

### 4. I bobning katta xulosasi va II bobga ko'prik

Siz 3 hafta davomida Web Full-stack dasturlashning eng asosiy poydevorini qurdingiz:
1. Internet qanday ishlashi va DNS mohiyati;
2. HTML teglar: sarlavhalar, paragraflar, formatlash;
3. Rasmlar, multimedia (`<video>`, `<audio>`), jadvallar va interaktiv formalar;
4. HTML5 semantikasi: toza, xatosiz, SEO talablariga javob beradigan sahifa arxitekturasi.

Endi sahifalarimiz skeletga ega. Keyingi 4-haftadan boshlab biz **II bob — CSS texnologiyasi va sahifa dizayni**ga o'tamiz. Biz bu quruq skeletga ranglar, shriftlar, fonlar, soylar, animatsiyalar va zamonaviy go'zallik berishni o'rganamiz!

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Global atribut** | Barcha HTML elementlari bilan birgalikda ishlatilishi mumkin bo'lgan universal atribut |
| **`id`** | Sahifada faqat bitta elementga tegishli bo'lgan yagona identifikator |
| **`class`** | Bir nechta elementlarni umumiy guruhga birlashtiruvchi sinf nomi |
| **`title`** | Sichqoncha ustiga borganda chiqadigan kichik yordamchi eslatma (tooltip) |
| **`data-*`** | Dasturchi o'zining shaxsiy yashirin ma'lumotlarini elementga biriktirishi uchun atribut |
| **`hidden`** | Elementni sahifadan butunlay yashirib qo'yuvchi mantiqiy atribut |
| **`contenteditable`** | Foydalanuvchiga matnni brauzerda to'g'ridan-to'g'ri tahrirlash imkonini beruvchi xususiyat |
| **`tabindex`** | Klaviaturadagi `Tab` tugmasi bosilganda elementlarning fokus olish ketma-ketligi |
| **`type="color"`** | HTML5 forma ichida ranglar palitrasini ochuvchi kiritish turi |
| **`type="range"`** | Boshlang'ich va yakuniy qiymatlar orasida suriluvchi qulay slayder boshqaruvi |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

1. **`data-*` ning cheksizligi:** Bitta element ichida xohlagancha `data-*` atributi ochishingiz mumkin: masalan, `data-x="10" data-y="20" data-speed="100"`.
2. **Tab tugmasining qulayligi:** Tajribali dasturchilar veb-saytni test qilayotganda sichqonchaga tegmasdan, faqat `Tab` va `Enter` orqali to'liq formani to'ldirib yuborishadi.
3. **Brauzer xotirasi:** `contenteditable` orqali yozilgan matn sahifa qayta yuklanganda o'chib ketadi; uni saqlab qolish uchun kelajakda o'rganiladigan JavaScript va `localStorage` kerak bo'ladi.
4. **W3C qoidalari:** `id` nomi raqam bilan boshlanishi mumkin emas (masalan, `id="1blok"` xato, `id="blok-1"` to'g'ri).

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. `title` va `id` atributlari amaliyoti <Badge type="tip" text="oson" />
Shaxsiy fotosuratingiz yoki sevimli avtomobilingiz rasmini joylang. Unga `id="asosiy-rasm"` va `title="Ushbu rasm 2026-yilda olingan"` atributlarini bering. Sichqonchani rasm ustiga olib borib, eslatma chiqqanini tekshiring.
**Kutiladigan natija:** Kursorni ustiga borganda yordamchi matn chiqaruvchi element.

### 2. `contenteditable` bilan tahrirlanuvchi blok yasash <Badge type="tip" text="oson" />
Sahifada bitta `<h2>` sarlavha va bitta `<p>` paragraf yarating. Ularning ikkalasiga ham `contenteditable="true"` atributini bering. Brauzerda ochib, matnni o'chirib, o'z ismingizni yozib sinang.
**Kutiladigan natija:** Foydalanuvchi tomonidan bevosita ekranda tahrirlanuvchi matn bloki.

### 3. `hidden` atributi orqali sirli xabar <Badge type="tip" text="oson" />
Ikkita paragraf yozing: biri oddiy, ikkinchisi esa `hidden` atributiga ega bo'lsin. Brauzerda tekshiring: ikkinchi paragraf ekranda ko'rinmasligi kerak.
**Kutiladigan natija:** Ekrandan to'liq yashirilgan element kodi.

### 4. Yangi rang tanlash (`color`) kiritish maydoni <Badge type="tip" text="oson" />
Oddiy forma yarating. Unda `type="color"` bo'lgan input joylashtiring. Brauzerda ushbu maydonni bosib, ranglar palitrasi ochilganini ko'ring.
**Kutiladigan natija:** Rang tanlash interfeysiga ega mini-forma.

### 5. `data-*` atributlari bilan mahsulot kartochkasi <Badge type="warning" text="o'rta" />
Bitta smartfon kartochkasi (`<article>`) tuzing. Unda:
- `data-id="9901"`
- `data-model="Samsung Galaxy"`
- `data-price="600"`
- `data-brand="Samsung"`
atributlari bo'lsin. Ichida telefon nomi va narxi ko'rinsin.
**Kutiladigan natija:** Yashirin metama'lumotlarga ega semantik mahsulot kartochkasi.

### 6. Slayder (`range`) boshqaruvi bilan ovoz balandligi <Badge type="warning" text="o'rta" />
Forma ichida 0 dan 100 gacha bo'lgan oraliqni boshqaruvchi `<input type="range" min="0" max="100" value="50">` slayderini qo'ying. Oldiga `<label>` bilan «Ovoz balandligi:» deb yozing.
**Kutiladigan natija:** O'ngga-chapga suriluvchi standart HTML5 slayderi.

### 7. `tabindex` orqali ro'yxatdan o'tish formasini tartiblash <Badge type="warning" text="o'rta" />
3 ta kiritish maydonidan iborat forma tuzing: Ism, Familiya, Telefon. `tabindex` atributi orqali birinchi bo'lib Ismga (`tabindex="1"`), keyin Telefonga (`tabindex="2"`), oxirida Familiyaga (`tabindex="3"`) o'tadigan tartib o'rnating va klaviaturadagi `Tab` tugmasi bilan tekshiring.
**Kutiladigan natija:** Qat'iy tartibli klaviatura fokusi zanjiri.

### 8. Murakkab forma validatsiyasi <Badge type="warning" text="o'rta" />
Quyidagi talablarga ega ro'yxatdan o'tish formasini yozing:
- Ism (`type="text" required placeholder="Kamida 3 ta harf" minlength="3"`);
- Yosh (`type="number" min="10" max="18" required`);
- Elektron pochta (`type="email" required`);
- Tug'ilgan sana (`type="date" required`).
Bo'sh qoldirib yuborish tugmasi bosilganda brauzer qanday ogohlantirish berishini sinab ko'ring.
**Kutiladigan natija:** HTML5 ning ichki avtomatik validatsiyasiga ega mukammal forma.

### 9. I bob katta yakuniy loyihasi: «Mening interaktiv veb-sahifam» <Badge type="danger" text="qiyin" />
O'zingiz qiziqqan mavzuda (kosmos, avtomobillar, kibersport, IT sohalari) to'liq 1 sahifalik loyiha quring. Loyihada bo'lishi shart:
1. Semantik arxitektura (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`);
2. Kamida 1 ta video pleer yoki audio pleer;
3. Bitta ilmiy rasm `<figure>` va `<figcaption>` bilan;
4. 2 ta savoldan iborat `<details>` akkordeoni;
5. Bilim yoki yutuqlar foizi `<progress>` bilan;
6. Fikr-mulohaza yuborish formasi (`color`, `date`, `textarea`).
**Kutiladigan natija:** I bobning barcha bilimlarini namoyish etuvchi tayyor shaxsiy veb-loyiha.

### 10. Kod auditi va semantik xatolarni tuzatish <Badge type="danger" text="qiyin" />
Sinfdoshingiz yozgan kodni tekshiring:
- Barcha ochilgan teglar to'g'ri yopilganmi?
- Bitta sahifada faqat 1 ta `<main>` ishlatilganmi?
- Rasmlarda `alt` atributi bormi?
- Formalarda `label` va `input` to'g'ri bog'langanmi?
Xatolarni aniqlab, ularni tuzatilgan variantini taqdim eting.
**Kutiladigan natija:** Dasturchilik tahlili va kodni tekshirish ko'nikmasi.

### 11. Kelajakka qadam: CSS bilan dastlabki tajriba <Badge type="info" text="bonus" />
Tuzgan HTML5 sahifangizning `<head>` qismiga `<style>` tegi oching. Unda:
`body { background-color: #f0f4f8; font-family: sans-serif; }`
`header { background-color: #0066cc; color: white; padding: 20px; }`
deb yozib ko'ring. Sahifa qanday o'zgarganini kuzating va keyingi 4-haftada nimalarni o'rganishingizni tasavvur qiling!
**Kutiladigan natija:** HTML skeletining CSS yordamida jonlanishini his qilish va yangi bobga motivatsiya.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Maxsus atributlar (masalan `src`) bilan global atributlar (`id`, `class`) o'rtasidagi farq nima?
2. `id` va `class` qanday vaziyatlarda qo'llaniladi va ularning asosiy farqi nimada?
3. `data-*` atributining vazifasi va u qanday nomlanishi mumkin?
4. `hidden` atributi qanday ishlaydi?
5. `contenteditable="true"` elementi qanday imkoniyat beradi?
6. Yangi HTML5 input turlaridan 3 tasini sanab bering.
7. I bob yakunida HTML bo'yicha qanday eng muhim bilimlarni egalladingiz?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. **Nazariy xulosa:** I bobda o'tilgan barcha 9 ta dars konspektlarini ko'zdan kechiring.
2. **Katta loyihani yakunlash:** «Mening interaktiv shaxsiy portfoliom» sahifasini to'liq kodlab, `index.html` fayli sifatida saqlang.
3. **II bobga tayyorgarlik:** Keyingi haftada boshlanadigan CSS (Cascading Style Sheets) texnologiyasi haqida qisqacha ma'lumot qidiring.

</div>

