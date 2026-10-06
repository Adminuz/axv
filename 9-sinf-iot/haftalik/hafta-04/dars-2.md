# 11-dars: Breadboardda DIP switch (DPST) va LED yordamida oddiy elektron sikl yaratish (1-qism)

**Fan:** Internet of Things (IoT — Buyumlar Interneti)  
**Sinf:** 9-sinf  
**Hafta:** 4-hafta, 2-dars (umumiy 11-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga mikrokontrollersiz eng oddiy **elektr zanjiri (sikl)** — manba, kalit, rezistor va LED — tuzilishini, uning **ochiq va yopiq** holatlarini, breadboard ichki ulanishlarini, kalitlar turlari (SPST, SPDT, DPST, DPDT) va **DIP switch** tuzilishini o'rgatish; Om qonuni asosida LED uchun rezistor qiymatini hisoblash va Tinkercad'da DIP switch orqali LEDni yoqib-o'chiradigan sxemani yig'ish ko'nikmasini shakllantirish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- Elektr zanjirining 4 ta asosiy qismini (manba, o'tkazgich, iste'molchi, kalit) ayta olish;
- Ochiq va yopiq zanjir farqini tushuntira olish: tok faqat **yopiq** zanjirda oqadi;
- Breadboardda qaysi teshiklar o'zaro ulanganini (quvvat relslari, 5 teshikli ustunlar, markaziy ariqcha) bilish;
- Pole (qutb) va throw (yo'nalish) tushunchalari orqali SPST, SPDT, DPST, DPDT kalitlarini farqlay olish;
- DIP switch nima ekanini va har bir juft kontakt mustaqil kalit ekanini bilish;
- Om qonuni bo'yicha rezistor qiymatini hisoblay olish: `R = (U − U_LED) / I`;
- Tinkercad'da manba → DIP switch → rezistor → LED → GND zanjirini yig'ib, sinab ko'ra olish.

---

## Kerakli jihozlar va vositalar

- Kompyuter yoki noutbuk (internetga ulangan), Tinkercad.com (Circuits);
- Real to'plam (bo'lsa): breadboard, DIP switch (2 pozitsiyali), LEDlar, 220–330 Om rezistorlar, ulash simlari, 5V manba yoki 9V batareya (uslubiy ko'rsatma);
- Proyektor yoki monitor (namoyish uchun).

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Takrorlash | LED anod/katod, rezistor vazifasi, 10-darsdagi «holat» tushunchasi |
| **10–25 min** | Yangi mavzu: elektr zanjiri | Manba, o'tkazgich, iste'molchi, kalit; ochiq va yopiq zanjir |
| **25–35 min** | Breadboard tuzilishi | Quvvat relslari, terminal ustunlari, markaziy ariqcha |
| **35–45 min** | Kalitlar va DIP switch | SPST, SPDT, DPST, DPDT; DIP korpus, ON tomoni |
| **45–55 min** | Om qonuni va rezistor hisobi | 5V va 9V manba uchun misollar |
| **55–75 min** | Amaliy laboratoriya | Tinkercad'da DIP switch + LED zanjiri, ochiq/yopiq holat sinovi |
| **75–80 min** | Xulosa va uyga vazifa | Mavzuni umumlashtirish |

> Manba: o'quv dasturi — «Breadboardda DIP switch (DPST) va LED yordamida oddiy elektron sikl yaratish» (komponentlarni to'g'ri joylashtirish, DIP switch orqali signal boshqarish, LED bilan holatni ko'rsatish, ochiq va yopiq holat, xatolarni aniqlash); uslubiy ko'rsatma — kerakli jihozlar (breadboard, DIP switch DPST, LED, 220–330 Om rezistor, simlar, 9V yoki 5V manba, Tinkercad), ulash tartibi va «dastur yozilmaydi, chunki mikrokontrollerdan foydalanmadik».

---

## Nazariy ma'lumotlar

### 1. Elektr zanjiri (sikl) nima?

**Elektr zanjiri** — tok manbadan chiqib, iste'molchidan o'tib, yana manbaga qaytadigan **berk yo'l**. Uslubiy ko'rsatmada bu «elektron sikl» deb ataladi: tok sikl bo'ylab aylanadi.

| Qism | Vazifasi | Bizning sxemada |
|---|---|---|
| Manba | Kuchlanish beradi (+ va −) | 5V manba yoki 9V batareya |
| O'tkazgich | Tokni olib boradi | ulash simlari, breadboard ichki plastinkalari |
| Iste'molchi | Energiyani ishga aylantiradi | LED (yorug'lik) |
| Kalit | Zanjirni ochadi yoki yopadi | DIP switch |
| Himoya | Tokni cheklaydi | rezistor 220–330 Om |

