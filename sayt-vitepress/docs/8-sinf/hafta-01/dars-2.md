---
title: "2-dars. HTML hujjat strukturasi. Teg, atribut, head, sarlavhalar"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "8-sinf", "link": "/8-sinf/"}, "week": {"n": 1, "link": "/8-sinf/hafta-01/"}, "g": 2, "title": "HTML hujjat strukturasi. Teg, atribut, head, sarlavhalar", "lead": "Bugun siz birinchi marta brauzer tushunadigan haqiqiy HTML faylni o'zingiz yozasiz: skelet, ko'rinmas sozlamalar va sarlavhalar. Shundan keyin istalgan sayt «ichini» ochib o'qiy olasiz.", "slide": "/slaydlar/8-sinf/hafta-01/dars-2.html", "test": "/slaydlar/8-sinf/hafta-01/dars-2-test.html", "tabs": [{"g": 1, "link": "/8-sinf/hafta-01/dars-1", "current": false}, {"g": 2, "link": "/8-sinf/hafta-01/dars-2", "current": true}, {"g": 3, "link": "/8-sinf/hafta-01/dars-3", "current": false}], "prev": {"g": 1, "title": "Internet qanday ishlaydi? DNS, hosting, domain. Front-end va Back-end", "link": "/8-sinf/hafta-01/dars-1"}, "next": {"g": 3, "title": "Matn teglari, <a> tegi, block va inline elementlar", "link": "/8-sinf/hafta-01/dars-3"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- HTML — veb-sahifaning skeleti (tuzilishi). Hisoblamaydi, faqat «bu sarlavha, bu abzats» deb belgilaydi.
- Teg — burchakli qavs ichidagi buyruq (`<p>`). Ochuvchi, mazmun va yopuvchi teg birga **element** deyiladi.
- Atribut tegga qo'shimcha ma'lumot beradi: `nom="qiymat"`, faqat ochuvchi tegda.
- Teglar matryoshka kabi ichma-ich: oxirgi ochilgan teg birinchi yopiladi.
- Skelet: `<!DOCTYPE html>`, `<html lang="uz">`, `<head>` (ko'rinmaydi), `<body>` (ko'rinadi).
- Head ichida: `title`, `meta charset`, `meta viewport`, `meta description`, `meta author`.
- `h1`–`h6`: mazmun darajasi. Sahifada odatda bitta `h1`, tartib buzilmaydi.
- Kodni 2 probel bilan suramiz (indent): o'qish osonlashadi.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### Nega HTML «dasturlash tili» emas?
Dasturlash tilida siz amal bajarasiz: hisoblaysiz, shart tekshirasiz. HTML esa faqat belgilaydi. Uni uy rejasiga o'xshating: «bu yerda xona, bu yerda eshik». Rejaning o'zi hech narsa qurmaydi, lekin usiz qurish mumkin emas. Rang va shakl (CSS) hamda harakat (JavaScript) keyin qo'shiladi.

### Bo'sh teglar nega yopilmaydi?
Ko'pchilik teglar mazmunni «o'rab oladi»: `<p>...</p>`. Lekin `<br>` (qator uzish) yoki `<img>` (rasm) o'rab oladigan narsaga ega emas, ular bir joyga bitta narsa qo'yadi. Shuning uchun ularga yopuvchi teg kerak emas.

```html
<p>Birinchi qator<br>Ikkinchi qator</p>
```

### Brauzer bo'sh joylarni nima qiladi?
Kodda ketma-ket 10 ta probel yoki 5 ta Enter yozsangiz ham, brauzer ularni **bitta** probelga aylantiradi. Yangi abzats kerakmi, `<p>` yozing; faqat qator uzish kerakmi, `<br>`.

```html
<p>Salom,        dunyo!</p>
<!-- brauzerda: Salom, dunyo! -->
```

### charset va viewport: ko'rinmas, lekin muhim
- `<meta charset="UTF-8">` bo'lmasa, `o'`, `g'` va boshqa harflar «krakozyabra»ga (buzilgan belgilarga) aylanishi mumkin. Uni head'ning birinchi qatoriga yozing.
- `<meta name="viewport" content="width=device-width, initial-scale=1.0">` telefonga: «sahifani o'z ekran kengligida ko'rsat» deydi. Usiz telefon butun kompyuter sahifasini mayda qilib sig'dirishga urinadi.

### Sarlavha kattalik uchun emas
«Matn katta bo'lsin» deb `h1` ni tanlamang: kattalikni keyinroq CSS beradi. Sarlavha — **daraja**. Kitobdagi bob, paragraf va kichik paragraf kabi. Google va ko'zi ojiz foydalanuvchilar ishlatadigan ekran o'quvchilar sahifani aynan shu sarlavhalar orqali tushunadi.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| HTML | HyperText Markup Language: sahifa tuzilishini belgilash tili |
| Teg (tag) | Burchakli qavs ichidagi buyruq, masalan `<p>` |
| Element | Ochuvchi teg + mazmun + yopuvchi teg |
| Atribut | Tegga qo'shimcha ma'lumot beruvchi `nom="qiymat"` juftligi |
| Nesting | Teglarni bir-birining ichiga to'g'ri tartibda joylash |
| Bo'sh teg | Yopilmaydigan teg: `<br>`, `<img>`, `<meta>`, `<link>` |
| DOCTYPE | Brauzerga «bu zamonaviy HTML5 hujjat» deydigan e'lon |
| head | Sahifa haqidagi xizmat ma'lumotlari qismi (ekranda ko'rinmaydi) |
| body | Ekranda ko'rinadigan hamma narsa qismi |
| meta | Sahifa haqida ma'lumot beruvchi bo'sh teg |
| Indent | Ichki teglarni 2 probel surib yozish odati |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Hozirgi HTML versiyasi HTML5 deb ataladi, `<!DOCTYPE html>` aynan shuni bildiradi.
- Brauzer xato yozilgan HTML'ni ham «tuzatib» ko'rsatishga urinadi, shuning uchun xatolar ba'zan darrov sezilmaydi, lekin turli brauzerda har xil chiqishi mumkin.
- `meta keywords` bir paytlar qidiruvda muhim edi, hozir qidiruv tizimlari unga deyarli e'tibor bermaydi.
- Sahifaning istalgan joyida o'ng tugmani bosib «Ko'rish kodi» (View source) qilsangiz, o'sha sayt HTML'ini o'qiy olasiz.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Skeletni ko'rmasdan yozing <Badge type="tip" text="oson" />
`sahifa.html` yarating va `DOCTYPE`, `html`, `head`, `body`, `title` ni namunaga qaramay yozing. `title` ga ismingizni, `body` ga `h1` bilan «Salom, ...!» yozing.

