# 13-dars. Arduino va Raspberry Pi taqqosi

> Biri — bitta ishni yillar davomida to'xtovsiz bajaradigan «tirishqoq ishchi», ikkinchisi — kaftga sig'adigan haqiqiy kompyuter. Bugun Arduino va Raspberry Pi'ni yonma-yon qo'yib, qaysi loyihaga qaysi biri kerakligini o'rganamiz.

## Dars xulosasi

- IoT zanjiri: **sensor** sezadi → **mikrokontroller / mikrokompyuter** qaror qiladi → **tarmoq** uzatadi → **aktuator** harakat qiladi.
- **Arduino** — ochiq kodli mikrokontroller platformasi: plata + Arduino IDE. UNO markazida **ATmega328P**.
- Arduino dasturi: `setup()` bir marta, `loop()` cheksiz takror. Pinlar: raqamli, analog, PWM.
- Arduino afzalliklari: oson, arzon, kutubxonalar ko'p. Cheklovi: **Wi-Fi/Bluetooth yo'q**, kuchi kam.
- **Raspberry Pi** — Linux (Raspberry Pi OS) da ishlaydigan mikrokompyuter: ARM protsessor, GPU, RAM, microSD, GPIO, HDMI, USB, Wi-Fi.
- Raspberry Pi afzalliklari: kamera, ekran, AI, server. Cheklovi: qimmatroq, ko'p energiya, murakkabroq.
- Tanlash mezonlari: murakkablik, internet, energiya, pinlar, dasturlash, byudjet.

## Qo'shimcha ma'lumot

### 1. Svetofor va ofis kompyuteri
Chorrahadagi svetofor boshqaruvchisini tasavvur qiling: u faqat bitta ishni biladi — ranglarni almashtirish. Lekin buni kunu tun, yillab, xatosiz qiladi. **Arduino** aynan shunday. Ofisdagi kompyuter esa hujjat, internet, video, dasturlar — hammasini bajaradi, lekin uni yoqish, sozlash va elektr bilan ta'minlash kerak. **Raspberry Pi** — shunday kompyuterning kaftdek kichik versiyasi.

### 2. Bir vazifa — ikki kod
LEDni har soniyada yoqib-o'chirish:

```cpp
// Arduino (C/C++): kod to'g'ridan-to'g'ri chipda
void setup() { pinMode(13, OUTPUT); }
void loop() {
  digitalWrite(13, HIGH); delay(1000);
  digitalWrite(13, LOW);  delay(1000);
}
```

```python
# Raspberry Pi (Python, gpiozero): dastur Linux ichida ishlaydi
from gpiozero import LED
from time import sleep
led = LED(17)
while True:
    led.on();  sleep(1)
    led.off(); sleep(1)
```

Natija bir xil, lekin Raspberry Pi bir vaqtda bu dastur bilan birga brauzer, server yoki kamera dasturini ham ishlata oladi (multitasking).

### 3. Raspberry Pi modellari
- **Zero / Zero W** — juda kichik va arzon, 512 MB RAM.
- **3 Model B+** — 4 yadro, 1 GB RAM: aqlli uy, kamera.
- **4** — 4 yadro, 2–8 GB RAM, 4K video: gateway, web-server.
- **5** — eng kuchli: AI va yirik loyihalar.
- **Pico / Pico W** — diqqat! Bu **mikrokontroller** (RP2040), operatsion tizimi yo'q.

### 4. Qanday tanlash kerak?
O'zingizga 4 savol bering:
1. Loyiha oddiymi (1–3 sensor, 1 aktuator)? → Arduino.
2. Internet kerakmi? → ichida Wi-Fi bor qurilma (ESP yoki Raspberry Pi).
3. Batareyada ishlaydimi? → kam quvvatli mikrokontroller.
4. Kamera, video, AI, server kerakmi? → Raspberry Pi.

### 5. Odatiy xatolar
- Raspberry Pi'ni elektrdan to'satdan uzish — microSD dagi tizim buzilishi mumkin.
- Raspberry Pi GPIO pinlari 3.3 V da ishlaydi, Arduino UNO — 5 V: ularni to'g'ridan-to'g'ri ulash xavfli.
- «Eng kuchli — eng yaxshi» degan fikr: oddiy LED indikator uchun Raspberry Pi ortiqcha.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Mikrokontroller | Bitta chipda protsessor, xotira va portlar; bitta vazifani bajaradi |
| Mikrokompyuter | Operatsion tizimda ishlaydigan kichik to'liq kompyuter |
| Arduino | Ochiq kodli mikrokontroller platformasi: plata + IDE |
| ATmega328P | Arduino UNO markazidagi mikrokontroller |
| Arduino IDE | Arduino uchun kod yozish va yuklash dasturi |
| Raspberry Pi | Linux'da ishlaydigan arzon mikrokompyuter |
| Raspberry Pi OS | Raspberry Pi uchun Linux asosidagi operatsion tizim |
| GPIO | Umumiy kirish-chiqish pinlari: sensor va aktuator ulanadi |
| PWM | Impuls kengligi modulyatsiyasi: LED yorqinligi, motor tezligi |
| microSD | Raspberry Pi'da OS va ma'lumot saqlanadigan karta |
| Multitasking | Bir vaqtda bir nechta dasturni bajarish |

