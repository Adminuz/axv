---
title: "15-dars. 9-dars: Arduino UNO yordamida LED indikatorlari va push-button bilan interaktiv interfeys (2-qism)"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (IoT)", "link": "/9-sinf-iot/"}, "week": {"n": 3, "link": "/9-sinf-iot/hafta-03/"}, "g": 15, "title": "9-dars: Arduino UNO yordamida LED indikatorlari va push-button bilan interaktiv interfeys (2-qism)", "lead": "Mikrokontroller tushunchasi va IoT qurilmalaridagi o‘rni (1-qism)", "slide": "/slaydlar/9-sinf-iot/hafta-03/dars-9.html", "tabs": [{"g": 13, "link": "/9-sinf-iot/hafta-03/dars-7", "current": false}, {"g": 14, "link": "/9-sinf-iot/hafta-03/dars-8", "current": false}, {"g": 15, "link": "/9-sinf-iot/hafta-03/dars-9", "current": true}], "prev": {"g": 14, "title": "8-dars: Arduino UNO yordamida LED indikatorlari va push-button bilan ishlash (1-qism)", "link": "/9-sinf-iot/hafta-03/dars-8"}, "next": null}
---

**Fan:** Internet of Things (IoT — Buyumlar Interneti)  
**Sinf:** 9-sinf  
**Mavzu:** Interaktiv boshqaruv, Toggle mantig'i, kontakt dirillashi (Bounce & Debounce), ko'p tugmali tizimlar

---

<div class="blk">

## <Icon name="file-text" /> Darsning qisqacha mazmuni

Ushbu darsda biz interaktiv elektron boshqaruvning eng professional bosqichiga o'tamiz. Real hayotdagi ko'plab qurilmalarda (masalan, chiroq kaliti, konditsioner yoki xonadon domofoni) tugma ushlab turilmaydi, balki bitta qisqa bosish orqali rejimlar almashtiriladi. Dars davomida mexanik kontaktlarning dirillashi (Button Bounce) muammosini dasturiy yo'l bilan bartaraf etish (Debounce), Toggle effekti va bir nechta tugmalar orqali turli LEDlarni mustaqil boshqarishni o'rganamiz.

### Asosiy tushunchalar:
- **Toggle (Trigged / Kalit) effekti:** Tugma 1 marta bosilganda holat o'zgaradi va yoniq qoladi, yana 1 marta bosilganda esa o'chadi;
- **Kontaktlarning dirillashi (Button Bounce):** Tugma bosilganda metall qismlar 5–20 millisekund davomida mikroskopik sakrashi;
- **Debounce:** Tebranish davridagi soxta signallarni e'tiborga olmaslik uchun 30–50 ms lik dasturiy filtr qo'llash;
- **Holat o'zgarishini aniqlash (State Change):** `buttonState != lastButtonState` sharti orqali bosilish lahzasini tutish;
- **Mantiqiy inkor (NOT):** `ledState = !ledState` orqali 0 ni 1 ga, 1 ni 0 ga bir harakatda aylantirish;
- **Master Switch:** Bitta bosh tugma orqali barcha chiroqlarni birdaniga yoqish yoki o'chirish.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Mustaqil bajarish uchun topshiriqlar

### 1-topshiriq <Badge type="tip" text="oson" />
Tinkercad Circuits muhitida yangi loyiha oching va unga `9-sinf_Familiya_Dars9` deb nom bering. Ish maydoniga Arduino Uno, Breadboard, 1 ta Push-button va 1 ta Qizil LED (220 Om rezistor bilan) joylashtiring.

### 2-topshiriq <Badge type="tip" text="oson" />
Tugmani Arduino ning `D2` piniga va `GND` ga ulang. Qizil LED anodini 220 Om rezistor orqali `D9` piniga, katodini esa `GND` ga bog'lang.

### 3-topshiriq <Badge type="tip" text="oson" />
C++ dasturida global o'zgaruvchilarni e'lon qiling va `setup()` funksiyasini to'ldiring:
```cpp
const int btnPin = 2;
const int ledPin = 9;
int ledState = LOW;
int lastBtn = HIGH;

void setup() {
  pinMode(btnPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);
}
```

### 4-topshiriq <Badge type="tip" text="oson" />
Quyidagi Toggle dasturini `loop()` ichiga kiriting va simulyatsiyani ishga tushiring:
```cpp
void loop() {
  int reading = digitalRead(btnPin);
  if (reading != lastBtn && reading == LOW) {
    ledState = !ledState;
    digitalWrite(ledPin, ledState);
    delay(50);
  }
  lastBtn = reading;
}
```
Tugmani bitta bosib qo'yib yuboring. LED yoniq qolganini va yana bir marta bosganda o'chganini tekshiring.

### 5-topshiriq <Badge type="warning" text="o'rta" />
Dasturdagi `delay(50);` qatorini olib tashlang (izohga oling `//delay(50);`). Simulyatsiyani qayta ishga tushirib, tugmani tez-tez bosib ko'ring. Nima uchun ba'zi bosishlarda LED kutilmaganda yonmay yoki o'chmay qolganini daftaringizga yozing. So'ngra 50 ms kechikishni qaytaring.

### 6-topshiriq <Badge type="warning" text="o'rta" />
Sxemaga ikkinchi tugma (`D3` va `GND`) hamda ikkinchi Sariq LED (`D11` va 220 Om rezistor) qo'shing.
Har bir tugma o'ziga tegishli LEDni mustaqil ravishda Toggle qiladigan (1-tugma Qizilni, 2-tugma Sariqni) kodni tuzing.

### 7-topshiriq <Badge type="warning" text="o'rta" />
Ikki tugmali "Start/Stop" boshqaruvi dasturlang:
- 1-tugma (Start) bosilganda: Ikkala chiroq ham yonadi;
- 2-tugma (Stop) bosilganda: Ikkala chiroq ham o'chadi.

### 8-topshiriq <Badge type="warning" text="o'rta" />
Sxemaga uchinchi Yashil LED (`D10` va 220 Om rezistor) qo'shing. Bitta tugma yordamida "Rejimlar selektori" (Mode Selector) yasang:
- Boshlanishda barcha chiroqlar o'chiq;
- 1-bosish: Faqat Qizil yonadi;
- 2-bosish: Faqat Sariq yonadi;
- 3-bosish: Faqat Yashil yonadi;
- 4-bosish: Hammasi o'chadi va sikl qayta boshlanadi.

### 9-topshiriq <Badge type="danger" text="qiyin" />
Rasmiy uslubiy qo'llanmadagi kabi 3 ta tugma va 3 ta LED dan iborat tizim tuzing:
- 1-tugma: 1-LED holatini almashtiradi;
- 2-tugma: 1-LED va 2-LED holatlarini birgalikda almashtiradi;
- 3-tugma: 2-LED va 3-LED holatlarini birgalikda almashtiradi.

### 10-topshiriq <Badge type="danger" text="qiyin" />
Tizimga "Heartbeat" (tizim tirikligi indikatori) LEDini qo'shing (masalan, Arduino platasidagi o'rnatilgan 13-pin). Ushbu chiroq tugmalar bosilishidan qat'i nazar, fon rejimida har 1 soniyada uzluksiz miltillab tursin.

### 11-topshiriq <Badge type="info" text="bonus" />
"Aqlli xonadon koridori" loyihasi: Koridorning boshida va oxirida ikkita tugma bor. Istalgan tugma bosilganda koridor chirog'i (LED) yonsin, istalgan tugma yana bosilganda esa chiroq o'chsin (o'tkazgichli kross-kalit mantiqiy modeli).

</div>

