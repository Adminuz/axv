# 9-dars: Arduino UNO yordamida LED indikatorlari va push-button bilan interaktiv interfeys (2-qism)

**Fan:** Internet of Things (IoT — Buyumlar Interneti)  
**Sinf:** 9-sinf  
**Hafta:** 3-hafta, 3-dars (umumiy 9-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga bir nechta tugma va bir nechta LED dan iborat interaktiv tizimlarni loyihalash, tugma bosilishini aniqlash (holat o'zgarishi — State Change Detection), Toggle (trigged / kalit) mantig'i, mexanik kontaktlarning tebranishi (Bounce) muammosi va uni dasturiy bartaraf etish (Debounce) usullarini o'rgatish hamda Tinkercad-da to'liq interaktiv interfeysni simulyatsiya qilish ko'nikmalarini shakllantirish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- Oddiy bosib turish (Hold) bilan bosib qo'yib yuborish (Click / Toggle) o'rtasidagi farqni tushunish;
- Mexanik kontaktlarning dirillashi (Button Bounce) hodisasi nima ekanini va nima sababdan bir bosishda LED bir necha marta yonib-o'chib ketishini bilish;
- Dasturiy Debounce (kechikish orqali shovqinni tozalash) algoritmini qo'llay olish;
- Holat o'zgarishini aniqlash: `lastButtonState` o'zgaruvchisi yordamida tugma bosilgan lahzani (Transition) ushlash;
- `!digitalRead(ledPin)` orqali LED holatini bitta buyruq bilan teskarisiga o'zgartirish (Toggle);
- Bir nechta tugmalar va LED lar bilan ko'p funksiyali interaktiv interfeys dasturini yoza olish.

---

## Kerakli jihozlar va vositalar

- Kompyuter yoki noutbuk (internetga ulangan);
- Veb-brauzer orqali Tinkercad.com virtual laboratoriyasiga kirish;
- Proyektor yoki monitor (namoyish uchun).

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va o'tgan mavzuni takrorlash | `INPUT_PULLUP`, suzuvchi pin, `digitalRead()` bo'yicha blits-so'rov |
| **10–25 min** | Yangi mavzu: Toggle mantig'i va Kontakt dirillashi (Bounce) | Nega tugma bir marta bosilganda chiroq yoniq qolishi kerak? Kontaktlarning 10 ms tebranishi |
| **25–40 min** | Debounce va Holat o'zgarishini aniqlash algoritmi | `lastButtonState`, `millis()` yoki `delay(50)` yordamida tebranishni filtrlash |
| **40–60 min** | Amaliy laboratoriya: Toggle tugma va 2 ta LED | 2 ta tugma va 2 ta LED sxemasi: 1-tugma Qizil LEDni o'zgartiradi, 2-tugma ikkala LEDni boshqaradi |
| **60–75 min** | Mustaqil amaliy topshiriqlar | 3-tugma qo'shish va rejimlar (Modes) o'rtasida almashinuvchi menyu interfeysi |
| **75–80 min** | Xulosa va uyga vazifa | Mavzuni umumlashtirish, baholash mezonlari |

---

## Nazariy ma'lumotlar

### 1. Toggle (Trigged) mantig'i nima?

8-darsda biz ko'rgan oddiy boshqaruvda LED faqat tugma **bosib turilgan vaqtdagina** yonib turardi (xuddi xonadon qo'ng'irog'i kabi).
Biroq xona chiroqlari yoki televizor pulti boshqacha ishlaydi:
- Tugma 1 marta bosilib qo'yib yuboriladi -> Chiroq **yonadi va yoniq qoladi**;
- Tugma yana 1 marta bosilib qo'yib yuboriladi -> Chiroq **o'chadi va o'chiq qoladi**.

Bu rejim elektronikada **Toggle** (holatni almashtirish) deb ataladi. Buning uchun mikrokontroller doimiy ravishda emas, aynan **tugma bosilgan lahzani (o'tish jarayonini)** ushlashi kerak.

### 2. Kontaktlarning dirillashi (Button Bouncing) muammosi

Inson ko'ziga tugma bir marta silliq bosilgandek ko'rinadi. Lekin mikroskopik darajada tugma ichidagi metall kontaktlar bir-biriga urilganda elastiklik sababli **5–20 millisekund davomida bir necha bor sakraydi (dirillaydi)**.
- Mikrokontroller sekundiga 16 million amal bajargani sababli, ushbu 10 ms ichida 20–30 marta 0 va 1 signallarini o'qib ulguradi!
- Natijada Toggle dasturi bitta bosishni 5 marta bosildi deb qabul qilib, LED tasodifiy holatda qolib ketadi.

**Yechim (Debounce):**
Tugma bosilgani aniqlangach, dasturda 50 millisekundlik kichik pauza beriladi yoki tebranish to'xtaguncha yangi signallar e'tiborga olinmaydi.

### 3. Holat o'zgarishini aniqlash (State Change Detection)

Tugmaning joriy holati (`buttonState`) avvalgi holati (`lastButtonState`) bilan solishtiriladi:
```cpp
int buttonState = digitalRead(buttonPin);

// Agar holat o'zgargan bo'lsa VA yangi holat LOW bo'lsa (ya'ni endi bosildi):
if (buttonState != lastButtonState && buttonState == LOW) {
  ledState = !ledState;              // LED holatini teskarisiga aylantirish
  digitalWrite(ledPin, ledState);
  delay(50);                         // Debounce kechikishi
}

lastButtonState = buttonState;       // Yangi holatni eslab qolish
```

---

## Amaliy mashg'ulot va topshiriqlar

### 1-topshiriq. 1 ta tugma bilan LEDni Toggle qilish (oson)
Tinkercad Circuits ish maydonida Arduino Uno, 1 ta Push-button (Pin 2 va GND) va 1 ta LED (Pin 9 va GND) ulang.
Tugma har bosilganda LED o'z holatini o'zgartirsin (yoniq bo'lsa o'chsin, o'chiq bo'lsa yonsin).

**Yechim:**
```cpp
const int buttonPin = 2;
const int ledPin = 9;

int ledState = LOW;
int lastButtonState = HIGH;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, ledState);
}

void loop() {
  int reading = digitalRead(buttonPin);

  if (reading != lastButtonState && reading == LOW) {
    ledState = !ledState;
    digitalWrite(ledPin, ledState);
    delay(50); // Debounce
  }

  lastButtonState = reading;
}
```

### 2-topshiriq. Ikki tugmali mustaqil boshqaruv (o'rta)
Sxemaga ikkinchi tugma (Pin 3 va GND) va ikkinchi Sariq LED (Pin 11 va GND) qo'shing:
- 1-tugma (Pin 2) bosilganda: Qizil LED o'zgaradi (Toggle);
- 2-tugma (Pin 3) bosilganda: Sariq LED o'zgaradi (Toggle).
Ikkala chiroq bir-biriga xalaqit bermasdan mustaqil boshqarilishi kerak.

**Yechim:**
```cpp
const int btn1 = 2;
const int btn2 = 3;
const int ledRed = 9;
const int ledYellow = 11;

int stateRed = LOW;
int stateYellow = LOW;
int lastBtn1 = HIGH;
int lastBtn2 = HIGH;

void setup() {
  pinMode(btn1, INPUT_PULLUP);
  pinMode(btn2, INPUT_PULLUP);
  pinMode(ledRed, OUTPUT);
  pinMode(ledYellow, OUTPUT);
}

void loop() {
  int r1 = digitalRead(btn1);
  if (r1 != lastBtn1 && r1 == LOW) {
    stateRed = !stateRed;
    digitalWrite(ledRed, stateRed);
    delay(50);
  }
  lastBtn1 = r1;

  int r2 = digitalRead(btn2);
  if (r2 != lastBtn2 && r2 == LOW) {
    stateYellow = !stateYellow;
    digitalWrite(ledYellow, stateYellow);
    delay(50);
  }
  lastBtn2 = r2;
}
```

### 3-topshiriq. Aqlli Master Switch (Bosh kalit) tizimi (qiyin)
Sxemaga uchinchi tugma (Pin 4) qo'shing:
- 1-tugma: Faqat Qizil LEDni yoqadi/o'chiradi;
- 2-tugma: Faqat Sariq LEDni yoqadi/o'chiradi;
- 3-tugma (Master Switch): Bitta bosishda ikkala LEDni ham bir vaqtda yoqadi; ikkinchi marta bosilganda ikkala LEDni ham bir vaqtda o'chiradi.

**Yechim:**
Rasmiy uslubiy qo'llanmadagi kabi har bir tugmaning holati tekshiriladi va uchinchi tugma bosilganda ikkala chiroq holati sinxron o'zgartiriladi:
```cpp
const int btn3 = 4;
int lastBtn3 = HIGH;
// loop ichida:
int r3 = digitalRead(btn3);
if (r3 != lastBtn3 && r3 == LOW) {
  // Agar kamida bittasi yoniq bo'lsa - ikkalasini o'chiramiz, aks holda yoqamiz
  if (stateRed == HIGH || stateYellow == HIGH) {
    stateRed = LOW;
    stateYellow = LOW;
  } else {
    stateRed = HIGH;
    stateYellow = HIGH;
  }
  digitalWrite(ledRed, stateRed);
  digitalWrite(ledYellow, stateYellow);
  delay(50);
}
lastBtn3 = r3;
```

---

## Tezkor nazorat savollari

1. Oddiy bosib turish (Hold) bilan Toggle boshqaruvi o'rtasidagi asosiy farq nimada?
   - *Javob:* Hold rejimida detal faqat tugma ushlab turilganda ishlaydi; Toggle rejimida esa tugma bir marta bosib qo'yib yuborilganda holat saqlanib qoladi.
2. Tugma kontaktlarining tebranishi (Button Bounce) hodisasi nima sababdan yuzaga keladi?
   - *Javob:* Tugma ichidagi metall plastinkaning mexanik elastikligi tufayli bir-biriga urilganda 5–20 ms ichida bir necha bor sakrab tutashishi sababli.
3. Nima uchun Toggle dasturida `delay(50)` qo'yiladi?
   - *Javob:* Mexanik dirillash (bouncing) paytida hosil bo'ladigan soxta impulslarni e'tiborga olmaslik (Debounce qilish) uchun.
4. `ledState = !ledState;` amali qanday vazifani bajaradi?
   - *Javob:* Mantiqiy inkor (NOT) amali: agar o'zgaruvchi HIGH bo'lsa LOW qiladi, agar LOW bo'lsa HIGH qiladi.

---

## Keng tarqalgan xatolar va ularning oldini olish

- **Holat o'zgarishini emas, doimiy holatni tekshirish:** Agar o'quvchi `if (buttonState == LOW)` deb yozsa va `lastButtonState` bilan solishtirmasa, tugma bosib turilgan yarim soniya ichida tsikl yuzlab marta aylanib, LED telbalarcha miltillab qoladi. Har doim avvalgi holat bilan solishtirish shart.
- **Debounce kechikishini haddan tashqari katta qilish:** Agar `delay(500)` yoki `delay(1000)` qo'yilsa, tizim "qotib qolgan"dek taassurot qoldiradi va tez-tez bosilganda buyruqlarni o'tkazib yuboradi. Optimal kechikish 30–50 ms atrofida bo'lishi lozim.
