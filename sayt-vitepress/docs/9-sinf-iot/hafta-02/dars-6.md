---
title: "9-dars. 6-dars: Elektron sxema asosida bitta LED lampaning ishlash prinsipi va ulanishi"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (IoT)", "link": "/9-sinf-iot/"}, "week": {"n": 2, "link": "/9-sinf-iot/hafta-02/"}, "g": 9, "title": "6-dars: Elektron sxema asosida bitta LED lampaning ishlash prinsipi va ulanishi", "lead": "Arduino UNO yordamida LED indikatorlari va push-button bilan interaktiv interfeys (2-qism)", "slide": "/slaydlar/9-sinf-iot/hafta-02/dars-6.html", "test": "/slaydlar/9-sinf-iot/hafta-02/dars-6-test.html", "tabs": [{"g": 7, "link": "/9-sinf-iot/hafta-02/dars-4", "current": false}, {"g": 8, "link": "/9-sinf-iot/hafta-02/dars-5", "current": false}, {"g": 9, "link": "/9-sinf-iot/hafta-02/dars-6", "current": true}], "prev": {"g": 8, "title": "5-dars: Tinkercad muhitida virtual elektron komponentlar bilan ishlash", "link": "/9-sinf-iot/hafta-02/dars-5"}, "next": null}
---

**Fan:** Internet of Things (IoT — Buyumlar Interneti)  
**Sinf:** 9-sinf  
**Mavzu:** Arduino Uno platasi, raqamli GPIO pinlar, Om qonuni, bitta LED sxemasi va C++ dasturi (Blink)

---

<div class="blk">

## <Icon name="file-text" /> Darsning qisqacha mazmuni

Ushbu darsda biz ilk bor haqiqiy dasturlanadigan mikrokontroller — Arduino Uno bilan amaliyotni boshlaymiz. Oddiy batareyadan farqli o'laroq, mikrokontroller o'z pinlaridan chiquvchi tokni dastur orqali mikrosoniyagacha aniqlikda boshqarish imkonini beradi. Dars davomida bitta LED lampani Arduino ning 9-raqamli piniga ulab, C++ tilida uni yoqib-o'chirishni (Blink) o'rganamiz.

