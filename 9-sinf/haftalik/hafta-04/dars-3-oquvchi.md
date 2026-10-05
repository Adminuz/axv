# 12-dars. UI kompozitsiyasi va vizual ierarxiya asoslari

> Shriftlar va ranglar chiroyli tanlangan, lekin interfeysda nima qayerdaligi tushunarsizmi? Ushbu darsda kompozitsiyaning 4 oltin tamoyili, vizual ierarxiya va bo'sh joy (White space) qudratini o'rganamiz.

## Dars xulosasi

- **Kompozitsiya** &mdash; vizual elementlarni mantiqiy tartibga solish va foydalanuvchi diqqatini eng muhim harakatga yo'naltirish san'atidir.
- **Kompozitsiyaning 4 asosiy tamoyili:**
  1. **Balans (Muvozanat):**
     - *Simmetrik:* Chap va o'ng tomonlar bir xil, klassik barqarorlik.
     - *Asimmetrik:* Elementlar har xil, ammo vizual og'irlik teng taqsimlangan (zamonaviy).
  2. **Kompozitsion markaz (Focal Point):** Ekranga qaraganda ko'z birinchi to'xtaydigan eng asosiy nuqta (katta banner, CTA tugma).
  3. **Ritm:** Bir xil intervallar (masalan 8px, 16px), takroriy kartalar va ikonalar oqimi.
  4. **Kontrast:** Muhim elementlarni o'lcham, qalinlik va rang bilan ajratish.
- **Bo'sh joy (White Space / Negative Space):** Elementlarning bir-biriga yopishib ketmasligi va foydalanuvchi miyasiga tanaffus berish uchun zarur bo'shliq.
- **8-point Grid tizimi:** Barcha masofalar, o'lchamlar va chekinishlar 8 ga karrali (8, 16, 24, 32, 48px) qilib belgilanadi.

## Qo'shimcha ma'lumot

### F va Z shaklidagi skanerlash naqshlari
- **F-pattern:** Matn ko'p bo'lgan veb-saytlarda (yangiliklar, bloglar) odamlar ekranni F harfi kabi (avval tepadan o'ngga, keyin pastga va qisqaroq o'ngga) ko'zdan kechiradi.
- **Z-pattern:** Landing page va ilova bosh sahifalarida odamlar Z harfi kabi (Logotip &rarr; Menyu &rarr; Markaziy rasm &rarr; Asosiy CTA tugma) qaraydi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Composition | Kompozitsiya &mdash; elementlarni uyg'un joylashtirish tuzilmasi |
| Focal Point | Kompozitsion markaz (asosiy diqqat nuqtasi) |
| Visual Hierarchy | Vizual ierarxiya &mdash; ma'lumotlarning muhimlilik darajasi tartibi |
| White Space | Bo'sh joy (foydalanuvchi ko'zi dam oladigan toza oraliqlar) |
| Grid System | To'r tizimi &mdash; elementlarni tekis joylashtirish qoidalari |
| CTA (Call to Action) | Harakatga chaqiruvchi asosiy tugma («Sotib olish», «Ro'yxatdan o'tish») |

## Bilasizmi?

- Mashhur dizaynerlar kompozitsiyada "3 soniya qoidasi"ga amal qiladi: foydalanuvchi ekranga qaraganidan so'ng 3 soniya ichida bu ilova nima haqidaligini va qaysi tugmani bosish kerakligini tushunishi shart!
- Apple kompaniyasi o'z mahsulotlarining taqdimot sahifalarida ekran maydonining 60% dan ortig'ini toza bo'sh joy (White Space) qilib qoldiradi.

## Topshiriqlar

### 1. Balans turlari · oson

Simmetrik va asimmetrik balans farqini daftaringizga bittadan chizma bilan tushuntiring.

**Kutiladigan natija:** 2 ta chizma: biri markazga nisbatan teng, ikkinchisi har xil o'lchamli, lekin muvozanatli.

### 2. Simmetrik karta · oson

Figma'da ikonka, sarlavha va tugma markazda joylashgan ma'lumot kartasini chizing.

**Kutiladigan natija:** barcha elementlar vertikal o'q bo'ylab markazlangan karta.

