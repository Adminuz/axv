---
title: "3-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "10-sinf (Cyber)", "link": "/10-sinf-cyber/"}, "n": 3, "bob": "I-bob · Kiberxavfsizlikka kirish", "lessons": [{"g": 7, "title": "Xavfsizlikni anglash (2-qism): raqamli gigiyena, brauzer xavfsizligi va 2FA", "lead": "Xavfsizlikni anglash tushunchasi (2-qism): raqamli gigiyena, brauzer xavfsizligi va ikki bosqichli autentifikatsiya (2FA)", "link": "/10-sinf-cyber/hafta-03/dars-1", "slide": "/slaydlar/10-sinf-cyber/hafta-03/dars-1.html"}, {"g": 8, "title": "Xavfsizlikni anglash (3-qism): tahdidlarni modellashtirish, Red/Blue Team va CTF", "lead": "Xavfsizlikni anglash tushunchasi (3-qism): tahdidlarni modellashtirish, Red Team vs Blue Team va CTF asoslari", "link": "/10-sinf-cyber/hafta-03/dars-2", "slide": "/slaydlar/10-sinf-cyber/hafta-03/dars-2.html"}, {"g": 9, "title": "Tarmoq asoslari: mijoz-server arxitekturasi, topologiyalar, OSI va TCP/IP modellari", "lead": "Tarmoq asoslari: mijoz-server arxitekturasi, topologiyalar, OSI va TCP/IP modellari", "link": "/10-sinf-cyber/hafta-03/dars-3", "slide": "/slaydlar/10-sinf-cyber/hafta-03/dars-3.html"}]}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Ushbu haftada o'tilgan darslar bo'yicha mustaqil amaliy uyga vazifalar ro'yxati:

---

### 7-dars. Raqamli gigiyena va shaxsiy kiberxavfsizlik
1. O'zingiz muntazam foydalanadigan brauzeringizga (Chrome, Firefox yoki Edge) `uBlock Origin` va `ClearURLs` kengaytmalarini o'rnating. Har qanday 3 ta ommabop yangiliklar saytiga kirib, qancha kuzatuvchi (tracker) va reklama skriptlari bloklanganini qayd eting.
2. Shaxsiy kompyuteringiz yoki smartfoningizda shifrlangan xavfsiz DNS serverini (Cloudflare `1.1.1.1` yoki `1.1.1.2` zararli dasturlardan himoyalangan DNS) sozlang. Sozlash jarayonini skrinshotlar orqali hujjatlashtiring.
3. Telegram yoki Google hisobingizda 2-bosqichli tasdiqlash (2FA) yoqilganligini tekshiring, agar yoqilmagan bo'lsa yoqing va maxfiy tiklash kodi/parolini ishonchli offline joyda saqlang.

---

### 8-dars. STRIDE tahdid modeli, Red Team vs Blue Team va CTF musobaqalari
1. O'zingiz bilgan bitta onlayn servis (masalan, maktab oshxonasi to'lov ilovasi yoki onlayn kutubxona tizimi) uchun STRIDE modeli bo'yicha tahdidlar tahlili jadvalini to'ldiring:
   - **S (Spoofing):** Birov boshqa o'quvchi nomidan tizimga kirish xavfi;
   - **T (Tampering):** Hisobdagi balans yoki kitob ma'lumotlarini o'zgartirish xavfi;
   - **R (Repudiation):** O'tkazilgan to'lov yoki olingan kitobni rad etish xavfi;
   - **I (Information Disclosure):** O'quvchilar telefon raqamlari yoki parollarining oqib ketishi;
   - **D (Denial of Service):** Tizimni ko'p so'rovlar yuborib ishdan chiqarish;
   - **E (Elevation of Privilege):** Oddiy o'quvchining administrator huquqiga ega bo'lib olishi.
2. Red Team va Blue Team rollarini solishtiruvchi qisqa esse (1 sahifa) yozing: nega tashkilotlar uchun faqat himoyalanish (Blue Team) yetarli emas va doimiy mustaqil sinovlar (Red Team) talab etiladi?
3. CTF musobaqalarining asosiy yo'nalishlari (Web, Forensics, Reverse, Pwn, Crypto) bo'yicha konspekt tuzing.

---

### 9-dars. Tarmoq asoslari: topologiyalar, OSI modeli va TCP/IP steki
1. Yulduzsimon (Star) va To'rsimon (Mesh) topologiyalarining kamida 3 tadan afzallik va kamchiliklarini taqqoslovchi jadval tuzing. Nima sababdan hozirgi zamonaviy lokal tarmoqlarda yulduzsimon topologiya keng qo'llaniladi?
2. OSI modelining 7 ta qatlamini tartib bilan yozing va har bir qatlamda ishlaydigan kamida bittadan protokol yoki qurilmani ko'rsating.
3. TCP va UDP protokollari o'rtasidagi farqni tushuntiring:
   - Nima sababdan veb-saytlarni yuklashda (HTTP/HTTPS) va fayl uzatishda TCP ishlatiladi?
   - Nima sababdan onlayn o'yinlar, videoqo'ng'iroqlar va jonli efirlarda UDP afzal ko'riladi?
4. Kompyuteringiz terminalida `ping` va `traceroute` (yoki Windowsda `tracert`) buyruqlari orqali `google.com` yoki `edu.uz` manziliga tarmoq marshrutini tahlil qiling va natijalarni yozib oling.

---

</div>
