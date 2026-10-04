# 3-hafta. Uyga vazifalar

Har bir vazifa 20–30 daqiqa. Kodlar alohida `hafta-03` papkasida saqlanadi.

## 7-dars uchun (Takrorlanuvchi algoritm va for sikli)
**1-topshiriq: «Karra jadvali va toq sonlar yig‘indisi»**
`for_mashq.py` faylini oching:
1. `for` sikli yordamida 8 sonining 1 dan 10 gacha bo‘lgan to‘liq ko‘paytirish jadvalini konsolga chiqaring.
2. `[1, 100]` oralig‘idagi barcha toq sonlarning yig‘indisini hisoblovchi dastur tuzing (`range(1, 101, 2)`).
3. 20 dan 1 gacha teskari sanovchi dastur yozing (`range(20, 0, -1)`).

**Kutiladigan natija:** Barcha amallar `for` sikli yordamida to‘g‘ri hisoblanishi.

## 8-dars uchun (Shartli takrorlanish: while sikli)
**2-topshiriq: «Xavfsiz PIN-kod va cheksiz sikl boshqaruvi»**
`while_mashq.py` faylida:
1. Rasmiy 1.44-rasmda ko‘rsatilganidek, foydalanuvchiga 3 ta urinishda PIN-kodni tekshiruvchi dastur yozing. To‘g‘ri kiritilsa `break` bilan chiqilsin, 3 ta xato bo‘lsa `"Karta bloklandi"` xabari berilsin.
2. Foydalanuvchi `0` kiritmaguncha kiritilgan barcha sonlarning o‘rtacha arifmetik qiymatini hisoblovchi dastur tuzing.

**Kutiladigan natija:** `while`, `if` va `break` kombinatsiyasidan to‘g‘ri foydalanilgan bo‘lishi.

## 9-dars uchun (Tanlash operatori: match / case)
**3-topshiriq: «Rasmiy amaliy dasturlar to‘plami»**
`amaliyot_3.py` faylini oching:
1. `[1, n]` intervaldan faqat 3 ga karrali sonlarni chiqarish dasturini ham `for`, ham `while` bilan yozing (`n = 30`).
2. 1 dan 12 gacha bo‘lgan songa qarab oy nomini chiqaruvchi dasturni `match / case` orqali to‘liq yozing.
3. Ikki son va amal belgisini (`+`, `-`, `*`, `/`) qabul qilib hisoblovchi mini-kalkulyatorni `match / case` orqali yakunlang.

**Kutiladigan natija:** Barcha 3 ta masala rasmiy dastur talablari asosida to‘liq ishlab chiqilishi.

## Mentor uchun
Keyingi dars boshida o‘quvchilar bilan `match / case` ning `if-elif` ga nisbatan afzalliklarini muhokama qiling. Python versiyasi 3.10 dan past bo‘lgan o‘quvchilarda yuzaga kelishi mumkin bo‘lgan xatoliklarni tekshirib, interpretatorni yangilashga yordam bering.
