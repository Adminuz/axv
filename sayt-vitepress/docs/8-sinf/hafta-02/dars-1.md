---
title: "4-dars. Rasm va ro'yxat teglari: <img>, <figure>, <ul>, <ol>, <dl>"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "8-sinf", "link": "/8-sinf/"}, "week": {"n": 2, "link": "/8-sinf/hafta-02/"}, "g": 4, "title": "Rasm va ro'yxat teglari: <img>, <figure>, <ul>, <ol>, <dl>", "lead": "Surat mingta so'zdan afzal, ro'yxatlar esa har qanday chalkashlikni tartibga soladi. Ushbu darsda veb-sahifaga rasm joylash, to'g'ri manzillarni ko'rsatish va 3 xil ro'yxat turidan foydalanishni o'rganamiz.", "slide": "/slaydlar/8-sinf/hafta-02/dars-1.html", "tabs": [{"g": 4, "link": "/8-sinf/hafta-02/dars-1", "current": true}, {"g": 5, "link": "/8-sinf/hafta-02/dars-2", "current": false}, {"g": 6, "link": "/8-sinf/hafta-02/dars-3", "current": false}], "prev": null, "next": {"g": 5, "title": "Jadval teglari: <table>, <tr>, <td>, <th>, colspan va rowspan", "link": "/8-sinf/hafta-02/dars-2"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- `<img>` — yopiluvchi jufti bo'lmagan (void), inline-block element.
- `src` atributi rasm manzilini, `alt` esa rasm ochilmay qolganda yoki screen reader uchun muqobil matnni bildiradi.
- `alt` atributini hech qachon tashlab ketmang — bu foydalanuvchilar qulayligi va SEO uchun nihoyatda zarur.
- Fayl yo'llari ikki xil bo'ladi: **mutlaq** (internetdagi to'liq URL) va **nisbiy** (joriy fayl joylashgan joyga nisbatan yo'l).
- `<figure>` va `<figcaption>` teglari rasmni va uning rasmiy izohini bitta semantik blok sifatida birlashtiradi.
- `<ul>` (Unordered List) — tartibsiz, nuqtali ro'yxat; har bir band `<li>` bilan belgilanadi.
- `<ol>` (Ordered List) — raqamlangan ro'yxat; `type`, `start`, `reversed` atributlariga ega.
- `<dl>` (Description List) — atamalar (`<dt>`) va ularning izohi (`<dd>`) uchun ta'riflar ro'yxati.
- Ro'yxatlar ichma-ich (nested) joylashishi mumkin: ichki ro'yxat har doim ota ro'yxatning `<li>` tegi ichiga yoziladi.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### Nisbiy yo'llarda adashmaslik siri
Ko'pchilik boshlovchilar rasm sahifada ko'rinmay qolsa hayron bo'lishadi. Bunga sabab — fayl yo'lining (path) noto'g'ri ko'rsatilishidir:
- Agar `index.html` va `rasm.png` bir papkada bo'lsa: `src="rasm.png"`.
- Agar `rasm.png` shu papka ichidagi `images` nomli jildda bo'lsa: `src="images/rasm.png"`.
- Agar `index.html` biror papka ichida, rasm esa tashqarida bo'lsa: `src="../rasm.png"` (`..` bitta yuqoridagi papkaga chiqishni bildiradi).

### Nega rasm o'lchamini (width va height) HTMLda yozish tavsiya etiladi?
Agar `width="600" height="400"` atributlarini yozmasangiz, brauzer rasm yuklanguncha uning o'lchamini bilmaydi. Rasm internetdan yuklangach, butun matn to'satdan pastga sakrab ketadi (buni dasturchilar **CLS — Cumulative Layout Shift** deb atashadi). O'lcham oldindan berilsa, brauzer rasm uchun joy ajratib qo'yadi va sahifa qotmay, chiroyli ochiladi.

### `<ol>` ning maxsus atributlari
Raqamlangan ro'yxat faqat 1, 2, 3 bilan cheklanmaydi:
- `type="A"` — A, B, C...
- `type="a"` — a, b, c...
- `type="I"` — I, II, III...
- `start="10"` — sanashni 10-raqamdan boshlaydi.
- `reversed` — teskari sanaydi (masalan, 3, 2, 1). Raketa uchirish yoki top-10 talik uchun ayni muddao!

### Ro'yxat ichida ro'yxat (Nested List) xatosi
Eng ko'p uchraydigan xato — ichki `<ul>` ni `<li>` dan tashqariga chiqarib qo'yish:
```html
<!-- XATO VARIANT: -->
<ul>
  <li>Meva</li>
  <ul>
    <li>Olma</li>
  </ul>
</ul>

<!-- TO'G'RI VARIANT: -->
<ul>
  <li>Meva
    <ul>
      <li>Olma</li>
    </ul>
  </li>
</ul>
```

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| `<img>` (Image) | Veb-sahifaga rasm joylashtiruvchi teg |
| `src` (Source) | Rasm yoki faylning kelib chiqish manbasi / manzili |
| `alt` (Alternative Text) | Rasm ochilmaganda chiqadigan matnli tavsif |
| Nisbiy yo'l (Relative Path) | Faylning joriy sahifaga nisbatan joylashuvi |
| Mutlaq yo'l (Absolute Path) | Faylning to'liq internet manzili (URL) |
| `<figure>` | Mustaqil rasm, diagramma yoki kod bloki semantik tegi |
| `<figcaption>` | `<figure>` ichidagi rasmning matnli izohi |
| `<ul>` (Unordered List) | Tartibsiz (markerli) ro'yxat konteyneri |
| `<ol>` (Ordered List) | Tartiblangan (raqamli) ro'yxat konteyneri |
| `<li>` (List Item) | Ro'yxatning alohida bir elementi/bandi |
| `<dl>` (Description List) | Ta'riflar ro'yxati konteyneri |
| `<dt>` / `<dd>` | Ta'rif atamasi (term) / ta'rif izohi (details) |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Birinchi internet sahifasida (1991-yilda Tim Berners-Li tomonidan yaratilgan) birorta ham rasm bo'lmagan, faqatgina matn va havolalar bo'lgan.
- `<img>` tegi birinchi marta 1993-yilda NCSA Mosaic brauzerida paydo bo'lgan va internet olamida haqiqiy inqilob yasagan!
- Saytlardagi aksariyat navigatsiya menyulari (bosh sahifa, xizmatlar, aloqa tugmalari) aslida CSS yordamida chiroyli qilingan oddiy `<ul>` va `<li>` ro'yxatlaridir.
- Rasm yuklanish tezligini oshirish uchun zamonaviy brauzerlarda `loading="lazy"` atributi qo'llaniladi — bu rasm foydalanuvchi skroll qilib unga yaqinlashgandagina yuklanishini ta'minlaydi.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Saytingizga rasm joylang <Badge type="tip" text="oson" />
O'z kompyuteringizdagi yoki internetdagi ixtiyoriy rasmni `<img>` tegi yordamida sahifaga joylang. Unga `alt`, `width` va `title` atributlarini bering.

**Kutiladigan natija:** sahifada kursor olib borganda izoh ko'rsatadigan rasm paydo bo'ladi.

### 2. Xaridlar ro'yxati <Badge type="tip" text="oson" />
Bozorlik uchun 5 ta mahsulotdan iborat tartibsiz (`<ul>`) ro'yxat tuzing.

**Kutiladigan natija:** sahifada nuqtali markerlar bilan ajratilgan 5 ta mahsulot ro'yxati.

### 3. Kun tartibim <Badge type="tip" text="oson" />
Ertalab uyqudan turgandan to maktabga borguncha bajaradigan 5 ta amalingizni tartiblangan (`<ol>`) ro'yxat shaklida yozing.

**Kutiladigan natija:** 1 dan 5 gacha raqamlangan aniq ketma-ketlik.

### 4. Lug'at tuzing <Badge type="tip" text="oson" />
`<dl>`, `<dt>`, `<dd>` teglaridan foydalanib, o'zingiz bilgan 3 ta internet atamasiga qisqa izoh bering.

**Kutiladigan natija:** atamalar va ularning surilib yozilgan izohlari chiroyli ko'rinishda chiqadi.

### 5. Xatoni toping va to'g'rilang <Badge type="warning" text="o'rta" />
Quyidagi kodda 3 ta xato bor. Ularni toping va to'g'ri variantini yozing:
```html
<img href="logo.png">
<ol>
  Rim raqamlari
  <li>Birinchi</li>
  <li>Ikkinchi</li>
<ol>
```

**Kutiladigan natija:** xatolar tushuntirilgan va to'g'rilangan ishchi kod.

### 6. Teskari sanash va Rim raqamlari <Badge type="warning" text="o'rta" />
Ikkita alohida `<ol>` ro'yxat yarating: birinchisi 10 dan 1 gacha teskari sanasin (`reversed`), ikkinchisi esa Rim raqamlari bilan (I, II, III...) boshlansin.

**Kutiladigan natija:** sahifada teskari raqamlangan va rim raqamli ikkita ro'yxat.

### 7. Maqola uchun rasm (`<figure>`) <Badge type="warning" text="o'rta" />
O'zingiz yoqtirgan hayvon yoki shahar haqida 2 jumlalik matn, uning rasmi va rasmining ostida `<figcaption>` yordamida izoh berilgan semantik blok tuzing.

**Kutiladigan natija:** `<figure>` ichida birlashgan rasm va uning ostki rasmiy izohi.

### 8. Ikki bosqichli menyu <Badge type="warning" text="o'rta" />
Maktab fanlari ro'yxatini ichma-ich ro'yxat shaklida tuzing: "Aniq fanlar" ichida (Matematika, Informatika), "Tabiiy fanlar" ichida (Fizika, Biologiya) bo'lsin.

**Kutiladigan natija:** asosiy bandlar va ularning ichida 2 tadan ichki element.

### 9. O'quvchi portfeli sahifasi <Badge type="danger" text="qiyin" />
`profil.html` sahifasini yarating. Unda:
- Sizning rasmingiz (`<figure>` bilan);
- O'zingiz haqingizda qisqa tanishtiruv;
- Qiziqishlaringiz ro'yxati (`<ul>`);
- Eng katta 3 ta maqsadingiz (`<ol>`);
- Biladigan texnologiyalaringiz lug'ati (`<dl>`).

**Kutiladigan natija:** to'liq va barcha teglardan foydalanilgan shaxsiy tanishtiruv sahifasi.

### 10. Nisbiy yo'llar xaritasi <Badge type="danger" text="qiyin" />
Kichik loyiha papkalari tuzilmasini yarating:
```
loyiha/
  index.html
  assets/
    images/
      avatar.jpg
  pages/
    about.html
```
Savol: `about.html` sahifasidan `avatar.jpg` rasmini qanday yo'l (`src`) bilan chaqirish kerak? `index.html` dan-chi? Ikkala kodni yozing va yo'llar mantig'ini tushuntiring.

**Kutiladigan natija:** `../assets/images/avatar.jpg` va `assets/images/avatar.jpg` yo'llarining batafsil tahlili.

### 11. Milliy taomlar interaktiv menyusi <Badge type="info" text="bonus" />
Restoran menyusi sahifasini tuzing. Unda kamida 3 xil toifa (Taomlar, Ichimliklar, Shirinliklar) bo'lsin. Har bir taom yonida uning kichik rasmi (`width="100"`), narxi, masalliqlari (`<ul>`) va qisqa ta'rifi joylashsin.

**Kutiladigan natija:** to'liq formatlangan, rasmlar va ro'yxatlar bilan boyitilgan haqiqiy restoran menyusi sahifasi.

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. `src` va `href` atributlari o'rtasidagi farq nima?
2. `alt` atributi qanday holatlarda foydalanuvchiga yordam beradi?
3. Nisbiy yo'lda `../` belgisi nimani anglatadi?
4. `<figure>` tegi oddiy `<div>` dan nima bilan farq qiladi?
5. Qachon `<ul>`, qachon esa `<ol>` ishlatish to'g'ri bo'ladi?
6. Ichma-ich ro'yxat tuzganda eng asosiy sintaksis qoidasi qanday?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

O'zingiz qiziqqan biror mavzuda (masalan, sevimli avtomobilingiz, sport turi yoki kompyuter o'yini) veb-sahifa tayyorlang. Unda kamida 2 ta rasm (`<figure>` va `<figcaption>` bilan), 1 ta tartiblangan ro'yxat, 1 ta tartibsiz ro'yxat va 1 ta ta'riflar lug'ati (`<dl>`) bo'lsin.

</div>

