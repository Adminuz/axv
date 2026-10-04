# 3-dars. IoT arxitekturasi: Tarmoq, bulut va foydalanuvchi interfeysi

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga IoT tizimlarining yuqori qatlamlarini — tarmoq texnologiyalari (Wi-Fi, Bluetooth BLE, ZigBee, LoRaWAN, 4G/5G) va protokollarini (MQTT, HTTP), Edge computing va Cloud computing arxitekturalarini, ma'lumotlarni filtrlash va xavfsizlikni hamda foydalanuvchi interfeysi (UI dashboardlar, mobil ilovalar, bildirishnomalar)ni o'rgatish.
- **Kutiladigan natija:** O'quvchilar IoT tarmoqlarini masofa va energiya sarfiga qarab to'g'ri tanlay oladi; MQTT protokoli (Publish/Subscribe, Broker) ishlash mexanizmini tushunadi; Edge computing va Cloud computing farqini biladi; IoT telemetriya ma'lumotlarini dashboardlarda vizualizatsiya qilish tamoyillarini o'zlashtiradi.
- **Vaqt taqsimoti:**
  - O'tgan mavzuni takrorlash (Sensorlar, aktuatorlar va Arduino): 10 daqiqa
  - Yangi mavzu: Tarmoq texnologiyalari (Wi-Fi, BLE, LoRaWAN) va protokollar (MQTT vs HTTP): 25 daqiqa
  - Bulutli tizimlar, Edge Computing va kiberxavfsizlik: 20 daqiqa
  - Ilova qatlami (Dashboardlar, mobil ilovalar): 15 daqiqa
  - Dars yakuni va nazorat savollari: 10 daqiqa

---

## Mentor konspekti

### 1. IoT Tarmoq Texnologiyalari (Connectivity)
IoT qurilmalari o'z sharoiti, masofasi va quvvat manbaiga qarab turli tarmoqlardan foydalanadi:
1. **Wi-Fi (IEEE 802.11):** Yuqori tezlik (Mbps), qamrov 10–50 m. Energiya sarfi yuqori. Doimiy elektr tarmog'iga ulangan aqlli uy qurilmalari, videokameralar uchun.
2. **Bluetooth Low Energy (BLE):** Qisqa masofa (1–20 m), juda kam quvvat sarfi. Smart soatlar, fitnes bilakuzuklar va tibbiy sensorlar uchun.
3. **ZigBee:** Qamrov 10–100 m, past tezlik, o'zaro to'rsimon (**Mesh network**) ulanadi (har bir qurilma signalni keyingisiga uzatadi). Ko'p datchikli aqlli uylar uchun.
4. **LoRaWAN (Long Range WAN):** Uzoq masofa (shahar tashqarisida 10–15 km), juda past tezlik (bir necha bayt), batareyada **5–10 yil** ishlaydi. Qishloq xo'jaligi, o'rmon yong'inlari va suv omborlari monitoringi uchun.
5. **NB-IoT / LTE-M va 4G/5G:** Mobil operatorlar infratuzilmasi orqali shahar bo'ylab harakatlanuvchi transportlar va aqlli hisoblagichlar (gaz, elektr) uchun.

### 2. IoT Protokollari: MQTT vs HTTP
- **HTTP / REST API (Request / Response):**
  - Mijoz so'rov yuboradi, server javob beradi. Har bir so'rovda katta sarlavhalar (headers) mavjud.
  - IoT uchun kamchiligi: og'ir, ortiqcha internet-trafik va quvvat sarflaydi.
