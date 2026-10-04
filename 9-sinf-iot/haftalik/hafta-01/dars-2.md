# 2-dars. IoT arxitekturasi: Sensorlar, aktuatorlar va apparat ta'minoti

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga IoT tizimlarining ko'p qatlamli arxitekturasini, xususan, quyi apparat ta'minoti — qurilmalar qatlami (Device/Perception Layer)ni chuqur o'rgatish; analog va raqamli sensorlarning ishlash fizikasi, aktuatorlar (ijrochi mexanizmlar) turlari va mikrokontrollerning (Arduino, ESP32) tizimdagi boshqaruv rolini amaliy misollar bilan tushuntirish.
- **Kutiladigan natija:** O'quvchilar IoT ning 4 qatlamli modelini biladi; sensor va aktuator vazifalarini aniq ajrata oladi; analog va raqamli signallar farqini tushunadi; Arduino va ESP32 kabi apparat platformalarining asosiy xususiyatlarini sanay oladi.
- **Vaqt taqsimoti:**
  - O'tgan mavzuni takrorlash (IoT tushunchasi va sohalari): 10 daqiqa
  - Yangi mavzu: IoT ning 4 qatlamli modeli va qurilmalar qatlami: 20 daqiqa
  - Sensorlar (analog vs raqamli) va aktuatorlar (servo, rele, motor): 25 daqiqa
  - Mikrokontrollerlar (Arduino, ESP32, Raspberry Pi) arxitekturasi: 15 daqiqa
  - Nazorat savollari va dars xulosasi: 10 daqiqa

---

## Mentor konspekti

### 1. IoT ning 4 qatlamli arxitekturasi
Har qanday professional IoT tizimi 4 ta asosiy qatlamdan tashkil topadi:
1. **Qurilmalar qatlami (Device / Perception Layer):** Atrof-muhitni sezuvchi datchiklar (sensorlar), jismoniy harakat bajaruvchi asboblar (aktuatorlar) va ularni boshqaruvchi mikrokontrollerlar.
2. **Tarmoq qatlami (Network Layer):** Ma'lumotlarni simsiz (Wi-Fi, Bluetooth, LoRaWAN, GSM) yoki simli (Ethernet) yo'l bilan shlyuzlar (Gateway) orqali uzatish.
3. **Ma'lumotlarni qayta ishlash qatlami (Data Processing / Cloud Layer):** Bulutli serverlar, ma'lumotlar bazasi, filtrlash, tahlil va sun'iy intellekt algoritmlari.
4. **Ilova qatlami (Application Layer):** Foydalanuvchi ko'radigan mobil ilova, veb-dashboard yoki avtomatlashtirilgan boshqaruv paneli.

