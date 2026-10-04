---
title: "7-dars. 4-dars: Tinkercad.com virtual laboratoriyasida ro‘yxatdan o‘tish va interfeys"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (IoT)", "link": "/9-sinf-iot/"}, "week": {"n": 2, "link": "/9-sinf-iot/hafta-02/"}, "g": 7, "title": "4-dars: Tinkercad.com virtual laboratoriyasida ro‘yxatdan o‘tish va interfeys", "lead": "Elektron sxema asosida ikki LED lampaning ishlash prinsipi va ulanishi", "slide": "/slaydlar/9-sinf-iot/hafta-02/dars-4.html", "tabs": [{"g": 7, "link": "/9-sinf-iot/hafta-02/dars-4", "current": true}, {"g": 8, "link": "/9-sinf-iot/hafta-02/dars-5", "current": false}, {"g": 9, "link": "/9-sinf-iot/hafta-02/dars-6", "current": false}], "prev": null, "next": {"g": 8, "title": "5-dars: Tinkercad muhitida virtual elektron komponentlar bilan ishlash", "link": "/9-sinf-iot/hafta-02/dars-5"}}
---

**Fan:** Internet of Things (IoT — Buyumlar Interneti)  
**Sinf:** 9-sinf  
**Mavzu:** Tinkercad platformasida ro‘yxatdan o‘tish, "Circuits" bo'limi, ishchi maydon (Workplane) va boshqaruv panellari

---

<div class="blk">

## <Icon name="file-text" /> Darsning qisqacha mazmuni

Tinkercad.com — bu Autodesk kompaniyasi tomonidan yaratilgan, brauzer orqali ishlovchi bepul 3D modellashtirish va virtual elektronika simulyatoridir. Mazkur platforma yordamida haqiqiy komponentlarni kuydirib qo'yish yoki xarid qilish xavfisiz, internet orqali xavfsiz muhitda elektron sxemalar yig'ish, mikrokontrollerlarga kod yozish va real vaqtda simulyatsiya qilish mumkin.

### Asosiy tushunchalar:
- **Virtual laboratoriya:** Kompyuter dasturi yoki veb-xizmat orqali fizik qonuniyatlarni va elektron komponentlarni real vaqtda modellashtiruvchi muhit;
- **Circuits (Sxemalar):** Tinkercad platformasining elektron zanjirlar va mikrokontrollerlar bilan ishlashga mo'ljallangan maxsus bo'limi;
- **Workplane:** Komponentlar joylashtiriladigan va simlar orqali ulanadigan markaziy ishchi maydon;
- **Komponentlar paneli:** Chap/o'ng tomondagi elementlar kutubxonasi (Basic va All toifalari);
- **Start Simulation:** Zanjirga virtual elektr tokini uzatib, uning ishlashini tekshirish tugmasi;
- **Tezkor klavishlar:** `R` — komponentni 30° ga burish, `Del` — o'chirish, `Ctrl+Z` — orqaga qaytarish, `N` — matnli eslatma qo'yish.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Mustaqil bajarish uchun topshiriqlar

### 1-topshiriq <Badge type="tip" text="oson" />
`tinkercad.com` rasmiy saytiga kiring va shaxsiy Google akkauntingiz orqali ro'yxatdan o'ting. Shaxsiy profilingiz sozlamalarida ism va familiyangiz to'g'ri ko'rsatilganini tekshiring.

### 2-topshiriq <Badge type="tip" text="oson" />
Tinkercad boshqaruv panelidagi (Dashboard) "Circuits" bo'limiga o'ting va "Create new Circuit" tugmasini bosib, yangi toza loyiha ishchi maydonini oching.

### 3-topshiriq <Badge type="tip" text="oson" />
Yangi ochilgan loyihaning yuqori chap burchagidagi tasodifiy generatsiya qilingan nomni o'zgartiring va unga `9-sinf_Familiya_01` nomini bering.

### 4-topshiriq <Badge type="tip" text="oson" />
O'ng tomondagi "Basic" komponentlar panelidan quyidagi 4 ta komponentni toping va ularni ish maydoniga (Workplane) sichqoncha bilan tortib olib chiqing:
1. Arduino Uno R3;
2. Kichik maket plata (Small Breadboard);
3. Oddiy qizil LED;
4. 1 ta rezistor.

### 5-topshiriq <Badge type="warning" text="o'rta" />
Ish maydoniga qo'yilgan rezistor ustiga bosing. Chiqqan parametrlar oynasida qarshilik qiymatini `220` raqamiga o'zgartiring va o'lchov birligini `kΩ` (kilo-om) dan `Ω` (Om) ga o'tkazing. Rezistordagi rangli chiziqlar ketma-ketligi qanday o'zgarganini daftaringizga yozing.

### 6-topshiriq <Badge type="warning" text="o'rta" />
Ish maydoniga yana 3 ta turli xil LED lampalarni joylashtiring. Ularning parametrlar oynasi orqali ranglarini mos ravishda Sariq (Yellow), Yashil (Green) va Ko'k (Blue) ranglarga sozlang.

### 7-topshiriq <Badge type="warning" text="o'rta" />
Komponentlarni burish asbobi (`Rotate` yoki klaviaturadagi `R` tugmasi) yordamida breadboard platasini 90 gradusga, bitta rezistorni esa vertikal holatga keltiring. Har bir burish qadami necha gradusga teng ekanini aniqlang.

### 8-topshiriq <Badge type="warning" text="o'rta" />
Komponentlar filtrini "Basic" dan "All" (Barchasi) rejimiga o'tkazing. Qidiruv maydoni orqali quyidagi 3 ta komponentni topib ish maydoniga qo'ying:
1. Ultrasonic Distance Sensor (HC-SR04);
2. PIR Sensor (harakat datchigi);
3. Micro Servo (motor).

### 9-topshiriq <Badge type="danger" text="qiyin" />
"Notes" (Izohlar) asbobidan foydalanib, ish maydonidagi har bir komponent yoniga uning vazifasini bildiruvchi qisqa matnli yorliq biriktiring (masalan: "Ultrasonic — masofani o'lchaydi", "Servo — eshikni ochuvchi mexanizm"). Keyin eslatmalarni yashirish va ko'rsatish tugmasini sinab ko'ring.

### 10-topshiriq <Badge type="danger" text="qiyin" />
Yuqori paneldagi "Start Simulation" tugmasini bosing. Nega hech qanday sim ulanmagan holatda hech bir komponent harakatlanmadi yoki yonmadi? "Stop Simulation" tugmasini bosing va elektr zanjirida tok oqishi uchun qanday ikki muhim qoida bajarilishi shartligini yozma bayon qiling.

### 11-topshiriq <Badge type="info" text="bonus" />
Yuqori o'ng burchakdagi "Share" (Ulashish) tugmasi orqali sxemangizning ommaviy havolasini (Public Share Link) hosil qiling va ushbu havolani do'stingizga yoki o'qituvchiga yuborib, uning brauzerida sxemangiz to'g'ri ko'rinayotganini tekshirib ko'ring.

</div>

