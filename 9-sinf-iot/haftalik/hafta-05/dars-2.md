# 14-dars. IoT uchun asosiy qurilmalar: ESP8266 va ESP32 imkoniyatlari

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga ichida Wi-Fi o'rnatilgan arzon mikrokontrollerlar — ESP8266 va ESP32 (Espressif Systems) imkoniyatlarini o'rgatish: versiyalar (ESP-01, ESP-12E, NodeMCU; ESP-WROOM-32, DevKit v1, ESP32-C3), Wi-Fi rejimlari (Station va Access Point), protokollar (HTTP, MQTT, WebSocket), pinlar va interfeyslar, energiya tejash (Deep Sleep), dasturlash muhitlari; ikki modulni taqqoslash va Arduino IDE'ga ESP platalarini qo'shish.
- **Kutiladigan natija:** O'quvchilar ESP8266 va ESP32 ni 6 ta xususiyat bo'yicha (protsessor tezligi, yadrolar, Bluetooth, GPIO soni, ADC, UART) taqqoslaydi; Station va AP rejimlarini farqlaydi; Arduino IDE'da ESP32/ESP8266 platasini o'rnatish tartibini biladi; Wi-Fi'ga ulanish dasturini o'qib, qatorlarini tushuntiradi va IP-manzil hamda signal kuchini (RSSI) tahlil qiladi.
- **Vaqt taqsimoti:**
  - Takrorlash (Arduino va Raspberry Pi): 10 daqiqa
  - ESP8266: Wi-Fi, versiyalar, rejimlar, protokollar: 15 daqiqa
  - ESP32: Wi-Fi + Bluetooth, ikki yadro, interfeyslar: 15 daqiqa
  - Taqqoslash va tanlash: 10 daqiqa
  - Amaliyot: Arduino IDE'ga ESP qo'shish va Wi-Fi'ga ulanish kodi: 25 daqiqa
  - Xulosa: 5 daqiqa

> Manba: o'quv dasturi — 2.1 «IoT uchun asosiy qurilmalar (Arduino, ESP8266, ESP32, Raspberry Pi)» («Wi-Fi va Bluetooth orqali ulanishni amalga oshirish. Real vaqt rejimida ma'lumot uzatish»); o'quv qo'llanma — 2.1-bo'lim (ESP8266 va ESP32 tavsifi, versiyalar, Station/AP rejimlari, HTTP/MQTT/WebSocket, `ESP8266WiFi.h`, `PubSubClient.h`, ESP32 interfeyslari, dasturlash muhitlari, Deep Sleep), 2.3-bo'lim jadvallari (80 MHz va 160–240 MHz, 1 va 2 yadro, GPIO ~17 va ~34+), 6-bob (`WiFi.h`, `WiFi.begin()`, DHCP, `WiFi.RSSI()` < −70 dBm); uslubiy ko'rsatma — Arduino IDE «Additional boards manager URLs». Ikki yadroli arxitektura, MicroPython va bulutga JSON yuborish batafsil — 17-dars.

---

## Mentor konspekti

### 1. ESP8266 — «internetga ulanish nuqtasi»

- Espressif Systems ishlab chiqqan, **ichiga Wi-Fi moduli o'rnatilgan** arzon, ixcham mikrokontroller; ichida **32-bitli mikroprotsessor**.
- Qo'shimcha tarmoq kartasi kerak emas — IoT uchun juda qulay. Arduino UNO bilan Wi-Fi moduli sifatida ham ishlatiladi.
- **Versiyalar:** ESP-01, ESP-07, ESP-12E, **NodeMCU** (USB orqali ulanadi, qulay pinlar) — bir xil chip, farqi pinlar soni, antenna, xotira.
- **Dasturlash:** Arduino IDE (eng ommabop), Lua (NodeMCU firmware).
- **Kutubxonalar:** `ESP8266WiFi.h` — Wi-Fi ulanishi; `PubSubClient.h` — MQTT orqali uzatish.
- **Cheklov:** pinlari kam, og'ir hisoblashga unchalik mos emas.

### 2. Wi-Fi rejimlari va protokollar

| Rejim | Qanday ishlaydi | Misol |
|---|---|---|
| **Station (client)** | mavjud routerga ulanadi va internetga chiqadi | sensor ma'lumotini bulutga yuborish |
| **Access Point (AP)** | modulning o'zi Wi-Fi tarmoq yaratadi, telefon unga ulanadi | internet yo'q joyda qurilmani boshqarish |

