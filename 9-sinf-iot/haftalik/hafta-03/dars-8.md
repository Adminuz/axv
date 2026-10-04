# 8-dars: Arduino UNO yordamida LED indikatorlari va push-button bilan ishlash (1-qism)

**Fan:** Internet of Things (IoT — Buyumlar Interneti)  
**Sinf:** 9-sinf  
**Hafta:** 3-hafta, 2-dars (umumiy 8-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga raqamli kirish (Digital Input) tushunchasi, Push-button (bosiluvchi tugma) mexanikasi va ichki kontaktlari tuzilishini o'rgatish; "suzuvchi pin" (floating pin) muammosi hamda Pull-up / Pull-down rezistorlari va Arduino ning o'rnatilgan `INPUT_PULLUP` rejimi ishlash prinsipini tushuntirish; `digitalRead()` funksiyasi orqali tugma holatini o'qish va Serial Monitor vositasida real vaqtda ma'lumotlarni kuzatish ko'nikmalarini shakllantirish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- Raqamli kirish (INPUT) va chiqish (OUTPUT) signallari o'rtasidagi asosiy farqni bilish;
- 4 oyoqli Push-button ichki kontaktlari qanday tutashganini tushunish;
- Suzuvchi pin (Floating Pin) nega xavfli ekanini va nima sababdan Pull-up/Pull-down rezistori zarurligini izohlay olish;
- Arduino platasining ichki tortuvchi rezistori — `pinMode(pin, INPUT_PULLUP)` imkoniyatidan foydalanish;
- `digitalRead(buttonPin)` buyrug'i yordamida 0 (LOW) va 1 (HIGH) mantiqiy signallarini qabul qilish;
- Serial Monitor oynasini `Serial.begin(9600)` orqali ishga tushirib, tugma bosilgan/qo'yib yuborilgan holatini kompyuter ekranida ko'rish.

---

## Kerakli jihozlar va vositalar

- Kompyuter yoki noutbuk (internetga ulangan);
- Veb-brauzer orqali Tinkercad.com virtual laboratoriyasiga kirish;
- Proyektor yoki monitor (namoyish uchun).

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va o'tgan mavzuni takrorlash | Ketma-ket vs parallel ulanish, 2 ta LED ni mustaqil boshqarish bo'yicha blits-savollar |
| **10–25 min** | Yangi mavzu: Push-button mexanikasi va Floating pin | 4 ta oyoq ichki sxemasi, havoda qolgan pin xatosi, Pull-up va Pull-down rezistorlari |
| **25–40 min** | Ichki rezistor: INPUT_PULLUP va Serial Monitor | Tashqi rezistorsiz ulash afzalligi, `Serial.begin(9600)` va `Serial.println()` |
| **40–60 min** | Amaliy laboratoriya: Tugma holatini o'qish | Tugma + Arduino Pin 2 ulanishi, Serial Monitor orqali 0 va 1 signallarini tekshirish |
| **60–75 min** | Mustaqil amaliy topshiriqlar | Tugma bosilganda LED yonishi va qo'yib yuborilganda o'chishi dasturini yig'ish |
| **75–80 min** | Xulosa va uyga vazifa | Asosiy xulosalarni qayd etish, vazifalarni berish |

---

## Nazariy ma'lumotlar

### 1. Push-button (Bosiluvchi tugma) tuzilishi

Push-button — bu foydalanuvchi tomonidan bosilganda mexanik ravishda ikkita kontaktni bir-biriga tutashtiruvchi, qo'yib yuborilganda esa prujina kuchi bilan yana uzib qo'yuvchi Normal Ochiq (Normally Open — NO) kirish asbobidir.
- Tugmada **4 ta oyoq** bor (odatda 1a, 1b, 2a, 2b deb belgilanadi);
- 1a va 1b oyoqlari ichkaridan doimiy tutashgan;
- 2a va 2b oyoqlari ham ichkaridan doimiy tutashgan;
- Tugma bosilganda 1-guruh va 2-guruh kontaktlari o'zaro tutashadi.
> **Qoida:** Tugmani breadboardning markaziy ariqchasi ustiga o'rnatish tavsiya etiladi (chap oyoqlari bir tomonda, o'ng oyoqlari ikkinchi tomonda).

