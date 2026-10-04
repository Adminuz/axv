# 1-hafta: Uyga vazifalar to'plami

Mazkur haftada o'tilgan darslar bo'yicha mustaqil bajarish uchun topshiriqlar. Har bir vazifa 20–30 daqiqaga mo'ljallangan.

---

## 1-dars: IoT tushunchasi va qo‘llanish sohalari

1. O'zingiz yashayotgan xonadonda yoki maktabda IoT yordamida avtomatlashtirish mumkin bo'lgan 2 ta muammoni aniqlang (masalan, chiroqni o'chirishni unutish, gulni qachon sug'orishni bilmaslik).
2. Ushbu muammolarni an'anaviy yechim va IoT yechimi nuqtai nazaridan solishtirib bering.
3. Har bir tizim qaysi sohaga (Smart Home, Smart Agriculture, IIoT yoki Smart City) tegishli ekanini yozing.
4. Tizimda inson omilini kamaytirish (M2M — Machine to Machine tamoyili) qanday afzallik keltirishini 3 ta jumla bilan ifodalang.

---

## 2-dars: IoT arxitekturasi: Sensorlar, aktuatorlar va apparat ta'minoti

1. O'zingiz o'ylab topgan bitta IoT loyihasi (masalan, aqlli eshik qo'ng'irog'i yoki aqlli akvarium) uchun zarur bo'ladigan komponentlar ro'yxatini tuzing:
   - Kamida 2 ta sensor (analog va raqamli);
   - Kamida 2 ta aktuator (masalan, rele, motor, buzzer, ekran);
   - Bitta boshqaruvchi platasi (Arduino Uno yoki ESP32).
2. Nima sababdan ushbu boshqaruvchi platasini tanlaganingizni asoslab bering (Wi-Fi kerakmi yoki oddiy hisoblash yetarlimi?).
3. Nima uchun 220V tokda ishlaydigan elektr asboblarini to'g'ridan-to'g'ri mikrokontroller piniga ulab bo'lmasligini va bu yerda rele moduli qanday vazifani bajarishini tushuntiring.

---

## 3-dars: IoT arxitekturasi: Tarmoq, bulut va foydalanuvchi interfeysi

1. O'z loyihangiz uchun eng ma'qul simsiz aloqa texnologiyasini tanlang (Wi-Fi, Bluetooth Low Energy, LoRaWAN yoki Zigbee) va nima sababdan aynan shu texnologiya tanlanganini (masofa, quvvat sarfi, tezlik) tushuntiring.
2. Mikrokontrollerdan bulutga ma'lumot uzatishda nima uchun HTTP emas, balki MQTT protokoli tavsiya etilishini 3 ta asosiy sabab bilan bayon qiling.
3. Foydalanuvchi mobil telefondagi Blynk (yoki shunga o'xshash) dashboard orqali qanday ko'rsatkichlarni ko'rishi va qanday tugmalar orqali qurilmani boshqarishi mumkinligining sxematik eskizini chizing yoki matn ko'rinishida tavsiflang.
4. Tizimda qaysi muhim qarorlar internetga qaramasdan Edge (lokal) darajasida, qaysilari esa Cloud (bulut) darajasida qabul qilinishini ajratib bering.

---

## Mentor uchun

### Baholash mezonlari (Jami 100 ball)
- **1-dars vazifasi (30 ball):** IoT ning M2M tabiati to'g'ri tushunilgani, real hayotiy muammolar aniqlangani va to'g'ri sohalarga ajratilgani.
- **2-dars vazifasi (35 ball):** Sensor va aktuatorlar to'g'ri tanlangani, analog/raqamli farqi, relening galvanik izolyatsiya roli hamda Arduino/ESP32 imkoniyatlari to'g'ri baholangani.
- **3-dars vazifasi (35 ball):** Simsiz tarmoq turi (Wi-Fi vs LoRaWAN), MQTT protokoli afzalligi, dashboard loyihasi hamda Edge vs Cloud Computing tushunchalari to'g'ri qo'llangani.

### Eslatma
- O'quvchilar apparat qismlarini (hardware) shunchaki nomma-nom sanab ketmasdan, ularning signallari (kirish sensori -> mikrokontroller dasturi -> chiqish aktuatori) qanday zanjir hosil qilishini tushunganiga e'tibor bering.
