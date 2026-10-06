# 14-dars. UI dizayn: tugmalar, menyular, HUD (1-qism): Tugmalar turlari, holatlari (Normal, Hover, Pressed)

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga UI dizayn tushunchasini va uning o'yindagi rolini, UI-dizaynerning asosiy vazifalarini, asosiy UI elementlarini (tugma, menyu, HUD) tanishtirish; tugmalar turlari (Primary, Secondary, interaktiv) va tugma dizayniga qo'yiladigan talablarni o'rgatish; Photoshop'da tugmaning Normal, Hover va Pressed holatlarini alohida qatlamlarda yaratishni amalda bajarish.
- **Kutiladigan natija:** O'quvchilar UI dizaynning o'yindagi 5 ta vazifasini ayta oladi; Primary va Secondary tugmani farqlaydi; Photoshop'da Rectangle Tool, Corners, Stroke, Layer Styles (gradient, shadow, glow) bilan «START» tugmasini chizadi va uning 3 ta holatini alohida qatlamlarda tayyorlab, shaffof PNG qilib eksport qiladi.
- **Vaqt taqsimoti:**
  - Takrorlash (sprayt sheet, atlas): 10 daqiqa
  - Yangi mavzu: UI dizayn, UI-dizayner vazifalari, UI elementlari: 15 daqiqa
  - Tugmalar turlari va dizayn talablari: 10 daqiqa
  - Amaliyot: Photoshop'da tugma chizish (uslubiy ko'rsatma bo'yicha): 20 daqiqa
  - Amaliyot: Normal, Hover, Pressed holatlari va eksport: 20 daqiqa
  - Xulosa: 5 daqiqa

> Manba: o'quv dasturi — «UI dizayn: tugmalar, menyular, HUD» moduli («UI dizayn tushunchasi va o'yinlardagi roli. Foydalanuvchi tajribasiga (UX) ta'siri. O'yinlarda UI-dizaynerning asosiy vazifalari. Tugmalar turlari va dizayni uchun talablar»); o'quv qo'llanma — 2.4-bo'lim (ta'rif, vazifalar, tugmalar turlari, talablar, Photoshop'da UI yaratish bosqichlari: «Tugmalar uchun hover va pressed holatlar alohida layerlarda yaratiladi»); uslubiy ko'rsatma — 1.4-mashg'ulot (1920×1080 hujjat, Rectangle Tool, Corners 30 px, Stroke, Text Tool «START»). Menyular — 15-dars, HUD — keyingi darslar.

---

## Mentor konspekti

### 1. UI dizayn nima?

O'quv qo'llanma ta'rifi: **UI-dizayn** (foydalanuvchi interfeysi dizayni) — tugmalar, menyular, belgilar va o'yinchi o'zaro ta'sir qiladigan boshqa elementlarni o'z ichiga olgan o'yinning vizual va interaktiv qismini yaratish jarayoni. Vazifasi — o'yinni boshqarishni **tushunarli, qulay va estetik jozibali** qilish.

Interfeys orqali o'yinchi:
- personaj holati (sog'lik, energiya, inventar) haqida ma'lumot oladi;
- o'yin jarayonini boshqaradi (menyu, pauza, qurol tanlash, sozlamalar);
- o'yin dunyosi bilan aloqada bo'ladi (xarita, kvestlar, dialoglar).

UX bilan bog'liqlik: yaxshi UI o'yinchi tajribasini (UX) yaxshilaydi — «sifatli dizayn o'yin taassurotini yaxshilaydi, yomon dizayn esa o'yinchini chalg'itadi va tushkunlikka olib keladi».

### 2. UI-dizaynerning asosiy vazifalari (qo'llanma bo'yicha)

1. **Axborotni vizual uzatish** — grafika, animatsiya, tovush orqali tushunarli format.
2. **Soddalik va aniqlik** — chalg'ituvchi omillarni kamaytirish.
3. **Muvofiq uyg'unlik** — interfeys o'yin uslubiga mos, muhitni to'ldiradi.
4. **Funksional imkoniyatlar** — qulay boshqaruv vositalari.
5. **Estetika va uslub** — ranglar, shriftlar, illyustratsiyalar ko'zga yoqimli va tanib olinadigan.

### 3. Asosiy UI elementlari

- **Tugmalar (Buttons)** — buyruq berish, tanlov, amal bajarish.
- **Menyular (Menus)** — imkoniyatlar orasida tanlov tuzilmasi.
- **HUD (Head-Up Display)** — o'yin davomida doim ko'rinadigan ma'lumot (nomi aviatsiyadan: uchuvchining old oynasiga tushirilgan ma'lumot).
- Shuningdek: ikonlar, indikatorlar, progress barlar, bildirishnomalar.

