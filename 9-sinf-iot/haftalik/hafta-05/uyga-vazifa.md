# 5-hafta: Uyga vazifalar to'plami

Mazkur haftada o'tilgan darslar bo'yicha mustaqil bajarish uchun topshiriqlar. Har bir vazifa 20–30 daqiqaga mo'ljallangan. Natijani hujjat (jadval, rasm) yoki Tinkercad/Wokwi havolasi va skrinshotlar bilan topshiring.

---

## 13-dars: Arduino va Raspberry Pi

1. Arduino UNO va Raspberry Pi 4 ni 6 mezon bo'yicha taqqoslovchi jadval tuzing: OS, protsessor/RAM, tarmoq, dasturlash tili, energiya, narx.
2. Har bir qurilma uchun 2 tadan real IoT loyiha misolini yozing va nega aynan shu qurilma tanlanganini 1 jumlada asoslang.
3. Raspberry Pi Pico nega «mikrokompyuter» emas, balki mikrokontroller ekanini 2–3 jumlada tushuntiring.

---

## 14-dars: ESP8266 va ESP32 imkoniyatlari

1. ESP8266 va ESP32 taqqoslash jadvalini tuzing (7 xususiyat: tezlik, yadrolar, Wi-Fi, Bluetooth, GPIO, ADC, UART).
2. Wi-Fi'ga ulanish dasturini (`WiFi.h`) qatorma-qator izohlang; Station va Access Point rejimlariga bittadan misol keltiring.
3. 3 ta loyihaga mos modulni tanlang va asoslang: (a) Wi-Fi rele; (b) Bluetooth'li qadam sanagich; (c) 5 ta sensorli ob-havo stansiyasi + ekran + bulut.
4. Qo'shimcha: Wokwi'da ESP32 Wi-Fi ulanish kodini ishga tushirib, IP va RSSI qiymatlarini skrinshot bilan yuboring.

---

## 15-dars: Mikrokontroller tushunchasi (1-qism)

1. Mikrokontroller va mikroprotsessorni 5 mezon bo'yicha taqqoslovchi jadval tuzing (tuzilishi, vazifasi, tezlik/quvvat, narx, misollar).
2. Arduino UNO rasmida ATmega328P, raqamli pinlar (14), analog pinlar (6), 5V/3.3V/GND, USB-B va kvars generatorni belgilang.
3. «Tugma → LED» dasturida Input va Output qatorlarini, RAM'dagi o'zgaruvchini va CPU qaror qabul qiladigan qatorni belgilang. Tok o'chib-yonsa nima saqlanishini yozing.
4. Uyingizdan ichida mikrokontroller ishlaydigan 5 ta qurilmani toping va har birining «bitta vazifasini» yozing.

---

## Mentor uchun

### Baholash mezonlari (Jami 100 ball)
- **13-dars vazifasi (30 ball):** jadval 6 mezonli va to'g'ri (Arduino — OS yo'q, modul kerak; Pi — Linux, Wi-Fi/BT/Ethernet), loyiha misollari mantiqiy asoslangan, Pico — RP2040 mikrokontroller ekani tushuntirilgan.
- **14-dars vazifasi (35 ball):** jadvaldagi qiymatlar (80 va 160–240 MHz, 1 va 2 yadro, BT faqat ESP32, ~17 va ~34+ GPIO), kod izohi (`WiFi.begin`, `WL_CONNECTED`, `localIP`, `RSSI`), Station/AP misollari, tanlov: (a) ESP8266, (b) ESP32, (c) ESP32.
- **15-dars vazifasi (35 ball):** MCU/MPU jadvali to'liq, plata xaritasi 6 qismni to'g'ri ko'rsatadi, kod qismlari to'g'ri belgilangan (Flash saqlanadi, RAM yo'qoladi), 5 ta qurilma va vazifalari.

Dasturdagi shkala: **90–100 — 5**, **71–89 — 4**, **60–70 — 3**, **0–59 — 2**.

### Eslatma
- 15-dars — mavzuning 1-qismi. Sensor → MCU → aktuator → bulut zanjiri va analog/raqamli pinlar 16-darsda chuqurlashtiriladi, shuning uchun bu haftada faqat tuzilish va qismlar baholanadi.
