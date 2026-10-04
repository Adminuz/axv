# 3-dars. Androidning imkoniyatlari va qo‘llanilish sohalari

**Sinf:** 9-sinf (Android dasturlash)  
**Hafta:** 1-hafta  
**Dars tartibi:** 3-dars (umumiy 102 darsdan 3-darsi)  
**Davomiyligi:** 80 daqiqa  
**Format:** Amaliy va tahliliy mashg'ulot  

---

## 1. Dars maqsadi va kutiladigan natijalar

- **Maqsad:** O'quvchilarga Android platformasining texnik imkoniyatlari (ko'p vazifalilik, on-device AI/ML, bulutli integratsiya) hamda uning smartfonlardan tashqari turli xil sohalarda (Wear OS, Android Auto, Android TV, IoT va tibbiyot) qo'llanilishi bo'yicha to'liq tasavvur berish.
- **Kutiladigan natijalar:**
  - O'quvchi Androidning multitasking (Split-screen, Picture-in-Picture) va sun'iy intellekt imkoniyatlarini tushuntira oladi;
  - Android faqat telefon operatsion tizimi emas, balki global ekotizim ekanini anglaydi;
  - Wear OS (aqlli soatlar), Android Auto (avtomobil tizimlari), Android TV (televizorlar) va IoT qurilmalarining o'ziga xos arxitekturasini ajrata oladi;
  - Har xil turdagi ekran o'lchamlari va moslashuvchan dizayn (Responsive / Adaptive UI) tushunchasini biladi;
  - Tibbiyot, transport, ta'lim va savdo sohalarida Android asosidagi ixtisoslashgan qurilmalar (POS-terminallar, tibbiy monitorlar, interaktiv panellar) rolini tahlil qila oladi.

---

## 2. Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 daq** | O'tgan mavzuni takrorlash va kirish | Androidning 5 qatlami, ART va Sandbox bo'yicha blits-so'rov. Muammoli savol: "Aqlli soat va avtomobil ekranidagi Android smartfondagidan nimasi bilan farq qiladi?" |
| **10–35 daq** | Yangi mavzu: Texnik imkoniyatlar | Multitasking (Split-screen, PiP), on-device sun'iy intellekt (Gemini Nano, NNAPI), bulutli texnologiyalar bilan integratsiya |
| **35–55 daq** | Yangi mavzu: Qo'llanilish sohalari | Wear OS (aqlli soatlar), Android Auto / Automotive OS (avtomobillar), Android TV, IoT va sanoat qurilmalari |
| **55–65 daq** | Amaliy keys va guruhlarda tahlil | Turli qurilmalar uchun foydalanuvchi interfeysi (UI/UX) cheklovlarini solishtirish (soat ekrani vs televizor ekrani) |
| **65–75 daq** | Mustahkamlash va test sinovi | Interaktiv savol-javob, konspekt tekshiruvi |
| **75–80 daq** | Xulosa va 1-hafta sarhisobi | Dars xulosasi, baholash, 1-haftaning umumiy uyga vazifasini tushuntirish |

---

## 3. Nazariy tushunchalar (Mentor uchun to'liq konspekt)

