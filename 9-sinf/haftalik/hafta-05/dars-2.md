# 14-dars. Mashhur UI kitlar: HIG, Ant Design, Bootstrap, Figma UI Kit, Material UI

**Hafta:** 5 · **Davomiyligi:** 80 daqiqa · **Turi:** ma'ruza + tahliliy amaliyot (Figma Community) · **I-bob**, 1.5-mavzu, 2-dars

**Manba:** o'quv qo'llanma, 1.5 «UI kit va dizayn tizimlariga kirish» (eng mashhur UI kitlar: Human Interface Kit (HIG) — 1977-yil Apple II, bo'limlari Platforms, Foundations, Patterns, Components, Inputs, Technologies; Ant Design — React.js asosida, korporativ veb-ilovalar, 5 guruh komponentlar; Bootstrap UI Kit — HTML/CSS/JS, Twitter dasturchilari, responsiv dizayn, 5 guruh komponentlar; Figma UI Kit — komponentlar va shablonlar, interaktiv prototiplash; Material UI — Google Material Design, React, `npm install @mui/material`, props `variant`, `color`, `size`, `disabled`, `sx`; xulosa: UI kitlar funksionallik, platformaga moslik, komponentlar soni va moslashuvchanlik bilan farqlanadi; nazorat savollari). Figma Community'dan kit ochish qadamlari — amaliyot uchun qo'shimcha (Figma rasmiy funksiyalari asosida).

## 1. Dars rejasi

**Maqsad:** o'quvchilar 5 ta mashhur UI kit (Apple HIG, Ant Design, Bootstrap, Figma UI Kit, Material UI) ning kim tomonidan, qaysi texnologiya va platforma uchun yaratilganini, ularning asosiy komponent guruhlarini o'rganadi; ularni taqqoslab, loyiha uchun mos kitni tanlashni o'rganadi va Figma Community'dagi tayyor kitni tahlil qiladi.

**Kutiladigan natija:**
- 5 ta mashhur UI kitni nomlaydi va har birining yaratuvchisi/asosini aytadi;
- HIG'ning 6 ta asosiy bo'limini sanaydi;
- Ant Design, Bootstrap va Figma UI Kit komponent guruhlarini misollar bilan ajratadi;
- Material UI tugmasining `variant`, `color`, `size`, `disabled` xususiyatlarini tushuntiradi;
- Loyiha turiga qarab (iOS ilova, korporativ panel, responsiv sayt, prototip) mos UI kitni tanlaydi va asoslaydi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va kirish | UI Kit vs dizayn tizimi, 5 qism, tokenlar. Savol: «iPhone va Android ilovalari nega har xil ko'rinadi?» |
| 10–35 daq | Yangi mavzu | HIG, Ant Design, Bootstrap, Figma UI Kit, Material UI; taqqoslash jadvali |
| 35–40 daq | Tanaffus | Harakatli tanaffus |
| 40–70 daq | Amaliy mashg'ulot | Figma Community'dan 2 ta UI kitni ochish, tugma va inputlarini taqqoslash, «E-kutubxona» uchun kit tanlash |
| 70–76 daq | Tezkor nazorat | 5 ta savol |
| 76–80 daq | Xulosa va uyga vazifa | Keyingi dars: UI kit amaliyoti — «E-kutubxona» header va kategoriya paneli |

---

## 2. Dars konspekti

### 2.1. Kirish: nega har xil kitlar bor?
UI kitlar bir-biridan **funksionalligi, platformaga mosligi, komponentlar soni va moslashuvchanligi** bilan farqlanadi (qo'llanma xulosasi). iOS ilovasi Apple qoidalariga, korporativ admin-panel jadval va formalarga boy kitga, oddiy responsiv sayt esa tez yig'iladigan kitga muhtoj.

### 2.2. Human Interface Guidelines (HIG) — Apple
- **Apple** kompaniyasi ishlab chiqqan dizayn qo'llanmasi: iOS, macOS, watchOS, tvOS va visionOS ilovalari uchun eng yaxshi amaliyotlar va tamoyillar.
- Maqsad: UI dizaynini standartlashtirish, izchillikni saqlash, foydalanuvchi tajribasini yaxshilash.
- Tarix: dastlab **1977-yilda Apple II** uchun yaratilgan, bugun butun Apple ekotizimini qamrab oladi.

| Bo'lim | Mazmuni |
|---|---|
| **Platforms** | iOS, macOS, watchOS, tvOS, visionOS uchun tavsiyalar |
| **Foundations** | rang, shrift, layout, kompozitsiya, accessibility |
| **Patterns** | share actions, multitasking, search, feedback naqshlari |
| **Components** | menyular, navigatsiya, tugmalar, kartalar, form elementlari |
| **Inputs** | touch, keyboard, gestures, remote, eye gaze (visionOS) |
| **Technologies** | Apple Pay, iCloud, Maps, Game Center, HomeKit |

Apple dizaynerlar uchun Figma/Sketch formatidagi rasmiy **Apple Design Resources** (iOS UI kit) ni ham taqdim etadi.

### 2.3. Ant Design (AntD)
- **React.js** asosidagi professional UI komponentlar to'plami; **korporativ veb-ilovalar** (admin-panel, CRM, hisobotlar) uchun.
- Maqsad: interfeysni standartlashtirish va ishlab chiqishni tezlashtirish.

| Guruh | Komponentlar |
|---|---|
| Navigatsiya | menu, breadcrumb, tabs |
| Forma | input, checkbox, radio, select, datepicker |
| Vizual | button, icon, tooltip, avatar, badge, tag |
| Ma'lumotlar | table, list, card, collapse, pagination |
| Grafik | chart, progress, skeleton |

### 2.4. Bootstrap UI Kit
- **HTML, CSS va JavaScript** asosidagi eng mashhur komponentlar kutubxonasi; **Twitter** dasturchilari yaratgan.
- Asosiy afzalligi — **responsiv dizayn**: turli ekran o'lchamlariga moslashuvchan sahifalarni tez yaratish.

| Guruh | Komponentlar |
|---|---|
| Navigatsiya va tartib | navbar, breadcrumb, tabs, pagination |
| Forma | input, textarea, checkbox, radio, select, form validation |
| Vizual | button, badge, alert, card, modal, tooltip |
| Layout va grid | container, row, col, flexbox |
| JavaScript | carousel, collapse, dropdown, popover, scrollspy |

### 2.5. Figma UI Kit
- **Figma** muhiti uchun tayyor komponentlar va shablonlar; interaktiv prototiplash va vizual dizaynda qo'llaniladi.
- Dizayn jarayonini tezlashtiradi, yagona uslub va jamoaviy ishlashni ta'minlaydi.

| Guruh | Elementlar |
|---|---|
| Navigatsiya | menu, tabs, sidebars |
| Forma | input, checkbox, radio, dropdown, slider |
| Vizual | button, icon, modal, tooltip, avatar, badge |
| Shablonlar va ramkalar | ekran tartiblari, wireframe shablonlari, prototip sahifalari |
| Interaktiv | hover, klik, drag & drop effektlari |

Figma'da tayyor kitlar **Community** bo'limida: qidiruv → «UI kit» → **Open in Figma** — fayl nusxasi «Drafts» ga tushadi.

### 2.6. Material UI (MUI)
- **Google Material Design** konsepsiyasiga asoslangan, **React** komponentlari kutubxonasi; tayyor, moslashtiriladigan, yagona uslubdagi komponentlar.
- O'rnatish (react va react-dom ham kerak):
```
npm install @mui/material
yarn add @mui/material
```
- Har bir komponent **props** (xususiyatlar) orqali sozlanadi — ular rasmiy hujjatning **Component API** bo'limida yozilgan:
```jsx
<Button variant="text">Button</Button>
<Button variant="contained" size="large">Button</Button>
<Button variant="outlined" disabled>Button</Button>
```
- `variant` — ko'rinish (text, contained, outlined); `color` — rang; `size` — o'lcham (small, medium, large); `disabled` — faol emas.
- `sx` — barcha komponentlardagi maxsus xususiyat: qo'shimcha CSS uslublari uchun:
```jsx
<Button variant="contained" sx={{ backgroundColor: 'purple', width: 200, color: 'white' }}>Button</Button>
```

### 2.7. Taqqoslash va tanlash
| Kit | Kim | Asos | Eng mos holat |
|---|---|---|---|
| HIG | Apple | qo'llanma + rasmiy kitlar | iOS/macOS ilova |
| Ant Design | Ant Group (Alibaba) | React | korporativ panel, jadval/formalar |
| Bootstrap | Twitter dasturchilari | HTML/CSS/JS | tez responsiv sayt |
| Figma UI Kit | Figma hamjamiyati | Figma komponentlari | prototip, dizayn bosqichi |
| Material UI | Google Material Design | React | Android uslubidagi veb/ilova |

Qoida: avval **platforma** (iOS, Android, veb), keyin **loyiha turi** (korporativ, sayt, prototip), so'ng **jamoa texnologiyasi** (React, oddiy HTML).

---

## 3. Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Kitni toping (oson)
Qaysi kit: (a) 1977-yil Apple II uchun boshlangan; (b) Twitter dasturchilari yaratgan; (c) `npm install @mui/material`; (d) korporativ panellar uchun React kutubxonasi.

**Yechim:** (a) HIG; (b) Bootstrap; (c) Material UI; (d) Ant Design.

### 2-topshiriq. Loyihaga kit tanlang (o'rta)
4 ta buyurtma: (1) maktab uchun iPhone ilovasi; (2) bank xodimlari uchun jadvalli admin-panel; (3) o'quv markazining 1 kunda tayyor bo'lishi kerak bo'lgan responsiv sayti; (4) investorga ko'rsatiladigan klikli prototip. Har biriga kit tanlang va bir jumlada asoslang.

**Yechim:** (1) HIG — Apple qoidalari va komponentlari; (2) Ant Design — table, pagination, datepicker tayyor; (3) Bootstrap — grid va navbar bilan tez responsiv; (4) Figma UI Kit — hover/klik interaktivligi bilan prototip.

### 3-topshiriq. Figma Community tahlili (qiyin)
Figma → **Community** → «Material 3 Design Kit» va «iOS UI Kit» (yoki «Ant Design») fayllarini oching. Har biridan **Button** va **Text field / Input** komponentini toping, yangi `Tahlil` frame'iga nusxalang va jadval tuzing: burchak radiusi, balandlik, asosiy rang, holatlar soni (default/hover/pressed/disabled), shrift.

**Yechim (tekshiruv):** frame'da 2 kitdan 4 ta komponent; jadvalda 5 mezon bo'yicha farqlar (masalan, Material tugmasi to'liq yumaloq «pill» shakl, iOS tugmasi tizim shrifti SF Pro); xulosa: «E-kutubxona» uchun qaysi kit uslubi mos va nega.

---

## 4. Tezkor nazorat (savollar va javoblar)

1. **HIG qaysi kompaniyaniki va qachon boshlangan?**
   - *Javob:* Apple, 1977-yil Apple II uchun.
2. **HIG'ning asosiy bo'limlari?**
   - *Javob:* Platforms, Foundations, Patterns, Components, Inputs, Technologies.
3. **Ant Design qaysi texnologiyaga asoslangan va qayerda qo'llaniladi?**
   - *Javob:* React.js; korporativ veb-ilovalarda.
4. **Bootstrap UI Kit'ning asosiy afzalligi?**
   - *Javob:* HTML/CSS/JS asosida tez responsiv dizayn yaratish.
5. **Material UI qaysi dizayn tamoyiliga asoslanadi?**
   - *Javob:* Google'ning Material Design konsepsiyasiga.

---

## 5. Uyga vazifa

1. Figma Community'dan bitta UI kitni (Material 3, iOS, Ant Design yoki Bootstrap) oching.
2. Undan 5 ta komponentni (button, input, checkbox, card, navbar/tabs) «E-kutubxona» faylingizga nusxalang va 13-darsdagi stillaringiz bilan qayta bo'yang.
3. «Bu kit menga nimasi bilan yoqdi / yoqmadi» — 3–4 jumlali izoh yozing.
