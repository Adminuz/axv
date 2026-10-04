---
title: "CIA uchligi (1-qism): konfidensiallik, yaxlitlik va foydalanuvchanlik tamoyillari"
description: "Axborot xavfsizligining oltin uchligi — Confidentiality, Integrity, Availability tamoyillari va ularning real hayotiy ahamiyati"
dars: 1
hafta: 2
sinf: 10-sinf-cyber
---

# 4-dars. CIA uchligi (1-qism): konfidensiallik, yaxlitlik va foydalanuvchanlik tamoyillari

## Dars rejasi (80 daqiqa)

1. **Kirish va o'tgan haftani takrorlash (10 daqiqa):** 1-hafta mavzulari (Malware, Fishing, O'RQ-764) yuzasidan tezkor savol-javob.
2. **Nazariy qism (25 daqiqa):**
   - Axborot xavfsizligining asosiy modeli — **CIA triadasi (CIA uchligi)**.
   - **Confidentiality (Konfidensiallik / Maxfiylik):**
     - Ruxsatsiz «o'qish»dan himoya qilish;
     - Axborotni himoyalash mexanizmlari (shifrlash, kirish huquqlari — ACL).
     - Alisaning Onlayn Banki (AOB) misolida Bobning balansi maxfiyligi.
   - **Integrity (Yaxlitlik):**
     - Ruxsatsiz «yozish» va o'zgartirishdan himoya qilish;
     - Xesh funksiyalari (SHA-256) va raqamli imzolar orqali yaxlitlikni nazorat qilish.
     - AOB misolida tranzaksiya summasining o'zgarmasligi.
   - **Availability (Foydalanuvchanlik):**
     - Tizim va ma'lumotlarning ruxsat etilgan foydalanuvchi so'rovi bo'yicha doimo tayyor turishi;
     - Zaxira serverlar (redundancy), yuklamani taqsimlash (Load Balancing), DoS/DDoS himoyasi.
   - Turli sohalarda (Bank, Tibbiyot, Favqulodda xizmatlar) CIA ustuvorliklari.
3. **Amaliy mashg'ulot va keyslar tahlili (30 daqiqa):**
   - 3 xil soha (Tibbiyot, Bank, Yangiliklar portali) uchun CIA ustuvorlik matritsasini tuzish.
   - Fayl yaxlitligini xesh qiymati (CertUtil / sha256sum) yordamida tekshirish amaliyoti.
4. **Mustaqil topshiriqlar va muhokama (10 daqiqa):** 10 ta amaliy topshiriqni yechish.
5. **Xulosa va baholash (5 daqiqa):** Dars natijalarini sarhisob qilish.

---

## Asosiy tushunchalar

- **CIA Triadasi (CIA uchligi):** Axborot xavfsizligi arxitekturasining uchta tayanch ustuni: Confidentiality (Konfidensiallik), Integrity (Yaxlitlik), Availability (Foydalanuvchanlik).
- **Konfidensiallik (Confidentiality):** Axborot yoki uni eltuvchisining shunday holatiki, undan faqat ruxsat berilgan shaxslar tanisha oladi va ruxsatsiz tanishish yoki nusxalashning to'liq oldi olingan bo'ladi.
- **Yaxlitlik (Integrity):** Axborotning buzilmagan, aniq, to'liq va o'zgartirilmagan asl holatida mavjud bo'lishi xususiyati; unga ruxsatsiz kiritilgan har qanday o'zgarishni darhol aniqlash imkoniyati.
- **Foydalanuvchanlik (Availability):** Avtorizatsiyalangan subyekt so'rovi bo'yicha tizim, servis va ma'lumotlarning belgilangan vaqtda va kerakli hajmda tayyor hamda xizmat ko'rsatish holatida bo'lishi.
- **Xesh (Hash sum):** Ma'lumotlar o'zgargan-o'zgarmaganligini bir zumda bilib beruvchi bir tomonlama matematik barmoq izi (masalan, SHA-256).
- **Redundancy (Ortiqchalik / Zaxira tizim):** Asosiy server yoki aloqa kanali ishdan chiqqanda xizmat to'xtab qolmasligi uchun parallel ishlovchi qo'shimcha komponentlar mavjudligi.

