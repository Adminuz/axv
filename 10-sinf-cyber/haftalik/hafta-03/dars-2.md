---
title: "Xavfsizlikni anglash (3-qism): tahdidlarni modellashtirish, Red/Blue Team va CTF"
description: "Tahdidlarni modellashtirish (STRIDE), Red Team vs Blue Team mashqlari hamda Capture The Flag (CTF) musobaqalari asoslari"
dars: 2
hafta: 3
sinf: 10-sinf-cyber
---

# 8-dars. Xavfsizlikni anglash (3-qism): tahdidlarni modellashtirish, Red/Blue Team va CTF

## Dars rejasi (80 daqiqa)

1. **Kirish va takrorlash (10 daqiqa):** Raqamli gigiyena va 2FA mavzularini takrorlash, dars maqsadlari.
2. **Nazariy qism (25 daqiqa):**
   - **Tahdidlarni modellashtirish (Threat Modeling):** tizim qurilishidan oldin xavflarni xaritalash.
   - **STRIDE tahdid modeli:**
     1. Spoofing (Identifikatorni soxtalashtirish);
     2. Tampering (Ma'lumotlarni o'zgartirish);
     3. Repudiation (Harakatni inkor etish);
     4. Information Disclosure (Ma'lumotlar sizib chiqishi);
     5. Denial of Service (Xizmatni to'xtatish);
     6. Elevation of Privilege (Huquqlarni noqonuniy oshirish).
   - **Red Team vs Blue Team mashqlari:**
     - Red Team (Hujumchilar): real buzg'unchi kabi zaifliklarni topish va tizimga kirish;
     - Blue Team (Himoyachilar): xavfsizlik monitoringi (SIEM/SOC), loglarni tahlil qilish va hujumlarni qaytarish;
     - Purple Team: hujum va himoya guruhlarining o'zaro hamkorligi va tajriba almashinuvi.
   - **CTF (Capture The Flag) musobaqalari:**
     - Musobaqa turlari: Jeopardy (kategoriyalar bo'yicha) va Attack-Defense;
     - Asosiy yo'nalishlar: Web, Crypto, Forensics, Reverse Engineering, Pwn, OSINT.
   - Mashhur global kiberinsidentlar darsi: WannaCry va SolarWinds tahlili.
3. **Amaliy mashg'ulot (30 daqiqa):**
   - Maktab elektron tizimi uchun STRIDE tahdid modelini ishlab chiqish.
   - CTF Jeopardy uslubidagi sodda kriptografik va steganografik topshiriqni yechish.
4. **Mustaqil topshiriqlar va muhokama (10 daqiqa):** 10 ta amaliy vazifani yechish.
5. **Xulosa va baholash (5 daqiqa):** Dars xulosasi va tezkor savol-javob.

---

## Asosiy tushunchalar

- **Tahdidlarni modellashtirish (Threat Modeling):** Tizim loyihalash jarayonida qanday buzg'unchilar hujum qilishi mumkinligini, hujum yo'nalishlarini va potensial zaifliklarni oldindan tizimli aniqlash jarayoni.
- **STRIDE:** Microsoft tomonidan ishlab chiqilgan va xalqaro standartga aylangan 6 ta asosiy tahdid toifasi qisqartmasi (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege).
- **Red Team (Qizil jamoa):** Tashkilot xavfsizligini tekshirish uchun buzg'unchi (haker) rolida harakat qiluvchi, tizimdagi barcha zaifliklarni topib kirishga urinuvchi xavfsizlik mutaxassislari.
- **Blue Team (Ko'k jamoa):** Tashkilot axborot tizimlarini himoya qiluvchi, tarmoq monitoringini (SOC) olib boruvchi, hodisalarni qayd etuvchi va hujumlarga javob beruvchi mutaxassislar.
- **Purple Team:** Red Team va Blue Team guruhlarining birgalikda o'tkazadigan amaliy integratsion mashg'uloti.
- **CTF (Capture The Flag):** Kiberxavfsizlik bo'yicha amaliy musobaqa bo'lib, unda qatnashchilar turli zaifliklarni topib, yashirin «bayroq»ni (masalan: `FLAG{cyber_mindset_2026}`) qo'lga kiritishadi.
- **Jeopardy CTF:** Ishtirokchilarga turli sohalar (Web, Crypto, Forensic) bo'yicha mustaqil topshiriqlar beriladigan va ball to'planadigan format.
- **Attack-Defense CTF:** Har bir jamoaga o'z serveri beriladi; ular o'z serverlarini himoya qilishi (Blue) va bir vaqtning o'zida raqiblar serveriga hujum qilishi (Red) kerak bo'lgan format.

---

## Dars mazmuni

### 1. STRIDE tahdid modeli

```
+--------------------------------------------------------------------------+
|                            STRIDE TAHID MODELI                           |
+--------------------------------------------------------------------------+
| S - Spoofing               -> Boshqa odam nomidan tizimga kirish         |
| T - Tampering              -> Ma'lumotlarni o'zgartirish yoki buzish     |
| R - Repudiation            -> «Bu ishni men qilganim yo'q» deb inkor etish|
| I - Information Disclosure -> Maxfiy ma'lumotlarning oshkor bo'lishi     |
| D - Denial of Service      -> Tizimni to'xtatib qo'yish (Crash)          |
| E - Elevation of Privilege -> Oddiy foydalanuvchining admin bo'lib olishi|
+--------------------------------------------------------------------------+
```

1. **Spoofing (Soxtalashtirish):** Hujumchi Bobning parolini o'g'irlab, Alisaning bankiga «Men Bobman» deb kirishi. (Himoya: Kuchli autentifikatsiya, 2FA).
2. **Tampering (O'zgartirish):** Tridining tranzaksiya summasini yoki xodimlar maoshini o'zgartirishi. (Himoya: Xesh funksiyalari, raqamli imzo).
3. **Repudiation (Inkor etish):** Xodim o'zi bajargan xavfli buyruqni «men qilmadim, loglar yo'q» deb rad etishi. (Himoya: O'chmas audit loglari, raqamli imzo).
4. **Information Disclosure (Oshkor qilish):** Mijozlar bazasi internetga sizib chiqishi. (Himoya: Shifrlash, kirish nazorati).
5. **Denial of Service (DoS):** Serverni soxta so'rovlar bilan to'ldirish. (Himoya: Rate limit, WAF, yuklamani taqsimlash).
6. **Elevation of Privilege (Imtiyozlarni oshirish):** Oddiy talaba hisobi orqali maktab baholar bazasining to'liq ma'muri (Admin) huquqini qo'lga kiritish. (Himoya: Rolli boshqaruv — RBAC, Principle of Least Privilege).

---

### 2. Red Team va Blue Team mashqlari

Tashkilot xavfsizligini faqat qog'ozda tekshirib bo'lmaydi. Uni real jangga o'xshash mashg'ulotlarda sinash kerak:
- **Red Team (Hujumchilar):** Real xakerlar kabi fikrlaydi. Ijtimoiy muhandislik, zaif parollarni skanerlash, fishing xatlari yuborish va binoga jismoniy kirishga urinishlar orqali tizimni sinovdan o'tkazadi.
- **Blue Team (Himoyachilar):** Tizimni 24/7 monitoring qiladi. Tarmoq trafigini, tizim loglarini (Event Viewer, SIEM) kuzatadi, Red Team harakatlarini aniqlaydi va ularni bloklaydi.
- **Natija:** Mashg'ulot tugagach, har ikki jamoa uchrashib (Purple Team), qayerda xato bo'lganini muhokama qiladi va himoya devorlarini yanada mustahkamlaydi.

---

### 3. Capture The Flag (CTF) nima?

CTF musobaqalari bo'lajak kiberxavfsizlik mutaxassislari uchun eng katta amaliy maydondir:
- **Web Exploitation:** Saytlardagi SQL Injection, XSS, CSRF zaifliklarini topish.
- **Cryptography:** Qadimgi va zamonaviy shifrlarni (Sesar, RSA, AES) ochish.
- **Forensics:** Disk obrazlari, `.pcap` tarmoq fayllari yoki xotira dumpidan yashirilgan ma'lumotlarni qidirish.
- **Reverse Engineering:** Noma'lum `.exe` faylini dekompilyatsiya qilib, uning ichidagi parolni topish.

---

## Amaliy laboratoriya mashg'uloti

### 1-topshiriq: Maktab elektron jurnali uchun STRIDE tahlili
O'quvchilar guruhlarga bo'linib, maktab elektron jurnali uchun quyidagi savollarga javob yozadilar:
- O'quvchi o'qituvchi nomidan kirishi qaysi tahdidga kiradi? (**Spoofing**)
- O'quvchining jurnaldagi bahosini 3 dan 5 ga o'zgartirishi nima? (**Tampering**)
- Bahoni kim qo'yganini isbotlay olmaslik nima? (**Repudiation**)
- Baholar ro'yxatining Telegramda tarqalib ketishi nima? (**Information Disclosure**)
- Dars paytida jurnal serverining qotib qolishi nima? (**Denial of Service**)
- O'quvchi hisobining tizim adminiga aylanishi nima? (**Elevation of Privilege**)

### 2-topshiriq: Sodda CTF bayrog'ini topish (Kripto va Steganografiya)
1. Matn berilgan: `U1RSSURFVEVTVF9GTEFHe2N5YmVyX21pbmRzZXRfMjAyNn0=`
2. O'quvchi ushbu matn `Base64` algoritmi bilan kodlanganligini aniqlaydi.
3. Terminalda yoki onlayn CyberChef vositasida dekodlaydi:
   ```bash
   echo "U1RSSURFVEVTVF9GTEFHe2N5YmVyX21pbmRzZXRfMjAyNn0=" | base64 -d
   ```
4. Natija: `STRIDETEST_FLAG{cyber_mindset_2026}`.

---

## Mustaqil topshiriqlar

### 1. STRIDE qisqartmasi tahlili · oson
STRIDE ning 6 ta harfi qaysi tahdid turlarini ifodalashini inglizcha va o'zbekcha yozing.
**Yechim:**
- S: Spoofing (Shaxsni soxtalashtirish);
- T: Tampering (Ma'lumotlarni o'zgartirish);
- R: Repudiation (Harakatni inkor etish);
- I: Information Disclosure (Axborotni oshkor qilish);
- D: Denial of Service (Xizmatni to'xtatish);
- E: Elevation of Privilege (Imtiyozlarni oshirish).

### 2. Red Team va Blue Team farqi · oson
Tashkilot xavfsizlik mashg'ulotida Red Team va Blue Team ning asosiy vazifasi nimalardan iborat?
**Yechim:** Red Team — buzg'unchi (hujumchi) sifatida tizimdagi zaifliklarni topib, ularga suqilib kirishni simulyatsiya qiladi. Blue Team — himoyachi sifatida tarmoqni kuzatadi, loglarni tahlil qiladi va Red Team hujumlarini fosh etib to'xtatadi.

### 3. Repudiation (Inkor etish) tahdidiga qarshi himoya · o'rta
Xodim tizimdan 1 million so'm pul o'tkazdi va keyin: «Bu operatsiyani men qilganim yo'q, xato ketgan» deb da'vo qilmoqda. Repudiation ga yo'l qo'ymaslik uchun tizimda nimalar bo'lishi shart?
**Yechim:** Tizimda o'zgartirib va o'chirib bo'lmaydigan, foydalanuvchining shaxsiy raqamli imzosi bilan tasdiqlangan to'liq audit jurnali (Audit Logging) bo'lishi shart. Har bir amal vaqt tamg'asi (Timestamp) va foydalanuvchi identifikatori bilan qayd etilishi kerak.

### 4. Elevation of Privilege ssenariysi · o'rta
Kompaniyaning kichik amaliyotchisi (intern) qanday qilib butun tizim boshqaruvchisi (Domain Admin) bo'lib olishi mumkin? Bunga nima sabab bo'ladi?
**Yechim:** Tizimda «Eng kam imtiyoz berish» (Least Privilege) qoidasiga amal qilinmagan bo'lsa yoki Windows/Linux da imtiyozlarni oshirish (Privilege Escalation) zaifliklari mavjud bo'lsa, oddiy foydalanuvchi tizim fayllarini o'zgartirib administrator huquqini qo'lga kiritishi mumkin.

### 5. Purple Team tushunchasi mohiyati · o'rta
Nima sababdan kiberxavfsizlikda faqat Red Team yoki faqat Blue Team yetarli emas va Purple Team amaliyoti joriy etiladi?
**Yechim:** Agar jamoalar alohida ishlasa, Red Team qanday buzganini sir saqlashi, Blue Team esa o'z kamchiliklarini tan olmasligi mumkin. Purple Team formatida ikkala jamoa yonma-yon o'tirib, hujum va himoya usullarini birgalikda tahlil qiladi va himoyani tezkor kuchaytiradi.

### 6. CTF Jeopardy yo'nalishlari · oson
CTF Jeopardy musobaqalarida eng keng tarqalgan 4 ta toifani sanang va qisqacha tavsiflang.
**Yechim:**
1. Web — veb-sayt zaifliklarini topish;
2. Crypto — shifrlarni buzish va kalitlarni topish;
3. Forensics — fayllar, tasvirlar va tarmoq trafigidan yashirin ma'lumotlarni qidirish;
4. Reverse Engineering — dasturlarni dekompilyatsiya qilib ichki mantiqni o'rganish.

### 7. WannaCry hujumi tahlili · o'rta
2017-yilda dunyo bo'ylab 200 mingdan ortiq kompyuterni zararlagan WannaCry hujumi qanday qilib bir necha soatda butun dunyoga tarqaldi?
**Yechim:** WannaCry kompyuter qurti (Worm) mexanizmidan foydalandi. U Windows tizimidagi SMBv1 protokoli zaifligi (EternalBlue) orqali odam ishtirokisiz tarmoqdagi barcha ochiq 445-portli kompyuterlarga avtomatik o'tib ketdi.

### 8. Base64 kodlashning xavfsizlikka aloqasi · o'rta
Nima uchun Base64 shifrlash (encryption) emas, balki oddiy kodlash (encoding) hisoblanadi?
**Yechim:** Chunki Base64 ma'lumotlarni maxfiy saqlash uchun kalitdan (key) foydalanmaydi. Istalgan odam Base64 matnini algoritmni bilgan holda hech qanday parolsiz darhol o'qiy oladi. U faqat ikkilik ma'lumotlarni matn shakliga o'tkazish uchun xizmat qiladi.

### 9. Least Privilege (Eng kam imtiyoz) tamoyili · qiyin
Kompaniya ma'muri barcha xodimlarga har ehtimolga qarshi «Administrator» huquqini berib qo'ydi. Bu STRIDE ning qaysi tahdidlariga to'g'ridan-to'g'ri eshik ochadi?
**Yechim:** Bu Tampering (fayllarni o'zgartirish), Information Disclosure (maxfiy ma'lumotlarni ko'rish) va Elevation of Privilege tahdidlariga to'liq yo'l ochadi. Har qanday xodim kompyuteriga virus tushsa, virus ham admin huquqi bilan butun tizimni yo'q qila oladi.

### 10. Korporativ tahdid xaritasi (Threat Model) tuzish · bonus
Onlayn ta'lim platformasi (masalan, masofaviy maktab) uchun STRIDE modeli asosida to'liq xavflar matritsasini ishlab chiqing.
**Yechim:**
- Spoofing: O'quvchi boshqa o'quvchi nomidan test topshirishi (Himoya: 2FA, sessiya tekshiruvi);
- Tampering: Test natijalari bazada o'zgartirib qo'yilishi (Himoya: Tranzaksiya xeshlari);
- Repudiation: O'qituvchi baho qo'ymaganini aytishi (Himoya: Batafsil loglar);
- Information Disclosure: Barcha o'quvchilar telefon raqamlari sizib chiqishi (Himoya: Bazani shifrlash);
- Denial of Service: Imtihon paytida saytga sun'iy yuklama berish (Himoya: Rate limit, WAF);
- Elevation of Privilege: O'quvchi o'zini o'qituvchi statusiga o'tkazib olishi (Himoya: Rolli kirish boshqaruvi — RBAC).

---

## Tezkor savol-javob

1. **Savol:** STRIDE nima?
   **Javob:** Microsoft tomonidan yaratilgan 6 ta asosiy tahdid toifasi modeli.
2. **Savol:** Red Team nima bilan shug'ullanadi?
   **Javob:** Tizimga buzg'unchi kabi hujum qilib, real zaifliklarni aniqlaydi.
3. **Savol:** CTF musobaqasining maqsadi nima?
   **Javob:** Amaliy zaifliklarni yechib «bayroq» (flag) ni topish.
4. **Savol:** Base64 shifrlashmi yoki kodlash?
   **Javob:** Kodlash (Encoding), chunki unda maxfiy kalit yo'q.

---

## Mentor uchun eslatma

- O'quvchilar bilan birgalikda Base64 yoki oddiy sezar shifrida CTF bayrog'ini topish mashqini sinfda jonli bajaring.
- Red Team va Blue Team rollarini o'quvchilar orasida taqsimlab, kichik muhokama o'tkazing.