Protokollar: **HTTP/HTTPS** (web-serverga yuborish/olish), **MQTT** (IoT uchun eng qulay: tezkor, kam energiya, broker orqali), **WebSocket** (real vaqtda ikki tomonlama).

### 3. ESP32 — keyingi avlod

- ESP8266 ning **keyingi avlodi**: hisoblash quvvati, tarmoq, xavfsizlik, energiya samaradorligi kuchliroq.
- **Wi-Fi + Bluetooth (BLE va Classic)** birga o'rnatilgan.
- **Ikki yadroli (dual-core) 32-bitli protsessor**: bir yadro sensorni o'qiydi, ikkinchisi tarmoqni boshqaradi (batafsil — 17-dars).
- **Interfeyslar:** ADC, **DAC**, PWM, GPIO, SPI, I2C, UART, **touch** pinlar, **Hall sensori**, ichki **harorat sensori**.
- **Modullar:** ESP-WROOM-32, ESP32-S, ESP32-C3, DevKit v1, NodeMCU-32.
- **Dasturlash:** Arduino IDE, ESP-IDF (professional), MicroPython, Lua, PlatformIO.
- **Cheklov:** Arduino'dan murakkabroq, energiya sarfi ESP8266 dan yuqoriroq.

### 4. Taqqoslash (qo'llanma jadvallari)

| Xususiyat | ESP8266 | ESP32 |
|---|---|---|
| Protsessor tezligi | 80 MHz | 160–240 MHz |
| Yadrolar | 1 | 2 |
| Wi-Fi | bor | bor |
| Bluetooth | yo'q | bor (Classic + BLE) |
| GPIO | ~17 | ~34+ |
| ADC | bitta kanal | ko'p kanal |
| UART | 2 | 2–3 |
| IoT uchun | oddiy qurilmalar | murakkab tizimlar |

Ikkalasi ham HTTP va MQTT ni qo'llab-quvvatlaydi va **Deep Sleep** rejimida juda kam quvvat sarflab, uzoq muddat batareyada ishlay oladi.

Tanlash: oddiy Wi-Fi sensor yoki rele → ESP8266; Bluetooth, ko'p sensor, real vaqt, ko'p vazifa → ESP32.

### 5. Arduino IDE'ga ESP platalarini qo'shish (uslubiy ko'rsatma)

1. **File → Preferences → Additional boards manager URLs** — ESP32/ESP8266 platalari uchun Espressif URL manzili kiritiladi.
2. **Tools → Board → Boards Manager** — «esp32» (yoki «esp8266») qidirilib o'rnatiladi.
3. **Tools → Board** — masalan, «ESP32 Dev Module» yoki «NodeMCU 1.0».
4. **Tools → Port** — USB port tanlanadi; Serial Monitor tezligi — `115200`.

### 6. Wi-Fi'ga ulanish dasturi (`WiFi.h`)

```cpp
#include <WiFi.h>              // ESP8266 da: #include <ESP8266WiFi.h>

const char* ssid  = "Maktab_WiFi";   // namuna: tarmoq nomi
const char* parol = "********";      // parolni kodda ochiq qoldirmang

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, parol);           // Station rejimi: routerga ulanish
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");               // ulanguncha nuqta chiqaradi
  }
  Serial.println();
  Serial.println(WiFi.localIP());    // DHCP bergan IP-manzil
  Serial.println(WiFi.RSSI());       // signal kuchi, dBm
}

void loop() { }
```

Jarayon (qo'llanma): SSID va parol → router bilan autentifikatsiya → **DHCP** orqali IP-manzil → HTTP/MQTT bilan ma'lumot almashish. **RSSI** −70 dBm dan past bo'lsa, aloqa beqaror — qurilmani routerga yaqinlashtirish kerak. IP olinmasa — `WiFi.begin()` ni qayta chaqirish yoki statik IP berish.

Plata qo'lda bo'lmasa — Wokwi simulyatorida ESP32 bilan sinab ko'rish mumkin (uslubiy ko'rsatma manbalarida tavsiya etilgan).

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. ESP8266 yoki ESP32? (oson)
Qaysi biriga tegishli: (a) Bluetooth bor; (b) 80 MHz, 1 yadro; (c) Hall va touch sensor bor; (d) NodeMCU versiyasi mashhur, Lua firmware.