---

## Dars mazmuni

### 1. CIA uchligining mohiyati

Har qanday kiberxavfsizlik chorasi, texnik dastur yoki xavfsizlik siyosati aynan ushbu 3 omildan kamida bittasini himoyalashga qaratilgan:

```
                      +-------------------+
                      |         C         |
                      |  Confidentiality  |
                      |   (Maxfiylik)     |
                      +---------+---------+
                               / \
                              /   \
                             /     \
                            /       \
                           /         \
        +-----------------+           +-----------------+
        |        I        |-----------|        A        |
        |    Integrity    |           |  Availability   |
        |   (Yaxlitlik)   |           | (Foydalanuvchan)|
        +-----------------+-----------+-----------------+
```

### 2. Alisaning Onlayn Banki (AOB) misolida CIA

1. **Konfidensiallik (Confidentiality):**
   - Bob o'z hisobidagi pul miqdorini Tridi ko'rishini istamaydi.
   - Bankdagi barcha mijozlar balansi, login-parollar va shaxsiy ma'lumotlar shifrlangan bo'lishi shart.
2. **Yaxlitlik (Integrity):**
   - Bob Alisaga «100 000 so'm o'tkazilsin» deb so'rov yubordi.
   - Agar Tridi bu xabarni ushlab olib, summani «10 000 000 so'm» qilib o'zgartirsa, yaxlitlik buziladi. Bank tizimi bunday o'zgarishni darhol aniqlab, so'rovni bekor qilishi shart.
3. **Foydalanuvchanlik (Availability):**
   - Bob do'konda to'lov qilayotganda bank ilovasiga kira olmasa yoki Tridi bank serveriga DoS hujum uyushtirib uni qotirib qo'ysa, foydalanuvchanlik buziladi. Mijoz to'lov qila olmaydi, bank esa daromad va ishonchni yo'qotadi.

---

### 3. Turli sohalarda CIA ustuvorliklari

Har bir sohada CIA uchligining ustuvorligi turlicha bo'ladi:

| Soha | 1-o'rindagi ustuvorlik | Sababi |
|---|---|---|
| **Favqulodda xizmatlar (103, 101, 102)** | **Availability (Foydalanuvchanlik)** | Tizim soniyali kechikishsiz ishlashi shart, aks holda inson hayoti xavf ostida qoladi. |
| **Moliyaviy tizimlar va Banklar** | **Integrity (Yaxlitlik)** | Hisob raqamlardagi balans va o'tkazma summalari 1 tiyinga ham adashmasligi, soxtalashtirilmasligi shart. |
| **Harbiy va davlat sirlari** | **Confidentiality (Maxfiylik)** | Maxfiy hujjatlar va rejalar begona qo'llarga tushmasligi mutlaq talab hisoblanadi. |
| **Sog'liqni saqlash (Bemor tarixi)** | **Integrity & Confidentiality** | Bemor qon guruhi o'zgarib qolsa vafot etishi mumkin (Integrity); kasallik siri oshkor bo'lmasligi kerak (Confidentiality). |

---

## Amaliy mashg'ulot

### 1-topshiriq: Fayl yaxlitligini xesh (SHA-256) orqali tekshirish