### 3. Asimmetrik karta · oson

Xuddi shu ma'lumotni asimmetrik ko'rinishda qayta chizing: rasm chapda, matn va tugma o'ngda.

**Kutiladigan natija:** vizual og'irligi muvozanatli, zamonaviy ko'rinishdagi karta.

### 4. 8-point oraliqlar · oson

3 ta element orasidagi masofani `16px` va `24px` qiling. `Alt` tugmasini bosib, masofani tekshiring.

**Kutiladigan natija:** skrinshotda Figma ko'rsatgan masofalar aynan 16 va 24.

### 5. Kompozitsion markaz · o'rta

Oq ekranda diqqatni darhol tortadigan katta va yorqin «Super chegirma 50%» bannerini chizing. Qolgan elementlar unga xalaqit bermasin.

**Kutiladigan natija:** ekranga qaraganda ko'z birinchi bo'lib bannerga tushadi.

### 6. Z-pattern sarlavha bloki · o'rta

Veb-sahifa bosh qismini Z-pattern bo'yicha joylang: yuqori chapda logotip, yuqori o'ngda «Kirish», o'rtada illyustratsiya, pastki o'ngda yorqin «Boshlash» tugmasi.

**Kutiladigan natija:** ko'z yo'li Z harfi shaklida o'tadigan maket.

### 7. Bo'sh joy bilan tozalash · o'rta

Elementlari bir-biriga yopishgan tartibsiz kartani oling va unga yetarli bo'sh joy (padding 24px) qo'shing. Oldin va keyin nusxalarini yonma-yon qo'ying.

**Kutiladigan natija:** «keyin» nusxasi toza va yengil ko'rinadi.

### 8. Ritmik qator · o'rta

Bir xil o'lchamdagi 4 ta kitob kartasini bir xil `16px` oraliq bilan gorizontal qatorga joylang.

**Kutiladigan natija:** oraliqlari teng, takroriy ritmga ega kartalar qatori.

### 9. Ilova tahlili · qiyin

Eng ko'p ishlatadigan ilovangiz bosh ekranining skrinshotini oling. Kompozitsion markaz, ritm, kontrast va bo'sh joyni rangli belgilar bilan ko'rsating.

**Kutiladigan natija:** belgilangan skrinshot va har tamoyil uchun bitta jumla izoh.

### 10. F yoki Z? · qiyin

Yangiliklar sayti va mahsulot reklama sahifasi uchun qaysi o'qish naqshi (F yoki Z) mos? Har biriga sxema chizib asoslang.

**Kutiladigan natija:** 2 ta sxema: matnli sahifa uchun F, kam matnli reklama uchun Z.

### 11. Xatoni toping · qiyin

Ekranda hamma sarlavhalar bir xil o'lchamda, oraliqlar 7px, 13px, 22px va 3 ta bir xil yorqin tugma bor. Ierarxiya va ritm xatolarini toping va tuzating.

**Kutiladigan natija:** xatolar ro'yxati va 8-point grid hamda bitta asosiy CTA bilan tuzatilgan ekran.

### 12. E-kutubxona bosh ekrani · bonus

«E-kutubxona» ilovasining to'liq bosh ekranini yakunlang: yuqori panel, qidiruv, «Hafta kitobi» banneri, «Yangi kitoblar» qatori va pastki menyu. Shrift, rang va kompozitsiya qoidalariga rioya qiling.

**Kutiladigan natija:** 4-hafta mavzularini birlashtirgan, muvozanatli va tartibli mobil ekran.

## O'zingizni tekshiring

1. Kompozitsiyaning asosiy maqsadi nima?
2. Kompozitsiyaning 4 tamoyilini sanang.
3. Simmetrik va asimmetrik balans farqi nima?
4. Kompozitsion markaz (focal point) nima va u qanday yaratiladi?
5. Nega bo'sh joy (white space) xato emas?
6. F-pattern va Z-pattern qachon ishlatiladi?
7. 8-point grid nima uchun kerak?

## Uyga vazifa

«E-kutubxona to'liq bosh ekrani»: 8-point grid bo'yicha yuqori panel, banner va yorqin tugma, kitoblar kartalari qatori va pastki menyuni chizing (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
