# 16-dars. Sekin o'zgaruvchi o'lchamlar (SCD Type 1, Type 2) va surrogat kalitlar

> Dunyo o'zgaradi, hisobot esa o'tgan yilni to'g'ri ko'rsatishi kerak. Bugun dimension tarixini saqlashni o'rganamiz.

## Dars xulosasi

- SCD — dimension atributlari sekin o'zgarishini boshqarish usullari.
- Type 1 — ustiga yozish, tarix yo'q; Type 2 — yangi qator, tarix saqlanadi.
- Type 2 ustunlari: `boshlandi`, `tugadi`, `joriy`.
- Surrogate kalit — omborning sun'iy kaliti; Type 2 da shart.
- Fakt jadval surrogate kalitga bog'lanadi, shuning uchun tarix to'g'ri ko'rinadi.
- Tanlov biznes savoliga bog'liq: tarix kerakmi?

## Qo'shimcha ma'lumot

### Type 3
Eski qiymat uchun alohida ustun (`eski_direktor`) qo'shiladi: faqat bitta oldingi qiymat saqlanadi. Dasturda faqat «SCD turlari» deyilgan; Type 1 va 2 bu yerda chuqur ko'riladi.

### 9999-12-31
Joriy qator uchun «cheksiz kelajak» sanasi: shartlarda `NULL` bilan ishlashdan qulayroq.

### Tranzaksiya
UPDATE va INSERT bitta tranzaksiyada bo'lsa, ombor izchil qoladi.

### Tarixni tekshirish
Eski yil hisobotini qayta ishga tushirganda natija o'zgarmasligi kerak: Type 2 shuni ta'minlaydi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| SCD | Slowly Changing Dimension |
| Type 1 | Ustiga yozish |
| Type 2 | Yangi qator, tarix |
| Surrogate kalit | Sun'iy kalit |
| Natural kalit | Manba identifikatori |
| `joriy` | Joriy qator bayrog'i |
| `tugadi` | Versiya tugash sanasi |
| Tarix | O'zgarishlar ketma-ketligi |
| Tranzaksiya | Bo'linmas amallar guruhi |

## Bilasizmi?

- Type 2 jadvali vaqt o'tishi bilan kattalashadi, shuning uchun faqat tarix kerak atributlar uchun ishlatiladi.
- Ko'p DWH vositalarida SCD Type 2 uchun tayyor funksiyalar bor.
- Kimball metodologiyasi SCD ni dimension modellashning asosiy qismi deb hisoblaydi.

## Topshiriqlar

### 1. SCD nima · oson

SCD ni 2 jumlada ta'riflang.

**Kutiladigan natija:** To'g'ri ta'rif.

### 2. Type 1 · oson

Type 1 ning bitta afzalligi va bitta kamchiligini yozing.

**Kutiladigan natija:** Oddiy; tarix yo'q.

### 3. Type 2 · oson

Type 2 ning bitta afzalligi va bitta kamchiligini yozing.

**Kutiladigan natija:** Tarix bor; jadval kattalashadi.

### 4. Kalit turlari · oson

Surrogate va natural kalitga misol keltiring.

**Kutiladigan natija:** `maktab_key`, `maktab_id`.

### 5. Qaysi tur · o'rta

Telefon raqami xatosi, manzil o'zgarishi: qaysi biriga Type 2?

**Kutiladigan natija:** Manzil o'zgarishi.

### 6. Type 1 yozing · o'rta

Direktorni Type 1 bilan yangilang.

**Kutiladigan natija:** `UPDATE`.

### 7. Type 2 yozing · o'rta

Direktorni Type 2 bilan yangilang.

**Kutiladigan natija:** `UPDATE` + `INSERT`.

### 8. Joriy qator · o'rta

Faqat joriy qatorlarni chiqaring.

**Kutiladigan natija:** `WHERE joriy = 1`.

### 9. Tarix JOIN · qiyin

Fakt va dimension JOIN qilib har yil direktorini chiqaring.

**Kutiladigan natija:** Yillar bo'yicha direktor.

### 10. Xatoni toping · qiyin

Type 2 da eski qator yopilmagan. Nima bo'ladi?

**Kutiladigan natija:** Ikkita joriy qator.

### 11. Tranzaksiya · qiyin

UPDATE va INSERT ni bitta tranzaksiyaga o'rang (`sqlite3`).

**Kutiladigan natija:** `commit` bir marta.

### 12. Type 3 · bonus

Type 3 qanday ishlashini 3 jumlada yozing.

**Kutiladigan natija:** Eski qiymat ustuni.

## O'zingizni tekshiring

1. SCD nima?
2. Type 1 va Type 2 farqi?
3. Type 2 ustunlari?
4. Surrogate kalit nima?
5. Joriy qator qanday olinadi?
6. Qachon Type 2 kerak?

## Uyga vazifa

`dim_maktab` da Type 1 va Type 2 ni sinang (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
