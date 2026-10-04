# 3-hafta: Uyga vazifalar to'plami

Mazkur haftada o'tilgan darslar bo'yicha mustaqil bajarish uchun topshiriqlar. Har bir vazifa 20–30 daqiqaga mo'ljallangan.

---

## 7-dars: Elektron sxema asosida ikki LED lampaning ishlash prinsipi va ulanishi

1. Tinkercad-da Arduino Uno, Breadboard, 2 ta 220 Om rezistor hamda Qizil va Yashil LED dan iborat mustaqil parallel sxemani yig'ing (Qizil — Pin 9, Yashil — Pin 11).
2. C++ tilida yo'l harakati xavfsizligi mayoqchasini (Traffic Flasher) dasturlang:
   - Qizil LED 3 marta tez miltillaydi (har biri 150 ms yoniq, 150 ms o'chiq);
   - Yashil LED 3 marta tez miltillaydi (har biri 150 ms yoniq, 150 ms o'chiq);
   - Ikkala LED 1 soniyaga o'chib tanaffus qiladi va tsikl takrorlanadi.
3. Nima uchun 3 ta LED ni 5V manbaga ketma-ket ulaganda ular yonmasligini kuchlanishlar yig'indisi formulasi ($U = U_1 + U_2 + U_3$) orqali asoslab bering.

---

## 8-dars: Arduino UNO yordamida LED indikatorlari va push-button bilan ishlash (1-qism)

1. Arduino `D2` piniga va `GND` ga Push-button ulang. `pinMode(2, INPUT_PULLUP)` sozlamasidan foydalaning.
2. Tugma holatini o'qib, Serial Monitorga chiqaruvchi dastur yozing.
3. Sxemaga Pin 9 dagi LEDni qo'shing va quyidagi xavfsizlik signalizatsiyasi mantiqini tuzing:
   - Tugma bo'sh turganda (eshik yopiq deb hisoblanadi): LED o'chiq bo'lsin;
   - Tugma bosilganda (eshik buzib ochildi): LED tez miltillab xavf signali bersin va Serial Monitorga "DIQQAT: Eshik ochildi!" matni uzatilsin.

---

## 9-dars: Arduino UNO yordamida LED indikatorlari va push-button bilan interaktiv interfeys (2-qism)

1. 1 ta Push-button va 1 ta LED yordamida to'liq Toggle (trigged) kalitini dasturlang: tugma 1 marta bosilganda LED yonsin va yoniq qolsin, yana 1 marta bosilganda esa o'chsin.
2. Dasturda nima sababdan `delay(50)` qo'yilganini mexanik kontaktlarning dirillashi (Button Bounce) hodisasi misolida tushuntiring.
3. Sxemaga ikkinchi tugma va ikkinchi LED qo'shing. Biri Qizil chiroqni, ikkinchisi Yashil chiroqni mustaqil boshqarsin. Ikkala chiroq bir-biriga xalaqit bermasdan ishlashini simulyatsiyada ko'rsating.

---

## Mentor uchun

### Baholash mezonlari (Jami 100 ball)
- **7-dars vazifasi (30 ball):** 2 ta LED uchun mustaqil pinlar va alohida rezistorlar to'g'ri ulangani, ketma-ket va parallel farqi to'g'ri hisoblangani hamda mayoqcha kodi to'g'ri tuzilgani.
- **8-dars vazifasi (35 ball):** Push-button `INPUT_PULLUP` orqali to'g'ri ulangani, suzuvchi pin muammosi anglangani, Serial Monitor vositasida xabar chiqarish va `if-else` sharti to'g'ri ishlagani.
- **9-dars vazifasi (35 ball):** Toggle mantig'i (`!ledState`), `lastButtonState` yordamida bosilish lahzasi aniqlangani, 50 ms Debounce filtri qo'llangani va ko'p tugmali tizim bekamu ko'st ishlagani.

### Eslatma
- O'quvchilar Toggle dasturida tugma bosib turilganda tsikl tinimsiz aylanib ketmasligi uchun aynan holat o'zgarishi (`reading != lastBtn`) shartidan foydalanganini tekshiring.
