# 17-dars. Interfeys elementlari va UI komponentlar: tugma, maydon, karta, Auto layout va variantlar

**Fan:** UX/UI dizayn va Advanced Front-end
**Sinf:** 9-sinf
**Hafta:** 6-hafta, 2-dars (umumiy 17-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** Uslubiy ko'rsatma, II bob, 2.1 «Figma'da interfeys dizayni»: «Interfeys elementlari mahsulotning tashqi ko'rinishini va foydalanuvchi bilan o'zaro aloqasini belgilaydi. Figma'da foydalanuvchi tugmalar, piktogrammalar, fikr-mulohaza shakllari va boshqa elementlarni yaratishi mumkin.» Auto layout, Constraints va Variants bo'yicha qadamlar Figma'ning umumiy ish tartibidan olingan; interfeys yangilanishi mumkin.

---

## Darsning maqsadi

O'quvchilarga asosiy interfeys elementlari (tugma, kiritish maydoni, ikonka, karta) va ularning holatlarini (oddiy, hover, bosilgan, o'chirilgan, xato) o'rgatish; Auto layout (gap, padding, Hug/Fill) va Constraints bilan moslashuvchan element yasash; komponent (main va instance) hamda variantlarni yaratish.

## Kutiladigan natija

- Tugma, kiritish maydoni va kartaning asosiy qismlarini va holatlarini aytadi;
- Auto layout bilan padding va gap beradi, Hug va Fill farqini biladi;
- Elementni komponentga aylantiradi, nusxalari (instance) qanday o'zgarishini tushuntiradi;
- Tugma uchun variantlar (Holat, O'lcham) yaratadi;
- «Kitob» kartasi komponentini E-kutubxona maketida qo'llaydi.

## Kerakli jihozlar

- Kompyuter va Figma
- 16-darsdagi «E-kutubxona» fayli
- Mentor tayyorlagan kitob kartasi namunasi

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 00–08 | Takrorlash | 16-dars: fayl tuzilmasi, vektor |
| 08–22 | Yangi mavzu 1 | Interfeys elementlari va holatlari |
| 22–32 | Yangi mavzu 2 | Auto layout va Constraints |
| 32–38 | Tanaffus + mini-quiz | Slayddagi `.quiz` |
| 38–50 | Yangi mavzu 3 | Komponent va variantlar |
| 50–75 | Amaliyot | Kitob kartasi: yig'ish, tekshirish, xulosa |
| 75–80 | Xulosa | Tezkor nazorat, uyga vazifa |

---

## Konspekt (mentor aytadigan matn)

### 1. Interfeys elementlari va ularning holatlari

Interfeys elementlari — foydalanuvchi ko'radigan va bosadigan bo'laklar: **tugma**, **kiritish maydoni** (label, placeholder, xato xabari), **ikonka**, **karta** (rasm, nom, muallif, tugma), **menyu**. Har bir interaktiv elementning **holatlari** (states) bor: **oddiy** (default), **hover** (kursor ustida), **bosilgan** (pressed), **o'chirilgan** (disabled), maydonda yana **fokus** va **xato**. Holatlar foydalanuvchiga «bu bosiladi, bu hozir ishlamaydi» deb tushuntiradi. Qoidalar: tugma kamida 44 × 44 px (barmoq uchun), matn va fon kontrasti yetarli, bir sahifada bitta asosiy (primary) tugma, masofalar 8 ga karrali.

Dizaynda ham har holatni alohida chizing: dasturchi hover va disabled ko'rinishini siz chizmasangiz, o'zi taxmin qiladi.

### 2. Auto layout va Constraints

**Auto layout** (`Shift+A`) — ichidagi elementlarni avtomatik qator yoki ustun qilib tizadi va CSS Flexbox'ga mos keladi: **yo'nalish** (gorizontal/vertikal), **gap** (elementlar orasi), **padding** (ichki masofa). Element o'lchamini ikki xil belgilash mumkin: **Hug contents** (mazmunga moslashadi, CSS'dagi `fit-content` kabi) va **Fill container** (bo'sh joyni to'ldiradi, `flex: 1` kabi), **Fixed** — qotirilgan o'lcham. Shu sabab tugmadagi matn uzayganda tugma ham kengayadi. **Constraints** (Left, Right, Top, Bottom, Center, Scale) — frame kattalashganda element qayerga «yopishishini» bildiradi: masalan, savat ikonkasi header'ning o'ng tomoniga (Right) yopishsin.

Auto layout bilan maket yaratsangiz, kodga o'tkazish ancha oson bo'ladi: Auto layout qiymatlari to'g'ridan-to'g'ri `gap` va `padding` ga aylanadi.

### 3. Komponent va variantlar

