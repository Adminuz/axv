# 15-dars. UI dizayn: tugmalar, menyular, HUD (2-qism): Bosh menyu, sozlamalar va pauza menyusi dizayni

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga menyu tushunchasini va menyu turlarini (asosiy menyu, sozlamalar menyusi, o'yin ichidagi pauza menyusi), gorizontal va vertikal menyularni, ikonka va matn uyg'unligini, rang va effektlarni qo'llashni o'rgatish; uslubiy ko'rsatma bo'yicha Photoshop'da START, Sozlamalar, Chiqish tugmalaridan iborat to'liq asosiy menyuni yaratish va eksport qilish.
- **Kutiladigan natija:** O'quvchilar uchta menyu turining vazifasini va tarkibini ayta oladi; 1920×1080 hujjatda MENU sarlavhasi, 3 ta tugma, Solid Color fon va bezak doiralaridan iborat bosh menyuni yaratadi; qatlamlarni guruhlaydi (`Ctrl + G`) va nomlaydi; sozlamalar yoki pauza menyusi eskizini tuzadi; natijani PNG/JPG qilib eksport qiladi.
- **Vaqt taqsimoti:**
  - Takrorlash (tugma turlari va holatlari): 10 daqiqa
  - Yangi mavzu: menyu tushunchasi va turlari, gorizontal/vertikal: 15 daqiqa
  - Ikonka va matn uyg'unligi, rang va effektlar: 10 daqiqa
  - Amaliyot: Photoshop'da bosh menyu (uslubiy ko'rsatma bo'yicha): 25 daqiqa
  - Amaliyot: pauza yoki sozlamalar menyusi, eksport: 15 daqiqa
  - Xulosa: 5 daqiqa

> Manba: o'quv dasturi — «Menyu turlari ... Photoshopda menyular dizayni. Gorizontal va vertikal menyular. Icon va matn uyg'unligi. Rang va effektlarni qo'llash»; o'quv qo'llanma — 2.4-bo'lim (menyu ta'rifi; Main Menu, Settings Menu, Pause Menu; «Menyular uchun panel dizayni, iconlar, matn joylashuvi va rang uyg'unligi ishlanadi. Har bir bo'lim (masalan, "Play", "Settings", "Exit") uchun alohida tugmalar ... yaratiladi»; 6-bosqich — guruhlash `Ctrl+G`); uslubiy ko'rsatma — 1.4-mashg'ulot (1.88–1.106-rasmlar: tugmani dublikat qilish, «Sozlamalar», «Chiqish» — qizil, Solid Color fon, MENU sarlavhasi, guruhlash, Ellipse Tool bezaklari, Export As). HUD batafsil — keyingi darslar.

---

## Mentor konspekti

### 1. Menyu nima?

O'quv qo'llanma: **Menyu** — foydalanuvchi o'yin imkoniyatlari orasida tanlov qiladigan tuzilma. U interfeysning **tashkiliy va navigatsion** qismi bo'lib, o'yinchi uchun boshqaruv tizimini ta'minlaydi.

### 2. Menyu turlari

| Tur | Qachon ochiladi | Tarkibi (namuna) |
|---|---|---|
| **Asosiy menyu (Main Menu)** | o'yin ishga tushganda | O'yinni boshlash, Sozlamalar, Chiqish |
| **Sozlamalar menyusi (Settings Menu)** | asosiy yoki pauza menyusidan | tovush, grafika, boshqaruv variantlari |
| **O'yin ichidagi menyu (Pause Menu)** | o'yin jarayonida (Esc / pauza tugmasi) | Davom etish, Sozlamalar, Bosh menyuga chiqish |

Bog'lanish: Main Menu → Settings → (Ortga) → Main Menu; O'yin → Pause → Davom etish → O'yin. Har ekranda **ortga yo'l** bo'lishi kerak.

### 3. Gorizontal va vertikal menyular

- **Vertikal menyu:** tugmalar ustma-ust, bir xil masofada. Bosh menyu va pauza uchun eng ko'p ishlatiladi — o'qish tartibi tepadan pastga, eng muhimi tepada.
- **Gorizontal menyu:** tugmalar yonma-yon. Bo'limlar (tablar) uchun qulay: sozlamalarda «Tovush | Grafika | Boshqaruv», do'konda kategoriyalar, pastki navigatsiya paneli (mobil).

### 4. Ikonka va matn uyg'unligi

- Ikonka matnni **to'ldiradi**, almashtirmaydi (yangi o'yinchi uchun matn aniqroq).
- Bir xil o'lcham, bir xil uslub (11-dars ikonkalari), ikonka matndan chapda, vertikal markazda.
- Bir xil masofa: ikonka — matn oralig'i barcha tugmalarda teng.
- Kichik ekranda faqat ikonka qolsa, u hammaga tanish bo'lsin (tishli g'ildirak — sozlamalar, uy — bosh menyu).

