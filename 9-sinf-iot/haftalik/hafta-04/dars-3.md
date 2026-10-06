# 12-dars: Breadboardda DIP switch (DPST) va LED yordamida oddiy elektron sikl yaratish (2-qism)

**Fan:** Internet of Things (IoT — Buyumlar Interneti)  
**Sinf:** 9-sinf  
**Hafta:** 4-hafta, 3-dars (umumiy 12-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

11-darsdagi DIP switch + LED zanjirini rivojlantirish: kalitlarni **ketma-ket** (AND — «VA») va **parallel** (OR — «YOKI») ulash orqali mantiqiy boshqaruv yaratish, rezistor qiymati LED yorqinligi va tokka qanday ta'sir qilishini **multimetr** bilan o'lchash, yig'ilgan sxemadagi xatolarni tizimli izlash (troubleshooting) va bob yakunida DIP switch'ni Arduino UNO ning raqamli kirishlariga ulab, uning holatini **ikkilik kod** (2 bit → 4 rejim) sifatida o'qishni o'rgatish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- Ketma-ket ulangan ikki kalit **VA** (AND), parallel ulangan ikki kalit **YOKI** (OR) mantiqini berishini tushuntirish va haqiqat jadvalini tuzish;
- Tinkercad multimetri bilan kuchlanish (parallel ulab) va tokni (zanjirni uzib, ketma-ket ulab) o'lchay olish;
- Rezistor qiymati oshganda tok kamayib, LED xiralashishini o'lchov bilan isbotlash;
- Ishlamayotgan sxemada xatoni bosqichma-bosqich topish (manba → kalit → rezistor → LED → GND);
- DIP switch'ni `INPUT_PULLUP` bilan Arduino'ga ulab, ON holat `LOW` o'qilishini bilish;
- Ikki kalitdan 2 bitli son (0–3) hosil qilib, rejimni tanlovchi dastur yoza olish.

---

## Kerakli jihozlar va vositalar

- Kompyuter yoki noutbuk (internetga ulangan), Tinkercad.com (Circuits);
- Breadboard, DIP Switch DPST, 2–3 ta LED, rezistorlar (220, 330, 1000 Om), multimetr, 5 V manba, Arduino UNO (oxirgi topshiriq uchun);
- Proyektor yoki monitor (namoyish uchun).

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Takrorlash | Ochiq/yopiq zanjir, breadboard qatorlari, Om qonuni bo'yicha 3 ta savol |
| **10–25 min** | Kalitlar mantig'i | Ketma-ket = VA, parallel = YOKI; haqiqat jadvallari, real misollar |
| **25–40 min** | Multimetr bilan o'lchash | Kuchlanish va tok; 220 / 330 / 1000 Om tajribasi |
| **40–50 min** | Nosozliklarni izlash | 6 qadamli tekshiruv ro'yxati |
| **50–70 min** | DIP switch + Arduino | `INPUT_PULLUP`, 2 bit, 4 rejim, Serial Monitor |
| **70–80 min** | Xulosa, uyga vazifa | II bob yakuni, keyingi bobga ko'prik |

> Manba: o'quv dasturi — «DIP switch orqali signal boshqarish», «Tok oqimini zanjir bo'ylab taqsimlash», «Oddiy boshqaruv mexanizmini yaratish», «Yig'ilgan sxemani tekshirish, xatolarni aniqlash va tuzatish»; uslubiy ko'rsatma — «switchning ikkita juftini alohida yoqib/o'chirib ... har bir kontaktning siklga ta'sirini tahlil qilish», «rezistor qiymatini o'zgartirish orqali LED yorqinligi va tok oqimini o'rganish».

---

## Nazariy ma'lumotlar

### 1. Ketma-ket ulangan kalitlar — VA (AND)

Ikki kalit bitta yo'lga **ketma-ket** qo'yilsa, tok ikkalasidan ham o'tishi kerak:

```
+5V → DIP1 → DIP2 → 330 Om → LED → GND
```

| DIP1 | DIP2 | LED |
|---|---|---|
| OFF | OFF | o'chiq |
| ON | OFF | o'chiq |
| OFF | ON | o'chiq |
| ON | ON | **yoniq** |

LED faqat **ikkala** kalit yoqilganda yonadi. Real misol: sanoat pressi faqat ishchi **ikkala qo'li** bilan ikki tugmani bosganda ishlaydi — qo'l xavfsizligi.

### 2. Parallel ulangan kalitlar — YOKI (OR)

Ikki kalit ikki **parallel** yo'l hosil qilsa, tok istalgan biridan o'ta oladi:

```
        ┌─ DIP1 ─┐
+5V ────┤        ├── 330 Om → LED → GND
        └─ DIP2 ─┘
```

| DIP1 | DIP2 | LED |
|---|---|---|
| OFF | OFF | o'chiq |
| ON | OFF | **yoniq** |
| OFF | ON | **yoniq** |
| ON | ON | **yoniq** |

Real misol: avtobusdagi «to'xtash» signali — istalgan eshik yonidagi tugma chiroqni yoqadi.

Breadboardda parallel ulash: ikkala kontaktning **kirish** oyoqlari `+` relsga, **chiqish** oyoqlari esa **bitta umumiy qatorga** ulanadi va shu qatordan rezistor boshlanadi.

### 3. Multimetr bilan o'lchash

| O'lchov | Rejim | Qanday ulanadi | Kutilgan natija (5 V, qizil LED, 330 Om) |
|---|---|---|---|
| Kuchlanish manbada | Voltage (V) | manbaga **parallel** | ≈ 5 V |
| Kuchlanish LEDda | Voltage (V) | LED oyoqlariga **parallel** | ≈ 2 V |
| Kuchlanish rezistorda | Voltage (V) | rezistor uchlariga **parallel** | ≈ 3 V |
| Tok | Current (A/mA) | zanjirni uzib, **ketma-ket** | ≈ 9 mA |

Tekshiruv: rezistordagi va LEDdagi kuchlanishlar yig'indisi manba kuchlanishiga teng: 3 V + 2 V = 5 V (7-darsdagi `U = U1 + U2`).

**Diqqat:** tok rejimidagi multimetrni hech qachon manbaga parallel ulamang — u qisqa tutashuv hosil qiladi.

### 4. Rezistor va yorqinlik

| Rezistor | Tok `I = (5 − 2) / R` | LED |
|---|---|---|
| 220 Om | ≈ 13,6 mA | yorqin |
| 330 Om | ≈ 9,1 mA | o'rtacha |
| 1000 Om | ≈ 3 mA | xira |

Qarshilik **oshsa — tok kamayadi — LED xiralashadi**. Bu uslubiy ko'rsatmadagi «rezistor qiymatini o'zgartirish orqali LED yorqinligi va tok oqimini o'rganish» tajribasi.

### 5. Nosozliklarni izlash: 6 qadam

Sxema ishlamasa, tokning yo'li bo'yicha **manbadan GND gacha** yuring:

1. **Manba:** multimetr bilan `+` va `−` relslar orasida 5 V bormi?
2. **Relslar:** sim to'g'ri relsga kirganmi (qizil `+`, ko'k `−`)? Katta breadboardda rels o'rtada uzilmaganmi?
3. **DIP switch:** ariqcha ustidami? Richag ON tomondami? Kontaktdan keyin 5 V chiqyaptimi?
4. **Rezistor:** ikki oyog'i turli qatorlarda? Qiymati to'g'rimi (rangli halqalar yoki Tinkercad xususiyati)?
5. **LED:** anod `+` tomonda? LED oyoqlarida ≈ 2 V bormi? Kuymaganmi?
6. **GND:** katod qatoridan GND relsga sim bormi?

Har qadamda «kutgan natija» bilan «o'lchangan natija» solishtiriladi — farq chiqqan joy xato joyi.

### 6. DIP switch va Arduino: holatni dastur o'qiydi

Mikrokontrollersiz kalit LEDni **to'g'ridan-to'g'ri** boshqaradi. Arduino bilan esa kalit **kirish signali**, LED esa **chiqish** bo'ladi va ular orasida **dastur** turadi.

Ulash (har bir kontakt uchun): bir oyoq → raqamli pin (2 yoki 3), qarama-qarshi oyoq → GND. Dasturda `INPUT_PULLUP`:
- richag **OFF** → kontakt ochiq → pin `HIGH`;
- richag **ON** → pin GND ga ulanadi → `LOW`.

Ikki kalit — **2 bit**: `kod = bit1 × 2 + bit0`, ya'ni 4 ta kombinatsiya (0–3). 8 pozitsiyali DIP switch esa 2⁸ = 256 ta qiymat beradi — shuning uchun routerlar va pultlarda manzil sozlash uchun ishlatiladi.

| DIP1 (bit1) | DIP2 (bit0) | kod | rejim |
|---|---|---|---|
| OFF | OFF | 0 | hammasi o'chiq |
| OFF | ON | 1 | Yashil yoniq |
| ON | OFF | 2 | Qizil yoniq |
| ON | ON | 3 | ikkalasi miltillaydi |

Keyingi bobda (13-dars) Arduino va Raspberry Pi kabi IoT qurilmalarini taqqoslaymiz — kirish va chiqishlarni dastur bilan boshqarish g'oyasi aynan shu yerdan boshlanadi.

---

## Amaliy mashg'ulot va topshiriqlar

### 1-topshiriq. «Ikki qo'l» xavfsizlik zanjiri — AND (oson)
DIP switch'ning ikki kontaktini ketma-ket ulang: LED faqat ikkala richag ON bo'lganda yonsin. Haqiqat jadvalini to'ldiring.

**Yechim:**
```
+5V (qizil rels) → DIP1 kirish
DIP1 chiqish → DIP2 kirish (bitta sim bilan)
DIP2 chiqish → 330 Om → LED anod
LED katod → GND (ko'k rels)
```
Jadval: OFF/OFF, ON/OFF, OFF/ON — o'chiq; ON/ON — yoniq. Bitta kalit OFF bo'lsa ham yo'l uziladi.

### 2-topshiriq. «Istalgan tugma» signali — OR (o'rta)
Endi ikki kontaktni parallel ulang: istalgan richag ON bo'lganda LED yonsin. Sxemani 1-topshiriqdan qanday o'zgartirish kerakligini tushuntiring.

**Yechim:**
```
+5V → DIP1 kirish   va   +5V → DIP2 kirish
DIP1 chiqish → umumiy qator X
DIP2 chiqish → umumiy qator X
qator X → 330 Om → LED anod → LED katod → GND
```
O'zgarish: DIP1 chiqishidan DIP2 kirishiga boradigan sim olib tashlanadi; ikkala kirish `+` ga, ikkala chiqish bitta qatorga ulanadi. Jadval: faqat OFF/OFF da o'chiq.

### 3-topshiriq. Rezistor tajribasi multimetr bilan (o'rta)
11-darsdagi bitta LED zanjirida rezistorni navbat bilan 220, 330 va 1000 Om ga almashtiring. Har safar Tinkercad multimetri bilan tokni (ketma-ket) va LED kuchlanishini (parallel) o'lchang, jadval tuzing va xulosa yozing.

**Yechim (taxminiy natijalar, Tinkercad'da biroz farq qilishi mumkin):**
| R | I (o'lchangan) | U_LED | Yorqinlik |
|---|---|---|---|
| 220 Om | ≈ 13–14 mA | ≈ 2,0 V | yorqin |
| 330 Om | ≈ 9 mA | ≈ 2,0 V | o'rtacha |
| 1000 Om | ≈ 3 mA | ≈ 1,9 V | xira |

Xulosa: LED kuchlanishi deyarli o'zgarmaydi, tok esa qarshilikka teskari proporsional — `I = (U − U_LED) / R`. Tok rejimida multimetr zanjirni uzib, rezistor va LED orasiga qo'yiladi.

### 4-topshiriq. DIP switch — Arduino rejim tanlagichi (qiyin)
DIP1 → Pin 2, DIP2 → Pin 3 (qarama-qarshi oyoqlar GND ga). Qizil LED — Pin 9, Yashil LED — Pin 10 (220 Om orqali GND). Yuqoridagi jadval bo'yicha 4 rejimni dasturlang; kod o'zgarganda Serial Monitor'ga `Kod: 2 -> Qizil` kabi yozuv chiqsin. Miltillash `millis()` bilan bo'lsin.

**Yechim:**
```cpp
const byte SW1 = 2;    // bit1
const byte SW2 = 3;    // bit0
const byte LED_R = 9;
const byte LED_G = 10;
const char* nomlar[] = {"O'chiq", "Yashil", "Qizil", "Miltillash"};

byte oldingiKod = 255;           // hali o'qilmagan
unsigned long lastBlink = 0;
bool blinkOn = false;

void setup() {
  pinMode(SW1, INPUT_PULLUP);
  pinMode(SW2, INPUT_PULLUP);
  pinMode(LED_R, OUTPUT);
  pinMode(LED_G, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  byte bit1 = (digitalRead(SW1) == LOW) ? 1 : 0;   // ON -> LOW -> 1
  byte bit0 = (digitalRead(SW2) == LOW) ? 1 : 0;
  byte kod = bit1 * 2 + bit0;

  if (kod != oldingiKod) {                         // faqat o'zgarganda
    oldingiKod = kod;
    Serial.print("Kod: ");
    Serial.print(kod);
    Serial.print(" -> ");
    Serial.println(nomlar[kod]);
  }

  switch (kod) {
    case 0: digitalWrite(LED_R, LOW);  digitalWrite(LED_G, LOW);  break;
    case 1: digitalWrite(LED_R, LOW);  digitalWrite(LED_G, HIGH); break;
    case 2: digitalWrite(LED_R, HIGH); digitalWrite(LED_G, LOW);  break;
    case 3:
      if (millis() - lastBlink >= 300) {
        lastBlink = millis();
        blinkOn = !blinkOn;
        digitalWrite(LED_R, blinkOn);
        digitalWrite(LED_G, !blinkOn);
      }
      break;
  }
}
```
DIP switch tugmadan farqli ravishda **holatini saqlaydi**, shuning uchun bu yerda Toggle va Debounce kerak emas — joriy holat to'g'ridan-to'g'ri o'qiladi.

---

## Tezkor nazorat savollari

1. Ikki kalit ketma-ket ulansa, LED qachon yonadi?
   - *Javob:* Faqat ikkala kalit ham yoqilganda (VA / AND mantiqi).
2. Parallel ulangan kalitlar qanday mantiqni beradi?
   - *Javob:* YOKI (OR): kamida bittasi yoqilsa LED yonadi.
3. Multimetr bilan tok qanday o'lchanadi?
   - *Javob:* Zanjir uziladi va multimetr (Current rejimi) ketma-ket ulanadi.
4. Rezistor 330 Om dan 1000 Om ga almashtirilsa, nima o'zgaradi?
   - *Javob:* Tok taxminan 3 marta kamayadi (≈ 9 mA dan ≈ 3 mA ga), LED xiralashadi.
5. `INPUT_PULLUP` bilan ulangan DIP switch ON bo'lganda pin nima o'qiydi?
   - *Javob:* `LOW`, chunki kontakt pinni GND ga ulaydi.
6. 4 pozitsiyali DIP switch nechta turli kombinatsiya beradi?
   - *Javob:* 2⁴ = 16 ta.

---

## Keng tarqalgan xatolar va ularning oldini olish

- **Parallel o'rniga ketma-ket (yoki aksincha):** o'quvchi DIP1 chiqishini DIP2 kirishiga ulab qo'yadi va OR o'rniga AND oladi. Tok yo'lini barmoq bilan «yurib» chiqishni so'rang.
- **Tok rejimidagi multimetrni parallel ulash:** qisqa tutashuv — Tinkercad'da manba ogohlantiradi, real qurilmada multimetr saqlagichi kuyadi. Tok — faqat ketma-ket.
- **Arduino'da ON = HIGH deb o'ylash:** `INPUT_PULLUP` da ON holat `LOW`. `== LOW ? 1 : 0` o'zgarishini tushuntiring.
- **Serial'ga har aylanishda yozish:** `oldingiKod` bilan solishtirmasdan yozilsa, monitor to'lib ketadi.
- **Arduino 5V ni to'g'ridan-to'g'ri DIP orqali pinga berish va pull-up yo'qligi:** kalit OFF bo'lganda pin «suzib» qoladi (8-dars). Kontaktni GND ga ulab, `INPUT_PULLUP` ishlating.