Fayl ichidagi bitta harf yoki nuqta o'zgarsa ham uning SHA-256 xesh qiymati butunlay o'zgaradi (qor ko'chkisi effekti).

**Windows buyruqlar satrida (CMD / PowerShell):**
```powershell
# 1. Sinov fayli yaratish
"Maxfiy shartnoma matni: summa 50000 USD" | Out-File -FilePath shartnoma.txt

# 2. Asl xesh qiymatini olish
CertUtil -hashfile shartnoma.txt SHA256

# 3. Faylni biroz o'zgartirish (masalan 50000 o'rniga 90000 qilish)
"Maxfiy shartnoma matni: summa 90000 USD" | Out-File -FilePath shartnoma.txt

# 4. Qayta xesh olish va solishtirish
CertUtil -hashfile shartnoma.txt SHA256
```

**Linux / macOS terminalida:**
```bash
echo "Maxfiy shartnoma matni: summa 50000 USD" > shartnoma.txt
sha256sum shartnoma.txt

echo "Maxfiy shartnoma matni: summa 90000 USD" > shartnoma.txt
sha256sum shartnoma.txt
```

---

## Mustaqil topshiriqlar

### 1. CIA atamalari ta'rifi · oson
CIA uchligidagi C, I, va A harflarining to'liq inglizcha va o'zbekcha nomlarini yozing hamda har birining ma'nosini bir jumla bilan izohlang.
**Yechim:**
- C: Confidentiality (Konfidensiallik / Maxfiylik) — axborotni ruxsatsiz o'qishdan himoya qilish.
- I: Integrity (Yaxlitlik) — axborotni ruxsatsiz o'zgartirishdan va buzilishdan himoya qilish.
- A: Availability (Foydalanuvchanlik) — tizim va ma'lumotlarning kerakli vaqtda qonuniy foydalanuvchilar uchun ochiq va tayyor turishi.

### 2. Konfidensiallik va Yaxlitlik farqi · oson
Tridi Bobning Alisaga yuborgan xabarini shifrlanganligi sababli o'qiy olmadi, biroq xabarning oxiriga tasodifiy belgilar qo'shib buzib yubordi. Bu yerda CIA ning qaysi mezoni saqlanib qoldi va qaysi biri buzildi?
**Yechim:** Tridi xabarni o'qiy olmagani uchun Konfidensiallik (Confidentiality) saqlanib qoldi. Ammo xabar matniga begona belgilar qo'shilib o'zgargani sababli Yaxlitlik (Integrity) buzildi.

### 3. Favqulodda tizimlarda CIA ustuvorligi · o'rta
Nima sababdan tez tibbiy yordam (103) yoki qutqaruv xizmatlarida eng asosiy ustuvorlik Foydalanuvchanlikka (Availability) beriladi?
**Yechim:** Favqulodda vaziyatlarda insonning hayoti soniyalarga bog'liq. Agar qo'ng'iroq markazi serveri yoki telefon tarmog'i bir necha daqiqaga to'xtab qolsa (Availability yo'qolsa), tez yordam yetib bora olmaydi va odamlar vafot etishi mumkin.

### 4. Xesh qiymati va yaxlitlik tahlili · o'rta
Dastur ishlab chiquvchi o'zining veb-saytida dastur yuklash havolasi yoniga uning SHA-256 xeshini yozib qo'ydi. Nima sababdan foydalanuvchi yuklab olingan fayl xeshini saytdagi xesh bilan solishtirishi shart?
**Yechim:** Yuklab olish jarayonida internetdagi hujumchi (MITM) faylni almashtirib ichiga troyan joylagan bo'lishi yoki fayl chala yuklangan bo'lishi mumkin. Agar foydalanuvchi olgan fayl xeshi saytdagi asl xesh bilan 100% mos kelsa, fayl yaxlit va xavfsiz ekanligi tasdiqlanadi.

### 5. Bank tizimida Yaxlitlik ustuvorligi · o'rta
Tasavvur qiling, bank tizimida konfidensiallik ta'minlangan (hech kim ko'rmaydi), ammo yaxlitlik buzildi. Bu qanday oqibatlarga olib kelishi mumkin?
**Yechim:** Agar yaxlitlik buzilsa, balanslar o'zgarib ketishi mumkin: masalan, hisobida 100 000 so'mi bor odamning balansi 100 000 000 bo'lib qolishi yoki aksincha pullari yo'qolib qolishi mumkin. Bu bank tizimining moliyaviy barbod bo'lishiga va ishonchning butunlay yo'qolishiga sabab bo'ladi.

### 6. DoS hujumining CIA ga ta'siri · oson
DDoS hujumi uyushtirilganda CIA uchligining qaysi elementi to'g'ridan-to'g'ri nishonga olinadi va buziladi?
**Yechim:** Foydalanuvchanlik (Availability). Chunki DDoS ma'lumotlarni o'g'irlamaydi yoki o'zgartirmaydi, balki serverni band qilib, qonuniy foydalanuvchilarga xizmat ko'rsatishni to'xtatadi.

