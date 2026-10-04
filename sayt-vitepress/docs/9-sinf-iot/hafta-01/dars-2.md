---
title: "2-dars. IoT arxitekturasi: Sensorlar, aktuatorlar va apparat ta'minoti"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (IoT)", "link": "/9-sinf-iot/"}, "week": {"n": 1, "link": "/9-sinf-iot/hafta-01/"}, "g": 2, "title": "IoT arxitekturasi: Sensorlar, aktuatorlar va apparat ta'minoti", "lead": "", "slide": "/slaydlar/9-sinf-iot/hafta-01/dars-2.html", "tabs": [{"g": 1, "link": "/9-sinf-iot/hafta-01/dars-1", "current": false}, {"g": 2, "link": "/9-sinf-iot/hafta-01/dars-2", "current": true}, {"g": 3, "link": "/9-sinf-iot/hafta-01/dars-3", "current": false}], "prev": {"g": 1, "title": "IoT tushunchasi va qo‘llanish sohalari", "link": "/9-sinf-iot/hafta-01/dars-1"}, "next": {"g": 3, "title": "IoT arxitekturasi: Tarmoq, bulut va foydalanuvchi interfeysi", "link": "/9-sinf-iot/hafta-01/dars-3"}}
---


<div class="blk">

## <Icon name="file-text" /> Darsning asosiy mazmuni

IoT tizimi qanchalik murakkab bo'lmasin, uning poydevori apparat ta'minotiga — sensorlar, aktuatorlar va mikrokontrollerlarga tayanadi. Ushbu darsda biz "qurilmalar qatlami" qanday ishlashini va ularning fizik imkoniyatlarini o'rganamiz.

---

</div>

<div class="blk">

## <Icon name="file-text" /> 1. IoT ning 4 qatlamli arxitekturasi

```
+---------------------------------------------------------------+
| 4. ILOVA QATLAMI (Application)      | Smartfon, Dashboard, UI |
+-------------------------------------+-------------------------+
| 3. QAYTA ISHLASH (Cloud/Processing) | Server, Ma'lumotlar baz.|
+-------------------------------------+-------------------------+
| 2. TARMOQ QATLAMI (Network/Gateway) | Wi-Fi, BLE, LoRa, 4G/5G |
+-------------------------------------+-------------------------+
| 1. QURILMALAR QATLAMI (Device/Per.) | SENSOR, MIKROKONTROLLER,|
|                                     | AKTUATOR (Apparat qismi)|
+---------------------------------------------------------------+
```

---

</div>

<div class="blk">

## <Icon name="file-text" /> 2. Sensorlar — Tizim Ko'zi va Qulog'i

Sensor atrof-muhitdagi fizik ko'rsatkichlarni (harorat, bosim, yorug'lik) sezib, ularni elektr signaliga aylantiradi.

| Sensor turi | Ishlash printsipi | Qayerda ishlatiladi? |
|---|---|---|
| **Analog sensor** | Uzluksiz o'zgaruvchi kuchlanish (0–5V) beradi. | Harorat (TMP36), yorug'lik (LDR fotorezistor), gaz (MQ-2) |
| **Raqamli sensor** | Faqat 2 ta holatni (0 yoki 1) yoki raqamli paket uzatadi. | Harakat (PIR datchigi), tugma (Button), harorat-namlik (DHT22) |

---

</div>

<div class="blk">

## <Icon name="file-text" /> 3. Aktuatorlar — Tizimning Ijrochi Qo'llari

Aktuatorlar mikrokontrollerdan kelgan elektr buyruqni jismoniy harakatga, yorug'likka yoki tovushga aylantiradi.

