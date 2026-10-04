# 1-dars. IoT tushunchasi va qo‘llanish sohalari

## Darsning asosiy mazmuni

Bugungi kunda texnologiyalar shunchalik rivojlandiki, nafaqat kompyuter va smartfonlar, balki choynaklar, muzlatgichlar, svetoforlar, tibbiy apparatlar va butun boshli fabrikalar internet orqali bir-biri bilan "gaplashmoqda". Ushbu ulkan ekotizim **Internet of Things (IoT) — Buyumlar Interneti** deb ataladi.

---

## 1. IoT nima va u qanday paydo bo'lgan?

- **Ta'rifi:** **Buyumlar Interneti (IoT)** — bu internet tarmog'iga ulangan, o'rnatilgan sensorlar orqali atrof-muhitni sezuvchi va inson aralashuvisiz bir-biri bilan ma'lumot almashib, avtomatik qarorlar qabul qiluvchi aqlli jismoniy qurilmalar tizimidir.
- **Tarixi:** Ushbu atama birinchi marta **1999 yilda** britaniyalik kompyuter olimi **Kevin Eshton (Kevin Ashton)** tomonidan radiochastotali identifikatsiya (RFID) texnologiyalari taqdimotida qo'llanilgan.

### An'anaviy Internet va IoT Tarmog'i Taqqosi:

| Ko'rsatkich | An'anaviy Internet | Internet of Things (IoT) |
|---|---|---|
| **Asosiy ishtirokchilar** | Odamlar (Foydalanuvchilar) | Mashinalar va qurilmalar (Smart Devices) |
| **Muloqot turi** | Inson — Inson (H2H) yoki Inson — Kompyuter | Mashina — Mashina (**M2M** — Machine to Machine) |
| **Ma'lumot manbai** | Odamlar klaviatura orqali yozgan matn, rasm, video | Sensorlar o'lchagan fizik kattaliklar (harorat, bosim, gaz) |
| **Harakat tartibi** | Odam buyruq bersa bajariladi | Belgilangan qoidalar asosida **avtonom (avtomatik)** ishlaydi |

---

## 2. IoT ning 3 ta asosiy bo'g'ini

Har qanday IoT qurilmasi inson organizmiga o'xshash 3 ta vazifani bajaradi:

1. **Sezish (Sensing):** Sensorlar xuddi inson ko'zi, qulog'i va terisi kabi atrofdagi harorat, yorug'lik, harakat va gazni sezadi va elektr signaliga aylantiradi.
2. **Ulanish (Connectivity):** To'plangan ma'lumotlar Wi-Fi, Bluetooth, ZigBee, LoRaWAN yoki mobil tarmoq orqali serverga yoki bulutga (Cloud) uzatiladi.
3. **Bajarish (Actuation):** Tizim buyruq berganda, aktuatorlar (dvigatellar, relelar, klapanlar) inson qo'li kabi jismoniy harakatni bajaradi (chiroqni yoqadi, eshikni qulflaydi, suv purkaydi).

---

## 3. IoT texnologiyalarining asosiy qo'llanish sohalari

```
+--------------------------------------------------------------------------+
|                  INTERNET OF THINGS (IoT) QO'LLANILISHI                  |
+-------------------+------------------+------------------+----------------+
|    Aqlli Uy       |   Sanoat (IIoT)  |  Tibbiyot (IoMT) |   Qishloq Xo'j.|
| (Smart Home)      | (Industrial IoT) | (Medical Things) |  (Smart Agri)  |
|                   |                  |                  |                |
| - Aqlli termostat | - Stanoklar vibr.| - Masofaviy EKG  | - Tuproq naml. |
| - Avto chiroqlar  | - Oldindan ta'mir| - Smart glyukoza | - Avto sug'or. |
| - Oqish datchigi  | - Robot konveyer | - Tez yordam GPS | - Dron nazorat |
+-------------------+------------------+------------------+----------------+
```