## Bilasizmi?

- Arduino 2005-yilda Italiyaning Ivrea shahrida talabalar uchun arzon o'quv vositasi sifatida yaratilgan; nomi esa u yerdagi bir kafe nomidan olingan.
- Raspberry Pi'ning birinchi modeli 2012-yilda chiqqan va bolalarga dasturlashni o'rgatish maqsadida yaratilgan.
- Raspberry Pi kompyuterlari Xalqaro kosmik stansiyaga ham olib chiqilgan — o'quvchilar ular uchun yozgan dasturlar orbitada ishlagan (Astro Pi loyihasi).
- Arduino platalarining sxemalari ochiq — shuning uchun dunyoda juda ko'p mos «klon» platalar ishlab chiqariladi.

## Topshiriqlar

### 1. IoT zanjiri · oson
Aqlli chiroq loyihasi: yorug'lik sensori, Arduino, rele, chiroq. Har birining zanjirdagi rolini yozing.

**Kutiladigan natija:** 4 qatorli jadval «qurilma — rol».

### 2. Kim bu? · oson
Ta'riflarga qurilma nomini yozing: (a) «HDMI va kamera porti bor, Linux'da ishlaydi»; (b) «ATmega328P, setup va loop»; (c) «RP2040, OS yo'q».

**Kutiladigan natija:** 3 ta javob.

### 3. Pinlar · oson
Arduino'dagi raqamli, analog va PWM pinlarga bittadan qurilma misoli keltiring.

**Kutiladigan natija:** 3 ta misol.

### 4. Afzallik va cheklov · oson
Arduino va Raspberry Pi uchun 2 tadan afzallik va 1 tadan cheklov yozing.

**Kutiladigan natija:** 2 ustunli ro'yxat.

### 5. Kodni tushuntiring · o'rta
Darsdagi Arduino va Python kodlarini qatorma-qator izohlang: qaysi qator nimani qiladi?

**Kutiladigan natija:** har bir qator uchun 1 jumla.

### 6. Bashorat qiling · o'rta
Arduino kodida `delay(1000)` ikkalasini `delay(250)` ga almashtirsak nima o'zgaradi? Agar faqat birinchisini almashtirsak-chi?

**Kutiladigan natija:** 2 ta javob va izoh.

### 7. Taqqoslash jadvali · o'rta
Arduino UNO va Raspberry Pi 4 ni 6 mezon bo'yicha taqqoslang: OS, tarmoq, til, energiya, narx, kuchli tomon.

**Kutiladigan natija:** 6 qatorli jadval.

### 8. Model tanlang · o'rta
Quyidagilarga Raspberry Pi modelini tanlang: (a) eng kichik va arzon mini qurilma; (b) 4K video va web-server; (c) OS kerak emas, real vaqt boshqaruvi.

**Kutiladigan natija:** 3 ta model nomi va sabab.

### 9. Loyihaga qurilma · qiyin
(1) sinf harorati LED indikatori; (2) maktab kirishidagi yuz tanuvchi kamera; (3) daladagi batareyali namlik sensori. Qurilma tanlang va har biriga 2 mezon bilan asoslang.

**Kutiladigan natija:** 3 ta asoslangan tanlov.

### 10. Xatoni toping · qiyin
Do'stingiz aytdi: «Raspberry Pi Pico'ga Linux o'rnataman va unda kamera bilan yuz taniyman». Nima noto'g'ri? Qanday maslahat berasiz?

**Kutiladigan natija:** 2–3 jumla tushuntirish.

### 11. Tadqiqot · qiyin
Arduino Mega va Arduino Nano haqida ma'lumot toping: UNO'dan nimasi bilan farq qiladi (pinlar soni, o'lcham)? Qaysi loyihaga mos?

**Kutiladigan natija:** kichik taqqoslash jadvali.

### 12. Aqlli uy rejasi · bonus
Uyingiz uchun IoT tizim rejasini chizing: Raspberry Pi markaz (gateway) bo'lsin, xonalarda esa kichik mikrokontrollerlar. Kim nima qiladi?

**Kutiladigan natija:** sxema va qisqa izoh.

## O'zingizni tekshiring

1. Mikrokontroller va mikrokompyuter qanday farqlanadi?
2. Arduino platformasi qaysi ikki qismdan iborat?
3. `setup()` va `loop()` nima uchun kerak?
4. Raspberry Pi tuzilishining asosiy qismlarini sanang.
5. Nega Raspberry Pi'da multitasking bor, Arduino'da esa yo'q?
6. Raspberry Pi Pico boshqa Pi modellaridan nimasi bilan farq qiladi?
7. Qurilma tanlashda qaysi mezonlarga qaraladi?

## Uyga vazifa

Arduino UNO va Raspberry Pi 4 taqqoslash jadvalini (6 mezon) to'ldiring va o'zingiz o'ylab topgan 3 ta IoT loyihaga mos qurilmani asoslab tanlang (20–30 daqiqa). Batafsil — haftalik uyga vazifada.
