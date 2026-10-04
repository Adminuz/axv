# 9-dars. Simulyator va Emulator haqida tushuncha (1-qism)

**Sinf:** 9-sinf (Android dasturlash)  
**Hafta:** 3-hafta  
**Dars tartibi:** 9-dars (umumiy 102 darsdan 9-darsi)  
**Davomiyligi:** 80 daqiqa  
**Format:** Nazariy va amaliy laboratoriya mashg'uloti  

---

## 1. Dars maqsadi va kutiladigan natijalar

- **Maqsad:** O'quvchilarga mobil dasturlashda testlash muhiti — Simulyator va Emulyator o'rtasidagi fundamental farq, Android Virtual Device (AVD) yaratish va sozlash, kompyuter protsessorida apparat virtualizatsiyasining (Intel VT-x / AMD-V) roli hamda emulyator imkoniyatlarini o'rgatish.
- **Kutiladigan natijalar:**
  - O'quvchi Simulyator (Simulator) va Emulyator (Emulator) o'rtasidagi texnik farqni tushuntira oladi;
  - AVD Manager oynasi orqali yangi virtual qurilma yarata oladi (qurilma modeli, tizim tasviri, RAM hajmi);
  - Protsessor virtualizatsiyasi (Intel VT-x, AMD-V, KVM) nima uchun emulyator tezligi uchun zarurligini biladi;
  - Emulyatorning yon boshqaruv panelidagi vositalardan (aylantirish, ovoz, kamera, GPS taqlidi, batareya holati) foydalana oladi;
  - Virtual qurilma va real smartfonda testlashning afzallik va kamchiliklarini taqqoslay oladi.

---

## 2. Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 daq** | O'tgan mavzuni takrorlash va kirish | «Hello World» ilovasi, setContentView, TextView bo'yicha blits-so'rov. Muammoli savol: "Hamma dasturchida 10 ta har xil telefon bormi? Ular ilovani turli ekranlarda qanday tekshiradi?" |
| **10–30 daq** | Yangi mavzu: Simulyator vs Emulyator | Tashqi xatti-harakatni taqlid qilish (Simulation) vs Apparatni modellashtirish (Emulation), Android Emulator tuzilishi |
| **30–50 daq** | Yangi mavzu: AVD Manager va Virtualizatsiya | AVD yaratish bosqichlari (Device, System Image: Google APIs vs AOSP), Intel VT-x va AMD-V nima uchun kerak? |
| **50–65 daq** | Yangi mavzu: Emulyatorning interaktiv paneli | Yon panel: GPS koordinatalarini uzatish, qo'ng'iroq va SMS simulyatsiyasi, ekranni aylantirish va skrinshot olish |
| **65–75 daq** | Amaliy mashq va laboratoriya | O'quvchilar bilan kompyuterda AVD qurilmasini ishga tushirish va uning sozlamalarini o'rganish |
| **75–80 daq** | Xulosa va 3-hafta sarhisobi | Dars yakunlari, o'quvchilarni baholash, 3-haftaning umumiy uyga vazifasini topshirish |

---

## 3. Nazariy tushunchalar (Mentor uchun to'liq konspekt)

### 3.1. Simulyator va Emulyator o'rtasidagi fundamental farq
Ko'pincha bu ikki atama yanglish holda bir xil ma'noda ishlatiladi, ammo ular tubdan farq qiladi:
1. **Simulyator (Simulator):**
   - Faqat tashqi interfeys va dasturiy qoidalarni taqlid qiladi.
   - U apparat qismlarini (protsessor registrlarini, xotira kontrollerlarini) modellashtirmaydi, balki kompyuterning o'z arxitekturasida ishlaydi (masalan, iOS Simulator Mac kompyuterining x86 yoki ARM64 yadrolarida bevosita ishlaydi).
   - *Kamchiligi:* Haqiqiy telefon apparatida (masalan, xotira yetishmovchiligida yoki sensorlar ishlashida) yuzaga keladigan real muammolarni aniqlay olmaydi.
