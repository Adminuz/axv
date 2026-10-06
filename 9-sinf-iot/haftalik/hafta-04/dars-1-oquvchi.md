# 10-dars. Arduino UNO va tugma orqali LED holatini boshqarish dasturi

> Fonarni bir bosishda yoqasiz, ikkinchi bosishda u miltillay boshlaydi, uchinchisida tez miltillaydi. Bitta tugma — bir nechta rejim. Bugun shunday «aqlli» boshqaruv dasturini yozamiz.

## Dars xulosasi

- **Holat (state)** — LED yoki qurilmaning ayni paytdagi vaziyati (yoniq/o'chiq, rejim raqami). U o'zgaruvchida saqlanadi va faqat **hodisa** — tugma bosilgan lahzada o'zgaradi.
- `INPUT_PULLUP` da tugma bosilmaganda `HIGH`, bosilganda `LOW` o'qiladi.
- `#define Pressed LOW` va `const byte LED = 9;` — kodni o'qiluvchan qiladi, «sehrli sonlar» yo'qoladi.
- **Yordamchi funksiya** `checkSwitch(pin, lastState)` bosilgan lahzani topadi; `&` belgisi o'zgaruvchining o'zini o'zgartirish imkonini beradi.
- `delay()` dasturni to'xtatadi; `millis()` bilan esa bir vaqtda ham miltillash, ham tugmani kuzatish mumkin.
- **Heartbeat LED** (13-pin, 700 ms) — dastur ishlab turganining belgisi.
- `mode = (mode + 1) % 4;` va `switch/case` — bitta tugma bilan 4 ta rejim.
- Serial Monitor'ga faqat **holat o'zgarganda** yozing.

## Qo'shimcha ma'lumot

### 1. Kirish, hodisa, holat, chiqish

| Tushuncha | Misol |
|---|---|
| Kirish | `digitalRead(2)` — tugma signali |
| Hodisa | `HIGH → LOW` o'tishi (bosildi) |
| Holat | `ledState`, `mode` |
| Chiqish | `digitalWrite(9, HIGH)` — LED |

### 2. `millis()` andozasi

```cpp
unsigned long oxirgi = 0;
void loop() {
  if (millis() - oxirgi >= 500) {   // 500 ms o'tdimi?
    oxirgi = millis();
    // shu yerda ish bajariladi
  }
  // boshqa ishlar to'xtovsiz davom etadi
}
```

Vaqt o'zgaruvchilari har doim `unsigned long` bo'lsin.

### 3. 4 rejimli chiroq

| `mode` | Rejim | LED |
|---|---|---|
| 0 | O'CHIQ | o'chiq |
| 1 | YONIQ | yoniq |
| 2 | SEKIN | 500 ms da almashadi |
| 3 | TEZ | 100 ms da almashadi |

### 4. Debounce `millis()` bilan

Tugmani har 50 ms da bir marta tekshirish kifoya: kontakt dirillashi 5–20 ms davom etadi, shuning uchun soxta impulslar o'tkazib yuboriladi va `delay(50)` kerak bo'lmaydi.

### 5. Odatiy xatolar

- `byte &lastState` o'rniga `byte lastState` — holat saqlanmaydi.
- `int` da `millis()` ni saqlash — 33 soniyadan keyin manfiy bo'ladi.
- `% 4` ni unutish — rejim 4, 5, 6... bo'lib, `switch` ishlamaydi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Holat (state)** | Qurilmaning ayni paytdagi vaziyati, o'zgaruvchida saqlanadi |
| **Hodisa (event)** | Holatni o'zgartiruvchi lahza, masalan tugma bosilishi |
| **`#define`** | Kompilyatsiyadan oldin nomni qiymat bilan almashtiruvchi buyruq |
| **`const byte`** | O'zgarmas, 0–255 oralig'idagi 1 baytli son |
| **Havola (`&`)** | Funksiyaga o'zgaruvchining nusxasi emas, o'zini uzatish |
| **`millis()`** | Plata yoqilgandan beri o'tgan millisekundlar |
| **Bloklamaydigan kod** | `delay()` siz, `loop()` ni to'xtatmaydigan dastur |
| **Heartbeat LED** | Dastur ishlayotganini ko'rsatuvchi miltillovchi LED |
| **Rejim (mode)** | Qurilmaning tanlangan ish tartibi |
| **Holat mashinasi** | Holatlar va ular orasidagi o'tishlar bilan ishlovchi dastur |
| **`%` (qoldiq)** | Bo'linmaning qoldig'i: `5 % 4 = 1` |

## Bilasizmi?

- Kir yuvish mashinasi, mikroto'lqinli pech va svetoforlar aynan holat mashinasi tamoyilida ishlaydi: har bir tugma yoki taymer bir holatdan ikkinchisiga o'tkazadi.
- `millis()` qiymati taxminan 49,7 kunda to'lib, yana 0 dan boshlanadi. `millis() - oxirgi >= interval` usuli shu o'tishda ham to'g'ri ishlaydi.
- Arduino UNO sekundiga 16 million amal bajaradi — `delay(1000)` paytida u shuncha amalni «bekorga» kutib o'tkazadi.
- Ko'pchilik velosiped fonarlari bitta tugma bilan 3–5 rejimni (doimiy, sekin, tez, «strob») aylantiradi.

## Topshiriqlar

### 1. Kirish yoki holat? · oson
Quyidagilarni «kirish», «hodisa», «holat», «chiqish» ga ajrating: `digitalRead(2)`, `mode = 2`, `digitalWrite(9, HIGH)`, tugma bosilgan lahza, `ledState`.

**Kutiladigan natija:** 5 ta to'g'ri ajratilgan element.

### 2. Nomli konstantalar · oson
Ushbu kodni `#define` va `const byte` bilan qayta yozing: `pinMode(2, INPUT_PULLUP); if (digitalRead(2) == LOW) digitalWrite(9, HIGH);`

**Kutiladigan natija:** `BTN`, `LED`, `Pressed` nomlari bilan o'qiluvchan kod.

### 3. Qoldiq amali · oson
`mode = (mode + 1) % 4;` 0 dan boshlab 6 marta bajarilsa, `mode` qaysi qiymatlarni oladi? `% 3` bo'lsa-chi?

**Kutiladigan natija:** 1, 2, 3, 0, 1, 2 va 1, 2, 0, 1, 2, 0.

### 4. Ikki LED almashib · oson
Bitta tugma (Pin 2) bilan Qizil (Pin 9) va Yashil (Pin 10) LEDlarni almashib yoqing: har bosishda yonib turgani o'chib, ikkinchisi yonsin.

**Kutiladigan natija:** Tinkercad'da ishlaydigan sxema va kod.

### 5. Heartbeat · o'rta
Pin 13 dagi LED `millis()` yordamida har 700 ms da miltillasin. `delay()` ishlatmang.

**Kutiladigan natija:** bir tekis miltillovchi LED va kod.

### 6. Heartbeat + Toggle · o'rta
5-topshiriqqa tugma (Pin 2) va LED (Pin 9) qo'shing: tugma LEDni Toggle qilsin, heartbeat esa to'xtamasin. `checkSwitch()` funksiyasini yozing.

**Kutiladigan natija:** ikkala ish bir vaqtda bajariladi.

### 7. 4 rejimli chiroq · o'rta
Bitta tugma bilan O'CHIQ → YONIQ → SEKIN → TEZ rejimlarini aylantiring. Rejim nomi Serial Monitor'da chiqsin.

**Kutiladigan natija:** `switch/case` li kod va Serial'da `Rejim: TEZ` kabi yozuvlar.

### 8. `&` tajribasi · o'rta
`checkSwitch()` dagi `&` belgisini olib tashlang va tugmani bosib turing. Nima bo'ldi? Nega?

**Kutiladigan natija:** kuzatuv va 2–3 jumlali tushuntirish.

### 9. Uslubiy qo'llanma sxemasi · qiyin
3 tugma (7, 8, 9), 3 LED (10, 11, 12) va heartbeat (13) sxemasini yig'ing va qo'llanmadagi dasturni ishga tushiring. Har bir tugma qaysi LEDlarni almashtirishini jadvalga yozing.

**Kutiladigan natija:** ishlaydigan sxema va 3 qatorli jadval.

### 10. Reset tugmasi · qiyin
9-topshiriqda 3-tugma hamma LEDni o'chirsin; har o'zgarishdan keyin Serial'ga `LED: 1 0 1` ko'rinishida holat chiqsin.

**Kutiladigan natija:** massiv va `for` sikli ishlatilgan kod.

### 11. Uzoq bosish · qiyin
Tugma 1 soniyadan uzoq bosib turilsa, rejim darhol 0 ga (O'CHIQ) qaytsin; qisqa bosish esa rejimni oshirsin.

**Kutiladigan natija:** `millis()` bilan bosish davomiyligini o'lchovchi kod.

### 12. Aqlli tungi chiroq · bonus
Ikki tugma: biri rejimni oshiradi, ikkinchisi kamaytiradi (3 → 2 → 1 → 0, 0 dan pastga tushmaydi). Rejimlar: 0 — o'chiq, 1 — xira (`analogWrite(9, 60)`), 2 — o'rtacha (150), 3 — to'liq (255).

**Kutiladigan natija:** PWM pin (9) da 4 darajali yorqinlik va Serial'da daraja raqami.

## O'zingizni tekshiring

1. Holat va kirish signali o'rtasidagi farq nima?
2. `#define Pressed LOW` dasturga qanday foyda beradi?
3. `checkSwitch()` funksiyasida `&` nima uchun kerak?
4. Nega miltillash bilan birga tugma kuzatiladigan dasturda `delay()` ishlatilmaydi?
5. `millis()` qiymatini qaysi turdagi o'zgaruvchida saqlash kerak va nima uchun?
6. Heartbeat LED nimani ko'rsatadi?
7. `mode = (mode + 1) % 4;` qanday ishlaydi?

## Uyga vazifa

Bitta tugma va bitta LED bilan 4 rejimli chiroq dasturini `millis()` asosida yozing, rejim o'zgarganda Serial Monitor'ga nomini chiqaring va Tinkercad havolasi yoki skrinshotini topshiring. Batafsil: `uyga-vazifa.md`.
