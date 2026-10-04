# 3-dars. IoT arxitekturasi: Tarmoq, bulut va foydalanuvchi interfeysi

## Darsning asosiy mazmuni

Qurilmalar yig'gan ma'lumotlar foydalanuvchiga yetib borishi va avtomatik boshqaruv ishlashi uchun ular tarmoq va bulut tizimlariga ulanishi kerak. Ushbu darsda biz IoT simsiz aloqa turlari, eng yengil IoT protokoli — MQTT, Edge va Cloud computing hamda zamonaviy dashboardlarni o'rganamiz.

---

## 1. IoT Simsiz Tarmoq Texnologiyalari

| Texnologiya | Qamrov masofasi | O'tkazish tezligi | Energiya sarfi | Asosiy qo'llanish sohasi |
|---|---|---|---|---|
| **Wi-Fi** | 10–50 metr | Juda yuqori (Mbps) | Yuqori | Aqlli uy, videokameralar, elektr tarmog'iga ulangan qurilmalar |
| **Bluetooth (BLE)** | 1–20 metr | O'rtacha (kbps/Mbps) | **Juda past** | Aqlli soatlar, tibbiy sensorlar, mobil periferiya |
| **ZigBee** | 10–100 metr | Past (kbps) | Past | To'rsimon (Mesh) aqlli uylar, o'nlab sensorlar tarmog'i |
| **LoRaWAN** | **10–15 km** | Juda past (kbps) | **O'ta past (5-10 yil batareya)** | Aqlli qishloq xo'jaligi, o'rmonlar, uzoq masofali monitoring |
| **NB-IoT / 4G / 5G** | Shahar bo'ylab | Yuqori / O'rtacha | O'rtacha | Harakatdagi avtomobillar, dronlar, aqlli elektr hisoblagichlar |

---

## 2. MQTT Protokoli — IoT ning Oltin Standarti

**MQTT (Message Queuing Telemetry Transport)** — bu cheklangan resursli qurilmalar va zaif tarmoqlar uchun maxsus yaratilgan eng yengil ma'lumot uzatish protokolidir.

```
[Sensor: Publisher]  ---- (Nashr: uy/oshxona/gaz = 15) --->  [ BROKER: Markaziy Server ]
                                                                      |
                                                               (Tarqatish)
                                                                      v
                                                      [Smartfon Ilova: Subscriber]
```

- **Broker:** Markaziy server (masalan, Mosquitto, HiveMQ, EMQX). Barcha xabarlarni qabul qiladi va kerakli mijozlarga yo'naltiradi.
- **Publisher (Nashr etuvchi):** Datchik ma'lumotini ma'lum bir mavzuga (**Topic**) jo'natuvchi qurilma.
- **Subscriber (Obunachi):** Kerakli mavzuni tinglab, yangi ma'lumot kelishi bilan uni qabul qiluvchi qurilma yoki ilova.
- **Topic (Mavzu):** Daraxtsimon manzil, masalan: `maktab/3-bino/14-xona/harorat`.

---

## 3. Edge Computing vs Cloud Computing

1. **Cloud Computing (Bulutli hisoblash):**
   - Ma'lumotlar internet orqali uzoqdagi kuchli serverlarga (AWS, Azure, Blynk) yuboriladi.
   - Yillik statistikani saqlash, sun'iy intellekt tahlili va global boshqaruv uchun qulay.
2. **Edge Computing (Chekka / Mahalliy hisoblash):**
   - Ma'lumotlar bulutga ketmasdan, bevosita qurilmaning o'zida (ESP32) yoki xonadagi Gateway'da qayta ishlanadi.
   - **Afzalligi:** Internet o'chib qolsa ham tizim ishlayveradi va qarorlar 1 millisekundda qabul qilinadi (masalan, gaz sizganda darhol klapanni yopish).

---

## 4. Foydalanuvchi Interfeysi (Dashboardlar)

