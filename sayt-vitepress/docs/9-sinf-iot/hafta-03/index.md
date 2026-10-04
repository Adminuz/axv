---
title: "3-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "9-sinf (IoT)", "link": "/9-sinf-iot/"}, "n": 3, "bob": "III-bob · Mikrokontrollerlar va IoT qurilmalari (Arduino, ESP8266, ESP32)", "lessons": [{"g": 13, "title": "7-dars: Elektron sxema asosida ikki LED lampaning ishlash prinsipi va ulanishi", "lead": "IoT uchun asosiy qurilmalar: Arduino va Raspberry Pi taqqosi", "link": "/9-sinf-iot/hafta-03/dars-7", "slide": "/slaydlar/9-sinf-iot/hafta-03/dars-7.html"}, {"g": 14, "title": "8-dars: Arduino UNO yordamida LED indikatorlari va push-button bilan ishlash (1-qism)", "lead": "IoT uchun asosiy qurilmalar: ESP8266 va ESP32 imkoniyatlari", "link": "/9-sinf-iot/hafta-03/dars-8", "slide": "/slaydlar/9-sinf-iot/hafta-03/dars-8.html"}, {"g": 15, "title": "9-dars: Arduino UNO yordamida LED indikatorlari va push-button bilan interaktiv interfeys (2-qism)", "lead": "Mikrokontroller tushunchasi va IoT qurilmalaridagi o‘rni (1-qism)", "link": "/9-sinf-iot/hafta-03/dars-9", "slide": "/slaydlar/9-sinf-iot/hafta-03/dars-9.html"}]}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Mazkur haftada o'tilgan darslar bo'yicha mustaqil bajarish uchun topshiriqlar. Har bir vazifa 20–30 daqiqaga mo'ljallangan.

---

### 7-dars: Elektron sxema asosida ikki LED lampaning ishlash prinsipi va ulanishi

1. Tinkercad-da Arduino Uno, Breadboard, 2 ta 220 Om rezistor hamda Qizil va Yashil LED dan iborat mustaqil parallel sxemani yig'ing (Qizil — Pin 9, Yashil — Pin 11).
2. C++ tilida yo'l harakati xavfsizligi mayoqchasini (Traffic Flasher) dasturlang:
   - Qizil LED 3 marta tez miltillaydi (har biri 150 ms yoniq, 150 ms o'chiq);
   - Yashil LED 3 marta tez miltillaydi (har biri 150 ms yoniq, 150 ms o'chiq);
   - Ikkala LED 1 soniyaga o'chib tanaffus qiladi va tsikl takrorlanadi.
3. Nima uchun 3 ta LED ni 5V manbaga ketma-ket ulaganda ular yonmasligini kuchlanishlar yig'indisi formulasi ($U = U_1 + U_2 + U_3$) orqali asoslab bering.

---

### 8-dars: Arduino UNO yordamida LED indikatorlari va push-button bilan ishlash (1-qism)

1. Arduino `D2` piniga va `GND` ga Push-button ulang. `pinMode(2, INPUT_PULLUP)` sozlamasidan foydalaning.
2. Tugma holatini o'qib, Serial Monitorga chiqaruvchi dastur yozing.
3. Sxemaga Pin 9 dagi LEDni qo'shing va quyidagi xavfsizlik signalizatsiyasi mantiqini tuzing:
   - Tugma bo'sh turganda (eshik yopiq deb hisoblanadi): LED o'chiq bo'lsin;
   - Tugma bosilganda (eshik buzib ochildi): LED tez miltillab xavf signali bersin va Serial Monitorga "DIQQAT: Eshik ochildi!" matni uzatilsin.

---

### 9-dars: Arduino UNO yordamida LED indikatorlari va push-button bilan interaktiv interfeys (2-qism)

1. 1 ta Push-button va 1 ta LED yordamida to'liq Toggle (trigged) kalitini dasturlang: tugma 1 marta bosilganda LED yonsin va yoniq qolsin, yana 1 marta bosilganda esa o'chsin.
2. Dasturda nima sababdan `delay(50)` qo'yilganini mexanik kontaktlarning dirillashi (Button Bounce) hodisasi misolida tushuntiring.
3. Sxemaga ikkinchi tugma va ikkinchi LED qo'shing. Biri Qizil chiroqni, ikkinchisi Yashil chiroqni mustaqil boshqarsin. Ikkala chiroq bir-biriga xalaqit bermasdan ishlashini simulyatsiyada ko'rsating.

---

</div>
