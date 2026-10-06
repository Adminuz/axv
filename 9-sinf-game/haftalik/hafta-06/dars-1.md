# 16-dars. UI dizayn: tugmalar, menyular, HUD (3-qism): Jonli o'yin HUD'i (Health bar, tangalar, mini-xarita)

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga HUD ning vazifasini va tarkibini (sog'liq paneli, tangalar/ballar, mini-xarita, vaqt, inventar), HUD ga qo'yiladigan talablarni (aniqlik, joylashuv, minimalizm, janrga moslik, vizual uslub) o'rgatish hamda Photoshop'da health bar, tanga hisoblagichi va mini-xaritadan iborat jonli o'yin HUD maketini chizishni mashq qildirish.
- **Kutiladigan natija:** O'quvchilar hUD ning 5 ta talabini va 4 ta asosiy elementini aytadi; health bar'ni 3 qatlamda (fon, to'ldirish, ramka) chizadi va to'ldirish uzunligini foizdan hisoblaydi; tanga hisoblagichini ikonka va matndan yig'adi; mini-xaritani Ellipse Tool bilan chizib, qahramon va dushman belgilarini joylashtiradi; hUD elementlarini guruhlaydi va shaffof fonli PNG qilib eksport qiladi.
- **Vaqt taqsimoti:**
  - 14–15-dars: tugma holatlari, menyular: 10 daqiqa
  - HUD: tarkibi va talablari: 10 daqiqa
  - Health bar va tanga hisoblagichi: 20 daqiqa
  - Mini-xarita, guruhlash, eksport: 15 daqiqa
  - Amaliyot: to'liq HUD maketi: 25 daqiqa

> Manba: o'quv dasturi — «UI dizayn: tugmalar, menyular, HUD» moduli («HUD tushunchasi, unga qo'yilgan talablar va o'yinlarda vazifasi»); o'quv qo'llanma — 2.4-bo'lim («2.6-jadval. HUD tarkibi», HUD talablari, Photoshop'da UI yaratish bosqichlari: 1920×1080, Transparent fon, har element alohida layerda); uslubiy ko'rsatma — 1.4–1.5-mashg'ulotlar (Rectangle/Ellipse Tool, Blending Options, Ctrl+G, tanga ikonkasi, Export). Piksel o'lchamlari va rang chegaralari (yashil/sariq/qizil) — namunaviy tavsiya, mentor o'zgartirishi mumkin.

---

## Mentor konspekti

### 1. Jonli o'yin HUD'i: tarkibi va talablari

**HUD** (Head-Up Display) — o'yin davomida o'yinchiga zarur ma'lumotni doimiy ko'rsatadigan «ekran usti interfeysi». Qo'llanmadagi 2.6-jadvalga ko'ra HUD tarkibi: **sog'liq paneli** (HP — qahramonning sog'lig'i), **energiya/mana**, **xarita/minimap** (joylashuv va yo'nalish), **ball, statistika, resurslar** (masalan, tangalar), **qurol yoki inventar**, **vaqt yoki topshiriqlar**. Talablar: 1) **aniqlik va o'qilishi** — kontrast, tushunarli shrift va belgi; 2) **joylashuv** — odatda ekran burchaklarida, o'yinchi ko'rish maydoniga xalaqit bermaydi; 3) **minimalizm** — ortiqcha element yo'q; 4) **janrga moslik** — shooter'da minimal va tezkor, RPG'da batafsil; 5) **vizual uslub** — ranglar, ikonkalar va ramkalar o'yin uslubiga mos. Bugun «Robo-changyutkich» o'yinining HUD'ini chizamiz: chap yuqorida health bar, o'ng yuqorida tangalar, o'ng pastda mini-xarita.

```text
+--------------------------------------------------+
| [HP ########--] 80/100               COIN x 12   |
|                                                  |
|                                                  |
|                  O'yin sahnasi                   |
|                                                  |
|                                      +--------+  |
|                                      | mini-  |  |
|                                      | xarita |  |
|                                      +--------+  |
+--------------------------------------------------+
```

