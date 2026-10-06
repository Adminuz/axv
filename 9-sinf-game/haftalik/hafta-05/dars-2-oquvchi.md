# 14-dars. Tugmalar turlari va holatlari (Normal, Hover, Pressed)

> «START» tugmasini bosganingizda u biroz botib ketadi va o'yin boshlanadi. Shu kichik o'zgarish — dizaynerning puxta ishi. Bugun o'yin tugmalarini o'zimiz yaratamiz.

## Dars xulosasi

- **UI dizayn** — tugmalar, menyular, belgilar va o'yinchi o'zaro ta'sir qiladigan elementlarni yaratish jarayoni; maqsad — boshqaruvni tushunarli, qulay va chiroyli qilish.
- UI-dizaynerning 5 vazifasi: axborotni vizual uzatish, soddalik, uslubga moslik, funksional boshqaruv, estetika.
- Asosiy UI elementlari: **tugmalar, menyular, HUD** (va ikonlar, indikatorlar, progress barlar).
- **Primary** tugma — asosiy harakat (Start, OK); **Secondary** — bekor qilish, ortga (Cancel, Back).
- Tugma talablari: qulay o'lcham va joy, ajralib turuvchi rang va shakl, **holatlar aniq farqli**.
- Holatlar: **Normal** (tinch), **Hover** (kursor ustida), **Pressed** (bosilgan).
- Photoshop: Rectangle Tool, Corners, Stroke, Text Tool, Layer Styles; holatlar alohida qatlamlarda, alohida PNG.

## Qo'shimcha ma'lumot

### 1. Tugma — o'yinchi bilan suhbat
Tugma o'yinchiga uch narsani aytishi kerak: «meni bosish mumkin» (Normal), «siz meni tanladingiz» (Hover), «buyruq qabul qilindi» (Pressed). Agar holatlar bir xil bo'lsa, o'yinchi ikki-uch marta bosib, adashib qoladi. Lift tugmasini eslang: bosilganda u yonadi — siz buyruq qabul qilinganini bilasiz.

### 2. Ierarxiya: qaysi tugma muhimroq?
Bir ekranda «Davom etish» va «Chiqish» yonma-yon tursa, o'yinchi ko'pincha birinchisini xohlaydi. Shuning uchun:
- **Primary:** yorqin to'yingan rang (yashil, ko'k), kattaroq, to'liq to'ldirilgan.
- **Secondary:** sokin (kulrang yoki faqat kontur), kichikroq.
- **Xavfli harakat** (o'chirish, chiqish) ko'pincha qizil va boshqalardan biroz uzoqroq joylashadi — tasodifan bosilmasin.

### 3. Holatlarni qanday farqlash?

| Holat | Rang | Soya / effekt | Joylashuv |
|---|---|---|---|
| Normal | asosiy | Drop Shadow | joyida |
| Hover | ochroq | Outer Glow | biroz kattaroq (ixtiyoriy) |
| Pressed | to'qroq | soya yo'q yoki Inner Shadow | 2–4 px pastda |

Qoida: kamida **ikki belgi** bilan farqlang (masalan, rang + soya), faqat rang bilan emas — rang ko'rish farqi bor o'yinchilar ham sezsin.

### 4. Qatlamlar tartibi

```
btn_start (Group)
  btn_start_normal
  btn_start_hover
  btn_start_pressed
```

Har holat — Normal guruhining nusxasi (`Ctrl + J`), faqat farqlari o'zgartiriladi. Eksportda keraklisidan boshqasini yashiring (ko'z belgisi) va fonni ham yashiring.

### 5. Odatiy xatolar
- Matn tugmadan chiqib ketgan yoki chetga yopishgan.
- Juda ko'p effekt: gradient + bevel + glow + pattern — tugma «og'ir» ko'rinadi.
- Oq fon bilan saqlangan PNG — o'yin fonida oq to'rtburchak.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| UI (User Interface) | Foydalanuvchi o'yin bilan muloqot qiladigan vizual va interaktiv elementlar |
| UX | Foydalanuvchi tajribasi: o'yinchi interfeysdan qanday taassurot oladi |
| Tugma (Button) | Buyruq berish, tanlov qilish yoki amal bajarish elementi |
| Primary button | Asosiy harakat tugmasi: Start, OK |
| Secondary button | Ikkinchi darajali tugma: Cancel, Back |
| Normal | Tugmaning tinch holati |
| Hover | Kursor (yoki tanlov) tugma ustiga kelgan holat |
| Pressed | Tugma bosilgan payt |
| Stroke | Shakl atrofidagi kontur chizig'i |
| Layer Styles | Qatlam effektlari: gradient, soya, glow, bevel |
| HUD | O'yin davomida doim ko'rinadigan ma'lumot paneli |

## Bilasizmi?

