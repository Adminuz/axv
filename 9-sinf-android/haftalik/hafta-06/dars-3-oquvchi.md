# 18-dars. Kotlinda OOP bilan tanishish (1-qism): obyektga yo'naltirilgan dasturlash asoslari va inkapsulyatsiya (private, protected, public)

> Bank kartasidagi pulni hamma o'zgartira olsa, nima bo'lardi? Bugun OYD asoslarini va inkapsulyatsiyani o'rganamiz: ma'lumotni yopamiz va faqat xavfsiz metodlar orqali ochamiz.

## Dars xulosasi

- OYD: dastur obyektlar to'plami sifatida tuziladi.
- 4 tamoyil: inkapsulyatsiya, meros, polimorfizm, abstraksiya.
- Inkapsulyatsiya — ichki ma'lumotni himoya qilish.
- Kirish huquqlari: public, private, protected, internal.
- `private set` — tashqaridan o'qish mumkin, yozish mumkin emas.
- Metodlarda qoidalarni tekshiring.

## Qo'shimcha ma'lumot

### Getter/Setter
Xossa o'qish va yozish funksiyalari.

### `field`
Setter ichida xossaning haqiqiy qiymati.

### `const val`
Kompilyatsiya vaqtidagi konstanta.

### `companion object`
Sinfga tegishli umumiy a'zolar.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| OYD | Obyektga yo'naltirilgan dasturlash |
| Inkapsulyatsiya | Ma'lumotni himoya qilish |
| public | Hamma joyda ko'rinadi |
| private | Faqat sinf ichida |
| protected | Sinf va merosxo'rlarda |
| internal | Modul ichida |
| Setter | Qiymat yozish funksiyasi |
| field | Xossaning haqiqiy qiymati |

## Bilasizmi?

- Kotlin'da sinflar standart holatda `final` (meros olib bo'lmaydi): buning uchun `open` kerak (keyingi dars).
- `internal` Android loyihasida bitta Gradle moduli ichida ko'rinishni bildiradi.
- Android'da `ViewModel` ichidagi holat ko'pincha `private`, tashqariga faqat o'qish uchun ochiladi.

## Topshiriqlar

### 1. OYD · oson

OYD ni qisqa tushuntiring.

**Kutiladigan natija:** Obyektlar bilan dastur tuzish.

### 2. Tamoyillar · oson

OYD ning 4 tamoyilini sanang.

**Kutiladigan natija:** Inkapsulyatsiya, meros, polimorfizm, abstraksiya.

### 3. Standart huquq · oson

Kotlinda standart modifikator?

**Kutiladigan natija:** `public`.

### 4. private · oson

`private` nimani bildiradi?

**Kutiladigan natija:** Faqat sinf ichida.

### 5. Inkapsulyatsiya misoli · o'rta

Hayotdan inkapsulyatsiya misolini yozing.

**Kutiladigan natija:** Bank kartasi, bankomat.

### 6. protected · o'rta

`protected` qayerda ko'rinadi?

**Kutiladigan natija:** Sinf va merosxo'rlarda.

### 7. private set · o'rta

`private set` ni misol bilan yozing.

**Kutiladigan natija:** `var x = 0` ostida `private set`.

### 8. internal · o'rta

`internal` nimani anglatadi?

**Kutiladigan natija:** Modul ichida.

### 9. Setter · qiyin

Baho 0..100 bo'lishini setter bilan ta'minlang.

**Kutiladigan natija:** `if (value in 0..100) field = value`.

### 10. Yechish metodi · qiyin

`yechish()` qaysi shartlarni tekshiradi?

**Kutiladigan natija:** Summa musbat va balansdan ko'p emas.

### 11. Xato tahlili · qiyin

Nega `h.balans = 5` xato beradi?

**Kutiladigan natija:** `private set`.

### 12. Talaba sinfi · bonus

Himoyalangan `Talaba` sinfini yozing.

**Kutiladigan natija:** private xossalar, metodlar bilan.

## O'zingizni tekshiring

1. OYD nima?
2. Inkapsulyatsiya nima?
3. Kirish modifikatorlari?
4. `private set` nima?
5. Setter nima uchun?
6. `protected` qayerda?

## Uyga vazifa

«BankHisobi» sinfini yozing va himoyalang (30–40 daqiqa). To'liq shart: `uyga-vazifa.md`.
