# 11-dars. O'yin uchun ikonka va spraytlar yaratish (1-qism): Sprayt va ikonka tushunchasi, formatlar (PNG, SVG)

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga ikonka va sprayt tushunchalari, o'yinlardagi ikonkalar turlari va vazifalari, spraytlardan foydalanish sohalari (personaj, obyekt, fon), rastr va vektor grafika farqi, PNG, SVG va GIF formatlarining xususiyatlari, sprayt va ikonka yaratish vositalari (Photoshop, Aseprite, Piskel) hamda bepul asset kutubxonalari haqida bilim berish; Photoshop'da Custom Shape asosida birinchi vektor ikonkani yaratib, shaffof fonli PNG va SVG qilib eksport qilishni o'rgatish.
- **Kutiladigan natija:** O'quvchilar ikonka va spraytni farqlaydi; ikonkaning 6 turini misollar bilan aytadi; vazifaga qarab PNG, SVG yoki GIF ni tanlaydi; Photoshop'da 128×128 px ikonka chizadi va uni shaffof fon bilan PNG ga eksport qiladi; asset kutubxonalaridan foydalanishda litsenziyani tekshirish zarurligini tushunadi.
- **Vaqt taqsimoti:**
  - O'tgan mavzuni takrorlash (palitra, kulrang test): 10 daqiqa
  - Yangi mavzu: Ikonka va sprayt, turlari va vazifalari: 15 daqiqa
  - Rastr va vektor, PNG, SVG, GIF: 15 daqiqa
  - Vositalar va bepul kutubxonalar: 10 daqiqa
  - Amaliyot: Photoshop'da ikonka yaratish va eksport: 25 daqiqa
  - Xulosa: 5 daqiqa

> Manba: o'quv dasturi — «O'yin uchun ikonka va spraytlar yaratish» moduli: «Ikonka va spraytlar haqida umumiy tushuncha. Sprayt va ikonka yaratishda dasturiy vositalar. O'yinlardagi ikonkalarning turlari va vazifalari ... Kutubxonalar. Photoshopda ikonkalar. PNG, SVG, GIF formatlari»; o'quv qo'llanma — 2.3-bo'lim (ikonkalar turlari, spraytlar, Aseprite, Piskel, Spine, DragonBones, 2.4-jadval «Spraytlarning bepul kutubxonalari», PNG/SVG/GIF tavsifi, Custom Shape).

---

## Mentor konspekti

### 1. Ikonka nima?

**Ikonka** — interfeysda obyekt, harakat yoki ma'lumotni ifodalovchi kichik grafik rasm (piktogramma). O'yinda ikonkalar o'yinchiga uzun matnni o'qimasdan tez tushunish va harakat qilish imkonini beradi.

Nima uchun muhim (o'quv qo'llanma):
- **Tez tushunish** — yurak belgisi «jon» ekanini o'yinchi bir zumda biladi.
- **Ixchamlik** — murakkab tushuncha kichik joyda ko'rsatiladi.
- **Til to'sig'ini kamaytirish** — yaxshi ikonka har qanday tildagi o'yinchiga tushunarli.

### 2. O'yinlardagi ikonkalar turlari

| Tur | Vazifasi | Misol |
|---|---|---|
| **Axborot** | O'yinchi holati yoki dunyo haqida xabar | jon (yurak), chidamlilik, mini-xarita belgisi |
| **Interaktiv** | Bosiladigan tugma va elementlar | do'kon savatchasi, sozlamalar (tishli g'ildirak), pauza |
| **O'yin (buyum)** | O'yin buyumlari | qilich, zelye, kalit, tanga |
| **Uslubiy** | O'yinning vizual uslubini belgilaydi | minimalistik, realistik, multfilm uslubi |
| **Bezak** | Funksiyasiz, interfeysni chiroyli qiladi | ramka burchaklari, yulduzchalar |
| **Navigatsiya** | Olam yoki menyuda mo'ljal olish | strelka, kompas, «chiqish» belgisi |

Yaxshi ikonka qoidalari: **oddiy siluyet**, kichik o'lchamda ham tanilishi (32×32 da tekshiring), bitta to'plamda **bir xil uslub, qalinlik va palitra** (10-dars palitrasi).

### 3. Sprayt nima?

**Sprayt** — 2D o'yinda qahramon, obyekt, fon va boshqa elementlarni ifodalovchi ikki o'lchovli tasvir yoki animatsiya. Spraytlar **statik** (tanga, daraxt) yoki **animatsion** (yuruvchi qahramon — bir nechta kadr) bo'ladi.

Qo'llanish:
- **Personajlar** — qahramon va dushmanlar (Super Mario Bros dagi Mario, Luidji);
- **Obyektlar** — tanga, qurol, bonus;
- **Fon** — daraxt, tog', bino, taylsetlar.

