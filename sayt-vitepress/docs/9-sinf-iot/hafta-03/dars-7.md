---
title: "13-dars. 7-dars: Elektron sxema asosida ikki LED lampaning ishlash prinsipi va ulanishi"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (IoT)", "link": "/9-sinf-iot/"}, "week": {"n": 3, "link": "/9-sinf-iot/hafta-03/"}, "g": 13, "title": "7-dars: Elektron sxema asosida ikki LED lampaning ishlash prinsipi va ulanishi", "lead": "IoT uchun asosiy qurilmalar: Arduino va Raspberry Pi taqqosi", "slide": "/slaydlar/9-sinf-iot/hafta-03/dars-7.html", "test": "/slaydlar/9-sinf-iot/hafta-03/dars-7-test.html", "tabs": [{"g": 13, "link": "/9-sinf-iot/hafta-03/dars-7", "current": true}, {"g": 14, "link": "/9-sinf-iot/hafta-03/dars-8", "current": false}, {"g": 15, "link": "/9-sinf-iot/hafta-03/dars-9", "current": false}], "prev": null, "next": {"g": 14, "title": "8-dars: Arduino UNO yordamida LED indikatorlari va push-button bilan ishlash (1-qism)", "link": "/9-sinf-iot/hafta-03/dars-8"}}
---

**Fan:** Internet of Things (IoT — Buyumlar Interneti)  
**Sinf:** 9-sinf  
**Mavzu:** Ikki LED lampaning ketma-ket va parallel ulanishi, Arduino Pin 9 va Pin 11 orqali mustaqil dasturiy boshqaruv

---

<div class="blk">

## <Icon name="file-text" /> Darsning qisqacha mazmuni

Avvalgi darsda bitta LED bilan ishlashni o'rgangan bo'lsak, endi tizimni kengaytiramiz. Real IoT loyihalarida (masalan, svetofor, xavfsizlik signalizatsiyasi, aqlli uy holati indikatorlari) odatda bir nechta turli rangdagi LEDlar bir vaqtning o'zida yoki navbatma-navbat ishlatiladi. Ushbu darsda biz ikkita LEDni ketma-ket va parallel ulashning fizik farqlarini tahlil qilamiz hamda Arduino orqali ularni mustaqil boshqarish dasturini tuzamiz.

### Asosiy tushunchalar:
- **Ketma-ket ulanish (Series):** Tok kuchi bir xil ($I_{umumiy} = I_1 = I_2$), kuchlanish esa bo'linadi ($U_{umumiy} = U_1 + U_2$);
- **Parallel ulanish (Parallel):** Har bir tarmoqqa to'liq manba kuchlanishi tushadi ($U_{umumiy} = U_1 = U_2$), toklar esa qo'shiladi ($I_{umumiy} = I_1 + I_2$);
- **Mustaqil boshqaruv:** Har bir LED mikrokontrollerning alohida raqamli piniga va alohida 220 Om rezistorga ulanishi;
- **Svetofor mantig'i:** Chiroqlarning qat'iy vaqt oralig'i (delay) bilan navbatma-navbat almashinib yonishi;
- **O'zgaruvchilar:** `int red = 9;` va `int yellow = 11;` orqali pinlarni nomlash.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Mustaqil bajarish uchun topshiriqlar

### 1-topshiriq <Badge type="tip" text="oson" />
Tinkercad Circuits-da yangi loyiha oching va unga `9-sinf_Familiya_Dars7` deb nom bering. Ish maydoniga Arduino Uno, kichik Breadboard, 2 ta 220 Om rezistor, 1 ta Qizil va 1 ta Sariq LED joylashtiring.

### 2-topshiriq <Badge type="tip" text="oson" />
Breadboard ustiga Qizil LED va Sariq LED ni bir-biridan kamida 5 ta ustun masofada o'rnating. Har birining anodi yoniga 220 Om rezistorni ulab chiqing.

### 3-topshiriq <Badge type="tip" text="oson" />
Sxemani Arduino ga ulang:
- Qizil LED rezistorini Arduino `D9` piniga;
- Sariq LED rezistorini Arduino `D11` piniga;
- Ikkala LED katodlarini breadboardning `-` shinasiga va undan Arduino `GND` ga bog'lang.

### 4-topshiriq <Badge type="tip" text="oson" />
"Code" panelida C++ matnli rejimiga o'ting va `setup()` funksiyasida ikkala pinni ham chiqish (`OUTPUT`) sifatida sozlang:
```cpp
pinMode(9, OUTPUT);
pinMode(11, OUTPUT);
```

### 5-topshiriq <Badge type="warning" text="o'rta" />
Rasmiy qo'llanmadagi quyidagi to'liq kodni muharrirga kiriting:
```cpp
int red = 9;
int yellow = 11;

void setup() {
  pinMode(red, OUTPUT);
  pinMode(yellow, OUTPUT);
}

void loop() {
  digitalWrite(red, 1);
  delay(5000);
  digitalWrite(red, 0);
  digitalWrite(yellow, 1);
  delay(2000);
  digitalWrite(yellow, 0);
  delay(5000);
}
```
"Start Simulation" tugmasini bosing va chiroqlarning navbatma-navbat yonishini kuzatib, vaqtlarni daftaringizga yozing.

### 6-topshiriq <Badge type="warning" text="o'rta" />
Dastur kodini o'zgartiring: Qizil va Sariq chiroqlar bir vaqtning o'zida yonsin (1 soniya), so'ngra bir vaqtda o'chsin (1 soniya). Ushbu sinxron miltillash kodi qanday yozilishini ko'rsating.

### 7-topshiriq <Badge type="warning" text="o'rta" />
Qizil va Sariq LEDlar bir-biriga qarama-qarshi (antifaza) rejimda ishlasin: Qizil yonganda Sariq o'chsin, Qizil o'chganda esa Sariq yonsin (har bir holat 1 soniyadan).

### 8-topshiriq <Badge type="warning" text="o'rta" />
Alohida bo'sh breadboardda 9V batareyaga ikkita qizil LEDni avval ketma-ket (bitta 220 Om rezistor orqali), so'ngra parallel (har biri alohida rezistor orqali) ulang. Ikkala holatdagi yorqinlik farqini ko'zdan kechiring va fizik sababini tushuntiring.

### 9-topshiriq <Badge type="danger" text="qiyin" />
Yo'l harakatini tartibga soluvchi svetofor siklini takomillashtiring:
- Qizil yonadi (4 soniya);
- Qizil o'chmasdan, Sariq ham qo'shilib yonadi (tayyorgarlik — 1.5 soniya);
- Ikkalasi o'chadi (2 soniya);
- Tsikl boshidan takrorlanadi.

### 10-topshiriq <Badge type="danger" text="qiyin" />
Politsiya mashinasining miltillovchi patrul chiroqlari (Strobe Light) algoritmini tuzing:
- Qizil chiroq 3 marta tez miltillaydi (har biri 80 ms yoniq, 80 ms o'chiq);
- So'ng Sariq chiroq 3 marta tez miltillaydi (har biri 80 ms yoniq, 80 ms o'chiq);
- Jarayon to'xtovsiz takrorlansin.

### 11-topshiriq <Badge type="info" text="bonus" />
Zanjirga uchinchi Yashil LED qo'shing va uni Arduino ning `D7` piniga ulang. Qizil (5s) -> Sariq (2s) -> Yashil (5s) -> Sariq miltillash (2s) ko'rinishidagi to'liq haqiqiy avtomobil svetofori dasturini yozing.

</div>

