# 12-dars. O'yin uchun ikonka va spraytlar yaratish (2-qism): Personaj va obyektlar uchun spraytlar chizish

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga spraytlarni yaratish bosqichlarini (uslub va o'lchamni aniqlash, eskiz va siluyet, cheklangan palitra bilan asosiy ranglar, soya va yorug'lik, kontur, eksport va test) Photoshop'da piksel-art usulida amalda bajarishni o'rgatish; personaj va obyekt spraytlarining xususiyatlari, piksel to'r (grid) bilan ishlash, Pencil Tool, Nearest Neighbor interpolyatsiyasi va oddiy 2 kadrli animatsiya (idle) tushunchasini berish.
- **Kutiladigan natija:** O'quvchilar 32×32 px qahramon spraytini va 16×16 yoki 32×32 px obyekt spraytini (tanga, zelye, sandiq) 10-dars palitrasida chizadi; siluyet testi va kulrang testdan o'tkazadi; spraytni sifat yo'qotmasdan (Nearest Neighbor) kattalashtirib, shaffof PNG ga eksport qiladi; nafas olish (idle) animatsiyasining 2 ta kadrini tayyorlaydi.
- **Vaqt taqsimoti:**
  - O'tgan mavzuni takrorlash (ikonka turlari, PNG/SVG): 10 daqiqa
  - Yangi mavzu: Sprayt yaratish bosqichlari, personaj va obyekt: 15 daqiqa
  - Photoshop'ni piksel-art uchun sozlash: 10 daqiqa
  - Amaliyot: qahramon spraytini bosqichma-bosqich chizish: 25 daqiqa
  - Obyekt spraytlari va 2 kadrli idle animatsiya: 15 daqiqa
  - Xulosa: 5 daqiqa

> Manba: o'quv dasturi — «O'yin uchun ikonka va spraytlar yaratish» moduli: «Spraytlarni yaratish bosqichlari ... Personaj va obyektlar uchun spraytlar», «Photoshopda ikonkalar yasash (HP, coin va boshqalar)»; o'quv qo'llanma — 2.3-bo'lim, «Spraytlarni yaratish bosqichlari» (uslub va o'lcham — «retro o'yin uchun 32x32 pikselli spraytlar mos keladi», eskiz — «qalam» vositasi, detallar va rang — «chegaralangan ranglar palitrasi», soya va yorug'lik, animatsiya kadrlari, «PNG yoki GIF formatida eksport qiling va ... sinab ko'ring»). Sprayt sheet (atlas) va optimallashtirish — 13-dars mavzusi.

---

## Mentor konspekti

### 1. Personaj va obyekt spraytlari

| | Personaj spraytlari | Obyekt spraytlari |
|---|---|---|
| Misollar | qahramon, dushman, NPC | tanga, zelye, sandiq, kalit, platforma |
| Asosiy talab | xarakter, tanilishi, harakat holatlari (idle, yurish, sakrash) | bir qarashda vazifasi tushunilishi |
| Animatsiya | deyarli doim | ko'pincha oddiy (aylanish, yaltirash) yoki yo'q |
| Rang | eng yuqori kontrast va to'yinganlik | vazifaga ko'ra rang kodlash (oltin — tanga, qizil — jon) |

### 2. Sprayt yaratishning 6 bosqichi (o'quv qo'llanma asosida)