| | Ikonka | Sprayt |
|---|---|---|
| Qayerda | UI (interfeys) qatlamida | o'yin olamida |
| Vazifa | ma'lumot berish, bosish | o'yin obyektini ko'rsatish, harakatlanish |
| Animatsiya | kamdan-kam | ko'pincha (kadrlar) |

### 4. Rastr va vektor

- **Rastr grafika** — piksellardan iborat (Photoshop, Aseprite). Kattalashtirilsa, «zinapoya» va xiralik paydo bo'ladi. Murakkab rangli detallar uchun qulay.
- **Vektor grafika** — matematik chiziq va shakllardan iborat (Illustrator, Figma, Photoshop Shape qatlamlari). Istalgan o'lchamga sifat yo'qotmasdan kattalashtiriladi. Oddiy UI ikonkalar uchun qulay.

### 5. Formatlar: PNG, SVG, GIF

| Format | Turi | Shaffoflik | Animatsiya | O'yinda qayerda |
|---|---|---|---|---|
| **PNG** | rastr, sifatni yo'qotmasdan siqish | to'liq (alpha kanal) | yo'q (oddiy PNG) | qahramon, obyekt, tugmalar, sprayt sheet; Unity, Godot, Unreal yaxshi qo'llab-quvvatlaydi |
| **SVG** | vektor (matnli XML fayl) | bor | (CSS/JS bilan) | menyu ikonkalari, sozlamalar belgisi, mini-xarita belgilari, veb-o'yinlar UI |
| **GIF** | rastr, 256 rang | faqat «bor/yo'q» (yarim shaffof emas) | bor | menyudagi kichik animatsiyalar, veb-o'yinlardagi sodda effektlar |
| JPG (taqqoslash uchun) | rastr, sifat yo'qotib siqish | yo'q | yo'q | fotosurat fonlar; sprayt uchun **yaramaydi** (shaffoflik yo'q) |

Asosiy qoida: **sprayt va o'yin ichidagi ikonka → PNG**, **masshtablanadigan UI ikonka → SVG**, **oddiy animatsion belgi → GIF**.

### 6. Vositalar

**Grafik muharrirlar:**
- **Photoshop** — kuchli rastr muharrir + vektor shakllar; batafsil spraytlar, teksturalar, UI.
- **Aseprite** — piksel grafika va animatsiya uchun mashhur (pullik, ochiq kodini o'zi yig'ish mumkin).
- **Piskel** — brauzerda ishlaydigan bepul piksel sprayt muharriri (piskelapp.com).

**Animatsiya dasturlari:**
- **Spine** — skelet (suyak) animatsiyasi, murakkab 2D personajlar uchun;
- **DragonBones** — Spine ga o'xshash bepul vosita.

### 7. Bepul asset kutubxonalari

| Sayt | Nima bor | Formatlar |
|---|---|---|
| OpenGameArt | spraytlar, taylsetlar, qahramonlar, fonlar | PNG, GIF, SVG, ba'zan PSD |
| Kenney Assets | platformer paketlari, UI elementlar | PNG, SVG, PSD |
| CraftPix (Freebies) | RPG qahramonlar, UI, effektlar | PNG, PSD |
| Itch.io (assets) | turli mualliflar to'plamlari | PNG, GIF, PSD |

**Muhim:** har bir assetning **litsenziyasini** o'qing (masalan, CC0 — erkin; CC-BY — muallifni ko'rsatish shart). Muallifni ko'rsatmasdan foydalanish — mualliflik huquqini buzish.

### 8. Photoshop'da birinchi ikonka (128×128 px)

1. **File → New**: Width 128, Height 128 px, Resolution 72, Background Contents — **Transparent**.
2. **Custom Shape Tool** (U, Shape asboblari ichida): yuqori panelda **Shape** rejimi, Shapes ro'yxatidan yurak/yulduz/qalqon shaklini tanlang va chizing (Shift — proporsiya saqlanadi).
3. **Fill** — 10-dars palitrasidan asosiy rang; **Stroke** — 4 px to'q kontur.
4. Hajm berish: yangi qatlam → **Clipping Mask** (Alt + bosish) → yumshoq oq cho'tka bilan yuqori chap tomonga yorug'lik dog'i (yorug'lik manbai — yuqori chapda).
5. Kichik o'lchamda tekshirish: **View → 100%** va `Image Size` nusxasida 32×32 — ikonka hali taniladimi?
6. **Eksport PNG:** File → Export → **Export As...** → Format: **PNG**, **Transparency** belgilangan → `ikon_jon_128.png`.
7. **Eksport SVG:** Shape qatlami ustida o'ng tugma → **Export As...** → SVG (yangi versiyalarda SVG tanlovi bo'lmasa, Illustrator yoki Figma'da qayta chizish tavsiya etiladi).

