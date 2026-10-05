# 10-dars. Normalizatsiya asoslari va BI'dagi o'rni

> Bitta katta Excel jadval — qulaydek tuyuladi. Lekin mijoz telefonini 50 joyda almashtirish kerak bo'lsa-chi? Bugun ma'lumotni «to'g'ri bo'laklarga ajratish» san'ati — normalizatsiyani o'rganamiz.

## Dars xulosasi

- **Redundansiya** — bir xil ma'lumotning bazada ortiqcha takrorlanishi.
- Redundansiya **3 ta anomaliyaga** olib keladi:
  - **Update anomaly** — ma'lumot faqat bir joyda yangilanadi, boshqa joyda eskisi qoladi;
  - **Insert anomaly** — bir ma'lumotni boshqasisiz qo'shib bo'lmaydi;
  - **Delete anomaly** — bir yozuvni o'chirganda kerakli boshqa ma'lumot ham yo'qoladi.
- **Normalizatsiya** — jadvallarni bog'langan kichik jadvallarga ajratib, takrorlanishni kamaytirish va yaxlitlikni ta'minlash.
- **1NF:** har bir katakda bitta (atomar) qiymat, takrorlanuvchi ustunlar (`Mahsulot1`, `Mahsulot2`) yo'q.
- **2NF:** 1NF + kalit bo'lmagan ustunlar **butun** kalitga bog'liq (qisman bog'liqlik yo'q).
- **3NF:** 2NF + kalit bo'lmagan ustunlar bir-biriga emas, **faqat kalitga** bog'liq (tranzitiv bog'liqlik yo'q).
- **BI'da:** tranzaksion bazalar (OLTP) normalizatsiyalangan; hisobot uchun ko'pincha **Star schema** — markazda **Fact** jadval (raqamlar), atrofida **Dimension** jadvallar (tavsiflar).

---

## Qo'shimcha ma'lumot

### 1. Bitta qoida — uchta shakl

Eslab qolish uchun: «Har bir ustun **kalitga** (1NF), **butun kalitga** (2NF) va **faqat kalitga** (3NF) bog'liq bo'lsin».

### 2. Misol: do'kon buyurtmalari

Boshlang'ich «yassi» jadval: `BuyurtmaID, Sana, MijozIsmi, MijozTelefon, Mahsulotlar, Narxlar` — mijoz har buyurtmada takrorlanadi, bir katakda bir nechta mahsulot.

3NF dan keyin:
```
Mijozlar(MijozID PK, Ism, Telefon, Shahar)
Buyurtmalar(BuyurtmaID PK, Sana, MijozID FK)
Mahsulotlar(MahsulotID PK, Nomi, Narx)
BuyurtmaTarkibi(BuyurtmaID FK, MahsulotID FK, Soni)
```
Endi telefon bitta joyda, yangi mahsulotni buyurtmasiz qo'shish mumkin, buyurtma o'chsa ham mijoz qoladi.

### 3. Normalizatsiya vs denormalizatsiya

| | Normalizatsiya | Denormalizatsiya |
|---|---|---|
| Qayerda | kassa, bank, sayt bazasi (OLTP) | BI hisobotlari, dashboardlar |
| Afzallik | takrorlanish yo'q, yaxlitlik | tez o'qish, oddiy hisobot |
| Kamchilik | ko'p jadval, ko'p bog'lash | biroz takrorlanish |

### 4. Star schema

```
             DimSana
                |
DimMijoz --- FactSotuv --- DimMahsulot
```
**Fact** — nima sodir bo'ldi va qancha (Soni, Summa). **Dimension** — kim, nima, qachon, qayerda.

---

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Redundansiya** | Ma'lumotning ortiqcha takrorlanishi |
| **Anomaliya** | Takrorlanish tufayli yuzaga keladigan yangilash, qo'shish yoki o'chirish xatosi |
| **Normalizatsiya** | Jadvallarni takrorsiz va izchil tuzilmaga keltirish jarayoni |
| **Normal shakl (NF)** | Normalizatsiya bosqichi: 1NF, 2NF, 3NF |
| **Atomar qiymat** | Bo'linmaydigan bitta qiymat (bir katakda bitta ma'lumot) |
| **Kompozit kalit** | Ikki yoki undan ortiq ustundan iborat Primary Key |
| **Qisman bog'liqlik** | Ustunning kompozit kalitning faqat bir qismiga bog'liqligi |
| **Tranzitiv bog'liqlik** | Kalit bo'lmagan ustunning boshqa kalit bo'lmagan ustunga bog'liqligi |
| **OLTP** | Kundalik tranzaksiyalarni qayd etuvchi tizim |
| **Denormalizatsiya** | Tahlil tezligi uchun jadvallarni qasddan birlashtirish |
| **Fact jadval** | O'lchanadigan hodisalar va raqamlar jadvali |
| **Dimension jadval** | Tavsiflovchi ma'lumotlar jadvali (mijoz, mahsulot, sana) |

---

## Bilasizmi?

- Normal shakllar g'oyasini relatsion model muallifi Edgar F. Codd 1970-yillar boshida taklif qilgan.
- 3NF dan keyin ham shakllar bor (BCNF, 4NF, 5NF), lekin amaliyotda ko'pchilik bazalar 3NF da to'xtaydi.
- Power BI kabi vositalar Star schema bilan eng tez ishlaydi — shuning uchun BI analitiklari uni «oltin standart» deyishadi.
- Excel'dagi «har bir ustun — bitta o'zgaruvchi» qoidasi aslida 1NF ning o'zi.