1. **Uslub va o'lcham.** Retro platformer uchun qahramon **32×32 px**, mayda obyektlar **16×16 px**. Barcha spraytlar bitta masshtabda bo'lishi shart.
2. **Siluyet va eskiz.** Avval bitta to'q rang bilan **siluyet** (soyaning shakli): bosh, tana, qo'l-oyoq, o'ziga xos detal (shlyapa, qilich). Siluyet qora rangda ham tanilsa — dizayn yaxshi.
3. **Asosiy ranglar (flat).** 10-darsdagi palitradan, har bir qism uchun bitta rang: teri, kiyim, soch, qurol. Qahramon uchun **4–6 rang** yetarli.
4. **Soya va yorug'lik.** Yorug'lik manbai — **yuqori chapda** (barcha spraytlarda bir xil). Har rangga bitta soya (pastki o'ng) va bitta yorug'lik (yuqori chap) pog'onasi — hue shifting bilan (10-dars).
5. **Kontur (outline).** 1 px to'q kontur — spraytni fondan ajratadi. Qora o'rniga obyektning eng to'q rangidan foydalanish yumshoqroq ko'rinish beradi.
6. **Eksport va test.** Shaffof PNG, o'yin foniga qo'yib tekshirish, kattalashtirib ko'rish.

### 3. Photoshop'ni piksel-art uchun sozlash

- **Yangi hujjat:** 32×32 px, 72 ppi, Background — **Transparent**. Ko'rish uchun 800–1600% ga yaqinlashtiring (`Ctrl + +`).
- **Piksel to'ri:** Edit → Preferences → **Guides, Grid & Slices** → Gridline Every: **1 pixel**, Subdivisions: 1; so'ng View → Show → **Grid** (`Ctrl + '`).
- **Pencil Tool** (B guruhida, `Shift + B` bilan almashtiriladi) — **Size 1 px**, qattiq chet. Brush Tool emas: u chetlarni yumshatib, «xira» piksellar hosil qiladi.
- **Eraser Tool** (E) — Mode: **Pencil**, 1 px.
- **Paint Bucket** (G) — **Anti-alias o'chirilgan**, Contiguous yoqilgan.
- **Interpolyatsiya:** Edit → Preferences → General → Image Interpolation: **Nearest Neighbor (preserve hard edges)**. Image Size bilan kattalashtirishda ham Resample: **Nearest Neighbor** tanlanadi — piksellar keskin qoladi.

### 4. Piksel-art qoidalari

- **Bir piksel — bir qaror:** har bir piksel ataylab qo'yiladi.
- **«Jaggies» dan qoching:** chiziq bo'laklari bir tekis o'zgarsin (2-2-2 yoki 3-2-1), tartibsiz zinapoyalar emas.
- **Orphan piksellar** (yolg'iz, hech narsaga ulanmagan piksel) — shovqin, o'chiring.
- **Doubles** — kontur 2 px qalinlashib qolgan joylar; 1 px ga tushiring.
- **Kam rang:** qahramon uchun 4–6, butun sahna uchun 16–32 rang.

### 5. Qahramon spraytini chizish: namuna (32×32)

```
Qatlamlar (pastdan yuqoriga):
  01_siluyet   - to'q ko'k-binafsha, keyin yashiriladi
  02_flat      - asosiy ranglar
  03_soya      - soyalar (Clipping Mask)
  04_yoruglik  - yorug'lik dog'lari (Clipping Mask)
  05_kontur    - 1 px kontur
```

Nisbat (chibi/retro uslub): bosh ~ 12 px, tana ~ 10 px, oyoqlar ~ 8 px, tepada va pastda 1 px bo'sh joy. Ko'zlar — 1×2 px oq va to'q piksellar.

### 6. Obyekt spraytlari

- **Tanga (16×16):** oltin doira, 1 px to'q-jigarrang kontur, yuqori chapda 2–3 px oq yaltiroq, o'rtada belgi.
- **Zelye (16×16):** shisha idish siluyeti, ichida rangli suyuqlik (qizil — jon, moviy — mana), oq aks.
- **Sandiq (32×32):** jigarrang yog'och, oltin temir qoplamalar, qulf — o'yinchiga «ochish mumkin» signalini beradi.

Obyektlar personajdan **oddiyroq** va ko'pincha **kamroq to'yingan** bo'ladi (bonuslardan tashqari).

### 7. Oddiy animatsiya: idle (nafas olish) — 2 kadr

1. Tayyor qahramon qatlamlarini guruhlang → guruhni nusxalang (`Ctrl + J`).
2. 2-kadrda tanani va boshni **1 px pastga** siljiting (Move Tool, `↓` strelka), oyoqlar joyida qoladi.
3. **Window → Timeline** → **Create Frame Animation** → 1-kadrda 1-guruh ko'rinadi, **Duplicate frame** → 2-kadrda 2-guruh.
4. Har kadr vaqti: **0.5 sec**, Looping: **Forever**. Play bilan tekshiring.
5. Eksport: kadrlarni alohida PNG (`sprayt_qahramon_idle_01.png`, `_02.png`) yoki **File → Export → Save for Web (Legacy) → GIF** — namoyish uchun.

Kelgusi darsda (13-dars) kadrlar **sprayt sheet (atlas)** ga yig'iladi.

### 8. Eksport va test

- **Export As → PNG**, Transparency ✓; masshtab 100% (o'yin dvijoki o'zi kattalashtiradi) va prezentatsiya uchun 800% (Nearest Neighbor bilan).
- **Fon testi:** spraytni 10-dars lokatsiya fonida tekshiring — kulrang testdan o'tadimi?
- **Masshtab testi:** barcha spraytlar yonma-yon: tanga qahramondan kattami? Proporsiyalar to'g'rimi?

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Siluyet testi (oson)
Uch xil qahramon g'oyasi uchun 32×32 px da faqat bitta to'q rang bilan siluyet chizing (ritsar, sehrgar, robot). Sinfdoshingiz siluyetga qarab kimligini topa oladimi?

**Yechim:**
Ritsar — dubulg'a pati va qalqon; sehrgar — uchli shlyapa va tayoq; robot — to'rtburchak bosh va antenna. Har biriga bitta o'ziga xos «chiqib turgan» detal kerak — u kichik o'lchamda tanilishni ta'minlaydi. Sinfdosh 3 dan 3 ni topsa — siluyetlar muvaffaqiyatli.

### 2-topshiriq. Photoshop sozlamalari (oson)
32×32 px piksel-art hujjatini tayyorlang: shaffof fon, 1 px grid, Pencil 1 px, Nearest Neighbor interpolyatsiya.

**Yechim:**
File → New (32×32, Transparent) → Preferences → Guides, Grid & Slices (Gridline Every 1 px, Subdivisions 1) → View → Show → Grid → Pencil Tool (Shift + B), Size 1 px → Preferences → General → Image Interpolation: Nearest Neighbor. Tekshirish: 1 px chizilganda chetlari xira emas, to'liq kvadrat.

### 3-topshiriq. Qahramon spraytini 5 qatlamda chizish (o'rta)
1-topshiriqdagi siluyetlardan birini tanlab, 10-dars palitrasidan 5–6 rang bilan to'liq spraytga aylantiring: flat, soya, yorug'lik (yuqori chapdan), kontur. Qatlamlarni nomlang.

**Yechim:**
1. `01_siluyet` ustida `02_flat`: teri, kiyim, soch, aksessuar — har biri bitta rang (Pencil, Paint Bucket Anti-alias o'chiq).
2. `03_soya` (Clipping Mask): pastki o'ng tomonlarga hue shifting soyalar.
3. `04_yoruglik`: yuqori chap qirralarga 1 px yorug'lik.
4. `05_kontur`: 1 px kontur, doubles va orphan piksellar tozalanadi.
5. `01_siluyet` yashiriladi. Kulrang testda qahramon fondan ajraladi; Export As → PNG `sprayt_qahramon_idle_32.png`.

### 4-topshiriq. Obyektlar to'plami va idle animatsiya (qiyin)
16×16 px da 3 ta obyekt (tanga, jon zelyesi, kalit) chizing va qahramoningiz uchun 2 kadrli idle animatsiyani Timeline'da yarating. Natijani GIF ko'rinishida saqlang.

**Yechim:**
- Obyektlar: bir xil kontur rangi va yorug'lik yo'nalishi, rang kodlash (oltin, qizil, kumush/oltin).
- Idle: guruh nusxasi, tana va bosh 1 px pastga, Timeline → Create Frame Animation, 2 kadr × 0.5 s, Forever.
- File → Export → Save for Web (Legacy) → GIF, Transparency ✓, Image Size 800% (Nearest Neighbor) → `qahramon_idle.gif`.
Tekshirish: qahramon «nafas olayotgandek» yumshoq tebranadi, oyoqlar sakramaydi.

---

## Tezkor nazorat savollari

1. Retro o'yin uchun qahramon spraytining odatiy o'lchami qancha?
   - *Javob:* 32×32 piksel (mayda obyektlar 16×16).
2. Nima uchun avval siluyet chiziladi?
   - *Javob:* Qahramon shakli rangsiz ham tanilishini tekshirish uchun.
3. Piksel-artda nega Brush emas, Pencil Tool ishlatiladi?
   - *Javob:* Pencil qattiq chetli piksel qo'yadi; Brush chetlarni yumshatib xira piksellar hosil qiladi.
4. Spraytni kattalashtirganda qaysi interpolyatsiya tanlanadi?
   - *Javob:* Nearest Neighbor — piksellar keskin saqlanadi.
5. Barcha spraytlarda yorug'lik manbai qayerda bo'lishi kerak?
   - *Javob:* Bir xil joyda, odatda yuqori chapda.

---

## Keng tarqalgan xatolar va ularning oldini olish

- **Brush Tool bilan chizish:** xira chetlar — Pencil va Anti-alias o'chiq ishlating.
- **Bicubic bilan kattalashtirish:** sprayt loyqa bo'ladi — Nearest Neighbor.
- **Juda ko'p rang va gradient:** 32 px da shovqin — 4–6 rang yetarli.
- **Har xil yorug'lik yo'nalishi:** bir spraytda chapdan, boshqasida o'ngdan — sahna «buziladi».
- **Masshtab buzilishi:** tanga qahramondan katta — barcha spraytlarni yonma-yon tekshiring.
- **Oq fonda saqlash:** Transparent hujjat va PNG/GIF Transparency ni tekshiring.