- **Yopiq zanjir:** kalit yoqilgan (ON), yo'l uzluksiz → tok oqadi → LED yonadi.
- **Ochiq zanjir:** kalit o'chirilgan (OFF) yoki sim uzilgan → tok oqmaydi → LED o'chiq.

Bu 10-darsdagi «holat» ning eng oddiy shakli: kalitning holati to'g'ridan-to'g'ri LED holatini belgilaydi, **dastur yozilmaydi**.

### 2. Breadboard tuzilishi

**Breadboard** — komponentlarni payvandlashsiz ulash uchun teshikli plata. Ichida metall plastinkalar teshiklarni guruhlab ulaydi:

| Qism | Qanday ulangan | Nima uchun |
|---|---|---|
| Quvvat relslari (`+` qizil, `−` ko'k chiziq) | Butun uzunlik bo'ylab **gorizontal** | Manbaning `+` va GND ini tarqatish |
| Terminal ustunlari (a–e, f–j) | Har bir raqamli qatorda **5 ta teshik** o'zaro ulangan | Komponent oyoqlarini bir-biriga ulash |
| Markaziy ariqcha | Ikki yarmini **ajratadi** | DIP korpusli detallarni ustiga qo'yish uchun |

Qoida: bitta komponentning ikki oyog'i **bir xil 5 teshikli qatorga** tushsa, u qisqa tutashadi va ishlamaydi.

### 3. Kalitlar turlari: pole va throw

- **Pole (qutb)** — kalit nechta **mustaqil zanjirni** boshqaradi.
- **Throw (yo'nalish)** — har bir qutb nechta **holatga** ulana oladi.

| Tur | To'liq nomi | Ma'nosi | Misol |
|---|---|---|---|
| SPST | Single Pole, Single Throw | 1 zanjir, yoq/o'chir | oddiy chiroq kaliti |
| SPDT | Single Pole, Double Throw | 1 zanjir, 2 yo'nalishdan biri | ikki joydan boshqariladigan chiroq |
| DPST | Double Pole, Single Throw | 2 zanjir, yoq/o'chir | ikki simni birga uzuvchi kalit |
| DPDT | Double Pole, Double Throw | 2 zanjir, 2 yo'nalish | motor yo'nalishini almashtirish |

### 4. DIP switch

**DIP switch** (Dual In-line Package) — mikrosxema korpusiga o'xshash, ikki qator oyoqli kichik blok; ichida bir nechta **kichik kalit** (2, 4, 8 pozitsiya) bor. Har bir richag **bir juft kontaktni** ulaydi yoki uzadi.

- Uslubiy ko'rsatma va Tinkercad'dagi **DIP Switch DPST** — 2 pozitsiyali blok: **ikki juft kontakt**, har biri o'z richagi bilan **mustaqil** boshqariladi.
- Korpusda **ON** yozuvi bor: richag shu tomonga surilsa — kontakt yopiq.
- Breadboardga **markaziy ariqcha ustiga** qo'yiladi: shunda har bir oyoq alohida qatorga tushadi va juft kontaktlar bir-biri bilan qisqa tutashmaydi.
- Qo'llanishi: qurilma manzilini yoki rejimini **bir marta sozlash** (router, pult, sanoat qurilmalari).

### 5. Om qonuni va rezistor hisobi

`U = I × R` (kuchlanish = tok × qarshilik). LED uchun:

```
R = (U_manba − U_LED) / I
```

- `U_LED` — LED dagi kuchlanish tushishi: qizil ≈ 2 V, yashil/ko'k ≈ 3 V;
- `I` — xavfsiz tok: 10–15 mA (0,010–0,015 A), maksimal ≈ 20 mA.

| Manba | LED | Hisob | Tanlov |
|---|---|---|---|
| 5 V | qizil (2 V), 10 mA | (5 − 2) / 0,010 = 300 Om | **330 Om** |
| 5 V | qizil (2 V), 14 mA | (5 − 2) / 0,014 ≈ 214 Om | **220 Om** |
| 9 V | qizil (2 V), 15 mA | (9 − 2) / 0,015 ≈ 467 Om | **470 Om** |

Shuning uchun uslubiy ko'rsatmadagi 220–330 Om — **5V manba** uchun. **9V batareya** bilan kamida **470 Om** qo'ying: 220 Om da tok ≈ 32 mA bo'ladi va LED qizib, ishdan chiqishi mumkin.

Rezistor kichik → tok katta → LED juda yorqin, qiziydi. Rezistor katta → tok kichik → LED xira yoki umuman yonmaydi (uslubiy ko'rsatma).

### 6. Ulash tartibi (uslubiy ko'rsatma bo'yicha)

```
Manba (+)  →  DIP kontakt 1 (kirish)
DIP kontakt 1 (chiqish)  →  rezistor 330 Om
rezistor  →  LED anod (uzun oyoq, +)
LED katod (qisqa oyoq, −)  →  GND relsi
GND relsi  →  Manba (−)
```

1. DIP switch'ni markaziy ariqcha ustiga tekis joylang.
2. Manba `+` ini qizil relsga, `−` ini ko'k relsga ulang.
3. Qizil relsdan DIP kontaktining bir oyog'iga sim torting.
4. Kontaktning qarama-qarshi oyog'idan rezistor orqali LED anodiga.
5. LED katodini ko'k (GND) relsga.
6. Hammasini tekshirib, so'ng manbani yoqing. Richagni ON/OFF qilib LEDni kuzating.

---

## Amaliy mashg'ulot va topshiriqlar

### 1-topshiriq. Breadboard ulanishlarini aniqlash (oson)
Breadboard rasmida quyidagi juftliklar o'zaro ulanganmi? `a5` va `e5`; `a5` va `a6`; `e10` va `f10`; yuqori qizil relsdagi 1- va 30-teshik.

**Yechim:**
- `a5` va `e5` — **ulangan** (bir qatorning a–e qismi);
- `a5` va `a6` — **ulanmagan** (har xil qatorlar);
- `e10` va `f10` — **ulanmagan** (markaziy ariqcha ajratadi);
- qizil relsning 1- va 30-teshigi — **ulangan** (rels butun uzunlik bo'ylab). Eslatma: ba'zi katta breadboardlarda relslar o'rtada uzilgan bo'ladi — multimetr bilan tekshiring.

### 2-topshiriq. Rezistorni hisoblang (o'rta)
a) 5 V manba, yashil LED (3 V), tok 10 mA. b) 9 V batareya, qizil LED (2 V), tok 12 mA. Har biri uchun qarshilikni hisoblab, standart qatordan (220, 330, 470, 680, 1000 Om) mosini tanlang.

**Yechim:**
- a) R = (5 − 3) / 0,010 = **200 Om** → standartdan kattarog'i **220 Om** (tok biroz kamayadi, xavfsiz).
- b) R = (9 − 2) / 0,012 ≈ **583 Om** → **680 Om** (tok ≈ 10 mA). 470 Om ham mumkin (≈ 15 mA), lekin kattaroq tanlash xavfsizroq.

