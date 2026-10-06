# 17-dars. Figma: interfeys, komponentlar va dizaynni front-endga tayyorlash

**Fan:** Web Full-stack dasturlash
**Sinf:** 8-sinf
**Hafta:** 6-hafta, 2-dars (umumiy 17-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** O'quv dasturi, 7-mavzu «Moslashuvchan (responsiv) dizayn va media so'rovlar va Figma»: «Figma interfeysi va asosiy elementlar (frame, artboard), komponentlar va ularning variantlari, rang va shriftlarni aniqlash, spacing va layout gridlarni ishlatish, ... eksport qilish (SVG, PNG, JPEG) va front-endga tayyorlash, CSS uchun rang, font, o'lcham, margin/padding qiymatlarini olish.» Figma interfeysi tez-tez yangilanadi: tugma joylari mentor ekranida tekshirilishi kerak.

---

## Darsning maqsadi

O'quvchilarga Figma interfeysi (asboblar paneli, qatlamlar, xossalar paneli), frame (artboard) tushunchasi, rang va shriftlarni belgilash, layout grid va auto layout, komponent va variantlar, hamda dizayndan CSS qiymatlarini (rang, shrift, o'lcham, padding, radius) olish va rasm/ikonkalarni SVG, PNG, JPEG ko'rinishida eksport qilishni o'rgatish.

## Kutiladigan natija

- Figma interfeysining asosiy qismlarini (asboblar, Layers, Design paneli) ko'rsatadi;
- Telefon va kompyuter uchun frame yaratadi;
- Rang, shrift va masofalarni belgilab, layout grid qo'yadi;
- Tugma komponentini yaratib, variantlarini (masalan, oddiy va bosilgan) qiladi;
- Dizayndagi qiymatlarni CSS ga o'tkazadi va rasm/ikonkani SVG yoki PNG qilib eksport qiladi.

## Kerakli jihozlar

- Kompyuter, brauzer va Figma akkaunti (mentor yordami bilan)
- Mentor tayyorlagan demo Figma fayli
- 15–16-darslardagi «Maktab sayti» sahifasi

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 00–08 | Takrorlash | 15–16-dars: responsiv sahifa |
| 08–22 | Yangi mavzu 1 | Figma interfeysi va frame |
| 22–32 | Yangi mavzu 2 | Rang, shrift, layout grid, auto layout |
| 32–38 | Tanaffus + mini-quiz | Slayddagi `.quiz` |
| 38–50 | Yangi mavzu 3 | Komponent, variantlar va eksport |
| 50–75 | Amaliyot | CSS qiymatlarini olish, xulosa |
| 75–80 | Xulosa | Tezkor nazorat, uyga vazifa |

---

## Konspekt (mentor aytadigan matn)

### 1. Figma interfeysi va frame

