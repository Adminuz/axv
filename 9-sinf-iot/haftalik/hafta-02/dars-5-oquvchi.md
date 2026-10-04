# 5-dars: Tinkercad muhitida virtual elektron komponentlar bilan ishlash

**Fan:** Internet of Things (IoT — Buyumlar Interneti)  
**Sinf:** 9-sinf  
**Mavzu:** Virtual elektron komponentlar: Breadboard, rezistor, LED, batareyalar, kalitlar va multimetr

---

## Darsning qisqacha mazmuni

Haqiqiy elektronika va IoT qurilmalarini yaratishdan oldin ularning ishlash qonuniyatlarini tushunish muhimdir. Mazkur darsda biz elektronikaning "yuragi" hisoblangan asosiy elementlar — maket plata (Breadboard), tokni cheklovchi rezistorlar, yorug'lik chiqaruvchi diodlar (LED), quvvat manbalari hamda ko'rsatkichlarni o'lchovchi virtual multimetr bilan amalda ishlaymiz.

### Asosiy tushunchalar:
- **Breadboard (Maket plata):** Komponentlarni lehimlamasdan tez ulab sinash uchun mo'ljallangan plata. Quvvat shinalari gorizontal, markaziy teshiklari esa vertikal ulangan;
- **Rezistor (Qarshilik):** Elektr zanjirida tok kuchini cheklovchi element. O'lchov birligi — Om (Ω), kOm va MOm;
- **LED (Yorug'lik diodi):** Tok faqat bir tomonga o'tganda yorug'lik chiqaruvchi yarimo'tkazgich. Anod — musbat (`+`), Katod — manfiy (`-`);
- **Slide Switch / Push Button:** Zanjirni uzish va ulash uchun xizmat qiluvchi mexanik kalitlar;
- **Multimetr:** Kuchlanish (Volt — parallel ulanadi) va tok kuchini (Amper — ketma-ket ulanadi) o'lchovchi universal asbob;
- **Himoya qarshiligi:** LED kristalini yuqori tokdan saqlash uchun ketma-ket ulanadigan 220–330 Om rezistor.

---

## Mustaqil bajarish uchun topshiriqlar

### 1-topshiriq · oson
Tinkercad Circuits muhitida yangi loyiha oching va unga `9-sinf_Familiya_Dars5` deb nom bering. Ish maydoniga kichik breadboard (Small Breadboard) va 9V batareyani joylashtiring.

### 2-topshiriq · oson
9V batareyaning musbat (Positive) simini breadboardning yuqori qizil `+` shinasiga, manfiy (Negative) simini esa yuqori qora `-` shinasiga ulang. Sim ranglarini mos ravishda Qizil va Qora qilib belgilang.

### 3-topshiriq · oson
Ish maydoniga 1 ta rezistor qo'ying. Uning qiymatini parametrlar panelidan `330` qilib belgilang va birligini `Ω` (Om) ga o'tkazing. Rezistordagi rang chiziqlari qaysi ranglarga aylanganini daftaringizga qayd eting.

### 4-topshiriq · oson
Ish maydoniga qizil rangli LED joylashtiring. Sichqoncha kursorini uning oyoqlari ustiga olib borib, qaysi biri "Anode" va qaysi biri "Cathode" deb nomlanishini aniqlang.

### 5-topshiriq · o'rta
Breadboard ustiga quyidagi zanjirni yig'ing:
1. `+` shinasidan sim chiqarib, 330 Om rezistorning birinchi oyog'iga ulang;
2. Rezistorning ikkinchi oyog'ini LED ning Anodiga (uzun oyog'iga) ulang;
3. LED ning Katodini (qisqa oyog'ini) `-` (GND) shinasiga ulang.
"Start Simulation" tugmasini bosing va LED yonganini kuzating.

### 6-topshiriq · o'rta
Zanjirga "Slide Switch" (suriluvchi kalit) qo'shing. Kalitni surganingizda LED o'chishi va yoqilishi lozim. Kalitning 3 ta oyog'idan qaysi ikkitasi ulanishini tushuntirib bering.

### 7-topshiriq · o'rta
Komponentlar panelidan "Multimeter" asbobini olib chiqing va uni "Voltage" rejimiga qo'ying. Multimetrning qizil probini LED anodiga, qora probini katodiga ulang (parallel ulanish). "Start Simulation" bosib, LED dagi kuchlanish tushuvini (Volt) daftaringizga yozing.

### 8-topshiriq · o'rta
Zanjirdan LED katodi bilan GND o'rtasidagi simni uzing. Ikkinchi multimetrni "Amperage" rejimiga qo'ying va uni uzilgan oraliqqa ketma-ket ulang. Zanjirdan o'tayotgan tok kuchini (milliAmper — mA) aniqlang.

### 9-topshiriq · qiyin
Rezistor qiymatini avval `1 kΩ` (1000 Om), so'ngra `10 kΩ` (10000 Om) ga o'zgartiring va har safar simulyatsiyani ishga tushirib ko'ring. LED yorqinligi va ampermetr ko'rsatkichi qanday o'zgarganini taqqoslang va xulosa chiqaring.

### 10-topshiriq · qiyin
Alohida bo'sh joyda 9V batareyaga to'g'ridan-to'g'ri rezistorsiz LED ulab "Start Simulation" tugmasini bosing. LED ustida qanday belgi paydo bo'ldi? Kursorni ushbu belgi ustiga olib boring va Tinkercad bergan ogohlantirish xabarini so'zma-so'z ko'chirib yozing. Nima sababdan bu holat sodir bo'ldi?

### 11-topshiriq · bonus
3V tanga batareya (Coin Cell 3V — CR2032) oling. Nima uchun ushbu batareyaga 1 ta ko'k yoki oq LED ulanganda u rezistorsiz ham portlab ketmaydi, ammo 9V batareyada yonib ketadi? Fizik sababini tushuntirib bering.