### 2. "Suzuvchi Pin" (Floating Pin) muammosi

Agar tugmaning bir oyog'ini 5V ga, ikkinchi oyog'ini esa to'g'ridan-to'g'ri Arduino raqamli piniga ulasak:
- Tugma bosilganda pinga aniq **5V (HIGH)** keladi;
- Ammo tugma qo'yib yuborilganda pin havoda osilib qoladi (na 5V ga, na GND ga ulanmagan);
- Bunday holatda pin mikroantennaga aylanadi va atrofdagi elektromagnit to'lqinlar, statik elektr ta'sirida tasodifiy tarzda goh 0, goh 1 qiymatini o'qiy boshlaydi (**Suzuvchi holat**).
- Buning oldini olish uchun pin doimiy ravishda yuqori qarshilikli (10 kOm) rezistor orqali aniq bir potensialga tortib qo'yilishi shart.

### 3. INPUT_PULLUP: Ichki tortuvchi rezistor

Arduino mikrokontrolleri ichida har bir raqamli pin uchun o'rnatilgan **20–50 kOm ichki Pull-up rezistori** mavjud.
Dasturda:
```cpp
pinMode(2, INPUT_PULLUP);
```
deb yozilsa, pin avtomatik tarzda ichkaridan 5V ga ulanadi.
Endi tashqaridan hech qanday 10 kOm rezistor qo'yish shart emas! Tugmaning bitta oyog'i 2-pinga, ikkinchi oyog'i esa to'g'ridan-to'g'ri **GND** ga ulanadi:
- **Tugma qo'yib yuborilgan holatda:** Pin ichki rezistor orqali 5V oladi -> `digitalRead(2)` natijasi **HIGH (1)** bo'ladi;
- **Tugma bosilgan holatda:** Pin to'g'ridan-to'g'ri GND ga ulanadi -> `digitalRead(2)` natijasi **LOW (0)** bo'ladi.

### 4. Serial Monitor (Ketma-ket port monitoringi)

Serial Monitor — Arduino kompyuterga USB kabel orqali matn va raqamli ko'rsatkichlarni uzatishi hamda ekranda ko'rsatishi uchun xizmat qiluvchi oyna.
1. `Serial.begin(9600);` — ma'lumot uzatish tezligini 9600 bod (baud rate) qilib sozlaydi (`setup()` ichida 1 marta yoziladi);
2. `Serial.println(qiymat);` — qiymatni yangi qatordan ekranga chiqaradi;
3. Tinkercad-da pastki o'ng burchakdagi **"Serial Monitor"** tugmasi bosilsa, terminal oynasi ochiladi.

---

## Amaliy mashg'ulot va topshiriqlar

### 1-topshiriq. Push-button va Arduino sxemasini yig'ish (oson)
Tinkercad ish maydoniga Arduino Uno, Breadboard va 1 ta Push-button joylashtiring.
- Tugmani breadboard markaziy ariqchasi ustiga qo'ying;
- Tugmaning terminal 1a oyog'ini sim orqali Arduino ning `D2` piniga ulang;
- Tugmaning terminal 2a oyog'ini qora sim orqali Arduino ning `GND` piniga ulang.

**Yechim:**
1. Breadboard o'rtasiga Push-button o'rnatiladi.
2. Chap yuqori oyoqdan (Terminal 1a) yashil sim tortilib, Arduino raqamli `2` piniga ulanadi.
3. O'ng yuqori oyoqdan (Terminal 2a) qora sim tortilib, Arduino `GND` piniga ulanadi.
4. Sxema juda ixcham: hech qanday tashqi rezistor talab qilinmaydi (chunki ichki PULLUP ishlatiladi).