**Kutiladigan natija:** brauzer yorlig'ida ismingiz, sahifada katta sarlavha.

### 2. Bu kod nima chiqaradi? <Badge type="tip" text="oson" />
Quyidagi kodni brauzer qanday ko'rsatadi? Avval bashorat qiling, keyin tekshiring.

```html
<p>Birinchi        qator
ikkinchi qator<br>uchinchi qator</p>
```

**Kutiladigan natija:** nechta qator ko'rinishi va nima uchun shunday bo'lgani haqida bir jumla izoh.

### 3. Atributni o'zgartiring <Badge type="tip" text="oson" />
`<p title="Salom!">Kursorni bosib turing</p>` yozing. Keyin `title` qiymatini o'zgartirib, ismingizni chiqaring.

**Kutiladigan natija:** kursor abzats ustida turganda ismingiz yozuvi chiqadi.

### 4. Teglarni ajrating <Badge type="tip" text="oson" />
`<p>Bu <strong>muhim</strong> gap.</p>` qatoridagi: ochuvchi teglar, yopuvchi teglar, mazmun va elementlarni alohida yozib chiqing (nechta element bor?).

**Kutiladigan natija:** to'g'ri ro'yxat va elementlar sonini aniq aytish.

### 5. «Men haqimda» sahifasi <Badge type="warning" text="o'rta" />
`haqimda.html` yarating: `meta charset`, `viewport`, `description`, `author`; `h1` (ismingiz), uchta `h2` (Men haqimda, Qiziqishlarim, Maqsadlarim) va har birining ostida kamida bitta `p`. Matnda `o'` va `g'` harflari bo'lsin.

**Kutiladigan natija:** ierarxiyali sahifa, o'zbekcha harflar to'g'ri ko'rinadi.

