# 18-dars. Arduino Uno va Tinkercad asosida svetofor tizimini modellashtirish (1-qism)

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga svetofor ishlash algoritmini, LED va tokni cheklovchi rezistorning vazifasini (Om qonuni), Arduino Uno pinlariga LEDlarni ulash tartibini, Tinkercad'da sxema yig'ishni hamda `pinMode`, `digitalWrite`, `delay` yordamida ketma-ket ishlaydigan svetofor dasturini yozishni o'rgatish.
- **Kutiladigan natija:** O'quvchilar svetofor algoritmini (qizil, sariq, yashil, vaqtlar) tavsiflaydi; lED va rezistor vazifasini, anod va katodni farqlaydi; tinkercad'da Arduino Uno, 3 ta LED va 3 ta rezistorli sxemani yig'adi; `setup()` va `loop()` ichida svetofor dasturini yozadi va tushuntiradi; simulyatsiyani ishga tushirib, natijani tahlil qiladi va xatoni topadi.
- **Vaqt taqsimoti:**
  - 16-dars: sensor, aktuator, PWM: 10 daqiqa
  - Svetofor algoritmi, LED va rezistor: 10 daqiqa
  - Tinkercad'da sxema yig'ish: 20 daqiqa
  - Dastur: setup, loop, delay: 15 daqiqa
  - Simulyatsiya, tahlil, xulosa: 25 daqiqa

> Manba: o'quv dasturi — «Arduino Uno va Tinkercad virtual laboratoriyasi asosida ketma-ket ishlaydigan svetofor tizimini modellashtirish» (svetofor algoritmi, LED chiroqlarni ketma-ket boshqarish, Tinkercad'da sxema yig'ish, vaqt intervallarini sozlash); uslubiy ko'rsatma — 2.1-mashg'ulot (kerakli vositalar, ishning bajarish tartibi, LED va rezistor qoidalari: 220–330 Ω, anod → pin, katod → GND; pinlar 9, 8, 7; qizil 5 s, sariq 2 s, yashil 5 s). Rezistor hisobi (Om qonuni, LED ~2 V) standart elektronika bilimiga ko'ra qo'shildi. Kodning sintaksisi tekshirilgan; Tinkercad'da mentor simulyatsiyani oldindan sinab ko'rishi tavsiya etiladi.

---

## Mentor konspekti

### 1. Svetofor algoritmi, LED va rezistor

**Svetofor** — chiroqlar ketma-ket yonib-o'chadigan tizim. Uslubiy ko'rsatmadagi algoritm: **qizil LED 5 soniya** yonadi va o'chadi → **sariq 2 soniya** → **yashil 5 soniya** → sikl doimiy takrorlanadi (bir sikl = 12 soniya). Uch aktuator — uch LED, har biri Arduino'ning bitta raqamli chiqish pinida. **LED** — tok o'tganda yorug'lik chiqaradigan diod: **anod (+)** pinga/musbatga, **katod (−)** GND ga ulanadi; teskari ulansa ishlamaydi. LED **rezistor** orqali ulanadi (220–330 Ω), aks holda ortiqcha tok uni tezda ishdan chiqaradi. Rezistor hisobi **Om qonuni** bilan: **R = (U − U_LED) / I**. Namuna: pin 5 V, qizil LED ≈ 2 V, tok ≈ 14 mA bo'lsa, R = (5 − 2) / 0,014 ≈ 215 Ω — shuning uchun 220 Ω. LED turiga qarab U_LED farq qiladi (qizil ≈ 2 V, yashil va ko'k odatda balandroq) — shuning uchun 220–330 Ω keng qo'llanadi.

```text
Om qonuni:  R = (U - U_LED) / I

U = 5 V (Arduino pini)
U_LED ~ 2 V (qizil)
I ~ 14 mA = 0.014 A

R = (5 - 2) / 0.014 ~ 214 Ohm  ->  220 Ohm

Tekshiruv: I = (5 - 2) / 220 ~ 0.0136 A (13.6 mA)
```

> Professional maslahat: Qoida: LED hech qachon rezistorsiz ulanmaydi. Tinkercad'da ham rezistorsiz LED «kuyishi» mumkin — bu ham o'rganish.

### 2. Tinkercad'da svetofor sxemasini yig'ish

Tartib (uslubiy ko'rsatma): 1) **tinkercad.com** ga kiring, akkaunt orqali tizimga ulaning; **Circuits → Create new Circuit**. 2) Komponentlar ro'yxatidan **Arduino Uno** ni ish maydoniga qo'ying. 3) **Uchta LED** (qizil, sariq, yashil) tanlang; har birini **rezistor (220 Ω)** orqali Arduino'ning raqamli chiqish pinlariga ulang: qizil — 9-pin, sariq — 8-pin, yashil — 7-pin. 4) LEDlarning **katodlarini GND** ga ulang. 5) Sxemani tekshiring: ulanishlar to'g'rimi, qisqa tutashuv yo'qmi, har LED o'z rezistoriga ulanganmi. Breadboard'da bitta umumiy GND qatori (manfiy chiziq) ishlatish qulay: Arduino GND → breadboard manfiy qator → har LED katodi. Rezistor LEDning anodi tomonida yoki katodi tomonida bo'lishi mumkin — ikkalasi ham to'g'ri ishlaydi, asosiysi — zanjirda bo'lishi.

```text
Arduino 9  --[220 Ohm]--> (+) QIZIL LED (-) --+
Arduino 8  --[220 Ohm]--> (+) SARIQ LED (-) --+--> GND
Arduino 7  --[220 Ohm]--> (+) YASHIL LED (-)--+

(+) = anod (uzun oyoq),  (-) = katod (qisqa oyoq)
```

