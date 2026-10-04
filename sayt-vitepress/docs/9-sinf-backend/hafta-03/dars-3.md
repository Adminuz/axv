---
title: "9-dars. Tanlash operatori: match / case va amaliy topshiriqlar"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (Back-end)", "link": "/9-sinf-backend/"}, "week": {"n": 3, "link": "/9-sinf-backend/hafta-03/"}, "g": 9, "title": "Tanlash operatori: match / case va amaliy topshiriqlar", "lead": "Uzun va noqulay if-elif zanjirlarini unuting! Ushbu darsda Python 3.10 ning eng zamonaviy imkoniyati bo‘lgan match / case tanlash operatori bilan tanishamiz va rasmiy qo‘llanmadagi barcha amaliy topshiriqlarni (3 ga karralilar, oylar, hafta kunlari) to‘liq kodlaymiz.", "slide": "/slaydlar/9-sinf-backend/hafta-03/dars-3.html", "tabs": [{"g": 7, "link": "/9-sinf-backend/hafta-03/dars-1", "current": false}, {"g": 8, "link": "/9-sinf-backend/hafta-03/dars-2", "current": false}, {"g": 9, "link": "/9-sinf-backend/hafta-03/dars-3", "current": true}], "prev": {"g": 8, "title": "Shartli takrorlanish: while sikli va boshqaruv operatorlari", "link": "/9-sinf-backend/hafta-03/dars-2"}, "next": null}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **`match / case`** (Pattern Matching) — berilgan qiymatni bir nechta aniq variantlar bilan solishtirib, mos kelgan blokni bajaruvchi zamonaviy tanlash operatori.
- Ko‘p sonli variantlar (hafta kunlari, oylar, menyu buyruqlari) mavjud bo‘lganda `if/elif` ga qaraganda ancha qisqa va toza yoziladi.
- `case _:` — barcha oldingi holatlarga tushmagan qolgan har qanday qiymatlar uchun ishlaydi (`else` ning analogi).
- `|` (quvur / pipe) belgisi orqali bitta `case` ichida bir nechta qiymatni birlashtirish mumkin (`case 6 | 7:`).
- `[1, n]` oralig‘idagi sonlarni filtrlashda (masalan, 3 ga karrali) ham `for`, ham `while` sikllaridan muvaffaqiyatli foydalanish mumkin.
- 1-bobning asosiy algoritmlari (arifmetika, shartlar, sikllar, tanlash operatorlari) to‘liq yakunlandi!

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### Nega boshqa tillarda switch bor, Pythonda esa yo‘q edi?
C, C++, Java va JavaScript tillarida o‘nlab yillardan beri `switch / case` operatori mavjud edi. Python yaratuvchilari esa oddiy `switch` tilga yangilik qo‘shmaydi deb hisoblab, uni uzoq vaqt kiritishmagan. Ammo Python 3.10 versiyasida (2021-yil) shunchaki switch emas, balki ancha kuchliroq bo‘lgan **Strukturaviy andozalar moslashuvi (Structural Pattern Matching)** — ya'ni `match / case` joriy qilindi. U nafaqat son va matnlarni, balki murakkab ro‘yxatlar, lug‘atlar va obyektlar tuzilishini ham bir zumda tahlil qila oladi!

### case _ nima uchun pastki chiziq bilan yoziladi?
Pythonda `_` (pastki chiziq) "menga bu qiymatning aniq nomi muhim emas, har qanday boshqa qiymat qabul qilinsin" degan ma'noni anglatadi. Dasturlashda bu **wildcard** deb ataladi. Agar siz `case _:` ni eng tepaga yozib qo‘ysangiz, barcha holatlar o‘sha yerda to‘xtab qoladi. Shuning uchun `case _:` har doim eng oxirida turishi shart.

### Guard shartlari (case ... if)
`match/case` da variant ichida qo‘shimcha `if` shartini qo‘yish mumkin:
```python
ball = 95
match ball:
    case b if b >= 90:
        print("A'lo darajali stipendiya!")
    case b if b >= 70:
        print("Oddiy stipendiya")
    case _:
        print("Stipendiya yo'q")
```
Bu backendda buyurtmalar holatini tekshirishda juda qo‘l keladi.

