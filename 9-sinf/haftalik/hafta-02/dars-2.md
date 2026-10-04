# 5-dars. Wireframe tushunchasi va Balsamiq dasturiga kirish

**Hafta:** 2 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliyot (dizayn vositasi) · **I-bob**, 5-dars

## 1. Dars rejasi

**Maqsad:** o'quvchi interfeysni loyihalashda Wireframe'ning o'rni va ahamiyatini tushunadi, past aniqlikdagi (Low-fidelity) karkas yaratish tamoyillarini o'rganadi, Balsamiq dasturining asosiy interfeysi va asboblari yordamida birinchi raqamli wireframe'ni chiza oladi.

**Kutiladigan natija:**
- Wireframe tushunchasini, uning eskiz (sketch), mockup va prototipdan farqini tushuntiradi.
- Nega wireframe boshlang'ich bosqichda rangsiz (monoxrom) bo'lishi kerakligini asoslab beradi.
- Balsamiq ishchi muhiti (Canvas, UI Library, Quick Add, Inspector) bilan ishlay oladi.
- Asosiy UI elementlarni (Container, Button, Text, Image placeholder, Input) to'g'ri joylashtiradi.
- Mobil yoki veb-sahifaning 1 ta ekrani uchun toza Low-fi wireframe yaratadi va PNG/PDF formatida eksport qiladi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 | Takrorlash | 4-dars (Ssenariy, User Flow, CJM) |
| 10–30 | Yangi mavzu 1 | Wireframe nima? Low-fi vs High-fi, nega rangsiz chizamiz? |
| 30–40 | Yangi mavzu 2 | Balsamiq bilan tanishuv: "qo'lda chizilgan" uslub falsafasi |
| 40–45 | Tanaffus | |
| 45–55 | Yangi mavzu 3 | Balsamiq elementlar kutubxonasi va Quick Add |
| 55–75 | Amaliyot | "Mobile_Book" bosh sahifasi wireframe'ini Balsamiqda yaratish |
| 75–80 | Tezkor nazorat va xulosa | 5 ta savol, xulosa |

**Vositalar:** Balsamiq Cloud (bepul demo/trial brauzerda: balsamiq.cloud) yoki qog'oz va marker/qalam. O'rnatish shart emas.

---

## 2. Konspekt