### 4. Tugmalar turlari

| Tur | Vazifasi | Misol |
|---|---|---|
| **Asosiy (Primary)** | o'yin boshlash, davom ettirish, tasdiqlash | Start, OK, Davom etish |
| **Ikkinchi darajali (Secondary)** | bekor qilish, ortga qaytish | Cancel, Back, Ortga |
| **Interaktiv** | hover, bosish (pressed), yoritish yoki animatsiya effektlari bilan | har qanday «jonli» tugma |

Primary tugma ko'zga birinchi tashlanadi (yorqin rang, kattaroq); Secondary — sokinroq (kulrang, kontur, kichikroq).

### 5. Tugma dizayni uchun talablar (qo'llanma)

- **O'lcham va joylashuv qulay** bo'lishi kerak (telefonda barmoq bilan bosish oson).
- **Rang va shakl** boshqa elementlardan ajralib tursin.
- **Holatlar (normal, hover, bosilgan) aniq farqlansin.**
- Misol: «Start Game» tugmasi odatda **markazda** va e'tiborni tortuvchi rangda (yashil yoki ko'k).

### 6. Tugma holatlari

| Holat | Qachon | Vizual farq (namuna) |
|---|---|---|
| **Normal** | tugma tinch turibdi | asosiy rang, yengil soya |
| **Hover** | kursor ustiga keldi (yoki geympadda tanlangan) | ochroq rang yoki Outer Glow, biroz kattaroq |
| **Pressed** | bosilgan payt | to'qroq rang, soya yo'q yoki ichki soya, 2–4 px pastga siljigan |

Qo'llanmada rangning ham o'rni aytilgan: *«UI elementlarda rang orqali interaktivlikni ko'rsatish (masalan, hover holatida tugma rangi o'zgaradi)»*. Ba'zi o'yinlarda to'rtinchi holat — **Disabled** (bosib bo'lmaydi, kulrang) ham bo'ladi.

### 7. Photoshop'da tugma (uslubiy ko'rsatma, 1.4-mashg'ulot)

1. File → New (`Ctrl + N`): **1920×1080 px**, 72 ppi, RGB, nomi «O'yin menyusi».
2. **Rectangle Tool (U)** bilan to'rtburchak (masalan, 400×100 px).
3. Layers panelida shaklga ikki marta bosib, **Color Picker** bilan rang.
4. **Move Tool (V)** bilan markazga.
5. Properties → **Corners: 30 px** — burchaklar yumaloq.
6. Properties → **Stroke**: rang va qalinlik (masalan, 4 px).
7. **Text Tool (T)**: «START», Properties → Character: shrift, o'lcham, rang; matn markazga.
8. Qo'llanma bo'yicha **Layer Styles**: gradient, Drop Shadow, Inner Glow, Outer Glow, Bevel & Emboss.

### 8. Holatlarni qatlamlarda tayyorlash

```
Layers:
  btn_start (Group)
    btn_start_normal   (shakl + matn + Drop Shadow)
    btn_start_hover    (nusxa: ochroq rang + Outer Glow)
    btn_start_pressed  (nusxa: to'qroq rang, soya o'chiq, 3 px pastga)
```

