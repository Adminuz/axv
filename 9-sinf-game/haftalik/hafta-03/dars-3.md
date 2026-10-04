# 9-dars. Ranglar nazariyasi va dizayn asoslari (2-qism): Color Picker, Swatches va Gradient bilan ishlash

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga dizaynning oltin tamoyillarini (kompozitsiya, vizual ierarxiya, kontrast, muvozanat) o'rgatish hamda Adobe Photoshop dasturida ranglar bilan professional ishlash vositalarini — Color Picker (RGB, HEX, HSB), Eyedropper (I), Swatches paneli orqali maxsus o'yin palitralari yaratish va Gradient Tool (G) yordamida dinamik o'yin elementlarini (UI panellari, osmon manzarasi, nurlar) bo'yashni amalda qo'llash ko'nikmasini rivojlantirish.
- **Kutiladigan natija:** O'quvchilar Color Picker tizimida HEX va HSB parametrlarini erkin boshqara oladi; o'yin uslubiga mos Swatches palitrasini yig'ib saqlay oladi; 5 xil gradiyent turidan (Linear, Radial, Angle, Reflected, Diamond) o'rinli foydalanib, o'yin UI panellari va atmosferasini chiza oladi.
- **Vaqt taqsimoti:**
  - O'tgan mavzuni takrorlash (RGB vs CMYK, Itten g'ildiragi va rang psixologiyasi): 10 daqiqa
  - Yangi mavzu: Dizayn tamoyillari, Color Picker va Eyedropper vositasi: 20 daqiqa
  - Swatches paneli va palitralar arxitekturasi: 15 daqiqa
  - Gradient Tool (G) turlari va Gradient Editor amaliyoti: 20 daqiqa
  - Amaliy topshiriqlar va dars yakuni: 15 daqiqa

---

## Mentor konspekti

### 1. O'yin dizaynining 6 ta asosiy tamoyili
1. **Kompozitsiya va Balans:** Sahnadagi elementlarning vizual og'irligi bir tomonga og'ib ketmasligi kerak. Simmetrik va asimmetrik muvozanat.
2. **Vizual Ierarxiya:** O'yinchi ko'zi birinchi navbatda nimani ko'rishi kerak? (1 — Qahramon, 2 — Dushman yoki Maqsad, 3 — HUD, 4 — Fon).
3. **Kontrast:** O'lcham, shakl yoki rang farqi orqali muhim detalni darhol ajratib ko'rsatish.
4. **Proportsiya va Ritm:** Elementlar o'lchamlarining mutanosibligi va takrorlanish tartibi (masalan, platformalar orasidagi masofa).
5. **Tipografiya:** Interfeysdagi matnlar o'yin janriga mos va har qanday sharoitda o'ta o'qishli (readable) bo'lishi lozim.
6. **Soddalik va Minimalizm:** Keraksiz vizual shovqindan qochish — foydalanuvchi ekranga qaraganda chalg'imasligi shart.

