# 15-dars. Mikrokontroller tushunchasi va IoT qurilmalaridagi o'rni (1-qism)

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga mikrokontroller (MCU) tushunchasini, uning mikroprotsessor (MPU) va kompyuterdan farqini, asosiy qismlarini — protsessor (CPU), xotira (Flash/ROM, RAM, EEPROM) va kirish-chiqish portlari (I/O) — hamda bu qismlarning birgalikda ishlashini Arduino UNO (ATmega328P) misolida tushuntirish.
- **Kutiladigan natija:** O'quvchilar mikrokontrollerga ta'rif beradi; MCU va MPU ni 5 mezon bo'yicha (tuzilishi, vazifasi, tezlik/quvvat, narx, misollar) taqqoslaydi; Flash va RAM farqini «darslik va doska» o'xshatishi bilan tushuntiradi; pinning Input va Output rejimini farqlaydi; Arduino UNO platasida ATmega328P, 14 ta raqamli va 6 ta analog pin, quvvat pinlari, USB-B va kvars generatorni ko'rsatadi; «tugma → LED» dasturida qaysi qism qayerda ishlashini aytib beradi.
- **Vaqt taqsimoti:**
  - Takrorlash (ESP8266 va ESP32): 10 daqiqa
  - Mikrokontroller nima: MCU, MPU va kompyuter: 15 daqiqa
  - Asosiy qismlar: CPU, xotira, I/O portlar: 15 daqiqa
  - Arduino UNO tuzilishi (ATmega328P): 10 daqiqa
  - Amaliyot: qismlarni topish, taqqoslash, «tugma → LED» tahlili: 25 daqiqa
  - Xulosa: 5 daqiqa

