# 12-dars. Breadboardda DIP switch (DPST) va LED: oddiy elektron sikl (2-qism)

> Sanoat pressi ishchi ikkala qo'li bilan ikki tugmani bosgandagina ishlaydi, avtobusdagi «to'xtash» chirog'i esa istalgan tugmadan yonadi. Bu «VA» va «YOKI» mantig'i — bugun uni ikki kalit bilan yig'amiz va DIP switch'ni Arduino'ga ulaymiz.

## Dars xulosasi

- **Ketma-ket** ulangan ikki kalit — **VA (AND):** LED faqat ikkalasi ON bo'lganda yonadi.
- **Parallel** ulangan ikki kalit — **YOKI (OR):** kamida bittasi ON bo'lsa LED yonadi.
- **Multimetr:** kuchlanish — parallel ulanadi; tok — zanjirni uzib, ketma-ket ulanadi.
- Rezistor oshsa — tok kamayadi — LED xiralashadi: 220 Om ≈ 13,6 mA, 330 Om ≈ 9 mA, 1000 Om ≈ 3 mA (5 V, qizil LED).
- **Nosozlikni izlash** — tok yo'li bo'yicha manbadan GND gacha 6 qadam.
- DIP switch Arduino'ga ulansa, u **kirish** bo'ladi: `INPUT_PULLUP` da ON = `LOW`.
- Ikki kalit = **2 bit** = 4 kombinatsiya (0–3): `kod = bit1 × 2 + bit0`.

## Qo'shimcha ma'lumot

### 1. Haqiqat jadvallari

| DIP1 | DIP2 | AND (ketma-ket) | OR (parallel) |
|---|---|---|---|
| OFF | OFF | o'chiq | o'chiq |
| ON | OFF | o'chiq | yoniq |
| OFF | ON | o'chiq | yoniq |
| ON | ON | yoniq | yoniq |

### 2. Sxemalar

```
AND:  + → DIP1 → DIP2 → 330 Om → LED → GND

OR:   + → DIP1 ┐
      + → DIP2 ┴→ umumiy qator → 330 Om → LED → GND
```

### 3. Multimetr o'lchovlari (5 V, qizil LED, 330 Om)

| Nimani | Natija |
|---|---|
| Manba | ≈ 5 V |
| Rezistor | ≈ 3 V |
| LED | ≈ 2 V |
| Tok | ≈ 9 mA |

3 V + 2 V = 5 V — kuchlanishlar yig'indisi manbaga teng.

### 4. Nosozlikni izlash ro'yxati

1. Manbada 5 V bormi?
2. Simlar to'g'ri relslardami?
3. DIP ariqcha ustida va ON holatdami?
4. Rezistor oyoqlari turli qatorlardami?
5. LED anodi `+` tomondami?
6. Katoddan GND gacha sim bormi?

### 5. DIP switch → Arduino

| DIP1 | DIP2 | kod | rejim |
|---|---|---|---|
| OFF | OFF | 0 | o'chiq |
| OFF | ON | 1 | Yashil |
| ON | OFF | 2 | Qizil |
| ON | ON | 3 | miltillash |

```cpp
byte bit1 = (digitalRead(2) == LOW) ? 1 : 0;
byte bit0 = (digitalRead(3) == LOW) ? 1 : 0;
byte kod = bit1 * 2 + bit0;
```

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Ketma-ket ulanish** | Komponentlar bitta yo'lda birin-ketin |
| **Parallel ulanish** | Komponentlar alohida yo'llarda, uchlari umumiy |
| **AND (VA)** | Natija faqat barcha shartlar bajarilganda |
| **OR (YOKI)** | Natija kamida bitta shart bajarilganda |
| **Haqiqat jadvali** | Barcha kirish kombinatsiyalari va natijalar jadvali |
| **Multimetr** | Kuchlanish, tok va qarshilikni o'lchovchi asbob |
| **Nosozlikni izlash (troubleshooting)** | Xatoni bosqichma-bosqich topish usuli |
| **Bit** | Ikkilik raqam: 0 yoki 1 |
| **Ikkilik kod** | Bitlardan tuzilgan son: `10` = 2 |
| **`INPUT_PULLUP`** | Pinni ichki rezistor bilan `HIGH` ga tortish rejimi |

## Bilasizmi?

- Kompyuter protsessoridagi milliardlab tranzistorlar aynan AND, OR, NOT kabi mantiqiy elementlar sifatida ishlaydi — siz bugun ularning «qo'lda» versiyasini yig'dingiz.
- Mantiqiy algebrani XIX asrda ingliz matematigi Jorj Bul ishlab chiqqan, shuning uchun dasturlashdagi `bool` turi uning nomi bilan atalgan.
- 8 pozitsiyali DIP switch 2⁸ = 256 xil kod beradi — eski televizor pultlari va garaj eshiklari shu usulda «o'z» qurilmasini tanigan.
- Multimetr tok rejimida deyarli nol qarshilikka ega — shuning uchun uni manbaga parallel ulash qisqa tutashuvga olib keladi.

