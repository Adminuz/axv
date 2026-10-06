# 15-dars. UI kit amaliyoti: «E-kutubxona» header va kategoriya paneli

**Hafta:** 5 · **Davomiyligi:** 80 daqiqa · **Turi:** dizayn amaliyoti (Figma) · **I-bob**, 1.5-mavzu, 3-dars

**Manba:** uslubiy ko'rsatma, 1.4 «UI kit va dizayn tizimlariga kirish» — amaliy qism (1.29–1.42-rasmlar: header'da qidiruv maydoni Rectangle, W/H va x/y, Fill #FFFFFF, Corner radius 25; 50 × 50 qidiruv tugmasi, sariq #FFFB00, opacity ≈ 47%, radius 25; Fill → Image orqali lupa ikonka va Crop; «Kirish» matni Inter 25 px; profil ikonka 38 × 38, Exposure; savat ikonka; Shape tools → Line, stroke #000000, 2 px, center; yon panel Rectangle — Drop shadow, Opacity 100%, Fill #FFFFFF, Stroke #000000 1 px Inside; kategoriya ajratuvchi chiziqlari; red guides orqali masofalarni tekshirish; «more categories» havolasi; kategoriya nomlari, masalan «Maktab darsliklari»; amaliy topshiriq: sahifaga tugmalar va qo'shimcha elementlar joylashtirib, yagona uslubni ta'minlash). Komponentga aylantirish (Create component) — 13-darsdagi atom/molekula g'oyasini mustahkamlash uchun qo'shimcha.

## 1. Dars rejasi

**Maqsad:** o'quvchilar 13–14-darslarda o'rganilgan UI kit g'oyasini amalda qo'llab, Figma'da «E-kutubxona» sahifasining header qismini (qidiruv maydoni, qidiruv tugmasi, «Kirish», profil va savat ikonkalari) va yon tomondagi «Kategoriya» panelini aniq o'lcham, rang, radius, stroke va soya parametrlari bilan yaratadi; elementlarni yagona uslubga keltiradi va qayta ishlatiladigan komponentga aylantiradi.

**Kutiladigan natija:**
- Rectangle o'lchami (W/H), joylashuvi (x/y), Fill va Corner radius'ini Design panelida aniq sozlaydi;
- Fill → Image orqali ikonka yuklaydi va Crop bilan moslaydi; Exposure bilan ikonka ko'rinishini fonga moslaydi;
- Line elementiga stroke (rang, qalinlik, joylashuv) beradi va bo'limlarni ajratadi;
- Drop shadow va Inside stroke bilan yon panel yaratadi, red guides bilan masofalarni tekshiradi;
- Header va kategoriya panelini yagona uslubda yig'ib, qidiruv maydonini komponentga aylantiradi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va kirish | Mashhur UI kitlar, atom → molekula → organizm. Namuna: tayyor «E-kutubxona» header'i |
| 10–20 daq | Ko'rsatish | Design paneli: W/H, x/y, Fill, Corner radius, Effects, Stroke |
| 20–35 daq | Amaliyot 1 | Header: qidiruv maydoni, sariq qidiruv tugmasi, lupa ikonka, «Kirish», profil va savat |
| 35–40 daq | Tanaffus | Harakatli tanaffus |
| 40–68 daq | Amaliyot 2 | Kategoriya paneli: soya, stroke, ajratuvchi chiziqlar, nomlar, «more categories», red guides |
| 68–75 daq | Tezkor nazorat | 5 ta savol, juftlikda bir-birining ishini tekshirish |
| 75–80 daq | Xulosa va uyga vazifa | Keyingi hafta: Figma'da komponentlar va prototiplash |

---

## 2. Dars konspekti

### 2.1. Sahifa tuzilmasi
«E-kutubxona» bosh sahifasi uchun Desktop frame (1440 × 1024) olinadi. Bugun 2 ta organizm yig'iladi:
- **Header** — yuqori panel: logotip, markazda qidiruv maydoni + qidiruv tugmasi, o'ngda «Kirish», profil va savat ikonkalari.
- **Kategoriya paneli** — chap tomonda: sarlavha, kategoriyalar ro'yxati, ajratuvchi chiziqlar, «more categories» havolasi.

### 2.2. Qidiruv maydoni (1.29–1.30-rasmlar)
1. **Rectangle (R)** bilan header markazida to'rtburchak chiziladi.
2. Design panelida **W** (eni) va **H** (bo'yi), **X** va **Y** koordinatalari aniq kiritiladi (masalan, W 600, H 50).
3. **Fill** → rang oynasi → **#FFFFFF** (oq) — toza va neytral ko'rinish.
4. **Corner radius = 25** — balandlikning yarmi, shuning uchun maydon to'liq yumaloq («pill») bo'ladi.

### 2.3. Qidiruv tugmasi va ikonka (1.31–1.33-rasmlar)
1. Maydonning o'ng tomoniga **50 × 50** Rectangle.
2. Fill: sariq **#FFFB00**, **opacity ≈ 47%**; **Corner radius = 25** — dumaloq tugma.
3. Lupa ikonka: yangi kichik Rectangle → **Fill → Image** → kompyuterdan rasm → **Crop** bilan o'lcham va joylashuvni moslash.

### 2.4. «Kirish», profil va savat (1.34–1.36-rasmlar)
- **Text (T)** → «Kirish»: shrift **Inter**, o'lcham **25 px** — tizimga kirish funksiyasi.
- Profil ikonka: Image sifatida yuklanadi, o'lchami **38 × 38 px**; Image sozlamalarida **Exposure** (yorug'lik) bilan fonga moslanadi.
- Savat (cart) ikonka ham xuddi shunday: Image + Exposure.