### Asosiy tushunchalar:
- **Arduino Uno:** ATmega328P mikrokontrolleri asosidagi 16 MGts chastotali boshqaruv platasi. 14 ta raqamli kirish/chiqish pinlariga ega;
- **GPIO (General Purpose Input/Output):** Umumiy maqsadli raqamli pinlar. Ular kirish (datchikdan signal olish) yoki chiqish (LED, motorga tok berish) rejimida ishlaydi;
- **LED fizikasi:** Yarimo'tkazgich kristalidagi p-n o'tish orqali elektronlar va kovaklar rekombinatsiyasi paytida fotonlar (yorug'lik) nurlanishi;
- **Om qonuni hisobi:** $R = (U_{manba} - U_{led}) / I_{led} = (5\text{V} - 2\text{V}) / 0.015\text{A} = 200\ \Omega \approx 220\ \Omega$;
- **`void setup()`:** Dastur boshida faqat 1 marta bajariladigan dastlabki sozlashlar bo'limi;
- **`void loop()`:** Dastur to'xtovsiz, cheksiz aylanadigan asosiy ishchi tsikli;
- **Asosiy buyruqlar:** `pinMode(pin, OUTPUT)`, `digitalWrite(pin, HIGH/LOW)`, `delay(millisekund)`.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Mustaqil bajarish uchun topshiriqlar

### 1-topshiriq <Badge type="tip" text="oson" />
Tinkercad Circuits muhitida yangi loyiha oching va unga `9-sinf_Familiya_Dars6` deb nom bering. Ish maydoniga Arduino Uno R3 platasi, kichik Breadboard, 220 Om rezistor va qizil LED joylashtiring.

### 2-topshiriq <Badge type="tip" text="oson" />
Arduino platasining korpusini ko'zdan kechiring. Undagi raqamli pinlar soni nechta ekanini (0 dan 13 gacha) va ulardan qaysilarining yonida `~` (tilda / PWM) belgisi borligini daftaringizga yozing.

### 3-topshiriq <Badge type="tip" text="oson" />
Breadboard ustiga bitta LED va 220 Om rezistorni o'rnating. Rezistor rangli chiziqlari ketma-ketligi (Qizil - Qizil - Jigarrang - Oltin) to'g'ri ekanini tekshiring.

### 4-topshiriq <Badge type="tip" text="oson" />
Elektron sxemani simlar orqali quyidagicha ulang:
- Arduino ning `D9` raqamli pinidan sim chiqarib, rezistorga ulang;
- Rezistorning ikkinchi oyog'idan LED ning Anodiga (uzun oyog'iga) ulang;
- LED ning Katodidan (qisqa oyog'idan) qora sim chiqarib, Arduino ning `GND` piniga ulang.

### 5-topshiriq <Badge type="warning" text="o'rta" />
Yuqori paneldagi "Code" bo'limini oching va rejimni "Text" ga o'tkazing. Rasmiy darslikdagi quyidagi C++ kodini muharrirga kiriting:
```cpp
int LED = 9;

void setup() {
  pinMode(LED, OUTPUT);
}

void loop() {
  digitalWrite(LED, 1);
  delay(2000);
  digitalWrite(LED, 0);
  delay(1000);
}
```
"Start Simulation" tugmasini bosing va LED 2 soniya yonib, 1 soniya o'chayotganini kuzating.

### 6-topshiriq <Badge type="warning" text="o'rta" />
`delay()` parametrlarini o'zgartiring: LED 500 ms (yarim soniya) yonsin va 500 ms o'chsin. Simulyatsiyani qayta ishga tushirib, miltillash tezligi qanday o'zgarganini solishtiring.

### 7-topshiriq <Badge type="warning" text="o'rta" />
`setup()` funksiyasi ichidagi `pinMode(LED, OUTPUT);` qatorini izohga olib qo'ying (oldiga `//` qo'ying) va "Start Simulation" tugmasini bosing. Nima yuz berdi? Nega LED juda xira yonib qolganini tushuntirib bering. So'ngra kodni yana asl holiga qaytaring.

### 8-topshiriq <Badge type="warning" text="o'rta" />
LED rangini qizildan Moviy (Blue) rangga o'zgartiring. Moviy LED ning ochilish kuchlanishi ~3.2V ekanini hisobga olib, Om qonuni bo'yicha unga qanday qarshilikdagi rezistor kerakligini hisoblang ($R = (5 - 3.2) / 0.015$).

### 9-topshiriq <Badge type="danger" text="qiyin" />
Arduino 9-piniga ulangan LED yordamida "Yurak urishi" (Heartbeat) effektini dasturlang:
- 1-zarba: 100 ms yoniq, 100 ms o'chiq;
- 2-zarba: 100 ms yoniq, 700 ms o'chiq;
- Tsikl cheksiz takrorlansin.

### 10-topshiriq <Badge type="danger" text="qiyin" />
Morze alifbosi asosida xalqaro favqulodda xabar — **SOS** signali (`... --- ...`) miltillash dasturini tuzing:
- 3 ta qisqa miltillash (har biri 200 ms yoniq, 200 ms o'chiq);
- 3 ta uzun miltillash (har biri 800 ms yoniq, 200 ms o'chiq);
- 3 ta qisqa miltillash (har biri 200 ms yoniq, 200 ms o'chiq);
- To'liq signallar oralig'ida 3 soniya tanaffus.

### 11-topshiriq <Badge type="info" text="bonus" />
Sxemaga ikkinchi yashil rangli LED qo'shing va uni Arduino ning `D11` piniga 220 Om rezistor orqali ulang. C++ kodida `setup()` va `loop()` funksiyalarini shunday to'ldiringki, qizil va yashil chiroqlar navbatma-navbat (biri yonganda ikkinchisi o'chib) miltillaydigan politsiya mayoqchasi (Strobe light) effekti hosil bo'lsin.

</div>