**IoT Dashboard** — bu sensorlardan kelgan raqamlar oqimini vizual grafiklar, rangli shkalalar va interaktiv boshqaruv tugmalariga aylantirib beruvchi veb yoki mobil paneldir.

- **Mashhur platformalar:** Blynk IoT, Ubidots, ThingsBoard, Home Assistant.
- **Xususiyatlari:** Real vaqt ko'rsatkichlari, o'tgan haftalik dinamika, avtomatik Telegram/SMS ogohlantirishlar.

---

## Amaliy topshiriqlar

### 1-topshiriq. Tarmoq texnologiyasini tanlash · oson
Quyidagi 3 ta qurilma uchun eng mos tarmoqni (Wi-Fi, Bluetooth BLE, LoRaWAN) tanlang:
a) Shahardan 8 km uzoqlikdagi bug'doy dalasida tuproq namligi sensori;
b) Xonadagi yuqori sifatli jonli video uzatuvchi xavfsizlik kamerasi;
c) Cho'ntakdagi telefon bilan ulanuvchi aqlli fitnes bilakuzuk.

### 2-topshiriq. MQTT ning 3 ta asosiy bo'g'ini · oson
MQTT protokolidagi Broker, Publisher va Subscriber tushunchalarining vazifalarini oddiy pochta yoki xat tashuvchi misolida tushuntiring.

### 3-topshiriq. MQTT mavzusi (Topic) ierarxiyasini tuzish · oson
O'z uyingiz uchun MQTT mavzular daraxtini tuzing:
- Oshxona harorati;
- Mehmonxona yorug'ligi;
- Kirish eshigi qulfi holati.

### 4-topshiriq. Wi-Fi va LoRaWAN taqqosi · o'rta
Nima uchun ulkan paxta maydonlarida Wi-Fi o'rniga LoRaWAN ishlatiladi? Qamrov masofasi va batareya muddati bo'yicha ikkala texnologiyani solishtiring.

### 5-topshiriq. Nega IoT da HTTP o'rniga MQTT tanlanadi? · o'rta
Oddiy veb-saytlar uchun ishlatiladigan HTTP protokoli kichik batareyali IoT datchiklari uchun nima sababdan noqulay va og'irlik qiladi?

### 6-topshiriq. Edge Computing hayotiy zarurati · o'rta
Aqlli avtomobilda to'siqni ko'rib tormoz bosish tizimi o'rnatilgan. Ushbu qarorni qabul qilish Cloud Computing orqali bo'lishi kerakmi yoki Edge Computing? Nima sababdan?

### 7-topshiriq. Blynk platformasida boshqaruv panelini loyihalash · o'rta
Blynk mobil ilovasida xona haroratini ko'rsatish va xona chirog'ini yoqish uchun qanday 2 ta vizual vidjet (Widget) tanlanishi kerak?

### 8-topshiriq. Aqlli shahar svetoforlari tarmog'i · qiyin
Shahar bo'ylab 50 ta chorrahadagi svetoforlar tirbandlik ma'lumotlarini markaziy dispetcherlik serveriga uzatishi kerak. Tizimda qaysi simsiz tarmoq va qaysi protokol qo'llanilishi maqsadga muvofiq?

### 9-topshiriq. Kiberxavfsizlik: Zaif MQTT serveri · qiyin
Agar kompaniya o'zining MQTT Broker serverini parolsiz, ochiq internetga ulab qo'ysa, yovuz niyatli kishi qanday xavfli buyruqlarni yuborishi mumkin? IoT da parollash va shifrlash (TLS/SSL) nima uchun muhim?

### 10-topshiriq. Telegram Bot integratsiyasi g'oyasi · bonus
Tuproq namligi 30% dan pastga tushganda yoki xonada yong'in chiqqanda fermerning yoki uy egasining Telegramiga avtomatik xabar yuboruvchi IoT tizimi qanday ishlashini tasvirlang.
