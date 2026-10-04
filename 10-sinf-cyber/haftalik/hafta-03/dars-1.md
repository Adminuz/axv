---
title: "Xavfsizlikni anglash (2-qism): raqamli gigiyena, brauzer xavfsizligi va 2FA"
description: "Raqamli gigiyena asoslari, xavfsiz brauzer kengaytmalari (uBlock, Cookie AutoDelete, ClearURLs), 1.1.1.1 DNS hamda Telegramda 2FA va maxfiylik"
dars: 1
hafta: 3
sinf: 10-sinf-cyber
---

# 7-dars. Xavfsizlikni anglash (2-qism): raqamli gigiyena, brauzer xavfsizligi va 2FA

## Dars rejasi (80 daqiqa)

1. **Kirish va takrorlash (10 daqiqa):** Xavfsizlik tafakkuri (Security Mindset) va parollar xavfsizligini takrorlash, dars maqsadlari.
2. **Nazariy qism (25 daqiqa):**
   - **Raqamli gigiyena (Digital Hygiene) tushunchasi:** raqamli dunyoda shaxsiy daxlsizlik va xavfsizlik odatlari.
   - Har bir foydalanuvchi rioya qilishi lozim bo'lgan 4 ta oltin qoida:
     1. Faqat HTTPS dan foydalanish, treker va reklamalarni bloklash;
     2. Har bir xizmat uchun alohida kuchli parol ishlatish;
     3. Barcha muhim akkauntlarda 2 bosqichli autentifikatsiyani (2FA) yoqish;
     4. Ijtimoiy tarmoqlarda shaxsiy ma'lumotlarni minimal darajada oshkor etish.
   - Brauzer xavfsizligi va treking (kuzatuv) texnologiyalari (Cookies, Web Beacons, Browser Fingerprinting).
   - Xavfsiz DNS xizmatlari (Cloudflare 1.1.1.1 va DNS-over-HTTPS — DoH).
   - Ikki bosqichli autentifikatsiya (2FA) turlari: SMS, Authenticator ilovalari (TOTP) va apparat kalitlar (FIDO2 / YubiKey).
3. **Amaliy laboratoriya mashg'uloti (30 daqiqa):**
   - Brauzerni himoyalash: 4 ta muhim kengaytmani o'rnatish va sozlash (HTTPS Everywhere, uBlock Origin, Cookie AutoDelete, ClearURLs).
   - DNS sozlamalarini 1.1.1.1 va 1.0.0.1 ga o'zgartirish hamda `1.1.1.1/help` orqali tekshirish.
   - Telegram messenjerida 5 bosqichli xavfsizlik va maxfiylik auditini o'tkazish (Maxfiy hisob, 2FA, Faol seanslar, Guruh cheklovlari).
4. **Mustaqil topshiriqlar va muhokama (10 daqiqa):** 10 ta amaliy vazifani yechish.
5. **Xulosa va baholash (5 daqiqa):** Dars xulosasi va tezkor savol-javob.

---

## Asosiy tushunchalar

- **Raqamli gigiyena (Digital Hygiene):** Internet va elektron qurilmalardan foydalanganda shaxsiy ma'lumotlar, moliyaviy mablag'lar va obro'-e'tiborni asrash uchun har kuni muntazam ravishda bajariladigan sodda va xavfsiz odatlar majmui.
- **Kuki (Cookie):** Foydalanuvchining veb-saytga kirish sozlamalari, savatcha ma'lumotlari yoki sessiya identifikatorini saqlovchi kichik matnli fayllar. Treker kukilar odamning barcha saytlardagi harakatlarini kuzatib boradi.
- **uBlock Origin:** Veb-sahifalardagi keraksiz reklamalar, josuslik trekerlari va zararli skriptlarni yuklanishidan oldin bloklovchi eng yengil va samarali ochiq kodli brauzer kengaytmasi.
- **ClearURLs:** Havolalar (URL) ichiga yashirilgan kuzatuvchi treker parametrlarini (masalan, `?utm_source=...`, `?fbclid=...`) avtomatik tozalovchi kengaytma.
- **Cookie AutoDelete:** Sayt yopilishi bilanoq undan qolgan barcha kukilarni avtomatik o'chirib yuboruvchi vosita.
- **DoH (DNS-over-HTTPS):** DNS so'rovlarini (qaysi saytga kirayotganingizni) internet provayder yoki buzg'unchi ko'ra olmasligi uchun HTTPS orqali shifrlab uzatuvchi xavfsiz protokol.
- **2FA (Two-Factor Authentication):** Tizimga kirishda bitta parolga qo'shimcha ravishda ikkinchi omilni (telefon kodi, TOTP generator yoki biometriya) talab qiluvchi kuchaytirilgan xavfsizlik usuli.
- **Faol seanslar (Active Sessions):** Sizning qayd yozuvingizga (masalan, Telegram yoki Google) qaysi qurilmalardan, qaysi IP manzildan va qachon kirilganligini ko'rsatuvchi ro'yxat.

