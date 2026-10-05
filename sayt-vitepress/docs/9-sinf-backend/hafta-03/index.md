---
title: "3-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "9-sinf (Back-end)", "link": "/9-sinf-backend/"}, "n": 3, "bob": "I-bob · Python dasturlash tili asoslari", "lessons": [{"g": 7, "title": "Takrorlanuvchi algoritm va for sikli", "lead": "Bir xil kodni qayta-qayta yozishdan charchadingizmi? Ushbu darsda dasturlashning eng qudratli kuchi — for sikli va range() funksiyasi yordamida minglab amallarni bir soniyada bajarishni o‘rganamiz.", "link": "/9-sinf-backend/hafta-03/dars-1", "slide": "/slaydlar/9-sinf-backend/hafta-03/dars-1.html", "test": "/slaydlar/9-sinf-backend/hafta-03/dars-1-test.html"}, {"g": 8, "title": "Shartli takrorlanish: while sikli va boshqaruv operatorlari", "lead": "Dastur siz aytgan shart bajarilmaguncha tinimsiz ishlaydi! Ushbu darsda shartli takrorlanuvchi while sikli, cheksiz sikllardan himoyalanish hamda siklni muddatidan oldin to‘xtatuvchi break va keyingi qadamga o‘tkazuvchi continue operatorlarini o‘rganamiz.", "link": "/9-sinf-backend/hafta-03/dars-2", "slide": "/slaydlar/9-sinf-backend/hafta-03/dars-2.html", "test": "/slaydlar/9-sinf-backend/hafta-03/dars-2-test.html"}, {"g": 9, "title": "Tanlash operatori: match / case va amaliy topshiriqlar", "lead": "Uzun va noqulay if-elif zanjirlarini unuting! Ushbu darsda Python 3.10 ning eng zamonaviy imkoniyati bo‘lgan match / case tanlash operatori bilan tanishamiz va rasmiy qo‘llanmadagi barcha amaliy topshiriqlarni (3 ga karralilar, oylar, hafta kunlari) to‘liq kodlaymiz.", "link": "/9-sinf-backend/hafta-03/dars-3", "slide": "/slaydlar/9-sinf-backend/hafta-03/dars-3.html", "test": "/slaydlar/9-sinf-backend/hafta-03/dars-3-test.html"}], "test": "/slaydlar/9-sinf-backend/hafta-03/hafta-test.html"}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Har bir vazifa 20–30 daqiqa. Kodlar alohida `hafta-03` papkasida saqlanadi.

### 7-dars uchun (Takrorlanuvchi algoritm va for sikli)
**1-topshiriq: «Karra jadvali va toq sonlar yig‘indisi»**
`for_mashq.py` faylini oching:
1. `for` sikli yordamida 8 sonining 1 dan 10 gacha bo‘lgan to‘liq ko‘paytirish jadvalini konsolga chiqaring.
2. `[1, 100]` oralig‘idagi barcha toq sonlarning yig‘indisini hisoblovchi dastur tuzing (`range(1, 101, 2)`).
3. 20 dan 1 gacha teskari sanovchi dastur yozing (`range(20, 0, -1)`).

**Kutiladigan natija:** Barcha amallar `for` sikli yordamida to‘g‘ri hisoblanishi.

### 8-dars uchun (Shartli takrorlanish: while sikli)
**2-topshiriq: «Xavfsiz PIN-kod va cheksiz sikl boshqaruvi»**
`while_mashq.py` faylida:
1. Rasmiy 1.44-rasmda ko‘rsatilganidek, foydalanuvchiga 3 ta urinishda PIN-kodni tekshiruvchi dastur yozing. To‘g‘ri kiritilsa `break` bilan chiqilsin, 3 ta xato bo‘lsa `"Karta bloklandi"` xabari berilsin.
2. Foydalanuvchi `0` kiritmaguncha kiritilgan barcha sonlarning o‘rtacha arifmetik qiymatini hisoblovchi dastur tuzing.

**Kutiladigan natija:** `while`, `if` va `break` kombinatsiyasidan to‘g‘ri foydalanilgan bo‘lishi.

### 9-dars uchun (Tanlash operatori: match / case)
**3-topshiriq: «Rasmiy amaliy dasturlar to‘plami»**
`amaliyot_3.py` faylini oching:
1. `[1, n]` intervaldan faqat 3 ga karrali sonlarni chiqarish dasturini ham `for`, ham `while` bilan yozing (`n = 30`).
2. 1 dan 12 gacha bo‘lgan songa qarab oy nomini chiqaruvchi dasturni `match / case` orqali to‘liq yozing.
3. Ikki son va amal belgisini (`+`, `-`, `*`, `/`) qabul qilib hisoblovchi mini-kalkulyatorni `match / case` orqali yakunlang.

**Kutiladigan natija:** Barcha 3 ta masala rasmiy dastur talablari asosida to‘liq ishlab chiqilishi.

</div>