### 2.5. Chiziq bilan ajratish (1.37–1.38-rasmlar)
- Pastki asboblar panelidagi **Shape tools**: Rectangle, Line, Arrow, Ellipse, Polygon, Star → **Line (L)**.
- **Stroke:** rang **#000000**, qalinlik **2 px**, joylashuv **Center** — header va kontentni ajratadi.

### 2.6. Kategoriya paneli (1.39–1.42-rasmlar)
1. Chap tomonda vertikal Rectangle: **Opacity 100%**, **Fill #FFFFFF**, **Stroke #000000, 1 px, Inside**.
2. **Effects → Drop shadow** — panel fondan ajralib, chuqurlik (depth) hissi paydo bo'ladi.
3. Ichida bir nechta gorizontal **Line** — har bir kategoriya bandini ajratadi.
4. **Red guides:** element tanlangan holda **Alt (Option)** bosib turib boshqa elementga sichqonchani olib borilsa, qizil o'lchov chiziqlari masofani ko'rsatadi — oraliqlar teng ekanini tekshiring (8-point grid: 16 yoki 24).
5. Pastda **«more categories»** matni — qo'shimcha kategoriyalar sahifasiga havola.
6. Kategoriya nomlari: «Maktab darsliklari», «Badiiy adabiyot», «Ilmiy-ommabop», «Bolalar adabiyoti», «Chet tillar».

### 2.7. Stroke joylashuvi
| Joylashuv | Natija |
|---|---|
| **Inside** | chiziq shakl ichida — o'lcham o'zgarmaydi (panel uchun qulay) |
| **Center** | yarmi ichda, yarmi tashqarida |
| **Outside** | chiziq tashqarida — element vizual kattalashadi |

### 2.8. Yagona uslub va komponent
- Hamma joyda 13-darsdagi **Color va Text styles** ishlatiladi (oq fon, sariq urg'u, qora chiziq, Inter).
- Qidiruv maydoni + tugma + lupa tanlanadi → **Ctrl/Cmd + Alt/Option + K** (Create component) → nom `Search/Default`. Endi uni boshqa sahifalarda nusxa (instance) sifatida ishlatish mumkin — bu UI kitning birinchi «molekulasi».

---

## 3. Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Qidiruv maydoni (oson)
600 × 50 oq Rectangle yarating, Corner radius 25 bering, o'ng tomoniga 50 × 50 sariq (#FFFB00, 47%) dumaloq tugma joylashtiring.

**Yechim (tekshiruv):** Design panelida W 600 / H 50, radius 25; tugma 50 × 50, Fill #FFFB00 47%, radius 25; tugma maydonning o'ng chetiga tekislangan (Align right).

### 2-topshiriq. To'liq header (o'rta)
Header'ga lupa ikonka (Fill → Image + Crop), «Kirish» (Inter 25 px), profil (38 × 38) va savat ikonkalarini qo'shing, pastdan 2 px qora Line bilan ajrating.

**Yechim (tekshiruv):** ikonkalar bir xil balandlikda va vertikal markazda; «Kirish» va ikonkalar orasidagi masofa red guides bo'yicha teng; Line stroke #000000 2 px Center; Exposure bilan ikonkalar fonda «yorqin dog'» bo'lib qolmagan.

### 3-topshiriq. Kategoriya paneli va komponent (qiyin)
Yon panelni (Fill #FFFFFF, Stroke #000000 1 px Inside, Drop shadow) yarating, 5 ta kategoriya va ajratuvchi chiziqlar, «more categories» havolasini qo'shing. Qidiruv blokini `Search/Default` komponentiga aylantiring va sahifaga yana 1 ta tugma (masalan, «Barcha kitoblar») yagona uslubda qo'shing.

**Yechim (tekshiruv):** Layers panelida panel guruh (Frame) nomi `Kategoriya`; 5 nom alohida qatorlarda, chiziqlar orasidagi masofa teng; Effects'da Drop shadow; Assets bo'limida `Search/Default` komponenti bor; yangi tugma ranglari va radiusi qidiruv tugmasi bilan uyg'un.

---

## 4. Tezkor nazorat (savollar va javoblar)

1. **Qidiruv maydoni nega Corner radius 25 bilan to'liq yumaloq bo'ladi?**
   - *Javob:* Balandligi 50 px, radius uning yarmi — burchaklar to'liq yarim doira bo'ladi.
2. **Rectangle ichiga rasm (ikonka) qanday joylanadi?**
   - *Javob:* Fill → Image → rasmni yuklash → Crop bilan moslash.
3. **Exposure nima uchun ishlatildi?**
   - *Javob:* Ikonka yorug'ligini sozlab, uni header foniga uyg'unlashtirish uchun.
4. **Stroke Inside va Outside farqi?**
   - *Javob:* Inside — chiziq shakl ichida, o'lcham o'zgarmaydi; Outside — tashqarida, element vizual kattalashadi.
5. **Red guides nima uchun kerak?**
   - *Javob:* Elementlar orasidagi masofani o'lchab, tartibli va simmetrik joylashuvni tekshirish uchun.

---

## 5. Uyga vazifa

1. «E-kutubxona» sahifasiga (header + kategoriya paneli) yana 3 ta element qo'shing: asosiy menyu (Bosh sahifa, Yangi kitoblar, Mualliflar, Aloqa), «Barcha kitoblar» tugmasi va banner joyi.
2. Barcha elementlar yagona uslubda bo'lsin: bir xil ranglar (stillar), Inter shrifti, radius va 8-point grid oraliqlari.
3. Qidiruv blokini va tugmani komponentga aylantiring; Figma havolasini (view huquqi bilan) mentorga yuboring.