- Normal guruhni `Ctrl + J` bilan nusxalang, nomini o'zgartiring, faqat farqlarini tahrirlang.
- Har holatni alohida eksport: boshqalarini yashirib (ko'z belgisi), **File → Export → Export As → PNG** (Transparency). Fon qatlamini yashirish yoki o'chirish shart.
- Nomlash: `btn_start_normal.png`, `btn_start_hover.png`, `btn_start_pressed.png`.
- Barcha holatlar **bir xil o'lchamdagi** kanvasda — dvijokda almashtirilganda tugma «sakramaydi».
- Bonus: 13-darsdagi atlas g'oyasi — 3 holatni bitta sheetga (3 qator) yig'ish mumkin.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Primary yoki Secondary? (oson)
Quyidagi tugmalarni turlarga ajrating: Start, Back, OK, Cancel, Davom etish, Bekor qilish.

**Yechim:**
Primary: Start, OK, Davom etish. Secondary: Back, Cancel, Bekor qilish. Sabab: primary — asosiy maqsadli harakat (boshlash, tasdiqlash), secondary — chekinish yoki rad etish.

### 2-topshiriq. START tugmasi (oson)
Uslubiy ko'rsatma bo'yicha 1920×1080 hujjatda yumaloq burchakli (30 px), stroke'li «START» tugmasini chizing.

**Yechim:**
Ctrl + N (1920×1080, 72 ppi, RGB) → Rectangle Tool (U), ~400×100 → Color Picker (masalan, yashil) → Properties: Corners 30 px, Stroke 4 px to'q yashil → Text Tool (T) «START», oq, qalin shrift, ~48 pt → Move Tool bilan markaz. Tekshirish: matn tugma ichida markazda, chetlari tekis.

### 3-topshiriq. Uch holat (o'rta)
2-topshiriqdagi tugmaning Normal, Hover va Pressed holatlarini alohida qatlamlarda yarating.

**Yechim:**
1. Shakl va matnni `btn_start_normal` guruhiga (`Ctrl + G`), Drop Shadow (Distance 6 px).
2. `Ctrl + J` → `btn_start_hover`: Color Overlay yoki Fill ochroq yashil, Outer Glow (Size 15 px).
3. `Ctrl + J` → `btn_start_pressed`: to'qroq yashil, Drop Shadow o'chiq (yoki Inner Shadow), guruh 3 px pastga.
4. Tekshirish: ko'z belgisini navbat bilan yoqib-o'chirganda farq aniq ko'rinadi, tugma chegarasi joyidan siljimaydi (pressed'dagi 3 px dan tashqari).

### 4-topshiriq. Tugmalar to'plami va eksport (qiyin)
Primary («START») va Secondary («ORTGA») tugmalarni bir uslubda yarating, har biri uchun 3 holat, barchasini shaffof PNG qilib nomlab eksport qiling.

**Yechim:**
- Secondary: kulrang yoki kontur (Fill 0%, Stroke 4 px), kichikroq (320×80), matn «ORTGA».
- Holatlar: Primary bilan bir xil mantiq (hover — ochroq/glow, pressed — to'qroq/pastga).
- Eksport: fonni yashirish → har holat uchun boshqalarini yashirib Export As → PNG. 6 ta fayl: `btn_start_normal.png`... `btn_ortga_pressed.png`.
- Tekshirish: barcha PNG'lar shaffof, bir holatdagi fayllar bir xil o'lchamda.

---

## Tezkor nazorat savollari

1. UI dizayn nima?
   - *Javob:* O'yinchi o'zaro ta'sir qiladigan tugma, menyu, belgi kabi elementlarni o'z ichiga olgan vizual va interaktiv qismni yaratish jarayoni.
2. Primary va Secondary tugma farqi?
   - *Javob:* Primary — asosiy harakat (Start, OK), Secondary — bekor qilish, ortga (Cancel, Back).
3. Tugmaning uchta holati?
   - *Javob:* Normal, Hover, Pressed.
4. HUD nomi qayerdan kelib chiqqan?
   - *Javob:* Aviatsiyadan: muhim ma'lumot uchuvchining old oynasiga tushirilgan.
5. Photoshop'da tugma holatlari qanday tayyorlanadi?
   - *Javob:* Alohida qatlamlarda (layerlarda), har biri alohida PNG qilib eksport qilinadi.

---

## Keng tarqalgan xatolar va ularning oldini olish

- **Holatlar deyarli bir xil:** o'yinchi bosilganini sezmaydi — rang, soya va siljish farqini aniq qiling.
- **Matn tugmadan chiqib ketadi:** Font Size'ni kamaytiring, matnni markazlang.
- **Secondary tugma Primary'dan yorqinroq:** o'yinchi adashadi — ierarxiyani saqlang.
- **Oq fon bilan eksport:** Background qatlamini yashiring, PNG Transparency.
- **Holatlar har xil o'lchamda:** dvijokda tugma sakraydi — bir xil kanvas.
- **Juda ko'p effekt:** Bevel + Glow + Gradient + Pattern birdaniga — tugma «og'ir»; 2–3 effekt yetarli.
