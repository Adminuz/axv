# 1-dars. Android nima va uning rivojlanish tarixi

**Sinf:** 9-sinf (Android dasturlash)  
**Hafta:** 1-hafta  
**Dars tartibi:** 1-dars (umumiy 102 darsdan 1-darsi)  
**Davomiyligi:** 80 daqiqa  
**Format:** Ma'ruza va interaktiv kirish mashg'uloti  

---

## 1. Dars maqsadi va kutiladigan natijalar

- **Maqsad:** O'quvchilarga mobil operatsion tizimlarning evolyutsiyasi, Android tizimining vujudga kelishi, Google tomonidan rivojlantirilishi, versiyalar ketma-ketligi hamda Androidning zamonaviy dunyoda va O'zbekiston raqamli iqtisodiyotidagi o'rnini tushuntirish.
- **Kutiladigan natijalar:**
  - O'quvchi Android operatsion tizimining mohiyati va ochiq kodli (open source / AOSP) ekanligini anglaydi;
  - Android Inc. asoschilari (Andy Rubin, Rich Miner, Nick Sears, Chris White) va 2005-yilda Google sotib olganini biladi;
  - Ilk tijoriy Android qurilmasi (HTC Dream / T-Mobile G1, 2008-yil) xususiyatlarini tushuntira oladi;
  - Android versiyalarining nomlanish tizimini (shirinliklar davri: Cupcake'dan Pie'gacha va zamonaviy raqamlar davri: Android 10 dan 15 gacha) taqqoslay oladi;
  - O'zbekistondagi ommabop Android ilovalari (Click, Payme, Apelsin, Yandex Go, MyTaxi, EduOn) misolida mobil dasturlashning ijtimoiy-iqtisodiy ahamiyatini tahlil qila oladi.

---

## 2. Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 daq** | Tashkiliy qism va kirish | Salomlashish, yo'nalish mazmuni bilan tanishtirish, qiziqtiruvchi savol: "Dunyoda har kuni nechta Android qurilmasi faollashadi?" |
| **10–30 daq** | Yangi mavzu: Tarix va evolyutsiya | Mobil operatsion tizimlar tarixi (Symbian, BlackBerry, iOS), Android Inc. va Andy Rubin, Google xaridi, HTC Dream |
| **30–50 daq** | Yangi mavzu: Versiyalar va ochiq kod falsafasi | Cupcake'dan Android 15 gacha bo'lgan rivojlanish, AOSP (Android Open Source Project) va turli qobiqlar (OneUI, MIUI, HyperOS) |
| **50–65 daq** | Amaliy keys va guruhlarda muhokama | O'zbekistondagi mobil ilovalar ekotizimi, smartfonlardagi Android versiyalari va texnik imkoniyatlar tahlili |
| **65–75 daq** | Mustahkamlash va test sinovi | Tezkor savol-javob (blits), atamalarni takrorlash |
| **75–80 daq** | Xulosa va uyga vazifa | Darsni sarhisob qilish, o'quvchilarni baholash va uyga vazifa berish |

---

## 3. Nazariy tushunchalar (Mentor uchun to'liq konspekt)

### 3.1. Androidning mohiyati va boshqaruv mexanizmi
Android — bu sensorli ekranli mobil qurilmalar (smartfonlar, planshetlar) va aqlli gadjetlar uchun maxsus moslashtirilgan, **Linux yadrosiga (Linux Kernel)** asoslangan ochiq kodli operatsion tizimdir. Uni **Google** boshchiligidagi Open Handset Alliance konsortsiumi rivojlantiradi.

Operatsion tizim sifatida Android quyidagi asosiy jarayonlarni boshqaradi:
1. **Apparat ta'minoti va resurslar boshqaruvi:** Protsessor (CPU), operativ xotira (RAM), doimiy xotira (Flash Storage) resurslarini taqsimlaydi;
2. **Periferiya va sensorlar nazorati:** Kamera, mikrafon, akselerometr, giroskop, GPS, barmoq izi skaneri va boshqa modullar faoliyatini muvofiqlashtiradi;
3. **Ilovalarning xavfsiz izolyatsiyasi:** Har bir ilova alohida Linux foydalanuvchisi (UID) va alohida jarayonda xavfsiz «sandbox» rejimida ishlaydi.

