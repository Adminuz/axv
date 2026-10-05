# 10-dars. Relatsion ma'lumotlar bazalari va model tushunchasi (2-qism): Normalizatsiya asoslari va BI'dagi o'rni

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga normalizatsiya tushunchasi, ortiqcha takrorlanish (redundansiya) va undan kelib chiqadigan anomaliyalar (Update, Insert, Delete), birinchi, ikkinchi va uchinchi normal shakllar (1NF, 2NF, 3NF) hamda normalizatsiyaning Business Intelligence (BI) tizimlaridagi o'rni (OLTP va tahliliy modellar, denormalizatsiya, Fact va Dimension jadvallar) haqida tushuncha berish.
- **Kutiladigan natija:** O'quvchilar takrorlanuvchi ma'lumotli «yassi» jadvaldagi muammolarni aniqlaydi; jadvalni 1NF, 2NF va 3NF qoidalari bo'yicha bosqichma-bosqich bog'langan jadvallarga ajratadi; nima uchun BI hisobotlari uchun ba'zan qasddan denormalizatsiya qilingan (Star schema) model ishlatilishini tushuntiradi.
- **Vaqt taqsimoti:**
  - O'tgan darsni takrorlash (PK, FK, munosabatlar): 10 daqiqa
  - Yangi mavzu: Redundansiya va 3 ta anomaliya: 15 daqiqa
  - 1NF, 2NF, 3NF bosqichma-bosqich misolda: 25 daqiqa
  - Normalizatsiya va BI: OLTP, Star schema, Fact va Dimension: 15 daqiqa
  - Amaliy topshiriqlar, nazorat savollari va xulosa: 15 daqiqa

> Manba: o'quv dasturi — «Ma'lumotlar bazasi va relatsion model tushunchasi» moduli; o'quv qo'llanma — «Normalizatsiya jarayoni» bo'limi (anomaliyalar, 1NF, 2NF, 3NF; «amaliyotda ko'pchilik relatsion tizimlar kamida 3NF gacha normalizatsiya qilinadi»). Star schema, Fact va Dimension jadvallar dasturning keyingi (Power BI modellashtirish) moduli mavzusi — bu darsda faqat tanishtiriladi.

---

## Mentor konspekti

### 1. Muammo: «yassi» jadval