### Odatiy xatolar
- Eski Python versiyasida ishlatish: Agar kompyuteringizda Python 3.9 yoki undan eski versiya o‘rnatilgan bo‘lsa, `match` operatori ishlamaydi (`SyntaxError` beradi). Albatta Python 3.10 yoki undan yuqori versiya kerak.
- `case` dan keyin ikki nuqtani unutish: Har bir `case` qatori oxirida `:` bo‘lishi shart.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| match / case | Python 3.10+ tanlash va andozalarni moslashtirish operatori |
| Pattern Matching | Ma'lumotlar andozasini solishtirish mexanizmi |
| Wildcard (_) | Har qanday boshqa holatni qamrab oluvchi belgi |
| Pipe (|) | Bir nechta variantni birlashtiruvchi "yoki" belgisi |
| Karrali son | Biror songa qoldiqsiz bo‘linadigan son |
| Menu routing | Foydalanuvchi buyrug‘iga qarab kerakli funksiyani ishga tushirish |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Telegram botlarda foydalanuvchi tugmalarni bosganda (masalan, "Katalog", "Sozlamalar", "Bog'lanish") keladigan buyruqlarni qayta ishlash uchun professional backend dasturchilar aynan `match / case` dan foydalanishadi.
- FastAPI va REST API tizimlarida HTTP status kodlarini (200, 201, 400, 404, 500) tahlil qilishda `match / case` eng qisqa va tezkor yechim hisoblanadi.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Dastur menyusi (1.47-rasm) <Badge type="tip" text="oson" />
Foydalanuvchi 1, 2 yoki 3 kiritadi:
- 1 &rarr; `"Dastur boshlandi"`
- 2 &rarr; `"Sozlamalar ochildi"`
- 3 &rarr; `"Dastur yopildi"`
- Boshqa &rarr; `"Noto'g'ri tanlov"`
dasturini `match / case` bilan yozing.
**Kutiladigan natija:** Tanlangan raqamga mos xabar chiqishi.

### 2. Hafta kunlari (1.48-rasm) <Badge type="tip" text="oson" />
1 dan 7 gacha raqam kiritilganda haftaning mos kunini (Dushanba...Yakshanba) chiqaruvchi dastur tuzing. Boshqa holatda `"Xato! 1–7 oralig'ida kiriting"` deb chiqarsin.
**Kutiladigan natija:** 1 kiritilganda `Dushanba` chiqishi.

### 3. [1, n] 3 ga karrali sonlar (for bilan) <Badge type="tip" text="oson" />
Foydalanuvchi `n = 30` sonini kiritadi. `for` sikli yordamida 1 dan 30 gacha bo‘lgan barcha 3 ga bo‘linadigan sonlarni chiqaring.
**Kutiladigan natija:** `3 6 9 12 15 18 21 24 27 30`

### 4. [1, n] 3 ga karrali sonlar (while bilan) <Badge type="tip" text="oson" />
Aynan 3-topshiriqni `while` sikli yordamida qayta yozing va natijalar bir xilligini tekshiring.
**Kutiladigan natija:** `3 6 9 12 15 18 21 24 27 30`

### 5. Oylar nomi (1.3-topshiriq) <Badge type="warning" text="o'rta" />
Foydalanuvchi 1 dan 12 gacha bo‘lgan oy raqamini kiritganda tegishli oy nomini (Yanvar, Fevral, ..., Dekabr) chiqaruvchi to‘liq dasturni `match / case` orqali yozing.
**Kutiladigan natija:** 10 kiritilganda `Oktyabr` chiqishi.

### 6. Fasllarni aniqlash <Badge type="warning" text="o'rta" />
Oy raqamiga qarab faslni aniqlang (`|` operatoridan foydalaning):
- 12, 1, 2 &rarr; `"Qish"`
- 3, 4, 5 &rarr; `"Bahor"`
- 6, 7, 8 &rarr; `"Yoz"`
- 9, 10, 11 &rarr; `"Kuz"`
**Kutiladigan natija:** 4 kiritilganda `Bahor` chiqishi.