**Yechim:**
(a) ESP32; (b) ESP8266; (c) ESP32; (d) ESP8266 (NodeMCU-32 esa ESP32 versiyasi, lekin Lua firmware odatda ESP8266 NodeMCU bilan bog'liq).

### 2-topshiriq. Station yoki AP? (oson)
(1) Uydagi harorat sensori ma'lumotni bulutga yuboradi; (2) dalada internet yo'q, telefon to'g'ridan-to'g'ri modulga ulanib nasosni yoqadi.

**Yechim:**
(1) **Station** — mavjud routerga ulanadi; (2) **Access Point** — modul o'z tarmog'ini yaratadi.

### 3-topshiriq. Kodni tushuntiring (o'rta)
Wi-Fi ulanish dasturidagi `WiFi.begin`, `while (WiFi.status() != WL_CONNECTED)`, `WiFi.localIP()`, `WiFi.RSSI()` qatorlarini tushuntiring. Serial Monitor'da `.......` dan keyin `192.168.1.37` va `-78` chiqdi — xulosa qiling.

**Yechim:**
`WiFi.begin` — SSID/parol bilan ulanishni boshlaydi; `while` — ulanmaguncha har 0.5 s da nuqta chiqarib kutadi; `localIP` — DHCP bergan manzil (bu yerda 192.168.1.37 — lokal tarmoq); `RSSI` — signal kuchi. −78 dBm < −70 dBm — **aloqa beqaror**, qurilmani routerga yaqinlashtirish kerak.

### 4-topshiriq. Loyihaga modul tanlang (qiyin)
(1) Rele orqali chiroqni telefondan Wi-Fi bilan yoqish; (2) fitnes bilaguzuk: telefon bilan Bluetooth, yurak urishi sensori, batareya; (3) issiqxona: 6 ta sensor, ekran, bulutga yuborish va bir vaqtda mahalliy boshqaruv. Har biriga ESP8266 yoki ESP32 ni tanlab, sababini yozing.

**Yechim:**
1. **ESP8266** — oddiy, Wi-Fi yetarli, arzon.
2. **ESP32** — Bluetooth (BLE) kerak; Deep Sleep bilan batareya tejaladi.
3. **ESP32** — ko'p GPIO va ADC kanallari, ikki yadro (sensorlar + tarmoq bir vaqtda), I2C/SPI ekran uchun.

---

## Tezkor nazorat savollari

1. ESP8266 ning eng asosiy afzalligi?
   - *Javob:* Ichiga Wi-Fi moduli o'rnatilgan, arzon va kichik.
2. ESP32 ni ESP8266 dan nima ajratib turadi?
   - *Javob:* Bluetooth, ikki yadro, 160–240 MHz, ko'proq GPIO va interfeyslar.
3. Station va Access Point rejimi farqi?
   - *Javob:* Station — routerga ulanadi; AP — o'zi tarmoq yaratadi.
4. IoT uchun eng qulay protokol qaysi va nega?
   - *Javob:* MQTT — tezkor va kam energiya sarflaydi.
5. RSSI = −80 dBm nimani bildiradi?
   - *Javob:* Signal kuchsiz (−70 dan past) — aloqa beqaror.

---

## Keng tarqalgan xatolar va ularning oldini olish

- **Board noto'g'ri tanlangan:** «Arduino Uno» tanlangan holda ESP32 ga yuklash — xato. Tools → Board → ESP32 Dev Module.
- **Serial Monitor tezligi mos emas:** `Serial.begin(115200)` bo'lsa, monitor ham 115200 — aks holda «g'alati belgilar».
- **Noto'g'ri kutubxona:** ESP8266 da `WiFi.h` o'rniga `ESP8266WiFi.h`.
- **5 GHz tarmoq:** ESP8266/ESP32 odatda 2.4 GHz Wi-Fi bilan ishlaydi — 5 GHz tarmoqqa ulanmaydi.
- **Parol kodda ochiq va GitHub'ga yuklangan:** parolni alohida faylda saqlash yoki yuklashdan oldin o'chirish.
- **«ESP32 har doim yaxshiroq»:** oddiy rele uchun ESP8266 arzonroq va kam energiya sarflaydi.
