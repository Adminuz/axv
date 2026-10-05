---
title: "2-dars. Sodda ma’lumot toifalari va arifmetik amallar"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (Back-end)", "link": "/9-sinf-backend/"}, "week": {"n": 1, "link": "/9-sinf-backend/hafta-01/"}, "g": 2, "title": "Sodda ma’lumot toifalari va arifmetik amallar", "lead": "Kompyuter shunchaki ulkan hisoblagich! Ushbu darsda Pythondagi sodda ma'lumot turlari bilan tanishamiz va butun bo‘lish, qoldiq olish hamda darajaga oshirish kabi amallarni professional darajada o‘rganamiz.", "slide": "/slaydlar/9-sinf-backend/hafta-01/dars-2.html", "test": "/slaydlar/9-sinf-backend/hafta-01/dars-2-test.html", "tabs": [{"g": 1, "link": "/9-sinf-backend/hafta-01/dars-1", "current": false}, {"g": 2, "link": "/9-sinf-backend/hafta-01/dars-2", "current": true}, {"g": 3, "link": "/9-sinf-backend/hafta-01/dars-3", "current": false}], "prev": {"g": 1, "title": "Python: o‘rnatish, muhit sozlash va ilk dastur", "link": "/9-sinf-backend/hafta-01/dars-1"}, "next": {"g": 3, "title": "O‘zgaruvchilar va ma'lumotlar bilan ishlash", "link": "/9-sinf-backend/hafta-01/dars-3"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- Kompyuter xotirasidagi ma'lumotlar turli toifalarga bo‘linadi: matn (`str`), butun son (`int`), kasr son (`float`), mantiqiy (`bool`).
- Har qanday qiymatning turini tekshirish uchun `type()` funksiyasidan foydalaniladi.
- Oddiy bo‘lish (`/`) natijasi Python-da har doim kasr son (`float`) bo‘ladi (masalan, `8 / 2 = 4.0`).
- Butun bo‘lish (`//`) bo‘linmaning faqat butun qismini ajratib oladi (`91 // 2 = 45`).
- Qoldiqni topish (`%`) bo‘lishdan ortib qolgan qoldiqni beradi (`8 % 3 = 2`).
- Darajaga oshirish uchun ikkita yulduzcha (`**`) ishlatiladi (`2 ** 3 = 8`).
- Amallarning bajarilish tartibini boshqarish uchun qavslardan `( ... )` foydalaniladi.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### Nega oddiy bo‘lish (/) har doim float qaytaradi?
Ko‘pgina boshqa dasturlash tillarida (C, Java) ikkita butun sonni bo‘lsangiz, natija ham butun son bo‘lib qoladi va kasr qismi yo‘qoladi (`7 / 2 = 3` bo‘lib qolishi mumkin). Python 3 dasturchilarni kutilmagan xatolardan asrash uchun oddiy bo‘lishda (`/`) har doim aniq kasr son (`float`) qaytarish qoidasini kiritgan: `7 / 2 = 3.5`. Agar sizga faqat butun qism kerak bo‘lsa, maxsus `//` operatoridan foydalanasiz.

### Qoldiqli bo‘lish (%) amaliyotda nima uchun kerak?
Qoldiq amali backend dasturlashda juda ko‘p amaliy vazifalarni hal qiladi:
1. **Juft va toqlikni aniqlash:** Har qanday sonni 2 ga bo‘lgandagi qoldiq `0` bo‘lsa juft, `1` bo‘lsa toq (`n % 2`).
2. **Vaqt va o‘lchov birliklarini ajratish:** Masalan, 125 sekundni daqiqa va sekundga ajratish: `daqiqa = 125 // 60` (2 daqiqa), `sekund = 125 % 60` (5 sekund).
3. **Sahifalash (Pagination):** Foydalanuvchilarga ma'lumotlarni 10 tadan qilib ko‘rsatishda sahifalar sonini hisoblash.