> Manba: o'quv dasturi — 2.2 «Mikrokontroller tushunchasi va IoT qurilmalaridagi o'rni» («Mikrokontroller tushunchasini o'rganish. Kirish va chiqish signallarini qayta ishlash»); o'quv qo'llanma — 2.2-bo'lim (mikrokontroller ta'rifi, «Shveysariya pichog'i» va «Formula-1 dvigateli» o'xshatishi, kompyuterdan farqi — mikroto'lqinli pech misoli, 1-jadval MCU va MPU, CPU «miya/dirijyor», Flash — darslik, RAM — doska, I/O — «qo'l-oyoq va ko'z-quloq», Input/Output rejimlari), 2.1-bo'lim (Arduino UNO: ATmega328P 8-bit AVR, flash/SRAM/EEPROM, 14 raqamli va 6 analog pin, 5V/3.3V/GND, 7–12V, USB-B, ATmega16U2, 16 MHz). IoT'dagi vazifasi, sensor → aktuator zanjiri, dastur yuklash jarayoni, analog va raqamli pinlar batafsil — 16-dars (2-qism).

---

## Mentor konspekti

### 1. Mikrokontroller nima?

- **Mikrokontroller** — bitta mikrosxema (chip) ichiga joylashtirilgan **ixcham kompyuter**. U atrofdagi qurilmalarni boshqarish uchun yaratilgan.
- Kompyuter inson foydalanishi uchun; mikrokontroller esa **buyumlar ichida yashirinib** ishlaydi: kir yuvish mashinasi, avtomobil tormoz tizimi, masofadan boshqarish pulti.
- «Hamma narsa o'zida»: bitta kristallda **CPU + xotira (RAM va ROM) + kirish-chiqish portlari** — qo'shimcha qismlarsiz mustaqil ishlaydi.

### 2. Mikrokontroller va mikroprotsessor

Mikroprotsessor (Intel, AMD) — faqat «miya»: juda kuchli, lekin ishlashi uchun tashqaridan RAM, qattiq disk, boshqaruv sxemalari ulanishi kerak. Mikrokontroller kuchsizroq, lekin **yaxlit tizim**.

| Xususiyat | Mikrokontroller (MCU) | Mikroprotsessor (MPU) |
|---|---|---|
| Tuzilishi | yaxlit: protsessor, xotira, portlar bitta chipda | faqat «miya»: RAM, disk alohida ulanadi |
| Vazifasi | maxsus — aniq bir ish (haroratni o'lchash) | umumiy — o'yin, video montaj |
| Tezlik va quvvat | MHz, juda kam tok, batareyada yillab | GHz, ko'p energiya va kuler |
| Narxi | arzon (ba'zan 1 dollardan kam) | qimmat (yuzlab dollar) |
| Misollar | Arduino (ATmega328), ESP32, STM32 | Intel Core i7, AMD Ryzen, Apple M1 |

**O'xshatish:** MCU — «Shveysariya pichog'i» (kichik, hamma asbob o'zida, mayda aniq ishlar uchun). MPU — «Formula-1 dvigateli» (qudratli, lekin g'ildirak, korpus, yoqilg'i baki alohida kerak).

### 3. Kompyuterdan farqi

- Kompyuter — **universal**: Windows/Linux OS, bir vaqtda yuzlab dastur.
- Mikrokontrollerda odatda **OS yo'q** (yoki juda sodda), u **bitta aniq vazifaga** dasturlanadi va bitta dasturni **tinimsiz takrorlaydi** (Arduino'dagi `loop()`).
- Misol: mikroto'lqinli pechdagi MCU faqat vaqtni sanaydi va qizdiradi — internetga kirmaydi, musiqa qo'ymaydi.
- Qoida: video montaj, o'yin → kompyuter (MPU). Robot, avtomatik chiroq → mikrokontroller.

### 4. Asosiy qismlar — uchta ustun

| Qism | Vazifasi | O'xshatish |
|---|---|---|
| **CPU** | dastur buyruqlarini o'qiydi, tushunadi, bajaradi; arifmetik va mantiqiy amallar («harorat ko'tarilsa, nima qilish kerak?»); tezligi MHz — soniyasiga millionlab buyruq | «miya», «dirijyor» |
| **Flash (ROM)** | dastur kodi; tok o'chganda **saqlanadi** | darslik — yozuvlar o'zgarmaydi |
| **RAM** | o'zgaruvchilar, oraliq natijalar; tok o'chsa **o'chadi** | sinf doskasi — yozasiz, foydalanasiz, o'chirasiz |
| **I/O portlar (pinlar)** | tashqi dunyo bilan fizik aloqa | «qo'l-oyoq» va «ko'z-quloq» |

- **Input** rejimi: sensordan xabar oladi (tugma bosildimi, yorug'lik bormi, harorat qancha).
- **Output** rejimi: qarorga ko'ra buyruq beradi (chiroqni yoqish, motorni aylantirish).
- Uchalasi birga: **portlar xabar oladi → CPU Flash'dagi dastur asosida tahlil qiladi → portlar orqali javob**.

### 5. Arduino UNO misolida

- Markazda **ATmega328P** — **8-bitli AVR** arxitektura, plataning «miyasi».
- Ichida uch xotira: **flash** (dastur), **SRAM** (vaqtinchalik ma'lumot), **EEPROM** (tok o'chganda ham saqlanishi kerak bo'lgan sozlamalar).
- **14 ta raqamli pin** (HIGH/LOW) va **6 ta analog pin** (A0–A5, o'zgaruvchan qiymat).
- Quvvat pinlari: **5V, 3.3V, GND**; tashqi manba **7–12V**.
- **USB-B**: dastur yuklash va quvvat; USB–Serial konvertor chipi **ATmega16U2**.
- **Kvars generator** — vaqt chastotasi, odatda **16 MHz**.

### 6. «Tugma → LED»: qismlar qanday birga ishlaydi

```cpp
const int TUGMA = 2;           // Flash'da saqlanadigan dastur qismi
const int LED = 13;
int holat = 0;                 // o'zgaruvchi — RAM'da

void setup() {
  pinMode(TUGMA, INPUT);       // 2-pin: Input — «quloq»
  pinMode(LED, OUTPUT);        // 13-pin: Output — «qo'l»
}

void loop() {                  // bitta vazifani tinimsiz takrorlaydi
  holat = digitalRead(TUGMA);  // port xabar oladi
  if (holat == HIGH) {         // CPU mantiqiy amal bajaradi
    digitalWrite(LED, HIGH);   // port orqali javob
  } else {
    digitalWrite(LED, LOW);
  }
}
```

Tok o'chib yonsa: kod (Flash) saqlanadi va qayta ishga tushadi, `holat` qiymati (RAM) yo'qoladi va `0` dan boshlanadi. Plata bo'lmasa — Tinkercad yoki Wokwi'da yig'ish mumkin (tugma uchun 10 kΩ pull-down rezistor).

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Qayerda mikrokontroller bor? (oson)
Ro'yxatdan mikrokontroller bilan ishlaydigan qurilmalarni ajrating va har biri qanday **bitta vazifani** bajarishini yozing: kir yuvish mashinasi, noutbuk, televizor pulti, mikroto'lqinli pech, o'yin kompyuteri, aqlli termostat.

**Yechim:**
MCU: kir yuvish mashinasi (dastur bo'yicha suv, aylantirish, vaqt), pult (tugmani IR signalga aylantirish), mikroto'lqinli pech (vaqtni sanash, qizdirish), aqlli termostat (haroratni o'lchab isitishni boshqarish). Noutbuk va o'yin kompyuteri — MPU asosidagi universal kompyuterlar (ichida yordamchi MCU'lar ham bo'lishi mumkin — qo'shimcha izoh).

### 2-topshiriq. Qismni toping (oson)
Ta'rifga mos qismni yozing: (a) tok o'chganda ham kodni saqlaydi; (b) buyruqlarni bajaradi, «dirijyor»; (c) tok o'chsa tozalanadigan «doska»; (d) tugma holatini o'qiydi; (e) chiroqni yoqadi.

**Yechim:**
(a) Flash (ROM); (b) CPU; (c) RAM; (d) kirish porti (Input rejim); (e) chiqish porti (Output rejim).

### 3-topshiriq. MCU va MPU jadvali (o'rta)
5 mezonli jadval tuzing (tuzilishi, vazifasi, tezlik/quvvat, narx, misollar) va «Shveysariya pichog'i / Formula-1 dvigateli» o'xshatishini o'z so'zingiz bilan tushuntiring.

**Yechim:**
Jadval — konspektdagi 2-bo'limdagidek. O'xshatish: pichoq kichik va hamma asbob o'zida — MCU ham CPU, xotira, portni bitta chipda jamlagan, mayda aniq ishga mos. F-1 dvigateli juda kuchli, lekin g'ildirak va bakisiz yurmaydi — MPU ham RAM, disk, plata ulanmaguncha ishlamaydi.

### 4-topshiriq. Dasturni qismlarga ajrating (qiyin)
«Tugma → LED» dasturida: (1) qaysi qatorlar Input va qaysilari Output portni ishlatadi; (2) qaysi ma'lumot Flash'da, qaysi biri RAM'da; (3) CPU qayerda qaror qabul qiladi; (4) tok o'chib qayta yonsa, nima saqlanadi va nima yo'qoladi; (5) agar tugmalar bosilish sonini tok o'chganda ham saqlash kerak bo'lsa, qaysi xotira kerak?

**Yechim:**
1. Input: `pinMode(TUGMA, INPUT)`, `digitalRead(TUGMA)`; Output: `pinMode(LED, OUTPUT)`, `digitalWrite(LED, ...)`.
2. Dastur (barcha buyruqlar, `TUGMA`, `LED` konstantalari) — Flash; `holat` o'zgaruvchisi — RAM.
3. `if (holat == HIGH)` — mantiqiy amal.
4. Dastur saqlanadi va `setup()` dan qayta boshlanadi; `holat` yo'qoladi (0).
5. **EEPROM** — tok o'chganda ham saqlanishi kerak bo'lgan ma'lumot uchun (`EEPROM.h` kutubxonasi qo'llanmada keyingi mavzularda).

---

## Tezkor nazorat savollari

1. Mikrokontroller nima?
   - *Javob:* Bitta chip ichidagi ixcham kompyuter: CPU, xotira va kirish-chiqish portlari birga.
2. Mikroprotsessor nega mustaqil ishlay olmaydi?
   - *Javob:* U faqat «miya» — tashqi RAM, disk va boshqaruv sxemalari kerak.
3. Flash va RAM farqi?
   - *Javob:* Flash — dastur, tok o'chganda saqlanadi; RAM — vaqtinchalik, tok o'chsa o'chadi.
4. Pinning Input va Output rejimi?
   - *Javob:* Input — sensordan ma'lumot oladi; Output — qurilmaga buyruq beradi.
5. Arduino UNO'da qancha raqamli va analog pin bor, chip qaysi?
   - *Javob:* 14 raqamli, 6 analog; ATmega328P (8-bit AVR), 16 MHz.

---

## Keng tarqalgan xatolar va ularning oldini olish

- **«Mikrokontroller = kichik kompyuter, unda ham Windows bor»:** MCU'da odatda OS yo'q, bitta dastur `loop()` da takrorlanadi.
- **MCU va MPU ni adashtirish:** asosiy farq — xotira va portlar chip ichidami (MCU) yoki tashqaridami (MPU).
- **«RAM'dagi ma'lumot saqlanib qoladi»:** tok o'chganda RAM tozalanadi; saqlash kerak bo'lsa — EEPROM.
- **Pin rejimini belgilamaslik:** `pinMode()` siz pin kutilgandek ishlamaydi; tugma uchun INPUT, LED uchun OUTPUT.
- **Tugma «suzib yuradi»:** pull-down (yoki `INPUT_PULLUP`) bo'lmasa, `digitalRead` tasodifiy qiymat beradi.
- **Raspberry Pi Pico / ESP32 ni «mikrokompyuter» deb atash:** ular ham mikrokontrollerlar (13–14-darslar).
