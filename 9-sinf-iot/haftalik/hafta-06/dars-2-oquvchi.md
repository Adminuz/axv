# 17-dars. ESP8266 va ESP32 mikrokontrollerlari haqida umumiy tushuncha

> Kichkina va arzon chip butun uyni internetga ulashi mumkin. Bugun ESP8266 va ESP32 ning farqlarini, pinlarini va ma'lumotni bulutga yuborish yo'lini o'rganamiz.

## Dars xulosasi

- ESP8266 va ESP32 — ichki Wi-Fi'li arzon mikrokontrollerlar.
- ESP32: 2 yadro, Bluetooth, ko'proq xotira va pin.
- Ikkalasi 3,3 V da ishlaydi — 5 V ulamang.
- Pin turlari: GPIO, ADC, PWM, I2C, SPI.
- Ma'lumot JSON ko'rinishida HTTP yoki MQTT bilan yuboriladi.
- Dastur: Arduino IDE (C/C++) yoki MicroPython; energiya uchun Deep Sleep.

## Qo'shimcha ma'lumot

### ThingSpeak, Blynk
Sensor ma'lumotini ko'rsatuvchi bulut platformalari.

### Level shifter
5 V va 3,3 V orasida signal darajasini moslovchi qurilma.

### MicroPython
Python'ning mikrokontrollerlar uchun yengil versiyasi.

### OTA
Simsiz (Wi-Fi orqali) dastur yangilash.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| ESP8266 | Wi-Fi'li 32-bitli mikrokontroller |
| ESP32 | 2 yadroli, Wi-Fi + Bluetooth |
| GPIO | Umumiy kirish-chiqish pini |
| JSON | Matnli ma'lumot formati |
| HTTP | Veb protokoli |
| MQTT | IoT xabar protokoli |
| MicroPython | Mikrokontroller uchun Python |
| Deep Sleep | Chuqur uyqu rejimi |

## Bilasizmi?

- ESP32 da ichki harorat sensori va Hall sensori bor (qo'llanma).
- Ko'p aqlli rozetka va lampalarning ichida ESP8266/ESP32 turadi.
- MQTT «publish/subscribe» tamoyilida ishlaydi: qurilma mavzuga yozadi, boshqalar o'qiydi.

## Topshiriqlar

### 1. Farqlar · oson

ESP32 ning ESP8266 dan 3 ta ustunligini yozing.

**Kutiladigan natija:** 2 yadro, Bluetooth, ko'p pin

### 2. Kuchlanish · oson

ESP ning ish kuchlanishi qancha?

**Kutiladigan natija:** 3,3 V

### 3. Pin · oson

GPIO nima?

**Kutiladigan natija:** Raqamli kirish-chiqish pini

### 4. Format · oson

Sensor ma'lumoti qaysi formatda yuboriladi?

**Kutiladigan natija:** JSON

### 5. Tanlov · o'rta

Faqat Wi-Fi kerak bo'lgan arzon rozetka uchun qaysi chip?

**Kutiladigan natija:** ESP8266

### 6. Protokol · o'rta

HTTP va MQTT ni qisqa ta'riflang.

**Kutiladigan natija:** Veb protokol / IoT xabar protokoli

### 7. Sxema · o'rta

DHT11 ni ESP ga ulash sxemasini yozing.

**Kutiladigan natija:** VCC-3,3V, GND-GND, DATA-pin

### 8. JSON · o'rta

Harorat va bosimni JSON ga yozing.

**Kutiladigan natija:** {"t":..,"p":..}

### 9. Loyiha · qiyin

Aqlli chiroq loyihasi elementlarini sanang.

**Kutiladigan natija:** ESP, sensor, rele, LED

### 10. Til · qiyin

Arduino IDE va MicroPython farqini yozing.

**Kutiladigan natija:** C/C++ va Python

### 11. Energiya · qiyin

Batareyali qurilmada energiyani tejash usulini yozing.

**Kutiladigan natija:** Deep Sleep

### 12. O'z loyihangiz · bonus

ESP asosida o'z IoT g'oyangizni sxema bilan tushuntiring.

**Kutiladigan natija:** Mustaqil loyiha

## O'zingizni tekshiring

1. ESP32 va ESP8266 farqi?
2. Ish kuchlanishi?
3. Pin turlari?
4. JSON nima?
5. HTTP va MQTT?
6. Deep Sleep nima?

## Uyga vazifa

ESP8266 va ESP32 bo'yicha qiyoslash va loyiha rejasini tuzing (30–40 daqiqa). To'liq shart: `uyga-vazifa.md`.
