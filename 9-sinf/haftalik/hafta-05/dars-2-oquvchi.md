# 14-dars. Mashhur UI kitlar: HIG, Ant Design, Bootstrap, Figma UI Kit, Material UI

> iPhone ilovalari bir-biriga o'xshaydi, Google ilovalari ham — o'zaro. Sababi oddiy: ular bir xil UI kit va qoidalar asosida yaratilgan. Bugun dunyodagi 5 ta eng mashhur UI kit bilan tanishasiz va o'z loyihangiz uchun to'g'risini tanlashni o'rganasiz.

## Dars xulosasi

- **Human Interface Guidelines (HIG)** — **Apple** qo'llanmasi; iOS, macOS, watchOS, tvOS, visionOS uchun; **1977-yil Apple II** dan boshlangan.
- HIG bo'limlari: **Platforms, Foundations, Patterns, Components, Inputs, Technologies**.
- **Ant Design** — **React.js** asosida, **korporativ** veb-ilovalar uchun (jadval, forma, pagination).
- **Bootstrap UI Kit** — **HTML, CSS, JS** asosida, **Twitter** dasturchilari yaratgan; kuchi — **responsiv dizayn**.
- **Figma UI Kit** — Figma uchun tayyor komponent va shablonlar; prototiplashni tezlashtiradi.
- **Material UI (MUI)** — **Google Material Design** asosida, React komponentlari; `npm install @mui/material`.
- Kitlar **funksionallik, platformaga moslik, komponentlar soni va moslashuvchanlik** bilan farqlanadi.

## Qo'shimcha ma'lumot

### Kitni qanday tanlash kerak?
| Savol | Javob → kit |
|---|---|
| iPhone/Mac ilova? | HIG |
| Ko'p jadval va formali admin-panel? | Ant Design |
| Tez tayyor bo'ladigan responsiv sayt? | Bootstrap |
| Faqat dizayn va klikli prototip? | Figma UI Kit |
| Android uslubidagi React ilova? | Material UI |

### Material UI tugmasi
```jsx
<Button variant="text">Button</Button>
<Button variant="contained" size="large">Button</Button>
<Button variant="outlined" disabled>Button</Button>
```
- `variant` — ko'rinish: **text** (faqat matn), **contained** (to'ldirilgan), **outlined** (chegarali).
- `size` — small, medium, large; `disabled` — tugma faol emas; `sx` — qo'shimcha CSS.

### Figma Community'dan kit ochish
1. Figma'da chap paneldan **Community** (yoki qidiruvda «UI kit»).
2. Kerakli kitni tanlang → **Open in Figma**.
3. Fayl nusxasi **Drafts** ga tushadi — endi undan komponentlarni nusxalab olish mumkin.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| HIG | Human Interface Guidelines — Apple dizayn qo'llanmasi |
| Foundations | Asoslar — rang, shrift, layout, accessibility |
| Patterns | Naqshlar — search, feedback kabi tipik yechimlar |
| Ant Design | React asosidagi korporativ UI kutubxona |
| Bootstrap | HTML/CSS/JS asosidagi responsiv UI kutubxona |
| Material Design | Google'ning dizayn konsepsiyasi |
| MUI | Material UI — Material Design asosidagi React kutubxona |
| Props | Komponent xususiyatlari (variant, color, size) |
| Responsive | Turli ekran o'lchamiga moslashuvchan |
| Figma Community | Figma'dagi tayyor fayl va kitlar ombori |

## Bilasizmi?

- Bootstrap dastlab «Twitter Blueprint» deb atalgan va 2011-yilda ochiq kod sifatida e'lon qilingan.
- Ant Design Xitoyning Ant Group (Alibaba guruhi) jamoasi tomonidan yaratilgan.
- visionOS'da HIG «eye gaze» — ko'z qarashi bilan boshqarishni ham kirish usuli sifatida tavsiflaydi.

## Topshiriqlar

### 1. Juftlang · oson

5 ta kitni yaratuvchisi bilan juftlang: HIG, Ant Design, Bootstrap, Figma UI Kit, Material UI.

**Kutiladigan natija:** 5 ta to'g'ri juftlik.

### 2. HIG bo'limlari · oson

HIG'ning 6 bo'limini yozing va har biriga bittadan misol keltiring.

**Kutiladigan natija:** 6 qatorli ro'yxat.

### 3. Texnologiya · oson

Qaysi kitlar React, qaysisi HTML/CSS/JS asosida ishlaydi?

**Kutiladigan natija:** 2 guruhli ro'yxat.

### 4. Komponent guruhi · oson

`datepicker`, `scrollspy`, `skeleton`, `slider`, `breadcrumb` — har biri qaysi kitning qaysi guruhida keltirilgan?

**Kutiladigan natija:** 5 ta javob.

### 5. Loyihaga kit · o'rta

iOS ilova, bank admin-paneli, o'quv markazi sayti, investor prototipi uchun kit tanlang va asoslang.

**Kutiladigan natija:** 4 ta asoslangan tanlov.

### 6. MUI tugmalar · o'rta

`variant` ning 3 qiymati uchun tugma ko'rinishini qog'ozda chizing.

**Kutiladigan natija:** 3 ta eskiz.

### 7. Props · o'rta

Katta, chegarali, faol bo'lmagan MUI tugma kodini yozing.

**Kutiladigan natija:** `<Button variant="outlined" size="large" disabled>`.

### 8. Ant vs Bootstrap · o'rta

Ikkala kitdagi umumiy 5 ta komponentni toping.

**Kutiladigan natija:** masalan, tabs, breadcrumb, input, button, card.

### 9. Community · qiyin

Figma Community'dan bitta UI kitni oching va undagi tugmaning barcha holatlarini toping.

**Kutiladigan natija:** holatlar ro'yxati va skrinshot.

### 10. Taqqoslash · qiyin

2 ta kitning Button va Input komponentlarini 5 mezon bo'yicha taqqoslang.

**Kutiladigan natija:** jadval va xulosa.

### 11. sx xususiyati · qiyin

Binafsha fonli, oq matnli, eni 200 px bo'lgan MUI tugma kodini `sx` bilan yozing.

**Kutiladigan natija:** to'g'ri `sx={{...}}` obyekti.

### 12. Kit kolleksiyasi · bonus

Tanlangan kitdan 5 ta komponentni «E-kutubxona» stillari bilan qayta bo'yang.

**Kutiladigan natija:** yangilangan komponentlar frame'i.

## O'zingizni tekshiring

1. UI kitlar bir-biridan nimasi bilan farqlanadi?
2. HIG qaysi kompaniya tomonidan va qachon yaratilgan?
3. HIG'ning asosiy bo'limlarini sanang.
4. Ant Design qaysi texnologiya asosida va qayerda qo'llaniladi?
5. Bootstrap UI Kit'ning asosiy afzalligi nimada?
6. Figma UI Kit dizaynerlarga qanday imkoniyat beradi?
7. Material UI qaysi dizayn tamoyiliga asoslanadi va qanday o'rnatiladi?

## Uyga vazifa

Figma Community'dan bitta UI kitni oching, 5 ta komponentni «E-kutubxona» stillari bilan qayta bo'yang va qisqa izoh yozing (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