2. **Emulyator (Emulator):**
   - Haqiqiy qurilmaning butun apparat ta'minotini (Hardware) to'liq dasturiy modellashtiradi: virtual CPU, virtual RAM, virtual Bluetooth, modem va kamera drayverlari.
   - **Android Emulator (QEMU negizida):** Haqiqiy Android operatsion tizimi virtual qurilma ichida noldan yuklanadi (boot bo'ladi). U apparat ta'minotining barcha cheklovlari va xatti-harakatlarini 100% aks ettiradi.

### 3.2. AVD (Android Virtual Device) Manager
AVD — bu kompyuteringiz xotirasida saqlanadigan virtual smartfon yoki planshet konfiguratsiyasidir.
Uni yaratishda 4 ta asosiy parametr tanlanadi:
1. **Hardware Profile (Apparat profili):** Qurilma modeli (masalan, Pixel 8 Pro), ekranning fizik o'lchami (6.7 dyuym) va piksellar aniqligi (1344 x 2992, 489 dpi);
2. **System Image (Tizim tasviri):** Android versiyasi (Android 14 API 34). Tavsiya etiladigan variant: **Google APIs (x86_64)** — bu variant kompyuter protsessorida tez ishlaydi va Google Play Services xizmatlariga ega;
3. **Memory and Storage (Xotira):** Emulyator uchun ajratiladigan RAM (masalan, 2048 MB) va ichki xotira (masalan, 6 GB);
4. **Graphics Emulation:** `Hardware - GLES 2.0` — kompyuteringizning videokartasidan (GPU) foydalanib, emulyator grafikasini 60 kadr/soniya (fps) tezlikda silliq ko'rsatish.

### 3.3. Protsessor virtualizatsiyasi (Hardware Virtualization)
Nima uchun ba'zi kompyuterlarda emulyator umuman ochilmaydi?
- Emulyator kompyuter ichida butun bir operatsion tizimni ishga tushirishi sababli, unga apparat tezlatgichi kerak bo'ladi.
- **Intel protsessorlarida:** `Intel VT-x` (Virtualization Technology);
- **AMD protsessorlarida:** `AMD-V` (SVM);
- **Apple Silicon (M1/M2/M3/M4):** ARM-to-ARM to'g'ridan-to'g'ri virtualizatsiya (Hypervisor Framework).
- Agar kompyuter BIOS/UEFI sozlamalarida virtualizatsiya o'chirilgan bo'lsa, emulyator bir necha daqiqalab ochiladi yoki qotib qoladi. Shuning uchun BIOS'da virtualizatsiya yoqilgan bo'lishi shart!

### 3.4. Emulyatorning kengaytirilgan boshqaruv paneli (Extended Controls)
Emulyator oynasining yon tomonidagi vertikal asboblar paneli orqali dasturchi hayotiy ssenariylarni sinab ko'radi:
- **Location (GPS):** Xaritadan istalgan nuqtani (masalan, Toshkent, Samarqand yoki Parij) tanlab, ilovaga soxta GPS koordinatalarini yuborish;
- **Cellular & Battery:** Batareya zaryadini 10% qilib, ilova kam quvvatda qanday ishlashini yoki tarmoq tezligini "LTE" dan "GPRS" ga tushirib sinash;
- **Phone:** Virtual telefonga qo'ng'iroq qilish yoki SMS yuborish;
- **Camera:** Kompyuter veb-kamerasini virtual telefon kamerasi sifatida ulash;
- **Display:** Ekranni 90 darajaga aylantirib (Landscape), ilovaning gorizontal ko'rinishini tekshirish.

---

## 4. Darsda bajariladigan amaliy topshiriqlar va yechimlari

### 1-topshiriq. Simulyator va Emulyator taqqoslash matritsasi (Oson)
**Topshiriq:** Simulyator va Emulyator tushunchalarini ishlash prinsipi va apparat modellashtirishi bo'yicha taqqoslang.

**Yechim:**
| Xususiyat | Simulyator (Simulator) | Emulyator (Emulator) |
|---|---|---|
| Modellashtirish darajasi | Faqat dasturiy interfeys va xatti-harakat | To'liq apparat ta'minoti (CPU, xotira, datchiklar) |
| Tezlik | Juda tez (kompyuter kodi kabi) | O'rtacha (virtualizatsiyaga bog'liq) |
| Aniqlik | O'rtacha | Haqiqiy telefonga 99% yaqin |
| Misol | Apple iOS Simulator | Android Virtual Device (AVD) |