- **MQTT (Message Queuing Telemetry Transport):**
  - IoT ning oltin standarti! IBM tomonidan 1999 yilda neft quvurlarini sun'iy yo'ldosh orqali monitoring qilish uchun yaratilgan.
  - **Publish / Subscribe (Nashr / Obuna) modeli:**
    - *Broker (Markaziy server):* Xabarlarni qabul qiladi va tarqatadi (masalan, Mosquitto, EMQX).
    - *Publisher (Yuboruvchi):* Sensor ma'lumotni ma'lum bir mavzuga (Topic) jo'natadi (masalan: `home/kitchen/temp` -> `24.5`).
    - *Subscriber (Qabul qiluvchi):* Smartfon ilovasi yoki fan ushbu mavzuga obuna bo'ladi va yangi ma'lumot kelishi bilan uni darhol qabul qiladi.
    - Sarlavha hajmi atigi **2 bayt** — zaif mobil tarmoqlarda ham uzluksiz ishlaydi.

### 3. Edge Computing vs Cloud Computing
- **Cloud Computing (Bulutli hisoblash):**
  - Barcha ma'lumotlar uzoqdagi serverlarga (AWS, Azure, Blynk) yuboriladi.
  - Katta hajmdagi ma'lumotlarni saqlash, yillik tahlillar va murakkab ML algoritmlari uchun a'lo.
  - Kamchiligi: internet uzilsa yoki kechikish (latency) bo'lsa, xavfli vaziyatda kechikishi mumkin.
- **Edge Computing (Chekka / Lokal hisoblash):**
  - Ma'lumotlar bulutga ketmasdan, bevosita qurilmaning o'zida (ESP32) yoki xonadagi Gateway'da tahlil qilinadi.
  - Tezkor javob (1 millisekund): gaz sezilsa, bulutga so'rov yuborib o'tirmay, mikrokontroller darhol klapanni yopadi!
  - Internet o'chsa ham lokal xavfsizlik 100% ishlayveradi.

### 4. Ilova Qatlami va Ma'lumotlarni Vizualizatsiya Qilish
- **Dashboard (Boshqaruv paneli):** Sensorlardan kelayotgan raqamlar oqimini inson tushunadigan shaklga aylantirish:
  - Harorat va namlik grafigi (dinamika);
  - Status indikatorlari (Yashil/Qizil chiroq);
  - Boshqaruv tugmalari (On/Off switch).
- Mashhur IoT platformalari: **Blynk**, **Ubidots**, **ThingsBoard**, **Home Assistant**.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Aloqa texnologiyasini tanlash (oson)
Quyidagi 3 ta IoT loyihasi uchun eng mos keluvchi simsiz tarmoqni (Wi-Fi, Bluetooth BLE yoki LoRaWAN) tanlang va asoslang:
1) Bemorning bilagiga taqilgan puls-oksimetr datchigi;
2) Shahardan 10 km uzoqlikdagi paxta dalasidagi tuproq namligi sensori;
3) Uy xonasidagi yuqori aniqlikdagi xavfsizlik videokamerasi.

**Yechim:**
1. **Puls-oksimetr:** `Bluetooth Low Energy (BLE)` — juda kam energiya sarflaydi, kichik batareyada oylarcha ishlaydi va bemorning cho'ntagidagi smartfon bilan yaqin masofada bog'lanadi.
2. **Paxta dalasi sensori:** `LoRaWAN` — 10-15 km masofaga ma'lumot uzata oladi va elektr simi bo'lmagan dalada batareyasi 5 yilgacha yetadi.
3. **Videokamera:** `Wi-Fi` — katta hajmdagi video oqimini (HD video) uzatish uchun yuqori o'tkazuvchanlik tezligi (Mbps) talab etiladi.

### 2-topshiriq. MQTT mavzusi (Topic) va xabarlar oqimi (o'rta)
Aqlli uyda 3 ta xona bor: `mehmonxona`, `oshxona`, `yotoqxona`. Har bir xonada harorat va yorug'lik sensorlari o'rnatilgan.
MQTT daraxtsimon ierarxiyasi bo'yicha ushbu xonalardagi haroratni yuborish uchun 3 ta to'g'ri mavzu (Topic) nomini tuzing va smartfon qanday qilib bir vaqtning o'zida barcha xonalar haroratiga bitta so'rov bilan obuna bo'lishi mumkinligini tushuntiring.

