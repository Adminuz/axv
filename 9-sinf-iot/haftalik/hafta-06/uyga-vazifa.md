# 6-hafta: Uyga vazifa

**Fan:** IoT  
**Sinf:** 9-sinf  
**Hafta:** 6-hafta  
**Topshirish muddati:** Keyingi darsga qadar (7-hafta, 1-dars)

---

## Topshiriq 1: Mikrokontroller va IoT (2-qism) · qiyin

1. Mikrokontrollerning IoT dagi ikki vazifasini misollar bilan 5–6 gapda yozing.
2. ADC qiymatlari 100, 400, 900 uchun kuchlanishni hisoblang (U = 5 × qiymat / 1023).
3. Chegara dasturini o'zgartiring: qiymat 800 dan oshsa LED to'liq yonsin, aks holda o'chsin; kodni daftaringizga yozing.
4. Sensor → mikrokontroller → aktuator → bulut zanjiri uchun o'z misolingizni (masalan, aqlli sug'orish) chizing.

---

## Topshiriq 2: ESP8266 va ESP32 (umumiy) · o'rta

1. ESP8266 va ESP32 ni 6 ta xususiyat bo'yicha jadvalda solishtiring.
2. DHT11 ni ESP ga ulash sxemasini daftaringizga chizing va nega 3,3 V ishlatilishini yozing.
3. Harorat 24,0, namlik 48 va bosim 1012 qiymatlarini JSON ko'rinishida yozing.
4. Aqlli chiroq yoki ob-havo stansiyasi loyihasining blok-sxemasini chizing: sensor, ESP, Wi-Fi, bulut, foydalanuvchi.
5. Deep Sleep nima uchun kerakligini 3 jumlada tushuntiring.

---

## Topshiriq 3: Svetofor: Arduino va Tinkercad (1-qism) · oson

1. Tinkercad'da svetofor sxemasini yig'ing (9, 8, 7 pinlar), dasturni yozing va ekran suratini saqlang.
2. Qizil 6 s, sariq 2 s, yashil 8 s bo'ladigan variantni yozing; bir sikl necha soniyani olishini hisoblang.
3. 220 Ω va 330 Ω rezistorlar uchun LED tokini hisoblang (U = 5 V, U_LED = 2 V): I = (5 − 2) / R.
4. Dasturning har bir qatorini o'z so'zlaringiz bilan izohlang (komment sifatida).
5. Real svetofor tartibiga (qizil → yashil → sariq) mos variantni yozing.

---

## Baholash mezoni

| Mezon | Ball |
|---|---|
| 16-dars: Sensor, ADC va PWM bo'yicha masalalar | 3 |
| 17-dars: ESP8266/ESP32: farqlar, pinlar, JSON va 3,3 V | 3 |
| 18-dars: Svetofor: sxema va dastur bo'yicha topshiriqlar | 2 |
| Toza, o'z vaqtida va mustaqil bajarilgan | 2 |
| **Jami** | **10** |
| Bonus: bonus darajadagi topshiriq | +2 |

---

## Mentor uchun

**Tekshirish:**
- 16-dars: Dastur qayerga yuklanadi?? Javobi: Flash xotiraga; tok o'chganda ham saqlanadi.
- 17-dars: Energiya tejash rejimi?? Javobi: Deep Sleep.
- 18-dars: LEDning anodi va katodi qayerga ulanadi?? Javobi: Anod — pinga (rezistor orqali), katod — GND ga.

**Keng tarqalgan xatolar:**
- 16-dars: Analog pinni raqamli deb o'ylash va qiymatni 0/1 kutish.
- 17-dars: ESP ga 5 V ulash.
- 18-dars: LEDni rezistorsiz ulash.