1. **Aqlli Uy (Smart Home):** Odam uyga kelganda eshik qulfi yuzni tanib ochiladi, chiroqlar avtomatik yonadi, konditsioner xona haroratini 22°C ga sozlaydi. Gaz yoki suv sizib chiqsa, avtomatik to'xtatilib, egasining telefoniga xabar yuboriladi.
2. **Sanoat IoT (IIoT):** Katta zavodlarda minglab sensorlar o'rnatiladi. Ular stanoklarning qizib ketishi yoki tebranishini nazorat qilib, avariya bo'lishidan bir necha kun oldin nosozlikni aniqlaydi (**Predictive Maintenance**).
3. **Tibbiyot IoT (IoMT):** Smart soatlar va taqiladigan datchiklar bemorning yurak urishini, qon bosimini va kislorod miqdorini doimiy o'lchab, shifokorga yuboradi. Zarurat tug'ilsa, tez yordamga avtomatik chaqiriq ketadi.
4. **Aqlli Qishloq Xo'jaligi (Smart Agriculture):** Dalaga o'rnatilgan sensorlar tuproq namligini kuzatadi. Suv yetishmasa nasos o'zi ishga tushadi, yomg'ir yog'sa o'chadi. Suv va o'g'it sarfi 50% gacha tejaladi.
5. **Aqlli Shahar (Smart City):** Tirbandlikka qarab vaqtini o'zgartiruvchi svetoforlar, faqat mashina yaqinlashganda yorishuvchi ko'cha chiroqlari va to'lganida signal beruvchi aqlli chiqindi qutilari.

---

## Amaliy topshiriqlar

### 1-topshiriq. IoT atamasining ta'rifi · oson
"Buyumlar Interneti" (IoT) nima? Kevin Eshton ushbu atamani nechanchi yilda va qanday maqsadda taklif qilgan?

### 2-topshiriq. Oddiy buyum va IoT buyum farqi · oson
Quyidagi juftliklardagi oddiy qurilma bilan aqlli IoT qurilmasi o'rtasidagi farqni bitta jumlada tushuntiring:
a) Oddiy mexanik choynak va Aqlli elektr choynak;
b) Oddiy devor soati va Smart soat (Apple Watch / Galaxy Watch).

### 3-topshiriq. Sensor va aktuatorning inson organi bilan o'xshashligi · oson
IoT tizimidagi "Sensor" va "Aktuator" tushunchalarini insonning qaysi tana a'zolari bilan qiyoslash mumkin? 2 tadan hayotiy misol keltiring.

### 4-topshiriq. Xonani xavfsiz qilish bo'yicha g'oya · o'rta
O'zingiz yashayotgan xona uchun gaz sizib chiqishi (propan/metan) va yong'inni aniqlovchi sodda IoT tizimini o'ylab toping. Tizimda qanday sensor va qanday ogohlantiruvchi vosita bo'lishi kerak?

### 5-topshiriq. Aqlli muzlatgich ssenariysi · o'rta
Agar oshxonadagi muzlatgichga IoT sensorlari (kamera, vazn datchigi va Wi-Fi) o'rnatilsa, u o'z egasiga qanday 3 ta foydali avtomatik xizmatni ko'rsatishi mumkin?

### 6-topshiriq. Sanoatda IoT tejamkorligi (IIoT) · o'rta
Katta elektr stansiyasida turbinalarga vibratsiya (tebranish) sensorlari o'rnatildi. Bu texnologiya turbina to'satdan sinib, butun shahar chiroqsiz qolishining oldini qanday oladi?

### 7-topshiriq. Aqlli shahar transporti · o'rta
Toshkent shahrida avtomobil tirbandliklarini kamaytirish uchun chorrahalarga qanday sensorlar o'rnatilishi va svetoforlar o'z vaqtini qanday avtomatik o'zgartirishi kerak? Tizim loyihasini chizing yoki yozing.

### 8-topshiriq. Aqlli issiqxona sxemasini tuzish · qiyin
Pomidor yetishtiriladigan issiqxona uchun to'liq IoT tizimi rejasini tuzing:
- Qanday 3 ta parametr o'lchanadi?
- Agar harorat juda ko'tarilib ketsa, qaysi qurilma nima ish qiladi?
- Ma'lumot fermerning telefonida qanday ko'rinadi?

### 9-topshiriq. IoT xavfsizligi va xakerlik tahdidi · qiyin
Tasavvur qiling, shifoxonadagi bemorlarning yurak stimulyatorlari yoki uydagi aqlli eshik qulflari internetga ulangan, ammo parollari oddiy (`12345`). Agar kiberjinoyatchi bu tizimga kirsa, qanday halokatli oqibatlar kelib chiqishi mumkin? IoT da xavfsizlik nima uchun birinchi o'rinda turishi kerak?

### 10-topshiriq. O'zingizning mualliflik IoT loyihangiz · bonus
Maktabingiz yoki uyingizdagi biror muammoni (masalan, partalarning tozaligi, o'simliklarni o'z vaqtida sug'orish, dars vaqtida chiroqlarni tejash) hal qiluvchi o'zingizning original IoT qurilmangiz g'oyasini yozing. Qurilmaning nomi, vazifasi va tarkibiy qismlarini ko'rsating.