**Yechim:**
1. **Topic nomlari:**
   - Mehmonxona: `uy/mehmonxona/harorat`
   - Oshxona: `uy/oshxona/harorat`
   - Yotoqxona: `uy/yotoqxona/harorat`
2. **Umumiy obuna:**
   - MQTT da `+` (bitta darajali wildcard) belgisi ishlatiladi.
   - Smartfon ilovasi `uy/+/harorat` mavzusiga obuna bo'lsa, u barcha xonalardan kelgan harorat xabarlarini avtomatik qabul qiladi.

### 3-topshiriq. Nega gaz sizib chiqqanda Cloud emas, Edge Computing kerak? (qiyin)
Oshxonada gaz sizib chiqishini aniqlovchi xavfsizlik tizimi o'rnatilgan.
Agar tizim faqat Cloud Computing asosida ishlasa va to'satdan uydagi Wi-Fi router yoki tashqi internet aloqasi uzilib qolsa, qanday fojia sodir bo'lishi mumkin? Ushbu muammo Edge Computing yordamida qanday hal qilinadi?

**Yechim:**
1. **Faqat Cloud bo'lsa:** Sensor gazni sezadi, lekin ma'lumotni bulutga yubora olmaydi (internet yo'q). Bulutdan "Klapanni yop!" buyrug'i kelmagani uchun gaz xonaga to'lishda davom etadi va portlash xavfi yuzaga keladi.
2. **Edge Computing yechimi:**
   - Qaror qabul qilish mantiqi to'g'ridan-to'g'ri mikrokontrollerning (masalan, Arduino yoki ESP32) o'ziga yoziladi.
   - Sensor signali belgilangan xavfli chegaradan oshishi bilan mikrokontroller internetga qaramasdan, 10 millisekund ichida relega signal berib, gaz klapanini zudlik bilan yopadi va ovozli buzzerni yoqadi.
   - Internet mavjud bo'lganda esa qo'shimcha ravishda bulutga xabar yuboriladi.

---

## Tezkor nazorat savollari

1. IoT uchun eng yengil va ommabop hisoblangan Publish/Subscribe protokoli qaysi?
   - *Javob:* MQTT (Message Queuing Telemetry Transport).
2. Qaysi simsiz tarmoq texnologiyasi shahar tashqarisida 10–15 km masofaga kam quvvat sarfi bilan ma'lumot uzatish imkonini beradi?
   - *Javob:* LoRaWAN.
3. Edge Computing bilan Cloud Computing o'rtasidagi asosiy farq nima?
   - *Javob:* Edge Computing ma'lumotlarni bevosita qurilmaning o'zida tezkor tahlil qiladi (internet talab qilmaydi); Cloud Computing esa ma'lumotlarni uzoq serverlarda saqlaydi va global tahlil qiladi.
4. Smartfonda sensor ko'rsatkichlarini grafik va tugmalar ko'rinishida chiqarib beruvchi mashhur IoT mobil platformasi qaysi?
   - *Javob:* Blynk (yoki Ubidots, ThingsBoard).

---

## Keng tarqalgan xatolar va ularning oldini olish

- **HTTP va MQTT ni chalkashtirish:** O'quvchilar sensor har 1 soniyada serverga ma'lumot yuborishi uchun og'ir HTTP POST so'rovini qo'llashga harakat qilishadi. Bu mikrokontroller xotirasini to'ldirib, batareyani bir kunda tugatadi. Sensor telemetriyasi uchun har doim MQTT tavsiya etiladi.
- **Lokal xavfsizlikni unutish (Cloud dependency):** Barcha funksiyalarni faqat bulutga bog'lab qo'yish (masalan, chiroqni yoqish uchun internet orqali buyruq kutish). Internet uzilganda ham xona chirog'i yoki gaz xavfsizligi lokal ravishda mustaqil ishlashi shart.