### 7. Shifrlashning CIA dagi roli · o'rta
Kriptografik shifrlash (masalan, AES-256) CIA uchligining aynan qaysi mezonini ta'minlash uchun xizmat qiladi?
**Yechim:** Konfidensiallikni (Confidentiality). Shifrlangan ma'lumotni kalitsiz hech kim o'qiy olmaydi. (Agar shifrlash bilan birga HMAC yoki GCM ishlatilsa, u yaxlitlikni ham kafolatlaydi).

### 8. CIA muvozanatini saqlash muammosi · qiyin
Xavfsizlik tizimida konfidensiallikni oshirish uchun 5 bosqichli autentifikatsiya, har bir amal uchun SMS-kod va 256 belgili parol talab qilinsa, bu CIA ning qaysi komponentiga salbiy ta'sir ko'rsatadi?
**Yechim:** Bu Foydalanuvchanlikka (Availability) va qulaylikka (Usability) salbiy ta'sir qiladi. Tizim shu qadar murakkab va sekin bo'lib qoladiki, xodimlar va mijozlar o'z vaqtida zarur ishlarni bajara olmay qoladilar.

### 9. Tibbiy tashkilotda CIA tahlili · qiyin
Kasalxona kompyuter tarmog'ida bemorlarning operatsiya qilish ro'yxati saqlanadi.
a) Agar hujumchi ro'yxatni o'qisa nima buziladi?
b) Agar ro'yxatdagi bemorning operatsiya qilinadigan a'zosi nomini o'zgartirsa nima buziladi?
c) Agar elektr ta'minoti uzilib tizim o'chib qolsa nima buziladi?
**Yechim:**
a) Konfidensiallik (Confidentiality) buziladi.
b) Yaxlitlik (Integrity) buziladi (juda katta hayotiy xavf).
c) Foydalanuvchanlik (Availability) buziladi.

### 10. Zaxiralash (Backup) va CIA triadasidagi o'rni · bonus
Tashkilotda har kecha avtomatik ravishda ma'lumotlar bazasining zaxira nusxasi (Backup) olinadi. Ushbu chora CIA ning qaysi 2 ta mezonini qayta tiklashga xizmat qiladi va nima uchun?
**Yechim:**
1. Foydalanuvchanlik (Availability): Agar server qulasa yoki ransomware fayllarni qulflasa, zaxira nusxadan tizimni tezda qayta ishga tushirish mumkin;
2. Yaxlitlik (Integrity): Agar bazadagi ma'lumotlar xato sababli yoki hujumchi tomonidan buzib yuborilsa, so'nggi toza zaxira orqali ma'lumotlarning to'g'ri va asl holati tiklanadi.

---

## Tezkor savol-javob

1. **Savol:** CIA qisqartmasi nimani anglatadi?
   **Javob:** Confidentiality, Integrity, Availability.
2. **Savol:** Ma'lumotlarning o'zgarmaganligini tekshirish uchun qaysi texnologiya qo'llaniladi?
   **Javob:** Xesh funksiyalari (masalan, SHA-256) va raqamli imzolar.
3. **Savol:** Tez yordam xizmati uchun CIA ning qaysi biri eng muhim?
   **Javob:** Foydalanuvchanlik (Availability).
4. **Savol:** Xesh qiymati fayl o'zgarganda qanday o'zgaradi?
   **Javob:** Hatto 1 bit o'zgarsa ham xesh qiymati butunlay tanib bo'lmas darajada yangilanadi.

---

## Mentor uchun eslatma

- Darsda o'quvchilarga xesh funksiyasining amaliy namoyishini terminalda ko'rsating: oddiy matn faylida bitta harfni o'zgartirib qayta `sha256sum` oling.
- O'quvchilar ko'pincha konfidensiallik bilan yaxlitlikni bitta narsa deb o'ylashadi: ularning mutlaqo boshqa-boshqa tushunchalar ekanligini Alisa va Tridi misolida qat'iy tushuntiring.
