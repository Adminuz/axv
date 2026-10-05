---
title: "11-dars. CSS: rang va shrift bilan ishlash, meros olish"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "8-sinf", "link": "/8-sinf/"}, "week": {"n": 4, "link": "/8-sinf/hafta-04/"}, "g": 11, "title": "CSS: rang va shrift bilan ishlash, meros olish", "lead": "Bugun sahifangizga rang beramiz: matn, fon, gradient. Shrift va matn uslubi bilan o'qishni qulay qilamiz va «meros» sirini ochamiz.", "slide": "/slaydlar/8-sinf/hafta-04/dars-2.html", "test": null, "tabs": [{"g": 10, "link": "/8-sinf/hafta-04/dars-1", "current": false}, {"g": 11, "link": "/8-sinf/hafta-04/dars-2", "current": true}, {"g": 12, "link": "/8-sinf/hafta-04/dars-3", "current": false}], "prev": {"g": 10, "title": "CSS asoslari: ulash va selektorlar", "link": "/8-sinf/hafta-04/dars-1"}, "next": {"g": 12, "title": "CSS Box model: content, padding, border, margin", "link": "/8-sinf/hafta-04/dars-3"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- Matn rangi uchun `color`, fon rangi uchun `background-color`.
- Rang berish usullari: nom (`red`), hex (`#ff0000`), `rgb()`, `rgba()` (shaffoflik bilan), `hsl()`.
- Gradient: `background: linear-gradient(to right, royalblue, orange);`
- Shrift: `font-family`, `font-size`, `font-weight`, `font-style`.
- Matn: `text-decoration`, `text-align`, `line-height`, `letter-spacing`.
- Meros olish: `color`, `font-family`, `font-size` kabi xususiyatlar ota-elementdan bolaga o'tadi.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Hex rang qanday tuzilgan?
`#ff8000` — uchta juft: `ff` (qizil), `80` (yashil), `00` (ko'k). Har juft 00 dan ff gacha (0 dan 255 gacha). Hamma kanal to'liq yoqilsa `#ffffff` (oq), hammasi o'chiq bo'lsa `#000000` (qora).
```css
.oq { color: #ffffff; }
.qora { color: #000000; }
.qisqa { color: #f00; }   /* #ff0000 ning qisqa yozuvi */
```

### 2. rgba va shaffoflik
`rgba(0, 0, 0, 0.5)` — qora rang, 50% shaffof. Rasm ustidagi matn uchun yarim shaffof fon qulay:
```css
.yozuv {
  color: white;
  background-color: rgba(0, 0, 0, 0.6);
}
```

### 3. hsl nega qulay?
`hsl(210, 80%, 50%)`: birinchi son — rang burchagi (0 qizil, 120 yashil, 240 ko'k), keyingi ikkitasi — to'yinganlik va yorqinlik. Yorqinlikni o'zgartirib, bir rangning och va to'q variantlarini oson olasiz.

### 4. Zaxira shrift ro'yxati
```css
body {
  font-family: "Times New Roman", Georgia, serif;
}
```
Brauzer kompyuterda birinchi shriftni qidiradi, topilmasa ikkinchisiga o'tadi, oxirida `serif` (har qanday serifli shrift). Bo'sh joyli nomlar qo'shtirnoqda yoziladi.

### 5. Meros: oila o'xshatishi
Bola ota-onasidan ko'z rangini oladi, lekin kiyimini o'zi tanlaydi. Shuningdek `color` meros bo'lib o'tadi, `background-color` esa yo'q. Agar bola o'z qoidasini olsa, u meros ustidan yutadi.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| color | Matn rangi |
| background-color | Fon rangi |
| Hex | `#` bilan boshlanadigan 6 belgili rang kodi |
| rgb / rgba | Qizil, yashil, ko'k kanallar (a: shaffoflik) |
| hsl | Rang burchagi, to'yinganlik, yorqinlik |
| Gradient | Ranglar orasidagi silliq o'tish |
| font-family | Shrift turi |
| line-height | Qator balandligi |
| letter-spacing | Harflar orasidagi masofa |
| Inheritance | Meros olish: xususiyatning bolaga o'tishi |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Hex yozuvi bilan 16 777 216 xil rang yozish mumkin (256 × 256 × 256).
- CSS da 140 dan ortiq tayyor rang nomlari bor: masalan `tomato`, `skyblue`, `rebeccapurple`.
- `rebeccapurple` rangi 2014-yilda CSS ga vafot etgan qiz Rebekka Meyer xotirasiga qo'shilgan.
- Qator balandligi 1.5 – 1.6 atrofida bo'lsa, katta matnni o'qish qulay deb hisoblanadi.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Birinchi rang <Badge type="tip" text="oson" />
`h1` ning matnini qizil, fonini och sariq qiling: nom bilan.
**Kutiladigan natija:** qizil matn sariq fonda.

### 2. Hex bilan bo'yash <Badge type="tip" text="oson" />
`p` ga `#0a84ff` rangini bering. Keyin hex ni o'zgartirib, 3 ta boshqa rangni sinab ko'ring.
**Kutiladigan natija:** har safar abzats rangi o'zgaradi.

### 3. Shrift o'lchami <Badge type="tip" text="oson" />
`h1` ga `font-size: 36px`, `p` ga `font-size: 18px` bering.
**Kutiladigan natija:** sarlavha abzatsdan ancha katta.

### 4. Tagchiziqni olib tashlash <Badge type="tip" text="oson" />
Menyudagi havolalardan tagchiziqni olib tashlang va ularga rang bering.
**Kutiladigan natija:** havolalar chiziqsiz, rangli.

### 5. Bir rangning 4 xil yozuvi <Badge type="warning" text="o'rta" />
Bir xil ko'k rangni nom, hex, rgb va hsl bilan to'rt xil yozing (taxminiy ham bo'ladi).
**Kutiladigan natija:** 4 ta qoida, ranglar bir-biriga yaqin.

### 6. Shaffof fon <Badge type="warning" text="o'rta" />
`rgba()` yordamida yarim shaffof qora fon va oq matnli blok yarating.
**Kutiladigan natija:** orqa fon blok orasidan sezilib turadi.

### 7. Bu kod nima chiqaradi? <Badge type="warning" text="o'rta" />
```css
body { color: green; }
p { color: orange; }
```
```html
<body><h1>A</h1><p>B</p><span>C</span></body>
```
A, B va C qaysi rangda? Taxmin qiling, keyin tekshiring.
**Kutiladigan natija:** A va C yashil (meros), B to'q sariq.

### 8. Gradient banner <Badge type="warning" text="o'rta" />
`.banner` ga `linear-gradient` fon bering. Yo'nalishni `to right` dan `to bottom` ga o'zgartirib ko'ring.
**Kutiladigan natija:** gradient yo'nalishi o'zgargan.

### 9. O'qishga qulay matn <Badge type="danger" text="qiyin" />
Uzun matn uchun `font-family`, `font-size`, `line-height` va `letter-spacing` ni tanlang. Eng qulay variantni topish uchun 3 ta kombinatsiyani solishtiring.
**Kutiladigan natija:** o'zingiz tanlagan kombinatsiyaning sababi yozilgan.

### 10. Ko'rinmas matn xatosi <Badge type="danger" text="qiyin" />
Quyidagi sahifada matn ko'rinmaydi. Sababni toping va to'g'rilang:
```css
body { background-color: white; }
p { color: #ffffff; }
```
**Kutiladigan natija:** oq fonda oq matn bo'lgani aniqlangan va rang almashtirilgan.

### 11. Mening vizitkam <Badge type="danger" text="qiyin" />
Nom, kasb va aloqa ma'lumoti bor vizitka sahifasi yarating. Fon gradient, sarlavha markazda, havolalar chiziqsiz, matn `body` dan meros bo'lsin.
**Kutiladigan natija:** chiroyli, o'qiladigan vizitka.

### 12. Tadqiqot: meros bo'lmaydigan xususiyatlar <Badge type="info" text="bonus" />
`body` ga `border: 3px solid red` bering. Ichidagi elementlarga chegara o'tdimi? Yana qaysi xususiyatlar meros bo'lmasligini sinab, ro'yxat tuzing.
**Kutiladigan natija:** chegara faqat `body` da, ro'yxatda kamida 2 ta xususiyat.

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. `color` va `background-color` farqi nima?
2. Rangni qanday usullar bilan yozish mumkin?
3. `rgba()` dagi to'rtinchi qiymat nimani bildiradi?
4. `font-family` da nega bir nechta shrift yoziladi?
5. `line-height` va `letter-spacing` nimani o'zgartiradi?
6. Meros olish nima? Qaysi xususiyatlar o'tadi?
7. Bola elementga alohida qoida berilsa, meros bilan to'qnashsa nima bo'ladi?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

O'zingiz haqingizda sahifa yasab, unga rang palitrasi (kamida 3 rang), 2 xil shrift va gradient qo'shing. 20–30 daqiqa.

</div>

