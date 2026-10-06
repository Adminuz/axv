# 17-dars. ESP8266 va ESP32 mikrokontrollerlari haqida umumiy tushuncha

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga ESP8266 va ESP32 ning IoT tizimlaridagi o'rnini, asosiy farqlarini (tezlik, yadrolar, xotira, GPIO soni, Bluetooth), pin turlarini (GPIO, ADC, PWM, I2C, SPI), 3,3 V bilan ishlash qoidasini, sensor ma'lumotini JSON ko'rinishida HTTP/MQTT orqali bulutga yuborish tartibini, Arduino IDE va MicroPython tanlovini hamda energiya tejash g'oyasini tushuntirish.
- **Kutiladigan natija:** O'quvchilar eSP8266 va ESP32 ni 5 ta xususiyat bo'yicha solishtiradi; 3,3 V qoidasini va 5 V ulashning xavfini tushuntiradi; gPIO, ADC, PWM, I2C, SPI pinlarining vazifasini ayta oladi; sensor ma'lumotini JSON ko'rinishida yozadi va protokolni (HTTP/MQTT) tanlaydi; arduino IDE va MicroPython farqini hamda Deep Sleep g'oyasini biladi.
- **Vaqt taqsimoti:**
  - 14, 16-darslar: ESP, Wi-Fi, ADC, PWM: 10 daqiqa
  - ESP'ning IoT dagi o'rni va farqlar: 10 daqiqa
  - Pinlar va 3,3 V qoidasi: 20 daqiqa
  - Ma'lumot yuborish: JSON, HTTP, MQTT: 15 daqiqa
  - Dasturlash tanlovi, Deep Sleep, xulosa: 25 daqiqa

> Manba: o'quv dasturi — «ESP8266 va ESP32 mikrokontrollerlari haqida umumiy tushuncha»; o'quv qo'llanma — 2.3-bo'lim (IoT'dagi o'rni, asosiy farqlar jadvali: tezlik, yadrolar, SRAM, GPIO ~17 va ~34+; GPIO, ADC, PWM, I2C, SPI; dual-core va Bluetooth; Arduino IDE va MicroPython; DHT11/BMP280/MQ sensorlari; aqlli chiroq va ob-havo stansiyasi; HTTP/MQTT va JSON), 2.2-bo'lim (3,3 V xavfi, Wi-Fi termometr loyihasi). 14-darsdagi Wi-Fi kodi takrorlanmaydi. Deep Sleep namunasi ESP32 Arduino hujjatiga ko'ra qo'shildi; ESP kodlari plata yoki simulyatorda ishga tushirilmagan (MicroPython va JSON namunasining Python sintaksisi tekshirilgan).

---

## Mentor konspekti

### 1. ESP8266 va ESP32: o'rni va asosiy farqlar

ESP8266 va ESP32 — IoT tizimlarining eng muhim qurilmalaridan: **kichik, arzon, ichki Wi-Fi'li**; sensorlar va aktuatorlarni simsiz tarmoq orqali boshqaradi. Aqlli uyda harorat, namlik, yorug'lik va harakat sensorlaridan ma'lumot yig'ib bulutga uzatadi, foydalanuvchi telefonidan nazorat qiladi; sanoatda masofaviy monitoring uchun ishlatiladi. **ESP32 — ESP8266 ning halefi**: ikki yadroli protsessor, katta xotira, tezkor Wi-Fi va Bluetooth. ESP8266 oddiy loyihalar uchun yetarli va arzon, lekin GPIO, RAM va tezligi cheklangan. Qo'llanma jadvaliga ko'ra: tezlik — 80 MHz (ESP8266) va 160–240 MHz (ESP32); yadro — 1 va 2; SRAM — cheklangan va katta; Bluetooth — yo'q va bor; GPIO — taxminan 17 va 34+. Aniq raqamlar modelga qarab farq qiladi — plata hujjatini tekshiring. Tanlash qoidasi: oddiy sensor yoki rozetka → ESP8266; Bluetooth, ko'p pin yoki murakkab hisob kerak → ESP32.

```text
Xususiyat       ESP8266      ESP32
Tezlik          80 MHz       160-240 MHz
Yadro           1            2
SRAM            cheklangan   katta
Bluetooth       yo'q         bor (Classic + BLE)
GPIO            ~17          ~34+
Kuchlanish      3.3 V        3.3 V
```

> Professional maslahat: Jadvaldagi raqamlar taxminiy: «NodeMCU» va «DevKit» platalarida chiqarilgan pinlar soni boshqacha bo'lishi mumkin.

### 2. Pinlar (GPIO, ADC, PWM, I2C, SPI) va 3,3 V qoidasi

