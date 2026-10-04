# 4-dars: Tinkercad.com virtual laboratoriyasida ro‘yxatdan o‘tish va interfeys

**Fan:** Internet of Things (IoT — Buyumlar Interneti)  
**Sinf:** 9-sinf  
**Hafta:** 2-hafta, 1-dars (umumiy 4-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga Tinkercad.com bulutli virtual laboratoriyasi haqida to'liq tushuncha berish, unda Autodesk akkaunti orqali ro'yxatdan o'tishni o'rgatish, Circuits (Sxemalar) ishchi muhiti interfeysi, navigatsiya, asboblar paneli va virtual simulyatsiya imkoniyatlarini amalda o'zlashtirish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- Virtual laboratoriyalarning apparat vositalarini xavfsiz sinash va o'rganishdagi afzalliklarini tushunish;
- Tinkercad platformasida ro'yxatdan o'tish va shaxsiy profilni sozlash;
- "Circuits" bo'limida yangi loyiha ochish, unga nom berish va saqlash;
- Ishchi maydon (Workplane) asboblari: burish (Rotate), o'chirish (Delete), bekor qilish (Undo/Redo), izoh qo'yish (Notes) vositalaridan foydalanish;
- Komponentlar kutubxonasini ko'rish, qidirish va turlari (Basic / All) bo'yicha saralash;
- "Start Simulation" va "Code" panellarining asosiy vazifalarini bilish.

---

## Kerakli jihozlar va vositalar

- Kompyuter yoki noutbuk (internetga ulangan);
- Veb-brauzer (Google Chrome, Firefox, Edge);
- O'quvchining shaxsiy elektron pochta manzili (Google yoki Autodesk akkaunt);
- Proyektor yoki monitor (namoyish uchun).

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va o'tgan mavzuni takrorlash | IoT arxitekturasi qatlamlari, sensorlar va aktuatorlar bo'yicha blits-savollar |
| **10–25 min** | Yangi mavzu bayoni: Virtual laboratoriya nima? | Tinkercad afzalliklari: xavfsizlik, narx, tez prototiplash, tutashuv simulyatsiyasi |
| **25–40 min** | Amaliy namoyish: Ro'yxatdan o'tish va profil yaratish | Tinkercad.com sayti, Autodesk ID, shaxsiy va talaba profillari |
| **40–60 min** | Interfeys bilan amaliy tanishuv | Circuits bo'limi, "Create new Circuit", Workplane, asboblar paneli va komponentlar |
| **60–75 min** | Mustaqil amaliy topshiriqlar | Yangi sxema ochish, komponentlarni joylashtirish, nomlash va ulashish havolasini olish |
| **75–80 min** | Xulosa va uyga vazifa | Asosiy xulosalarni mustahkamlash, keyingi dars anonsi |

---

## Nazariy ma'lumotlar

### 1. Nima uchun virtual laboratoriya kerak?

Elektronika va IoT ni o'rganishda yangi boshlovchilar tez-tez quyidagi muammolarga duch kelishadi:
- **Xatolik xavfi:** Simlarni noto'g'ri ulash natijasida qimmatbaho mikrokontrollerlar (Arduino, ESP32) yoki sensorlar yonib ketishi (qisqa tutashuv) mumkin;
- **Moddiy xarajat:** Har bir tajriba uchun yangi komponentlar, rezistorlar, o'lchov asboblari sotib olish katta mablag' talab qiladi;
- **Laboratoriya cheklovi:** Haqiqiy apparat faqat sinfda mavjud bo'lib, o'quvchi uyda amaliyot qila olmaydi.

**Tinkercad.com** (Autodesk kompaniyasi tomonidan yaratilgan) — bu brauzerda to'g'ridan-to'g'ri ishlaydigan, hech qanday dastur o'rnatishni talab qilmaydigan bepul 3D modellashtirish va virtual elektronika simulyatoridir. Tinkercad Circuits muhiti elektr zanjiridagi fizik jarayonlarni (kuchlanish, tok kuchi, komponentlarning haddan tashqari qizib tutashi) real vaqt rejimida hisoblab, animatsiya orqali ko'rsatib beradi.

### 2. Ro'yxatdan o'tish bosqichlari

1. **Saytga kirish:** `www.tinkercad.com` manziliga o'tiladi.
2. **Ro'yxatdan o'tish (Sign Up):**
   - Agar o'quvchi maktab guruhiga qo'shilayotgan bo'lsa: "Students with Class Code" orqali o'qituvchi bergan kodni kiritadi;
   - Mustaqil o'rganuvchi bo'lsa: "Create a personal account" tanlanadi.
3. **Akkaunt turi:** Google akkaunti orqali ("Sign in with Google") bitta tugma bilan tezkor kirish tavsiya etiladi.
4. **Boshqaruv paneli (Dashboard):** Chap menyuda "3D Designs", "Circuits", "Codeblocks", "Tutorials" bo'limlari joylashgan. Bizga **Circuits** (Sxemalar) bo'limi kerak.

### 3. Tinkercad Circuits ishchi muhiti interfeysi

Circuits bo'limida **"Create your first circuit"** yoki **"Create new Circuit"** tugmasi bosilganda asosiy laboratoriya oynasi ochiladi:

1. **Yuqori chap panel (Asboblar):**
   - **Rotate (R):** Tanlangan komponentni 30 gradusga burish;
   - **Delete (Del):** Komponentni o'chirish;
   - **Undo (Ctrl+Z) / Redo (Ctrl+Y):** Harakatni bekor qilish yoki qaytarish;
   - **Notes (N):** Sxemaga matnli eslatma biriktirish;
   - **Toggle Notes Visibility:** Eslatmalarni yashirish yoki ko'rsatish;
   - **Wire Color:** Ulovchi sim rangini tanlash (qizil, qora, yashil, sariq, ko'k va h.k.);
   - **Wire Type:** Sim turi (oddiy sim, timsoh qisqich — alligator clip, avtomatik).

2. **Yuqori o'ng panel (Simulyatsiya va kod):**
   - **Code:** Mikrokontrollerlar uchun blokli (Scratch-ga o'xshash) yoki matnli (C/C++) kod muharriri;
   - **Start Simulation:** Elektr toki oqimi va mikrokontroller dasturini ishga tushirish tugmasi;
   - **Send To / Share:** Sxemani rasm sifatida yuklab olish yoki boshqalar bilan havolasini ulashish.

3. **O'ng panel (Komponentlar kutubxonasi):**
   - **Qidiruv maydoni (Search):** Komponent nomini inglizcha kiritish (masalan, `Arduino`, `LED`, `Resistor`);
   - **Filtr:** "Basic" (asosiy komponentlar) va "All" (barcha sensorlar, chiplar, tranzistorlar, motorlar).

4. **Markaziy maydon (Workplane):**
   - Komponentlar sichqoncha bilan tortib olib (drag-and-drop) joylashtiriladigan cheksiz ish maydoni. Sichqoncha g'ildiragi orqali masshtabni o'zgartirish (Zoom In / Zoom Out) mumkin.

---

## Amaliy mashg'ulot va topshiriqlar

### 1-topshiriq. Tinkercad Circuits muhitida yangi loyiha yaratish va sozlash (oson)
O'quvchi Tinkercad.com saytidan ro'yxatdan o'tib, "Circuits" bo'limida yangi loyiha yaratishi, loyihaga `9-sinf_IoT_Laboratoriya_01` deb nom berishi va ishchi maydonga ixtiyoriy 3 ta komponent (masalan: Arduino Uno, 9V batareya, LED) joylashtirishi lozim.

**Yechim:**
1. Brauzerda `tinkercad.com` ochiladi va Google akkaunt orqali kiriladi.
2. Chap paneldagi "Circuits" bo'limiga kirilib, "Create new Circuit" tugmasi bosiladi.
3. Yuqori chap burchakdagi standart avtomatik nom (masalan, `Amazing Juring-Bombul`) ustiga sichqoncha bilan bosilib, `9-sinf_IoT_Laboratoriya_01` ga o'zgartiriladi.
4. O'ng tarafdagi komponentlar panelidan "Arduino Uno R3", "9V Battery" va "LED" sichqoncha bilan ushlab, ish maydoniga tortib qo'yiladi.
5. Loyiha Tinkercad tomonidan avtomatik bulutga saqlanadi.

### 2-topshiriq. Asboblar paneli bilan ishlash va komponent parametrlarini sozlash (o'rta)
Ish maydoniga 1 ta rezistor va 1 ta LED joylashtiring. Rezistor qiymatini 220 Ω (Om) ga sozlang va uni 90 gradusga buring. LED rangini esa yashil (Green) rangga o'zgartiring. Sxemaga "Tinkercad 1-amaliyot" matnli eslatmasini (Notes) qo'ying.

**Yechim:**
1. O'ng panel qidiruviga `Resistor` yozilib, ish maydoniga qo'yiladi.
2. Rezistor bosilganda ochiladigan parametrlar oynasida:
   - "Resistance" qatoriga `220` yoziladi;
   - Yonidagi o'lchov birligi menyusidan `kΩ` o'rniga `Ω` (Om) tanlanadi (rang chiziqlari darhol o'zgaradi: qizil-qizil-jigarrang-oltin).
3. Rezistor tanlangan holatda klaviaturadagi `R` harfi 3 marta bosiladi (har bosish 30° buradi, jami 90° buriladi).
4. Ish maydoniga `LED` qo'yiladi va parametrlar oynasidan "Color" menyusi ochilib, `Green` tanlanadi.
5. Yuqori paneldagi "Notes" (N) belgisi bosilib, ish maydoniga `Tinkercad 1-amaliyot` matni kiritiladi.

### 3-topshiriq. Loyihani ommaviy ulashish (Share link) va o'qituvchiga topshirish (qiyin)
Tinkercad-da yaratilgan sxemalar odatiy holatda shaxsiy (Private) hisoblanadi. O'qituvchi o'quvchining ishini tekshirishi uchun o'quvchi ushbu sxemaning xavfsiz ommaviy havolasini (Public Share link) yaratishi va nusxalab olishi kerak. Bu qanday amalga oshiriladi?

**Yechim:**
1. Sxema muharririning yuqori o'ng burchagidagi "Send To" (yoki "Share") tugmasi bosiladi.
2. "Invite people" (Odamlarni taklif qilish) bo'limida "Generate new link" (Yangi havola yaratish) tugmasi bosiladi.
3. Hosil bo'lgan havola `https://www.tinkercad.com/things/...` ko'rinishida bo'ladi va "Copy link" tugmasi bosiladi.
4. Yoki asosiy Dashboard sahifasida sxema ustidagi tishli g'ildirak (Settings -> Properties) orqali kirilib, "Privacy" sozlamasi "Private" dan "Public" ga o'zgartiriladi va "Save Changes" saqlanadi. Shunda o'qituvchi istalgan brauzerda o'quvchi sxemasini ko'ra oladi va simulyatsiyani tekshirishi mumkin bo'ladi.

---

## Tezkor nazorat savollari

1. Tinkercad platformasining eng asosiy 3 ta afzalligi nimada?
   - *Javob:* Brauzerda bepul ishlashi, haqiqiy detallarni kuydirib qo'yish xavfining yo'qligi va o'rnatish talab etilmasligi.
2. Ish maydonidagi komponentni burish uchun klaviaturadagi qaysi tezkor tugma ishlatiladi?
   - *Javob:* `R` harfi (Rotate).
3. Tinkercad-da yaratilgan sxemani sinovdan o'tkazish uchun qaysi tugma bosiladi?
   - *Javob:* "Start Simulation" tugmasi.
4. Komponentlar ro'yxatida "Basic" va "All" rejimlarining farqi nimada?
   - *Javob:* "Basic" faqat eng ko'p ishlatiladigan 20 ga yaqin asosiy detallarni ko'rsatadi; "All" rejimida esa barcha sensorlar, mikrosxemalar va motorlar chiqadi.

---

## Keng tarqalgan xatolar va ularning oldini olish

- **Rezistor o'lchov birligini kΩ (kilo-om) holatida qoldirish:** O'quvchilar ko'pincha rezistorga `220` raqamini kiritishadi, lekin yonidagi birlik `kΩ` ligicha qolib ketadi. Natijada 220 Om o'rniga 220,000 Om qarshilik ulanib, LED yonmaydi. Har doim o'lchov birligini tekshirish lozim.
- **Standart loyiha nomini o'zgartirmaslik:** Tinkercad yangi sxemalarga `Luminous Snicket-Gogo` kabi tasodifiy nomlar beradi. Agar o'quvchi nomni vaqtida o'zgartirmasa, keyinroq o'nlab sxemalar ichidan keraklisini topa olmay qiynaladi.