### 2-topshiriq. Virtualizatsiya muammosi diagnostikasi (O'rta)
**Topshiriq:** O'quvchi Android Studio'da yangi AVD yaratdi, ammo emulyator ishga tushmayapti va quyidagi xatolik chiqmoqda:  
`"HAXM is not installed / VT-x is disabled in BIOS"`.  
Bu xatolik nimani bildiradi va uni qanday tuzatish kerak?

**Yechim:**
- **Sababi:** Kompyuterning markaziy protsessorida (CPU) apparat virtualizatsiyasi (Intel VT-x yoki AMD-V) BIOS/UEFI darajasida o'chirilgan (Disabled).
- **Tuzatish tartibi:**
  1. Kompyuterni qayta ishga tushirib (Restart), BIOS/UEFI menyusiga kiriladi (F2, F10 yoki Del tugmasi orqali);
  2. "Advanced" yoki "Security" -> "CPU Configuration" bo'limi topiladi;
  3. "Intel Virtualization Technology" (yoki "SVM Mode") parametri **"Enabled"** qilinadi va sozlamalar saqlanadi (F10);
  4. Kompyuter yoqilgach, Android Studio'da emulyator darhol tezkor ishga tushadi.

### 3-topshiriq. GPS simulyatsiyasi keysi (Qiyin)
**Topshiriq:** Siz taksi chaqirish ilovasini (masalan, Yandex Go yoki MyTaxi muqobilini) yaratmoqchisiz. Emulyatorda mashina harakatlanayotganini real smartfonsiz qanday tekshirish mumkin?

**Yechim:**
1. Emulyatorning yon panelidagi uch nuqta `...` (Extended controls) tugmasi bosiladi;
2. **Location** bo'limiga o'tiladi;
3. "Routes" yorlig'ida boshlang'ich va yakuniy manzil kiritiladi yoki GPX/KML fayli yuklanadi;
4. "Play Route" tugmasi bosilganda, emulyator belgilangan tezlikda (masalan, 40 km/soat) koordinatalarni ketma-ket uzatishni boshlaydi. Ilova xaritadagi avtomobil harakatini xuddi haqiqiy hayotdagidek chizadi.

---

## 5. Tezkor savol-javob (Blits-savollar)

1. **AVD qisqartmasi nimani anglatadi?**  
   *Javob:* Android Virtual Device (Android virtual qurilmasi).
2. **Emulyatorning simulyatordan asosiy farqi nima?**  
   *Javob:* Emulyator qurilmaning apparat ta'minotini (hardware) to'liq modellashtiradi, simulyator esa faqat dasturiy qobiqni taqlid qiladi.
3. **Intel protsessorlarida virtualizatsiya qanday nomlanadi?**  
   *Javob:* Intel VT-x.
4. **Emulyator sozlamalarida "Google APIs" tasvirining qanday afzalligi bor?**  
   *Javob:* Unda Google Maps, Google Sign-In va Firebase xizmatlari oldindan o'rnatilgan bo'ladi.
5. **Emulyatorda ekranni aylantirish uchun nima qilinadi?**  
   *Javob:* Yon boshqaruv panelidagi "Rotate left / Rotate right" tugmasi bosiladi.

---

## 6. Mentor uchun amaliy tavsiyalar

- O'quvchilarga emulyatorning Extended Controls oynasida GPS koordinatasini o'zgartirish qanday ishlashini ko'rsating.
- Agar kompyuterlarning RAM xotirasi kam bo'lsa (8 GB dan kam), keyingi darsda real telefonni USB kabel orqali ulab testlashni (USB Debugging) o'rganishimizni bildiring.