### 2. Photoshop Color Picker va Rang Formatlari
Color Picker oynasi rangni 4 xil matematik tizimda belgilash imkonini beradi:
- **HSB (Hue, Saturation, Brightness):** Dizaynerlar uchun eng qulay model:
  - *Hue (Tus):* 0° dan 360° gacha bo'lgan rang burchagi.
  - *Saturation (To'yinganlik):* 0% (kulrang) dan 100% gacha (sof yorqin rang).
  - *Brightness (Yorqinlik):* 0% (qora) dan 100% gacha (yorug').
- **RGB:** Qizil, Yashil, Ko'k kanallari (har biri 0 dan 255 gacha).
- **HEX (#RRGGBB):** O'yin dasturlashda va vebda keng ishlatiladigan 16-lik tizimdagi kod (masalan, `#FF0000` — sof qizil, `#00FF00` — sof yashil, `#FFFFFF` — oq).
- **Eyedropper Tool (I):** Xolstdagi yoki internetdan olingan namunadagi ixtiyoriy nuqtaga bosib, uning aniq rangini bir zumda tanlab oluvchi pipetka.

### 3. Swatches (Namunalar) Paneli
- O'yin dizaynida rang tasodifiy tanlanmaydi — butun o'yin uchun 4-6 ta asosiy rangdan iborat palitra oldindan tasdiqlanadi.
- **Palitra yaratish:**
  1. `Window -> Swatches` paneli ochiladi;
  2. Tanlangan rangni panelga qo'shish uchun `+` (Create new swatch) tugmasi bosiladi;
  3. Yangi guruh papkasi ochilib (`Cyberpunk_Palette`, `Forest_Level`), barcha ranglar bitta joyga tiziladi;
  4. Loyihani boshqa kompyuterga yoki jamoa a'zolariga o'tkazish uchun `Export Swatches (.aco)` qilinadi.

### 4. Gradient Tool (G) — Rang O'tishlari
Ranglarning biridan ikkinchisiga mayin oqib o'tish vositasi:
1. **Linear Gradient (Chiziqli):** To'g'ri chiziq bo'ylab rang o'tishi. Quyosh chiqishi/botishi osmoni, HP bar paneli uchun.
2. **Radial Gradient (Aylanma):** Markazdan tashqariga doira shaklida tarqaluvchi nur. Mash'ala nuri, sehrli qalqon, o'yin menyusidagi yorug'lik nuqtasi.
3. **Angle Gradient (Burchakli):** Markaz atrofida 360 daraja soat strelkasi bo'ylab aylanuvchi konus. Radar skaneri yoki metall disk yaltirashi uchun.
4. **Reflected Gradient (Akslantirilgan):** Markaziy chiziqning ikki tomoniga ko'zgu kabi simmetrik o'tuvchi nur. Qilich tig'ining yaltirashi yoki metall naychalar.
5. **Diamond Gradient (Olmos shaklli):** Romb/olmos shaklidagi yorug'lik aksi. Qimmatbaho javohirlar va yulduzlar yaraqlashi uchun.

### 5. Gradient Editor (Gradiyent Muharriri)
- Yuqori paneldagi gradiyent chizig'iga bosilganda ochiladi.
- **Pastki slayderlar (Color Stops):** Ranglarni belgilaydi. Sichqoncha bilan yangi nuqta qo'shish yoki o'chirish mumkin.
- **Yuqori slayderlar (Opacity Stops):** Gradiyentning turli nuqtalaridagi shaffoflikni (0% dan 100% gacha) boshqaradi.
- **Smoothness (Mayinlik):** Ranglar bir-biriga qanchalik silliq o'tishini foizda sozlaydi.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Color Picker'da HSB va HEX kodi bilan ishlash (oson)
O'yin interfeysida oltin tanga chizish uchun quyidagi parametrlarga ega oltin rangni Color Picker orqali qanday topish mumkin:
- Rang burchagi (Hue): 45°;
- To'yinganligi (Saturation): 90%;
- Yorqinligi (Brightness): 95%?
Ushbu rangning taxminiy HEX kodini aniqlang.

**Yechim:**
1. Photoshopda Foreground Color ustiga ikki marta bosilib, Color Picker ochiladi.
2. HSB bo'limidagi kataklarga mos ravishda yoziladi: `H: 45`, `S: 90%`, `B: 95%`.
3. Natijada yorqin tilla-sariq rang hosil bo'ladi.
4. Pastki `#` maydonida uning olti xonali kodi ko'rinadi (taxminan `#F2BF18` yoki `#F3C017`). Ushbu kodni ko'chirib olib, o'yin kodiga qo'yish mumkin.

### 2-topshiriq. Radial Gradient bilan sehrli qalqon nuri chizish (o'rta)
O'yin qahramonining atrofida aylanma ko'k nur taratuvchi shaffof sehrli qalqon (Magic Shield) hosil qilish kerak.
Gradient Tool va Gradient Editor yordamida ushbu shaffof nurni qanday yaratish mumkin?

**Yechim:**
1. Qahramon ustidan yangi bo'sh qatlam ochiladi (Layer: `Shield_Aura`).
2. `Gradient Tool (G)` tanlanadi va turi **Radial Gradient** ga o'tkaziladi.
3. Gradient Editor ochiladi:
   - Pastki ranglar: Markazda och moviy (`#00FFFF`), chekkada to'q ko'k (`#002288`).
   - Yuqori shaffoflik (Opacity): Markaziy nuqta 80%, eng chekka nuqta esa 0% (butunlay shaffof) qilinadi.
4. Qahramonning ko'krak markazidan boshlab tashqariga qarab sichqoncha bilan radius chizig'i tortiladi.
5. Qatlamning Blending rejimi `Screen` yoki `Color Dodge` ga o'tkaziladi — natijada chetlari mayin shaffoflashuvchi jozibador radial qalqon paydo bo'ladi.

### 3-topshiriq. 3 bosqichli dinamik Health Bar paneli (qiyin)
O'yinda qahramonning joni to'laligidan to kritik holatgacha pasayishini bitta Gradient bilan ifodalovchi progress bar dizaynini yaratmoqchisiz:
- Jon 100% da — Yashil;
- Jon 50% da — Sariq;
- Jon 10% da — Qizil.
Gradient Editor orqali ushbu 3 rangli mayin o'tuvchi chiziqli gradiyentni qanday sozlash kerak?

**Yechim:**
1. `Gradient Editor` ochiladi va `Linear Gradient` tanlanadi.
2. Pastki rang chizig'ida 3 ta rang to'xtash nuqtasi (Color Stops) joylashtiriladi:
   - 1-nuqta (Location: 0%): Qizil rang (`#FF1122`);
   - 2-nuqta (Location: 50%): Sariq rang (`#FFCC00`);
   - 3-nuqta (Location: 100%): Yashil rang (`#22CC44`).
3. Yuqori shaffoflik nuqtalari (Opacity Stops) barcha nuqtalarda 100% saqlanadi.
4. UI qatlamida to'rtburchak shakl chizilib, ushbu gradiyent chapdan o'ngga tortiladi.
5. O'yin dasturida jon kamaygan sari chiziq o'ng tomondan qisqarib boradi: yashil zonadan sariqqa, undan so'ng qizil kritik zonaga o'tadi.

---

## Tezkor nazorat savollari

1. Dizaynerlar uchun eng qulay bo'lgan HSB modelidagi harflar qanday ma'noni anglatadi?
   - *Javob:* Hue (Tus/burchak 0-360°), Saturation (To'yinganlik 0-100%), Brightness (Yorqinlik 0-100%).
2. Eyedropper Tool (I) ning o'yin dizayneriga beradigan asosiy foydasi nima?
   - *Javob:* Xolstdagi yoki internetdan olingan tayyor namunadagi rangni bir zumda aniq nusxalab olish imkonini beradi.
3. Markazdan tashqariga doira shaklida tarqaluvchi gradiyent turi qanday ataladi?
   - *Javob:* Radial Gradient (Aylanma gradiyent).
4. Photoshopda yig'ilgan maxsus ranglar palitrasini fayl sifatida eksport qilish formati qaysi?
   - *Javob:* `.aco` (Adobe Color Swatch).

---

## Keng tarqalgan xatolar va ularning oldini olish

- **Gradiyentda "Kir kulrang" zona paydo bo'lishi:** O'quvchilar ko'pincha komplementar ranglar (masalan, qizil va yashil) o'rtasida to'g'ridan-to'g'ri gradiyent tortishadi. Ikki qarama-qarshi rang o'rtasida muqarrar ravishda xira iflos kulrang zona paydo bo'ladi. Buning oldini olish uchun ularning o'rtasiga qo'shimcha sariq yoki olovrang oraliq rang qo'yish kerak.
- **Ko'p rangli tartibsizlik (Swatches ishlatmaslik):** Bitta o'yin sahnasidagi o'nlab elementlar har xil tasodifiy ranglarga bo'yaladi. Har doim ish boshlashdan oldin Swatches panelida 4-5 ta rangdan iborat bitta rasmiy guruh ochilishi va faqat shu ranglardan foydalanilishi shart.
- **Gradiyent qadamlarining ko'rinib qolishi (Color Banding):** Agar juda katta 4K xolstda juda yaqin ranglar orasida gradiyent tortilsa, mayin o'tish o'rniga pog'onali chiziqlar (chiziq-chiziq chandiqlar) paydo bo'ladi. Buni yo'qotish uchun gradiyent ustiga 1% `Noise` (shovqin) filtri qo'shiladi yoki 16-bit rang chuqurligi tanlanadi.