### 7. Ish kuni yoki dam olish kuni <Badge type="warning" text="o'rta" />
Hafta kuni raqami berilgan (1–7). `case 1 | 2 | 3 | 4 | 5:` orqali `"Ish kuni"`, `case 6 | 7:` orqali `"Dam olish kuni"` deb chiqaruvchi dastur yozing.
**Kutiladigan natija:** 6 kiritilganda `Dam olish kuni` chiqishi.

### 8. Mini-kalkulyator <Badge type="warning" text="o'rta" />
Foydalanuvchi ikkita son (`a = 12`, `b = 4`) va amal belgisini (`amal = "*"`) kiritadi. `match amal:` yordamida `+`, `-`, `*`, `/` amallarini bajaruvchi kalkulyator dasturini tuzing.
**Kutiladigan natija:** `Natija: 48`

### 9. [1, n] oralig‘idagi 3 ga va 5 ga karrali sonlar <Badge type="danger" text="qiyin" />
`[1, 100]` oralig‘ida bir vaqtning o‘zida ham 3 ga, ham 5 ga bo‘linadigan (ya'ni 15 ga karrali) barcha sonlarni toping, ekranga chiqaring va ularning sonini hisoblang.
**Kutiladigan natija:** `15 30 45 60 75 90` va `Jami: 6 ta`.

### 10. HTTP status kodlari routeri <Badge type="danger" text="qiyin" />
Serverdan kelgan status kodi berilgan (`status = 404`):
- 200 &rarr; `"OK: Muvaffaqiyatli"`
- 201 &rarr; `"Created: Yangi obyekt yaratildi"`
- 400 &rarr; `"Bad Request: Noto'g'ri so'rov"`
- 403 &rarr; `"Forbidden: Ruxsat berilmagan"`
- 404 &rarr; `"Not Found: Sahifa topilmadi"`
- 500 &rarr; `"Internal Server Error: Server xatoligi"`
- Boshqa &rarr; `"Noma'lum status kodi"`
**Kutiladigan natija:** 404 kiritilganda `Not Found: Sahifa topilmadi` chiqishi.

### 11. To‘liq konsol menyusi (Interaktiv) <Badge type="info" text="bonus" />
`while True:` sikli ichida ishlovchi, foydalanuvchiga doimiy menyu ko‘rsatuvchi dastur tuzing:
- 1: Balansni tekshirish
- 2: Pul qo‘shish
- 3: Chiqish (`break` bilan dastur yopiladi)
Har bir tanlov `match / case` orqali boshqarilsin.
**Kutiladigan natija:** To‘liq ishlovchi interaktiv bankomat/server konsol menyusi.

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. `match / case` operatorining `if-elif-else` dan qanday asosiy afzalliklari bor?
2. `case _:` dagi pastki chiziq belgisi nima uchun kerak?
3. Bitta `case` da bir nechta qiymatni tekshirish uchun qaysi belgi ishlatiladi?
4. Nega `[1, n]` oraliqdagi 3 ga karrali sonlarni chiqarish masalasida `for` ham, `while` ham ishlatilishi mumkin?
5. `match` operatori Pythonning qaysi versiyasidan boshlab mavjud?
6. Qanday vaziyatlarda `match / case` o‘rniga baribir `if-elif` ishlatish to‘g‘ri bo‘ladi?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. Rasmiy qo‘llanmadagi barcha amaliy topshiriqlarni alohida fayllarga saqlang:
   - `karrali_uch.py` (3 ga karralilarni for va while bilan chiqarish);
   - `oylar.py` (1 dan 12 gacha sonlarga qarab oy nomini match/case bilan chiqarish);
   - `kalkulyator.py` (+, -, *, / amallarini match/case bilan hisoblash).
2. Dasturlarni turli kiritmalar bilan sinab ko‘ring va 1-chorakning 3 haftalik mavzularini to‘liq takrorlang.

</div>

