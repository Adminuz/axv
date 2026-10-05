---
title: "12-dars. CSS Box model: content, padding, border, margin"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "8-sinf", "link": "/8-sinf/"}, "week": {"n": 4, "link": "/8-sinf/hafta-04/"}, "g": 12, "title": "CSS Box model: content, padding, border, margin", "lead": "Veb-sahifadagi har bir narsa bu quti. Bugun qutining ichini, devorini va atrofidagi bo'sh joyni boshqarishni o'rganasiz, shundan so'ng maketlar yasash osonlashadi.", "slide": "/slaydlar/8-sinf/hafta-04/dars-3.html", "test": null, "tabs": [{"g": 10, "link": "/8-sinf/hafta-04/dars-1", "current": false}, {"g": 11, "link": "/8-sinf/hafta-04/dars-2", "current": false}, {"g": 12, "link": "/8-sinf/hafta-04/dars-3", "current": true}], "prev": {"g": 11, "title": "CSS: rang va shrift bilan ishlash, meros olish", "link": "/8-sinf/hafta-04/dars-2"}, "next": null}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- Har bir HTML elementi to'rt qatlamli **quti** (box): content, padding, border, margin.
- **Padding** — mazmun va chegara orasidagi ichki masofa.
- **Border** — chegara: `border: 2px solid navy;`
- **Margin** — chegaradan tashqaridagi masofa, qo'shni elementlargacha.
- `padding: 10px 20px;` — tepa/past 10, chap/o'ng 20. To'rt qiymat — soat mili bo'yicha.
- `width` odatda faqat content ni beradi. `box-sizing: border-box` bilan padding va border ham ichiga kiradi.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Sovg'a qutisi o'xshatishi
Content — sovg'aning o'zi. Padding — qutidagi yumshoq qog'oz. Border — quti devori. Margin — javondagi qo'shni qutilargacha bo'sh joy. Qog'oz qalinlashsa, quti kattalashadi: xuddi `padding` oshganda element kattalashgani kabi.

### 2. Nega o'lcham «yolg'on gapiradi»?
```css
.quti {
  width: 300px;
  padding: 20px;
  border: 2px solid black;
}
```
Kutilgan: 300px. Aslida: 300 + 20·2 + 2·2 = **344px**. Chunki `width` faqat content o'lchami.
```css
* { box-sizing: border-box; }
```
Endi quti aniq 300px. Padding va border ichkariga «bosiladi», content kichrayadi.

### 3. Qisqa yozuvni o'qish
```css
margin: 10px;                /* hamma tomon */
margin: 10px 20px;           /* tepa-past | chap-o'ng */
margin: 10px 20px 30px 40px; /* tepa, o'ng, past, chap */
```
Esda tuting: soat miliga o'xshab tepadan boshlanadi.

### 4. Border-radius
`border-radius: 12px;` burchaklarni yumaloqlaydi. `50%` kvadratni doiraga aylantiradi.

### 5. Odatiy xatolar
- `margin` va `padding` ni almashtirish.
- `border` da tur (`solid`) yozilmasa chiziq chizilmaydi.
- `margin: 0 auto` faqat `width` berilgan blokda ishlaydi.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Box model | Elementning quti modeli |
| Content | Mazmun: matn, rasm |
| Padding | Ichki masofa |
| Border | Chegara |
| Margin | Tashqi masofa |
| width / height | Element eni va bo'yi |
| box-sizing | O'lchamni hisoblash usuli |
| border-box | width padding va border ni o'z ichiga oladi |
| border-radius | Burchakni yumaloqlash |
| DevTools | Brauzerdagi tekshirish asboblari (F12) |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Barcha brauzerlarning asboblar oynasida (F12) Box model ning rangli rasmi ko'rinadi: undan kerakli masofani darhol topish mumkin.
- Ko'plab loyihalar `box-sizing: border-box` ni birinchi qatorda yozadi, shu sababli hisoblash osonlashadi.
- `margin` salbiy ham bo'lishi mumkin: element qo'shnisi tomon siljiydi.
- Yumaloq ilova ikonkalari ko'pincha `border-radius: 50%` kabi qiymat bilan yasaladi.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. DevTools da quti <Badge type="tip" text="oson" />
Sahifadagi istalgan `div` ga `padding`, `border`, `margin` bering va F12 da Box model rasmini toping.
**Kutiladigan natija:** to'rt qatlam rangli ko'rinadi.