---

## Dars mazmuni

### 1. Raqamli gigiyenaning 4 ta asosiy qoidasi

```
+--------------------------------------------------------------------------+
|                     RAQAMLI GIGIYENANING 4 OLTIN QOIDASI                 |
+--------------------------------------------------------------------------+
| 1. Xavfsiz tarmoq va brauzer -> Faqat HTTPS, reklama va trekerlarni yopish|
| 2. Unikal kuchli parollar    -> Har bir saytga alohida 16+ belgili parol |
| 3. Ikki bosqichli himoya     -> Telegram, Google, banklarda 2FA yoqish   |
| 4. Shaxsiy ma'lumotlar me'yori-> Telefon raqam va rasmlarni begonalarga   |
|                                 ochiq qoldirmaslik                        |
+--------------------------------------------------------------------------+
```

### 2. Brauzerni himoyalash: 4 ta zarur kengaytma

Zamonaviy veb-saytlar foydalanuvchining har bir bosgan joyini, qancha vaqt qolganini va qayerga o'tganini yuzlab trekerlar orqali kuzatadi. Brauzerni mustahkamlash (Hardening) uchun quyidagi 4 ta kengaytma zarur:
1. **HTTPS Everywhere:** Agar saytda shifrlangan versiya bo'lsa, brauzerni majburan xavfsiz `https://` rejimiga o'tkazadi.
2. **uBlock Origin:** Reklama bannerlari orqali tarqaluvchi zararli dasturlarni (Malvertising) va shubhali skriptlarni bloklaydi.
3. **Cookie AutoDelete:** Tab yopilishi bilan kuzatuvchi kukilarni tozalaydi.
4. **ClearURLs:** Telegram yoki ijtimoiy tarmoqlardagi uzun havolalardagi shaxsiy kuzatuv kodlarini olib tashlaydi.

---

### 3. DNS xavfsizligi va 1.1.1.1 sozlamasi

Odatda kompyuterlar mahalliy internet provayderining (ISP) standart DNS serveridan foydalanadi. Natijada provayder siz qaysi saytlarga kirayotganingizni ko'rib turadi.
- DNS manzilini **1.1.1.1** va **1.0.0.1** (Cloudflare) yoki **8.8.8.8** (Google) ga o'zgartirish;
- Brauzerda **DNS-over-HTTPS (DoH)** ni yoqish orqali barcha qidiruvlar shifrlanadi va provayder siz kirgan saytlar ro'yxatini ko'ra olmaydi.

---

### 4. Telegramda xavfsizlik auditi (5 ta qadam)

1. **Maxfiylik sozlamalari:**
   - `Sozlamalar -> Maxfiylik va xavfsizlik -> Telefon raqamim`: «Mening kontaktlarim» yoki «Hech kim» qilib qo'yish.
   - `Oxirgi faol vaqtim`: «Mening kontaktlarim».
   - `Forward qilingan xabarlarda havola`: «Yoqish» (ismingizga havola berilmaydi).
2. **Ikki bosqichli autentifikatsiya (2FA):**
   - Faqat SMS kod bilan kirish yetarli emas (SIM-swap hujumi xavfi bor). Maxsus «Bulutli parol» (Cloud Password) o'rnatish lozim.
3. **Faol seanslarni tekshirish:**
   - `Qurilmalar (Faol seanslar)` bo'limiga kirib, sizga tegishli bo'lmagan yoki eski telefonlarni «Seansni tugatish» tugmasi bilan o'chirish.
