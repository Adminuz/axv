# 10-dars: Arduino UNO va tugma orqali LED holatini boshqarish dasturi

**Fan:** Internet of Things (IoT — Buyumlar Interneti)  
**Sinf:** 9-sinf  
**Hafta:** 4-hafta, 1-dars (umumiy 10-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga 8–9-darslarda o'rganilgan push-button, `INPUT_PULLUP`, Toggle va Debounce bilimlarini yaxlit, tartibli **LED holatini boshqarish dasturi**ga birlashtirishni o'rgatish: `#define` va `const byte` bilan o'qiluvchan kod, yordamchi funksiya (`checkSwitch`), `delay()` o'rniga `millis()` asosidagi bloklamaydigan dastur, «heartbeat» indikator LED, bitta tugma bilan bir nechta **rejim** (holat mashinasi, `switch/case`) va holatni Serial Monitor'ga chiqarish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- LED **holati** (state) tushunchasini va uni o'zgaruvchida saqlashni tushuntira olish;
- `#define Pressed LOW` kabi nomlangan konstantalar dasturni nima uchun o'qiluvchan qilishini bilish;
- Tugmani tekshiruvchi yordamchi funksiya yoza olish va `&` (havola orqali uzatish) ma'nosini tushunish;
- `delay()` dasturni «muzlatishini» va `millis()` bilan bir vaqtda bir nechta ishni bajarishni ko'rsata olish;
- Bitta tugma bilan 4 rejimli (O'CHIQ → YONIQ → SEKIN → TEZ) boshqaruvni `switch/case` bilan dasturlay olish;
- Uslubiy qo'llanmadagi 3 tugma + 3 LED + heartbeat LED dasturini o'qib, tahlil qila olish.

---

## Kerakli jihozlar va vositalar

- Kompyuter yoki noutbuk (internetga ulangan);
- Tinkercad.com (Circuits) yoki real to'plam: Arduino UNO, breadboard, 1–3 ta push-button, 1–4 ta LED, 220–330 Om rezistorlar, ulash simlari;
- Arduino IDE (real plata bilan ishlaganda);
- Proyektor yoki monitor (namoyish uchun).

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Takrorlash | `INPUT_PULLUP` (bosilganda `LOW`), Toggle, `lastButtonState`, Debounce bo'yicha blits-so'rov |
| **10–25 min** | Yangi mavzu: holat va dastur tuzilishi | LED holati, `#define`, `const byte`, yordamchi funksiya `checkSwitch()` |
| **25–40 min** | `delay()` muammosi va `millis()` | Bloklamaydigan dastur, heartbeat LED, 50 ms so'rov oralig'i |
| **40–60 min** | Amaliy laboratoriya: 4 rejimli chiroq | Bitta tugma, `mode` o'zgaruvchisi, `switch/case`, Serial Monitor |
| **60–75 min** | Mustaqil topshiriqlar | Uslubiy qo'llanmadagi 3 tugmali sxema va uni o'zgartirish |
| **75–80 min** | Xulosa va uyga vazifa | Mavzuni umumlashtirish, baholash mezonlari |

> Manba: o'quv dasturi — «Arduino UNO yordamida LED indikatorlari va push-button bilan interaktiv interfeys yaratish» (raqamli kirish va chiqish, shart operatorlari, tugma bosilganda LEDni boshqaruvchi kod); uslubiy ko'rsatma — 3 ta push-button, 3 ta LED va heartbeat LED dasturi, `millis()`, `INPUT_PULLUP`; o'quv qo'llanma — `setup()`/`loop()`, `delay()` va `millis()` farqi.

---

## Nazariy ma'lumotlar

### 1. LED holati (state) nima?

**Holat** — qurilmaning ayni paytdagi «vaziyati»: LED yoniq yoki o'chiq, rejim 0 yoki 3. Holat o'zgaruvchida saqlanadi va faqat **hodisa** (masalan, tugma bosilgan lahza) sodir bo'lganda o'zgaradi.

| Tushuncha | Misol | Qachon o'zgaradi |
|---|---|---|
| Kirish (input) | tugma — `digitalRead(2)` | foydalanuvchi bosganda |
| Hodisa (event) | `HIGH → LOW` o'tishi | bir marta, bosilgan lahzada |
| Holat (state) | `ledState`, `mode` | hodisaga javoban |
| Chiqish (output) | LED — `digitalWrite(9, ...)` | holatga qarab |

Eslatma: `INPUT_PULLUP` rejimida tugma **bosilmaganda `HIGH`**, **bosilganda `LOW`** o'qiladi (8-dars).

### 2. O'qiluvchan kod: `#define` va `const byte`

Uslubiy qo'llanmadagi dastur «sehrli sonlar» o'rniga nomlardan foydalanadi:

```cpp
#define Pressed  LOW    // tugma bosilgan
#define Released HIGH   // tugma qo'yib yuborilgan

const byte switchOne = 7;   // 1-tugma pini
const byte LED_One   = 10;  // 1-LED pini
```

- `#define` — kompilyatsiyadan oldin nomni qiymat bilan almashtiradi: `if (holat == Pressed)` o'qish `if (holat == LOW)` dan oson.
- `const byte` — o'zgarmas pin raqami; `byte` 0–255 oralig'idagi son uchun 1 bayt joy oladi (`int` — 2 bayt). Arduino UNO'da atigi 2 KB SRAM bor (o'quv qo'llanma).

> Uslubiy qo'llanmada `#define LEDon LOW` yozilgan: bu LED **5V dan pin tomonga** ulangan (active-LOW) sxema uchun. Bizning sxemada LED pin → rezistor → GND ulanadi, shuning uchun yoqish — `HIGH`.

### 3. Yordamchi funksiya: `checkSwitch()`

Har bir tugma uchun bir xil kodni takrorlamaslik uchun uni funksiyaga chiqaramiz:

```cpp
bool checkSwitch(byte pin, byte &lastState) {
  byte current = digitalRead(pin);
  if (current != lastState) {       // holat o'zgardimi?
    lastState = current;            // yangi holatni eslab qolamiz
    if (current == Pressed) {
      return true;                  // aynan hozir bosildi
    }
  }
  return false;
}
```

- `byte &lastState` — **havola** (reference): funksiya o'zgaruvchining nusxasini emas, **o'zini** o'zgartiradi. `&` bo'lmasa, `lastState = current` funksiyadan chiqqach unutiladi va tugma har safar «yangi bosildi» deb qabul qilinadi.
- Funksiya `true` faqat bosilgan **lahzada** qaytaradi — Toggle uchun aynan shu kerak.

### 4. `delay()` muammosi va `millis()`

`delay(500)` paytida Arduino **hech narsa qilmaydi**: tugma bosilsa ham sezmaydi. Ikki ish (miltillash + tugmani kuzatish) bir vaqtda kerak bo'lsa, `millis()` ishlatiladi.

`millis()` — plata yoqilgandan beri o'tgan millisekundlar (`unsigned long`). Qoida:

```cpp
unsigned long oxirgiVaqt = 0;
const unsigned long INTERVAL = 700;

void loop() {
  if (millis() - oxirgiVaqt >= INTERVAL) {   // 700 ms o'tdimi?
    oxirgiVaqt = millis();
    digitalWrite(13, !digitalRead(13));      // heartbeat LED ni almashtirish
  }
  // bu yerda boshqa ishlar to'xtovsiz bajariladi
}
```

**Heartbeat LED** (uslubiy qo'llanma, 13-pin, 700 ms) — dastur «tirikligi» belgisi: u bir tekis miltillab tursa, `loop()` qotib qolmagan.

**Debounce `millis()` bilan:** tugmalar har **50 ms** da bir marta tekshiriladi. Kontakt dirillashi 5–20 ms davom etgani uchun 50 ms oralig'idagi so'rov soxta impulslarni o'tkazib yuboradi va `delay()` kerak bo'lmaydi.

### 5. Rejimlar: bitta tugma — bir nechta holat

Ko'p qurilmalarda (fonar, ventilyator) bitta tugma rejimlarni aylantiradi. Buning uchun **hisoblagich** va `switch/case` ishlatiladi:

```cpp
mode = (mode + 1) % 4;   // 0 → 1 → 2 → 3 → 0 ...
```

| `mode` | Nomi | LED |
|---|---|---|
| 0 | O'CHIQ | doim o'chiq |
| 1 | YONIQ | doim yoniq |
| 2 | SEKIN | 500 ms da almashadi |
| 3 | TEZ | 100 ms da almashadi |

`%` — bo'linmaning qoldig'i: `4 % 4 = 0`, shuning uchun 3 dan keyin yana 0 ga qaytadi. Bu oddiy **holat mashinasi** (state machine).

### 6. Holatni Serial Monitor'ga chiqarish

```cpp
Serial.begin(9600);                 // setup() ichida
Serial.print("Rejim: ");
Serial.println(mode);               // faqat o'zgarganda chiqaring!
```

Xabarni `loop()` ning har aylanishida emas, faqat **holat o'zgarganda** chiqaring — aks holda monitor sekundiga minglab qator bilan to'lib ketadi.

### 7. Uslubiy qo'llanmadagi dastur tahlili (3 tugma, 3 LED, heartbeat)

| Element | Pin | Vazifa |
|---|---|---|
| `switchOne` | 7 | LED_One ni almashtiradi |
| `switchTwo` | 8 | LED_One va LED_Two ni almashtiradi |
| `switchThree` | 9 | LED_Two va LED_Three ni almashtiradi |
| `LED_One/Two/Three` | 10/11/12 | holat indikatorlari |
| `heartBeatLED` | 13 | har 700 ms da miltillaydi |

`loop()` ichida avval `heartBeat()` chaqiriladi, so'ng vaqt oralig'i o'tgan bo'lsa, uchala tugma `checkSwitch()` bilan tekshiriladi. `digitalWrite(LED, !digitalRead(LED))` — LED ning hozirgi holatini o'qib, teskarisini yozadi.

---

## Amaliy mashg'ulot va topshiriqlar

### 1-topshiriq. Bitta tugma — ikki LED almashib yonadi (oson)
Tinkercad'da Arduino UNO, tugma (Pin 2 va GND), Qizil LED (Pin 9) va Yashil LED (Pin 10) ni 220 Om rezistorlar orqali ulang. Boshida Qizil yoniq. Har bosishda yonib turgan LED o'chib, ikkinchisi yonsin (uslubiy qo'llanmadagi «navbat bilan yoqish» topshirig'i).

**Yechim:**
```cpp
#define Pressed LOW
const byte BTN = 2;
const byte LED_R = 9;
const byte LED_G = 10;

byte lastBtn = HIGH;
bool qizilYoniq = true;
unsigned long lastCheck = 0;

void setup() {
  pinMode(BTN, INPUT_PULLUP);
  pinMode(LED_R, OUTPUT);
  pinMode(LED_G, OUTPUT);
  digitalWrite(LED_R, HIGH);
  digitalWrite(LED_G, LOW);
}

void loop() {
  if (millis() - lastCheck >= 50) {          // 50 ms da bir tekshiruv (debounce)
    lastCheck = millis();
    byte now = digitalRead(BTN);
    if (now != lastBtn) {
      lastBtn = now;
      if (now == Pressed) {
        qizilYoniq = !qizilYoniq;
        digitalWrite(LED_R, qizilYoniq ? HIGH : LOW);
        digitalWrite(LED_G, qizilYoniq ? LOW : HIGH);
      }
    }
  }
}
```

### 2-topshiriq. To'rt rejimli chiroq va Serial Monitor (o'rta)
Bitta tugma (Pin 2) va bitta LED (Pin 9). Har bosishda rejim almashsin: O'CHIQ → YONIQ → SEKIN (500 ms) → TEZ (100 ms) → O'CHIQ. Rejim o'zgarganda Serial Monitor'ga `Rejim: SEKIN` kabi yozuv chiqsin. Miltillash paytida ham tugma darhol sezilsin (`delay()` ishlatmang).

**Yechim:**
```cpp
const byte BTN = 2;
const byte LED = 9;
const char* nomlar[] = {"O'CHIQ", "YONIQ", "SEKIN", "TEZ"};

byte mode = 0;
byte lastBtn = HIGH;
bool ledOn = false;
unsigned long lastCheck = 0;
unsigned long lastBlink = 0;

void setup() {
  pinMode(BTN, INPUT_PULLUP);
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
  Serial.println("Rejim: O'CHIQ");
}

void miltilla(unsigned long oraliq) {
  if (millis() - lastBlink >= oraliq) {
    lastBlink = millis();
    ledOn = !ledOn;
    digitalWrite(LED, ledOn);
  }
}

void loop() {
  if (millis() - lastCheck >= 50) {
    lastCheck = millis();
    byte now = digitalRead(BTN);
    if (now != lastBtn) {
      lastBtn = now;
      if (now == LOW) {
        mode = (mode + 1) % 4;
        Serial.print("Rejim: ");
        Serial.println(nomlar[mode]);
      }
    }
  }

  switch (mode) {
    case 0: digitalWrite(LED, LOW);  break;
    case 1: digitalWrite(LED, HIGH); break;
    case 2: miltilla(500);           break;
    case 3: miltilla(100);           break;
  }
}
```

### 3-topshiriq. Heartbeat va Toggle birga (o'rta)
Pin 13 dagi LED har 700 ms da miltillab tursin (heartbeat), shu bilan birga tugma (Pin 2) Pin 9 dagi LED ni Toggle qilsin. `checkSwitch()` funksiyasidan foydalaning. Nega `delay(700)` bilan bu ishlamasligini tushuntiring.

**Yechim:**
```cpp
#define Pressed LOW
const byte BTN = 2, LED = 9, HB = 13;
byte lastBtn = HIGH;
unsigned long hbMillis = 0, swMillis = 0;

bool checkSwitch(byte pin, byte &lastState) {
  byte current = digitalRead(pin);
  if (current != lastState) {
    lastState = current;
    if (current == Pressed) return true;
  }
  return false;
}

void setup() {
  pinMode(BTN, INPUT_PULLUP);
  pinMode(LED, OUTPUT);
  pinMode(HB, OUTPUT);
}

void loop() {
  if (millis() - hbMillis >= 700) {
    hbMillis = millis();
    digitalWrite(HB, !digitalRead(HB));
  }
  if (millis() - swMillis >= 50) {
    swMillis = millis();
    if (checkSwitch(BTN, lastBtn)) {
      digitalWrite(LED, !digitalRead(LED));
    }
  }
}
```
`delay(700)` paytida `loop()` to'xtaydi: shu 0,7 soniya ichida bosilgan tugma o'qilmaydi va bosish «yo'qoladi».

### 4-topshiriq. Uslubiy qo'llanma sxemasini kengaytirish (qiyin)
Uslubiy qo'llanmadagi 3 tugma (7, 8, 9) va 3 LED (10, 11, 12) + heartbeat (13) sxemasini yig'ing. Dasturni shunday o'zgartiring: 3-tugma (Pin 9) **hamma LEDni o'chirsin** («Reset»), har bir o'zgarishdan keyin Serial Monitor'ga uchala LED holati `LED: 1 0 1` ko'rinishida chiqsin.

**Yechim:**
```cpp
#define Pressed LOW
const byte SW[3]  = {7, 8, 9};
const byte LEDS[3] = {10, 11, 12};
const byte HB = 13;
byte lastSw[3] = {HIGH, HIGH, HIGH};
unsigned long hbMillis = 0, swMillis = 0;

bool checkSwitch(byte pin, byte &lastState) {
  byte current = digitalRead(pin);
  if (current != lastState) {
    lastState = current;
    if (current == Pressed) return true;
  }
  return false;
}

void holatniChiqar() {
  Serial.print("LED: ");
  for (byte i = 0; i < 3; i++) {
    Serial.print(digitalRead(LEDS[i]));
    Serial.print(" ");
  }
  Serial.println();
}

void setup() {
  Serial.begin(9600);
  for (byte i = 0; i < 3; i++) {
    pinMode(SW[i], INPUT_PULLUP);
    pinMode(LEDS[i], OUTPUT);
  }
  pinMode(HB, OUTPUT);
}

void loop() {
  if (millis() - hbMillis >= 700) {
    hbMillis = millis();
    digitalWrite(HB, !digitalRead(HB));
  }
  if (millis() - swMillis >= 50) {
    swMillis = millis();
    if (checkSwitch(SW[0], lastSw[0])) {
      digitalWrite(LEDS[0], !digitalRead(LEDS[0]));
      holatniChiqar();
    }
    if (checkSwitch(SW[1], lastSw[1])) {
      digitalWrite(LEDS[0], !digitalRead(LEDS[0]));
      digitalWrite(LEDS[1], !digitalRead(LEDS[1]));
      holatniChiqar();
    }
    if (checkSwitch(SW[2], lastSw[2])) {       // Reset
      for (byte i = 0; i < 3; i++) digitalWrite(LEDS[i], LOW);
      holatniChiqar();
    }
  }
}
```
Massivlar (`SW[3]`, `LEDS[3]`) va `for` sikli bir xil kodni uch marta yozishdan qutqaradi.

---

## Tezkor nazorat savollari

1. LED holati (state) va tugma kirishi o'rtasidagi farq nima?
   - *Javob:* Kirish — tugmaning ayni paytdagi signali; holat — o'zgaruvchida saqlanadigan natija (LED yoniq/o'chiq, rejim) va u faqat hodisa (bosilgan lahza) bo'lganda o'zgaradi.
2. `bool checkSwitch(byte pin, byte &lastState)` da `&` nima uchun kerak?
   - *Javob:* O'zgaruvchi havola orqali uzatiladi: funksiya asl `lastState` ni yangilaydi, nusxani emas.
3. Nega miltillovchi dasturda `delay()` o'rniga `millis()` ishlatiladi?
   - *Javob:* `delay()` dasturni to'xtatadi va shu vaqtda tugma bosilishi sezilmaydi; `millis()` vaqtni tekshiradi, lekin `loop()` ni bloklamaydi.
4. `mode = (mode + 1) % 4;` qanday ishlaydi?
   - *Javob:* Rejimni 1 ga oshiradi; 4 ga yetganda bo'linma qoldig'i 0 bo'lgani uchun yana 0 dan boshlanadi: 0, 1, 2, 3, 0...
5. Heartbeat LED nimani bildiradi?
   - *Javob:* Dastur ishlab turganini: u bir tekis miltillasa, `loop()` qotib qolmagan.

---

## Keng tarqalgan xatolar va ularning oldini olish

- **`&` siz funksiya:** `byte lastState` (havolasiz) yozilsa, holat saqlanmaydi va tugma bosib turilganda LED to'xtovsiz almashadi. Funksiya imzosini tekshiring.
- **`millis()` ni `int` ga saqlash:** `int` 32 767 dan oshganda manfiy bo'ladi (taxminan 33 soniyada). Vaqt o'zgaruvchilari doim `unsigned long`.
- **Serial'ga har aylanishda yozish:** Monitor to'lib, dastur sekinlashadi. Faqat holat o'zgarganda chiqaring.
- **`mode` chegarasini unutish:** `mode++` dan keyin `% 4` yoki `if (mode > 3) mode = 0;` bo'lmasa, `switch` hech bir `case` ga tushmaydi va LED «qotib» qoladi.
- **Active-LOW sxemani aralashtirish:** uslubiy koddagi `LEDon LOW` ni pin → rezistor → GND sxemasida ishlatsangiz, LED teskari ishlaydi. Sxemaga mos `HIGH`/`LOW` tanlang.
