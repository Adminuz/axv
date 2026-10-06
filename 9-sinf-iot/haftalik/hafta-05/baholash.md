# 9-sinf (IoT — Buyumlar Interneti): 5-hafta baholash qaydnomasi

**Mavzular:**
1. IoT uchun asosiy qurilmalar: Arduino va Raspberry Pi — mikrokontroller va mikrokompyuter, tuzilishi, OS, dasturlash, modellar, tanlash mezonlari
2. ESP8266 va ESP32 imkoniyatlari: ichki Wi-Fi, Bluetooth, ikki yadro, Station/AP, HTTP/MQTT/WebSocket, interfeyslar, Deep Sleep, `WiFi.h` bilan ulanish
3. Mikrokontroller tushunchasi va IoT qurilmalaridagi o'rni (1-qism): MCU va MPU, kompyuterdan farqi, CPU, Flash/RAM/EEPROM, Input/Output portlar, Arduino UNO tuzilishi

---

## Baholash mezonlari

| Mezon | Tavsif | Maks. ball |
|---|---|---|
| **Arduino va Raspberry Pi** | Mikrokontroller va mikrokompyuter farqi, Arduino UNO va Pi tuzilishi, OS va tillar, 6 mezonli taqqoslash, loyihaga qurilma tanlash va asoslash | 30 ball |
| **ESP8266 va ESP32** | Xususiyatlar jadvali, Station va AP rejimlari, protokollar, Arduino IDE'ga plata qo'shish, Wi-Fi ulanish kodini izohlash, IP va RSSI tahlili, modul tanlash | 35 ball |
| **Mikrokontroller tuzilishi (1-qism)** | MCU ta'rifi, MCU/MPU jadvali va o'xshatish, CPU, Flash/RAM/EEPROM farqi, Input/Output rejimlari, Arduino UNO plata xaritasi, «tugma → LED» tahlili | 35 ball |
| **JAMI** | | **100 ball** |

Dasturdagi shkala: **90–100 — 5**, **71–89 — 4**, **60–70 — 3**, **0–59 — 2**.

---

## O'quvchilar natijalari jadvali

| № | O'quvchi F.I.Sh. | Arduino va Pi (30) | ESP8266/ESP32 (35) | MCU tuzilishi (35) | Jami ball (100) | Izoh |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |
| 9 | | | | | | |
| 10 | | | | | | |
| 11 | | | | | | |
| 12 | | | | | | |

---

## Mentor qaydlari va tahlil

- **Darsdagi asosiy qiyinchiliklar:** o'quvchilar Raspberry Pi Pico va ESP32 ni ko'pincha «mikrokompyuter» deb ataydi — OS bor-yo'qligini asosiy mezon sifatida qayta-qayta so'rang. ESP darsida eng ko'p uchraydigan amaliy xato — Board noto'g'ri tanlangani va Serial Monitor tezligi mos emasligi.
- **Tekshirish usuli:** har bir o'quvchidan «tugma → LED» dasturida ma'lumot yo'lini og'zaki aytib berishni so'rang: port xabar oladi → CPU Flash'dagi dastur bo'yicha tahlil qiladi → port javob beradi; tok o'chsa Flash va RAM'da nima bo'lishini so'rang.
- **Iqtidorli o'quvchilar uchun:** ESP32'da Access Point rejimida oddiy web-sahifa orqali LED boshqarish, Deep Sleep bilan batareya muddatini hisoblash, EEPROM'da tugma bosilishlar sonini saqlash.