> Professional maslahat: Markaz bo'sh qoladi — o'yinchi sahnani ko'rishi kerak. HUD elementlari burchaklarga yig'iladi.

### 2. Health bar va tanga hisoblagichini chizish

Yangi hujjat: **File → New**, 1920×1080 px, RGB, **Background Contents → Transparent** — shunda HUD elementlari shaffof fonli bo'ladi (qo'llanma). Har element **alohida layerda** bo'ladi. **Health bar uch qatlamdan** iborat: 1) **Fon** — to'q kulrang Rounded Rectangle (masalan, 400×40 px); 2) **To'ldirish** — shu o'lchamdagi, rangli (qizil yoki yashil) shakl; 3) **Ramka** — Blending Options → Stroke yoki Properties panelidagi Stroke. To'ldirish uzunligi sog'liq foiziga bog'liq: **uzunlik = bar kengligi × HP / maksimal HP**. 400 px bar, HP 80/100 bo'lsa: 400 × 0,8 = **320 px**; 25/100 bo'lsa — 100 px. Bar yoniga yurak ikonkasi va «80/100» matni qo'yiladi (Text Tool). Tanga hisoblagichi: tanga ikonkasi (uslubiy ko'rsatmadagi kabi Move Tool bilan kerakli joyga) + «x 12» matni; ikkalasi Ctrl+G bilan bitta guruhga yig'ilib, «Tangalar» deb nomlanadi.

```text
Bar kengligi: 400 px, maksimal HP: 100

HP 100  ->  400 * 100 / 100 = 400 px
HP  80  ->  400 *  80 / 100 = 320 px
HP  50  ->  400 *  50 / 100 = 200 px
HP  25  ->  400 *  25 / 100 = 100 px

Rang: 50% dan ko'p - yashil
      25-50%      - sariq
      25% dan kam - qizil
```

> Professional maslahat: Rang almashishi — namunaviy tavsiya: o'yinchi sog'lig'i kamayganini rangdan darrov tushunadi.

### 3. Mini-xarita, guruhlash va eksport

**Mini-xarita** qahramonning atrofini ko'rsatadi, joylashuv va yo'nalishni bildiradi (qo'llanma: dushmanlar va joylarning o'rnini ko'rsatadi). Photoshop'da: **Ellipse Tool (U)** tanlanadi, **Shift** bosib turib sichqoncha tortiladi — mukammal doira hosil bo'ladi (uslubiy ko'rsatma); doira ichiga xarita fonini (to'q rang yoki xona tasviri) qo'ying, markazga qahramon belgisini (kichik och doira), atrofga dushman belgilarini (qizil nuqtalar) joylashtiring, ramka uchun Stroke bering. Joyi — o'ng pastki burchak. Keyin HUD qatlamlarini tartiblang: Shift bilan tanlab, **Ctrl + G** bilan guruhlang va nomlang: «HP», «Tangalar», «Mini-xarita», ularni esa umumiy «HUD» guruhiga soling. Eksport: **File → Export → Export As…** — **PNG** (shaffoflik saqlanadi). Qo'llanmaga ko'ra shaffof fonli HUD o'yin dvigateliga (masalan, Unity) Sprite sifatida import qilinadi.

```text
HUD
  HP
    Ikonka (yurak)
    Matn 80/100
    Bar ramka
    Bar to'ldirish
    Bar fon
  Tangalar
    Matn x 12
    Ikonka (tanga)
  Mini-xarita
    Qahramon belgisi
    Dushman belgilari
    Xarita fon
```

> Professional maslahat: Yuqori qatlam — ustida ko'rinadi: ramka to'ldirishdan, matn esa fondan tepada turishi kerak.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. HUD elementlari (oson)
HUD ning kamida 4 ta elementini sanang va har birining vazifasini yozing.

**Bajarish tartibi:**
Sog'liq paneli — qahramon sog'lig'ini ko'rsatadi; tanga/ball hisoblagichi — yig'ilgan resursni; mini-xarita — joylashuv va yo'nalishni; vaqt/inventar — topshiriq vaqti yoki qurol holatini.

### 2-topshiriq. Burchaklar (oson)
Health bar, tangalar va mini-xaritani ekranning qaysi burchaklariga qo'yasiz?

**Bajarish tartibi:**
Health bar — chap yuqori; tangalar — o'ng yuqori; mini-xarita — o'ng pastki. Markaz bo'sh qoladi.

### 3-topshiriq. Bar uzunligi (o'rta)
Bar kengligi 400 px. HP 60/100 va 35/100 bo'lsa, to'ldirish uzunligi qancha?

**Bajarish tartibi:**
400 × 60 / 100 = 240 px; 400 × 35 / 100 = 140 px.

### 4-topshiriq. Health bar chizish (o'rta)
Photoshop'da 400×40 px health bar'ni 3 qatlamda chizing.

**Bajarish tartibi:**
1) Rounded Rectangle 400×40 px, to'q kulrang — «Bar fon». 2) Shu o'lchamdagi rangli shakl — «Bar to'ldirish». 3) To'ldirish ustida Stroke qatlami yoki Blending Options → Stroke — «Bar ramka». Qatlamlar fon → to'ldirish → ramka tartibida joylashadi.

### 5-topshiriq. Tanga hisoblagichi (qiyin)
Tanga ikonkasi va «x 12» matnidan hisoblagich yig'ing, guruhlang va nom bering.

**Bajarish tartibi:**
Move Tool bilan tanga ikonkasini o'ng yuqoriga qo'ying; Text Tool bilan «x 12» yozing (o'lcham va rangni Properties panelida sozlang); ikkala qatlamni Shift bilan tanlab Ctrl + G bosing va guruhni «Tangalar» deb nomlang.

### 6-topshiriq. To'liq HUD (bonus)
Uchala elementdan iborat HUD'ni chizing, «HUD» guruhiga soling va shaffof PNG qilib eksport qiling.

**Bajarish tartibi:**
Ellipse Tool + Shift bilan mini-xarita doirasini chizing, qahramon (och) va dushman (qizil) belgilarini qo'ying; barcha guruhlarni «HUD» ga soling; File → Export → Export As… → PNG, Transparency yoqilgan.

---

## Tezkor nazorat savollari

1. HUD nima?
   - *Javob:* O'yin davomida doim ko'rinadigan ma'lumot — ekran usti interfeysi.
2. HUD ning 3 ta elementini ayting.
   - *Javob:* Masalan: sog'liq paneli, mini-xarita, tanga/ball hisoblagichi.
3. HUD talablaridan 3 tasi?
   - *Javob:* Aniqlik, burchaklarda joylashuv, minimalizm.
4. Health bar nechta qatlamdan iborat?
   - *Javob:* Uchta: fon, to'ldirish, ramka.
5. Shaffof fonli HUD qaysi formatda eksport qilinadi?
   - *Javob:* PNG.

---

## Uyga vazifa

1. 1920×1080 px, Transparent fonli hujjatda health bar'ni (fon, to'ldirish, ramka) chizing; HP 70/100 holatiga to'g'ri uzunlik hisoblang.
2. Tanga hisoblagichini (ikonka + «x 12») chizing va «Tangalar» guruhiga soling.
3. Mini-xaritani Ellipse Tool bilan chizing; qahramon va 2 ta dushman belgisini qo'ying.
4. Barcha qatlamlarni «HUD» guruhiga yig'ib, shaffof PNG qilib eksport qiling.
5. HUD joylashuvi haqida 3 gaplik izoh yozing: nima uchun elementlar aynan shu joylarda?
