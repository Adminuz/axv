---
title: "2-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "9-sinf (IoT)", "link": "/9-sinf-iot/"}, "n": 2, "bob": "II-bob · Elektronika va Arduino bilan interaktiv interfeyslar", "lessons": [{"g": 7, "title": "4-dars: Tinkercad.com virtual laboratoriyasida ro‘yxatdan o‘tish va interfeys", "lead": "Elektron sxema asosida ikki LED lampaning ishlash prinsipi va ulanishi", "link": "/9-sinf-iot/hafta-02/dars-4", "slide": "/slaydlar/9-sinf-iot/hafta-02/dars-4.html"}, {"g": 8, "title": "5-dars: Tinkercad muhitida virtual elektron komponentlar bilan ishlash", "lead": "Arduino UNO yordamida LED indikatorlari va push-button bilan ishlash (1-qism)", "link": "/9-sinf-iot/hafta-02/dars-5", "slide": "/slaydlar/9-sinf-iot/hafta-02/dars-5.html"}, {"g": 9, "title": "6-dars: Elektron sxema asosida bitta LED lampaning ishlash prinsipi va ulanishi", "lead": "Arduino UNO yordamida LED indikatorlari va push-button bilan interaktiv interfeys (2-qism)", "link": "/9-sinf-iot/hafta-02/dars-6", "slide": "/slaydlar/9-sinf-iot/hafta-02/dars-6.html"}]}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Mazkur haftada o'tilgan darslar bo'yicha mustaqil bajarish uchun topshiriqlar. Har bir vazifa 20–30 daqiqaga mo'ljallangan.

---

### 4-dars: Tinkercad.com virtual laboratoriyasida ro‘yxatdan o‘tish va interfeys

1. Tinkercad.com saytidagi shaxsiy profilingizga kiring va "Circuits" bo'limida yangi loyiha yarating. Unga `9-sinf_UygaVazifa_4` nomini bering.
2. Ish maydoniga kamida 4 ta turli komponentni joylashtiring (masalan: Arduino Uno, kichik Breadboard, LED, 9V batareya).
3. "Rotate" (R) asbobi yordamida breadboardni 90 gradusga buring, "Notes" (N) asbobi yordamida har bir komponent yoniga uning vazifasini bildiruvchi matnli yorliq biriktiring.
4. "Send To" / "Share" orqali sxemangizning ommaviy havolasini (Public Share link) oling va havola to'g'ri ochilayotganini tekshiring.

---

### 5-dars: Tinkercad muhitida virtual elektron komponentlar bilan ishlash

1. Breadboard ustida 9V batareya, suriluvchi kalit (Slide switch), 330 Om rezistor va sariq LED dan iborat mustaqil yopiq elektr zanjirini yig'ing.
2. Zanjirga virtual multimetrni "Voltage" rejimida ulab, sariq LED uchlaridagi kuchlanish tushuvini (Volt) o'lchang.
3. Ikkinchi multimetrni "Amperage" rejimida zanjirga ketma-ket ulab, zanjirdan o'tayotgan tok kuchini (milliAmper — mA) aniqlang.
4. Rezistor qiymatini 1 kOm ga oshiring va tok kuchi hamda yorug'lik intensivligi qanday o'zgarganini 2 ta jumla bilan tahlil qiling.

---

### 6-dars: Elektron sxema asosida bitta LED lampaning ishlash prinsipi va ulanishi

1. Arduino Uno platasining `D9` raqamli piniga 220 Om rezistor orqali bitta qizil LED ni ulang va katodini Arduino `GND` ga bog'lang.
2. Tinkercad "Code" panelida C++ tilida quyidagi mantiqqa ega dastur yozing:
   - LED 1 soniya yonsin;
   - 500 millisekund o'chsin;
   - LED 2 soniya yonsin;
   - 1 soniya o'chsin;
   - Tsikl cheksiz takrorlansin.
3. Nima uchun 5V quvvatda ishlaydigan Arduino uchun 220 Om rezistor tanlanganini Om qonuni formulasi ($R = (5\text{V} - 2\text{V}) / 0.015\text{A}$) asosida yozma asoslab bering.

---

</div>