### 2-topshiriq. Tugma holatini Serial Monitor orqali kuzatish (o'rta)
Code panelida matnli C++ rejimiga o'ting va quyidagi kodni yozing:
```cpp
const int buttonPin = 2;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  int buttonState = digitalRead(buttonPin);
  Serial.print("Tugma holati: ");
  Serial.println(buttonState);
  delay(200);
}
```
"Start Simulation" tugmasini bosing va pastdagi "Serial Monitor" oynasini oching. Tugma bosilmaganda va bosilganda qanday raqamlar chiqayotganini tahlil qiling.

**Yechim:**
1. Kod simulyatsiyaga kiritilib, ishga tushiriladi.
2. Serial Monitor ochiladi:
   - Tugma bosilmagan holatda har 200 ms da `Tugma holati: 1` yozuvi chiqadi;
   - Sichqoncha bilan tugma bosib turilganda `Tugma holati: 0` yozuvi chiqadi;
   - Qo'yib yuborilganda yana `1` ga qaytadi.
3. Bu tajriba `INPUT_PULLUP` rejimida 0 — bosilgan, 1 — bo'sh ekanligini amalda ko'rsatadi.

### 3-topshiriq. Tugma bosilganda LED yonishi dasturi (qiyin)
Sxemaga bitta qizil LED va 220 Om rezistorni qo'shing (LED anodini 9-pinga, katodini GND ga ulang).
Dasturda shartli operator (`if-else`) qo'llang:
- Agar tugma bosilsa (`buttonState == LOW`), LED yonsin;
- Aks holda (`buttonState == HIGH`), LED o'chsin.

**Yechim:**
```cpp
const int buttonPin = 2;
const int ledPin = 9;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  int buttonState = digitalRead(buttonPin);

  if (buttonState == LOW) { // Tugma bosilganda
    digitalWrite(ledPin, HIGH); // LED yonadi
  } else {                  // Tugma qo'yib yuborilganda
    digitalWrite(ledPin, LOW);  // LED o'chadi
  }
}
```

---

## Tezkor nazorat savollari

1. Push-button nima uchun kirish qurilmasi (Input Device) deb ataladi?
   - *Javob:* Chunki u inson harakatini (bosishini) elektr signaliga aylantirib, mikrokontroller ichiga kiritadi.
2. Nega ochiq qolgan pin "suzuvchi pin" deb ataladi va uning xavfi nimada?
   - *Javob:* U hech qanday kuchlanishga ulanmagani uchun atrofdagi to'lqinlarni qabul qilib, tasodifiy 0 va 1 qiymatlarini qaytaradi va dastur xato ishlaydi.
3. `pinMode(2, INPUT_PULLUP)` ishlatilganda tugma bosilsa qaysi qiymat o'qiladi: 0 mi yoki 1?
   - *Javob:* 0 (LOW), chunki tugma bosilganda pin to'g'ridan-to'g'ri yerga (GND) ulanadi.
4. Serial Monitor bilan aloqa o'rnatish uchun `setup()` da qaysi buyruq yoziladi?
   - *Javob:* `Serial.begin(9600);` (9600 bod tezlikda).

---

## Keng tarqalgan xatolar va ularning oldini olish

- **Oddiy `INPUT` rejimida tortuvchi rezistorni unutish:** Agar `pinMode(2, INPUT)` deb yozilib, tashqi rezistor ulanmasa, tugma qo'yib yuborilganda pin suzuvchi holatda qoladi va LED o'z-o'zidan yonib-o'chib qoladi. Har doim `INPUT_PULLUP` dan foydalanish eng to'g'ri va xavfsiz yo'ldir.
- **Tugmani 90 gradus noto'g'ri o'rnatish:** Push-button kvadrat shaklda bo'lsa-da, uning ichki kontaktlari faqat bitta yo'nalishda ochilib-yopiladi. Agar breadboardga noto'g'ri burib qo'yilsa, kontakt doimiy yopiq bo'lib qolishi mumkin.
