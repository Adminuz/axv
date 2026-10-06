# 11-dars. Breadboardda DIP switch (DPST) va LED: oddiy elektron sikl (1-qism)

> Uydagi chiroq kalitini bosganingizda nima sodir bo'ladi? Siz shunchaki elektr zanjirini yopasiz yoki ochasiz. Bugun dasturisiz, faqat breadboard, DIP switch va LED bilan shunday zanjirni o'zimiz yig'amiz.

## Dars xulosasi

- **Elektr zanjiri (sikl)** — tok manbadan chiqib, iste'molchidan o'tib, manbaga qaytadigan berk yo'l: manba, o'tkazgich, iste'molchi (LED), kalit va himoya rezistori.
- **Yopiq zanjir** — tok oqadi, LED yonadi; **ochiq zanjir** — yo'l uzilgan, LED o'chiq.
- **Breadboard:** quvvat relslari gorizontal ulangan; har bir raqamli qatorda 5 ta teshik (a–e yoki f–j) bir-biriga ulangan; markaziy ariqcha ikki yarmini ajratadi.
- **Kalitlar:** SPST, SPDT, DPST, DPDT. Pole — nechta zanjir, throw — nechta holat.
- **DIP switch** — bir korpusdagi bir nechta kichik kalit; har bir juft kontakt mustaqil. Ariqcha ustiga qo'yiladi, ON tomoni belgilangan.
- **Om qonuni:** `R = (U − U_LED) / I`. 5 V uchun 220–330 Om, 9 V uchun kamida 470 Om.
- Mikrokontroller yo'q — **dastur yozilmaydi**: kalit holati LEDni bevosita boshqaradi.

## Qo'shimcha ma'lumot

### 1. Zanjir qismlari

| Qism | Bizning sxemada |
|---|---|
| Manba | 5 V manba yoki 9 V batareya |
| O'tkazgich | simlar, breadboard plastinkalari |
| Iste'molchi | LED |
| Kalit | DIP switch |
| Himoya | 220–330 Om rezistor |

### 2. Breadboard xaritasi