- HUD atamasi harbiy aviatsiyadan kelgan: uchuvchi pastga — asboblarga qaramasdan, old oynadagi ma'lumotni ko'radi.
- Ko'p konsol o'yinlarida sichqoncha yo'q, shuning uchun «hover» o'rniga geympad bilan **tanlangan** (focus) holat ishlatiladi — u ham xuddi shunday ajralib turishi kerak.
- Mobil o'yinlarda tugma barmoqqa qulay bo'lishi uchun odatda kamida 44–48 piksel (nuqta) o'lchamda qilinadi.
- Ba'zi o'yinlarda tugma bosilganda kichik tovush va tebranish ham beriladi — bu ham «buyruq qabul qilindi» signali.

## Topshiriqlar

### 1. Tugmalarni ajrating · oson
Start, Back, OK, Cancel, Davom etish, Bekor qilish, Saqlash, Ortga — Primary va Secondary guruhlarga ajrating.

**Kutiladigan natija:** ikki ustunli jadval.

### 2. O'yindan misol · oson
Sevimli o'yiningiz bosh menyusidagi tugmalarni yozing: qaysi biri Primary, qaysi biri Secondary, qanday farqlanadi?

**Kutiladigan natija:** 3–5 qatorli tahlil.

### 3. START tugmasi · oson
Photoshop'da 1920×1080 hujjatda yumaloq burchakli (Corners 30 px), stroke'li «START» tugmasini chizing.

**Kutiladigan natija:** PSD fayl, matn markazda.

### 4. Holat jadvali · oson
O'zingizning START tugmangiz uchun Normal, Hover, Pressed holatlarida rang, soya va joylashuv qanday bo'lishini jadvalda yozing.

**Kutiladigan natija:** 3 qatorli jadval.

### 5. Uch holat · o'rta
START tugmasining 3 holatini alohida nomlangan qatlamlarda yarating.

**Kutiladigan natija:** `btn_start_normal`, `_hover`, `_pressed` qatlamlari.

### 6. Secondary tugma · o'rta
«ORTGA» tugmasini Secondary uslubda (kontur, kichikroq, sokin rang) START bilan bir uslubda yarating.

**Kutiladigan natija:** ikki tugma yonma-yon, ierarxiya aniq.

### 7. Xatoni toping · o'rta
Dizaynda: «Chiqish» tugmasi eng katta va yorqin yashil, «Boshlash» — kichik kulrang, Hover va Normal bir xil. Muammolarni yozing va tuzating.

**Kutiladigan natija:** kamida 3 ta muammo va yechim g'oyasi.

### 8. Eksport · o'rta
Har holatni alohida shaffof PNG qilib eksport qiling, to'g'ri nomlang.

**Kutiladigan natija:** 3 ta PNG, oq fon yo'q.

### 9. Disabled holat · qiyin
START tugmasiga to'rtinchi — **Disabled** (bosib bo'lmaydigan) holatni qo'shing. Uni boshqalardan qanday farqlaysiz?

**Kutiladigan natija:** 4-qatlam va 1–2 jumla izoh.

### 10. Uslubli tugma · qiyin
O'yiningiz uslubiga mos tugma yarating (masalan, yog'och taxta, tosh, neon) — gradient va Bevel & Emboss bilan, 3 holat.

**Kutiladigan natija:** 3 ta PNG, uslub o'yin atmosferasiga mos.

### 11. Holatlar sheet · qiyin
13-darsdagi bilim bilan: 3 holatni bitta PNG sheetga (3 qator, teng katak) yig'ing.

**Kutiladigan natija:** `btn_start_sheet.png` va katak o'lchami.

### 12. Ikonkali tugma · bonus
11-darsdagi sozlamalar (tishli g'ildirak) ikonkasidan dumaloq ikonka-tugma yasang: 3 holat.

**Kutiladigan natija:** 3 ta PNG, ikonka va tugma bir uslubda.

## O'zingizni tekshiring

1. UI dizayn nima va u UX ga qanday ta'sir qiladi?
2. UI-dizaynerning qaysi vazifalarini bilasiz?
3. Asosiy UI elementlarini sanang.
4. Primary va Secondary tugmalar qanday farqlanadi?
5. Tugma dizayniga qanday talablar qo'yiladi?
6. Hover va Pressed holatlarini qanday vizual belgilar bilan farqlash mumkin?
7. Nega holatlar alohida qatlamlarda tayyorlanadi?

## Uyga vazifa

O'yiningiz uchun Primary («START») va Secondary («ORTGA») tugmalarni bir uslubda yarating, har biri uchun Normal, Hover, Pressed holatlarini tayyorlab, 6 ta shaffof PNG qilib eksport qiling (20–30 daqiqa). Batafsil — haftalik uyga vazifada.
