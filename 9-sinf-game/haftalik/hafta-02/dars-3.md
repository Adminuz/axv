# 6-dars. Photoshop interfeysi va vositalari (2-qism): Tanlash vositalari, qatlamlar va uskunalar

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga Adobe Photoshop dasturidagi tanlash vositalari (Marquee, Lasso, Magic Wand / Quick Selection), chizish va tahrirlash asboblari (Brush, Eraser, Pen, Shape, Gradient), qatlamlar (Layers) ierarxiyasi, destruktiv bo'lmagan tahrirlash — qatlam maskalari (Layer Masks) hamda aralashtirish rejimlari (Blending Modes)dan foydalanib o'yin assetlari tayyorlashni o'rgatish.
- **Kutiladigan natija:** O'quvchilar murakkab shakldagi o'yin obyektlarini fondan ajrata oladi; qatlamlar va maskalar bilan buzilmasdan (non-destructive) ishlay oladi; Blending Modes orqali o'yin sahnasiga yorug'lik va soyalar bera oladi.
- **Vaqt taqsimoti:**
  - O'tgan mavzuni takrorlash (2D grafika turlari va Canvas): 10 daqiqa
  - Yangi mavzu: Tanlash vositalari (Marquee, Lasso, Wand): 20 daqiqa
  - Chizish vositalari: Brush, Pen, Shape va Gradient: 25 daqiqa
  - Qatlamlar, Maskalar va Blending Modes amaliyoti: 15 daqiqa
  - Nazorat savollari va dars xulosasi: 10 daqiqa

---

## Mentor konspekti

### 1. Tanlash vositalari (Selection Tools)
O'yin obyektlarini kesib olish, fondan ajratish yoki ma'lum bir sohani bo'yash uchun tanlash vositalari ishlatiladi:
1. **Marquee Tool (M):** To'rtburchak (`Rectangular`) va aylanma (`Elliptical`) aniq geometrik sohalarni tanlash.
   - *Shift* bosib turilsa — mukammal kvadrat yoki doira hosil bo'ladi.
2. **Lasso Tool (L):**
   - *Lasso (Erkin):* Qo'lda erkin chizib tanlash.
   - *Polygonal Lasso:* To'g'ri chiziqli qirralar (burchakli toshlar, binolar) uchun.
   - *Magnetic Lasso:* Ranglar kontrasti bo'ylab obyekt chetiga magnitdek o'zi yopishib boruvchi aqlli vosita.
3. **Magic Wand va Quick Selection Tool (W):**
   - *Magic Wand:* Bir xil rangdagi barcha piksellarni bitta bosishda tanlaydi (Tolerance parametri orqali sezgirligi sozlanadi). Bir rangli fonni 1 soniyada yo'qotish uchun eng qulay.
   - *Quick Selection:* Cho'tka kabi yurgizilganda obyekt shaklini avtomatik aniqlaydi.

