# 16-dars. Mikrokontroller tushunchasi va IoT qurilmalaridagi o'rni (2-qism)

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga mikrokontrollerning IoT qurilmasidagi ikki asosiy rolini (atrof-muhitni sezish va mahalliy boshqaruv; tarmoq bilan ma'lumot almashish), sensor → qayta ishlash → aktuator zanjirini, raqamli va analog signal farqini, ADC va PWM ning vazifasini o'rgatish va Arduino'da oddiy chegara (threshold) dasturini tahlil qildirish.
- **Kutiladigan natija:** O'quvchilar mikrokontrollerning IoT dagi ikki rolini ayta oladi; sensor → CPU → aktuator zanjirini misol bilan tushuntiradi; raqamli va analog signalni farqlaydi, ADC ning vazifasini biladi; aDC qiymatini (0–1023) kuchlanishga (0–5 V) o'giradi; pWM ning nima uchun kerakligini tushuntiradi va chegara dasturini o'qiydi.
- **Vaqt taqsimoti:**
  - 15-dars: CPU, Flash, RAM, portlar: 10 daqiqa
  - IoT'da MCU: sezish, o'ylash, harakat: 10 daqiqa
  - Raqamli va analog signal, ADC: 20 daqiqa
  - PWM va chegara dasturi: 15 daqiqa
  - Amaliyot, xulosa: 25 daqiqa

> Manba: o'quv dasturi — «Mikrokontroller tushunchasi va IoT qurilmalaridagi o'rni»; o'quv qo'llanma — 2.2-bo'lim («IoT qurilmalarida mikrokontrollerning vazifasi va ma'lumot almashishdagi roli», «Sensorlardan ma'lumot olib, aktuatorlarni boshqarish», raqamli va analog signallar, ADC, PWM, «nega sensor to'g'ridan-to'g'ri internetga ulanmaydi», qurilma yaratish bosqichlari); uslubiy ko'rsatma — 2.1-mashg'ulot (Arduino Uno: A0–A5 analog pinlar, 10-bit, 0–1023). Kuchlanish hisobi (5·qiymat/1023) va PWM pinlari (3, 5, 6, 9, 10, 11) standart Arduino hujjatiga ko'ra qo'shildi; kod namunalarining sintaksisi tekshirilgan, Arduino plata/Tinkercad'da ishga tushirilmagan.

---

## Mentor konspekti

### 1. Mikrokontroller IoT qurilmaning «miyasi»

IoT tizimida mikrokontroller shunchaki boshqaruvchi emas — **fizik dunyo bilan raqamli dunyoni bog'lovchi ko'prik**. Qo'llanmaga ko'ra uning **ikki asosiy vazifasi** bor. **1) Sezish va mahalliy boshqaruv:** sensorlardan analog yoki raqamli signal qabul qiladi, uni tushunarli qiymatga (masalan, «25 daraja») aylantiradi (boshlang'ich qayta ishlash) va kerak bo'lsa internetni kutmasdan darhol qaror qiladi — harorat me'yordan oshsa, ventilyatorni yoqadi. **2) Ma'lumot almashish:** qayta ishlangan ma'lumotni Wi-Fi, Bluetooth, GSM, LoRa yoki ZigBee kabi modullar orqali **protokollar** (MQTT, HTTP) bilan bulutga yuboradi; teskari yo'nalishda ham ishlaydi — telefondan kelgan buyruqni qabul qilib, chiroqni yoqadi yoki eshikni qulflaydi. Sensor va motor sodda qurilmalar: ular TCP/IP, MQTT tillarini bilmaydi va ma'lumotni shifrlay olmaydi — shuning uchun ular orasida «tarjimon» — mikrokontroller turadi.

```text
[Sensor] --signal--> [MIKROKONTROLLER] --buyruq--> [Aktuator]
                          |   ^
                  ma'lumot|   |buyruq
                          v   |
                     [Wi-Fi / Bluetooth]
                          |
                       [Bulut] <----> [Telefon]
```

> Professional maslahat: Oddiy qoida: sensor — «quloq», mikrokontroller — «miya», aktuator — «qo'l», Wi-Fi — «ovoz».

### 2. Raqamli va analog signal, ADC

Sensor signalini mikrokontroller ikki usulda qabul qiladi. **Raqamli** signal faqat ikki holatli: «bor» yoki «yo'q» (HIGH/LOW) — masalan, tugma bosildimi. **Analog** signal esa uzluksiz: harorat, namlik, yorug'lik, masofa — aniq va o'zgaruvchan qiymatlar. Mikrokontroller faqat nol va birni tushunadi, shuning uchun ichida **ADC** (Analog-Digital Converter — analog-raqamli o'zgartirgich) bor: u kuchlanishni songa aylantiradi. Arduino Uno'da **A0–A5** analog kirish pinlari kuchlanishni **10-bit** aniqlikda o'qiydi — qiymat **0 dan 1023 gacha** (0 V → 0, 5 V → 1023). Kuchlanishni topish formulasi: **U = 5 × qiymat / 1023**. Masalan, qiymat 512 bo'lsa, U ≈ 2,5 V. ESP32 da ADC o'lchamlari va kuchlanish diapazoni boshqacha (3,3 V) — ESP bilan ishlaganda hujjatga qarang.

```text
Arduino Uno: 10-bit ADC, 5 V

qiymat    kuchlanish (U = 5 * qiymat / 1023)
   0      0.00 V
 256      1.25 V
 512      2.50 V
 768      3.75 V
1023      5.00 V
```

