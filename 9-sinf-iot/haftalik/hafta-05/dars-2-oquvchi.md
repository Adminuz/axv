# 14-dars. ESP8266 va ESP32 imkoniyatlari

> Tirnoqdek chip, ichida esa Wi-Fi, ba'zan Bluetooth ham. Aqlli rozetka, aqlli lampa va ko'plab «aqlli» uy jihozlari ichida aynan shunday modullar ishlaydi. Bugun ESP8266 va ESP32 bilan tanishamiz.

## Dars xulosasi

- **ESP8266** — Espressif Systems ishlab chiqqan, **ichida Wi-Fi** bor 32-bitli arzon mikrokontroller; versiyalari: ESP-01, ESP-12E, **NodeMCU**.
- **ESP32** — keyingi avlod: **Wi-Fi + Bluetooth**, **ikki yadroli** protsessor (160–240 MHz), ko'p GPIO va interfeyslar.
- ESP32 ichida: ADC, DAC, PWM, SPI, I2C, UART, touch pinlar, Hall sensori, ichki harorat sensori.
- Wi-Fi rejimlari: **Station** (routerga ulanadi) va **Access Point** (o'zi tarmoq yaratadi).
- Protokollar: **HTTP**, **MQTT** (IoT uchun eng qulay), **WebSocket**.
- **Deep Sleep** — juda kam quvvat, uzoq muddat batareyada ishlash.
- Dasturlash: Arduino IDE (`WiFi.h`, `ESP8266WiFi.h`), ESP-IDF, MicroPython, Lua.

## Qo'shimcha ma'lumot

### 1. Wi-Fi'ning ikki rejimi
**Station** rejimini telefoningizga o'xshatish mumkin: u uydagi routerga ulanadi va internetga chiqadi. **Access Point** rejimida esa modul o'zi kichik «router»ga aylanadi — telefoningiz unga ulanadi. Bu internet yo'q joyda (dala, garaj) qurilmani boshqarish uchun juda qulay.

### 2. Wi-Fi'ga ulanish qanday kechadi?

```cpp
#include <WiFi.h>          // ESP8266 uchun: <ESP8266WiFi.h>
const char* ssid  = "Maktab_WiFi";   // namuna
const char* parol = "********";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, parol);                    // 1. ulanishni boshlash
  while (WiFi.status() != WL_CONNECTED) {     // 2. ulanguncha kutish
    delay(500);
    Serial.print(".");
  }
  Serial.println(WiFi.localIP());   // 3. router bergan IP-manzil
  Serial.println(WiFi.RSSI());      // 4. signal kuchi (dBm)
}
void loop() { }
```

Bosqichlar: SSID va parol → router bilan autentifikatsiya → **DHCP** IP-manzil beradi → qurilma ma'lumot almashishga tayyor.

### 3. RSSI — signal kuchi
RSSI manfiy son bilan o'lchanadi (dBm): **−40** — juda kuchli, **−60** — yaxshi, **−70 dan past** — beqaror. Agar Serial Monitor'da −80 chiqsa, qurilmani routerga yaqinroq qo'ying.

### 4. Qachon qaysi biri?

| Vaziyat | Tanlov |
|---|---|
| Oddiy Wi-Fi rele, bitta sensor | ESP8266 |
| Telefon bilan Bluetooth kerak | ESP32 |
| Ko'p sensor + ekran + bulut bir vaqtda | ESP32 |
| Eng arzon variant | ESP8266 |

### 5. Odatiy xatolar
- Arduino IDE'da **Board** noto'g'ri tanlangan (Arduino Uno qolib ketgan).
- Serial Monitor tezligi kodga mos emas (115200 bo'lishi kerak) — ekranda «g'alati belgilar».
- 5 GHz Wi-Fi'ga ulanishga urinish — ESP modullari odatda 2.4 GHz tarmoq bilan ishlaydi.
- Parolni kod bilan birga internetga yuklab qo'yish.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| ESP8266 | Ichida Wi-Fi bor arzon 32-bitli mikrokontroller |
| ESP32 | Wi-Fi + Bluetooth, ikki yadroli kuchliroq mikrokontroller |
| NodeMCU | USB bilan qulay ulanadigan ESP plata versiyasi |
| Station rejimi | Modul mavjud Wi-Fi routerga ulanadi |
| Access Point (AP) | Modul o'zi Wi-Fi tarmoq yaratadi |
| MQTT | IoT uchun tez va kam energiya sarflaydigan protokol |
| Deep Sleep | Juda kam quvvat sarflaydigan «chuqur uyqu» rejimi |
| BLE | Bluetooth Low Energy — kam energiyali Bluetooth |
| DHCP | Tarmoqqa ulangan qurilmaga avtomatik IP beruvchi xizmat |
| RSSI | Wi-Fi signal kuchi, dBm da |
| Dual-core | Ikki yadroli protsessor |

## Bilasizmi?

- ESP8266 2014-yilda paydo bo'lganda juda arzonligi tufayli ixlosmandlar orasida tez tarqaldi: birinchi paytlarda uning hujjatlari asosan xitoy tilida bo'lgan va jamoatchilik ularni o'zi tarjima qilgan.
- Espressif — Shanxaydagi kompaniya; ESP32 chiplari bugun ko'plab aqlli uy jihozlari ichida ishlaydi.
- ESP32 ichidagi «touch» pinlar barmoq tegishini sezadi — oddiy sim yoki folga parchasini sensor tugmaga aylantirish mumkin.
- Deep Sleep rejimida ESP32 bir necha mikroamper tok sarflaydi — shuning uchun batareyali sensorlar oylab ishlay oladi.

## Topshiriqlar

### 1. Kimniki? · oson
Xususiyatlarni ESP8266 yoki ESP32 ga ajrating: Bluetooth; 80 MHz; ikki yadro; Hall sensori; ~17 GPIO; DAC.

**Kutiladigan natija:** 2 ustunli ro'yxat.

### 2. Rejimni toping · oson
(1) Sensor ma'lumotni uydagi router orqali bulutga yuboradi; (2) dalada telefon to'g'ridan-to'g'ri modulga ulanadi. Qaysi Wi-Fi rejimi?

**Kutiladigan natija:** 2 ta javob va sabab.

### 3. Protokollar · oson
HTTP, MQTT va WebSocket'ni bir jumladan tushuntiring.

**Kutiladigan natija:** 3 ta jumla.

### 4. Versiyalar · oson
ESP8266 ning 3 ta va ESP32 ning 3 ta modul versiyasini yozing.

**Kutiladigan natija:** 6 ta nom.

### 5. Kod o'qish · o'rta
Wi-Fi ulanish dasturidagi har bir qatorni o'z so'zlaringiz bilan izohlang.

**Kutiladigan natija:** qatorma-qator izoh.

### 6. Bashorat qiling · o'rta
Parol noto'g'ri yozilgan. Serial Monitor'da nima ko'rinadi va nega?

**Kutiladigan natija:** 1–2 jumla javob.

### 7. RSSI tahlili · o'rta
Uch xonada o'lchandi: −45, −68, −82 dBm. Qaysi xonada aloqa yaxshi, qayerda beqaror? Nima qilish kerak?

**Kutiladigan natija:** 3 ta xulosa va maslahat.

### 8. Arduino IDE sozlash · o'rta
Arduino IDE'ga ESP32 platasini qo'shish bosqichlarini tartib bilan yozing (Preferences → Boards Manager → Board → Port).

**Kutiladigan natija:** 4 bosqichli ro'yxat.

### 9. Loyihaga modul · qiyin
(1) Wi-Fi rele bilan chiroq; (2) Bluetooth'li fitnes bilaguzuk; (3) 6 ta sensorli issiqxona + ekran + bulut. ESP8266 yoki ESP32 ni tanlang va asoslang.

**Kutiladigan natija:** 3 ta asoslangan tanlov.

### 10. Xatoni toping · qiyin
Do'stingizning kodi: `#include <WiFi.h>`, plata — NodeMCU (ESP8266), Board menyusida «Arduino Uno» tanlangan, Serial Monitor 9600. Kamida 3 ta xatoni toping.

**Kutiladigan natija:** 3 ta xato va tuzatish.

### 11. Simulyatorda sinash · qiyin
Wokwi simulyatorida ESP32 loyihasini oching va Wi-Fi ulanish kodini ishga tushiring (simulyatordagi tarmoq nomi bilan). IP va RSSI ni yozib oling.

**Kutiladigan natija:** skrinshot va 2 ta qiymat.

### 12. Batareya hisobi · bonus
Sensor har 10 daqiqada 1 soniya uyg'onib ma'lumot yuboradi, qolgan vaqt Deep Sleep'da. Bir soatda u necha soniya «uyg'oq»? Nega bu batareyani tejaydi?

**Kutiladigan natija:** hisob va 2 jumla izoh.

## O'zingizni tekshiring

1. ESP8266 ning asosiy afzalligi va cheklovi nima?
2. ESP32 ESP8266 dan qaysi jihatlari bilan ustun?
3. Station va Access Point rejimlarini farqlang.
4. Nega MQTT IoT uchun qulay?
5. DHCP nima qiladi?
6. RSSI qiymati qachon «yomon» hisoblanadi?
7. Deep Sleep qaysi loyihalar uchun muhim?

## Uyga vazifa

ESP8266 va ESP32 taqqoslash jadvalini (7 xususiyat) tuzing, Wi-Fi ulanish kodini qatorma-qator izohlang va 3 ta loyihaga mos modulni asoslab tanlang (20–30 daqiqa). Batafsil — haftalik uyga vazifada.
