# 4-hafta: Uyga vazifalar to'plami

Mazkur haftada o'tilgan darslar bo'yicha mustaqil bajarish uchun topshiriqlar. Har bir vazifa 20–30 daqiqaga mo'ljallangan. Natijani Tinkercad havolasi yoki skrinshotlar bilan topshiring.

---

## 10-dars: Arduino UNO va tugma orqali LED holatini boshqarish dasturi

1. Tinkercad'da Arduino UNO, tugma (Pin 2 → GND) va LED (Pin 9 → 220 Om → GND) sxemasini yig'ing.
2. `delay()` ishlatmasdan, `millis()` asosida 4 rejimli chiroq dasturini yozing: O'CHIQ → YONIQ → SEKIN (500 ms) → TEZ (100 ms) → O'CHIQ.
3. Rejim o'zgarganda Serial Monitor'ga `Rejim: SEKIN` kabi yozuv chiqsin (faqat o'zgarganda).
4. Qo'shimcha: Pin 13 ga heartbeat LED qo'shing (700 ms) va u rejimlardan qat'i nazar bir tekis miltillashini ko'rsating.

---

## 11-dars: DIP switch (DPST) va LED — oddiy elektron sikl (1-qism)

1. Tinkercad'da 5 V manba, Breadboard, DIP Switch DPST, qizil va yashil LED dan zanjir yig'ing: 1-kontakt Qizil LEDni, 2-kontakt Yashil LEDni mustaqil boshqarsin.
2. Har bir LED uchun rezistorni Om qonuni bo'yicha hisoblang (qizil 2 V, yashil 3 V, tok 10 mA) va standart qiymatni tanlang.
3. 4 ta holat (OFF/OFF, ON/OFF, OFF/ON, ON/ON) jadvalini tuzing va har biriga skrinshot qo'shing.
4. Agar manba 9 V bo'lsa, rezistorlar qanday o'zgarishi kerakligini hisob bilan yozing.

---

## 12-dars: DIP switch (DPST) va LED — oddiy elektron sikl (2-qism)

1. AND (ketma-ket) va OR (parallel) zanjirlarini yig'ing; har biri uchun haqiqat jadvalini skrinshotlar bilan tasdiqlang.
2. Multimetr bilan 220, 330 va 1000 Om rezistorlarda tokni o'lchab, jadval va xulosa yozing.
3. DIP switch'ni Arduino'ga ulang (DIP1 → Pin 2, DIP2 → Pin 3, qarama-qarshi oyoqlar GND) va 2 bitli kod bo'yicha 4 rejimli tanlagichni dasturlang: 0 — o'chiq, 1 — Yashil, 2 — Qizil, 3 — navbat bilan miltillash.

---

## Mentor uchun

### Baholash mezonlari (Jami 100 ball)
- **10-dars vazifasi (35 ball):** `millis()` andozasi to'g'ri (`unsigned long`, `oxirgi = millis()`), `% 4` bilan rejim aylanishi, `switch/case`, debounce (50 ms so'rov), Serial'ga faqat o'zgarishda yozish.
- **11-dars vazifasi (30 ball):** komponentlar turli qatorlarda, DIP ariqcha ustida, LED qutbi to'g'ri, rezistor hisoblari (qizil — 330 Om, yashil — 220 Om; 9 V uchun 470–680 Om) asoslangan, 4 holat jadvali.
- **12-dars vazifasi (35 ball):** AND va OR sxemalari va jadvallari, multimetr to'g'ri ulangan (tok — ketma-ket), rezistor xulosasi, `INPUT_PULLUP` va `== LOW ? 1 : 0` bilan kod hisoblash, 4 rejim ishlashi.

Dasturdagi shkala: **90–100 — 5**, **71–89 — 4**, **60–70 — 3**, **0–59 — 2**.

### Eslatma
- 12-dars Arduino topshirig'ida DIP switch tugmadan farqli ravishda holatini saqlashini, shuning uchun Toggle kerak emasligini o'quvchi tushuntira olishini tekshiring.