### 2. Chizish va shakl vositalari
- **Brush Tool (B):** Asosiy rasm chizish vositasi.
  - *Size (O'lcham):* `[` va `]` tugmalari orqali tezkor o'zgartiriladi.
  - *Hardness (Qattiqlik):* 0% (mayin tumanli) dan 100% gacha (o'tkir qirrali).
  - *Opacity va Flow:* Shaffoflik darajasi.
- **Pen Tool (P):** Bezye egri chiziqlari (Bezier curves) orqali o'ta aniq vektor konturlar chizish vositasi. O'yin logotiplari va silliq piktogrammalar uchun eng professional asbob.
- **Shape Tool (U):** To'rtburchak, aylana, yulduzcha va maxsus vektor shakllar (o'yin tugmalari va ramkalar uchun).
- **Gradient Tool (G):** Ranglarning biridan ikkinchisiga mayin o'tishi (Linear, Radial). O'yin osmoni yoki sehrli qalqon effektlari uchun zarur.

### 3. Qatlamlar (Layers) va Maskalar (Layer Masks)
- **Qatlam qoidasi:** Har bir yangi element (qahramon tanasi, quroli, soyasi) yangi qatlamda bo'lishi shart (`Ctrl + Shift + N`).
- **Nega Eraser (o'chirg'ich) o'rniga Maskadan foydalanish kerak?**
  - O'chirg'ich bilan o'chirsangiz, piksellar butunlay yo'qoladi (Destruktiv tahrir).
  - **Layer Mask (Qatlam niqobi):** Qatlamga oq-qora niqob ulaydi.
    - *Qora cho'tka bilan bo'yalsa:* Obyekt ko'rinmay qoladi (yashirinadi);
    - *Oq cho'tka bilan bo'yalsa:* Yashiringan obyekt qayta paydo bo'ladi!
    - Hech qanday ma'lumot yo'qolmaydi (Non-destructive editing).

### 4. Aralashtirish rejimlari (Blending Modes)
Qatlamlarning bir-biriga ta'sir qilish usuli:
- **Multiply:** Tasvirni qoraytiradi (soya va kir effektlari uchun);
- **Screen:** Tasvirni yoritadi (olov, lazer, sehrli nur va chaqmoqlar uchun);
- **Overlay:** Kontrastni kuchaytiradi (tekstura va rang to'yinganligi uchun).

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Oq fondan o'yin qahramonini ajratish (oson)
Oq fonda turgan 2D robot rasmi berilgan.
Magic Wand (W) yoki Quick Selection vositasi yordamida robotni oq fondan qanday qilib 3 ta qadamda ajratib olib, yangi shaffof qatlamga o'tkazish mumkin?

**Yechim:**
1. `Magic Wand Tool (W)` tanlanadi va oq fonga bosiladi (barcha oq piksellar tanlanadi).
2. Klaviaturada `Ctrl + Shift + I` (Invert Selection) bosiladi — endi fon emas, robotning o'zi tanlangan bo'ladi.
3. `Ctrl + J` bosiladi — robot avtomatik ravishda alohida shaffof qatlamga ko'chiriladi.

### 2-topshiriq. Layer Mask bilan olov effektini yaratish (o'rta)
O'yin qahramoni qo'liga sehrli qilich tutqazilgan. Qilich tig'idan asta-sekin alangalanuvchi olov chiqishi kerak.
O'chirg'ich ishlatmasdan, qanday qilib Layer Mask va Gradient yordamida olovning qilich tutqichiga tutashgan joyini mayin shaffof holatga keltirish mumkin?

**Yechim:**
1. Olov rasmi qilich qatlamining ustiga joylashtiriladi.
2. Olov qatlamiga `Add Layer Mask` tugmasi bosilib, niqob ulanadi.
3. `Gradient Tool (G)` tanlanadi: rang rejimi qora-oq qilinadi.
4. Niqob ustida tutqichdan tig' tomon chiziq tortiladi: qora qismi olov boshini mayin yo'qotadi, oq qismi esa tig'dagi olovni to'liq qoldiradi.

### 3-topshiriq. Blending Modes bilan o'yinda tungi chiroq yaratish (qiyin)
Kunduzgi o'rmon sahnasi berilgan. Uni tunda qahramonning qo'lidagi mash'ala (fonar) yorug'ligida ko'rinadigan qilib o'zgartirmoqchisiz.
Qatlamlar va Blending Modes yordamida ushbu yorug'lik effektini qanday bajarasiz?

**Yechim:**
1. Sahnaning ustiga to'q ko'k rang bilan to'ldirilgan yangi qatlam ochiladi va uning rejimi `Multiply` (yoki Opacity 70%) qilinadi — butun sahna tunga aylanadi.
2. Uning ustidan yana bitta bo'sh qatlam ochilib, rejimi `Screen` yoki `Color Dodge` ga o'tkaziladi.
3. Yumshoq (Hardness 0%) sariq-olovrang `Brush (B)` olinadi va qahramon mash'alasi joylashgan nuqtaga bitta katta bosiladi.
4. *Natija:* `Screen` rejimi tungi qora qatlamni yorib o'tib, daraxtlar va yo'l ustiga realistik tilla rang nur taratadi.

---

## Tezkor nazorat savollari

1. Photoshopda obyektni tanlashni teskarisiga o'girish (Invert Selection) tezkor tugmasi qaysi?
   - *Javob:* `Ctrl + Shift + I` (Mac'da `Cmd + Shift + I`).
2. Nima uchun professional dizaynerlar o'chirg'ich (Eraser) o'rniga Layer Mask ishlatishadi?
   - *Javob:* Chunki Layer Mask piksellarni yo'qotmaydi, xato bo'lsa oq cho'tka bilan istalgan vaqtda qayta tiklash mumkin (Non-destructive).
3. Qaysi Blending Mode yorug'lik va chaqnash effektlari uchun eng yaxshi natija beradi?
   - *Javob:* Screen (yoki Color Dodge / Linear Dodge).
4. Mo'yqalam (Brush) o'lchamini klaviaturada qaysi tugmalar bilan tezkor o'zgartirish mumkin?
   - *Javob:* `[` (kichraytirish) va `]` (kattalashtirish).

---

## Uyga vazifa

Kompyuterda (yoki daftarda sxematik tarzda):
1. O'yin bosh qahramoni uchun 3 ta qatlamdan iborat loyiha tuzing:
   - 1-qatlam: Qahramon soyasi (Yerda);
   - 2-qatlam: Qahramon tanasi va libosi;
   - 3-qatlam: Qahramon qo'lidagi qurol yoki qalqon.
2. Layer Mask qanday ishlashini o'z so'zlaringiz bilan 3 ta jumlada tushuntiring.
