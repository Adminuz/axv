# 15-dars. Mikrokontroller tushunchasi (1-qism)

> Kir yuvish mashinasi, mikroto'lqinli pech, televizor pulti, avtomobil tormozi — ularning hammasi ichida kichik «kompyuter» yashirinib ishlaydi. Bu — mikrokontroller. Bugun uning ichida nima borligini va qanday ishlashini bilib olamiz.

## Dars xulosasi

- **Mikrokontroller (MCU)** — bitta chip ichidagi ixcham kompyuter: **protsessor (CPU) + xotira + kirish-chiqish portlari**.
- **Mikroprotsessor (MPU)** — faqat «miya» (Intel, AMD, Apple M1): kuchli, lekin tashqi RAM va disk kerak.
- MCU — **maxsus** vazifa, MHz, juda kam energiya, arzon; MPU — **umumiy** vazifa, GHz, ko'p energiya, qimmat.
- Mikrokontrollerda odatda **operatsion tizim yo'q** — u bitta dasturni tinimsiz takrorlaydi.
- **Flash** — dastur (tok o'chganda saqlanadi); **RAM** — vaqtinchalik (tok o'chsa o'chadi); **EEPROM** — saqlanishi kerak bo'lgan sozlamalar.
- Pinlar **Input** (sensordan oladi) va **Output** (buyruq beradi) rejimida ishlaydi.
- Arduino UNO: **ATmega328P** (8-bit), 14 raqamli + 6 analog pin, 16 MHz.

## Qo'shimcha ma'lumot

### 1. Shveysariya pichog'i va Formula-1 dvigateli
Mikrokontroller — **Shveysariya pichog'i**: kichkina, hamma kerakli asbob o'zida, mayda aniq ishlar uchun juda qulay. Mikroprotsessor — **Formula-1 dvigateli**: juda qudratli, lekin yurishi uchun g'ildirak, korpus va yoqilg'i baki alohida ulanishi kerak.

| Xususiyat | Mikrokontroller | Mikroprotsessor |
|---|---|---|
| Tuzilishi | hammasi bitta chipda | faqat «miya» |
| Vazifasi | aniq bir ish | turli murakkab ishlar |
| Tezlik va quvvat | MHz, juda kam tok | GHz, ko'p energiya, kuler |
| Narxi | 1 dollardan ham arzon bo'lishi mumkin | yuzlab dollar |
| Misollar | ATmega328, ESP32, STM32 | Intel Core i7, AMD Ryzen, Apple M1 |

### 2. Uchta ustun: miya, xotira, sezgi a'zolari
- **CPU** — «miya» va «dirijyor»: buyruqlarni o'qiydi va bajaradi, hisoblaydi, «agar … bo'lsa» kabi qaror qabul qiladi.
- **Flash** — **darslik**: yozuvlar o'zgarmaydi, tok o'chsa ham saqlanadi. Har safar yonganda MCU dasturni shu yerdan o'qiydi.
- **RAM** — **sinf doskasi**: kerakli narsani yozasiz, foydalanasiz, dars tugagach o'chirasiz.
- **I/O portlar** — «qo'l-oyoq» va «ko'z-quloq»: tashqi olam bilan aloqa.

### 3. Tugma va LED: hammasi birga

```cpp
const int TUGMA = 2;
const int LED = 13;
int holat = 0;                 // RAM'da

void setup() {
  pinMode(TUGMA, INPUT);       // «quloq»
  pinMode(LED, OUTPUT);        // «qo'l»
}

void loop() {
  holat = digitalRead(TUGMA);  // port xabar oladi
  if (holat == HIGH) {         // CPU qaror qiladi
    digitalWrite(LED, HIGH);   // port javob beradi
  } else {
    digitalWrite(LED, LOW);
  }
}
```

Zanjir: **port xabar oladi → CPU Flash'dagi dastur bo'yicha tahlil qiladi → port orqali javob**.

### 4. Arduino UNO platasida nima bor?
- **ATmega328P** — 8-bitli AVR mikrokontroller, ichida flash, SRAM va EEPROM.
- **14 ta raqamli pin** (HIGH/LOW) va **6 ta analog pin** (A0–A5).
- Quvvat pinlari: **5V, 3.3V, GND**; tashqi manba 7–12V.
- **USB-B** porti — dastur yuklash va quvvat; yonida USB–Serial chip **ATmega16U2**.
- **Kvars generator** — 16 MHz «yurak urishi».

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Mikrokontroller (MCU) | CPU, xotira va portlar bitta chipda jamlangan ixcham kompyuter |
| Mikroprotsessor (MPU) | Faqat hisoblovchi «miya», tashqi qismlar kerak |
| CPU | Buyruqlarni bajaruvchi markaziy protsessor |
| Flash (ROM) | Dastur saqlanadigan, tok o'chganda yo'qolmaydigan xotira |
| RAM (SRAM) | Vaqtinchalik xotira, tok o'chsa tozalanadi |
| EEPROM | Sozlamalarni tok o'chganda ham saqlovchi kichik xotira |
| I/O port (pin) | Kirish-chiqish nuqtasi — tashqi qurilma ulanadi |
| Input | Pin sensordan ma'lumot oladi |
| Output | Pin qurilmaga signal beradi |
| AVR | ATmega chiplari arxitekturasi |
| MHz | Chastota: soniyasiga million tebranish |

## Bilasizmi?

- Zamonaviy avtomobil ichida o'nlab, ba'zan yuzdan ortiq mikrokontroller ishlaydi: dvigatel, tormoz, oyna ko'targich, konditsioner — har biriga alohida.
- Arduino UNO dagi ATmega328P ning dastur xotirasi atigi 32 KB — bu oddiy fotosuratdan ham ancha kichik, lekin robotni boshqarishga yetadi.
- «Arduino» nomi Italiyaning Ivrea shahridagi bar nomidan olingan — platforma yaratuvchilari o'sha yerda uchrashishgan.

## Topshiriqlar

### 1. Ichida MCU bormi? · oson
Kir yuvish mashinasi, noutbuk, televizor pulti, mikroto'lqinli pech, o'yin kompyuteri, aqlli termostat — qaysilari mikrokontroller bilan ishlaydi?

**Kutiladigan natija:** 2 guruhli ro'yxat.

### 2. Ta'rifni toping · oson
(a) tok o'chganda ham kodni saqlaydi; (b) buyruqlarni bajaradi; (c) tok o'chsa tozalanadi; (d) tugma holatini o'qiydi; (e) chiroqni yoqadi.

**Kutiladigan natija:** 5 ta qism nomi.

### 3. Bitta vazifa · oson
Uydagi 3 ta qurilmani tanlang va undagi mikrokontroller qaysi **bitta vazifani** takrorlashini yozing.

**Kutiladigan natija:** 3 ta qurilma va vazifasi.

### 4. Plata xaritasi · oson
Arduino UNO rasmini chizing (yoki chop eting) va ATmega328P, raqamli pinlar, analog pinlar, 5V/GND, USB-B ni belgilang.

**Kutiladigan natija:** 5 ta belgili rasm.

### 5. MCU va MPU jadvali · o'rta
5 mezon bo'yicha jadval tuzing: tuzilishi, vazifasi, tezlik/quvvat, narx, misollar.

**Kutiladigan natija:** 5 qatorli jadval.

### 6. O'xshatish · o'rta
«Shveysariya pichog'i» va «Formula-1 dvigateli» o'xshatishini o'z so'zlaringiz bilan tushuntiring va o'zingizning o'xshatishingizni o'ylab toping.

**Kutiladigan natija:** 3–4 jumla.

### 7. Darslik va doska · o'rta
Flash va RAM ni o'xshatish bilan tushuntiring. Tok o'chib-yonsa, «tugma → LED» dasturida nima saqlanadi, nima yo'qoladi?

**Kutiladigan natija:** 2 ta xulosa.

### 8. Input yoki Output? · o'rta
Harorat sensori, LED, servo motor, tugma, buzzer, yorug'lik sensori — har biri qaysi rejimdagi pinga ulanadi?

**Kutiladigan natija:** 6 ta javob.

### 9. Dasturni qismlarga ajrating · qiyin
«Tugma → LED» kodida Input, Output, RAM'dagi ma'lumot va CPU qaror qabul qiladigan qatorni belgilang.

**Kutiladigan natija:** 4 ta belgilangan qator.

### 10. Simulyatorda yig'ish · qiyin
Tinkercad yoki Wokwi'da Arduino UNO, tugma (10 kΩ rezistor bilan) va LED ni yig'ib, kodni ishga tushiring.

**Kutiladigan natija:** ishlaydigan sxema skrinshoti.

### 11. Qaysi xotira? · qiyin
Aqlli lampa foydalanuvchi tanlagan yorqinlikni tok o'chib-yonganda ham eslab qolishi kerak. Qiymat qaysi xotirada saqlanishi kerak va nega RAM yaramaydi?

**Kutiladigan natija:** asoslangan javob.

### 12. Uydagi MCU ovchisi · bonus
Uyingizda ichida mikrokontroller ishlaydigan kamida 10 ta qurilmani toping va ularni «sensor bor / tarmoq bor» bo'yicha guruhlang.

**Kutiladigan natija:** 10 qatorli jadval.

## O'zingizni tekshiring

1. Mikrokontroller nima va u qayerlarda yashirinib ishlaydi?
2. Mikroprotsessor nega mustaqil ishlay olmaydi?
3. MCU ning MPU dan 3 ta afzalligi?
4. Kompyuter va mikrokontrollerning asosiy farqi nima?
5. Flash, RAM va EEPROM qaysi ma'lumotni saqlaydi?
6. Input va Output rejimlariga 2 tadan misol keltiring.
7. Arduino UNO'dagi chip, pinlar soni va chastota qanday?

## Uyga vazifa

MCU va MPU taqqoslash jadvalini tuzing, Arduino UNO plata xaritasini belgilang va «tugma → LED» dasturini qismlarga ajrating (20–30 daqiqa). Batafsil — haftalik uyga vazifada.
