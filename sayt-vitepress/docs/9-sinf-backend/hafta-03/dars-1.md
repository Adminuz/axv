---
title: "7-dars. Takrorlanuvchi algoritm va for sikli"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (Back-end)", "link": "/9-sinf-backend/"}, "week": {"n": 3, "link": "/9-sinf-backend/hafta-03/"}, "g": 7, "title": "Takrorlanuvchi algoritm va for sikli", "lead": "Bir xil kodni qayta-qayta yozishdan charchadingizmi? Ushbu darsda dasturlashning eng qudratli kuchi — for sikli va range() funksiyasi yordamida minglab amallarni bir soniyada bajarishni o‘rganamiz.", "slide": "/slaydlar/9-sinf-backend/hafta-03/dars-1.html", "test": "/slaydlar/9-sinf-backend/hafta-03/dars-1-test.html", "tabs": [{"g": 7, "link": "/9-sinf-backend/hafta-03/dars-1", "current": true}, {"g": 8, "link": "/9-sinf-backend/hafta-03/dars-2", "current": false}, {"g": 9, "link": "/9-sinf-backend/hafta-03/dars-3", "current": false}], "prev": null, "next": {"g": 8, "title": "Shartli takrorlanish: while sikli va boshqaruv operatorlari", "link": "/9-sinf-backend/hafta-03/dars-2"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Takrorlanuvchi algoritm (sikl / loop)** — bir xil yoki o‘xshash amallarni belgilangan marta qayta-qayta bajaruvchi algoritm.
- Sikl 3 ta asosiy qismdan iborat: boshlanish (start), takrorlanishlar soni yoki shart (stop) va hisoblagichning o‘zgarishi (step).
- Qachonki takrorlanishlar soni oldindan ma'lum bo‘lsa, ko‘pincha **`for`** siklidan foydalaniladi.
- **`range()`** funksiyasi sonlar ketma-ketligini hosil qiladi.
- `range(5)` &rarr; `0, 1, 2, 3, 4` (Python-da sanoq har doim 0 dan boshlanadi).
- `range(start, stop)` &rarr; `stop` qiymatining o‘zi ketma-ketlikka kirmaydi!
- `range(start, stop, step)` &rarr; uchinchi parametr qadam miqdorini bildiradi.
- `[1, N]` oralig‘idagi sonlar yig‘indisini hisoblash uchun akkumulyator o‘zgaruvchisi (`s = 0`) va `s += i` amali qo‘llaniladi.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### Nega stop qiymati kirmaydi? (Off-by-one qoidasi)
Dasturlashda `range(1, 10)` yozilganda, nima uchun 10 kirmasligini ko‘pchilik yangi o‘rganuvchilar tushunmay qiynaladi. Buning sababi juda oddiy:
1. Chiqadigan sonlar soni har doim `stop - start` ga teng bo‘ladi: `10 - 1 = 9 ta son` chiqadi.
2. Agar siz `n` ta takrorlanish xohlasangiz, shunchaki `range(n)` yozasiz va u 0 dan `n-1` gacha aniq `n` marta aylanadi.
3. Agar `1` dan `N` gacha barcha sonlar (shu jumladan `N` ham) kerak bo‘lsa, oxirgi chegarani `N + 1` qilib belgilash lozim: `range(1, N + 1)`.

### Akkumulyator (Yig‘ib boruvchi) tushunchasi
Matematik hisob-kitoblarda biror natijani to‘plash uchun ishlatiladigan o‘zgaruvchiga dasturlashda **akkumulyator** deyiladi. Masalan:
- Yig‘indini hisoblashda boshlang‘ich qiymat: `s = 0` (chunki qo‘shishda 0 neytral);
- Ko‘paytmani (faktorial) hisoblashda boshlang‘ich qiymat: `p = 1` (chunki 0 ga ko‘paytirsangiz butun natija 0 bo‘lib ketadi!).

### Teskari qadam (Negative Step)
`range()` funksiyasida qadam manfiy son bo‘lishi ham mumkin. Bu holda boshlang‘ich son oxirgi sondan katta bo‘lishi kerak:
```python
for i in range(10, 0, -1):
    print(i, end=" ")
# Natija: 10 9 8 7 6 5 4 3 2 1
```

### Odatiy xatolar
- Qadam nol bo‘lishi: `range(1, 10, 0)` &rarr; `ValueError: range() arg 3 must not be zero`. Qadam hech qachon 0 bo‘lishi mumkin emas!
- Natijani sikl ichida chop etish: Agar `print(s)` ni `for` ning ichiga yozib qo‘ysangiz, u har bir aylanishda oraliq natijani qayta-qayta chiqaraveradi. Faqat yakuniy natija kerak bo‘lsa, `print()` ni sikl tashqarisida yozish kerak.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Sikl (Loop) | Takrorlanuvchi amallar kodi |
| Iteratsiya | Siklning bir marta to‘liq aylanib chiqishi |
| for | Belgilangan to‘plam yoki oraliq bo‘ylab aylanuvchi sikl operatori |
| range() | Sonlar oralig‘ini generator ko‘rinishida hosil qiluvchi funksiya |
| Hisoblagich (Counter) | Har bir iteratsiyada qiymati o‘zgarib boruvchi o‘zgaruvchi (odatda i, j, k) |
| Akkumulyator | Yig‘indi yoki ko‘paytmani to‘plab boruvchi o‘zgaruvchi |
| Off-by-one | Chegarani bitta son kam yoki ko‘p olib yuborish xatosi |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Pythonda `range()` xotirani deyarli egallamaydi! Siz `range(1000000000)` (1 milliard) desangiz ham, Python bu sonlarning barchasini birdaniga xotiraga yuklamaydi, balki har bir sonni faqat kerak bo‘lgan vaqtdagina generatsiya qiladi.
- Katta server tizimlarida ma'lumotlar bazasidagi millionlab yozuvlarni birma-bir tahlil qilish uchun `for` sikllaridan foydalaniladi.
- Dasturlash tarixida birinchi siklli algoritmni 1843-yilda birinchi ayol dasturchi Ada Lavleys (Ada Lovelace) mexanik hisoblash mashinasi uchun yozgan.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. 1 dan 10 gacha sanash <Badge type="tip" text="oson" />
`for` sikli orqali 1 dan 10 gacha bo‘lgan barcha butun sonlarni konsolga chiqaring.
**Kutiladigan natija:** 1 dan 10 gacha sonlar ekranda ko‘rinishi.