> Professional maslahat: Formulani yodlash shart emas: «5 V ni 1023 ga bo'ldik» — har birlik ≈ 0,0049 V (taxminan 4,9 mV).

### 3. PWM va chegara (threshold) dasturi

Aktuator ba'zan faqat yoqilishi/o'chirilishi yetarli (rele, chiroq). Lekin LEDni **xira** yoqish yoki motorni **sekin** aylantirish kerak bo'lsa, **PWM** (Pulse Width Modulation — kenglik-impulsli modulyatsiya) ishlatiladi: pin tez-tez yoqilib-o'chadi, yoqilgan vaqt ulushi (to'ldirish) o'zgaradi. Arduino'da `analogWrite(pin, 0..255)`: 0 — doim o'chiq, 255 — doim yoqiq, 128 ≈ 50% yorqinlik. Uno'da PWM pinlar `~` bilan belgilangan: 3, 5, 6, 9, 10, 11. Quyidagi dastur sensor qiymatini o'qiydi va **chegaradan** oshsa LEDni yoqadi — bu «sezish → o'ylash → harakat» zanjirining eng sodda ko'rinishi. Dastur yozish, kompilyatsiya va USB orqali yuklash — Flash xotiraga «muhrlanadi», qurilma yoqilganda avtomatik ishga tushadi.

```cpp
const int SENSOR = A0;     // analog kirish
const int LED = 9;         // chiqish (PWM pin)
const int CHEGARA = 512;   // ~2,5 V

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int qiymat = analogRead(SENSOR);   // 0..1023
  Serial.println(qiymat);
  if (qiymat > CHEGARA) {
    analogWrite(LED, 255);           // to'liq yorqin
  } else {
    analogWrite(LED, 40);            // xira
  }
  delay(200);
}
```

> Professional maslahat: Chegarani o'zgartirib ko'ring: 300, 700. Serial Monitor'da qiymat o'zgarishini kuzating — shunda sensor «tilini» tushunasiz.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Rolni toping (oson)
Mikrokontrollerning IoT dagi ikki vazifasini yozing.

**Yechim:** 1) Sezish va mahalliy boshqaruv: sensor signalini olib qayta ishlaydi va aktuatorga buyruq beradi. 2) Ma'lumot almashish: Wi-Fi, Bluetooth va protokollar (MQTT, HTTP) orqali bulut bilan aloqa qiladi.

### 2-topshiriq. Signal turi (oson)
Tugma, harorat sensori, yorug'lik sensori, masofa sensori — qaysi biri raqamli, qaysi biri analog?

**Yechim:** Tugma — raqamli (bosildi/bosilmadi). Harorat, yorug'lik va masofa — analog (uzluksiz qiymat, ADC orqali o'qiladi).

### 3-topshiriq. Kuchlanish (o'rta)
ADC qiymati 256 va 768 bo'lsa, kuchlanish qancha? (U = 5 × qiymat / 1023)

**Yechim:** 5 × 256 / 1023 ≈ 1,25 V; 5 × 768 / 1023 ≈ 3,75 V.

### 4-topshiriq. PWM hisobi (o'rta)
analogWrite(LED, 64) taxminan necha foiz yorqinlik beradi?

**Yechim:** 64 / 255 ≈ 0,25 → taxminan 25%.

### 5-topshiriq. Chegara dasturi (qiyin)
Qiymat 700 dan oshsa LED yonsin, aks holda o'chsin. Dasturning loop() qismini yozing.

**Yechim:**
```cpp
int qiymat = analogRead(A0);
if (qiymat > 700) {
  digitalWrite(9, HIGH);
} else {
  digitalWrite(9, LOW);
}
delay(200);
```

### 6-topshiriq. Tarjimon (bonus)
Nega sensor to'g'ridan-to'g'ri internetga ulanmaydi? Mikrokontroller qanday yordam beradi?

**Yechim:** Sensor sodda qurilma: TCP/IP va MQTT protokollarini bilmaydi, ma'lumotni shifrlay olmaydi. Mikrokontroller signalni qiymatga aylantiradi, tartibga solib paketlaydi va Wi-Fi moduli orqali xavfsiz yuboradi.

---

## Tezkor nazorat savollari

1. Mikrokontrollerning IoT dagi ikki vazifasi?
   - *Javob:* Sezish va mahalliy boshqaruv; ma'lumot almashish.
2. Raqamli va analog signal farqi?
   - *Javob:* Raqamli — ikki holat (HIGH/LOW); analog — uzluksiz qiymat.
3. ADC nima qiladi?
   - *Javob:* Analog kuchlanishni raqamli songa (Uno'da 0–1023) aylantiradi.
4. PWM nima uchun kerak?
   - *Javob:* LED yorqinligini yoki motor tezligini silliq boshqarish uchun.
5. Dastur qayerga yuklanadi?
   - *Javob:* Flash xotiraga; tok o'chganda ham saqlanadi.

---

## Uyga vazifa

1. Mikrokontrollerning IoT dagi ikki vazifasini misollar bilan 5–6 gapda yozing.
2. ADC qiymatlari 100, 400, 900 uchun kuchlanishni hisoblang (U = 5 × qiymat / 1023).
3. Chegara dasturini o'zgartiring: qiymat 800 dan oshsa LED to'liq yonsin, aks holda o'chsin; kodni daftaringizga yozing.
4. Sensor → mikrokontroller → aktuator → bulut zanjiri uchun o'z misolingizni (masalan, aqlli sug'orish) chizing.