### 3.2. Yaratilish tarixi va Google sotib olishi
- **2003-yil (Android Inc.):** AQSHning Kaliforniya shtati Palo-Alto shahrida Andy Rubin, Rich Miner, Nick Sears va Chris White Android Inc. kompaniyasiga asos solishdi. Dastlabki maqsad — raqamli kameralar uchun aqlli operatsion tizim yaratish edi. Ammo kameralar bozori torayib, mobil telefonlar jadal rivojlanayotganini ko'rgan jamoa diqqatini smartfonlarga qaratdi.
- **2005-yil (Google sotib olishi):** Google kompaniyasi Android Inc.ni taxminan 50 million dollarga sotib oldi. Andy Rubin Google vitse-prezidenti sifatida tizimni rivojlantirishga rahbarlik qildi. Google bepul, ochiq va moslashuvchan platforma yaratish orqali barcha qidiruv va internet xizmatlarini mobil muhitga integratsiya qilishni maqsad qildi.
- **2007-yil:** Open Handset Alliance (Google, HTC, Sony, Dell, Intel, Qualcomm, Samsung) tashkil etildi va Android rasman ommaga e'lon qilindi.
- **2008-yil 23-sentabr:** Tarixdagi birinchi tijoriy Android smartfoni — **HTC Dream (AQSHda T-Mobile G1)** sotuvga chiqdi. Qurilma sensorli ekran, to'liq QWERTY klaviatura, Wi-Fi, GPS va Android Market (hozirgi Google Play) do'koniga ega edi.