### 2. Ismni takrorlash <Badge type="tip" text="oson" />
O‘z ismingizni `for` sikli yordamida konsolga 5 marta chiqaring.
**Kutiladigan natija:** Ismingiz 5 qatorda takrorlanishi.

### 3. Juft sonlar zanjiri <Badge type="tip" text="oson" />
`range(2, 21, 2)` yordamida 2 dan 20 gacha bo‘lgan barcha juft sonlarni ekranga chiqaring.
**Kutiladigan natija:** `2 4 6 8 10 12 14 16 18 20`

### 4. Besh qadamli sanash <Badge type="tip" text="oson" />
0 dan boshlab 50 gacha bo‘lgan sonlarni 5 qadam bilan (`range(0, 51, 5)`) chiqaring.
**Kutiladigan natija:** `0 5 10 15 20 25 30 35 40 45 50`

### 5. [1, N] yig‘indisi <Badge type="warning" text="o'rta" />
Foydalanuvchi kiritgan `n = 20` sonigacha bo‘lgan barcha sonlar yig‘indisini (`1 + 2 + ... + 20`) hisoblovchi dastur yozing.
**Kutiladigan natija:** `Yig'indi: 210`

### 6. Ko‘paytirish jadvali <Badge type="warning" text="o'rta" />
6 sonining 1 dan 10 gacha bo‘lgan ko‘paytirish jadvalini quyidagi formatda chiqaring:
`6 x 1 = 6`, `6 x 2 = 12`, ..., `6 x 10 = 60`.
**Kutiladigan natija:** To‘liq 6 ning karra jadvali.

### 7. Teskari sanash (Start) <Badge type="warning" text="o'rta" />
`range(10, 0, -1)` yordamida 10 dan 1 gacha teskari sanang va sikl tugagach `"Start! Raketa havoga ko'tarildi!"` deb chiqaring.
**Kutiladigan natija:** 10 dan 1 gacha sonlar va start xabari.

### 8. Kvadratlar jadvali <Badge type="warning" text="o'rta" />
1 dan 10 gacha bo‘lgan sonlarning har birining kvadratini (`i ** 2`) hisoblab chiqaring.
**Kutiladigan natija:** `1 ning kvadrati: 1`, `2 ning kvadrati: 4`, ..., `10 ning kvadrati: 100`.

### 9. Faqat 3 ga karrali sonlar yig‘indisi <Badge type="danger" text="qiyin" />
`[1, 50]` oralig‘idagi faqat 3 ga bo‘linadigan sonlarni toping, ularni ekranga chiqaring va ularning umumiy yig‘indisini hisoblang.
**Kutiladigan natija:** 3 ga karrali barcha sonlar va ularning yakuniy summasi.

### 10. Juft va toqlar soni <Badge type="danger" text="qiyin" />
`[1, 100]` oralig‘ida nechta juft va nechta toq son borligini `for` va `if` yordamida sanab, konsolda ko‘rsating.
**Kutiladigan natija:**
```text
Juft sonlar soni: 50 ta
Toq sonlar soni: 50 ta
```

### 11. Faktorial hisoblagich <Badge type="info" text="bonus" />
Matematikada `N!` (faktorial) — 1 dan N gacha barcha sonlar ko‘paytmasidir (`5! = 1 * 2 * 3 * 4 * 5 = 120`). Foydalanuvchi kiritgan sonning faktorialini hisoblovchi dastur tuzing (e'tibor bering, boshlang‘ich ko‘paytma `1` bo‘lishi kerak!).
**Kutiladigan natija:** `5 ning faktoriali: 120`

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Takrorlanuvchi algoritm nima uchun kerak va u kodni qanday qisqartiradi?
2. Siklning 3 ta asosiy qismini sanab bering.
3. `range(1, 10)` ifodasida nega 10 soni kirmaydi?
4. `range(0, 30, 5)` qanday sonlarni generatsiya qiladi?
5. Akkumulyator o‘zgaruvchisi nima va yig‘indi hisoblashda uning boshlang‘ich qiymati nega 0 bo‘ladi?
6. Qanday qilib `range()` yordamida teskari sanash mumkin?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. `jadval.py` faylida 9 sonining 1 dan 10 gacha bo‘lgan ko‘paytirish jadvalini to‘liq konsolga chiqaring.
2. `[1, 50]` oralig‘idagi barcha juft sonlarning yig‘indisini `for` sikli bilan hisoblang.
3. 20 dan 0 gacha 2 qadam bilan teskari sanovchi dastur yozing (`range(20, -1, -2)`).

</div>

