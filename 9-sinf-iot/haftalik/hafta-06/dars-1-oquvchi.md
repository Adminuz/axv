# 16-dars. Mikrokontroller tushunchasi va IoT qurilmalaridagi o'rni (2-qism)

> Mikrokontroller sezadi, o'ylaydi va harakat qiladi. Bugun bu zanjirni sensor, ADC va PWM misolida ko'ramiz va IoT dagi o'rnini aniqlaymiz.

## Dars xulosasi

- Mikrokontroller — IoT qurilmaning miyasi va tarjimoni.
- Zanjir: sensor → mikrokontroller → aktuator.
- Raqamli signal — ikki holat, analog — uzluksiz.
- ADC analogni raqamga aylantiradi: Uno'da 0–1023.
- PWM yorqinlik va tezlikni boshqaradi: `analogWrite(0..255)`.
- Dastur Flash xotiraga yuklanadi va tok o'chganda saqlanadi.

## Qo'shimcha ma'lumot

### MQTT
IoT uchun yengil protokol: broker orqali xabar almashish.

### Sensor kalibrovkasi
Sensor qiymatini haqiqiy kattalikka moslash.

### Debounce
Tugma «titrashi»ni dasturda bartaraf etish.

### Interrupt
Muhim hodisaga darhol javob berish mexanizmi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Sensor | Atrof-muhitni sezuvchi qurilma |
| Aktuator | Ijrochi qurilma |
| ADC | Analog-raqamli o'zgartirgich |
| PWM | Kenglik-impulsli modulyatsiya |
| HIGH/LOW | Yuqori/past signal |
| Protokol | Ma'lumot almashish qoidasi |
| Bulut | Internetdagi server xizmati |
| Chegara | Qaror qabul qilish qiymati |

## Bilasizmi?

- Arduino Uno ADC dagi 1 birlik ≈ 4,9 mV ga teng.
- Ko'p IoT qurilmalari ko'p vaqtini «uyquda» o'tkazadi — batareya yillab chidashi uchun.
- Aktuator so'zi lotincha «actus» — harakat so'zidan kelib chiqqan.

## Topshiriqlar

### 1. Zanjir · oson

Sensor → mikrokontroller → aktuator zanjiriga 2 ta misol keltiring.

**Kutiladigan natija:** Tugma→LED; harorat→ventilyator

### 2. Signal · oson

Raqamli signal nima?

**Kutiladigan natija:** Ikki holat

### 3. ADC · oson

ADC ning to'liq nomi va vazifasini yozing.

**Kutiladigan natija:** Analog-raqamli o'zgartirgich

### 4. Aktuator · oson

3 ta aktuator nomini yozing.

**Kutiladigan natija:** LED, motor, rele

### 5. Kuchlanish · o'rta

Qiymat 512 bo'lsa, kuchlanish qancha?

**Kutiladigan natija:** ≈ 2,5 V

### 6. PWM · o'rta

analogWrite(pin, 255) va 0 nimani bildiradi?

**Kutiladigan natija:** To'liq yoqiq va o'chiq

### 7. Chegara · o'rta

Chegara dasturining mantig'ini so'z bilan yozing.

**Kutiladigan natija:** Qiymat > chegara bo'lsa yoq

### 8. Rollar · o'rta

IoT'da MCU ning ikki rolini misol bilan yozing.

**Kutiladigan natija:** Sezish va aloqa

### 9. Dastur · qiyin

Qiymat 300 dan kam bo'lsa LED yonsin: loop() yozing.

**Kutiladigan natija:** analogRead < 300

### 10. Tahlil · qiyin

Nega ADC qiymati 0–1023, 1024 ta daraja?

**Kutiladigan natija:** 10 bit = 2^10

### 11. PWM pinlar · qiyin

Uno'da qaysi pinlar PWM qo'llaydi?

**Kutiladigan natija:** 3, 5, 6, 9, 10, 11

### 12. Loyiha g'oyasi · bonus

Sensor + aktuator + Wi-Fi bilan o'z IoT g'oyangizni yozing.

**Kutiladigan natija:** Mustaqil g'oya

## O'zingizni tekshiring

1. MCU ning ikki roli?
2. Raqamli va analog farqi?
3. ADC nima?
4. Kuchlanish formulasi?
5. PWM nima uchun?
6. Dastur qayerda saqlanadi?

## Uyga vazifa

Sensor, ADC va PWM bo'yicha masalalarni yeching (30–40 daqiqa). To'liq shart: `uyga-vazifa.md`.