### 3.3. Versiyalar tarixi: Shirinliklar nomlaridan raqamlarga
2019-yilgacha Google har bir yangi Android versiyasini alifbo tartibida shirinliklar yoki pishiriqlar nomi bilan atagan:
- **1.5 Cupcake (2009):** Ekran klaviaturasi va vidjetlar qo'shildi;
- **1.6 Donut (2009):** Har xil ekran o'lchamlari qo'llab-quvvatlandi;
- **2.0/2.1 Eclair (2009):** Google Maps navigatsiyasi, ko'p hisobli pochta;
- **2.2 Froyo (2010):** JIT kompilyatori (tezlik 2-5 barobar oshdi), Wi-Fi hotspot;
- **2.3 Gingerbread (2010):** NFC qo'llab-quvvatlovi, o'yinlar uchun optimallashuv;
- **4.0 Ice Cream Sandwich (2011):** Holo dizayn tili, Face Unlock;
- **4.1–4.3 Jelly Bean (2012):** Project Butter (silliq 60 fps interfeys), Google Now;
- **4.4 KitKat (2013):** 512 MB operativ xotiraga ega arzon telefonlarda ham silliq ishlash;
- **5.0 Lollipop (2014):** **Material Design** dizayn tili, ART (Android Runtime) asosiy runtime sifatida kiritildi;
- **6.0 Marshmallow (2015):** Runtime permissions (dastur ishlayotgan paytda ruxsat so'rash);
- **7.0 Nougat (2016):** Split-screen (ekranni ikkiga bo'lish), tezkor javob;
- **8.0 Oreo (2017):** Project Treble (OS yangilanishlarini tezlashtirish);
- **9.0 Pie (2018):** Moslashuvchan batareya (Adaptive Battery), imo-ishoralar bilan boshqarish.

**Raqamli nomlash davri (2019-yildan):**
Global foydalanuvchilar madaniy farqlari tufayli shirinlik nomlarini tushunishda qiyinchilikka duch kelmasligi uchun Google rasmiy nomlarni raqamga o'tkazdi (garchi ichki kod nomlari shirinlik bo'lib qolgan bo'lsa-da):
- **Android 10 (2019):** Dark Theme (to'liq qora rejim), 5G qo'llab-quvvatlovi;
- **Android 11 (2020):** Bildirishnomalardagi muloqotlar (Conversations), bir martalik ruxsatlar;
- **Android 12 (2021):** **Material You (Material 3)** — fon rasmiga qarab ranglarni avtomatik moslashtiruvchi dinamik interfeys;
- **Android 13 (2022):** Ilova darajasida til tanlash, bildirishnoma ruxsatnomasi (POST_NOTIFICATIONS);
- **Android 14 (2023):** Ultra HDR tasvirlar, batareya unumdorligi, kattalashtirilgan shriftlar;
- **Android 15 (2024–2025):** Private Space (maxfiy bo'lim), sun'iy intellekt (Gemini Nano) integratsiyasi, ilovalarni sun'iy ushlab turishni cheklash.

### 3.4. Ochiq manba (AOSP) va ishlab chiqaruvchilar qobiqlari
Android asosida **AOSP (Android Open Source Project)** yotadi. Bu kod ochiq Apache 2.0 litsenziyasi ostida tarqatiladi. Shuning uchun smartfon ishlab chiqaruvchilari AOSP negizida o'zlarining shaxsiy interfeyslarini (firmware) yaratadilar:
- Samsung — **One UI**
- Xiaomi — **MIUI / HyperOS**
- OnePlus — **OxygenOS**
- Google Pixel — **Pixel UI (toza Android)**

---

## 4. Darsda bajariladigan amaliy topshiriqlar va yechimlari

### 1-topshiriq. Smartfon Android versiyasi va texnik parametrlarini aniqlash (Oson)
**Topshiriq:** Har bir o'quvchi o'z smartfonining (yoki sinfdagi planshetning) «Sozlamalar» (Settings) bo'limiga kirib:
1. Android versiyasini aniqlaydi;
2. «Android versiyasi» ustiga 3-4 marta tez bosib, yashirin «Easter Egg» animatsiyasini ochadi;
3. Qurilma modeli, protsessor turi va operativ xotirasini daftarga yozadi.

**Yechim:**
O'quvchi: Sozlamalar -> Telefon haqida (About phone) -> Dasturiy ta'minot ma'lumotlari (Software information) bo'limiga kiradi. Android versiyasi ustiga bir necha bor bosganda, masalan Android 14 bo'lsa kosmik kema animatsiyasi chiqadi. Barcha parametrlar qayd etiladi.

### 2-topshiriq. Android versiyalari taqqoslash jadvali (O'rta)
**Topshiriq:** Android 4.4 (KitKat), Android 5.0 (Lollipop) va Android 12 (Material You) versiyalarini asosiy texnik o'zgarishlari bo'yicha 3 ustunli jadvalga joylashtiring.

**Yechim:**
| Xususiyat | Android 4.4 KitKat | Android 5.0 Lollipop | Android 12 |
|---|---|---|---|
| Chiqqan yili | 2013 | 2014 | 2021 |
| Dizayn tili | Holo (qora/ko'k) | Material Design (tekis kartalar) | Material You (dinamik ranglar) |
| Runtime | Dalvik (standart) | ART (birlamchi qilib kiritildi) | ART (yanada tezlashgan) |
| Asosiy yangilik | 512MB RAM bilan ishlash | 64-bit CPU, yangi bildirishnomalar | Dynamic Theming, Privacy Dashboard |

### 3-topshiriq. O'zbekiston mobil ilovalar ekotizimi tahlili (Qiyin)
**Topshiriq:** Quyidagi mahalliy mobil ilovalardan kamida 4 tasini tanlab, ular qanday hayotiy muammoni hal qilishi va qaysi funksiyalari tufayli ommalashganini tahlil qiling:
`Click`, `Payme`, `Yandex Go`, `MyTaxi`, `EduOn`, `Kundalik / eMaktab`.

**Yechim:**
1. **Click / Payme:** Bank kartalarini bog'lash, P2P pul o'tkazmalari, kommunal to'lovlar, QR-kod orqali do'konda to'lash muammosini hal qiladi. Foydalanuvchilar navbatda turmasdan telefon orqali to'lov qiladi.
2. **Yandex Go / MyTaxi:** Yo'lovchi va haydovchini GPS orqali avtomatik bog'laydi. Narx oldindan aniq, mashinaning kelish yo'nalishi xaritada ko'rinadi.
3. **EduOn / eMaktab:** Ta'lim resurslariga masofaviy kirish, dars jadvallari va baholarni ota-onalar va o'quvchilarga onlayn ko'rsatish imkonini beradi.

---

## 5. Tezkor savol-javob (Blits-savollar)

1. **Android Inc. kompaniyasiga kim asos solgan?**  
   *Javob:* Andy Rubin, Rich Miner, Nick Sears va Chris White (2003-yil).
2. **Google Android kompaniyasini nechanchi yilda sotib olgan?**  
   *Javob:* 2005-yilda.
3. **Tarixdagi birinchi Android smartfoni qaysi va u qachon chiqqan?**  
   *Javob:* HTC Dream (T-Mobile G1), 2008-yil sentabr.
4. **Android operatsion tizimining asosi qaysi yadroga qurilgan?**  
   *Javob:* Linux yadrosiga (Linux Kernel).
5. **Nima uchun Android versiyalari endi shirinliklar bilan nomlanmaydi?**  
   *Javob:* Global miqyosda foydalanuvchilar chalkashmasligi va versiyalarni raqamlar bo'yicha tushunish qulay bo'lishi uchun (Android 10 dan boshlab).
6. **AOSP nima degani?**  
   *Javob:* Android Open Source Project — Androidning ochiq kodli loyihasi.

---

## 6. Mentor uchun amaliy tavsiyalar

- O'quvchilarda dasturlashga nisbatan ishtiyoq uyg'otish uchun telefonlaridagi ilovalarning yaratilish tarixi bilan darsni bog'lang.
- O'quvchilarga Android faqat telefonlarda emas, balki televizor, avtomobil va soatlarda ham ishlashini ta'kidlang (bu 3-dars mavzusiga ko'prik bo'ladi).
- HTC Dream va zamonaviy flagmanlarni taqqoslab, texnologiya 15-18 yil ichida qanchalik ulkan masofani bosib o'tganini ko'rsating.