### 5. Rang va effektlar

- Fon — sokin (Solid Color yoki xira o'yin sahnasi), tugmalar — fondan ajraladi.
- Primary (START) — eng yorqin; Chiqish — qizil (uslubiy ko'rsatmada ham shunday), boshqalari — neytralroq.
- Effektlar (Layer Styles): Drop Shadow, Outer Glow, gradient — me'yorida.
- Pauza menyusida orqada **o'yin sahnasi xiralashtirilgan** yoki qorong'ilashtirilgan bo'ladi — o'yinchi qayerda to'xtaganini ko'radi.

### 6. Photoshop: bosh menyu (uslubiy ko'rsatma bo'yicha)

1. 14-darsdagi «O'yin menyusi» (1920×1080) hujjati: START tugmasi tayyor.
2. **Dublikat:** tugma shakli va matn qatlamini `Shift` bilan birga belgilab, Move Tool (V) bilan `Shift + Alt` bosib pastga suriladi — nusxa paydo bo'ladi.
3. Nusxa biroz kichraytiriladi, matni **«Sozlamalar»** ga o'zgartiriladi, Properties orqali matn o'lchami va shakl rangi o'zgartiriladi.
4. Yana dublikat → **«Chiqish»**, rangi **qizil**. Tugmalar **vertikal, bir xil masofada**.
5. **Fon:** Layers → yangi **Solid Color** (fill layer) → eng pastki qatlamga → mos rang.
6. **Sarlavha:** START matnini `Ctrl + J` bilan nusxalab, yuqoriga qo'yiladi, matni **«MENU»**, o'lchami kattaroq; qatlam Solid Color'dan yuqorida.
7. **Guruhlash:** shakllar va matnlar `Shift` bilan belgilanadi → `Ctrl + G` → guruh nomi **Main Menu** yoki **Buttons**.
8. Guruh Move Tool bilan markazga.
9. **Bezak:** Ellipse Tool (U), `Shift` bilan mukammal doira; kattalashtirish, rang; `Alt` bilan sudrab nusxalar.
10. **Eksport:** File → Export → **Export As** → PNG yoki JPG. Uslubiy ko'rsatma: JPG — hajm kichik, taqdimot va namoyish uchun qulay; o'yin ichida alohida elementlar (shaffof) — PNG.

### 7. Pauza menyusi (qo'shimcha amaliyot)

```
Pause Menu (Group)
  fon_xira       o'yin skrinshoti + Black qatlam, Opacity 60%
  panel          Rounded Rectangle, Stroke, Drop Shadow
  sarlavha       "PAUZA"
  btn_davom      Primary (yashil)
  btn_sozlama    oddiy
  btn_chiqish    qizil — "Bosh menyuga"
```

### 8. Sozlamalar menyusi eskizi

- Gorizontal tablar: **Tovush | Grafika | Boshqaruv**.
- Tovush: Musiqa va Effektlar uchun slayder (progress bar ko'rinishi), Grafika: sifat (Past/O'rta/Yuqori), to'liq ekran (on/off).
- Pastda: **Ortga** (Secondary) va **Saqlash** (Primary).

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Menyu turlari (oson)
Quyidagi tugmalar qaysi menyuga tegishli: «Davom etish», «Musiqa ovozi», «O'yinni boshlash», «Grafika sifati», «Bosh menyuga chiqish», «Chiqish».

**Yechim:**
Asosiy menyu: O'yinni boshlash, Chiqish. Sozlamalar: Musiqa ovozi, Grafika sifati. Pauza menyusi: Davom etish, Bosh menyuga chiqish. (Sozlamalar tugmasi asosiy va pauza menyusida ham bo'ladi.)

### 2-topshiriq. Bosh menyu (oson)
Uslubiy ko'rsatma bo'yicha START, Sozlamalar, Chiqish tugmalaridan iborat vertikal menyu yarating.

**Yechim:**
14-dars START tugmasi → Shift+Alt bilan 2 marta dublikat → matnlar «Sozlamalar», «Chiqish» → Chiqish rangi qizil → tugmalar orasidagi masofa teng (masalan, 40 px). Tekshirish: Align (Move Tool panelidagi Align horizontal centers) bilan markazlangan.

### 3-topshiriq. To'liq bosh menyu (o'rta)
2-topshiriqqa Solid Color fon, «MENU» sarlavhasi, 2 ta bezak doira qo'shing, guruhlang va PNG qilib eksport qiling.

**Yechim:**
1. Layer → New Fill Layer → Solid Color → eng pastga.
2. START matni Ctrl + J → yuqoriga → «MENU», ~120 pt.
3. Shakl va matnlar → Ctrl + G → nomi «Main Menu» → markazga.
4. Ellipse Tool + Shift → doira → Alt bilan nusxa → burchaklarga, fon rangidan biroz ochroq.
5. File → Export → Export As → PNG `bosh_menyu.png`. Tekshirish: sarlavha va tugmalar fondan aniq ajraladi.

### 4-topshiriq. Pauza menyusi (qiyin)
O'yin sahnasi ustida pauza menyusini yarating: xiralashtirilgan fon, panel, «PAUZA» sarlavhasi, 3 tugma (Davom etish — Primary, Sozlamalar, Bosh menyuga — qizil), ikonka + matn.

**Yechim:**
- Fon: o'yin skrinshoti (yoki 10-dars lokatsiyasi) + qora Solid Color, Opacity 60% (yoki Filter → Blur → Gaussian Blur).
- Panel: Rectangle, Corners 30 px, Stroke 4 px, Drop Shadow.
- Tugmalar: 14-dars uslubi; chap tomonda 11-dars ikonkalari (play, tishli g'ildirak, uy), ikonka–matn oralig'i teng.
- Guruh «Pause Menu», eksport PNG. Tekshirish: Davom etish — eng ko'zga tashlanadigan; Bosh menyuga — qizil va pastda.

---

## Tezkor nazorat savollari

1. Menyu nima?
   - *Javob:* O'yinchi o'yin imkoniyatlari orasida tanlov qiladigan tashkiliy va navigatsion tuzilma.
2. Uchta menyu turini ayting.
   - *Javob:* Asosiy (Main), Sozlamalar (Settings), O'yin ichidagi (Pause).
3. Vertikal va gorizontal menyu qachon ishlatiladi?
   - *Javob:* Vertikal — bosh va pauza menyusi; gorizontal — bo'limlar/tablar (sozlamalar, do'kon).
4. Uslubiy ko'rsatmada «Chiqish» tugmasi qaysi rangda?
   - *Javob:* Qizil.
5. Photoshop'da qatlamlar qanday guruhlanadi?
   - *Javob:* Shift bilan belgilab, Ctrl + G; guruhga nom beriladi.

---

## Keng tarqalgan xatolar va ularning oldini olish

- **Tugmalar orasidagi masofa har xil:** menyu tartibsiz — Align va teng oraliq.
- **Ortga yo'l yo'q:** Sozlamalardan chiqib bo'lmaydi — har ekranda Ortga.
- **Fon tugmalardan yorqin:** tugmalar yo'qolib qoladi — fon sokin.
- **Ikonka va matn uslubi har xil:** bir ikonka konturli, biri to'liq — bir uslubga keltiring.
- **Qatlamlar nomsiz:** «Rectangle 1 copy 3» — guruhlang va nomlang.
- **Pauza menyusida o'yin to'liq yashirilgan:** o'yinchi qayerda to'xtaganini unutadi — xira, lekin ko'rinadigan fon.
