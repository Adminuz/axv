# 4-dars. Kompyuterning asosiy va qo'shimcha qurilmalari

**Hafta:** 2 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliy ko'rgazma · **I-bob**, 4-dars

## 1. Dars rejasi

**Maqsad:** o'quvchilarda kompyuterning asosiy (tizim bloki, monitor, klaviatura, sichqoncha) va qo'shimcha periferiya qurilmalari (printer, skaner, proyektor, veb-kamera, dinamiklar), ularning vazifalari, kiritish/chiqarish portlari (USB, HDMI, DisplayPort, Audio jack) hamda qurilmalarni kompyuterga xavfsiz ulash va drayverlar bilan ishlash bo'yicha to'liq amaliy tushunchalarni shakllantirish.

**Kutiladigan natija:**
- Kompyuterning asosiy va qo'shimcha (periferiya) qurilmalarini aniq ajrata oladi.
- Kiritish (input), chiqarish (output) va axborot saqlash (storage) qurilmalari tasnifini biladi.
- Zamonaviy portlar (USB Type-A, USB Type-C, HDMI, DisplayPort, Ethernet RJ-45) va simsiz aloqa (Bluetooth, Wi-Fi) turlarini taniydi.
- Drayver (Driver) tushunchasini va uning periferiya qurilmalarini ishlatishdagi rolini tushuntiradi.
- Qurilmalarni xavfsiz ulash va ajratish («Safely Remove Hardware») qoidalariga rioya qiladi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va kirish | 1-hafta mavzularini takrorlash (arxitektura, Windows, fayllar). «Nega ba'zi printerlar kompyuterga ulanganda darhol ishlamaydi?» muammoli savol |
| 10–30 daq | Yangi mavzu: Nazariya | Asosiy va qo'shimcha qurilmalar, portlar va interfeyslar, drayverlar mohiyati, xavfsiz ulanish |
| 30–35 daq | Tanaffus | Harakatli jismoniy mashqlar |
| 35–65 daq | Amaliy mashg'ulot | Device Manager (Qurilmalar dispetcheri) bilan ishlash, ulangan portlarni tekshirish, drayver holatini ko'rish |
| 65–75 daq | Tezkor nazorat | 5 ta savol va interaktiv test |
| 75–80 daq | Xulosa va uyga vazifa | Asosiy xulosalar va uy vazifasini tushuntirish |

---

## 2. Dars konspekti

### 2.1. Kompyuterning asosiy qurilmalari

Kompyuterning to'liq ishlashi va inson u bilan muloqot qilishi uchun zarur bo'lgan minimal to'plam **asosiy qurilmalar** deyiladi. Bular 4 ta:
1. **Tizim bloki (System Unit):** Barcha hisoblash, ma'lumotlarni qayta ishlash va saqlash jarayonlarini bajaruvchi kompyuterning eng muhim korpusi. Uning ichida ona plata, protsessor (CPU), operativ xotira (RAM), doimiy saqlash disklari (SSD/HDD) va quvvat bloki (PSU) joylashgan.
2. **Monitor (Displey):** Matn, rasm, video va dasturlar interfeysini vizual tarzda ko'rsatib beruvchi asosiy chiqarish qurilmasi.
3. **Klaviatura (Keyboard):** Kompyuterga matn, raqamlar va buyruqlarni kiritish uchun xizmat qiluvchi asosiy kiritish qurilmasi.
4. **Sichqoncha (Mouse):** Grafik interfeysdagi kursor yordamida obyektlarni boshqarish, tanlash va ishga tushirish uchun xizmat qiluvchi kiritish qurilmasi.

### 2.2. Qo'shimcha (periferiya) qurilmalar

Kompyuterning imkoniyatlarini kengaytiruvchi, tashqi tomondan ulanadigan barcha qurilmalar **qo'shimcha (periferiya) qurilmalar** deyiladi. Ular vazifasiga ko'ra uch guruhga bo'linadi:

1. **Qo'shimcha kiritish qurilmalari:**
   - *Skaner:* Qog'ozdagi hujjat yoki rasmni raqamli tasvirga aylantiradi.
   - *Veb-kamera:* Videoqo'ng'iroqlar va jonli efir uchun video tasvirni kompyuterga kiritadi.
   - *Mikrofon:* Ovozli signallarni raqamli audio formatga aylantiradi.
   - *Grafik planshet (Stylus bilan):* Rassom va dizaynerlar uchun qalam bilan chizish imkonini beradi.