4. **Guruh va kanallarga qo'shilish:**
   - «Meni kim guruhlarga qo'shishi mumkin?» bandini «Mening kontaktlarim» qilib qo'yish (spam kanallarga avtomatik qo'shib yuborishning oldini oladi).
5. **Xabarlarni avtomatik o'chirish:**
   - Shaxsiy yozishmalarda xabarlarning 1 oy yoki 1 kunda avtomatik tozalanishini yoqish.

---

## Amaliy laboratoriya mashg'uloti

### 1-qadam: Brauzer kengaytmalarini o'rnatish
1. Chrome Web Store yoki Firefox Add-ons do'koniga kiring.
2. `uBlock Origin` va `ClearURLs` kengaytmalarini qidirib topib, «Brauzerga o'rnatish» tugmasini bosing.
3. Kengaytmalar panelida ularning faol (ishlayotgan) ekanligini tekshiring.

### 2-qadam: Tarmoq adapterida 1.1.1.1 DNS ni sozlash
1. Windows boshqaruv panelida: `Tarmoq va Internet -> Tarmoq ulanishlari -> Xususiyatlar -> IPv4`.
2. DNS qatoriga quyidagilarni kiriting:
   - Afzal ko'rilgan DNS: `1.1.1.1`
   - Muqobil DNS: `1.0.0.1`
3. Brauzerda `https://1.1.1.1/help` manziliga kiring va «Using DNS over HTTPS (DoH)» qatorida «Yes» yozuvi chiqqanligini tekshiring.

### 3-qadam: Telegram xavfsizligini tekshirish
1. Telegramda `Sozlamalar -> Maxfiylik va xavfsizlik -> Ikki bosqichli autentifikatsiya` ga kiring.
2. Kamida 12 belgili kuchli bulutli parol o'rnating va eslatuvchi savol qo'ying.
3. Faol seanslar ro'yxatini ochib, barcha begona qurilmalarni yakunlang.

---

## Mustaqil topshiriqlar

### 1. Raqamli gigiyena tushunchasi · oson
Raqamli gigiyena nima va nega u insonning shaxsiy gigiyenasi kabi har kuni muntazam bajarilishi kerak bo'lgan odat hisoblanadi?
**Yechim:** Raqamli gigiyena — bu virtual makonda shaxsiy ma'lumotlar, pullar va qurilmalarni himoya qilish uchun har kuni ongli ravishda qilinadigan xavfsiz harakatlar (parollarni saqlash, havolalarni tekshirish, yangilashlarni o'rnatish). Bir marotaba qilingan e'tiborsizlik (masalan, shubhali faylni ochish) oylab to'plangan ma'lumotlarning yo'qolishiga olib kelishi mumkin.

### 2. Cookie fayllari va treking xavfi · oson
Nima sababdan veb-saytlarning kuzatuvchi kuki (Tracking Cookie) fayllari foydalanuvchi maxfiyligiga tahdid soladi?
**Yechim:** Treker kukilar foydalanuvchining internetdagi barcha qiziqishlari, qidiruvlari, kirgan saytlari va xaridlarini yozib oladi va yagona raqamli profil shakllantiradi. Bu ma'lumotlar keyinchalik reklama agentliklariga sotiladi yoki ma'lumotlar bazasi sizib chiqqanda firibgarlar qo'liga tushishi mumkin.

### 3. uBlock Origin va oddiy AdBlock farqi · o'rta
uBlock Origin kengaytmasi nima sababdan kiberxavfsizlik mutaxassislari tomonidan oddiy AdBlock dasturlariga qaraganda ko'proq tavsiya etiladi?
**Yechim:** uBlock Origin faqat reklamani yashirib qo'ymaydi, balki zararli skriptlar va trekerlarni xotiraga yuklanishidan oldin to'xtatadi. U ochiq kodli (Open Source), juda kam kompyuter resursi (RAM/CPU) sarflaydi va ba'zi AdBlockerlar kabi «ruxsat etilgan reklamalar» uchun pul olmaydi.

### 4. ClearURLs kengaytmasining ishlash mexanizmi · o'rta
Do'stingiz sizga `https://shop.uz/product?id=12&utm_source=facebook&utm_medium=cpc&fbclid=IwAR2...` havolasini yubordi. ClearURLs bu havolani qanday qisqartiradi va nega bu muhim?
**Yechim:** ClearURLs havoladagi barcha treking parametrlarini (`utm_source`, `fbclid` va boshqalar) olib tashlab, faqat `https://shop.uz/product?id=12` qismini qoldiradi. Bu Facebook yoki Google ning ushbu havola aynan kim tomonidan kimga yuborilganini kuzatishiga yo'l qo'ymaydi.

### 5. DNS-over-HTTPS (DoH) afzalligi · o'rta
Oddiy shifrlanmagan DNS so'rovi bilan DoH (DNS-over-HTTPS) o'rtasidagi asosiy xavfsizlik farqi nimada?
**Yechim:** Oddiy DNS so'rovlari 53-port orqali ochiq matnda uzatiladi, bu esa mahalliy provayder yoki kafedagi xakerga siz qaysi saytlarga kirayotganingizni ko'rish va hatto soxta IP qaytarish (DNS Spoofing) imkonini beradi. DoH esa bu so'rovlarni 443-port orqali shifrlab uzatadi va hech kim siz qaysi sayt nomini so'rayotganingizni ko'ra olmaydi.