1. **Rele (Relay Module):** 5V mikrokontroller signali bilan 220V yuqori kuchlanishli maishiy chiroq va isitgichlarni xavfsiz yoqib-o'chiruvchi elektron kalit.
2. **Servomotor (Servo):** O'z o'qini berilgan aniq burchakka (masalan, 0° dan 180° gacha) buruvchi dvigatel (aqlli qulflar, robot qo'llar).
3. **DC Dvigatel:** Uzluksiz aylanuvchi motor (aqlli ventilyatorlar, g'ildiraklar).
4. **Solenoid Klapan:** Suv yoki gaz quvurlarini ochib-yopuvchi elektromagnit jo'mrak.
5. **Indikatorlar:** LED chiroqlari va ovozli Buzzer (signalizatsiya).

---

</div>

<div class="blk">

## <Icon name="file-text" /> 4. Mikrokontrollerlar — Tizimning Miyasi

| Qurilma | Turi | Xususiyatlari | Eng mos loyihalar |
|---|---|---|---|
| **Arduino Uno** | Mikrokontroller (ATmega328P) | 16 MHz, 32 KB Flash, 5V, tarmoqsiz | Elektronika asoslarini o'rganish, lokal robototexnika |
| **ESP32** | IoT Mikrokontroller | 240 MHz, 4 MB Flash, **Wi-Fi va Bluetooth bor** | Haqiqiy aqlli uy, bulutli IoT qurilmalari |
| **Raspberry Pi** | Bir platalik kompyuter (SBC) | To'liq Linux OT, 1-8 GB RAM, HDMI, USB | Katta serverlar, videokuzatuv va sun'iy intellekt |

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy topshiriqlar

### 1-topshiriq. 4 qatlamli model tahlili <Badge type="tip" text="oson" />
IoT ning 4 ta qatlami (Qurilmalar, Tarmoq, Qayta ishlash, Ilova) nomlarini yozing va har biriga bittadan mos komponent nomini ko'rsating.

### 2-topshiriq. Sensor yoki Aktuator? <Badge type="tip" text="oson" />
Quyidagi elementlarni Sensor yoki Aktuator ekanligini aniqlang:
a) Fotorezistor (LDR);
b) Servomotor (SG90);
c) MQ-2 gaz datchigi;
d) Elektromagnit rele;
e) Ovozli buzzer;
f) HC-SR04 ultratovush masofa o'lchagich.

### 3-topshiriq. Analog va raqamli signal farqi <Badge type="tip" text="oson" />
Xona harorati uzluksiz o'zgarib turadi (masalan, 20.1°C, 20.2°C, 20.5°C). Xonadagi deraza esa faqat ochiq yoki yopiq bo'ladi.
Ushbu ikki holatdan qaysi biri analog, qaysi biri raqamli signalga misol bo'ladi?

### 4-topshiriq. Rele moduli nima uchun kerak? <Badge type="warning" text="o'rta" />
Nima uchun xonadagi 220 voltli katta qandilni (chiroqni) to'g'ridan-to'g'ri Arduino platasiga ulab bo'lmaydi? Rele moduli qanday qilib past kuchlanishli Arduinoni yuqori kuchlanishdan himoyalaydi?

### 5-topshiriq. Servomotor burchagini boshqarish <Badge type="warning" text="o'rta" />
Servomotor oddiy doimiy tok (DC) motoridan nimasi bilan farq qiladi? Uning o'qini aniq burchakka burish xususiyati aqlli eshik qulfida qanday qo'llaniladi?

### 6-topshiriq. Arduino vs ESP32 taqqosi <Badge type="warning" text="o'rta" />
Siz masofadan turib smartfondan boshqariladigan aqlli choynak yasamoqchisiz. Bu loyiha uchun Arduino Uno yaxshiroqmi yoki ESP32? Sababini tushuntiring.

### 7-topshiriq. Aqlli ko'cha yoritgichi komponentlari <Badge type="warning" text="o'rta" />
Faqat qorong'i tushganda va odam yaqinlashganda yonuvchi aqlli ko'cha chirog'i uchun bitta Sensor, bitta Boshqaruvchi va bitta Aktuator tanlang.

### 8-topshiriq. Avtoturargoh shlagbaumi loyihasi <Badge type="danger" text="qiyin" />
Avtomobil 1 metr masofaga kelganda to'siqni ochuvchi aqlli shlagbaum loyihalashtirilmoqda. Tizimda qaysi masofa sensori va qaysi motor ishlatiladi? Tizimning 4 bosqichli ishlash ketma-ketligini yozing.

### 9-topshiriq. Tashqi quvvat manbai qoidasi <Badge type="danger" text="qiyin" />
Nima sababdan quvvatli motorlarni (masalan, suv nasosi yoki katta servoni) mikrokontrollerning o'zidan emas, alohida tashqi quvvat manbaidan (batareya yoki adapter) quvvatlash shart?

### 10-topshiriq. Mikrokontroller chipining ichki tuzilishi <Badge type="info" text="bonus" />
Mikrokontroller chipi ichida joylashgan 4 ta asosiy qismni (CPU, RAM, Flash xotira, I/O pinlar) sanab o'ting va ularning har biri qanday vazifa bajarishini tushuntiring.

</div>