**Komponent** — qayta ishlatiladigan element. Tanlab `Ctrl+Alt+K` (Mac: `⌘⌥K`) bosilsa, **main component** yaratiladi; uning nusxalari — **instance**. Main component o'zgartirilsa, barcha instance larda ham o'zgaradi: logotip rangini bir joyda almashtirasiz. Instance da matn, ikonka kabi alohida xossalarni o'zgartirish mumkin (override). **Variantlar** — bir komponentning turli ko'rinishlari: tugma uchun xossa `Holat` = oddiy / hover / bosilgan / o'chirilgan, `O'lcham` = kichik / katta. Komponentlar nomi `Tugma/Asosiy`, `Karta/Kitob` kabi slesh bilan tartiblanadi. Bu 13–15-darslardagi UI kit va dizayn tizimining amaliy qismi.

Komponentni yaratgach, uni hech qachon nusxalab «ajratmang» (Detach instance): aks holda bog'lanish uziladi va yangilanishlar kelmaydi.

---

## Kod namunasi

Kitob kartasi: Figma qiymatlari → CSS:

```css
.karta {
  display: flex;
  flex-direction: column;     /* Auto layout: vertikal */
  gap: 12px;                  /* gap 12 */
  padding: 16px;              /* padding 16 */
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 2px 8px #0003;
}
.karta img { width: 100%; aspect-ratio: 3 / 4; object-fit: cover; }
.karta h3 { font-size: 1.125rem; margin: 0; }
.karta .muallif { color: #666; }
.karta.tanlangan { outline: 2px solid #17e; }      /* variant: tanlangan */
.tugma { background: #17e; color: #fff; padding: 12px 24px; border-radius: 8px; }
.tugma:hover { background: #15b; }
.tugma:disabled { background: #ccc; color: #666; }
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Holatlarni sanang
Tugmaning 4 ta holatini yozing.

**Kutiladigan natija:** 4 holat.

**Yechim:** Oddiy, hover, bosilgan, o'chirilgan.

### 2-topshiriq (oson). Hover CSS
Tugma hover holatida to'qroq bo'lsin: CSS yozing.

**Kutiladigan natija:** Hover qoidasi.

**Yechim:** .tugma:hover { background: #15b; }

### 3-topshiriq (o'rta). Auto layout qiymatlari
Auto layout: gorizontal, gap 8, padding 12/24. CSS ga o'tkazing.

**Kutiladigan natija:** Flex CSS.

**Yechim:** 
```css
.tugma {
  display: inline-flex;
  gap: 8px;
  padding: 12px 24px;
}
```

### 4-topshiriq (o'rta). Hug yoki Fill
Qidiruv maydoni qolgan joyni to'ldirsin: qaysi o'lcham rejimi?

**Kutiladigan natija:** Fill container.

**Yechim:** Fill container (CSS dagi flex: 1 kabi).

### 5-topshiriq (qiyin). Variantlar xossalari
Tugma komponenti uchun 2 ta variant xossasini va qiymatlarini yozing.

**Kutiladigan natija:** 2 xossa.

**Yechim:** Holat: oddiy/hover/bosilgan/o'chirilgan; O'lcham: kichik/katta.

### 6-topshiriq (qo'shimcha). Karta komponenti
Kitob kartasi komponentining tuzilishini (qatlamlar va xossalar) yozing.

**Kutiladigan natija:** To'liq tuzilma.

**Yechim:** Karta/Kitob: rasm, nom, muallif, tugma; Auto layout vertikal, gap 12, padding 16; Holat: oddiy/tanlangan.

---

## Tezkor nazorat (dars oxirida)

1. Tugma holatlari? — Oddiy, hover, bosilgan, o'chirilgan.
2. Auto layout qaysi CSS ga mos? — Flexbox.
3. Hug va Fill farqi? — Hug — mazmunga, Fill — bo'sh joyga moslashadi.
4. Komponent nima uchun kerak? — Qayta ishlatish va bir joyda yangilash.
5. Instance nima? — Main componentdan olingan nusxa.

## Keng tarqalgan xatolar

- Faqat «oddiy» holatni chizib, boshqalarini unutish.
- Padding va gap ni 8 ga karrali qilmaslik.
- Komponent o'rniga elementni nusxalash.
- Instance ni Detach qilib, bog'lanishni uzish.
- Tugma o'lchamini juda kichik qilish (44px dan kam).

## Bilasizmi? (qo'shimcha)

- Material Design va iOS Human Interface Guidelines tugmalar va ularning holatlari uchun tayyor qoidalar beradi.
- Figma'dagi `Variables` rang va masofalarni nomlangan qiymat (token) sifatida saqlaydi.
- Auto layout ichida Auto layout joylashtirish mumkin: murakkab maketlar shunday yig'iladi.
