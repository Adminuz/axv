---
title: "2-dars. Operatsion tizimlar va Windows muhitida ishlash"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "8-sinf (Foundation)", "link": "/8-sinf-cs/"}, "week": {"n": 1, "link": "/8-sinf-cs/hafta-01/"}, "g": 2, "title": "Operatsion tizimlar va Windows muhitida ishlash", "lead": "Kompyuterni yoqqaningizda ekranda jilvalanadigan chiroyli ish stoli va derazalar ortida qanday kuch turibdi? Ushbu darsda kompyuterning «boshqaruvchi yuragi» bo'lgan operatsion tizimlar, Windows 10/11 imkoniyatlari, oynalarni bo'lish va dasturlarni professional boshqarishni o'rganamiz.", "slide": "/slaydlar/8-sinf-cs/hafta-01/dars-2.html", "tabs": [{"g": 1, "link": "/8-sinf-cs/hafta-01/dars-1", "current": false}, {"g": 2, "link": "/8-sinf-cs/hafta-01/dars-2", "current": true}, {"g": 3, "link": "/8-sinf-cs/hafta-01/dars-3", "current": false}], "prev": {"g": 1, "title": "Zamonaviy kompyuterlar va ularning arxitekturasi", "link": "/8-sinf-cs/hafta-01/dars-1"}, "next": {"g": 3, "title": "Axborot o‘lchov birliklari va fayl turlari. Windows operatsion tizimida fayl hamda papkalar yaratish. Tezkor tugmalar (Hot keys)", "link": "/8-sinf-cs/hafta-01/dars-3"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Operatsion tizim (OT)** — kompyuter apparat qismlarini boshqaruvchi va inson bilan kompyuter o'rtasida qulay muloqotni ta'minlovchi asosiy tizim dasturi.
- **Asosiy OT turlari:** Shaxsiy kompyuterlar uchun — Windows, Linux, macOS; mobil telefonlar uchun — Android va iOS.
- **Windows interfeysi elementlari:** Ish stoli (Desktop), Vazifalar paneli (Taskbar), Start menyusi va Bildirishnomalar maydoni (System Tray).
- **Oynalarni boshqarish:** Har bir dastur alohida oynada ochiladi. `Win + Chapga/O'ngga strelka` orqali ekranni bir zumda 50/50 qilib bo'lish mumkin (Snap layouts).
- **Sozlamalar (Settings, Win+I):** Tizim parametrlari, ekran, shaxsiylashtirish va dasturlar ro'yxatini boshqaruvchi zamonaviy markaz.
- **Dasturlarni to'g'ri o'chirish:** Ish stolidagi yorliqni (Shortcut) o'chirish dasturni yo'qotmaydi; uni to'liq o'chirish uchun Sozlamalar orqali «Uninstall» amali bajarilishi shart.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### Operatsion tizim — kompyuter orkestri dirijyori
Tasavvur qiling: sizda ajoyib musiqachilar guruhi bor (barabanchi, skripkachi, pianinochi). Bular — protsessor, RAM, videokarta va qattiq disk. Lekin ular dirijyorsiz bir vaqtda qaysi notani chalishni bilishmaydi va tartibsizlik yuzaga keladi.
**Operatsion tizim** — bu aynan o'sha dirijyordir! U qaysi dasturga qancha operativ xotira berishni, qachon protsessor hisoblashi kerakligini va qachon ma'lumot diskka yozilishini nazorat qilib turadi.

### Nega Linux dasturchilar va serverlar orasida birinchi o'rinda?
Windows dunyo bo'yicha oddiy foydalanuvchilar orasida yetakchi bo'lsa-da, katta IT olamida — serverlar, bulutli xizmatlar (Google, Amazon) va superkompyuterlarda deyarli 100% **Linux** ishlatiladi.
Buning sabablari:
1. **Ochiq kodli (Open-source):** Linux bepul va uning kodini har kim ko'rishi, o'zgartirishi mumkin.
2. **Xavfsiz va barqaror:** U oylab, hatto yillab qayta yuklanmasdan to'xtovsiz ishlashi mumkin.
3. **Resurslarni kam talab qiladi:** Hatto eng kuchsiz eski kompyuterlarda ham yeldek uchadi.

### Windows Snap yordamida dasturchidek ishlash
Dasturlashni o'rganayotganda bir vaqtning o'zida ikkita oyna bilan ishlash juda qulay: bir tomonda darslik yoki YouTube videosi, ikkinchi tomonda esa kod yozish muharriri.
Buni qo'lda tortib to'g'rilab o'tirish shart emas:
- Birinchi oynani bosing va `Win + Chapga strelka` tugmalarini bosing.
- Ikkinchi oynani bosing va `Win + O'ngga strelka` tugmalarini bosing.
- Ekranning har ikki tomoni to'liq va teng qoplanadi. Bu usul vaqtingizni ikki baravar tejaydi!

### Odatiy xato: «Yorliq» (Shortcut) bilan haqiqiy dasturni adashtirish
Ko'pchilik o'quvchilar fleshkaga o'yin yoki dasturni nusxalamoqchi bo'lib, ish stolidagi yorliqni (burchagida kichkina qayrilgan o'q belgisi bor ikonka) ko'chirib olishadi. Uyga borib ochishsa, dastur ishlamaydi.
Sababi: **Yorliq (Shortcut)** — bu dasturning o'zi emas, balki uning kompyuter qattiq diskidagi manziliga eltuvchi «ko'rsatkich» xolos. Uni fleshkaga ko'chirsangiz, siz bor-yo'g'i 1 kilobaytlik manzilni ko'chirgan bo'lasiz, dasturning o'zi esa maktab kompyuterida qolib ketadi!

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Operatsion tizim (OT)** | Kompyuter apparat qismlarini boshqaruvchi va boshqa dasturlar ishlashini ta'minlovchi bosh dastur. |
| **GUI (Graphical User Interface)** | Grafik foydalanuvchi interfeysi — kompyuter bilan buyruqlar matni emas, balki oynalar, piktogrammalar va tugmalar orqali vizual muloqot qilish tizimi. |
| **Desktop (Ish stoli)** | Windows yuklangach ekranda paydo bo'ladigan, barcha asosiy elementlar joylashadigan ish maydoni. |
| **Taskbar (Vazifalar paneli)** | Ekranning pastki qismidagi Start tugmasi va ochiq ilovalar belgilarini ushlab turuvchi chiziq. |
| **Start menyusi** | Kompyuterdagi barcha dasturlar, sozlamalar va o'chirish buyruqlarini jamlagan asosiy menyu. |
| **Snap Layouts** | Windowsda oynalarni ekranning yarmi, to'rtdan biri qilib avtomatik yonma-yon joylashtirish mexanizmi. |
| **Settings (Sozlamalar)** | Kompyuterning ekran, internet, ovoz va ilovalarini sozlovchi zamonaviy boshqaruv oynasi (`Win + I`). |
| **Shortcut (Yorliq)** | Haqiqiy dastur yoki fayl manziliga tezkor yo'l ko'rsatuvchi belgi (ikonka). |
| **Uninstall** | Dasturni kompyuter xotirasidan, reestridan va fayllar tizimidan butunlay to'g'ri o'chirish jarayoni. |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

1. Dunyodagi eng birinchi Windows (Windows 1.0) 1985-yilda chiqarilgan bo'lib, uning hajmi 1 megabaytdan ham kichik bo'lgan va oddiy floppi disketaga sig'gan.
2. «Windows» operatsion tizimi o'z nomini aynan dasturlarning ekranda to'rtburchak «oynalar» (windows) ichida ochilishi sababli olgan.
3. Bugungi kunda dunyodagi eng tezkor 500 ta superkompyuterning **100 foizi** Linux operatsion tizimida ishlaydi!
4. Android operatsion tizimi ham aslida Linux yadrosi (kernel) asosiga qurilgan bo'lib, u har kuni 3 milliarddan ortiq faol smartfonlarda ishlaydi.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Operatsion tizimlarni saralash <Badge type="tip" text="oson" />
Quyidagi operatsion tizimlarni ikkita guruhga ajrating: **Kompyuterlar uchun (PC)** va **Mobil qurilmalar uchun (Mobile)**.
Ro'yxat: Windows 11, Android, macOS, iOS, Ubuntu Linux, iPadOS.
**Kutiladigan natija:** 6 ta OT daftarga ikkita alohida ustunda to'g'ri yoziladi.

### 2. Sozlamalar oynasini tezkor ochish <Badge type="tip" text="oson" />
Klaviaturadagi `Win + I` tugmalarini bosing. Ochilgan Sozlamalar oynasida qaysi asosiy bo'limlar (System, Bluetooth & devices, Network & internet va h.k.) borligini ko'ring va kamida 4 tasining nomini yozing.
**Kutiladigan natija:** 4 ta asosiy sozlama bo'limi nomi qayd etiladi.

### 3. Oynalarni boshqarish tugmalari <Badge type="tip" text="oson" />
Har qanday dastur oynasining yuqori o'ng burchagidagi 3 ta belgi (`-`, `□`, `X`) nima vazifani bajarishini aniq tushuntirib bering.
**Kutiladigan natija:** Minimize, Maximize/Restore va Close tugmalarining vazifasi yoziladi.

### 4. Barcha oynalarni bir zumda yashirish <Badge type="tip" text="oson" />
Bir vaqtning o'zida bir nechta dasturni (masalan, brauzer, kalkulyator, papka) oching. So'ngra `Win + D` tugmalarini bosing. Nima sodir bo'ldi? Yana bir marta `Win + D` bossangiz-chi?
**Kutiladigan natija:** `Win + D` barcha oynalarni yashirishi va qayta tiklashi tajribada tasdiqlanadi.

### 5. Snap layouts amaliyoti <Badge type="warning" text="o'rta" />
Kalkulyator dasturi (`calc`) va Bloknot (`notepad`) dasturini oching. Klaviaturadagi `Win + Chapga strelka` va `Win + O'ngga strelka` yordamida ularni ekranga teng 50/50 qilib yonma-yon joylashtiring.
**Kutiladigan natija:** Ekran teng ikkiga bo'lingan holda ikkala dastur bilan qulay ishlash holatiga keltiriladi.

### 6. Alt + Tab bilan tezkor sakrash <Badge type="warning" text="o'rta" />
Klaviaturada `Alt` tugmasini bosib turgan holda `Tab` tugmasini ketma-ket bosing. Ushbu qisqa klavish nimaga xizmat qilishini tushuntiring va uning afzalligini yozing.
**Kutiladigan natija:** Ochiq dasturlar o'rtasida sichqonchasiz tezkor almashish tajribasi tasvirlanadi.

### 7. Virtual ish stollari (Virtual Desktops) <Badge type="warning" text="o'rta" />
Klaviaturada `Win + Tab` tugmalarini bosing. Yuqori qismdagi «New desktop» (Yangi ish stoli) tugmasini bosib, 2-ish stolini yarating. Nima uchun bitta kompyuterda bir nechta virtual ish stoli kerak bo'lishi mumkin?
**Kutiladigan natija:** O'qish va o'yinlarni/shaxsiy ishlarni turli ish stollariga ajratish haqida 2-3 jumlalik xulosa.

### 8. Yorliq va asl fayl farqi <Badge type="warning" text="o'rta" />
Ish stolidagi dastur yorlig'ining (Shortcut) ustiga sichqonchaning o'ng tugmasini bosing va «Open file location» (Fayl joylashgan joyni ochish) bandini tanlang. Dasturning haqiqiy fayli qaysi papkada (masalan, `C:\Program Files\...`) joylashganini aniqlang.
**Kutiladigan natija:** Dasturning haqiqiy o'rnatilgan manzili to'liq yoziladi.

### 9. O'rnatilgan ilovalarni taftish qilish <Badge type="danger" text="qiyin" />
`Win + I` → Apps → Installed apps bo'limini oching. Kompyuteringizdagi dasturlarni o'lchami (Size) bo'yicha saralang. Eng ko'p disk maydonini egallagan 3 ta dasturni va ularning hajmini (GB yoki MB) aniqlang.
**Kutiladigan natija:** Eng og'ir 3 ta dastur va ularning aniq diski hajmi ro'yxati.

### 10. Operatsion tizimlar arxitekturasi tahlili <Badge type="danger" text="qiyin" />
Nima uchun telefonlar (Android va iOS) da kompyuterlar kabi to'g'ridan-to'g'ri `.exe` dasturlarni ochib bo'lmaydi? Ular o'rtasida qanday apparat va dasturiy farqlar mavjud?
**Kutiladigan natija:** Protsessor arxitekturasi (ARM va x86) hamda operatsion tizim talablari asosida tahlil.

### 11. Yangi OT o'rnatish: Dual-boot nima? <Badge type="info" text="bonus" />
Bitta kompyuterga bir vaqtning o'zida ham Windows, ham Linux (Ubuntu) operatsion tizimini o'rnatish mumkinmi? Bu tizim qanday nomlanadi va dasturchilarga qanday yordam beradi?
**Kutiladigan natija:** Dual-boot tushunchasi va kompyuterni yoqqanda qaysi OT ni tanlash menyusi chiqishi haqida izoh.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Operatsion tizim nima va u kompyuterda qanday vositachi vazifasini bajaradi?
2. Shaxsiy kompyuterlar uchun mo'ljallangan eng asosiy 3 ta OT qaysilar?
3. Windows ish stoli, vazifalar paneli va Start menyusi qanday elementlardan iborat?
4. Oynani ekranning yarmiga yoki to'rtdan biriga avtomatik joylashtirish uchun qaysi klavishlar bosiladi?
5. `Win + I` va `Win + E` tugmalari qaysi dastur/oynalarni ochadi?
6. Nega dasturni o'chirish uchun uning ish stolidagi yorlig'ini o'chirish yetarli emas?
7. Dasturchilar nima uchun Linux operatsion tizimini juda qadrlashadi?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. O'z kompyuteringizda quyidagi 4 ta klaviatura kombinatsiyasini sinab ko'ring va natijasini daftaringizga yozing:
   - `Win + I`
   - `Win + D`
   - `Alt + Tab`
   - `Win + Chapga / O'ngga strelka`
2. `Win + I` orqali Sozlamalarga kiring va kompyuteringizda o'rnatilgan 3 ta sevimli dasturingiz qancha disk hajmini (MB yoki GB) egallab turganini daftaringizga qayd eting.
Vazifani bajarishga 20 daqiqa vaqt ajrating.

</div>