### 6. SMS orqali 2FA ning zaifligi · o'rta
Nima sababdan faqat SMS-kod orqali tasdiqlanadigan 2FA kiberxavfsizlikda eng ishonchsiz hisoblanadi va uning o'rniga nima tavsiya etiladi?
**Yechim:** SMS xabarlarini mobil aloqa zaifliklari (SS7 protokoli zaifligi) yoki SIM-kartani soxtalashtirish (SIM-Swap firibgarligi) orqali buzg'unchilar o'g'irlashi mumkin. Uning o'rniga mobil ilovadagi bir martalik kod generatorlari (TOTP — Google Authenticator, Aegis) yoki apparat kalitlar (YubiKey) tavsiya etiladi.

### 7. Telegramda «Mening kontaktlarim» sozlamasi · oson
Telegramda telefon raqamini «Hech kim» yoki «Mening kontaktlarim» qilib qo'yish qanday xavfning oldini oladi?
**Yechim:** Bu firibgarlar va botlarning sizning akkauntingiz orqali telefon raqamingizni aniqlashiga (OSINT razvedkasi) va raqam orqali bank hisoblaringizga yoki boshqa ijtimoiy tarmoqlaringizga hujum uyushtirishiga yo'l qo'ymaydi.

### 8. Faol seanslar (Active Sessions) auditi · o'rta
Telegramda faol seanslarni tekshirganingizda, o'zingiz tanimaydigan boshqa shahar yoki noma'lum qurilma (masalan, «Chrome on Linux, IP: 185.x.x.x») paydo bo'lganini ko'rdingiz. Bu nimani anglatadi va zudlik bilan nima qilish kerak?
**Yechim:** Bu sizning hisobingizga buzg'unchi ruxsatsiz kirib olganligini (Session Hijacking) bildiradi. Zudlik bilan «Boshqa barcha seanslarni tugatish» tugmasini bosish, akkauntga yangi murakkab 2FA parolini o'rnatish va parollarni yangilash shart.

### 9. Guruhlarga qo'shishni cheklash nima uchun muhim? · oson
Nima uchun Telegramda «Meni guruhlarga kim qo'shishi mumkin?» bandini «Mening kontaktlarim» qilib qo'yish kiberxavfsizlik talabi hisoblanadi?
**Yechim:** Agar «Hamma» turgan bo'lsa, xakerlik botlari va firibgarlar sizni avtomatik ravishda soxta investitsiya, kazino yoki moliyaviy piramida guruhlariga qo'shib, fishing tuzoqlariga ilintirishga harakat qiladi.

### 10. Shaxsiy raqamli gigiyena rejasi · bonus
O'zingizning shaxsiy smartfoningiz va kompyuteringiz xavfsizligini ta'minlash bo'yicha 5 ta banddan iborat haftalik tekshiruv rejasini ishlab chiqing.
**Yechim:**
1. Har hafta operatsion tizim va barcha dasturlar yangilanishlarini tekshirish;
2. Brauzer kesh va keraksiz kuki fayllarini tozalash;
3. Telegram, Google va ijtimoiy tarmoqlardagi faol seanslarni ko'rib chiqish;
4. Muhim fayllarning (hujjatlar, fotosuratlar) tashqi qattiq diskka yoki xavfsiz bulutga zaxira nusxasini olish;
5. Ishlatilmayotgan, shubhali ilovalarni telefon va kompyuterdan o'chirib tashlash.

---

## Tezkor savol-javob

1. **Savol:** uBlock Origin qanday kengaytma?
   **Javob:** Reklamalar, kuzatuvchi trekerlar va zararli skriptlarni bloklovchi ochiq kodli brauzer kengaytmasi.
2. **Savol:** Cloudflare ning mashhur xavfsiz DNS manzili qaysi?
   **Javob:** `1.1.1.1` va `1.0.0.1`.
3. **Savol:** 2FA nima uchun kerak?
   **Javob:** Parol o'g'irlangan taqdirda ham ikkinchi xavfsizlik omilisiz akkauntga kirishga yo'l qo'ymaslik uchun.
4. **Savol:** Telegramda faol seanslar qayerdan tekshiriladi?
   **Javob:** `Sozlamalar -> Qurilmalar` bo'limidan.

---

## Mentor uchun eslatma

- Darsda o'quvchilarga o'z telefonlarida Telegram maxfiylik sozlamalarini jonli tarzda ko'rsatib, birgalikda 2FA ni sozlashni topshiring.
- Brauzer kengaytmalarini o'rnatish jarayonini ekranda namoyish eting.
