# 14-dars. Fakt (Fact) va O'lcham (Dimension) jadvallarini loyihalash

> Yaxshi model — yaxshi hisobotning poydevori. Bugun fakt va o'lcham jadvallarini grain asosida loyihalab, yuklab va tekshirishni o'rganamiz.

## Dars xulosasi

- **Dimension:** surrogate kalit + natural kalit + tavsiflovchi atributlar.
- **Fact:** grain, dimension FK lari va raqamli o'lchovlar.
- **O'lchov turlari:** additive, semi-additive (vaqt bo'yicha jamlanmaydi), non-additive (nisbat).
- **Yuklash:** avval dimension, keyin fakt (JOIN orqali surrogate kalitlar).
- **Tekshiruv:** qatorlar soni, yetim kalit (`LEFT JOIN ... IS NULL`), grain dublikati.

## Qo'shimcha ma'lumot

### 1. Nega yillik o'quvchilar sonini yillar bo'yicha qo'shib bo'lmaydi
2022-yilda 485 ming, 2023-yilda 478 ming o'quvchi bo'lsa, ularning yig'indisi «jami o'quvchi» emas: o'quvchilar har yil qayta sanalgan. Bunday «holat» o'lchovlari hududlar bo'yicha jamlanadi, yillar bo'yicha esa o'rtacha yoki oxirgi qiymat olinadi.

### 2. Nisbatni saqlamang
`o'quvchi/o'qituvchi` nisbatini fakt jadvalda saqlasangiz, uni jamlab bo'lmaydi. Uning o'rniga ikkala sonni saqlang va nisbatni so'rovda `1.0 * oquvchilar / oqituvchilar` deb hisoblang.

### 3. Natural va surrogate kalit
Manba tizimidagi kod (natural kalit) o'zgarishi mumkin. Omborning o'z kaliti (surrogate) bunday o'zgarishlardan himoya qiladi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Surrogate key | Omborning sun'iy butun kaliti |
| Natural key | Manba tizimidagi kalit |
| Additive | Hamma o'lchamlar bo'yicha jamlanuvchi o'lchov |
| Semi-additive | Vaqt bo'yicha jamlab bo'lmaydigan o'lchov |
| Non-additive | Jamlab bo'lmaydigan o'lchov (nisbat) |
| Yetim kalit | Dimension da mos qatori yo'q FK |
| Yuklash (load) | Ma'lumotni omborga joylash |
| Grain | Fakt qatori aniqlik darajasi |

## Bilasizmi?

- Kimball «Toolkit» da surrogate kalitni deyarli har dimension uchun tavsiya qiladi.
- Real omborlarda fakt jadvallarda milliardlab qator bo'lishi mumkin, dimension lar esa nisbatan kichik.
- Power BI da fakt va dimension jadvallarini «yulduz» sxemada bog'lash hisobot tezligini oshiradi.

## Topshiriqlar

### 1. Dimension atributlari · oson

`dim_hudud` ga qaysi ustunlarni qo'shasiz? 4 tasini yozing.

**Kutiladigan natija:** `hudud_key`, `hudud_id`, `nomi`, `markaz`.

### 2. Surrogate yoki natural · oson

`hudud_key` va `hudud_id` dan qaysi biri surrogate? Nega?

**Kutiladigan natija:** `hudud_key`: omborning sun'iy kaliti.

### 3. Grain jumlasi · oson

`fact_kpi` grain ini bir jumlada yozing.

**Kutiladigan natija:** Bitta hudud, bitta yil.

### 4. O'lchov turlari · oson

`maktablar_soni`, `oquvchilar_soni`, nisbat — turini yozing.

**Kutiladigan natija:** additive*, semi-additive, non-additive.

### 5. dim_sana yaratish · o'rta

`dim_sana` ni `oquv_yili` ustuni bilan yarating va to'ldiring.

**Kutiladigan natija:** 3 qator: 2021/2022 kabi.

### 6. Fakt yuklash · o'rta

`fact_kpi` ni JOIN bilan yuklang.

**Kutiladigan natija:** 15 qator.

### 7. Natijani bashorat qiling · o'rta

`SELECT COUNT(*) FROM dim_sana` natijasi nima va nega?

**Kutiladigan natija:** 3: 3 ta alohida yil.

### 8. Nisbat hisoblash · o'rta

2024-yil uchun hududlar bo'yicha o'quvchi/o'qituvchi nisbatini so'rovda hisoblang.

**Kutiladigan natija:** Toshkent 15.16, Samarqand 12.92, Farg'ona 13.15, Andijon 13.58, Buxoro 13.05.

### 9. Yetim kalit · qiyin

Yetim kalitni topuvchi so'rov yozing.

**Kutiladigan natija:** Natija 0.

### 10. Semi-additive xato · qiyin

`SUM(oquvchilar_soni)` ni barcha yillar bo'yicha hisoblashning xatosini tushuntiring va to'g'ri so'rov yozing.

**Kutiladigan natija:** 7 434 000 mazmunsiz; 2024 uchun 2 526 000.

### 11. Dublikat tekshiruvi · qiyin

Grain bo'yicha dublikatni topuvchi so'rov yozing.

**Kutiladigan natija:** Bo'sh natija.

### 12. O'z modelingiz · bonus

`maktablar` jadvali asosida `fact_maktab` (grain: bitta maktab) loyihalang.

**Kutiladigan natija:** Grain, dimension va o'lchovlar yozilgan.

## O'zingizni tekshiring

1. Surrogate va natural kalit farqi nima?
2. Dimension da nima saqlanadi?
3. Additive, semi-additive, non-additive farqi?
4. `oquvchilar_soni` nega semi-additive?
5. Yuklash tartibi qanday?
6. Yetim kalit nima?
7. Nisbat nega fakt jadvalda saqlanmaydi?

## Uyga vazifa

Fakt va dimension jadvallarini yuklab, tekshiring (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