### 2. Sensorlar (Tizimning "Ko'zi va Qulog'i")
Sensorlar atrof-muhitdagi fizik, kimyoviy yoki mexanik ko'rsatkichlarni sezib, ularni elektr signaliga (kuchlanish yoki tok) aylantiradi.
- **Analog sensorlar:** Uzluksiz o'zgarib turuvchi kuchlanish signali beradi (masalan, 0V dan 5V gacha).
  - *Misollar:* TMP36 (harorat), LDR (fotorezistor — yorug'lik), MQ-2 (gaz miqdori), Potensiometr.
  - Mikrokontrollerdagi **ADC (Analog-to-Digital Converter)** uni 0 dan 1023 gacha raqamli qiymatga aylantiradi.
- **Raqamli sensorlar:** Faqat 2 ta holatni (0 yoki 1, LOW yoki HIGH) yoki tayyor raqamli baytlarni uzatadi.
  - *Misollar:* PIR (harakat sezgichi — faqat "harakat bor/yo'q"), tugma (Button), DHT11/DHT22 (raqamli harorat va namlik protokoli bilan).

### 3. Aktuatorlar (Tizimning "Qo'li va Ijrochi Mexanizmi")
Mikrokontroller buyrug'i asosida elektr quvvatini jismoniy mexanik harakatga, yorug'likka yoki tovushga aylantiruvchi qurilmalar:
1. **Rele (Relay Module):** Past kuchlanishli (5V) mikrokontroller signali orqali yuqori kuchlanishli (220V) maishiy asboblarni (chiroq, isitgich, nasos) xavfsiz yoqish/o'chirish kaliti.
2. **Servo motor (Servomotor):** O'z o'qini berilgan aniq burchakka (masalan, 0° dan 180° gacha) burish va ushlab turish imkonini beruvchi motor. Aqlli eshik qulflari, robot qo'llar va avtomatik darchalar uchun.
3. **DC motor va Step motor:** Uzluksiz aylanuvchi dvigatellar (konveyerlar, g'ildiraklar) va aniq qadamli dvigatellar (3D printerlar).
4. **Solenoid klapan (Valve):** Suv yoki gaz oqimini elektromagnit yordamida ochib-yopuvchi aqlli jo'mrak.
5. **Indikatorlar:** LED (yorug'lik signali) va Buzzer (ovozli signal / signalizatsiya).

### 4. Mikrokontroller (Tizimning "Miyasi")
Bitta yarimo'tkazgichli kristall (chip) ichida joylashgan ixcham kompyuter:
- **Tarkibi:** CPU (protsessor), RAM (tezkor xotira), Flash/ROM (dastur kodi saqlanadigan doimiy xotira), I/O (kirish-chiqish pinlari), Taymerlar, ADC, PWM va aloqa portlari (UART, SPI, I2C).
- **Asosiy turlari:**
  - *Arduino Uno (ATmega328P):* 16 MHz, 32 KB xotira, 5V. O'rganish va boshlang'ich prototiplash uchun eng qulay. Tarmoq moduli yo'q.
  - *ESP8266 / ESP32:* 80-240 MHz, megabaytlab Flash xotira, 3.3V, o'rnatilgan **Wi-Fi va Bluetooth**. Haqiqiy IoT loyihalari uchun eng mashhur mikrokontrollerlar.
  - *Raspberry Pi:* Mikrokontroller emas, balki to'liq **Single Board Computer (SBC)**. Unda to'liq Linux (Raspberry Pi OS) ishlaydi, monitor va klaviatura ulanadi, yuqori darajadagi video tahlil va server vazifalarini bajaradi.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Sensor va aktuatorlarni ajratish (oson)
Quyida berilgan qurilmalar ro'yxatini ikki guruhga (Sensorlar va Aktuatorlar) ajrating:
1) Fotorezistor (LDR); 2) Servomotor; 3) PIR harakat datchigi; 4) Elektromagnit rele; 5) Ovozli buzzer; 6) Tuproq namligi sensori.

**Yechim:**
- **Sensorlar (Atrofni sezuvchi):**
  - 1. Fotorezistor (LDR) — yorug'lik darajasini o'lchaydi;
  - 3. PIR datchigi — inson harakatini sezadi;
  - 6. Tuproq namligi sensori — tuproqdagi suv miqdorini aniqlaydi.
- **Aktuatorlar (Ijrochi harakat):**
  - 2. Servomotor — mexanik burchakka buriladi;
  - 4. Elektromagnit rele — 220V tarmoqni ulaydi/uzadi;
  - 5. Ovozli buzzer — ogohlantiruvchi tovush chiqaradi.

### 2-topshiriq. Rele moduli bilan xavfsiz boshqaruv sxemasi (o'rta)
Arduino mikrokontrolleri atigi 5V kuchlanish va bir necha o'n milliamper tok bera oladi. Oddiy xona qandili (chirog'i) esa 220V o'zgaruvchan tok bilan ishlaydi.
Nima uchun 220V li chiroqni to'g'ridan-to'g'ri Arduino piniga ulab bo'lmaydi va ushbu muammo Rele (Relay) moduli orqali qanday hal etiladi?