---

## Topshiriqlar

### 1. Redundansiyani toping · oson
`OquvchiID, Ism, Sinf, SinfRahbari, SinfRahbariTelefon` jadvalida qaysi ma'lumotlar takrorlanadi? Nima uchun?

**Kutiladigan natija:** takrorlanuvchi ustunlar va sababi (2–3 jumla).

### 2. Anomaliya turini aniqlang · oson
Uch holatni anomaliya turiga moslang: (a) mijoz manzili faqat bitta qatorda yangilandi; (b) hali sotilmagan mahsulotni jadvalga qo'shib bo'lmaydi; (c) yagona buyurtma o'chirilib, mijoz ham yo'qoldi.

**Kutiladigan natija:** 3 ta to'g'ri juftlik (Update, Insert, Delete).

### 3. 1NF ga keltiring · oson
`1 | Ali | Shaxmat, Futbol` va `2 | Malika | Robototexnika` qatorlarini 1NF ga keltiring.

**Kutiladigan natija:** har katakda bitta qiymatli 3 qatorli jadval.

### 4. Normal shakl qoidalari · oson
1NF, 2NF va 3NF qoidalarini o'z so'zlaringiz bilan bir jumladan yozing.

**Kutiladigan natija:** 3 ta aniq ta'rif.

### 5. Qisman bog'liqlikni toping · o'rta
Kalit — (`OquvchiID`, `FanID`). Ustunlar: `OquvchiIsmi`, `FanNomi`, `Baho`. Qaysi ustun butun kalitga, qaysilari kalitning bir qismiga bog'liq?

**Kutiladigan natija:** `Baho` — butun kalitga; `OquvchiIsmi`, `FanNomi` — qisman.

### 6. 2NF ga ajrating · o'rta
5-topshiriqdagi jadvalni 2NF ga keltiring: qaysi jadvallar hosil bo'ladi?

**Kutiladigan natija:** 3 ta jadval sxemasi (PK va FK bilan).

### 7. Tranzitiv bog'liqlik · o'rta
`Xodimlar(XodimID, Ism, BolimID, BolimNomi, BolimTelefon)` jadvalida tranzitiv bog'liqlikni toping va 3NF ga keltiring.

**Kutiladigan natija:** `Xodimlar` va `Bolimlar` jadvallari, FK bilan.

### 8. Fact yoki Dimension? · o'rta
Jadvallarni ajrating: `Sotuvlar(Sana, MahsulotID, Soni, Summa)`, `Mahsulotlar(MahsulotID, Nomi, Kategoriya)`, `Mijozlar(MijozID, Ism, Shahar)`, `Kalendar(Sana, Oy, Yil)`.

**Kutiladigan natija:** 1 ta Fact, 3 ta Dimension va qisqa sabab.

### 9. Kutubxonani 3NF ga keltiring · qiyin
`KitobID, KitobNomi, Muallif, MuallifDavlati, OquvchiIsmi, OquvchiSinfi, OlinganSana` jadvalini 3NF ga keltiring.

**Kutiladigan natija:** 3–4 ta bog'langan jadval, PK, FK va munosabat turlari.

### 10. Anomaliyalarni tekshiring · qiyin
9-topshiriqdagi yangi modelingizda 3 ta anomaliya endi nima uchun yuz bermasligini har biri uchun bir jumlada tushuntiring.

**Kutiladigan natija:** 3 ta asoslangan izoh.

### 11. Star schema loyihalang · qiyin
Kinoteatr chiptalari sotuvi uchun Star schema chizing: 1 Fact (`FactChipta`) va kamida 3 Dimension (film, zal, sana).

**Kutiladigan natija:** sxema, har jadvalda 3–4 ustun.

### 12. Qachon denormalizatsiya? · bonus
Do'kon direktori har kuni ertalab «kecha qaysi shaharda qancha sotildi» hisobotini ko'radi. Nega bu hisobot uchun ma'lumotni Star schema ga yig'ish foydali? 5–6 jumlali asoslash yozing.

**Kutiladigan natija:** OLTP va BI farqiga tayangan asoslash.

---

## O'zingizni tekshiring

1. Redundansiya nima va u qanday zarar keltiradi?
2. Uchta anomaliyaning har biriga misol keltiring.
3. 1NF ning ikkita talabi qaysi?
4. Qisman va tranzitiv bog'liqlik farqi nima?
5. 3NF dan keyin «Mijoz telefoni» necha joyda saqlanadi?
6. Fact va Dimension jadvallarida qanday ma'lumot turadi?
7. Nega BI modellarida ba'zan denormalizatsiya qilinadi?

---

## Uyga vazifa

Kutubxona «yassi» jadvalini (`KitobID, KitobNomi, Muallif, MuallifDavlati, OquvchiIsmi, OquvchiSinfi, OlinganSana, QaytarishSana`) 3NF ga keltiring va 3–4 ta bog'langan jadval sxemasini PK, FK va munosabat turlari bilan chizing. Batafsil: `uyga-vazifa.md`.