## Topshiriqlar

### 1. AND yoki OR? · oson
Hayotdan 4 ta misolni ajrating: lift (eshik yopiq VA tugma bosilgan), uy qo'ng'irog'i (old YOKI orqa eshik), seyf (kalit VA kod), xona chirog'i (ikki kalitdan istalgani).

**Kutiladigan natija:** 4 ta javob.

### 2. AND zanjiri · oson
Tinkercad'da DIP1 va DIP2 ni ketma-ket ulab, LED faqat ikkalasi ON bo'lganda yonishini ko'rsating.

**Kutiladigan natija:** sxema va 4 qatorli haqiqat jadvali.

### 3. OR zanjiri · oson
Endi kontaktlarni parallel ulang: istalgan richag LEDni yoqsin.

**Kutiladigan natija:** sxema va haqiqat jadvali.

### 4. Farqni tushuntiring · oson
AND sxemasini OR ga aylantirish uchun qaysi simni olib tashlash va qaysilarini qo'shish kerak?

**Kutiladigan natija:** 2–3 jumlali tushuntirish.

### 5. Kuchlanishlarni o'lchang · o'rta
Multimetr bilan manba, rezistor va LED dagi kuchlanishni o'lchang. Yig'indini tekshiring.

**Kutiladigan natija:** 3 ta o'lchov va `U = U1 + U2` tekshiruvi.

### 6. Tokni o'lchang · o'rta
Zanjirni uzib, multimetrni tok rejimida ketma-ket ulang. 330 Om da tok qancha?

**Kutiladigan natija:** ≈ 9 mA va ulanish skrinshoti.

### 7. Rezistor tajribasi · o'rta
220, 330, 1000 Om bilan tok va yorqinlikni solishtiring.

**Kutiladigan natija:** 3 qatorli jadval va xulosa.

### 8. Xatoni toping · o'rta
Sxemada LED yonmayapti: manbada 5 V bor, DIP chiqishida 5 V bor, LED oyoqlarida 0 V, rezistor uchlarida 5 V. Xato qayerda?

**Kutiladigan natija:** sabab (butun 5 V rezistorga tushyapti, LED da 0 V — LED qisqa tutashgan: ikki oyog'i bitta qatorda) va tuzatish.

### 9. DIP → Arduino · qiyin
DIP1 → Pin 2, DIP2 → Pin 3 (qarama-qarshi oyoqlar GND). Ikkala kalit holatini Serial Monitor'ga `DIP1: ON, DIP2: OFF` ko'rinishida faqat o'zgarganda chiqaring.

**Kutiladigan natija:** `INPUT_PULLUP` li kod va Serial yozuvlari.

### 10. 4 rejimli tanlagich · qiyin
2 bitli kod (0–3) bo'yicha ikki LEDni boshqaring: 0 — o'chiq, 1 — Yashil, 2 — Qizil, 3 — navbat bilan miltillash (`millis()`).

**Kutiladigan natija:** `switch (kod)` li ishlaydigan dastur.

### 11. Uch kalitli mantiq · qiyin
Uch kalit bilan sxema yig'ing: LED (DIP1 VA DIP2) YOKI DIP3 bo'lganda yonsin. 8 qatorli haqiqat jadvalini tuzing.

**Kutiladigan natija:** sxema va 8 qatorli jadval.

### 12. Ikkilik ko'rsatkich · bonus
4 pozitsiyali DIP switch'ni Arduino'ga ulang va 0–15 orasidagi sonni Serial Monitor'ga chiqaring; son 10 dan katta bo'lsa, qizil LED yonsin.

**Kutiladigan natija:** 4 bitni o'qib, `kod = b3*8 + b2*4 + b1*2 + b0` hisoblovchi dastur.

## O'zingizni tekshiring

1. Ketma-ket ulangan ikki kalit qanday mantiqni beradi?
2. Parallel ulanganda-chi? Real misol keltiring.
3. Multimetr bilan kuchlanish va tok qanday ulanadi?
4. Rezistor 330 dan 1000 Om ga oshsa, LED bilan nima bo'ladi?
5. Ishlamayotgan zanjirni qaysi tartibda tekshirasiz?
6. `INPUT_PULLUP` da DIP switch ON bo'lsa, pin nima o'qiydi?
7. Ikki kalit nechta kombinatsiya beradi? To'rt kalit-chi?

## Uyga vazifa

Tinkercad'da AND va OR zanjirlarini yig'ib, haqiqat jadvallarini skrinshotlar bilan tasdiqlang; so'ng DIP switch'ni Arduino'ga ulab, 4 rejimli tanlagich dasturini yozing. Batafsil: `uyga-vazifa.md`.