2. **Qo'shimcha chiqarish qurilmalari:**
   - *Printer:* Kompyuterdagi elektron hujjat yoki rasmni qog'ozga chop etadi (Lazerli va Purkagichli/Inkjet turlari bor).
   - *Proyektor:* Kompyuter ekranidagi tasvirni katta devorga yoki maxsus matoga kattalashtirib aks ettiradi.
   - *Akustik tizim (Kolonkalar va naushniklar):* Raqamli tovush signallarini insonga eshitiladigan akustik to'lqinlarga aylantiradi.
3. **Tashqi saqlash qurilmalari:**
   - *USB fleshka (Flash drive):* Ixcham, ko'chma flesh-xotira qurilmasi.
   - *Tashqi qattiq disk (External HDD/SSD):* Katta hajmdagi ma'lumotlarni nusxalash va zaxira (backup) qilish uchun ishlatiladi.

### 2.3. Ulanish portlari va interfeyslar

Qurilmalar tizim blokiga maxsus tirqishlar — **portlar** orqali ulanadi:
- **USB (Universal Serial Bus):** Eng universal port (klaviatura, sichqoncha, fleshka, printer ulanadi). Hozirgi kunda `USB Type-A` va ikki tomonlama ishlaydigan zamonaviy `USB Type-C` keng tarqalgan.
- **HDMI va DisplayPort:** Monitorni va proyektorni ulash uchun yuqori aniqlikdagi video hamda audio uzatuvchi raqamli portlar.
- **Ethernet (RJ-45):** Simli internet va lokal tarmoq kabelini ulash porti.
- **Audio Jack (3.5 mm):** Naushnik va mikrofon uchun audio tirqish.
- **Simsiz interfeyslar:** Bluetooth (quloqchin, klaviatura, sichqoncha uchun) va Wi-Fi (internet uchun).

### 2.4. Drayver (Driver) nima?

**Drayver** — operatsion tizimga yangi ulangan qurilma bilan qanday gaplashishni o'rgatuvchi maxsus mikrodastur.
Agar kompyuterga yangi printer yoki videokarta ulasangiz, operatsion tizim uning drayverisiz qurilmaning barcha imkoniyatlaridan foydalana olmaydi. Zamonaviy Windows tizimida ko'plab drayverlar «Plug and Play» (Ula va Ishlat) texnologiyasi orqali avtomatik tarzda o'rnatiladi.

### 2.5. Xavfsiz foydalanish qoidalari

1. Fleshka va tashqi disklarni to'satdan sug'urib olmang! Doimo vazifalar panelidan «Safely Remove Hardware» (Qurilmani xavfsiz ajratish) buyrug'ini bering, aks holda fayllar shikastlanishi mumkin.
2. Kompyuter qismlarini tozalashda yoki yangi qurilma ulashda elektr tarmog'idan uzilganligiga ishonch hosil qiling.
3. Statik elektr zaryadi nozik chiplarga zarar yetkazmasligi uchun korpusning metall qismiga qo'l tekkizib zaryadsizlaning.

---

## 3. Kod / Amaliy buyruqlar

Windows tizimida ulangan barcha qurilmalar va drayverlar holatini tekshirish:

```powershell
# 1. Qurilmalar dispetcherini (Device Manager) tezkor ochish
Win + X -> Device Manager (yoki devmgmt.msc buyrug'i)

# 2. Ulangan USB va Bluetooth qurilmalari ro'yxatini ko'rish
Win + I -> Bluetooth & devices

# 3. Printerlar va skanerlar bo'limini ochish
Win + I -> Bluetooth & devices -> Printers & scanners
```

---

## 4. Amaliy topshiriqlar

### 1-topshiriq (oson)
`Win + X` tugmalarini bosing va menyudan «Device Manager» (Qurilmalar dispetcheri)ni oching (yoki `Win + R` orqali `devmgmt.msc` kiriting). Kompyuteringizga ulangan klaviatura, sichqoncha va displey adapteri (videokarta) nomlarini aniqlang.

**Kutiladigan natija:** Kompyuterga ulangan 3 ta asosiy qurilmaning drayver ro'yxatidagi nomi daftarga yoziladi.