### 2.1. Takrorlash (10 daqiqa)
- User Flow bizga nima berdi? (Foydalanuvchi qaysi ekranlar orqali yurishini ko'rsatdi).
- Endi har bir ekranning ichida nimalar qanday joylashishini chizish vaqti keldi!

### 2.2. Wireframe nima?
**Wireframe** (so'zma-so'z: "simli karkas") — bu veb-sahifa yoki mobil ilova ekranining strukturasini, elementlarning joylashuvini va axborot ierarxiyasini ko'rsatuvchi sodda, vizual skeletdir.

Taqqoslash:
- Bino qurishda birinchi bo'lib pardalarning rangi yoki devor gulqog'ozi tanlanmaydi — avval poydevor, xonalarning o'lchami va eshik-romlarning o'rni chizilgan **chizma (cherteoj)** tayyorlanadi.
- Wireframe — dasturiy ta'minotning aynan shu arxitektura chizmasidir.

### 2.3. Aniqlik darajalari (Fidelity)
1. **Low-fidelity (Past aniqlikdagi):**
   - Oddiy qog'ozdagi chizma yoki oq-qora raqamli bloklar;
   - Aniq shrift, rang yoki haqiqiy rasmlar yo'q;
   - Rasmlar o'rniga ichiga "X" chizilgan to'rtburchak qo'yiladi;
   - Maqsad: g'oyani 5 daqiqada sinab ko'rish va tuzilmani kelishib olish.
2. **High-fidelity (Yuqori aniqlikdagi):**
   - Haqiqiy ranglar, shriftlar, sifatli fotosuratlar;
   - Figma yoki Sketch dasturlarida yaratiladi;
   - Tayyor dasturdan deyarli farq qilmaydi.

**Nega boshida ranglardan qochish kerak?**
Agar mijozga yoki jamoaga boshidanoq rangli dizayn ko'rsatilsa, hamma e'tiborini "Tugmaning qizil rangi menga yoqmadi" yoki "Rasm chiroyli emas" kabi ikkinchi darajali narsalarga qaratadi. Natijada eng muhim narsa — interfeysning qulayligi va mantiqiy tuzilishi e'tibordan chetda qoladi!

### 2.4. Balsamiq dasturi va uning falsafasi
**Balsamiq** — dunyoda eng mashhur tezkor wireframe yaratish vositasidir.
Uning o'ziga xosligi shundaki, uning barcha elementlari ataylab **daftar varag'iga qalam bilan qo'lda chizilgandek (sketch/hand-drawn)** ko'rinadi.

Balsamiq'ning afzalliklari:
1. **Piksel ketidan quvmaslik:** Siz chiziqlarni mikronigacha tekislashga vaqt sarflamaysiz, butun diqqat kontentda bo'ladi.
2. **Tezlik:** 10 daqiqada butun boshli ilova maketini chizib chiqish mumkin.
3. **Quick Add:** Shunchaki klaviaturadan nom yozib (masalan, `Button` yoki `Image`) istalgan elementni darhol ekranga tushirish mumkin.

### 2.5. Balsamiqning asosiy UI elementlari
- **Container / Browser / Smartphone:** Ekran ramkasi.
- **Heading / Label / Paragraph:** Sarlavha va matn bloklari.
- **Button:** Tugmalar.
- **TextInput:** Kiritish maydonchalari.
- **Image:** Ichida "X" bo'lgan to'rtburchak (rasm o'rni).
- **Icon:** Standart piktogrammalar (qidiruv lupasi, savatcha, profil).

---

## 3. Amaliy topshiriqlar

### 1-topshiriq. "Mobile_Book" Bosh ekrani wireframe'i
Balsamiq dasturida (yoki qog'ozda) mobil kitob ilovasining bosh sahifasini chizing.
Elementlar:
1. Telefon ramkasi (Smartphone container);
2. Yuqorida sarlavha va Profil ikonasi;
3. Qidiruv qatori (Search Input);
4. "Ommabop kitoblar" bloki (2 ta kitob muqovasi va nomi);
5. Pastki navigatsiya paneli (Bosh sahifa, Qidiruv, Kutubxona).

**Yechim (tuzilma tavsifi va eskiz):**
```
┌──────────────────────────────┐
│ [≡]   Mobile_Book        (O) │  <-- Header va profil
├──────────────────────────────┤
│ [ 🔍 Kitob nomini yozing... ] │  <-- Qidiruv paneli
├──────────────────────────────┤
│ Ommabop kitoblar             │  <-- Bo'lim sarlavhasi
│ ┌─────────┐   ┌─────────┐    │
│ │    X    │   │    X    │    │  <-- Kitob muqovalari
│ │  Rasm   │   │  Rasm   │    │
│ └─────────┘   └─────────┘    │
│ Kvant fiz.    O'tkan kunlar  │
│ ★ 4.8         ★ 4.9          │
├──────────────────────────────┤
│                              │
│ ┌──────────────────────────┐ │
│ │  Yangi qo'shilganlar...  │ │
│ └──────────────────────────┘ │
├──────────────────────────────┤
│ [🏠 Asosiy]  [🔍 Qidiruv] [📚]│  <-- Bottom Navigation Bar
└──────────────────────────────┘
```

### 2-topshiriq. Kitob tafsilotlari ekrani
Kitob bosilganda ochiladigan sahifaning Low-fi wireframe'ini tuzing:
- Orqaga qaytish tugmasi (`<`);
- Katta kitob rasmi (Image placeholder);
- Kitob nomi va muallifi;
- 3 ta statistik blok (Betlar soni, Hajmi, Tili);
- Qisqa annotatsiya matni;
- Katta "Mutolaa qilish / Yuklab olish" tugmasi.

**Yechim:**
Ekranning yuqori qismida markazlashgan muqova, pastida 3 ustunli qisqa ma'lumotlar bloki va ekranning eng quyi qismida to'liq eni bo'ylab joylashgan asosiy harakat tugmasi (CTA Button).

---

## 4. Tezkor nazorat (5 daqiqa)

1. Wireframe nima va uning arxitekturadagi o'xshashi nima?
   - **Javob:** Bu interfeysning vizual karkasi/skeleti; binoning chizmasi (cherteoj)ga o'xshaydi.
2. Low-fidelity va High-fidelity wireframe farqi nimada?
   - **Javob:** Low-fi — oddiy, tezkor, oq-qora tuzilma; High-fi — ranglar, shriftlar va haqiqiy rasmlar bilan boyitilgan aniq dizayn.
3. Nega wireframe yaratishda dastlab ranglardan foydalanilmaydi?
   - **Javob:** E'tibor ranglarga chalg'imay, interfeysning tuzilishi, mantiqi va qulayligiga qaratilishi uchun.
4. Balsamiq dasturining boshqa dizayn dasturlaridan asosiy farqi nima?
   - **Javob:** Uning elementlari qalamda qo'lda chizilgandek ko'rinadi va piksel ketidan quvmasdan tez loyihalashga undaydi.
5. Wireframe'da rasm o'rni qanday belgilanadi?
   - **Javob:** Ichiga diagonal "X" chizilgan to'rtburchak (Image placeholder) orqali.

---

## 5. Xulosa va keyingi darsga ko'prik
Bugun biz interfeys skeletini qurishni va Balsamiq dasturida dastlabki bloklarni joylashtirishni o'rgandik.
**Keyingi dars (6-dars):** Balsamiq va professional **Axure RP** vositasida murakkabroq komponentlar, navigatsiya menyulari va to'liq interfeys sxemalarini tuzishni o'rganamiz!