### 6. Charset tajribasi <Badge type="warning" text="o'rta" />
Faylingizdan `<meta charset="UTF-8">` qatorini vaqtincha o'chirib, sahifani yangilang. Harflar o'zgardimi? Keyin qaytarib qo'ying. Natijani qisqa yozib qo'ying (o'zgardi yoki yo'q, qaysi brauzerda).

**Kutiladigan natija:** tajriba tavsifi; ba'zi brauzerlar o'zi to'g'ri taxmin qiladi, shuning uchun natija har xil bo'lishi mumkin.

### 7. Sarlavha daraxti <Badge type="warning" text="o'rta" />
Sevimli filmingiz yoki o'yiningiz haqida sahifa yozing: bitta `h1`, kamida uchta `h2` va ba'zi `h2` ostida `h3`. Hamma sarlavhalar mantiqiy tartibda bo'lsin.

**Kutiladigan natija:** sarlavhalar tartibi buzilmagan (h1 dan keyin h4 yo'q).

### 8. Telefonda ko'rish <Badge type="warning" text="o'rta" />
Brauzerda sahifani oching, F12 → qurilma (telefon) rejimini yoqing. `viewport` qatori bor va yo'q holatlarni solishtiring.

**Kutiladigan natija:** ikki holatdagi farqni tasvirlaydigan 2-3 jumla.

### 9. Xatoni top <Badge type="danger" text="qiyin" />
Quyidagi kodda kamida 6 ta xato bor. Hammasini toping, ro'yxat qiling va to'g'ri variantini yozing.

```html
<html lang=uz>
  <body>
    <title>Test</title>
    <h1>Mening saytim
    <p>Birinchi abzats
    <h4>Kichik sarlavha</h4>
    <p><strong>Muhim matn</p></strong>
  </body>
</html>
```

**Kutiladigan natija:** xatolar ro'yxati va ishlaydigan, to'g'ri tuzilgan sahifa.

### 10. Boshqa sayt «ichida» <Badge type="danger" text="qiyin" />
Biror maktab yoki yangiliklar saytini oching, o'ng tugma → «View source». Toping: `lang` atributi, `title`, nechta `meta` bor, `h1` nechta.

**Kutiladigan natija:** to'rtta topilmaning ro'yxati va bitta qiziq kuzatuv.

### 11. Sinf saytining bosh sahifasi <Badge type="danger" text="qiyin" />
Sinfdoshlaringiz haqida sahifa yozing: `h1` (sinf nomi), har bir o'quvchi uchun `h2` (ism), uning ostida `h3` («Qiziqishi», «Maqsadi») va abzatslar. To'liq head (charset, viewport, description, author, title) va to'g'ri indent.

**Kutiladigan natija:** kamida 3 ta `h2`, 6 ta `h3`, hamma teglar yopilgan.

### 12. Bonus: o'z sahifangizni «buzing» <Badge type="info" text="bonus" />
Ataylab 3 xil xato qiling (yopilmagan teg, noto'g'ri tartib, `h1` dan keyin `h4`) va brauzer nima qilishini kuzating. Do'stingizga ko'rsating: u xatolarni topa oladimi?

**Kutiladigan natija:** xatolar ro'yxati va brauzer «tuzatgan» natija haqida kuzatuv.

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Qaysi qism ekranda ko'rinmaydi: `head` yoki `body`? Istisno bormi?
2. `<meta charset="UTF-8">` nima uchun kerak?
3. Teg va element o'rtasida qanday farq bor?
4. Atribut qayerda yoziladi va qanday ko'rinishga ega?
5. Nega `h1` dan keyin darrov `h4` yozmaymiz?
6. `<br>` va `<img>` nima uchun yopilmaydi?
7. `viewport` bo'lmasa telefonda nima bo'ladi?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

**«Sevimli o'yinim/hobbim» sahifasi** (20–30 daqiqa): `hobbi.html` yarating. To'liq skelet (`lang="uz"`, `charset`, `viewport`, `description`, `author`, `title`), bitta `h1`, ikkita `h2`, ularning ostida abzatslar va bitta `h3`. Kodda indent bo'lsin, barcha teglar yopilsin, o'zbekcha harflar to'g'ri chiqsin.

</div>