**Figma** — brauzerda ishlaydigan dizayn vositasi (bepul tarif mavjud). Asosiy qismlari: yuqorida yoki pastda **asboblar paneli** (Move, **Frame** — `F`, shakllar — `R` to'rtburchak, `O` ellips, **Text** — `T`), chap tomonda **Layers** (qatlamlar) va **Assets**, o'ng tomonda **Design** paneli (o'lcham, rang, shrift, effektlar). **Frame** (artboard) — dizayn «ekrani»: telefon yoki kompyuter oynasi. Frame ni tanlasangiz, o'ng panelda tayyor o'lchamlar chiqadi (masalan, Phone ~390px, Desktop ~1440px). Dizaynni 15–16-darsdagi uch breakpoint kabi uch frame bilan: telefon, planshet va kompyuter uchun chizish mumkin. Ob'ektlarni nomlash (`Header`, `Hero`, `Karta`) front-end uchun juda foydali.

Telefon frame ni birinchi chizing (mobile-first). Frame o'lchami — dizayn uchun asos, sayt esa har kenglikda ishlashi kerak.

### 2. Rang, shrift, layout grid va auto layout

Dizaynning izchilligi uchun oldin **rang** (asosiy, qo'shimcha, matn, fon), **shrift** (oila, o'lcham, qalinlik) va **masofalar** (8px ga karrali: 8, 16, 24, 32) tanlanadi. Rangni Design panelidagi **Fill** da HEX qiymat (`#17E`) bilan, shriftni **Text** bo'limida belgilaysiz. **Layout grid** (Frame → Layout grid, «+») sahifani ustunlarga bo'ladi: kompyuterda odatda 12 ustun, telefonda 4. **Auto layout** (`Shift+A`) elementlarni qator yoki ustunga tizadi, orasidagi masofa (**gap**) va ichki masofa (**padding**) ni beradi: bu aynan CSS Flexbox'ga mos. O'lcham o'zgarganda element ham moslashadi.

Ranglar va masofalarni CSS o'zgaruvchilar (`--nom`) ga yig'ing: dizaynerdan yangi rang kelsa, bitta joyda o'zgartirasiz.

### 3. Komponent, variantlar, eksport va CSS qiymatlari

**Komponent** — qayta ishlatiladigan element (tugma, karta, menyu). Elementni tanlab `Ctrl+Alt+K` (Mac: `⌘⌥K`) bosilsa, **asosiy komponent** yaratiladi, nusxalari (instance) undan o'zgaradi. **Variantlar** — bitta komponentning turli holati: `Holat = oddiy / bosilgan`, `O'lcham = kichik / katta`. Dizaynni kodga o'tkazish: elementni tanlab, o'ng paneldan **o'lcham (W, H)**, **Fill** rangi, **shrift**, **Corner radius**, auto layout **gap/padding** qiymatlarini o'qiysiz (Inspect/Dev Mode ko'rinishi tarifga qarab CSS kodni tayyor ko'rsatadi). Rasm va ikonkalar uchun: elementni tanlang → **Export** → format: **SVG** (ikonka, logotip — vektor), **PNG** (shaffoflik), **JPEG** (foto), masshtab 1x/2x.

Figma'dagi piksel qiymatini CSS ga o'tkazganda matn o'lchamini `rem` ga (px ÷ 16) aylantiring: 24px = 1.5rem. Rasmlarni eksportdan keyin hajmini kichraytiring.

---

## Kod namunasi

Figma dizayni asosida CSS (tugma va karta):

```css
:root {
  --asosiy: #17e;
  --matn: #222;
  --fon: #eee;
}
body { font-family: Arial, sans-serif; color: var(--matn); background: var(--fon); }

/* Figma: Component "Tugma" */
.tugma {
  background: var(--asosiy);
  color: #fff;
  font: 700 1rem/1.25 Arial, sans-serif;
  padding: 12px 24px;
  border-radius: 8px;
}
.tugma:hover { background: #15b; }

/* Figma: Component "Karta", auto layout: vertikal, gap 12, padding 16 */
.karta {
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 16px;
  background: #fff;
  border-radius: 12px;
}
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Frame yaratish
Telefon uchun Phone frame ni qanday yaratasiz? Qadamlarni yozing.

**Kutiladigan natija:** Frame yaratildi.

**Yechim:** Frame asbobi (F) → o'ng panelda Phone o'lchamini tanlash (~390px).

### 2-topshiriq (oson). Qiymatlarni o'qish
Figma'da tugma: Fill #17E, radius 8, padding 12/24. CSS ni yozing.

**Kutiladigan natija:** CSS tugma.

**Yechim:** 
```css
.tugma {
  background: #17e;
  border-radius: 8px;
  padding: 12px 24px;
}
```

### 3-topshiriq (o'rta). px → rem
24px shrift o'lchamini rem ga o'tkazing.

**Kutiladigan natija:** 1.5rem.

**Yechim:** 
```css
font-size: 1.5rem;   /* 24 / 16 */
```

### 4-topshiriq (o'rta). Auto layout
Auto layout: yo'nalish gorizontal, gap 16, padding 24. CSS ni yozing.

**Kutiladigan natija:** Flexbox CSS.

**Yechim:** 
```css
.panel {
  display: flex;
  flex-direction: row;
  gap: 16px;
  padding: 24px;
}
```

### 5-topshiriq (qiyin). Eksport formati
Logotip, foto va shaffof banner uchun qaysi formatlarni tanlaysiz?

**Kutiladigan natija:** To'g'ri tanlov.

**Yechim:** Logotip — SVG; foto — JPEG; shaffof banner — PNG.

### 6-topshiriq (qo'shimcha). Ranglar tizimi
Sayt uchun 4 ta rangni CSS o'zgaruvchilar bilan e'lon qiling.

**Kutiladigan natija:** Rang palitrasi.

**Yechim:** 
```css
:root {
  --asosiy: #17e;
  --ikkinchi: #fb0;
  --matn: #222;
  --fon: #eee;
}
```

---

## Tezkor nazorat (dars oxirida)

1. Frame nima? — Figma'dagi dizayn ekrani.
2. Auto layout qaysi CSS ga o'xshaydi? — Flexbox.
3. Komponent nima uchun kerak? — Qayta ishlatish va bir joyda o'zgartirish.
4. Ikonka uchun qaysi format? — SVG.
5. 24px necha rem? — 1.5rem.

## Keng tarqalgan xatolar

- Qatlamlarga nom bermaslik («Rectangle 47»).
- Har joyda boshqa-boshqa rang va masofa ishlatish.
- Komponent o'rniga elementni nusxalab yuborish.
- Foto uchun SVG, ikonka uchun JPEG tanlash.
- Piksel qiymatini CSS ga o'ylamay ko'chirib, rem ga o'tkazmaslik.

## Bilasizmi? (qo'shimcha)

- Figma'da `Ctrl+D` — nusxa, `Ctrl+G` — guruhlash, `Shift+A` — auto layout.
- Figma'ning Inspect/Dev Mode paneli dizayn qiymatlarini CSS ko'rinishida ko'rsatishi mumkin: ko'rinishi tarifga bog'liq.
- Dizayn tizimi (design system) katta kompaniyalarda yuzlab komponentdan iborat bo'ladi.
