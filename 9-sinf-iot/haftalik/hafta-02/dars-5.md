# 5-dars: Tinkercad muhitida virtual elektron komponentlar bilan ishlash

**Fan:** Internet of Things (IoT — Buyumlar Interneti)  
**Sinf:** 9-sinf  
**Hafta:** 2-hafta, 2-dars (umumiy 5-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga Tinkercad Circuits muhitidagi asosiy virtual elektron komponentlar: Breadboard (makrt plata), rezistor, LED, quvvat manbalari (9V batareya, 3V tanga batareya), kalitlar va virtual multimetr bilan ishlashni o'rgatish; ularni breadboard ustida to'g'ri o'zaro ulash hamda kuchlanish va tok kuchi ko'rsatkichlarini o'lchash ko'nikmalarini shakllantirish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- Breadboard (makrt plata) ichki tuzilishi: quvvat shinalari (gorizontal) va terminal teshiklar (vertikal) qanday bog'langanini tushunish;
- Rezistorning elektr zanjiridagi vazifasi (tokni cheklash) va rangli chiziqlar orqali qiymatini aniqlash;
- LED (yorug'lik diodi) qutblari: Anod (+) va Katod (-) ni farqlash hamda uning to'g'ri ulanishini ta'minlash;
- Virtual multimetrdan foydalanib, zanjirdagi kuchlanish (V) va tok kuchini (A / mA) to'g'ri o'lchash;
- Batareya, rezistor, kalit va LED dan iborat mustaqil yopiq elektr zanjirini breadboardda yig'ish va simulyatsiyada tekshirish.

---

## Kerakli jihozlar va vositalar

- Kompyuter yoki noutbuk (internetga ulangan);
- Veb-brauzer orqali Tinkercad.com hisobiga kirish;
- Proyektor yoki monitor (namoyish uchun).

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va o'tgan darsni takrorlash | Tinkercad interfeysi, tezkor klavishlar (R, Del, N) va sim ranglari bo'yicha blits-so'rov |
| **10–25 min** | Yangi mavzu: Breadboard va asosiy komponentlar | Makrt plata ichki arxitekturasi, rezistor (Om) va LED (Anod/Katod) qutblari |
| **25–40 min** | O'lchov asbobi: Virtual Multimetr | Multimetrni voltmetr va ampermetr rejimida zanjirga to'g'ri ulash (ketma-ket vs parallel) |
| **40–60 min** | Amaliy laboratoriya: Birinchi mustaqil zanjir | 9V batareya + Slide switch + 330 Om rezistor + LED zanjirini breadboardda yig'ish |
| **60–75 min** | Xatolarni tahlil qilish va tajribalar | Rezistor qiymatini o'zgartirib yorug'lik intensivligini kuzatish, rezistorsiz holat simulyatsiyasi |
| **75–80 min** | Xulosa va uyga vazifa | Asosiy xulosalarni qayd etish, vazifalarni e'lon qilish |

---

## Nazariy ma'lumotlar

### 1. Breadboard (Maket plata / Sxema yig'uvchi karta)

Breadboard — lehimlash (payka) talab qilmasdan, elektron zanjirlarni tez va oson yig'ish hamda prototiplash uchun xizmat qiluvchi maxsus plastik plata. Uning ichida metall prujinali o'tkazgich chiziqlar joylashgan:

1. **Quvvat shinalari (Power Rails — chetki qatorlar):**
   - Qizil chiziq bilan belgilangan `+` qatori butun bo'yi bo'ylab gorizontal ulangan (VCC / Quvvat uchun);
   - Moviy/qora chiziq bilan belgilangan `-` qatori ham bo'yi bo'ylab gorizontal ulangan (GND / Yer uchun).
2. **Terminal teshiklar (Markaziy ish maydoni):**
   - Harflar bilan belgilangan (a, b, c, d, e) va (f, g, h, i, j) 5 tadan teshik **vertikal ravishda (ustun bo'yicha)** bir-biri bilan tutashgan;
   - O'rtadagi chuqur ariqcha (DIP slot) chap va o'ng 5 talik qatorlarni bir-biridan elektr jihatdan ajratib turadi (mikrosxemalar o'rnatish uchun mo'ljallangan).

> **Muhim qoida:** Hech qachon bitta komponentning ikkala oyog'ini bir xil vertikal ustunga suqmang! Bu qisqa tutashuv (short circuit) keltirib chiqaradi va komponent orqali tok o'tmaydi.

### 2. Rezistor (Qarshilik) va ranglar kodi

Rezistor elektr tokining oqishiga to'sqinlik qiladi va zanjirdagi tok kuchini cheklaydi. Uning o'lchov birligi — **Om (Ω)**, shuningdek **kilo-om (1 kΩ = 1000 Ω)** va **mega-om (1 MΩ = 1 000 000 Ω)**.

Rezistor qiymatini aniqlash uchun korpusidagi rangli chiziqlar kodi qo'llaniladi:
- Masalan, **220 Ω** rezistor: Qizil (2) - Qizil (2) - Jigarrang (×10) - Oltin (±5%);
- **330 Ω** rezistor: To'q sariq (3) - To'q sariq (3) - Jigarrang (×10) - Oltin (±5%);
- **1 kΩ** rezistor: Jigarrang (1) - Qora (0) - Qizil (×100) - Oltin (±5%).

Rezistorning qutbi yo'q, uni zanjirga istalgan tomoni bilan ulash mumkin.

### 3. LED (Light Emitting Diode — Yorug'lik taratuvchi diod)

LED faqat bitta yo'nalishda tok o'tkazuvchi va yorug'lik nurlatuvchi yarimo'tkazgich asbobdir:
- **Anod (uzun oyoq, `+`):** Musbat kuchlanish manbaiga ulanadi;
- **Katod (qisqa oyoq, korpusi tekislangan tomon, `-`):** Manfiy qutbga (GND) ulanadi.

Oddiy LEDlar ishlashi uchun 15–20 mA tok va 1.8–3.2V kuchlanish talab etiladi. Agar unga to'g'ridan-to'g'ri 5V yoki 9V ulansa, cheklanmagan tok LED kristalini bir soniyada kuydiradi. Shuning uchun har doim LED bilan ketma-ket **220–330 Om** himoya rezistori ulanishi shart!

### 4. Virtual Multimetr bilan o'lchash

Tinkercad-dagi Multimetr 3 ta asosiy parametrni o'lchaydi:
1. **Voltage (Kuchlanish, V):** Zanjirga parallel ulanadi (komponentning ikki uchidagi potensiallar farqi);
2. **Amperage (Tok kuchi, A / mA):** Zanjir uzilib, multimetr zanjir bilan **ketma-ket** ulanadi (tok asbob ichidan o'tishi kerak);
3. **Resistance (Qarshilik, R):** Quvvat o'chirilgan holatda rezistorning ikki oyog'iga ulanadi.

---

## Amaliy mashg'ulot va topshiriqlar

### 1-topshiriq. Breadboardda quvvat shinalarini ulash (oson)
Ish maydoniga kichik breadboard (Small Breadboard) va 9V batareyani joylashtiring. 9V batareyaning musbat (qizil) simini breadboardning yuqori `+` shinasiga, manfiy (qora) simini esa `-` shinasiga ulang. Sim ranglarini standartga muvofiq qizil va qora qiling.

**Yechim:**
1. Components panelidan "Small Breadboard" va "9V Battery" olinadi.
2. 9V batareyaning "Positive" pinidan sim chiqarilib, breadboardning yuqori qizil `+` qatoriga ulanadi va ranglar menyusidan `Red` tanlanadi.
3. 9V batareyaning "Negative" pinidan sim chiqarilib, yuqori qora `-` qatoriga ulanadi va ranglar menyusidan `Black` tanlanadi.
4. Endi breadboardning butun yuqori qatori 9V quvvat bilan ta'minlandi.

### 2-topshiriq. Batareya, kalit, rezistor va LED zanjirini yig'ish (o'rta)
1-topshiriqda yig'ilgan quvvat shinasidan foydalanib, suriluvchi kalit (Slide switch), 330 Om rezistor va yashil LED dan iborat zanjir quring. Kalit surilganda LED yonishi, orqaga surilganda o'chishi lozim.

**Yechim:**
1. Breadboard o'rtasiga "Slide Switch" o'rnatiladi. Uning chap oyog'i (Terminal 1) qizil sim bilan `+` shinasiga ulanadi.
2. Kalitning o'rta oyog'idan (Common) bitta sim chiqarilib, breadboarddagi boshqa ustunga olib boriladi.
3. Shu ustunga 330 Om rezistorning bitta oyog'i, ikkinchi oyog'i esa yangi ustunga qo'yiladi.
4. Yashil LED ning Anodi (egik/uzun oyog'i) rezistor ustuniga, Katodi esa yonidagi bo'sh ustunga qo'yiladi.
5. LED ning Katodidan qora sim orqali breadboardning `-` (GND) shinasiga ulanadi.
6. "Start Simulation" bosiladi: kalit bosilganda zanjir ulanib, yashil LED charaqlab yonadi.

### 3-topshiriq. Multimetr yordamida LED kuchlanishi va tok kuchini o'lchash (qiyin)
2-topshiriqdagi zanjirga ikkita multimetr qo'shing: biri yashil LED dagi kuchlanish tushuvini (V), ikkinchisi esa zanjirdan o'tayotgan tok kuchini (mA) o'lchasin. Natijalarni tahlil qiling.

**Yechim:**
1. Birinchi multimetr "Voltage" rejimiga qo'yiladi. Qizil probi LED ning Anodiga, qora probi Katodiga (parallel) ulanadi.
2. Ikkinchi multimetr "Amperage" rejimiga qo'yiladi. Zanjir LED katodi bilan GND o'rtasida uziladi: LED katodi multimetrning musbat (qizil) probiga, multimetrning manfiy (qora) probi esa breadboard `-` shinasiga (ketma-ket) ulanadi.
3. "Start Simulation" bosiladi:
   - 1-multimetr (Voltmetr): Yashil LED da taxminan ~2.1V kuchlanish tushuvini ko'rsatadi;
   - 2-multimetr (Ampermetr): Zanjir bo'ylab taxminan ~20.9 mA tok oqayotganini ko'rsatadi.
4. Bu ko'rsatkichlar LED ning xavfsiz va to'liq nominal rejimda ishlayotganini isbotlaydi.

---

## Tezkor nazorat savollari

1. Breadboardning quvvat shinalari qaysi yo'nalishda, markaziy teshiklari qaysi yo'nalishda ulangan?
   - *Javob:* Quvvat shinalari bo'yi bo'ylab gorizontal ulangan; markaziy 5 talik teshiklar esa vertikal (ustun bo'yicha) ulangan.
2. LED ning Anod va Katod oyoqlarini qanday ajratish mumkin?
   - *Javob:* Anod — uzunroq va egilgan oyoq (musbat +); Katod — qisqaroq oyoq va korpusi bir tomondan tekislangan (manfiy -).
3. Tok kuchini o'lchashda ampermetr zanjirga qanday ulanadi?
   - *Javob:* Faqat ketma-ket (zanjirni uzib, tok asbob ichidan o'tishi ta'minlanadi).
4. Nega LED bilan har doim ketma-ket rezistor ulanishi kerak?
   - *Javob:* Rezistor tok kuchini 15–20 mA gacha cheklab, LED kristalining yonib ketishidan himoya qiladi.

---

## Keng tarqalgan xatolar va ularning oldini olish

- **Komponentning ikkala oyog'ini bitta ustunga tiqish:** O'quvchilar rezistor yoki LED ning har ikki oyog'ini bitta 5 talik vertikal qatorga ulab qo'yishadi. Natijada detalning ikki uchi tutashib qoladi (qisqa tutashuv) va detal orqali tok o'tmaydi. Har bir oyoq alohida ustunda bo'lishi shart.
- **Multimetrni Ampermetr rejimida parallel ulash:** Agar ampermetr to'g'ridan-to'g'ri batareya qutblariga parallel ulansa, ampermetr ichki qarshiligi 0 ga yaqin bo'lgani uchun kuchli qisqa tutashuv yuzaga keladi. Ampermetr har doim ketma-ket ulanadi.
