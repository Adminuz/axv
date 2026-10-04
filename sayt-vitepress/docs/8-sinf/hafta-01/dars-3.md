---
title: "3-dars. Matn teglari, <a> tegi, block va inline elementlar"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "8-sinf", "link": "/8-sinf/"}, "week": {"n": 1, "link": "/8-sinf/hafta-01/"}, "g": 3, "title": "Matn teglari, <a> tegi, block va inline elementlar", "lead": "Oddiy matn bugun «jonlanadi»: so'zlar qalin, qiyshiq, sariq bo'ladi va bosiladigan havolaga aylanadi. Telegramdagi har bir ko'k yozuv qanday ishlashini ham bilib olasiz.", "slide": "/slaydlar/8-sinf/hafta-01/dars-3.html", "tabs": [{"g": 1, "link": "/8-sinf/hafta-01/dars-1", "current": false}, {"g": 2, "link": "/8-sinf/hafta-01/dars-2", "current": false}, {"g": 3, "link": "/8-sinf/hafta-01/dars-3", "current": true}], "prev": {"g": 2, "title": "HTML hujjat strukturasi. Teg, atribut, head, sarlavhalar", "link": "/8-sinf/hafta-01/dars-2"}, "next": null}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- Matn teglari matnga **ma'no** beradi: `<strong>` (muhim), `<em>` (ta'kidlangan), `<mark>` (belgilangan).
- `<b>`, `<i>`, `<u>` faqat ko'rinishni o'zgartiradi, ma'no bermaydi. Ma'no uchun `strong` va `em` ishlatiladi.
- Pastki va yuqori indeks: `<sub>` va `<sup>`; klaviatura tugmasi: `<kbd>`; qisqartma: `<abbr title="...">`.
- `<a href="...">` havola yaratadi. `href` majburiy atribut.
- Yangi tabda ochish: `target="_blank"` va yoniga `rel="noopener noreferrer"`.
- Havola turlari: tashqi sayt, o'z saytingizdagi sahifa, sahifa ichidagi joy (`#id`), `mailto:` va `tel:`.
- Block elementlar (`h1`, `p`, `div`) yangi qatordan boshlanadi; inline elementlar (`span`, `a`, `strong`) qator ichida turadi.
- Inline element block ichida turadi; `<p>` ichiga `<p>` yoki `<h1>` qo'yib bo'lmaydi.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### Nega `strong` bor, `b` ham bor?

Tasavvur qiling, ikki kishi bir xil qalin yozuv yozdi. Birinchisi: «DIQQAT, ertaga imtihon!» (bu muhim). Ikkinchisi do'kon nomini chiroyli qilib qalin yozdi (bu shunchaki bezak). Ko'zga ikkalasi bir xil ko'rinadi, lekin ma'nosi boshqa. Brauzer, qidiruv tizimi va ekranni o'qib beruvchi dastur ma'noni `strong` orqali tushunadi. Bezak esa keyinroq **CSS** bilan beriladi. Shuning uchun qoida: avval ma'no, keyin ko'rinish.

### Havola yo'lining uch xili

```html
<a href="https://google.com">Google</a>   <!-- boshqa sayt: to'liq manzil -->
<a href="aloqa.html">Aloqa</a>            <!-- o'z saytingiz: faqat fayl nomi -->
<a href="#pastki">Pastga</a>              <!-- shu sahifada: # va id -->
```

Birinchisi xuddi shahar nomi va ko'cha bilan to'liq pochta manzil yozishga o'xshaydi. Ikkinchisi «qo'shni xonaga o'ting» deganidek: fayllar bir papkada bo'lsa, faqat nomi yetadi. Uchinchisi esa shu sahifaning ichidagi «yorliq»: `id="pastki"` qo'yilgan joyga sakraydi.

### Nega `rel="noopener noreferrer"`?

`target="_blank"` yangi tab ochadi. Ba'zi eski brauzerlarda yangi sahifa sizning sahifangizni nazorat qila olardi. `rel` shu yo'lni yopadi. Qoida oddiy: `target="_blank"` yozdingizmi, `rel` ham yozing.

### Block va inline: kitob o'xshatishi

Block elementlar kitobdagi abzats kabi: har biri yangi qatordan boshlanadi va butun kenglikni egallaydi. Inline elementlar esa gap ichidagi so'z kabi: faqat o'z o'rnini egallaydi. Shuning uchun `<span>` lar bir qatorda turadi, `<p>` lar esa pastga tushadi. Tegni `<p>` ichiga boshqa `<p>` qo'yish abzats ichida yana abzats yozishga o'xshaydi, bu mantiqsiz.

### Odatiy xatolar