- `+` (qizil) va `−` (ko'k) relslar — butun uzunlik bo'ylab ulangan.
- `a5, b5, c5, d5, e5` — o'zaro ulangan; `f5 ... j5` — alohida guruh.
- Markaziy ariqcha `e` va `f` ustunlarini ajratadi.

### 3. Rezistor hisoblash misollari

| Manba | LED | Hisob | Tanlov |
|---|---|---|---|
| 5 V | qizil 2 V, 10 mA | 3 / 0,010 = 300 Om | 330 Om |
| 5 V | yashil 3 V, 10 mA | 2 / 0,010 = 200 Om | 220 Om |
| 9 V | qizil 2 V, 15 mA | 7 / 0,015 ≈ 467 Om | 470 Om |

Standart qatorda aniq son bo'lmasa — **kattarog'ini** tanlang.

### 4. Ulash tartibi

```
+ → DIP kontakt → rezistor → LED anod (uzun oyoq)
LED katod (qisqa oyoq) → GND
```

### 5. Odatiy xatolar

- Komponentning ikki oyog'i bitta qatorda — zanjir ishlamaydi.
- DIP switch ariqcha ustida emas — kontaktlar qisqa tutashadi.
- LED teskari — yonmaydi; rezistorsiz — kuyadi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Elektr zanjiri (sikl)** | Tok aylanib o'tadigan berk yo'l |
| **Yopiq zanjir** | Uzluksiz yo'l, tok oqadi |
| **Ochiq zanjir** | Uzilgan yo'l, tok oqmaydi |
| **Breadboard** | Payvandlashsiz ulash uchun teshikli plata |
| **Quvvat relsi** | Breadboard chetidagi `+` va `−` uzun qatorlar |
| **Markaziy ariqcha** | Breadboardning ikki yarmini ajratuvchi chiziq |
| **Pole (qutb)** | Kalit boshqaradigan mustaqil zanjirlar soni |
| **Throw (yo'nalish)** | Har bir qutb ulanadigan holatlar soni |
| **DPST** | Double Pole, Single Throw — 2 zanjir, yoq/o'chir |
| **DIP switch** | Ikki qator oyoqli korpusdagi kichik kalitlar to'plami |
| **Om qonuni** | `U = I × R` — kuchlanish, tok va qarshilik bog'liqligi |
| **Anod / katod** | LED ning `+` (uzun) va `−` (qisqa) oyoqlari |

## Bilasizmi?

- «Breadboard» so'zma-so'z «non taxtasi» degani: XX asr boshida havaskorlar radiosxemalarni haqiqatan oshxonadagi yog'och non taxtalariga mixlab yig'ishgan.
- DIP — Dual In-line Package: aynan mikrosxemalar (masalan, Arduino UNO dagi ATmega328P ning DIP varianti) shunday ikki qator oyoqli korpusda chiqariladi.
- Eski kompyuter platalari va hozirgi garaj eshigi pultlarida DIP switch orqali «maxfiy kod» sozlanadi — 8 ta kalit 256 xil kod beradi.
- Qizil LED ga taxminan 2 V, ko'k va oq LED ga esa 3 V atrofida kuchlanish kerak.

## Topshiriqlar

### 1. Zanjir qismlari · oson
Cho'ntak fonari uchun zanjirning 5 qismini (manba, o'tkazgich, iste'molchi, kalit, himoya) toping va yozing.

**Kutiladigan natija:** 5 qatorli ro'yxat.

### 2. Ochiq yoki yopiq · oson
4 ta vaziyat uchun zanjir ochiqmi yoki yopiqmi: kalit OFF; sim uzilgan; kalit ON va hammasi ulangan; LED kuygan.

**Kutiladigan natija:** 4 ta javob va qisqa izoh.

### 3. Breadboard teshiklari · oson
`a3–d3`, `c7–c8`, `e12–f12`, `+` relsning 2- va 25-teshigi — qaysilari ulangan?

**Kutiladigan natija:** 4 ta «ha/yo'q» javob.

### 4. Kalit turlari · oson
SPST, SPDT, DPST, DPDT ni jadvalga yozing: nechta zanjir, nechta holat, bittadan misol.

**Kutiladigan natija:** 4 qatorli jadval.

### 5. Rezistor hisobi · o'rta
5 V manba, yashil LED (3 V), 10 mA. So'ng 9 V batareya, qizil LED (2 V), 12 mA. Har biri uchun standart rezistorni tanlang.

**Kutiladigan natija:** 200 → 220 Om va ≈ 583 → 680 Om.

### 6. Bitta LED zanjiri · o'rta
Tinkercad'da 5 V manba, DIP Switch DPST, 330 Om va qizil LED dan zanjir yig'ing. ON/OFF holatlarini skrinshot qiling.

**Kutiladigan natija:** 2 ta skrinshot (yoniq va o'chiq).

### 7. Ulanishlar jadvali · o'rta
6-topshiriqdagi barcha simlarni «qayerdan → qayerga» jadvali ko'rinishida yozing.

**Kutiladigan natija:** 6 qatorli jadval.

### 8. Xatoni toping · o'rta
Do'stingiz LED ning ikkala oyog'ini `b10` va `d10` ga qo'ydi. Nega LED yonmaydi? Qanday tuzatiladi?

**Kutiladigan natija:** sabab (bir qator — qisqa tutashuv) va to'g'ri joylashuv.

### 9. Ikki mustaqil LED · qiyin
DIP switch'ning ikkala juftidan foydalanib, Qizil va Yashil LEDni alohida boshqaring. 4 ta kombinatsiya jadvalini tuzing.

**Kutiladigan natija:** ishlaydigan sxema va 4 qatorli jadval.

### 10. 9 V xavfi · qiyin
9 V batareyaga 220 Om bilan qizil LED ulansa tok qancha bo'ladi? Xavfsiz rezistor qancha bo'lishi kerak?

**Kutiladigan natija:** ≈ 32 mA, kamida 470 Om, hisob bilan.

### 11. Uch rangli indikator · qiyin
Uch LED (qizil, sariq, yashil) va 4 pozitsiyali DIP switch'ning uch kontakti bilan svetofor modelini yig'ing — har bir rang o'z kaliti bilan.

**Kutiladigan natija:** uch zanjirli sxema, har biri o'z rezistori bilan.

### 12. Real qurilma tahlili · bonus
Uyingizdagi biror qurilmada (router, pult, eski kompyuter) DIP switch yoki kichik kalit toping yoki internetdan rasmini toping. U nimani sozlaydi?

**Kutiladigan natija:** rasm va 3–4 jumlali tushuntirish.

## O'zingizni tekshiring

1. Elektr zanjirining asosiy qismlarini ayting.
2. Ochiq va yopiq zanjir farqi nima?
3. Breadboardda qaysi teshiklar o'zaro ulangan?
4. DPST qisqartmasini tushuntiring.
5. DIP switch nega markaziy ariqcha ustiga qo'yiladi?
6. 5 V va qizil LED uchun rezistor qanday hisoblanadi?
7. Nega bu darsda dastur yozilmaydi?

## Uyga vazifa

Tinkercad'da DIP switch'ning ikki kontakti bilan ikki LEDni mustaqil boshqaruvchi zanjir yig'ing, rezistorlarni Om qonuni bo'yicha hisoblang va 4 ta holat jadvalini skrinshotlar bilan topshiring. Batafsil: `uyga-vazifa.md`.
