# 13-dars. UI kit va dizayn tizimi tushunchasi

**Hafta:** 5 · **Davomiyligi:** 80 daqiqa · **Turi:** ma'ruza + dizayn amaliyoti (Figma) · **I-bob**, 1.5-mavzu, 1-dars

**Manba:** o'quv qo'llanma, 1.5 «UI kit va dizayn tizimlariga kirish» (UI Kit ta'rifi, asosiy maqsadi, 4 ta afzallik: vaqtni tejash, vizual uyg'unlik, moslashuvchanlik, jamoaviy ishlash; mashhur UI kitlar ro'yxati); uslubiy ko'rsatma, 1.4 «UI kit va dizayn tizimlariga kirish» (UI Kit — vizual «konstruktor», yagona uslub; dizayn tizimi — yagona konseptual tizim; 5 asosiy qism: komponentlar, vizual uslublar/tokenlar, shablonlar, prinsip va qo'llanmalar, hujjatlashtirish). Atom → molekula → organizm ierarxiyasi va Figma'dagi Color/Text styles — qo'llanma mazmunini tushuntirish uchun qo'shimcha (Figma rasmiy funksiyalari asosida).

## 1. Dars rejasi

**Maqsad:** o'quvchilar UI Kit va dizayn tizimi (Design System) tushunchalarini, ularning farqi va UI/UX dizayndagi ahamiyatini o'rganadi; 4-haftada tanlangan ranglar, shriftlar va oraliqlardan foydalanib, Figma'da «E-kutubxona» loyihasi uchun birinchi mini UI kit sahifasini (ranglar, tipografiya, tugmalar) yaratadi.

**Kutiladigan natija:**
- UI Kit ta'rifini aytadi va uni «konstruktor» o'xshatishi bilan tushuntiradi;
- UI Kit'ning 4 ta afzalligini misol bilan izohlaydi;
- Dizayn tizimining 5 ta asosiy qismini sanaydi va UI Kit'dan farqini ko'rsatadi;
- Dizayn tokeni (rang, shrift, bo'shliq qiymati) nima ekanini tushunadi;
- Figma'da Color va Text styles yaratib, ulardan 3 ta tugma holatida foydalanadi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va kirish | Rang (60-30-10), shrift ierarxiyasi, 8-point grid. Muammo: «10 ta ekranda 10 xil ko'k tugma — nima bo'ladi?» |
| 10–35 daq | Yangi mavzu | UI Kit, afzalliklari, dizayn tizimi va 5 qismi, tokenlar, atom → molekula → organizm |
| 35–40 daq | Tanaffus | Harakatli tanaffus |
| 40–70 daq | Amaliy mashg'ulot | Figma'da «E-kutubxona UI kit» sahifasi: ranglar, tipografiya, tugmalar |
| 70–76 daq | Tezkor nazorat | 5 ta savol |
| 76–80 daq | Xulosa va uyga vazifa | Keyingi dars: mashhur UI kitlar (HIG, Ant Design, Bootstrap, Figma, Material UI) |

---

## 2. Dars konspekti

### 2.1. Muammo: «10 xil ko'k tugma»
Katta loyihada 5 ta dizayner har biri o'z tugmasini chizsa: ranglar biroz farq qiladi (#1E88E5, #2196F3, #1976D2...), burchaklar 4, 8, 12 px, shriftlar har xil. Foydalanuvchi bu ilovani «tartibsiz» deb his qiladi, dasturchi esa har bir tugmani alohida kodlaydi. Yechim — **UI Kit** va **dizayn tizimi**.

### 2.2. UI Kit nima?
**UI Kit (User Interface Kit)** — dizaynerlar va dasturchilar uchun mo'ljallangan, **tayyor va qayta ishlatiladigan** foydalanuvchi interfeysi komponentlari to'plami. U tugmalar, ikonalar, formalar, navigatsiya panellari, modal oynalar va boshqa elementlarni tayyor shaklda beradi.
- Uslubiy ko'rsatma ta'rifi: UI Kit — dizaynerlar uchun vizual **«konstruktor»**: interfeysni noldan chizmasdan, tayyor bo'laklardan yig'ish.
- UI Kit'lar odatda Figma, Sketch, Adobe XD kabi dasturlar uchun tayyorlanadi va loyihaning dastlabki bosqichlarida qo'llaniladi.
- Asosiy maqsad — **vaqtni tejash** va brendning vizual tilini (rang palitrasi, tipografiya) saqlash.

### 2.3. UI Kit'ning 4 afzalligi (qo'llanma)
| Afzallik | Ma'nosi | Misol |
|---|---|---|
| **Vaqtni tejash** | elementni noldan yaratish shart emas | tayyor «Kirish» tugmasini nusxalash |
| **Vizual uyg'unlik** | barcha komponentlar bir-biriga mos | hamma ekranda bir xil ko'k va bir xil burchak |
| **Moslashuvchanlik** | kitni o'z ehtiyojiga moslash mumkin | brend rangini almashtirish |
| **Jamoaviy ishlash** | dizayner va dasturchi uchun yagona vizual til | «Primary Button» — ikkalasi uchun bir xil narsa |

### 2.4. Dizayn tizimi (Design System)
**Dizayn tizimi** — faqat vizual elementlar to'plami emas, balki mahsulot dizaynini yaratish va rivojlantirishga xizmat qiluvchi **yagona konseptual tizim**: kompaniyaning barcha interfeyslari bir xil mantiq, uslub va qoidalarga asoslanadi.

Uslubiy ko'rsatma bo'yicha **5 asosiy qism**:
1. **Komponentlar (UI Elements)** — tugma, input, karta, menyu.
2. **Vizual uslublar (Visual Styles / Tokens)** — ranglar, tipografiya, bo'shliqlar.
3. **Shablonlar (Templates / Layouts)** — tayyor sahifa tuzilmalari.
4. **Prinsip va qo'llanmalar (Principles & Guidelines)** — «qachon, qanday ishlatiladi» qoidalari.
5. **Hujjatlashtirish (Documentation)** — hamma uchun yozma tavsif.

### 2.5. UI Kit va dizayn tizimi farqi
| | UI Kit | Dizayn tizimi |
|---|---|---|
| Nima | tayyor komponentlar to'plami | komponentlar + tokenlar + qoidalar + hujjatlar |
| Savol | «Nima bor?» | «Nima bor, qachon va nega ishlatiladi?» |
| O'xshatish | LEGO bo'laklari qutisi | LEGO qutisi + yig'ish yo'riqnomasi + qoidalar |
| Kim uchun | asosan dizayner | dizayner, dasturchi, menejer — butun jamoa |

UI Kit — dizayn tizimining **bir qismi**.

### 2.6. Dizayn tokenlari
**Token** — dizayn qarorining nomlangan qiymati:
```
color-primary   = #2563EB     (asosiy rang)
color-text      = #1F2937
font-heading    = Poppins, 24px, SemiBold
font-body       = Inter, 16px, Regular
space-s = 8px   space-m = 16px   space-l = 24px   (8-point grid)
radius-m = 8px
```
Token o'zgarsa (masalan, brend rangi), u ishlatilgan barcha joy avtomatik yangilanadi — Figma'da bu **Styles** (Color styles, Text styles) va **Variables** orqali amalga oshadi.

### 2.7. Kichikdan kattaga: atom → molekula → organizm
- **Atom** — eng kichik bo'lak: rang, shrift, ikonka, bitta tugma.
- **Molekula** — bir nechta atom: qidiruv maydoni (input + tugma + ikonka).
- **Organizm** — molekulalar majmuasi: header (logo + qidiruv + profil + savat).
Shablon va sahifa shu bo'laklardan yig'iladi. (Bu yondashuv amalda Atomic Design deb ataladi.)

---

## 3. Amaliy topshiriqlar va yechimlar

### 1-topshiriq. UI Kit yoki dizayn tizimi? (oson)
Quyidagilarni ajrating: (a) 20 ta tayyor tugma va ikonka fayli; (b) tugmalar + ranglar + «asosiy tugma sahifada bitta bo'ladi» qoidasi + hujjat sayti; (c) Figma'dagi «Mobile UI Kit» shabloni.

**Yechim:** (a) UI Kit; (b) dizayn tizimi — komponent, token, prinsip va hujjat bor; (c) UI Kit.

### 2-topshiriq. Tokenlar jadvali (o'rta)
4-haftadagi «E-kutubxona» uchun token jadvalini tuzing: 5 ta rang (primary, secondary, fon, matn, xato), 3 ta matn uslubi (H1, H2, Body), 4 ta bo'shliq (8, 16, 24, 32).

**Yechim (namuna):**
| Token | Qiymat |
|---|---|
| color-primary | #2563EB |
| color-secondary | #F59E0B |
| color-bg | #F9FAFB |
| color-text | #111827 |
| color-error | #DC2626 |
| text-h1 | Poppins 28 / SemiBold |
| text-h2 | Poppins 20 / SemiBold |
| text-body | Inter 16 / Regular, line-height 150% |
| space | 8 · 16 · 24 · 32 |

Tekshirish: primary rang oq matn bilan WCAG 4.5:1 kontrastga javob beradimi (11-dars).

### 3-topshiriq. Figma'da mini UI kit sahifasi (qiyin)
Figma'da `UI Kit` nomli yangi sahifa (Page) oching va 3 ta bo'lim yarating:
1. **Colors** — 5 ta 80 × 80 kvadrat; har biri **Color style** sifatida saqlangan (Fill → Style belgisi → **+** → nom: `Primary/500`).
2. **Typography** — H1, H2, Body, Caption namunalari; har biri **Text style**.
3. **Buttons** — Primary, Secondary, Disabled tugmalari: 160 × 48, corner radius 8, matn Body style, faqat yaratilgan stillardan foydalanilgan.

**Yechim (tekshiruv):** o'ng paneldagi «Local styles» ro'yxatida 5 ta rang va 4 ta matn uslubi bor; tugmalarda HEX qiymat qo'lda yozilmagan, balki stil nomi ko'rinadi; Primary rangni o'zgartirganda Primary tugma ham avtomatik o'zgaradi.

---

## 4. Tezkor nazorat (savollar va javoblar)

1. **UI Kit nima?**
   - *Javob:* Dizaynerlar va dasturchilar uchun tayyor, qayta ishlatiladigan interfeys komponentlari to'plami.
2. **UI Kit'ning 4 afzalligi?**
   - *Javob:* Vaqtni tejash, vizual uyg'unlik, moslashuvchanlik, jamoaviy ishlash.
3. **Dizayn tizimining 5 qismi?**
   - *Javob:* Komponentlar, vizual uslublar (tokenlar), shablonlar, prinsip va qo'llanmalar, hujjatlashtirish.
4. **UI Kit va dizayn tizimi farqi?**
   - *Javob:* UI Kit — komponentlar to'plami; dizayn tizimi — komponentlar + tokenlar + qoidalar + hujjatlar; UI Kit uning bir qismi.
5. **Dizayn tokeni nima?**
   - *Javob:* Dizayn qarorining nomlangan qiymati (masalan, `color-primary = #2563EB`), o'zgarsa hamma joyda yangilanadi.

---

## 5. Uyga vazifa

1. «E-kutubxona» UI kit sahifasini davom ettiring: Colors, Typography, Buttons bo'limlariga **Inputs** (oddiy, fokus, xato holatlari) bo'limini qo'shing.
2. Barcha elementlarda faqat Color va Text styles'dan foydalaning.
3. Token jadvalini (rang, shrift, bo'shliq) Figma sahifasining yon tomoniga matn sifatida yozing.