O'tgan darsda jadvallarni PK va FK orqali bog'lashni o'rgandik. Endi savol: **jadvallarni qanday ajratish kerak?** Quyidagi bitta katta Excel jadvalni ko'raylik (onlayn do'kon buyurtmalari):

| BuyurtmaID | Sana | MijozIsmi | MijozTelefon | MijozShahar | Mahsulotlar | Narxlar |
|---|---|---|---|---|---|---|
| 101 | 01.10 | Aziza Karimova | 90 111 22 33 | Toshkent | Sichqoncha, Klaviatura | 80000, 150000 |
| 102 | 02.10 | Aziza Karimova | 90 111 22 33 | Toshkent | Monitor | 1900000 |
| 103 | 02.10 | Bekzod Aliyev | 93 444 55 66 | Samarqand | Sichqoncha | 80000 |

Muammolar:
- Mijoz ma'lumoti (ism, telefon, shahar) har bir buyurtmada **takrorlanadi** — bu **redundansiya** (ortiqcha takrorlanish).
- Bitta katakda bir nechta qiymat bor (`Sichqoncha, Klaviatura`) — filtrlash va yig'indini hisoblash mumkin emas.

### 2. Uchta anomaliya

Redundansiya quyidagi xatolarga olib keladi (o'quv qo'llanma, «Normalizatsiya jarayoni»):

| Anomaliya | Nima bo'ladi | Misol |
|---|---|---|
| **Update anomaly** (yangilash) | Bir xil ma'lumot bir necha joyda, faqat bittasi o'zgartiriladi → ziddiyat | Aziza telefonini almashtirdi: 101-qatorda yangi, 102-qatorda eski raqam qoldi |
| **Insert anomaly** (qo'shish) | Bir ma'lumotni boshqasisiz qo'shib bo'lmaydi | Yangi mahsulotni hali hech kim sotib olmagan — uni jadvalga qo'yib bo'lmaydi, chunki har qator buyurtma |
| **Delete anomaly** (o'chirish) | Bir narsani o'chirganda kerakli boshqa ma'lumot ham yo'qoladi | Bekzodning yagona buyurtmasi (103) bekor qilindi va o'chirildi — Bekzod haqidagi barcha ma'lumot ham yo'qoldi |

**Normalizatsiya** — ma'lumotlarni bir nechta o'zaro bog'langan jadvallarga ajratib, redundansiyani kamaytirish va ma'lumotlar yaxlitligini ta'minlash usuli. Bosqichlari **normal shakllar (Normal Forms)** deb ataladi.

### 3. Birinchi normal shakl (1NF)

**Qoida:** har bir katakda faqat **bitta (atomar)** qiymat bo'lishi kerak va takrorlanuvchi ustunlar guruhi (`Mahsulot1`, `Mahsulot2`, `Mahsulot3`) bo'lmasligi kerak; har bir qator noyob aniqlanadi.

Yechim: har bir mahsulot alohida qatorga chiqariladi.

| BuyurtmaID | Sana | MijozIsmi | MijozTelefon | MijozShahar | Mahsulot | Narx |
|---|---|---|---|---|---|---|
| 101 | 01.10 | Aziza Karimova | 90 111 22 33 | Toshkent | Sichqoncha | 80000 |
| 101 | 01.10 | Aziza Karimova | 90 111 22 33 | Toshkent | Klaviatura | 150000 |
| 102 | 02.10 | Aziza Karimova | 90 111 22 33 | Toshkent | Monitor | 1900000 |
| 103 | 02.10 | Bekzod Aliyev | 93 444 55 66 | Samarqand | Sichqoncha | 80000 |

Endi kalit — **kompozit**: (`BuyurtmaID`, `Mahsulot`). 1NF bajarildi, lekin takrorlanish hali ham ko'p.

> Eslatma: Excel'dagi «Text-to-Columns» va «har bir ustun — bitta o'zgaruvchi» qoidasi (7-dars) aynan 1NF g'oyasiga mos keladi.

### 4. Ikkinchi normal shakl (2NF)

**Qoida:** jadval 1NF da bo'lishi va kalit bo'lmagan har bir ustun **butun** kalitga to'liq bog'liq bo'lishi kerak (qisman bog'liqlik bo'lmasligi kerak). Bu qoida faqat kompozit kalitli jadvallarda muhim.

Tahlil (kalit: `BuyurtmaID` + `Mahsulot`):
- `Sana`, `MijozIsmi` — faqat `BuyurtmaID` ga bog'liq (mahsulotga emas) → **qisman bog'liqlik**.
- `Narx` — faqat `Mahsulot` ga bog'liq → **qisman bog'liqlik**.

Yechim — 3 ta jadval:

```
Buyurtmalar(BuyurtmaID PK, Sana, MijozIsmi, MijozTelefon, MijozShahar)
Mahsulotlar(MahsulotID PK, Nomi, Narx)
BuyurtmaTarkibi(BuyurtmaID FK, MahsulotID FK, Soni)   -- PK: (BuyurtmaID, MahsulotID)
```

`BuyurtmaTarkibi` — o'tgan darsdagi M:N munosabatning oraliq (junction) jadvali.

### 5. Uchinchi normal shakl (3NF)

**Qoida:** jadval 2NF da bo'lishi va kalit bo'lmagan ustunlar **bir-biriga emas, faqat kalitga** bog'liq bo'lishi kerak (tranzitiv bog'liqlik bo'lmasligi kerak).

Tahlil: `Buyurtmalar` jadvalida `MijozTelefon` va `MijozShahar` buyurtmaga emas, **mijozga** bog'liq: `BuyurtmaID → Mijoz → Telefon`. Bu tranzitiv bog'liqlik.

Yechim — mijozlarni alohida jadvalga chiqaramiz:

```
Mijozlar(MijozID PK, Ism, Telefon, Shahar)
Buyurtmalar(BuyurtmaID PK, Sana, MijozID FK)
Mahsulotlar(MahsulotID PK, Nomi, Narx)
BuyurtmaTarkibi(BuyurtmaID FK, MahsulotID FK, Soni)
```

Natija: Aziza telefoni **bir joyda** saqlanadi (Update anomaly yo'q), yangi mahsulotni buyurtmasiz qo'shish mumkin (Insert anomaly yo'q), buyurtmani o'chirsak ham mijoz qoladi (Delete anomaly yo'q).

Qisqa eslab qolish usuli: «Har bir ustun **kalitga**, **butun kalitga** va **faqat kalitga** bog'liq bo'lsin» (1NF → 2NF → 3NF). Amaliyotda ko'pchilik tizimlar kamida 3NF gacha normalizatsiya qilinadi.

### 6. Normalizatsiyaning BI'dagi o'rni

| | Tranzaksion tizim (OLTP) | Tahliliy tizim (BI, OLAP) |
|---|---|---|
| Maqsad | Har kuni minglab yozuv qo'shish, o'zgartirish (kassa, bank, do'kon sayti) | Katta hajmdagi ma'lumotni o'qish, yig'ish, hisobot va dashboard |
| Model | **Normalizatsiyalangan** (3NF) — ko'p kichik jadval | Ko'pincha qisman **denormalizatsiyalangan** — **Star schema** |
| Ustuvorlik | Yaxlitlik, takrorlanmaslik | O'qish tezligi, soddalik |

**Denormalizatsiya** — tahlil tezligi uchun ba'zi jadvallarni qasddan birlashtirish (biroz takrorlanishga rozi bo'lish).

**Star schema (yulduz sxemasi):**
- markazda **Fact jadval** — o'lchanadigan hodisalar va raqamlar: `FactSotuv(SanaID, MijozID, MahsulotID, Soni, Summa)`;
- atrofida **Dimension jadvallar** — tavsiflovchi ma'lumotlar: `DimMijoz`, `DimMahsulot`, `DimSana`.

```
             DimSana
                |
DimMijoz --- FactSotuv --- DimMahsulot
```

Muhim fikr: BI analitigi **avval** normalizatsiyani tushunishi kerak — chunki ma'lumot manbalari (do'kon, bank bazalari) normalizatsiyalangan bo'ladi; tahlil uchun esa ulardan Star schema yig'iladi (Power BI modulida batafsil).

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Anomaliyani aniqlang (oson)
Maktab jadvali: `OquvchiID, Ism, Sinf, SinfRahbari, SinfRahbariTelefon`. 9-A sinfida 30 o'quvchi bor. Sinf rahbari telefonini almashtirdi. Qanday anomaliya xavfi bor?

**Yechim:**
**Update anomaly.** Sinf rahbari telefoni 30 qatorda takrorlanadi. Agar faqat bir nechta qatorda yangilansa, bazada bir odamning ikki xil telefoni paydo bo'ladi. Yechim: `Sinflar(SinfID, SinfRahbari, Telefon)` jadvalini ajratib, o'quvchilar jadvalida faqat `SinfID` (FK) saqlash.

### 2-topshiriq. 1NF ga keltiring (oson)
| OquvchiID | Ism | Togaraklar |
|---|---|---|
| 1 | Ali | Shaxmat, Futbol |
| 2 | Malika | Robototexnika |

**Yechim:**
Har katakda bitta qiymat bo'lishi uchun to'garaklarni alohida qatorlarga ajratamiz:

| OquvchiID | Ism | Togarak |
|---|---|---|
| 1 | Ali | Shaxmat |
| 1 | Ali | Futbol |
| 2 | Malika | Robototexnika |

Kalit: (`OquvchiID`, `Togarak`). Keyingi qadam (2NF): `Ism` faqat `OquvchiID` ga bog'liq → `Oquvchilar` va `OquvchiTogarak` jadvallariga ajratiladi.

### 3-topshiriq. 2NF va 3NF (o'rta)
Jadval: `BaholarID, OquvchiID, OquvchiIsmi, FanID, FanNomi, Oqituvchi, Baho`. Kalit — (`OquvchiID`, `FanID`) deb oling. Jadvalni 3NF ga keltiring.

**Yechim:**
- `OquvchiIsmi` faqat `OquvchiID` ga bog'liq → qisman bog'liqlik (2NF buziladi).
- `FanNomi`, `Oqituvchi` faqat `FanID` ga bog'liq → qisman bog'liqlik.
- `Baho` butun kalitga (o'quvchi + fan) bog'liq → joyida qoladi.

Natija:
```
Oquvchilar(OquvchiID PK, Ism)
Fanlar(FanID PK, FanNomi, Oqituvchi)
Baholar(OquvchiID FK, FanID FK, Baho)    -- PK: (OquvchiID, FanID)
```
(`BaholarID` ortiqcha — kompozit kalit yetarli; yoki aksincha, `BaholarID` ni sun'iy PK qilib, kompozit juftlikka UNIQUE qo'yish mumkin.) Agar har bir fanni bir nechta o'qituvchi o'tsa, `Oqituvchilar` ham alohida jadvalga ajratiladi.

### 4-topshiriq. Star schema chizing (qiyin)
Do'kon BI hisobotlari uchun «Sotuvlar» Star schema'sini loyihalang: bitta Fact va kamida 3 ta Dimension jadval, har birida 3–4 ta ustun.

**Yechim (namuna):**
```
FactSotuv(SotuvID, SanaID FK, MijozID FK, MahsulotID FK, DokonID FK, Soni, Summa)
DimSana(SanaID PK, Sana, Oy, Chorak, Yil)
DimMijoz(MijozID PK, Ism, Shahar, Yosh)
DimMahsulot(MahsulotID PK, Nomi, Kategoriya, Narx)
DimDokon(DokonID PK, Nomi, Shahar)
```
Fact jadvalda raqamlar (Soni, Summa) va Dimension'larga FK lar; Dimension'larda tavsiflar. Bu sxemada «2024-yil 3-chorakda Samarqanddagi do'konlarda qaysi kategoriya ko'p sotildi?» kabi savollarga tez javob topiladi.

---

## Tezkor nazorat savollari

1. Redundansiya nima?
   - *Javob:* Bir xil ma'lumotning bazada bir necha joyda ortiqcha takrorlanishi.
2. Update, Insert va Delete anomaliyalariga bittadan misol keltiring.
   - *Javob:* Telefon faqat bir qatorda yangilandi; yangi mahsulotni buyurtmasiz qo'shib bo'lmaydi; yagona buyurtma o'chirilganda mijoz ma'lumoti ham yo'qoldi.
3. 1NF ning asosiy talabi nima?
   - *Javob:* Har bir katakda faqat bitta atomar qiymat, takrorlanuvchi ustunlar guruhi yo'q.
4. 2NF va 3NF qanday bog'liqliklarni yo'qotadi?
   - *Javob:* 2NF — qisman bog'liqlikni (kompozit kalitning bir qismiga), 3NF — tranzitiv bog'liqlikni (kalit bo'lmagan ustun boshqa kalit bo'lmagan ustunga).
5. Nega BI modellarida ba'zan denormalizatsiya qilinadi?
   - *Javob:* Hisobot va tahlilda o'qish tezligi va soddalik muhim; Star schema da kamroq JOIN bilan tez yig'ish mumkin.

---

## Uyga vazifa

Quyidagi «yassi» jadvalni 3NF ga keltiring va natijani 3–4 ta bog'langan jadval sxemasi ko'rinishida daftarda chizing (PK, FK va munosabat turlari bilan):
`KitobID, KitobNomi, Muallif, MuallifDavlati, OquvchiIsmi, OquvchiSinfi, OlinganSana, QaytarishSana`.
Batafsil: `uyga-vazifa.md`.
