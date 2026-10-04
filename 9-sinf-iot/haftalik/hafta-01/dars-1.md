# 1-dars. IoT tushunchasi va qo‘llanish sohalari

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga Buyumlar Interneti (Internet of Things — IoT) tushunchasi, uning paydo bo'lish tarixi (Kevin Eshton, 1999), an'anaviy internetdan farqli jihatlari hamda IoT texnologiyalarining zamonaviy sohalarda (aqlli uy, sanoat, tibbiyot, qishloq xo'jaligi, transport) qo'llanilishi bo'yicha fundamental bilimlarni berish.
- **Kutiladigan natija:** O'quvchilar IoT tushunchasini to'g'ri ta'riflay oladi; inson aralashuvisiz qurilmalar o'rtasida ma'lumot almashish (M2M) tamoyilini tushunadi; o'z hayotiy misollarida turli sohalardagi IoT tizimlarini tahlil qila oladi.
- **Vaqt taqsimoti:**
  - Kirish va qiziqtirish ("Aqlli choynakdan to aqlli shahargacha"): 10 daqiqa
  - Yangi mavzu: IoT nima? Tarixi va an'anaviy internetdan farqi: 25 daqiqa
  - Qo'llanish sohalari tahlili (Smart Home, IIoT, IoMT, Smart City, Smart Ag): 25 daqiqa
  - Amaliy topshiriqlar va muhokama: 15 daqiqa
  - Dars xulosasi va tezkor savollar: 5 daqiqa

---

## Mentor konspekti

### 1. IoT tushunchasi va tarixi
- **IoT (Internet of Things — Buyumlar Interneti):** Bu internet orqali o'zaro bog'lanib, inson yordamiga ehtiyoj sezmasdan bir-biriga ma'lumot yubora oladigan, atrof-muhitni sezuvchi va avtomatik qaror qabul qiluvchi jismoniy qurilmalar tarmog'idir.
- **Tarixi:** Atama ilk bor 1999 yilda kompyuter olimi **Kevin Eshton (Kevin Ashton)** tomonidan Procter & Gamble kompaniyasida RFID (radiochastotali identifikatsiya) texnologiyalari taqdimotida ishlatilgan.
- **An'anaviy internet vs IoT:**
  - *An'anaviy Internet:* Odamlar tomonidan kiritilgan ma'lumotlar tarmog'i (Human-to-Human / Human-to-Computer: veb-saytlar, xabarlar, videolar).
  - *IoT Tarmog'i:* Qurilmalarning o'zlari to'plagan va almashadigan ma'lumotlar tarmog'i (Machine-to-Machine — M2M).

### 2. IoT ning 3 ta asosiy xususiyati
1. **Atrofni his qilish (Sensing):** Sensorlar orqali harorat, yorug'lik, bosim, gaz, harakat parametrlarini o'lchash.
2. **Ulanish (Connectivity):** To'plangan ma'lumotlarni simsiz (Wi-Fi, Bluetooth, LoRaWAN, GSM) yoki simli tarmoqlar orqali uzatish.
3. **Avtonom harakat (Actuation / Automation):** Kelgan buyruq asosida inson buyrug'isiz dvigatelni yoqish, eshikni qulflash, suv quyish yoki signal chalish.

### 3. IoT texnologiyalarining qo'llanish sohalari
1. **Aqlli Uy (Smart Home):**
   - Masofadan boshqariluvchi aqlli chiroqlar, aqlli termostatlar (masalan, Nest), harakat sezgichlari, qochqin gaz va suvni avtomatik to'suvchi klapanlar.
   - Maqsad: qulaylik, xavfsizlik va energiyani 30-40% gacha tejash.
2. **Sanoat IoT (IIoT — Industrial IoT):**
   - Zavod va fabrikalardagi stanoklar va konveyerlarga vibratsiya va harorat sensorlarini o'rnatish.
   - *Predictive Maintenance (Oldindan ta'mirlash):* Stanok buzilmasdan bir necha kun oldin tebranish o'zgarganini sezib, avtomatik xabar beradi.
3. **Tibbiyot IoT (IoMT — Internet of Medical Things):**
   - Aqlli puls-oksimetrlar, qondagi glyukoza datchiklari, yurak kardiomonitorlari.
   - Bemor uyida yotganda shifokor kompyuterida uning barcha ko'rsatkichlari real vaqtda ko'rinib turadi.
4. **Aqlli Qishloq Xo'jaligi (Smart Agriculture):**
   - Tuproq namligi va kislotaliligini o'lchovchi sensorlar, meteorologik stantsiyalar.
   - Tuproq qurisa, tomchilatib sug'orish nasosi avtomatik ishga tushadi; yomg'ir yog'sa, o'z-o'zidan to'xtaydi.
5. **Aqlli Shahar va Logistika (Smart City):**
   - Aqlli svetoforlar (tirbandlikka qarab yashil chiroq vaqtini o'zgartiradi), aqlli chiqindi qutilari (to'lganida mashinaga xabar beradi), GPS orqali yuk harakatini kuzatish.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Oddiy buyumni IoT qurilmaga aylantirish (oson)
Xonada turgan oddiy ko'cha chirog'i (fonar) mavjud.
Ushbu chiroqni "Aqlli ko'cha chirog'i"ga (Smart Street Light) aylantirish uchun unga qanday 3 ta komponent qo'shilishi kerak va u qanday avtomatik qoidada ishlashi lozim?

**Yechim:**
1. **Sensor:** LDR (fotorezistor — yorug'lik sensori) va PIR (harakat sensori).
2. **Boshqaruvchi (Mikrokontroller):** Arduino yoki ESP8266/ESP32 platasi.
3. **Aktuator:** Rele (Relay) yoki tranzistorli drayver (chiroqni yoqish/o'chirish uchun).
4. **Ishlash algoritmi:** Kunduzi yorug'lik yuqori bo'lganda chiroq butunlay o'chiq turadi. Tunda yorug'lik tushganda chiroq 20% xira rejimda turadi; agar PIR sensori odam yoki mashina yaqinlashganini sezsa, chiroq 100% yorqinlikka ko'tariladi va odam o'tib ketgach yana xiralashadi. Natijada shahar elektr energiyasi 70% gacha tejaladi.

### 2-topshiriq. Issiqxona uchun IoT monitoring tizimi arxitekturasi (o'rta)
Pomidor yetishtiriladigan zamonaviy issiqxonada hosildorlikni oshirish uchun avtomatlashtirilgan IoT tizimi loyihalanmoqda.
Issiqxona ichidagi qaysi 3 ta muhit parametrini doimiy o'lchash kerak va qanday aktuatorlar orqali harorat va namlik barqaror ushlab turiladi?

**Yechim:**
1. **O'lchanadigan parametrlar:**
   - Havo harorati va havoning nisbiy namligi (masalan, DHT22 sensori);
   - Tuproq namligi (Soil Moisture Sensor);
   - Quyosh nuri yoritilganlik darajasi (LDR / Lux sensor).
2. **Ijrochi mexanizmlar (Aktuatorlar):**
   - Agar havo harorati 32°C dan oshsa — avtomatik ventilyator yoki darcha ochuvchi servo-motor ishga tushadi;
   - Agar tuproq namligi 40% dan pastga tushsa — suv klapani (solenoid valve) ochilib, tomchilatib sug'orish nasosi yoqiladi;
   - Agar tuproq me'yoriga yetkazib namlansa — nasos avtomatik o'chadi.

### 3-topshiriq. An'anaviy tizim vs IoT: logistika sovuqxonasini taqqoslash (qiyin)
Muzqaymoq va dorilarni tashiydigan refrijerator yuk mashinasi mavjud.
An'anaviy usulda yuk tashish bilan IoT tizimi o'rnatilgan refrijerator o'rtasidagi xatolar va xavflarni solishtirib bering. IoT tizimi qanday qilib millionlab dollarlik zararning oldini oladi?

**Yechim:**
1. **An'anaviy tizimda:** Haydovchi yo'lga chiqadi, muzlatgich nosozligi yoki elektr uzilishi faqat manzilga yetib borganda (dorilar erib, yaroqsiz holga kelganda) aniqlanadi. Katta moliyaviy zarar va insonlar salomatligiga xavf yuzaga keladi.
2. **IoT tizimida:**
   - Refrijerator ichiga harorat sensori (DS18B20) va GPS/GSM moduli ulanadi.
   - Ma'lumot har 30 soniyada bulutli serverga (Cloud) uzatiladi.
   - Agar harorat -18°C dan -10°C gacha ko'tarilsa, tizim bir soniya ichida haydovchining smartfoniga va kompaniya dispetcheriga shoshilinch SMS/Telegram ogohlantirish yuboradi.
   - Haydovchi zudlik bilan to'xtab muzlatgichni tekshiradi va mahsulot buzilishining oldi olinadi.

---

## Tezkor nazorat savollari

1. "Internet of Things" (IoT) atamasi ilk bor qachon va kim tomonidan taklif qilingan?
   - *Javob:* 1999 yilda kompyuter olimi Kevin Eshton (Kevin Ashton) tomonidan.
2. An'anaviy internet bilan IoT tarmog'ining asosiy farqi nimada?
   - *Javob:* An'anaviy internetda ma'lumotlarni odamlar kiritadi va ko'radi (Human-to-Human), IoT da esa ma'lumotlarni qurilmalarning o'zlari inson aralashuvisiz to'playdi va almashadi (Machine-to-Machine — M2M).
3. Tibbiyot sohasida qo'llaniladigan IoT yo'nalishi qisqartmasi qanday ataladi?
   - *Javob:* IoMT (Internet of Medical Things).
4. IoT tizimida atrof-muhitdagi fizik ko'rsatkichlarni (harorat, yorug'lik, bosim) elektr signaliga aylantiruvchi qism qanday ataladi?
   - *Javob:* Sensor (Datchik).

---

## Keng tarqalgan xatolar va ularning oldini olish

- **IoT ni oddiy masofadan boshqarish (Remote Control) bilan adashtirish:** O'quvchilar ko'pincha televizor pultini yoki simsiz o'yinchoq mashinani IoT deb o'ylashadi. IoT bo'lishi uchun qurilma internet/bulut tarmog'iga ulangan bo'lishi, atrof-muhitdan mustaqil ma'lumot to'plashi va tahlil qila olishi shart.
- **Xavfsizlikni unutish:** IoT qurilmalari internetga to'g'ridan-to'g'ri ulangani sababli, agar standart parollar (masalan, `admin/admin`) o'zgartirilmasa, xakerlar aqlli kamera yoki eshik qulflarini osongina buzib kirishi mumkin. Dastlabki darslardanoq xavfsizlik madaniyatini singdirish lozim.
