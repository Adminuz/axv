# 13-dars. IoT uchun asosiy qurilmalar: Arduino va Raspberry Pi taqqosi

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga IoT tizimidagi qurilmalar zanjirini (sensor → mikrokontroller/mikrokompyuter → tarmoq → aktuator) eslatib, Arduino (mikrokontroller platformasi) va Raspberry Pi (Linux'da ishlaydigan mikrokompyuter) qurilmalarining tuzilishi, imkoniyatlari, cheklovlari va qo'llanish sohalarini o'rgatish; loyiha uchun qurilma tanlash mezonlarini tushuntirish.
- **Kutiladigan natija:** O'quvchilar Arduino UNO (ATmega328P, `setup()`/`loop()`, raqamli/analog/PWM pinlar) va Raspberry Pi (ARM protsessor, RAM, microSD, Raspberry Pi OS, GPIO, HDMI/USB/Ethernet/Wi-Fi) tuzilishini tushuntiradi; ikki qurilmani 6 ta mezon bo'yicha taqqoslaydi; berilgan loyiha uchun mos qurilmani asoslab tanlaydi.
- **Vaqt taqsimoti:**
  - Takrorlash (DIP switch, Arduino bilan 2 bit): 10 daqiqa
  - IoT qurilmalari zanjiri: sensor, mikrokontroller, mikrokompyuter, aktuator: 10 daqiqa
  - Arduino: platforma, plata, IDE, pinlar: 15 daqiqa
  - Raspberry Pi: tuzilishi, OS, modellar, dasturlash: 15 daqiqa
  - Taqqoslash va qurilma tanlash mezonlari (amaliy mashq): 25 daqiqa
  - Xulosa: 5 daqiqa

> Manba: o'quv dasturi — 2.1 «IoT uchun asosiy qurilmalar (Arduino, ESP8266, ESP32, Raspberry Pi)» («Har bir qurilmaning texnik imkoniyatlarini tahlil qilish ... IoT loyihalarida optimal qurilmani tanlash»); o'quv qo'llanma — 2.1-bo'lim (qurilmalar jadvali: tavsif, afzallik, cheklov, qo'llanish; Arduino platformasi; Raspberry Pi tuzilishi, OS, modellar jadvali; «Oddiy IoT loyihalarini yaratish uchun kerakli qurilmani tanlash mezonlari»). ESP8266/ESP32 — 14-dars.

---

## Mentor konspekti

### 1. IoT qurilmalari zanjiri (qo'llanma 2.1)

- **Sensorlar** — harorat, namlik, yorug'lik, bosim, harakat, gaz kabi fizik ko'rsatkichlarni sezib, raqamli ma'lumotga aylantiradi.
- **Mikrokontrollerlar** (Arduino, ESP32, STM32) — kichik, kam quvvatli; signallarni qayta ishlaydi, algoritm bo'yicha qaror qabul qiladi, aktuatorlarni boshqaradi.
- **Mikrokompyuterlar** (Raspberry Pi) — kuchliroq; murakkab hisob-kitob, sun'iy intellekt modellari, katta hajmdagi ma'lumot.
- **Aktuatorlar** — jismoniy amal: chiroq yoqish, eshik qulflash, nasos, motor.
- **Tarmoq modullari** — Wi-Fi, Bluetooth, LoRaWAN, ZigBee, NFC, mobil tarmoq.

### 2. Arduino

- **Ochiq kodli (open-source) platforma**: apparat (Arduino platalari) + dasturiy qism (**Arduino IDE**).
- Platalar: Uno, Mega, Nano, Micro, Due. Eng mashhuri — **Arduino Uno**, markazida **ATmega328P** mikrokontrolleri.
- Pinlar: **raqamli** (LED, tugma), **analog kirish** (harorat, yorug'lik darajasi), **PWM** (motor tezligi, LED yorqinligi).
- Dastur C/C++ ga o'xshash sintaksisda: `setup()` — bir marta, `loop()` — doimiy takror. USB orqali yuklanadi va darhol ishlaydi.
- Afzallik: oson, arzon, boshlovchilarga qulay, ko'p kutubxona va modul (DHT, LCD, servo, GSM, OLED).
- Cheklov: **ichida Wi-Fi yoki Bluetooth yo'q** (qo'shimcha modul kerak), hisoblash quvvati past.

```cpp
// Arduino UNO: 13-pindagi LED har soniyada yonib-o'chadi
void setup() {
  pinMode(13, OUTPUT);      // bir marta: pin chiqish rejimida
}
void loop() {               // cheksiz takrorlanadi
  digitalWrite(13, HIGH);   // LED yonadi
  delay(1000);
  digitalWrite(13, LOW);    // LED o'chadi
  delay(1000);
}
```

### 3. Raspberry Pi

- **Kichik o'lchamli, arzon, lekin kuchli mikrokompyuter**; Raspberry Pi Foundation ishlab chiqqan; maqsad — kompyuterni o'rganishni sodda va hammabop qilish.
- Tuzilishi: **ARM arxitekturali protsessor** («miya»), **GPU** (video va grafika), **RAM**, **microSD karta** (OS va doimiy ma'lumot).
- Interfeyslar: **GPIO pinlar**, USB, HDMI, Ethernet, Wi-Fi, Bluetooth, kamera va ekran portlari.
- **Operatsion tizim:** Raspberry Pi OS (Linux asosida); Ubuntu va boshqalar ham. Multitasking — bir vaqtda bir nechta dastur.
- Dasturlash: Python (eng qulay, kutubxonalar oldindan o'rnatilgan: RPi.GPIO, gpiozero), C/C++, Java, Node.js.
- Afzallik: kamera, ekran, grafik interfeys, AI modellari, web-server.
- Cheklov: **narxi yuqoriroq, energiya ko'p sarflaydi, boshqaruvi murakkab**.

Modellar (qo'llanma jadvali):

| Model | Protsessor | RAM | Qo'llanish |
|---|---|---|---|
| Zero / Zero W | 1 yadroli ARM11 | 512 MB | oddiy sensor, mini IoT |
| 3 Model B+ | 4 yadro 1.4 GHz | 1 GB | aqlli uy, kamera, monitoring |
| 4 | 4 yadro 1.5 GHz | 2–8 GB | IoT gateway, web-server, robototexnika |
| 5 | yangi ARM CPU | 4–8 GB | AI, yirik IoT loyihalar |
| Pico / Pico W | RP2040 **mikrokontroller** | 264 KB SRAM | real vaqt, portativ |

Diqqat: **Pico — mikrokompyuter emas, mikrokontroller** (OS yo'q).

```python
# Raspberry Pi: gpiozero kutubxonasi bilan GPIO17 dagi LED
from gpiozero import LED
from time import sleep

led = LED(17)
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
```

Bir xil vazifa, ikki yondashuv: Arduino'da kod to'g'ridan-to'g'ri chipda ishlaydi; Raspberry Pi'da Python dasturi Linux ichida, boshqa dasturlar bilan birga ishlaydi.

### 4. Taqqoslash

| Mezon | Arduino UNO | Raspberry Pi 4 |
|---|---|---|
| Turi | mikrokontroller platformasi | mikrokompyuter |
| OS | yo'q — bitta dastur `loop()` da | Raspberry Pi OS (Linux) |
| Tarmoq | ichida yo'q, modul kerak | Wi-Fi, Bluetooth, Ethernet bor |
| Dasturlash | Arduino IDE, C/C++ | Python, C/C++, Java, Node.js |
| Energiya | juda kam | ko'p, odatda elektrga ulangan |
| Narx | arzon | qimmatroq |
| Kuchli tomoni | sensor/aktuator, real vaqt, soddalik | kamera, video, AI, server, gateway |

O'xshatish: Arduino — **svetofor boshqaruvchisi** (bitta vazifani to'xtovsiz va aniq bajaradi), Raspberry Pi — **kichik ofis kompyuteri** (ko'p ishni bajaradi, lekin elektr va sozlash talab qiladi).

### 5. Qurilma tanlash mezonlari (qo'llanma)

1. **Murakkablik:** oddiy (bir necha sensor + 1 aktuator) → Arduino yoki Pi Pico; murakkab (videokuzatuv, aqlli uy markazi) → Raspberry Pi 3/4.
2. **Internetga ulanish:** Wi-Fi/Ethernet kerak bo'lsa → ichida Wi-Fi bor qurilma (ESP8266/ESP32, Raspberry Pi).
3. **Energiya:** batareyada ishlasa — kam quvvatli (ESP32 energiya tejash rejimi); Raspberry Pi — stasionar, elektrga ulangan.
4. **Sensor va aktuator mosligi:** GPIO soni, analog/raqamli pinlar, SPI, I2C, PWM.
5. **Dasturlash va qo'llab-quvvatlash:** kutubxonalar, jamoatchilik.
6. **Byudjet:** oddiy loyiha — arzon mikrokontroller.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Zanjirni to'ldiring (oson)
Aqlli issiqxona: tuproq namligi sensori, mikrokontroller, Wi-Fi, suv nasosi. Har birini IoT zanjiridagi roliga ajrating.

**Yechim:**
Namlik sensori — **sensor** (o'lchaydi); mikrokontroller — **qayta ishlash va qaror** («quruq bo'lsa nasosni yoq»); Wi-Fi — **tarmoq** (ma'lumotni bulutga/telefonga); suv nasosi — **aktuator** (jismoniy harakat).

### 2-topshiriq. Kim ekanini toping (oson)
Ta'riflar: (a) «Linux'da ishlaydi, HDMI va kamera porti bor»; (b) «markazida ATmega328P, `setup()` va `loop()`»; (c) «RP2040, OS yo'q, 264 KB SRAM».

**Yechim:**
(a) Raspberry Pi (3/4/5); (b) Arduino UNO; (c) Raspberry Pi Pico — mikrokontroller.

### 3-topshiriq. Taqqoslash jadvali (o'rta)
Arduino UNO va Raspberry Pi 4 ni 6 mezon bo'yicha (OS, tarmoq, dasturlash tili, energiya, narx, kuchli tomoni) jadvalda taqqoslang va har qurilmaga bitta loyiha misolini yozing.

**Yechim:**
Konspektdagi 4-bo'lim jadvali. Misollar: Arduino — tugma bilan svetofor, harorat sensori + LED ogohlantirish; Raspberry Pi — videokuzatuv kamerasi, uy serveri, IoT gateway.

### 4-topshiriq. Loyihaga qurilma tanlang (qiyin)
Uchta loyiha: (1) sinfdagi haroratni ko'rsatuvchi LED indikator; (2) maktab kirishida yuzni taniydigan kamera; (3) daladagi, batareyada ishlaydigan, Wi-Fi orqali namlik yuboradigan sensor. Har biriga qurilma tanlang va kamida 2 mezon bilan asoslang.

**Yechim:**
1. **Arduino UNO** — oddiy, internet shart emas, arzon, analog kirish bor.
2. **Raspberry Pi 4** — kamera porti, kuchli protsessor, AI modeli (OS kerak), elektrga ulangan.
3. **ESP32 (yoki ESP8266)** — ichida Wi-Fi, energiya tejash (Deep Sleep), arzon; Arduino'ga Wi-Fi yo'q, Raspberry Pi batareyada ko'p sarflaydi. (ESP — keyingi dars mavzusi, shu yerda ko'prik qilinadi.)

---

## Tezkor nazorat savollari

1. Mikrokontroller va mikrokompyuterning asosiy farqi?
   - *Javob:* Mikrokompyuter (Raspberry Pi) to'liq OS'da ishlaydi va kuchliroq; mikrokontroller (Arduino) bitta dasturni to'g'ridan-to'g'ri bajaradi, kam quvvat sarflaydi.
2. Arduino UNO markazida qaysi chip?
   - *Javob:* ATmega328P.
3. Arduino'ning asosiy cheklovi?
   - *Javob:* Ichida Wi-Fi/Bluetooth yo'q, hisoblash quvvati past.
4. Raspberry Pi qaysi operatsion tizimda ishlaydi?
   - *Javob:* Raspberry Pi OS (Linux asosida).
5. Batareyada uzoq ishlaydigan sensor uchun nega Raspberry Pi 4 mos emas?
   - *Javob:* Energiyani ko'p sarflaydi, odatda elektrga ulangan holda ishlatiladi.

---

## Keng tarqalgan xatolar va ularning oldini olish

- **«Raspberry Pi ham mikrokontroller»:** Pi 3/4/5 — mikrokompyuter; faqat Pico — mikrokontroller.
- **«Arduino internetga o'zi ulanadi»:** UNO'da Wi-Fi yo'q — modul yoki ESP kerak.
- **Eng kuchli qurilmani har doim tanlash:** oddiy vazifaga Raspberry Pi — qimmat, ko'p energiya, ortiqcha murakkablik.
- **Raspberry Pi'ni to'satdan elektrdan uzish:** OS bor — microSD buzilishi mumkin; to'g'ri o'chirish kerak (`sudo shutdown now`).
- **Pinlar kuchlanishini adashtirish:** Raspberry Pi GPIO — 3.3 V, Arduino UNO — 5 V; 5 V signalni to'g'ridan-to'g'ri Pi GPIO'ga berish xavfli.