### 3.1. Androidning zamonaviy texnik imkoniyatlari
Android platformasi rivojlanish jarayonida oddiy mobil telefondan qudratli hisoblash platformasiga aylandi:
1. **Ko'p vazifalilik (Multitasking):**
   - **Split-Screen (Ekranni ikkiga bo'lish):** Bir vaqtning o'zida ikkita ilovadan (masalan, yuqorida YouTube videosi, pastda konspekt ilovasi) teng foydalanish;
   - **Picture-in-Picture (PiP — Rasmdagi rasm):** Video qo'ng'iroq yoki xarita mini-oyna ko'rinishida ekranning bir burchagida suzib yuradi;
   - **Freeform Windows:** Planshetlar va buklanuvchi (Foldable) qurilmalarda xuddi kompyuterdagidek oynalarni erkin ko'chirish va o'lchamini o'zgartirish.
2. **Sun'iy intellekt va mashinali o'rganish (On-Device AI/ML):**
   - Zamonaviy Android versiyalarida (Android 14–15) AI hisob-kitoblari internetga so'rov yubormasdan to'g'ridan-to'g'ri qurilmaning NPU (Neural Processing Unit) chipida amalga oshiriladi;
   - **Android AICore va Gemini Nano:** Ovozni real vaqtda matnga aylantirish, matnlarni umumlashtirish (summarize), aqlli avto-javoblar.
3. **Bulutli sinxronizatsiya:**
   - Google Drive, Firebase va Cloud Messaging orqali bir qurilmada boshlangan ish boshqa qurilmada bir zumda davom ettiriladi.

### 3.2. Qo'llanilish sohalari va ixtisoslashgan Android versiyalari
Google Android yadrosi asosida turli qurilmalar sinfi uchun moslashtirilgan maxsus versiyalarni ishlab chiqqan:

#### 1. Smartfonlar, planshetlar va Foldable qurilmalar
- Har xil o'lchamli ekranlar (5 dyuymdan 14 dyuymgacha);
- Buklanuvchi ekranlar (Samsung Galaxy Fold, Pixel Fold) uchun maxsus moslashuvchan oynalar (Adaptive Layouts).

#### 2. Wear OS (Aqlli soatlar)
- **Ekran o'lchami:** 1.2 – 1.5 dyuymli dumaloq yoki to'rtburchak ekranlar;
- **Asosiy vazifasi:** Sog'liqni nazorat qilish (yurak urish tezligi — puls, qon bosimi, EKG, qadamlar), tezkor bildirishnomalar, kontaktsiz to'lov (NFC orqali);
- **Dasturlash xususiyati:** Batareyani maksimal tejash, minimalistik interfeys (Tiles va Complications), doimiy ochiq ekran (Always-on Display).

#### 3. Android Auto va Android Automotive OS
- **Android Auto:** Smartfon ekranini avtomobil monitoriga proyeksiyalovchi tizim (kabel yoki simsiz ulanish);
- **Android Automotive OS (AAOS):** Avtomobilning o'ziga o'rnatilgan mustaqil operatsion tizim (Volvo, Polestar, Ford). U nafaqat musiqa va navigatsiyani, balki konditsioner, o'rindiq isitish va akkumulyator quvvatini ham boshqaradi;
- **Xavfsizlik qoidasi:** Dasturchi haydovchining e'tiborini chalg'itmaydigan yirik tugmalar va ovozli boshqaruvga (Google Assistant) asoslangan interfeys yaratishi shart.

#### 4. Android TV va Google TV
- Katta ekranlar (32 dyuymdan 85+ dyuymgacha);
- Sensorli boshqaruv yo'q: foydalanuvchi pult (D-pad: yuqori, pastki, chap, o'ng, OK) orqali boshqaradi;
- Ko'rish masofasi: 2.5–3 metr ("10-foot UI");
- Qo'llanilishi: YouTube, Netflix, onlayn kinoteatrlar, o'yinlar.

#### 5. IoT (Internet of Things — Buyumlar Interneti) va sanoat qurilmalari
- **Savdo va xizmat ko'rsatish:** Android asosida ishlaydigan aqlli kassa va POS-terminallar (masalan, chek chiqaruvchi Smart POS apparatlari);
- **Tibbiyot:** Bemor parametrlarini kuzatuvchi statsionar monitorlar;
- **Aqlli uy:** Muzlatgich eshigidagi sensorli ekran, aqlli domofonlar va devor panellari.

---

## 4. Darsda bajariladigan amaliy topshiriqlar va yechimlari

### 1-topshiriq. Turli qurilmalar interfeysi taqqoslash jadvali (Oson)
**Topshiriq:** Smartfon, Wear OS (aqlli soat) va Android TV qurilmalarini ekran o'lchami, boshqaruv turi va asosiy vazifasi bo'yicha taqqoslang.