ESP platalari turli **pinlar** orqali sensorlar va aktuatorlarni boshqaradi (qo'llanma): **GPIO** — raqamli signalni o'qish va uzatish (LEDni yoqish); **ADC** — analog signalni raqamga aylantirish (yorug'lik sensori); **PWM** — LED yorqinligi, motor tezligini silliq boshqarish; **I2C** va **SPI** — bir nechta qurilmani (displey, sensor) bir paytda ulash protokollari. **Muhim qoida: ESP8266 ham, ESP32 ham 3,3 V da ishlaydi.** Arduino Uno'dagi kabi 5 V ulasangiz, chip ishdan chiqishi mumkin (qo'llanma: «darhol ishdan chiqadi»). Sensor ham 3,3 V da ishlashi kerak: masalan, DHT11 ning VCC oyog'i plataning 3,3 V iga, GND — GND ga, DATA — raqamli pinga ulanadi. 5 V li signalni 3,3 V pinga bevosita bermang — kuchlanish bo'lgich yoki darajani o'zgartiruvchi (level shifter) kerak. ESP32 da ikki yadro: biri sensorni o'qiydi, ikkinchisi tarmoqni boshqaradi — bir vazifa ikkinchisini to'xtatmaydi.

```text
DHT11            ESP (NodeMCU / DevKit)
VCC   ------->   3.3V        (5V EMAS!)
GND   ------->   GND
DATA  ------->   raqamli pin (masalan, D4)
```

> Professional maslahat: Plata va sensor modeliga qarab pin nomlari (D4, GPIO4) farq qiladi. Ulashdan oldin plata sxemasiga qarang.

### 3. Ma'lumotni bulutga yuborish va dasturlash tanlovi

Sensor ma'lumoti (DHT11, DHT22, BMP280, MQ gaz sensori) ESP orqali **HTTP POST** yoki **MQTT** bilan bulutga uzatiladi. Ma'lumot **JSON** formatida tuziladi — tahlil va vizualizatsiya oson: `{"temperature": 28.5, "humidity": 60}`. Bulutda (ThingSpeak, Blynk kabi platformalar) ma'lumot saqlanadi, grafik chiziladi, ogohlantirish (alert) va avtomatik boshqaruv yoqiladi. Loyihalar (qo'llanma): **aqlli chiroq** (ESP + harakat sensori + rele + LED), **ob-havo stansiyasi** (ESP + DHT/BMP + bulut), **masofadan boshqaruv** (Wi-Fi + HTTP/MQTT + mobil ilova). **Dasturlash:** Arduino IDE — C/C++; MicroPython — Python sintaksisi; kod USB kabel orqali yuklanadi. **Energiya tejash:** batareyali qurilma ko'p vaqt uxlab, faqat o'lchash va yuborish uchun uyg'onadi — ESP32 da bu **Deep Sleep** rejimi (taymer yoki tashqi signal bilan uyg'onish).

```python
from machine import Pin
import time

led = Pin(2, Pin.OUT)   # ichki LED pini modelga bog'liq

while True:
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)
```

> Professional maslahat: MicroPython'da `Pin`, `time` kabi modullar ESP ichida ishlaydi. Pin raqami (masalan, 2) plata modeliga bog'liq — hujjatga qarang.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Solishtirish (oson)
ESP8266 va ESP32 ni 4 ta xususiyat bo'yicha solishtiring.

**Yechim:** Tezlik — 80 MHz va 160–240 MHz; yadro — 1 va 2; Bluetooth — yo'q va bor; GPIO — ~17 va ~34+.

### 2-topshiriq. Kuchlanish (oson)
ESP ga sensorni qaysi kuchlanishdan ulaysiz? 5 V ulansa nima bo'ladi?

**Yechim:** Sensor ham 3,3 V ga ulanadi. 5 V ulansa, ESP chipi ishdan chiqishi mumkin.

### 3-topshiriq. Pin turlari (o'rta)
GPIO, ADC, PWM va I2C ning vazifasini bir gapdan yozing.

**Yechim:** GPIO — raqamli kirish-chiqish; ADC — analogni raqamga aylantirish; PWM — yorqinlik/tezlikni silliq boshqarish; I2C — bir nechta qurilmani ulash protokoli.

### 4-topshiriq. JSON yozish (o'rta)
Harorat 27,5 va namlik 55 qiymatlarini JSON ko'rinishida yozing.

**Yechim:**
```json
{"temperature": 27.5, "humidity": 55}
```

### 5-topshiriq. Loyiha tanlash (qiyin)
Batareyada yillab ishlaydigan oddiy sensor va Bluetooth kerak bo'lgan qurilma uchun qaysi chipni tanlaysiz? Nega?

**Yechim:** Bluetooth kerak bo'lsa — ESP32 (ESP8266 da Bluetooth yo'q). Batareya uchun ko'p vaqt uxlash (Deep Sleep) va faqat o'lchash/yuborish paytida uyg'onish kerak.

### 6-topshiriq. Deep Sleep g'oyasi (bonus)
Ob-havo stansiyasi har 10 daqiqada o'lchaydi. Energiyani qanday tejaysiz?

**Yechim:** O'lchash va yuborishdan keyin ESP32 ni Deep Sleep ga o'tkazib, taymer bilan 10 daqiqadan keyin uyg'otamiz; qolgan vaqt energiya deyarli sarflanmaydi.

---

## Tezkor nazorat savollari

1. ESP32 ESP8266 dan nimasi bilan farq qiladi?
   - *Javob:* Ikki yadro, tezroq, ko'p xotira va pin, Bluetooth bor.
2. ESP qaysi kuchlanishda ishlaydi?
   - *Javob:* 3,3 V.
3. GPIO nima?
   - *Javob:* Raqamli signalni o'qish va uzatish uchun umumiy pin.
4. Ma'lumot qaysi formatda yuboriladi?
   - *Javob:* JSON, HTTP yoki MQTT orqali.
5. Energiya tejash rejimi?
   - *Javob:* Deep Sleep.

---

## Uyga vazifa

1. ESP8266 va ESP32 ni 6 ta xususiyat bo'yicha jadvalda solishtiring.
2. DHT11 ni ESP ga ulash sxemasini daftaringizga chizing va nega 3,3 V ishlatilishini yozing.
3. Harorat 24,0, namlik 48 va bosim 1012 qiymatlarini JSON ko'rinishida yozing.
4. Aqlli chiroq yoki ob-havo stansiyasi loyihasining blok-sxemasini chizing: sensor, ESP, Wi-Fi, bulut, foydalanuvchi.
5. Deep Sleep nima uchun kerakligini 3 jumlada tushuntiring.
