---
title: "14-dars. 8-dars: Arduino UNO yordamida LED indikatorlari va push-button bilan ishlash (1-qism)"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (IoT)", "link": "/9-sinf-iot/"}, "week": {"n": 3, "link": "/9-sinf-iot/hafta-03/"}, "g": 14, "title": "8-dars: Arduino UNO yordamida LED indikatorlari va push-button bilan ishlash (1-qism)", "lead": "IoT uchun asosiy qurilmalar: ESP8266 va ESP32 imkoniyatlari", "slide": "/slaydlar/9-sinf-iot/hafta-03/dars-8.html", "tabs": [{"g": 13, "link": "/9-sinf-iot/hafta-03/dars-7", "current": false}, {"g": 14, "link": "/9-sinf-iot/hafta-03/dars-8", "current": true}, {"g": 15, "link": "/9-sinf-iot/hafta-03/dars-9", "current": false}], "prev": {"g": 13, "title": "7-dars: Elektron sxema asosida ikki LED lampaning ishlash prinsipi va ulanishi", "link": "/9-sinf-iot/hafta-03/dars-7"}, "next": {"g": 15, "title": "9-dars: Arduino UNO yordamida LED indikatorlari va push-button bilan interaktiv interfeys (2-qism)", "link": "/9-sinf-iot/hafta-03/dars-9"}}
---

**Fan:** Internet of Things (IoT — Buyumlar Interneti)  
**Sinf:** 9-sinf  
**Mavzu:** Raqamli kirish (Digital Input), Push-button mexanikasi, Suzuvchi pin, INPUT_PULLUP va Serial Monitor

---

<div class="blk">

## <Icon name="file-text" /> Darsning qisqacha mazmuni

Hozirgacha biz Arduino orqali faqat tashqi qurilmalarga signal yuborishni (chiqish — OUTPUT) o'rgandik. Bugungi darsdan boshlab Arduino tashqi dunyodan ma'lumot qabul qilishni (kirish — INPUT) boshlaydi. Buning uchun eng keng tarqalgan boshqaruv elementi — Push-button (bosiluvchi tugma)dan foydalanamiz. Dars davomida tugmani to'g'ri ulash, "suzuvchi pin" muammosi va kompyuter ekranida ma'lumotlarni ko'rish (Serial Monitor) bilan tanishamiz.

### Asosiy tushunchalar:
- **Raqamli kirish (Digital Input):** Mikrokontroller piniga kelayotgan kuchlanishni 0V (LOW) yoki 5V (HIGH) deb o'qish;
- **Push-button (Tugma):** Bosilganda kontaktlarni birlashtiruvchi, qo'yib yuborilganda uzuvchi kirish asbobi;
- **Suzuvchi pin (Floating pin):** Havoda osilib qolgan pin tasodifiy xatoliklarni o'qishi;
- **INPUT_PULLUP:** Arduino ning o'rnatilgan ichki 20–50 kOm tortuvchi rezistori. Tugma bosilganda 0, bo'sh turganda 1 beradi;
- **`digitalRead(pin)`:** Pin holatini (HIGH yoki LOW) o'qib beruvchi buyruq;
- **Serial Monitor:** USB port orqali kompyuterga ma'lumot uzatish va ekranda ko'rish vositasi (`Serial.begin(9600)` va `Serial.println()`).

---

</div>

<div class="blk">

## <Icon name="file-text" /> Mustaqil bajarish uchun topshiriqlar

### 1-topshiriq <Badge type="tip" text="oson" />
Tinkercad Circuits-da yangi loyiha oching va unga `9-sinf_Familiya_Dars8` deb nom bering. Ish maydoniga Arduino Uno, kichik Breadboard va 1 ta Push-button qo'ying.

### 2-topshiriq <Badge type="tip" text="oson" />
Push-buttonni breadboardning markaziy ariqchasi ustiga joylashtiring. Uning chap yuqori oyog'ini (Terminal 1a) Arduino ning `D2` piniga, o'ng yuqori oyog'ini (Terminal 2a) esa Arduino ning `GND` piniga ulang.

### 3-topshiriq <Badge type="tip" text="oson" />
Code panelida matnli C++ rejimiga o'ting va `setup()` funksiyasida 2-pinni ichki tortuvchi rezistor bilan sozlang hamda Serial portni oching:
```cpp
pinMode(2, INPUT_PULLUP);
Serial.begin(9600);
```

### 4-topshiriq <Badge type="tip" text="oson" />
`loop()` funksiyasi ichida `digitalRead(2)` natijasini o'zgaruvchiga saqlang va Serial Monitor oynasiga chop eting:
```cpp
int holat = digitalRead(2);
Serial.println(holat);
delay(200);
```
"Start Simulation" bosib, pastdagi "Serial Monitor" tugmasini bosing.

### 5-topshiriq <Badge type="warning" text="o'rta" />
Serial Monitor oynasida chiqayotgan qiymatlarni kuzating:
1. Tugma bosilmaganda qaysi raqam chiqmoqda?
2. Sichqoncha bilan tugmani bosib turganda qaysi raqam chiqmoqda?
Ushbu natijalarni daftaringizga qayd eting.

### 6-topshiriq <Badge type="warning" text="o'rta" />
Sxemaga bitta Qizil LED va 220 Om rezistor qo'shing (anodini Arduino `D9` piniga, katodini `GND` ga ulang). `setup()` ichida `pinMode(9, OUTPUT);` qatorini qo'shing.

### 7-topshiriq <Badge type="warning" text="o'rta" />
Dasturga shartli operator (`if-else`) qo'shing:
- Agar tugma bosilsa (`holat == 0`), 9-pindagi LED yonsin;
- Agar tugma bo'sh bo'lsa (`holat == 1`), LED o'chsin.
Simulyatsiyada tugmani bosib, LED ning bir zumda yonishini sinab ko'ring.

### 8-topshiriq <Badge type="warning" text="o'rta" />
`INPUT_PULLUP` o'rniga oddiy `INPUT` yozib ko'ring (`pinMode(2, INPUT)`). Tugmani bosmasdan simulyatsiyani kuzating. Nima sababdan Serial Monitor ko'rsatkichlari beqaror bo'lib qolganini tushuntiring. So'ngra kodni yana `INPUT_PULLUP` ga qaytaring.

### 9-topshiriq <Badge type="danger" text="qiyin" />
Dasturga hisoblagich (Counter) qo'shing: har safar tugma bosilganda Serial Monitorga "Tugma bosildi: 1 marta", "Tugma bosildi: 2 marta" deb o'sib boruvchi sonni chiqaring.

### 10-topshiriq <Badge type="danger" text="qiyin" />
Teskari mantiq (Inverted Logic) dasturlang: LED doimiy yonib tursin, ammo tugma bosilgan paytda 1 soniyaga o'chib, yana yonsin.

### 11-topshiriq <Badge type="info" text="bonus" />
Zanjirga ikkinchi Sariq LED (Pin 11) qo'shing. Shunday mantiq tuzingki:
- Tugma bo'sh turganda Yashil/Sariq LED yonib tursin;
- Tugma bosib turilganda esa Qizil LED yonsin, Sariq o'chsin (Avtomobil signalizatsiyasi yoki xavf tugmasi modeli).

</div>