**Yechim:**
1. **Nega ulab bo'lmaydi:** Arduino mikrokontrollerining chiqish pinlari maksimal 5V va 20–40 mA tokka mo'ljallangan. Agar unga 220V ulansa, mikrokontroller bir zumda yonib ketadi va elektr toki urish xavfi paydo bo'ladi.
2. **Rele qanday yordam beradi:**
   - Rele ichida elektromagnit g'altak (katushka) va mexanik kontaktlar joylashgan.
   - Arduino relening 5V li kirishiga signal yuboradi: elektromagnit tortilib, alohida 220V zanjirdagi metall kontaktlarni bir-biriga jismonan yopishtiradi.
   - Natijada Arduino va 220V yuqori kuchlanish o'rtasida **galvanik izolyatsiya (to'liq elektr xavfsizligi)** ta'minlanadi.

### 3-topshiriq. Aqlli to'siq (Shlagbaum) loyihasi uchun komponentlar tanlovi (qiyin)
Avtoturargoh kirishida avtomobil yaqinlashganda raqamini aniqlamasdan, shunchaki masofani o'lchab to'siqni ochuvchi va yopuvchi sodda IoT shlagbaum tizimi qurilmoqda.
Ushbu tizim uchun Sensor, Aktuator va Mikrokontroller tanlang hamda ularning o'zaro ishlash algoritmini yozing.

**Yechim:**
1. **Komponentlar tanlovi:**
   - *Sensor:* HC-SR04 ultratovush masofa sensori (avtomobil 1 metr masofaga kelganini aniqlash uchun).
   - *Aktuator:* Servomotor (SG90 yoki MG995 — shlagbaum tayoqchasini 90 darajaga ko'tarish uchun) va qizil/yashil LED indikatorlar.
   - *Mikrokontroller:* Arduino Uno yoki ESP32.
2. **Algoritm:**
   - 1. Ultratovush sensori har 100 millisekundda masofani o'lchaydi;
   - 2. Agar masofa > 100 sm bo'lsa: Qizil LED yonadi, Servo 0° (to'siq yopiq);
   - 3. Agar masofa <= 100 sm bo'lsa (mashina keldi): Yashil LED yonadi, Servo 90° ga buriladi (to'siq ko'tariladi);
   - 4. Mashina o'tib ketib, masofa yana 100 sm dan oshgach, 5 soniya kutib, Servo yana 0° ga qaytadi (to'siq yopiladi).

---

## Tezkor nazorat savollari

1. IoT ning 4 qatlamli modelidagi birinchi (eng quyi) qatlam qanday ataladi?
   - *Javob:* Qurilmalar qatlami (Device yoki Perception Layer).
2. Analog va raqamli sensorning asosiy farqi nimada?
   - *Javob:* Analog sensor uzluksiz o'zgaruvchi kuchlanish (0–5V) beradi, raqamli sensor esa faqat diskret 0 va 1 (yoki tayyor raqamli paket) uzatadi.
3. 5V mikrokontroller signali bilan 220V elektr chiroqni xavfsiz boshqarish uchun qaysi aktuator ishlatiladi?
   - *Javob:* Rele moduli (Relay Module).
4. ESP32 ning oddiy Arduino Uno dan eng asosiy ustunligi nimada?
   - *Javob:* ESP32 chipining ichida o'rnatilgan Wi-Fi va Bluetooth modullari mavjud bo'lib, protsessor tezligi va xotirasi ancha yuqori.

---

## Keng tarqalgan xatolar va ularning oldini olish

- **Arduino va Raspberry Pi ni bitta toifaga kiritish:** O'quvchilar ko'pincha Raspberry Pi ni ham mikrokontroller deb o'ylashadi. Arduino — bu bitta dasturni qattiq siklda aylantiruvchi mikrokontroller; Raspberry Pi esa operatsion tizim (Linux) o'rnatilgan to'liq mini-kompyuterdir.
- **Aktuatorlarni to'g'ridan-to'g'ri mikrokontroller pinidan quvvatlash:** Servo motor yoki kuchli dvigatellarni bevosita Arduino piniga ulash platani ishdan chiqarishi mumkin, chunki mikrokontroller pini bunday katta tok bera olmaydi. Motorlar har doim alohida tashqi quvvat manbaiga (External Power) ulanishi shart.