### Mantiqiy toifa (bool) haqida
`bool` toifasi ingliz matematigi Jorj Bul (George Boole) sharafiga nomlangan. Unda bor-yo‘g‘i ikkita qiymat mavjud: `True` (rost) va `False` (yolg‘on). E'tibor bering, Python-da ular katta harf bilan boshlanadi. Agar kichik harf bilan `true` deb yozsangiz, xatolik yuz beradi.

### Odatiy xatolar
- Nolga bo‘lish xatosi: `10 / 0` yoki `10 // 0` — bu `ZeroDivisionError: division by zero` xatosiga olib keladi. Kompyuterda nolga bo‘lish mumkin emas!
- Vergul va nuqta adashishi: Kasr sonlar vergul bilan emas, nuqta bilan yoziladi: `3.14` (to‘g‘ri), `3,14` (xato, bu kortej deb tushuniladi).
- Toifalarni aralashtirish: Matn va sonni to‘g‘ridan-to‘g‘ri qo‘shib bo‘lmaydi: `"Yoshim: " + 15` xato beradi (`TypeError`).

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| int (integer) | Butun sonlar toifasi (10, -5, 0) |
| float | O‘nli kasr sonlar toifasi (3.14, 0.5) |
| str (string) | Belgilar ketma-ketligi, matn toifasi ("Salom") |
| bool (boolean) | Mantiqiy toifa (True yoki False) |
| type() | Qiymat yoki o‘zgaruvchining toifasini aniqlovchi funksiya |
| Operator | Amallarni bajaruvchi maxsus belgi (+, -, *, //, %) |
| Operand | Operator qaysi qiymatlar ustida ishlasa, o‘sha qiymatlar |
| Butun bo‘lish (//) | Bo‘linmaning faqat butun qismini oluvchi operator |
| Qoldiq (%) | Butun sonli bo‘lishdan hosil bo‘lgan qoldiq operatori |
| Daraja (**) | Sonni darajaga oshiruvchi operator (2 ** 3 = 8) |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Pythonda butun sonlarning (`int`) maksimal chegarasi yo‘q! Boshqa tillarda 2 milliarddan oshganda sonlar sig‘may qoladi, Python esa kompyuteringiz xotirasi yetguncha istalgancha katta sonlarni hisoblay oladi (masalan, `2 ** 1000`).
- Butun bo‘lish (`//`) manfiy sonlarda pastga qarab yaxlitlaydi: masalan `-7 // 2` natijasi `-3` emas, balki `-4` bo‘ladi!
- Dasturlashda mantiqiy amallar kompyuter mikrosxemalaridagi tranzistorlarning yoniq (`1 - True`) yoki o‘chiq (`0 - False`) holatiga to‘liq mos keladi.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Toifani aniqlash <Badge type="tip" text="oson" />
Quyidagi qiymatlarning har birini `type()` funksiyasiga berib, toifasini konsolga chiqaring: `100`, `3.1415`, `"Muhammad al-Xorazmiy"`, `True`.
**Kutiladigan natija:**
```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

### 2. Oddiy hisoblagich <Badge type="tip" text="oson" />
Ikkita son berilgan: `45` va `15`. Ularning yig‘indisi, ayirmasi va ko‘paytmasini hisoblab chiqaring.
**Kutiladigan natija:**
```text
Yig'indi: 60
Ayirma: 30
Ko'paytma: 675
```

### 3. Ikkita bo‘lish farqi <Badge type="tip" text="oson" />
`91` sonini `8` ga oddiy bo‘ling (`/`) va `2` ga butun bo‘ling (`//`). Natijalarni alohida qatorlarda chiqaring.
**Kutiladigan natija:**
```text
Oddiy bo'lish: 11.375
Butun bo'lish: 45
```

### 4. Kvadrat va kub <Badge type="tip" text="oson" />
`7` sonining kvadrati (`7 ** 2`) va kubini (`7 ** 3`) hisoblab, konsolga chiqaring.
**Kutiladigan natija:**
```text
Kvadrati: 49
Kubi: 343
```

### 5. Qoldiqni topish <Badge type="warning" text="o'rta" />
`29` sonini `4` ga bo‘lgandagi qoldiqni `%` operatori orqali hisoblang va natijani quyidagicha chiqaring: `29 ni 4 ga bo'lganda qoldiq: ...`
**Kutiladigan natija:** `29 ni 4 ga bo'lganda qoldiq: 1`

### 6. Sekundlarni daqiqaga aylantirish <Badge type="warning" text="o'rta" />
Berilgan `350` sekund necha daqiqa va necha sekund bo‘lishini `//` va `%` amallari orqali aniqlang.
**Kutiladigan natija:** `350 sekund = 5 daqiqa va 50 sekund`

### 7. Amallar tartibi <Badge type="warning" text="o'rta" />
Quyidagi ifodaning natijasini avval qo‘lda hisoblang, keyin Python-da tekshiring:
`natija = (15 + 5) * 2 - (30 // 4)`
**Kutiladigan natija:** `33`

### 8. Juft yoki toqlik tekshiruvi <Badge type="warning" text="o'rta" />
Har qanday sonning juft yoki toqligini aniqlash uchun uni 2 ga bo‘lgandagi qoldig‘i tekshiriladi. `48` va `77` sonlarini 2 ga bo‘lgandagi qoldiqlarini hisoblang.
**Kutiladigan natija:**
```text
48 ning 2 ga qoldig'i: 0
77 ning 2 ga qoldig'i: 1
```

### 9. Kassa qaytimini hisoblash <Badge type="danger" text="qiyin" />
Xaridor narxi `64 000` so‘mlik mahsulot sotib oldi va kassaga `100 000` so‘m berdi. Qaytim summasini hisoblang hamda uni `10 000` so‘mlik va `1 000` so‘mlik pullarga ajrating.
**Kutiladigan natija:**
```text
Umumiy qaytim: 36000 so'm
10000 so'mliklar: 3 ta
1000 so'mliklar: 6 ta
```

### 10. O‘rtacha ball hisobi <Badge type="danger" text="qiyin" />
O‘quvchining 4 ta fan bo‘yicha to‘plagan ballari: `85`, `90`, `78`, `95`. Ularning umumiy yig‘indisi va o‘rtacha arifmetik qiymatini (kasr son ko‘rinishida) hisoblovchi dastur yozing.
**Kutiladigan natija:**
```text
Umumiy ball: 348
O'rtacha ball: 87.0
```

### 11. Kun, soat va daqiqa konverteri <Badge type="info" text="bonus" />
Katta vaqt oraliqlarini hisoblash backend tizimlarida (server uptime) juda muhim. `10 000` daqiqa necha kun, necha soat va necha daqiqa ekanligini hisoblab beruvchi mukammal dastur tuzing.
**Kutiladigan natija:** `10000 daqiqa = 6 kun, 22 soat va 40 daqiqa`

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Pythonda oddiy bo‘lish (`/`) va butun bo‘lish (`//`) o‘rtasida qanday asosiy farq bor?
2. `type()` funksiyasiga `type(15.0)` berilsa, qanday toifa qaytadi va nega?
3. Qoldiqni topish (`%`) operatoridan hayotiy tizimlarda qanday maqsadlarda foydalaniladi?
4. Nega `10 / 0` amalini bajarganda xatolik yuz beradi?
5. `2 ** 4` amali nimani anglatadi va natijasi nechchi bo‘ladi?
6. Mantiqiy toifadagi `True` va `False` qiymatlari nima uchun qo‘shtirnoqsiz yoziladi?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. Shaxsiy kompyuteringizda `arifmetika.py` faylini oching.
2. Unda quyidagi amallarni bajaring:
   - Tomonlari 15 va 8 bo‘lgan to‘g‘ri to‘rtburchakning yuzi va perimetrini hisoblang;
   - 4500 sekund necha soat, necha daqiqa va necha sekund bo‘lishini aniqlang;
   - `3 ** 5` amali natijasini ekranga chiqaring.
3. Barcha natijalarni izohli qilib `print()` orqali konsolda ko‘rsating.

</div>

