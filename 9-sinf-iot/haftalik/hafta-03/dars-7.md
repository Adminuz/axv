# 7-dars: Elektron sxema asosida ikki LED lampaning ishlash prinsipi va ulanishi

**Fan:** Internet of Things (IoT — Buyumlar Interneti)  
**Sinf:** 9-sinf  
**Hafta:** 3-hafta, 1-dars (umumiy 7-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga ikkita LED lampani elektron zanjirda ketma-ket (Series) va parallel (Parallel) ulash qonuniyatlarini o'rgatish; kuchlanish va tokning taqsimlanishidagi farqlarni tushuntirish; Arduino Uno mikrokontrollerining ikkita mustaqil raqamli pini (Pin 9 va Pin 11) orqali ikkita LEDni dasturiy boshqarish (navbatma-navbat yoqish, bir vaqtda miltillatish, svetofor boshlang'ich modeli) ko'nikmalarini shakllantirish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- Ketma-ket va parallel ulanishdagi fizik qonuniyatlarni (kuchlanish $U$ va tok $I$ taqsimoti) farqlay olish;
- Nega mikrokontrollerlarda har bir LED uchun alohida pin va alohida rezistor (parallel boshqaruv) tanlanishini asoslash;
- Arduino Uno platasining ikkita chiqish piniga (Pin 9 — Qizil, Pin 11 — Sariq) to'g'ri elektron sxema yig'ish;
- C++ tilida bir nechta o'zgaruvchilarni e'lon qilish (`int red = 9; int yellow = 11;`);
- `setup()` funksiyasida ikkala pinni ham `OUTPUT` rejimiga sozlash;
- `loop()` tsiklida navbatma-navbat yoqish algoritmini dasturlash va simulyatsiyada tekshirish.

---

## Kerakli jihozlar va vositalar

- Kompyuter yoki noutbuk (internetga ulangan);
- Veb-brauzer orqali Tinkercad.com virtual laboratoriyasiga kirish;
- Proyektor yoki monitor (namoyish uchun).

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va o'tgan mavzuni takrorlash | Arduino Uno xususiyatlari, Om qonuni, bitta LED Blink kodi bo'yicha blits-so'rov |
| **10–25 min** | Yangi mavzu: Ketma-ket vs Parallel ulanish | $U = U_1 + U_2$ va $I = I_1 + I_2$; nega ketma-ket LEDlar xira yonadi va biri ketsa ikkinchisi ham o'chadi |
| **25–40 min** | Mustaqil boshqaruv arxitekturasi | Arduino da 2 ta alohida pin (Pin 9 va Pin 11) orqali boshqarish sxemasi |
| **40–60 min** | Amaliy laboratoriya: Tinkercad-da 2 ta LED sxemasi | Sxemani yig'ish, C++ dasturini yozish (Qizil 5s, Sariq 2s, tanaffus 5s) |
| **60–75 min** | Mustaqil amaliy topshiriqlar | Qarama-qarshi miltillash (Strobe), bir vaqtda yonish va vaqt intervallari tahlili |
| **75–80 min** | Xulosa va uyga vazifa | Asosiy qonuniyatlarni umumlashtirish, baholash |

---

## Nazariy ma'lumotlar

### 1. Ketma-ket (Series) vs Parallel ulanish

Elektronikada bir nechta iste'molchilarni (LEDlarni) ikki xil usulda ulash mumkin:

1. **Ketma-ket ulanish (Series):**
   - LEDlar birining orqasidan biri zanjirga ulanadi (1-LED katodi 2-LED anodiga bog'lanadi);
   - **Tok kuchi:** Barcha komponentlardan bir xil tok o'tadi: $I_{umumiy} = I_1 = I_2$;
   - **Kuchlanish:** Umumiy kuchlanish LEDlar o'rtasida bo'linadi: $U_{umumiy} = U_1 + U_2$. Agar ikkita qizil LED ($2\text{V} + 2\text{V} = 4\text{V}$) ulansa, 5V dan rezistorga faqat 1V qoladi. Agar 3 ta LED ulansa ($6\text{V} > 5\text{V}$), 5V kuchlanish yetmasdan LEDlar umuman yonmaydi!
   - **Kamchiligi:** Agar bitta LED ishdan chiqsa (kuyib uzilsa), butun zanjir uzilib, barcha chiroqlar o'chadi (eski archa gulchambarlari kabi).

2. **Parallel ulanish (Parallel):**
   - Har bir LED o'zining shaxsiy rezistoriga ega bo'lib, umumiy quvvat va yerga mustaqil ulanadi;
   - **Kuchlanish:** Har bir LED ga to'liq manba kuchlanishi (5V) tushadi: $U_{umumiy} = U_1 = U_2$;
   - **Tok kuchi:** Umumiy tok har bir tarmoqdagi toklar yig'indisiga teng: $I_{umumiy} = I_1 + I_2$;
   - **Afzalligi:** LEDlar to'liq nominal yorqinlikda yonadi va birining kuyishi boshqasiga ta'sir qilmaydi.

### 2. Arduino orqali mustaqil dasturiy boshqaruv

Arduino da har bir LED mikrokontrollerning alohida raqamli piniga ulanadi:
- **Qizil LED:** Arduino Digital Pin 9 -> 220 Om rezistor -> Anod -> Katod -> GND;
- **Sariq LED:** Arduino Digital Pin 11 -> 220 Om rezistor -> Anod -> Katod -> GND;

Bu usul dasturchiga har bir chiroqni boshqasiga bog'liq bo'lmagan holda istalgan vaqtda yoqish, o'chirish yoki svetofor kabi ma'lum algoritm bo'yicha boshqarish imkonini beradi.

### 3. Rasmiy dastur kodi tahlili

```cpp
int red = 9;      // Qizil LED 9-pinga ulangan
int yellow = 11;  // Sariq LED 11-pinga ulangan

void setup() {
  pinMode(red, OUTPUT);    // 9-pin chiqish rejimida
  pinMode(yellow, OUTPUT); // 11-pin chiqish rejimida
}

void loop() {
  digitalWrite(red, 1);    // Qizil LED yoqiladi
  delay(5000);             // 5 soniya kutadi
  digitalWrite(red, 0);    // Qizil LED o'chiriladi
  digitalWrite(yellow, 1); // Sariq LED yoqiladi
  delay(2000);             // 2 soniya kutadi
  digitalWrite(yellow, 0); // Sariq LED o'chiriladi
  delay(5000);             // Ikkalasi ham o'chiq holda 5 soniya kutadi
}
```

Ushbu dastur soddalashtirilgan svetofor (yo'l harakatini tartibga solish) tamoyilini namoyish etadi.

---

## Amaliy mashg'ulot va topshiriqlar

### 1-topshiriq. Breadboardda 2 ta LED sxemasini yig'ish (oson)
Tinkercad Circuits ish maydonida Arduino Uno, Breadboard, 2 ta 220 Om rezistor, 1 ta Qizil va 1 ta Sariq LED joylashtiring.
- Qizil LED anodini 220 Om rezistor orqali Arduino `D9` ga ulang;
- Sariq LED anodini 220 Om rezistor orqali Arduino `D11` ga ulang;
- Ikkala LED ning katodlarini breadboardning `-` shinasiga va undan Arduino `GND` piniga ulang.

**Yechim:**
1. Qizil va Sariq LED breadboard ustunlariga joylashtiriladi.
2. Har bir LED ning anodi yoniga 220 Om rezistorlar vertikal qo'yiladi.
3. Rezistorlarning ochiq uchidan mos ravishda Arduino ning 9 va 11 pinlariga rangli simlar tortiladi.
4. LED katodlari breadboardning ko'k `-` shinasiga ulanadi.
5. Breadboard `-` shinasidan qora sim Arduino platasidagi `GND` piniga bog'lanadi.

### 2-topshiriq. Dastur kodini kiritish va sinovdan o'tkazish (o'rta)
Code panelida matnli C++ rejimiga o'ting va rasmiy qo'llanmadagi kodni kiriting. Simulyatsiyani ishga tushiring: Qizil chiroq 5 soniya yonib, so'ng o'chishi va sariq chiroq 2 soniya yonib o'chishi kerak.

**Yechim:**
1. Code paneli ochilib, matnli rejimga o'tiladi.
2. Yuqorida keltirilgan rasmiy kod yoziladi.
3. "Start Simulation" bosiladi.
4. Vaqt hisoblagichi (Simulator time) orqali jarayon kuzatiladi: 0–5s oralig'ida Qizil yonadi, 5–7s oralig'ida Sariq yonadi, 7–12s oralig'ida ikkalasi o'chadi va sikl qaytadan boshlanadi.

### 3-topshiriq. Politsiya patrul mayoqchasi (Strobe light) algoritmi (qiyin)
Ikki LED bir-biri bilan teskari fazada tezkor miltillaydigan patrul mashinasi chiroqlari algoritmini tuzing:
- Qizil yonsin, Sariq o'chsin (100 ms);
- Qizil o'chsin, Sariq yonsin (100 ms);
- Ushbu jarayon 5 marta tezkor takrorlangach, ikkala chiroq 500 ms ga o'chsin.

**Yechim:**
```cpp
int red = 9;
int yellow = 11;

void setup() {
  pinMode(red, OUTPUT);
  pinMode(yellow, OUTPUT);
}

void loop() {
  for (int i = 0; i < 5; i++) {
    digitalWrite(red, HIGH);
    digitalWrite(yellow, LOW);
    delay(100);
    digitalWrite(red, LOW);
    digitalWrite(yellow, HIGH);
    delay(100);
  }
  digitalWrite(red, LOW);
  digitalWrite(yellow, LOW);
  delay(500);
}
```

---

## Tezkor nazorat savollari

1. Agar ikkita LED ketma-ket ulansa, nima sababdan ular parallel ulangandagiga qaraganda xiraroq yonadi?
   - *Javob:* Chunki ketma-ket ulanishda 5V manba kuchlanishi ikkala LED o'rtasida bo'linadi (har biriga taxminan 2V–2.5V tushadi), parallel ulanishda esa har bir LED ga to'liq 5V beriladi.
2. Arduino dasturida ikkita pinni chiqish qilish uchun `setup()` da nechta `pinMode()` chaqirilishi kerak?
   - *Javob:* Har bir pin uchun alohida, ya'ni 2 ta `pinMode()` chaqiriladi.
3. Nega ikkita LED uchun bitta umumiy rezistor qo'yish tavsiya etilmaydi?
   - *Javob:* Bitta umumiy rezistor qo'yilsa, LEDlarning biri yoqilganda va ikkalasi bir vaqtda yoqilganda tok o'zgarib, yorqinlik bir tekis bo'lmaydi va xavfsiz tok chegarasi buziladi.
4. `digitalWrite(yellow, !digitalRead(yellow));` amali nimani anglatadi?
   - *Javob:* Sariq LEDning joriy holatini teskarisiga o'zgartiradi (agar yoniq bo'lsa o'chiradi, o'chiq bo'lsa yoqadi — Toggle effekti).

---

## Keng tarqalgan xatolar va ularning oldini olish

- **Ikkala LED uchun bitta rezistor ishlatish:** O'quvchilar rezistorni tejash maqsadida ikkita LED katodini bitta 220 Om rezistorga ulab qo'yishadi. Agar ikkala LED bir vaqtda yonsa, ulardan o'tadigan tok kamayib, yorug'lik xiralashadi. Har bir LED shaxsiy rezistorga ega bo'lishi shart.
- **Pin raqamlarini kodda chalkashtirib yuborish:** Dasturda `red = 9` deb e'lon qilib, simni 8 yoki 10-pinga ulab qo'yish. Sxema simi bilan dastur kodi bir-biriga qat'iy mos kelishi kerak.