Qoida: hisobdan chiqqan son standartda bo'lmasa, **kattaroq** qiymat tanlanadi.

### 3-topshiriq. DIP switch va bitta LED (o'rta)
Tinkercad'da: Breadboard Small, «DIP Switch DPST», qizil LED, 330 Om rezistor va 5 V manba (Power Supply komponenti, kuchlanishi 5 V ga sozlangan). Zanjirni yig'ing, Start Simulation bosing va richagni ON/OFF qilib, ochiq va yopiq holatni ko'rsating.

**Yechim:**
| Ulash | Qayerdan | Qayerga |
|---|---|---|
| 1 | Manba `+` | qizil rels |
| 2 | Manba `−` | ko'k rels |
| 3 | qizil rels | DIP 1-kontakt, yuqori oyoq |
| 4 | DIP 1-kontakt, pastki oyoq | 330 Om rezistorning bir uchi |
| 5 | rezistorning ikkinchi uchi | LED anod |
| 6 | LED katod | ko'k rels |

Natija: richag ON — LED yonadi (yopiq zanjir), OFF — o'chadi (ochiq zanjir). Agar LED umuman yonmasa — LED teskari qo'yilgan bo'lishi mumkin (anod/katod), uni 180° burang.

### 4-topshiriq. Ikki kontakt — ikki mustaqil LED (qiyin)
DIP switch'ning ikkala juftini ishlating: 1-kontakt Qizil LEDni, 2-kontakt Yashil LEDni boshqarsin (har biri o'z rezistori bilan). 4 ta holat kombinatsiyasi uchun natija jadvalini to'ldiring.