- Yopuvchi tegni unutish: keyingi matn hammasi qalin (yoki havola) bo'lib ketadi.
- Teglarni noto'g'ri tartibda yopish: `<b><i>x</b></i>`. To'g'risi: oxirgi ochilgan birinchi yopiladi.
- Atribut qiymatini qo'shtirnoqsiz yozish.
- Sarlavhani matn kattalashtirish uchun ishlatish.
- Fayl nomida bo'sh joy va katta harf: `Mening Sahifam.HTML`. To'g'risi: `index.html`, `aloqa.html`.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Semantik teg | Matnning ma'nosini bildiruvchi teg (`strong`, `em`) |
| Atribut | Tegga qo'shimcha ma'lumot beruvchi juft: `href="..."` |
| `href` | Havola manzili (hypertext reference) |
| `target` | Havola qayerda ochilishini belgilaydi |
| `rel` | Joriy sahifa va havola orasidagi aloqa; xavfsizlik uchun ham ishlatiladi |
| Nisbiy yo'l | Joriy fayldan boshlab yozilgan manzil: `aloqa.html` |
| Block element | Yangi qatordan boshlanib, butun kenglikni egallaydi |
| Inline element | Qator ichida, o'z kengligicha turadi |
| Indeks | Pastki (`sub`) yoki yuqori (`sup`) yozilgan kichik belgi |
| Indent | Kodni ichma-ich surib yozish |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Havola so'zi inglizchada *hyperlink* deyiladi, internet shu havolalar tufayli «to'r» (web) deb ataladi.
- `<mark>` tegi matnni xuddi markerda bo'yaganday sariq qiladi.
- `<q>` tegida qo'shtirnoqni o'zingiz yozmaysiz: brauzer o'zi qo'yadi.
- `mailto:` va `tel:` havolalar telefonda bosilganda pochta ilovasini yoki qo'ng'iroq oynasini ochadi.
- Qidiruv tizimlari `strong` va `em` ni o'qib, sahifaning nima haqida ekanini tushunadi.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Qaysi teg? <Badge type="tip" text="oson" />
Quyidagi jumlalarning har biri uchun mos tegni yozing: «muhim ogohlantirish», «sariq bilan belgilangan joy», «H2O dagi 2», «x2 dagi 2», «Ctrl tugmasi».

**Kutiladigan natija:** besh jumlaga besh to'g'ri teg nomi (daftarda yoki matn faylida).

