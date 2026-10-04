# 6-dars: Elektron sxema asosida bitta LED lampaning ishlash prinsipi va ulanishi

**Fan:** Internet of Things (IoT — Buyumlar Interneti)  
**Sinf:** 9-sinf  
**Hafta:** 2-hafta, 3-dars (umumiy 6-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga Arduino Uno mikrokontroller platasi arxitekturasi va raqamli pinlari, LEDning fizik ishlash prinsipi (p-n o'tish, rekombinatsiya) va Om qonuni asosida 220 Om himoya qarshiligini hisoblashni o'rgatish; Arduino Uno ga bitta LED lampani to'g'ri ulash hamda C++ dasturiy kodi (`pinMode`, `digitalWrite`, `delay`) yordamida dasturiy boshqarish va simulyatsiya qilish ko'nikmalarini shakllantirish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- Arduino Uno platasining asosiy parametrlarini (ATmega328P, 16 MHz, 14 ta raqamli pin, 6 ta PWM, GND, 5V) bilish;
- LEDning fizik ishlash mexanizmi (p-n o'tishda elektronlar va kovaklar rekombinatsiyasi orqali foton ajralishi)ni tushunish;
- Om qonuni bo'yicha LED uchun 220–330 Om himoya rezistorini mustaqil hisoblay olish;
- Arduino platasining raqamli chiqishi (Pin 9), rezistor, breadboard va LED dan iborat to'g'ri sxemani yig'ish;
- Arduino dasturining ikkita asosiy ustuni: `setup()` va `loop()` vazifalarini bilish;
- `pinMode()`, `digitalWrite()` va `delay()` buyruqlari yordamida LEDni turli vaqt oralig'ida dasturiy yoqib-o'chirish (Blink).

---

## Kerakli jihozlar va vositalar

- Kompyuter yoki noutbuk (internetga ulangan);
- Veb-brauzer orqali Tinkercad.com virtual laboratoriyasiga kirish;
- Proyektor yoki monitor (namoyish uchun).

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va o'tgan mavzuni takrorlash | Breadboard ichki tuzilishi, multimetr bilan o'lchash va rezistor ranglari bo'yicha blits-savollar |
| **10–25 min** | Yangi mavzu: Arduino Uno va LED fizikasi | ATmega328P chipi, 14 ta raqamli pin, LEDning p-n o'tishi va Om qonuni bo'yicha rezistor hisobi |
| **25–40 min** | Sxemani yig'ish va dasturlash nazariyasi | 9-pin -> 220 Om -> LED Anod -> Katod -> GND ulanishi; `setup()` va `loop()` arxitekturasi |
| **40–60 min** | Amaliy mashg'ulot: Tinkercad-da Blink loyihasi | Sxemani yig'ish, C++ matnli kodini kiritish, simulyatsiyani ishga tushirish |
| **60–75 min** | Mustaqil amaliy topshiriqlar | Vaqt intervallarini o'zgartirish (2s yoqiq / 1s o'chiq, tezkor miltillash, SOS signali) |
| **75–80 min** | Xulosa va uyga vazifa | Mavzuni yakunlash, o'quvchilarni baholash |

---

## Nazariy ma'lumotlar

### 1. Arduino Uno mikrokontroller platasi

Arduino Uno — bu italiyalik muhandislar tomonidan yaratilgan, dunyoda eng keng tarqalgan ochiq kodli apparat platformasidir.
- **Bosh protsessor:** **ATmega328P** mikrokontroller chipi (8-bitli AVR arxitekturasi);
- **Chastota:** **16 MGts** (sekundiga 16 million amal bajaradi);
- **Xotira:** 32 KB Flash xotira (dastur saqlanadi), 2 KB SRAM (tezkor o'zgaruvchilar) va 1 KB EEPROM;
- **Raqamli GPIO pinlari:** **14 ta** (0 dan 13 gacha). Bu pinlar kirish (INPUT) yoki chiqish (OUTPUT) sifatida 0V (LOW) va 5V (HIGH) signallari bilan ishlaydi;
- **PWM chiqishlari:** 3, 5, 6, 9, 10 va 11-pinlar to'lqin kenglik modulyatsiyasini (analogni taqlid qilish) qo'llab-quvvatlaydi;
- **Analog kirishlar:** A0 dan A5 gacha (0–5V kuchlanishni 0–1023 soniga aylantirib o'qiydi);
- **Quvvat pinlari:** 5V, 3.3V, VIN va 3 ta GND (Yer) pinlari.

### 2. LEDning fizik ishlash prinsipi va Om qonuni

**LED (Light Emitting Diode):** Yarimo'tkazgichli kristall (masalan, galliy arsenid yoki galliy fosfid) asosidagi diod.
- Kristall ichida ikki xil soha bor: **p-soha** (kovaklar — musbat zaryad tashuvchilar) va **n-soha** (elektronlar — manfiy zaryad tashuvchilar);
- Anodga musbat (+), Katodga manfiy (-) kuchlanish berilganda elektronlar va kovaklar o'zaro to'qnashadi (**rekombinatsiya**);
- Ushbu to'qnashuv paytida ortiqcha energiya issiqlik emas, balki to'g'ridan-to'g'ri yorug'lik zarrachalari — **fotonlar** ko'rinishida fazoga nurlanadi!

**Nima uchun 220 Om rezistor kerak? (Om qonuni hisobi):**
- Arduino pinining chiqish kuchlanishi: $U_{pin} = 5\text{ V}$;
- Qizil LED ning ochilish kuchlanishi: $U_{led} \approx 2.0\text{ V}$;
- LED uchun xavfsiz va yetarli tok kuchi: $I = 15\text{ mA} = 0.015\text{ A}$;
- Rezistorda tushishi kerak bo'lgan kuchlanish: $U_R = 5\text{ V} - 2\text{ V} = 3\text{ V}$;
- Om qonuni bo'yicha kerakli qarshilik:
  $$R = \frac{U_R}{I} = \frac{3\text{ V}}{0.015\text{ A}} = 200\ \Omega$$
Standart sanoat qatorida 200 Om ga eng yaqin nominal **220 Ω** (yoki 330 Ω) hisoblanadi.

### 3. Arduino C++ dastur arxitekturasi

Har bir Arduino dasturi (sketch) ikkita majburiy funksiyadan iborat:

```cpp
int LED = 9; // 9-raqamli pin o'zgaruvchisi

void setup() {
  pinMode(LED, OUTPUT); // 9-pinni chiqish (OUTPUT) rejimiga sozlash
}

void loop() {
  digitalWrite(LED, HIGH); // LEDni yoqish (5V berish)
  delay(2000);             // 2000 ms (2 soniya) kutish
  digitalWrite(LED, LOW);  // LEDni o'chirish (0V)
  delay(1000);             // 1000 ms (1 soniya) kutish
}
```

1. `void setup()` — mikrokontrollerga quvvat berilganda faqat **1 marta** ishga tushadi. U apparat pinlarini kirish yoki chiqish sifatida sozlash uchun xizmat qiladi.
2. `void loop()` — `setup()` tugagach, cheksiz takrorlanuvchi tsikl sifatida uzluksiz aylanadi.
3. `pinMode(pin, OUTPUT)` — ko'rsatilgan pin orqali tashqi qurilmaga tok yuborilishini belgilaydi.
4. `digitalWrite(pin, 1)` yoki `HIGH` — pinga 5V yuqori darajali signal beradi (LED yonadi).
5. `digitalWrite(pin, 0)` yoki `LOW` — pinga 0V beradi (LED o'chadi).
6. `delay(ms)` — protsessorni ko'rsatilgan millisekund davomida to'xtatib turadi (1000 ms = 1 s).

---

## Amaliy mashg'ulot va topshiriqlar

### 1-topshiriq. Arduino Uno va bitta LED sxemasini yig'ish (oson)
Tinkercad Circuits ish maydoniga Arduino Uno R3, kichik Breadboard, 220 Om rezistor va qizil LED joylashtiring.
Sxemani quyidagicha ulang:
- Arduino 9-pinidan sim olib, breadboarddagi rezistorning bir oyog'iga ulang;
- Rezistorning ikkinchi oyog'ini LED ning Anodiga ulang;
- LED ning Katodini qora sim bilan Arduino ning GND piniga ulang.

**Yechim:**
1. Workplane ga Arduino Uno, Breadboard, Resistor va LED tortib qo'yiladi.
2. Rezistor bosilib, "Resistance" qiymati `220`, birligi `Ω` qilinadi.
3. Arduino platasining `D9` pinidan (raqamli 9-pin) breadboarddagi rezistor ulanadigan ustunga moviy yoki sariq sim tortiladi.
4. Rezistorning ikkinchi oyog'i turgan ustunga LED ning Anod (egik) oyog'i suqiladi.
5. LED ning Katod oyog'idan qora sim chiqarilib, Arduino platasidagi `GND` piniga ulanadi.
6. Sxema elektr jihatdan to'liq yopiq zanjir hosil qiladi.

### 2-topshiriq. C++ kodini yozish va simulyatsiyani ishga tushirish (o'rta)
Yuqori paneldagi "Code" tugmasini bosing. Kod rejimini "Blocks" dan "Text" rejimiga o'tkazing (ogohlantirish oynasida "Continue" bosiladi). Rasmiy qo'llanmadagi kodni yozing: LED 2 soniya yonsin va 1 soniya o'chsin. "Start Simulation" tugmasini bosib, LED ning ishini kuzating.

**Yechim:**
1. "Code" paneli ochilib, tushuvchi menyudan "Text" tanlanadi.
2. Quyidagi kod yoziladi:
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
3. "Start Simulation" bosiladi:
   - USB kabeli Arduino ga ulanadi (animatsiya);
   - LED 2 soniya charaqlab yonadi, so'ng 1 soniya o'chadi va bu jarayon cheksiz davom etadi.

### 3-topshiriq. Tezkor SOS favqulodda signal algoritmi (qiyin)
Morze alifbosi bo'yicha xalqaro falokat signali — **SOS** hisoblanadi: 3 ta qisqa miltillash (S), 3 ta uzun miltillash (O), 3 ta qisqa miltillash (S).
Qisqa miltillash uchun: 200 ms yoniq, 200 ms o'chiq;
Uzun miltillash uchun: 800 ms yoniq, 200 ms o'chiq;
Harfrlar o'rtasida 500 ms, to'liq SOS signallari oralig'ida esa 3000 ms (3 s) tanaffus bo'lsin. Ushbu algoritm kodini yozing.

**Yechim:**
```cpp
int LED = 9;

void setup() {
  pinMode(LED, OUTPUT);
}

void loop() {
  // 3 ta qisqa (S: . . .)
  for(int i = 0; i < 3; i++) {
    digitalWrite(LED, HIGH);
    delay(200);
    digitalWrite(LED, LOW);
    delay(200);
  }
  delay(500); // Harf oralig'i

  // 3 ta uzun (O: - - -)
  for(int i = 0; i < 3; i++) {
    digitalWrite(LED, HIGH);
    delay(800);
    digitalWrite(LED, LOW);
    delay(200);
  }
  delay(500); // Harf oralig'i

  // 3 ta qisqa (S: . . .)
  for(int i = 0; i < 3; i++) {
    digitalWrite(LED, HIGH);
    delay(200);
    digitalWrite(LED, LOW);
    delay(200);
  }

  delay(3000); // Keyingi SOS sikligacha katta tanaffus
}
```

---

## Tezkor nazorat savollari

1. Arduino Uno platasining markaziy mikrokontroller chipi qanday nomlanadi va uning takt chastotasi qancha?
   - *Javob:* ATmega328P chipi, chastotasi 16 MGts.
2. Arduino dasturidagi `void setup()` bilan `void loop()` funksiyalarining eng asosiy farqi nimada?
   - *Javob:* `setup()` faqat mikrokontroller yoqilganda 1 marta bajariladi (sozlamalar uchun); `loop()` esa to'xtovsiz, cheksiz takrorlanadi.
3. `pinMode(9, OUTPUT);` buyrug'i mikrokontrollerga qanday ko'rsatma beradi?
   - *Javob:* 9-raqamli pinni chiqish rejimiga o'tkazadi, ya'ni bu pin orqali tashqariga elektr toki yuborish imkonini beradi.
4. 5V quvvatda ishlaydigan Arduino ga ulangan qizil LED uchun nima sababdan aynan 220 Om rezistor tavsiya etiladi?
   - *Javob:* Om qonuniga binoan, 5V dan LED ning 2V ochilish kuchlanishi ayirilib, qolgan 3V ni 15 mA xavfsiz tokda cheklash uchun $3\text{ V} / 0.015\text{ A} = 200\ \Omega$ talab etiladi, eng yaqin standart qiymat esa 220 Om dir.

---

## Keng tarqalgan xatolar va ularning oldini olish

- **`pinMode()` ni unutish yoki adashtirish:** O'quvchilar `setup()` ichida `pinMode(LED, OUTPUT)` deb yozishni unutishadi. Agar pin chiqish rejimiga sozlanmasa, `digitalWrite(LED, HIGH)` berilganda ham LED juda xira yonadi yoki umuman yonmaydi (chunki pin sukut bo'yicha INPUT rejimida yuqori qarshilikka ega bo'ladi).
- **Nuqta-vergul (`;`) ni tushirib qoldirish:** C++ tilida har bir buyruq qatori oxirida `;` bo'lishi shart. Uni unutish sintaktik xatolik (error: expected ';' before '...') keltirib chiqaradi.