**Yechim:**
| Qurilma turi | Ekran o'lchami | Boshqaruv turi | Asosiy maqsadi |
|---|---|---|---|
| **Smartfon** | 5.5 – 6.8 dyuym | Sensorli ekran (Touch, Multi-touch) | To'liq kommunikatsiya, internet, ish va o'yinlar |
| **Wear OS** | 1.2 – 1.5 dyuym | Kichik sensorli ekran, aylanuvchi tugma (Crown), ovoz | Tezkor xabarlar, sport va salomatlik nazorati |
| **Android TV** | 32 – 85+ dyuym | Masofadan boshqarish pulti (D-pad), ovoz | Video va multimedia ko'rish, qulay hordiq |

### 2-topshiriq. Android Auto va Android Automotive OS farqi (O'rta)
**Topshiriq:** Nima sababdan Android Auto va Android Automotive OS ikki xil texnologiya hisoblanadi? Ularning asosiy farqini tushuntiring.

**Yechim:**
- **Android Auto:** Bu mustaqil operatsion tizim emas. U haydovchining smartfonida ishlaydi va avtomobil ekraniga tasvirni uzatadi (Screen Casting). Agar smartfon uzilsa, tizim ishlamaydi.
- **Android Automotive OS (AAOS):** Bu avtomobilning bort kompyuteriga o'rnatilgan to'laqonli mustaqil operatsion tizimdir. U smartfonga bog'liq emas, avtomobil apparatiga (konditsioner, batareya holati, tezlik) to'g'ridan-to'g'ri ulangan.

### 3-topshiriq. IoT qurilmasi uchun Android ilovasi konsepsiyasi (Qiyin)
**Topshiriq:** Maktab oshxonasi uchun Android planshetida ishlaydigan «O'quvchi o'z-o'ziga xizmat ko'rsatish kioski» loyihasi g'oyasini ishlab chiqing:
1. Qurilma qaysi Android imkoniyatlaridan (NFC, kamera, chek printeri) foydalanadi?
2. Ilova interfeysi nima uchun oddiy telefon ilovasidan kattaroq va soddaroq bo'lishi kerak?

**Yechim:**
1. **Apparat imkoniyatlari:**
   - NFC moduli: O'quvchi ID-kartasini tekkazib to'lov qiladi;
   - Kamera / Barcode skaner: Mahsulot shtrix-kodini o'qiydi;
   - USB / Bluetooth drayveri: Kvitansiya (chek) chiqaruvchi termoprinterga ulanadi.
2. **Interfeys talablari:**
   - Kiosk bolalar va o'quvchilar tomonidan mustaqil ishlatiladi, shuning uchun tugmalar katta bo'lishi kerak;
   - Matnlar qisqa va tushunarli piktogrammalar (ikonkalar) bilan birga berilishi shart;
   - "Kiosk Mode" yoqilib, o'quvchilar ilovadan chiqib sozlamalarga kira olmasligi ta'minlanadi.

---

## 5. Tezkor savol-javob (Blits-savollar)

1. **Split-Screen nima?**  
   *Javob:* Ekranni ikkita ilova o'rtasida teng bo'lib, ikkalasini bir vaqtda ishlatish imkoniyati.
2. **Wear OS qaysi turdagi qurilmalar uchun mo'ljallangan?**  
   *Javob:* Aqlli soatlar (Smartwatches) uchun.
3. **Android TV boshqaruvining smartfondan eng asosiy farqi nima?**  
   *Javob:* Sensorli boshqaruv yo'q, pult (D-pad) va ovoz orqali boshqariladi.
4. **On-device AI deganda nima tushuniladi?**  
   *Javob:* Sun'iy intellekt modellarining internetga so'rov jo'natmasdan, telefonning o'z protsessorida (NPU) ishlashi.
5. **IoT nima degani?**  
   *Javob:* Internet of Things — Buyumlar interneti (turli maishiy va sanoat qurilmalarining tarmoq orqali o'zaro bog'lanishi).

---

## 6. Mentor uchun amaliy tavsiyalar

- O'quvchilarga Android dasturchisi faqat smartfon ilovalari bilan cheklanib qolmasdan, aqlli soat, televizor yoki avtomobillar uchun ham ilova yoza olishini tushuntiring.
- Keyingi haftadan boshlab biz Android ekotizimi va Android Studio dasturiy muhiti bilan amaliy tanishishni boshlashimizni e'lon qilib, qiziqishni oshiring.