### 2. Birinchi havola <Badge type="tip" text="oson" />
`ilk-havola.html` yarating (to'liq skelet bilan). Ichiga sevimli saytingizga havola qo'ying. Matni sayt nomi bo'lsin.

**Kutiladigan natija:** brauzerda havola bosilganda sayt ochiladi.

### 3. Block yoki inline? <Badge type="tip" text="oson" />
Quyidagilarning har birini block yoki inline deb belgilang: `<h2>`, `<span>`, `<p>`, `<a>`, `<div>`, `<em>`, `<code>`, `<h1>`.

**Kutiladigan natija:** 8 ta element, har biri to'g'ri turga ajratilgan.

### 4. Bu kod nima ko'rsatadi? <Badge type="tip" text="oson" />
Brauzer bu kodda nimani qanday ko'rsatadi? Avval daftarda bashorat qiling, keyin brauzerda tekshiring.

```html
<p>Sinfda <strong>3</strong> nafar o'quvchi. <em>Hammasi</em> faol!</p>
<span>A</span><span>B</span>
<p>C</p>
```

**Kutiladigan natija:** nechta qator hosil bo'lishi va qaysi so'z qanday ko'rinishi aytilgan; bashoratingiz brauzer bilan solishtirilgan.

### 5. Yangi tabda ochiladigan havola <Badge type="warning" text="o'rta" />
`havolalar.html` yarating: sarlavha, qisqa tanishtiruv abzatsi va kamida 3 havola. Biri yangi tabda (`target` va `rel` bilan), biri `title` bilan, biri `mailto:` bilan bo'lsin. Sahifa oxirida `<small>` bilan «© 2026» yozuvi tursin.

**Kutiladigan natija:** hamma havolalar ishlaydi; yangi tab to'g'ri ochiladi; kursorni olib borganda `title` chiqadi.

### 6. Xatoni toping <Badge type="warning" text="o'rta" />
Quyidagi kodda kamida 4 ta xato bor. Toping, nima uchun xato ekanini yozing va to'g'rilab, faylda ishlatib ko'ring.

```html
<p><h1>Mening saytim</h1></p>
<p>Menga <strong><em>sayt</strong></em> yoqadi.
<a href=https://uz.wikipedia.org target="_blank">Vikipediya</a>
```

**Kutiladigan natija:** to'g'rilangan kod, har bir xato uchun bir jumlali izoh.

### 7. Qisqartmalar lug'ati <Badge type="warning" text="o'rta" />
`qisqartma.html` yarating. Unda kamida 4 ta qisqartmani (masalan, HTML, CSS, DNS, URL) `<abbr title="...">` bilan yozing. Har biri uchun title da to'liq ingliz nomi bo'lsin.

**Kutiladigan natija:** kursor qisqartma ustida turganda to'liq nom chiqadi.

### 8. Klaviatura qo'llanmasi <Badge type="warning" text="o'rta" />
Kompyuterda ishlash uchun 5 ta tez tugma (masalan, nusxalash, qo'yish, saqlash) haqida qisqa qo'llanma sahifasi yarating. Har bir tugma `<kbd>` ichida bo'lsin, har bir qator alohida abzatsda.

**Kutiladigan natija:** 5 ta abzats, har birida kamida bitta `<kbd>`.

### 9. Ikki sahifali mini-sayt <Badge type="danger" text="qiyin" />
`index.html` va `haqida.html` yarating, ikkalasi bir papkada. Har birida to'liq skelet, `<title>` va `<meta name="description">` bo'lsin. Sahifalar bir-biriga havola qilsin. `index.html` da sahifa ichidagi havola ham bo'lsin: pastda `id="oxiri"` li `<h2>`, unga yetish uchun yetarlicha matn yozing.

**Kutiladigan natija:** ikki sahifa orasida o'tish ishlaydi; «Sahifa oxiriga» havolasi sahifani pastga sakratadi.

### 10. Mening maqolam <Badge type="danger" text="qiyin" />
Sevimli mavzuda (o'yin, hayvon, shahar) maqola yozing: `<h1>`, ikkita `<h2>` va abzatslar. Kamida bittadan `<strong>`, `<em>`, `<abbr>`, `<q>` va bitta tashqi havola bo'lsin.

**Kutiladigan natija:** sahifa to'g'ri ochiladi, barcha teglar yopilgan, kod surib yozilgan.

### 11. Mazmunli ro'yxat sahifasi <Badge type="danger" text="qiyin" />
Maktab jadvalini nusxa qilib, bitta sahifa yarating: har bir fan nomi `<strong>`, o'qituvchi ismi `<em>`, xona raqami `<mark>` bilan. Har bir fanning oxirida o'qituvchiga yozish uchun `mailto:` havola bo'lsin (manzillar soxta, masalan, `test@example.com`).

**Kutiladigan natija:** kamida 4 ta fan; har biri uchun uch xil teg va bitta havola ishlatilgan.

### 12. Tadqiqot: hamma narsa havola <Badge type="info" text="bonus" />
Sevimli saytingizni (Instagram, YouTube, maktab sayti) brauzerda oching. Sahifaning ustida o'ng tugmani bosing va «Ko'rish» (View page source) orqali kodini oching. `<a` ni qidirib, kamida 5 ta havolani toping. Har biri qaysi turga kirishini yozing: tashqi, nisbiy, `#id`, `mailto:` yoki `tel:`.

**Kutiladigan natija:** 5 ta havola ro'yxati, har biri uchun tur va qaysi atributlar borligi (`target`, `rel`, `title`).

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. `<strong>` va `<b>` ning farqi nima?
2. `href` atributi nima uchun kerak?
3. Havolani yangi tabda ochish uchun qanday atribut yoziladi va unga yana nima qo'shiladi?
4. `<p>` block elementmi yoki inline? `<span>`-chi?
5. H2O dagi 2 ni qaysi teg bilan yozasiz? x2 dagi 2-chi?
6. `<p>` ichiga `<h1>` qo'yish mumkinmi? Nima uchun?
7. Fayl nomi sifatida `Mening Sahifam.HTML` nima uchun noto'g'ri?
8. `mailto:` bilan boshlanuvchi havola bosilganda nima bo'ladi?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

**«Qiziqarli ma'lumot» (20–30 daqiqa).** `malumot.html` faylida 3 ta abzatsli kichik maqola yozing. Maqolada kamida `<strong>`, `<em>`, `<mark>`, `<sub>` yoki `<sup>`, `<abbr title>` va `<q>` bo'lsin; 2 ta havola ham bo'lsin (biri `target="_blank"` va `rel` bilan). Sahifa oxirida `<small>` bilan muallif yozuvi tursin.

Ixtiyoriy: 2-darsdagi `hobbi.html` bilan shu sahifa o'rtasida havolalar yarating.

</div>