Nomlash qoidasi: `tur_nom_o'lcham` → `ikon_tanga_64.png`, `sprayt_qahramon_idle_32.png` (bo'sh joysiz, lotin harflarida).

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Ikonka turini aniqlang (oson)
Turini aniqlang: yurak belgisi (jon), tishli g'ildirak (sozlamalar), qilich (inventar), kompas strelkasi, ramka burchagidagi naqsh.

**Yechim:**
Yurak — axborot; tishli g'ildirak — interaktiv; qilich — o'yin (buyum); kompas — navigatsiya; naqsh — bezak.

### 2-topshiriq. Formatni tanlang (oson)
Mos formatni tanlang va sababini ayting: (a) qahramonning shaffof fonli yurish kadrlari; (b) har qanday ekranda keskin ko'rinishi kerak bo'lgan menyu ikonkasi; (c) bosh menyudagi kichik aylanuvchi tanga animatsiyasi (veb-o'yin); (d) fon uchun fotosurat.

**Yechim:**
(a) PNG — shaffoflik, sifat, o'yin dvijoklari qo'llaydi; (b) SVG — vektor, sifat yo'qolmaydi; (c) GIF — oddiy animatsiya; (d) JPG (yoki PNG) — fotosurat, shaffoflik kerak emas.

### 3-topshiriq. Shaffof fonli ikonka (o'rta)
Photoshop'da 128×128 px shaffof hujjatda «tanga» ikonkasini yarating: doira, kontur, ichida belgi, yorug'lik dog'i. PNG ga eksport qiling.

**Yechim:**
1. New → 128×128, Transparent.
2. Ellipse Tool (U) + Shift: 110×110 doira, Fill `#F4C430`, Stroke 4 px `#8A5A00`.
3. Ichki kichik doira (Stroke, Fill yo'q) va Text yoki Custom Shape bilan yulduz belgisi.
4. Yangi qatlam → Clipping Mask → yuqori chapda oq yumshoq cho'tka (Opacity 40%).
5. Export As → PNG, Transparency ✓ → `ikon_tanga_128.png`. Tekshirish: fayl istalgan fonga qo'yilganda oq to'rtburchak ko'rinmaydi.

### 4-topshiriq. Kichik o'lcham sinovi va to'plam (qiyin)
Bir uslubdagi 4 ta ikonka to'plamini yarating (jon, tanga, kalit, sozlamalar). Ularni 128, 64 va 32 px o'lchamlarda eksport qiling. Qaysi biri 32 px da yomon taniladi va qanday soddalashtirasiz?

**Yechim:**
- Bir xil kontur qalinligi (128 px da 4 px), bir xil yorug'lik yo'nalishi, bitta palitra.
- Export As oynasida Scale (100%, 50%, 25%) yoki Image Size orqali 3 o'lcham.
- Odatda kalit va sozlamalar 32 px da «bo'tqa» bo'ladi: mayda tishlar va detallar olib tashlanadi, siluyet qalinlashtiriladi, kontur 2 px qoldiriladi. Xulosa: ikonka eng kichik o'lchamda ham tanilishi kerak.

---

## Tezkor nazorat savollari

1. Ikonka va sprayt farqi nima?
   - *Javob:* Ikonka — UI dagi ma'lumot/harakat belgisi; sprayt — o'yin olamidagi 2D obyekt yoki personaj (ko'pincha animatsion).
2. Ikonkalarning 6 turini ayting.
   - *Javob:* Axborot, interaktiv, o'yin (buyum), uslubiy, bezak, navigatsiya.
3. Nega sprayt uchun JPG yaramaydi?
   - *Javob:* JPG shaffoflikni qo'llamaydi va siqishda sifat yo'qotadi; PNG shaffof va sifatli.
4. SVG ning asosiy afzalligi nima?
   - *Javob:* Vektor — istalgan o'lchamga sifat yo'qotmasdan kattalashtiriladi, fayl yengil.
5. Bepul kutubxonadan asset olishda nimani tekshirish shart?
   - *Javob:* Litsenziyani (CC0, CC-BY va h.k.) va muallifni ko'rsatish talabini.

---

## Keng tarqalgan xatolar va ularning oldini olish

- **Oq fon bilan eksport:** hujjat Transparent emas yoki JPG tanlangan — ikonka atrofida oq to'rtburchak paydo bo'ladi.
- **Juda ko'p detal:** 128 px da chiroyli, 32 px da tanib bo'lmaydi — siluyetni soddalashtiring.
- **Har xil uslub:** bir to'plamda turli kontur qalinligi va yorug'lik yo'nalishi — qoidalarni oldindan belgilang.
- **Fayl nomlari:** `Untitled-1.png`, `yangi rasm.png` — nomlash qoidasidan foydalaning.
- **Litsenziyani o'qimaslik:** kutubxonadagi assetni muallifsiz ishlatish.
