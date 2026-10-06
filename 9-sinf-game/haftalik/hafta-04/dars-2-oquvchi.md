# 11-dars. Sprayt va ikonka tushunchasi, formatlar (PNG, SVG)

> Yurak belgisini ko'rgan har bir o'yinchi «bu jon» deb biladi — bir so'z ham o'qimasdan. Bugun o'yinlarning «tili» bo'lgan ikonkalar va spraytlar bilan tanishamiz va birinchi ikonkamizni yaratamiz.

## Dars xulosasi

- **Ikonka** — interfeysda ma'lumot yoki harakatni ifodalovchi kichik rasm (jon, sozlamalar, savatcha).
- **Ikonka turlari:** axborot, interaktiv, o'yin (buyum), uslubiy, bezak, navigatsiya.
- **Sprayt** — o'yin olamidagi 2D tasvir: personaj, obyekt yoki fon; **statik** yoki **animatsion** bo'ladi.
- **Rastr** — piksellardan (kattalashtirilsa xiralashadi); **vektor** — shakllardan (sifat yo'qolmaydi).
- **PNG** — shaffof, sifatli rastr; spraytlar va o'yin ikonkalari uchun asosiy format.
- **SVG** — vektor; masshtablanadigan UI ikonkalar uchun.
- **GIF** — oddiy animatsiya, 256 rang.
- **JPG** — shaffoflik yo'q, sprayt uchun yaramaydi.
- **Vositalar:** Photoshop, Aseprite, Piskel (brauzerda, bepul); animatsiya — Spine, DragonBones.
- **Bepul kutubxonalar:** OpenGameArt, Kenney, CraftPix, Itch.io — **litsenziyani** albatta o'qing.

## Qo'shimcha ma'lumot

### 1. Ikonka yoki sprayt?

| | Ikonka | Sprayt |
|---|---|---|
| Qayerda | interfeysda (UI) | o'yin olamida |
| Vazifa | ma'lumot, tugma | qahramon, obyekt, fon |
| Animatsiya | kam | ko'pincha |

Tanga o'yin olamida aylansa — sprayt; ekranning burchagida «tangalar soni» yonida tursa — ikonka.

### 2. Qaysi format?

- Qahramonning yurish kadrlari → **PNG**.
- Har qanday ekranda keskin bo'lishi kerak bo'lgan menyu belgisi → **SVG**.
- Menyudagi kichik aylanuvchi yulduzcha (veb-o'yin) → **GIF**.
- Fon fotosurat → **JPG**.

### 3. Yaxshi ikonkaning 4 qoidasi

1. Oddiy, aniq **siluyet**.
2. 32×32 px da ham **tanilishi**.
3. To'plamda **bir xil uslub**: kontur qalinligi, yorug'lik yo'nalishi, palitra.
4. Ma'nosi **bir xil**: bitta o'yinda «sozlamalar» doim bitta belgi.

### 4. Photoshop'da ikonka: qisqa yo'riqnoma

1. New: 128×128 px, **Transparent**.
2. **Custom Shape Tool (U)** → Shape rejimi → shakl tanlash → Shift bilan chizish.
3. Fill — palitradan rang, Stroke — 4 px to'q kontur.
4. Yangi qatlam → **Clipping Mask** → yuqori chapga yumshoq yorug'lik.
5. **File → Export → Export As → PNG**, Transparency ✓.

### 5. Fayl nomlash

`ikon_tanga_64.png`, `sprayt_qahramon_idle_32.png` — tur, nom, o'lcham; bo'sh joysiz va lotin harflarida.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Ikonka** | Interfeysdagi ma'lumot yoki harakat belgisi |
| **Sprayt** | O'yin olamidagi 2D tasvir yoki animatsiya |
| **Rastr grafika** | Piksellardan iborat tasvir |
| **Vektor grafika** | Matematik shakl va chiziqlardan iborat tasvir |
| **Piksel** | Rastr tasvirning eng kichik nuqtasi |
| **Shaffoflik (alpha)** | Tasvirning ko'rinmas (orqasi ko'rinadigan) qismi |
| **PNG** | Shaffoflikni qo'llaydigan sifatli rastr format |
| **SVG** | Masshtablanadigan vektor format |
| **GIF** | 256 rangli, animatsiyani qo'llaydigan format |
| **Asset** | O'yinda ishlatiladigan tayyor resurs (rasm, ovoz, model) |
| **Litsenziya** | Assetdan foydalanish shartlari (CC0, CC-BY) |
| **Custom Shape Tool** | Photoshop'da tayyor vektor shakllarni chizish asbobi |

## Bilasizmi?

- «Sprayt» (sprite) so'zi inglizchada «parisi, kichik ruh» degan ma'noni bildiradi — ekranda «uchib yuruvchi» kichik rasmlar uchun shu nom berilgan.
- 1997-yilgi Quake o'yini spraytlar o'rniga to'liq uch o'lchovli modellardan foydalangan — bu 3D o'yinlar davrining boshlanishi edi.
- Kenney saytidagi minglab assetlar CC0 litsenziyasida — ularni hatto tijoriy o'yinlarda ham bepul ishlatish mumkin.
- SVG fayli aslida matn (XML): uni Bloknotda ochib, ichidagi koordinatalarni o'qish mumkin.

## Topshiriqlar

### 1. Ikonka turini aniqlang · oson
Turini yozing: yurak (jon), tishli g'ildirak, qilich, kompas strelkasi, ramka naqshi.

**Kutiladigan natija:** 5 ta to'g'ri javob.

### 2. Ikonka yoki sprayt? · oson
Sevimli o'yiningizdan 3 ta ikonka va 3 ta spraytni toping va ajratib yozing.

**Kutiladigan natija:** 6 qatorli ro'yxat.

### 3. Formatni tanlang · oson
To'rt holat uchun format tanlang: yurish kadrlari, menyu belgisi, menyudagi kichik animatsiya, fon fotosurat.

**Kutiladigan natija:** PNG, SVG, GIF, JPG va sabablar.

### 4. Rastr va vektor · oson
Bitta oddiy shaklni Photoshop'da Brush bilan va Shape bilan chizing, 800% ga kattalashtirib solishtiring.

**Kutiladigan natija:** 2 ta skrinshot va 2 jumla xulosa.

### 5. Tanga ikonkasi · o'rta
128×128 px shaffof hujjatda tanga ikonkasini chizing (doira, kontur, belgi, yorug'lik) va PNG ga eksport qiling.

**Kutiladigan natija:** `ikon_tanga_128.png` shaffof fonda.

### 6. Custom Shape bilan jon ikonkasi · o'rta
Custom Shape Tool dan yurak shaklini olib, 10-dars palitrangiz ranglarida jon ikonkasini yarating.

**Kutiladigan natija:** `ikon_jon_128.png`.

### 7. Asset kutubxonasi · o'rta
OpenGameArt yoki Kenney saytidan bitta sprayt paketini toping va uning litsenziyasini, formatlarini va muallifini yozing.

**Kutiladigan natija:** paket nomi, litsenziya, format, muallif.

### 8. Piskel bilan tanishuv · o'rta
Piskel (brauzerda) da 16×16 px kalit ikonkasini chizing va PNG ga eksport qiling.

**Kutiladigan natija:** `ikon_kalit_16.png`.

### 9. 4 ikonkali to'plam · qiyin
Bir uslubdagi 4 ikonka yarating: jon, tanga, kalit, sozlamalar. Kontur qalinligi va yorug'lik yo'nalishi bir xil bo'lsin.

**Kutiladigan natija:** 4 ta PNG va umumiy ko'rinish skrinshoti.

### 10. Kichik o'lcham sinovi · qiyin
9-topshiriqdagi ikonkalarni 128, 64 va 32 px da eksport qiling. Qaysi biri 32 px da yomon taniladi va uni qanday soddalashtirdingiz?

**Kutiladigan natija:** 12 ta fayl va 3–4 jumla tahlil.

### 11. Format taqqoslash · qiyin
Bitta ikonkani PNG, JPG va GIF formatlarida saqlang va fayl hajmi, shaffoflik va sifatini jadvalda taqqoslang.

**Kutiladigan natija:** 3 qatorli jadval va xulosa.

### 12. HUD ikonkalar paneli · bonus
O'yin ekranining yuqori qismi uchun HUD panelini yarating: jon, tanga soni, mana va pauza tugmasi ikonkalari bilan.

**Kutiladigan natija:** 1920×200 px PNG panel.

## O'zingizni tekshiring

1. Ikonka va sprayt nimasi bilan farq qiladi?
2. Ikonkalarning 6 turini sanab bering.
3. Rastr va vektor grafikaning farqi nima?
4. Nega spraytlar uchun PNG eng ko'p ishlatiladi?
5. SVG qachon qulay?
6. Piskel va Aseprite nima uchun kerak?
7. Bepul kutubxonadan asset olishda nimaga e'tibor berasiz?

## Uyga vazifa

O'z o'yiningiz uchun bir uslubdagi 4 ta ikonka (jon, tanga, kalit, sozlamalar) yarating, 10-dars palitrasidan foydalaning va ularni 64 va 32 px o'lchamlarda shaffof PNG ga eksport qiling. Batafsil: `uyga-vazifa.md`.