### 2. Ichki masofa <Badge type="tip" text="oson" />
Matnli `div` ga fon rangi bering, `padding` ni 0, 10px, 30px qilib o'zgartiring.
**Kutiladigan natija:** fon rangi matn atrofida kengayadi.

### 3. Chegara turlari <Badge type="tip" text="oson" />
Beshta `div` ga `solid`, `dashed`, `dotted`, `double`, `none` chegaralarini bering.
**Kutiladigan natija:** har xil chegara uslubi ko'rinadi.

### 4. Tashqi masofa <Badge type="tip" text="oson" />
Ikkita `div` orasida 40px masofa hosil qiling.
**Kutiladigan natija:** bloklar orasi ochilgan.

### 5. Jami o'lchamni hisoblang <Badge type="warning" text="o'rta" />
`width: 250px; padding: 15px; border: 5px solid;` (content-box). Ko'rinadigan kenglik nechi piksel? Brauzerda tekshiring.
**Kutiladigan natija:** 250 + 30 + 10 = 290px.

### 6. Box-sizing farqi <Badge type="warning" text="o'rta" />
Yuqoridagi qutini `box-sizing: border-box` bilan qayta tekshiring.
**Kutiladigan natija:** endi aniq 250px.

### 7. Qisqa yozuvni oching <Badge type="warning" text="o'rta" />
`margin: 10px 20px 30px 40px;` ni to'rt alohida xususiyat bilan yozing.
**Kutiladigan natija:** `margin-top`, `margin-right`, `margin-bottom`, `margin-left`.

### 8. Bu kod nima chiqaradi? <Badge type="warning" text="o'rta" />
```css
.a { width: 200px; margin: 0 auto; }
```
Blok sahifada qayerda turadi? `width` ni olib tashlasa-chi?
**Kutiladigan natija:** width bilan markazda; widthsiz butun kenglikni egallaydi, markazlash seziladi.

### 9. Karta yasash <Badge type="danger" text="qiyin" />
Kengligi 300px, padding 20px, yumaloq burchak, chegara va fonli «yangilik kartasi» yasang. Yonma-yon 2 ta karta orasida masofa bo'lsin.
**Kutiladigan natija:** tartibli karta.

### 10. Maket xatosi <Badge type="danger" text="qiyin" />
Dizayner blok eni 300px bo'lsin degan, lekin brauzerda F12 da 344px chiqdi (`padding: 20px; border: 2px`). Sababi va yechimini yozing.
**Kutiladigan natija:** sabab content-box (width faqat content); yechim `box-sizing: border-box`.

### 11. Vizitka kartasi <Badge type="danger" text="qiyin" />
Rasm, ism va kasbdan iborat vizitka kartasini box model xususiyatlari bilan chiroyli qiling.
**Kutiladigan natija:** markazlashgan, yumaloq burchakli karta.

### 12. Doira avatar <Badge type="info" text="bonus" />
`border-radius: 50%` yordamida kvadrat rasmni doira avatarga aylantiring.
**Kutiladigan natija:** doira shaklidagi rasm.

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Box model ning to'rt qismini ichkaridan tashqariga ayting.
2. Padding va margin qanday farqlanadi?
3. `padding: 5px 10px 15px 20px` tomonlarni qanday taqsimlaydi?
4. `border: 2px solid red` qismlari nima?
5. `width: 300px; padding: 20px; border: 2px` qutining jami kengligi qancha?
6. `box-sizing: border-box` nima beradi?
7. `margin: 0 auto` qachon ishlaydi?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Uchta karta (`.karta`) li sahifa yasang: har birida sarlavha, matn, `padding`, `border`, `margin` va `box-sizing: border-box`. 20–30 daqiqa.

</div>

