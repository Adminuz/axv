# 2-hafta: Uyga vazifalar to'plami

Mazkur haftada o'tilgan darslar bo'yicha mustaqil bajarish uchun topshiriqlar. Har bir vazifa 20–30 daqiqaga mo'ljallangan.

---

## 4-dars: Tinkercad.com virtual laboratoriyasida ro‘yxatdan o‘tish va interfeys

1. Tinkercad.com saytidagi shaxsiy profilingizga kiring va "Circuits" bo'limida yangi loyiha yarating. Unga `9-sinf_UygaVazifa_4` nomini bering.
2. Ish maydoniga kamida 4 ta turli komponentni joylashtiring (masalan: Arduino Uno, kichik Breadboard, LED, 9V batareya).
3. "Rotate" (R) asbobi yordamida breadboardni 90 gradusga buring, "Notes" (N) asbobi yordamida har bir komponent yoniga uning vazifasini bildiruvchi matnli yorliq biriktiring.
4. "Send To" / "Share" orqali sxemangizning ommaviy havolasini (Public Share link) oling va havola to'g'ri ochilayotganini tekshiring.

---

## 5-dars: Tinkercad muhitida virtual elektron komponentlar bilan ishlash

1. Breadboard ustida 9V batareya, suriluvchi kalit (Slide switch), 330 Om rezistor va sariq LED dan iborat mustaqil yopiq elektr zanjirini yig'ing.
2. Zanjirga virtual multimetrni "Voltage" rejimida ulab, sariq LED uchlaridagi kuchlanish tushuvini (Volt) o'lchang.
3. Ikkinchi multimetrni "Amperage" rejimida zanjirga ketma-ket ulab, zanjirdan o'tayotgan tok kuchini (milliAmper — mA) aniqlang.
4. Rezistor qiymatini 1 kOm ga oshiring va tok kuchi hamda yorug'lik intensivligi qanday o'zgarganini 2 ta jumla bilan tahlil qiling.

---

## 6-dars: Elektron sxema asosida bitta LED lampaning ishlash prinsipi va ulanishi

1. Arduino Uno platasining `D9` raqamli piniga 220 Om rezistor orqali bitta qizil LED ni ulang va katodini Arduino `GND` ga bog'lang.
2. Tinkercad "Code" panelida C++ tilida quyidagi mantiqqa ega dastur yozing:
   - LED 1 soniya yonsin;
   - 500 millisekund o'chsin;
   - LED 2 soniya yonsin;
   - 1 soniya o'chsin;
   - Tsikl cheksiz takrorlansin.
3. Nima uchun 5V quvvatda ishlaydigan Arduino uchun 220 Om rezistor tanlanganini Om qonuni formulasi ($R = (5\text{V} - 2\text{V}) / 0.015\text{A}$) asosida yozma asoslab bering.

---

## Mentor uchun

### Baholash mezonlari (Jami 100 ball)
- **4-dars vazifasi (30 ball):** Tinkercad akkaunti to'g'ri ochilgani, loyiha nomlangani, asboblar (R, N) qo'llangani va ommaviy havola taqdim etilgani.
- **5-dars vazifasi (35 ball):** Breadboard ichki kontaktlari to'g'ri tushunilgani, kalit va rezistor to'g'ri ulangani, multimetr voltmetr (parallel) va ampermetr (ketma-ket) rejimida to'g'ri ko'rsatkich bergani.
- **6-dars vazifasi (35 ball):** Arduino 9-piniga to'g'ri sxema yig'ilgani, C++ tilida `setup()` va `loop()` arxitekturasi buzilmasdan vaqt intervallari to'g'ri kodlangani hamda Om qonuni hisobi keltirilgani.

### Eslatma
- O'quvchilar rezistor oyoqlarini bitta ustunga suqib qo'ymasligiga va kod yozishda `pinMode(LED, OUTPUT)` buyrug'ini tushirib qoldirmasligiga e'tibor qarating.