**Yechim:**
Har bir kontakt alohida zanjir: `+ → DIP1 → 330 Om → Qizil LED → GND` va `+ → DIP2 → 220 Om → Yashil LED → GND`. Ikki zanjir faqat `+` va GND relslari orqali umumiy.

| DIP1 | DIP2 | Qizil | Yashil |
|---|---|---|---|
| OFF | OFF | o'chiq | o'chiq |
| ON | OFF | yoniq | o'chiq |
| OFF | ON | o'chiq | yoniq |
| ON | ON | yoniq | yoniq |

Xulosa: har bir juft kontakt **mustaqil** — biri ikkinchisiga ta'sir qilmaydi (uslubiy ko'rsatma: «har bir juft kontakt LEDni mustaqil ravishda yoqish yoki o'chirish imkonini beradi»).

---

## Tezkor nazorat savollari

1. Elektr zanjirining asosiy qismlari qaysilar?
   - *Javob:* Manba, o'tkazgich, iste'molchi va kalit; LED zanjirida himoya uchun rezistor ham bo'ladi.
2. Ochiq zanjirda nima uchun LED yonmaydi?
   - *Javob:* Yo'l uzilgan — tok manbaga qaytolmaydi, shuning uchun oqmaydi.
3. DIP switch breadboardga nega markaziy ariqcha ustiga qo'yiladi?
   - *Javob:* Har bir oyoq alohida qatorga tushishi va kontaktlar qisqa tutashmasligi uchun.
4. DPST qisqartmasi nimani bildiradi?
   - *Javob:* Double Pole, Single Throw — ikki zanjir, har biri faqat yoq/o'chir holatida.
5. 5 V manba va qizil LED (2 V) uchun 10 mA tokda qanday rezistor kerak?
   - *Javob:* (5 − 2) / 0,01 = 300 Om → 330 Om.

---

## Keng tarqalgan xatolar va ularning oldini olish

- **Komponentning ikki oyog'i bir qatorda:** rezistor yoki LED ning ikkala oyog'i bitta 5 teshikli qatorga qo'yilsa, ular «aylanib o'tiladi» va zanjir ishlamaydi. Oyoqlar har doim **turli** qatorlarda bo'lsin.
- **DIP switch ariqcha ustiga qo'yilmagan:** juft kontaktlar bir qatorga tushib, kalit doim «yoqiq» bo'lib qoladi. Ariqcha ustiga qo'ying.
- **LED teskari:** uzun oyoq (anod) `+` tomonga, qisqa oyoq (katod) GND ga. Tinkercad'da LED ustiga sichqonchani olib borsangiz, oyoq nomi chiqadi.
- **Rezistorsiz ulash:** 5 V yoki 9 V to'g'ridan-to'g'ri LEDga berilsa, u kuyadi (Tinkercad'da LED ustida portlash belgisi chiqadi).
- **9 V batareyada 220 Om:** tok ≈ 32 mA — juda katta. 9 V uchun 470 Om yoki undan kattaroq qo'ying.
