# 2-hafta. Uyga vazifalar

Har bir vazifa 20–30 daqiqa. Kodlar alohida `hafta-02` papkasida saqlanadi.

## 4-dars uchun (Operatorlar va ifodalar)
**1-topshiriq: «Mantiqiy shartlar laboratoriyasi»**
`mantiq.py` faylini yarating:
1. `ball = 78`, `yosh = 15`, `faol_profil = True` o‘zgaruvchilarini e'lon qiling.
2. Quyidagi 3 ta ifodani konsolga chiqaring:
   - `ball >= 60 and yosh >= 14` (imtihondan o‘tish va yosh cheklovi);
   - `ball >= 90 or faol_profil` (imtiyoz berish sharti);
   - `not (yosh < 7)` (maktabga borish yoshida ekanligi).
3. Matn ichida qidirish: `izoh = "Python FastAPI bilan backend loyiha"` matnida `"FastAPI"` so‘zi borligini `in` yordamida tekshiring.

**Kutiladigan natija:** Barcha mantiqiy ifodalar to‘g‘ri `True` yoki `False` natija qaytarishi.

## 5-dars uchun (Tarmoqlanuvchi algoritm: if va else)
**2-topshiriq: «Juft-toq va harorat filtri»**
`shartli.py` faylini oching:
1. Berilgan `son = 43` sonini `if/else` va `% 2 == 0` yordamida juft yoki toqligini aniqlab ekranga chiqaring.
2. Havo harorati `t = 5` daraja. Agar u 0 dan past bo‘lsa `"Muzlama xavfi bor"`, aks holda `"Muzlama xavfi yo'q"` deb chiqaring.
3. Kassa dasturida xarid 100 000 so‘mdan oshsa 10% chegirma hisoblab beruvchi, aks holda to‘liq to‘lovni chiqaruvchi dastur tuzing.

**Kutiladigan natija:** Kodda to‘g‘ri chekinish (4 ta bo‘sh joy) va ikki nuqta (`:`) ishlatilgan bo‘lishi shart.

## 6-dars uchun (Ko‘p tarmoqli shartlar: elif)
**3-topshiriq: «Rasmiy amaliy dasturlar to‘plami»**
Quyidagi 4 ta rasmiy topshiriqni bitta `amaliyot_2.py` faylida alohida bloklar sifatida yozing:
1. Son musbat, manfiy yoki nol ekanligini aniqlash (`son > 0`, `son < 0`, `son == 0`);
2. Ikki sondan kattasini topish yoki `"Sonlar teng"` deb chiqarish;
3. Yosh toifasi: 0–6 `"Bog‘cha yoshi"`, 7–17 `"Maktab o‘quvchisi"`, 18+ `"Voyaga yetgan"`;
4. Harorat: 0 dan past `"Sovuq, qalin kiyining"`, 0–20 `"Salqin"`, 20 dan yuqori `"Issiq"`.

**Kutiladigan natija:** Barcha 4 ta algoritm to‘liq sinovdan o‘tkazilgan va konsolda toza natija berishi kerak.

## Mentor uchun
Keyingi dars boshidagi 10 daqiqalik takrorlashda o‘quvchilarning `elif` zanjiridagi shartlar tartibini tekshiring. Kichik qiymatni birinchi qo‘yib yuborish orqali yuzaga keladigan mantiqiy xatolarni (masalan, baholashda) ko‘rgazmali tarzda tushuntirib bering.