**Yechim:**
1. `Win + X` bosilib, «Device Manager» tanlanadi.
2. «Keyboards» bandi ochilib, klaviatura modeli ko'riladi (masalan, *Standard PS/2 Keyboard* yoki *HID Keyboard Device*).
3. «Mice and other pointing devices» bo'limida sichqoncha ko'riladi.
4. «Display adapters» bo'limida videokarta nomi (masalan, *Intel UHD Graphics* yoki *NVIDIA GeForce GTX 1650*) aniqlanadi.

---

### 2-topshiriq (o'rta)
Kompyuteringizning tizim blokida (yoki noutbuk korpusida) mavjud barcha tashqi portlarni ko'zdan kechiring. Quyidagi portlarning nechta donadan borligini aniqlang va jadval tuzing:
1. USB Type-A portlari soni.
2. USB Type-C porti bormi?
3. Monitor ulash uchun qaysi port bor (HDMI, DisplayPort yoki VGA)?
4. 3.5 mm audio tirqish va Ethernet (tarmoq) porti mavjudligi.

**Kutiladigan natija:** Kompyuterning portlari to'liq sanab chiqilgan jadval.

**Yechim:**
1. Korpusning old, orqa va yon tomonlari tekshiriladi.
2. Masalan: USB 3.0 Type-A — 4 ta, USB Type-C — 1 ta, HDMI — 1 ta, Audio Jack — 1 ta, RJ-45 Ethernet — 1 ta. Natija tartibli jadvalga yoziladi.

---

### 3-topshiriq (qiyin)
Fleshkani kompyuterga ulang, unga kichik fayl yozing. So'ngra uni birdaniga sug'urib olish o'rniga, Windows vazifalar panelining o'ng burchagidagi «Safely Remove Hardware and Eject Media» (Xavfsiz ajratish) amali orqali chiqarib oling. Nima uchun bu amal doimiy saqlash qurilmalari uchun muhimligini texnik jihatdan asoslang.

**Kutiladigan natija:** Xavfsiz ajratish amali to'g'ri bajariladi; keshlash va xotira kontrolleri ma'lumotlarni oxirigacha yozib ulgurishi kerakligi tushuntiriladi.

**Yechim:**
1. Vazifalar panelining o'ng quyi burchagidagi kichik strelka (System Tray) bosiladi.
2. Fleshka belgisi ustiga bosilib, «Eject [Fleshka nomi]» tanlanadi.
3. «Safe to Remove Hardware» xabari chiqqandan keyingina qurilma sug'uriladi.
4. Asoslash: Operatsion tizim fayllarni birdaniga diskka yozmasdan, vaqtincha kesh xotirada (RAM buffer) ushlab turishi mumkin. To'satdan sug'urilganda keshdagi ma'lumot yozilmay qolib, fayl tizimi (`FAT32`/`NTFS`) buziladi va fleshka «format talab qiladigan» bo'lib qoladi.

---

## 5. Tezkor nazorat

1. Kompyuterning 4 ta asosiy qurilmasini ayting.
   - *Javob:* Tizim bloki, monitor, klaviatura, sichqoncha.
2. Qo'shimcha (periferiya) qurilma deb nimaga aytiladi?
   - *Javob:* Kompyuter imkoniyatlarini kengaytirish uchun tashqi tomondan ulanadigan barcha qo'shimcha asboblar (printer, skaner, veb-kamera, proyektor).
3. Skaner va Printerning asosiy farqi nimada?
   - *Javob:* Skaner — kiritish qurilmasi (qog'ozdan kompyuterga o'tkazadi); Printer — chiqarish qurilmasi (kompyuterdan qog'ozga chop etadi).
4. Drayver (Driver) nima uchun kerak?
   - *Javob:* Operatsion tizim yangi ulangan apparat qurilmasi bilan to'g'ri muloqot qilishi va uni boshqarishi uchun zarur bo'lgan dastur.
5. Zamonaviy monitorlar tizim blokiga qaysi portlar orqali ulanadi?
   - *Javob:* HDMI va DisplayPort (eski kompyuterlarda VGA/DVI).

---

## 6. Uyga vazifa

1. Uyingizdagi yoki maktabdagi kompyuterga qanday periferiya qurilmalari (printer, naushnik, veb-kamera va h.k.) ulanganligini daftaringizga ro'yxat qilib yozing va ularni «Kiritish» hamda «Chiqarish» turlariga ajrating.
2. Kompyuteringizda `Win + X` → «Device Manager» orqali «Audio inputs and outputs» bo'limini ochib, o'rnatilgan dinamik va mikrofon nomini yozib oling.
Vazifani bajarish vaqti: 20 daqiqa.