> Professional maslahat: LED oyoqlarini farqlash: uzun oyoq — anod (+), qisqa oyoq — katod (−). Tinkercad'da LED ustiga sichqoncha olib borilsa, oyoqlar nomi ko'rinadi.

### 3. Svetofor dasturi: setup, loop, delay

Tinkercad'da **Code** bo'limiga o'tib, Arduino C/C++ dasturini yozamiz. **O'zgaruvchilar** pin raqamlarini nomlaydi: `red = 9`, `yellow = 8`, `green = 7` — kod o'qilishi oson, pin o'zgarsa bitta joyda tuzatiladi. **`setup()`** dastur ishga tushganda **bir marta** bajariladi: `pinMode(pin, OUTPUT)` har LED pinini chiqish qiladi. **`loop()`** **doimiy takrorlanadi** — svetofor to'xtamaydi. `digitalWrite(pin, 1)` (HIGH) — LEDni yoqadi, `0` (LOW) — o'chiradi. **`delay(ms)`** millisekund kutadi: 5000 ms = 5 s. Tartib: qizil yoq → 5 s → o'chir → sariq yoq → 2 s → o'chir → yashil yoq → 5 s → o'chir. Keyin **Start Simulation** bosiladi — LEDlar ketma-ket yonishi real vaqtda kuzatiladi. Tahlil: ketma-ketlik va vaqtlar to'g'rimi, LEDlar mantiqan almashyaptimi; xato bo'lsa, kod yoki sxema qayta tekshiriladi.

```cpp
int red = 9;
int yellow = 8;
int green = 7;

void setup() {
  pinMode(red, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(green, OUTPUT);
}

void loop() {
  digitalWrite(red, 1);
  delay(5000);
  digitalWrite(red, 0);
  digitalWrite(yellow, 1);
  delay(2000);
  digitalWrite(yellow, 0);
  digitalWrite(green, 1);
  delay(5000);
  digitalWrite(green, 0);
}
```

> Professional maslahat: Eslatma: `delay()` davomida Arduino boshqa ish qilmaydi — bu 19–20-darslarda kodni optimallashtirishda muhim mavzu bo'ladi.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Sikl vaqti (oson)
Svetofor sikli necha soniya davom etadi (5 s + 2 s + 5 s)?

**Yechim:** 5 + 2 + 5 = 12 soniya.

### 2-topshiriq. Ulanish (oson)
Qizil LED qaysi pinga va qanday ulanadi?

**Yechim:** 9-pin → 220 Ω rezistor → qizil LEDning anodi; katod → GND.

### 3-topshiriq. Rezistor (o'rta)
Pin 5 V, LED 2 V, tok 20 mA bo'lsa, rezistor qancha bo'lishi kerak? Standart qiymatdan qaysi biri mos?

**Yechim:** R = (5 − 2) / 0,02 = 150 Ω. Standart qatordan 150 Ω yoki biroz kattaroq (220 Ω) tanlanadi; 220 Ω da tok ≈ 13,6 mA — xavfsizroq.

### 4-topshiriq. Dasturni o'qing (o'rta)
`digitalWrite(yellow, 1); delay(2000); digitalWrite(yellow, 0);` nima qiladi?

**Yechim:** Sariq LEDni yoqadi, 2 soniya kutadi va o'chiradi.

### 5-topshiriq. Vaqtni o'zgartiring (qiyin)
Yashil 8 soniya, qizil 6 soniya bo'lishi uchun loop() ni yozing; sariq 2 soniya qolsin.

**Yechim:**
```cpp
void loop() {
  digitalWrite(red, 1);
  delay(6000);
  digitalWrite(red, 0);
  digitalWrite(yellow, 1);
  delay(2000);
  digitalWrite(yellow, 0);
  digitalWrite(green, 1);
  delay(8000);
  digitalWrite(green, 0);
}
```

### 6-topshiriq. Haqiqiy tartib (bonus)
Haqiqiy svetoforda tartib: qizil → yashil → sariq → qizil. loop() ni shunday qayta yozing.

**Yechim:**
```cpp
void loop() {
  digitalWrite(red, 1);
  delay(5000);
  digitalWrite(red, 0);
  digitalWrite(green, 1);
  delay(5000);
  digitalWrite(green, 0);
  digitalWrite(yellow, 1);
  delay(2000);
  digitalWrite(yellow, 0);
}
```

---

## Tezkor nazorat savollari

1. Svetofor algoritmini ayting.
   - *Javob:* Qizil 5 s → sariq 2 s → yashil 5 s → takrorlash.
2. LED nima uchun rezistor orqali ulanadi?
   - *Javob:* Tokni cheklab, LEDni ishdan chiqishdan saqlaydi.
3. `setup()` va `loop()` farqi?
   - *Javob:* setup — bir marta, loop — doimiy takrorlanadi.
4. `delay(2000)` nima qiladi?
   - *Javob:* 2 soniya kutadi.
5. LEDning anodi va katodi qayerga ulanadi?
   - *Javob:* Anod — pinga (rezistor orqali), katod — GND ga.

---

## Uyga vazifa

1. Tinkercad'da svetofor sxemasini yig'ing (9, 8, 7 pinlar), dasturni yozing va ekran suratini saqlang.
2. Qizil 6 s, sariq 2 s, yashil 8 s bo'ladigan variantni yozing; bir sikl necha soniyani olishini hisoblang.
3. 220 Ω va 330 Ω rezistorlar uchun LED tokini hisoblang (U = 5 V, U_LED = 2 V): I = (5 − 2) / R.
4. Dasturning har bir qatorini o'z so'zlaringiz bilan izohlang (komment sifatida).
5. Real svetofor tartibiga (qizil → yashil → sariq) mos variantni yozing.
