---
title: "8-dars. Xavfsizlikni anglash (3-qism): tahdidlarni modellashtirish, Red/Blue Team va CTF"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (Cyber)", "link": "/10-sinf-cyber/"}, "week": {"n": 3, "link": "/10-sinf-cyber/hafta-03/"}, "g": 8, "title": "Xavfsizlikni anglash (3-qism): tahdidlarni modellashtirish, Red/Blue Team va CTF", "lead": "Xavfsizlikni anglash tushunchasi (3-qism): tahdidlarni modellashtirish, Red Team vs Blue Team va CTF asoslari", "slide": "/slaydlar/10-sinf-cyber/hafta-03/dars-2.html", "tabs": [{"g": 7, "link": "/10-sinf-cyber/hafta-03/dars-1", "current": false}, {"g": 8, "link": "/10-sinf-cyber/hafta-03/dars-2", "current": true}, {"g": 9, "link": "/10-sinf-cyber/hafta-03/dars-3", "current": false}], "prev": {"g": 7, "title": "Xavfsizlikni anglash (2-qism): raqamli gigiyena, brauzer xavfsizligi va 2FA", "link": "/10-sinf-cyber/hafta-03/dars-1"}, "next": {"g": 9, "title": "Tarmoq asoslari: mijoz-server arxitekturasi, topologiyalar, OSI va TCP/IP modellari", "link": "/10-sinf-cyber/hafta-03/dars-3"}}
---

---
title: "Xavfsizlikni anglash (3-qism): tahdidlarni modellashtirish, Red/Blue Team va CTF"
description: "Tahdidlarni modellashtirish (STRIDE), Red Team vs Blue Team mashqlari hamda Capture The Flag (CTF) musobaqalari asoslari"
dars: 2
hafta: 3
sinf: 10-sinf-cyber
---

<div class="blk">

## <Icon name="file-text" /> Reja

1. Tahdidlarni modellashtirish (Threat Modeling) tushunchasi.
2. Microsoft STRIDE tahdidlar modeli (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege).
3. Red Team (Hujumchilar) va Blue Team (Himoyachilar) amaliy mashg'ulotlari.
4. Capture The Flag (CTF) musobaqalari: Jeopardy va Attack-Defense formatlari.
5. Mashhur kiberhujumlar darsi: WannaCry va SolarWinds tahlili.
6. Amaliy laboratoriya: Maktab tizimi tahdid modeli va sodda CTF bayrog'ini topish.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Nazariy qism

### 1. Tahdidlarni modellashtirish nima?

**Tahdidlarni modellashtirish (Threat Modeling)** — bu axborot tizimini ishlab chiqish yoki yangilash jarayonida «Bizning tizimimizga kimlar hujum qilishi mumkin?», «Qanday yo'llar bilan zarar yetkazishi mumkin?» va «Ulardan qanday himoyalanamiz?» degan savollarga oldindan tizimli javob topish metodologiyasidir.

### 2. STRIDE tahdidlar modeli

Microsoft kompaniyasi tomonidan yaratilgan va bugungi kunda dunyo kiberxavfsizligi standarti bo'lgan **STRIDE** 6 ta tahdid toifasini o'z ichiga oladi:

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

---

### 3. Red Team vs Blue Team

Kiberxavfsizlikda nazariy bilimlarni sinash uchun harbiy o'yinlarga o'xshash mashg'ulotlar o'tkaziladi:
- **Red Team (Qizil jamoa):** Hujumchilar roli. Tizimdagi kamchiliklarni izlaydi, buzg'unchilik ssenariylarini amalga oshiradi, ijtimoiy muhandislik bilan xodimlarni chalg'itadi.
- **Blue Team (Ko'k jamoa):** Himoyachilar roli. Tarmoq xavfsizligini 24/7 nazorat qiladi, loglarni tahlil qiladi va Red Team hujumlarini to'xtatadi.
- **Purple Team:** Ikkala jamoaning birgalikda o'tirib xatolarni tahlil qilishi va himoya choralarini yangilashi.

---

### 4. Capture The Flag (CTF) musobaqalari

CTF — bu butun dunyo talaba va yoshlari o'rtasida o'tkaziladigan eng qiziqarli kiberxavfsizlik musobaqasidir. Unda ishtirokchilar maxsus zaif tizimlarni tahlil qilib, sirli «bayroq» (Flag) ni topishlari kerak.

**Asosiy kategoriyalar:**
- **Web:** Veb-sayt zaifliklari (SQLi, XSS, CSRF);
- **Cryptography:** Shifrlangan xabarlar va kalitlar;
- **Forensics:** Tarmoq trafigi (`.pcap`) va disk tasvirlaridan ma'lumot qidirish;
- **Reverse Engineering:** Dasturlarni tahlil qilish;
- **OSINT:** Ochiq internet manbalari orqali ma'lumot qidirish.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy laboratoriya

### 1-topshiriq: Maktab elektron jurnali uchun STRIDE tahlili
Quyidagi vaziyatlar STRIDE ning qaysi tahdidiga mos kelishini aniqlang:
1. O'quvchi o'qituvchining login-paroli bilan tizimga kirdi.
2. O'quvchi o'zining bahosini 3 dan 5 ga o'zgartirdi.
3. Bahoni kim o'zgartirganini aniqlash imkoni bo'lmadi (loglar yo'q).
4. Barcha o'quvchilarning shaxsiy ma'lumotlari internetga sizib chiqdi.
5. Imtihon vaqtida saytga sun'iy so'rovlar yuborilib, tizim qotirib qo'yildi.
6. Oddiy o'quvchi akkaunti butun maktab admini huquqiga ega bo'lib oldi.

### 2-topshiriq: Kriptografik CTF bayrog'ini topish
Quyidagi kodlangan matndan maxfiy bayroqni ajratib oling:
`U1RSSURFVEVTVF9GTEFHe2N5YmVyX21pbmRzZXRfMjAyNn0=`
(Yordam: Base64 dekoder vositasidan foydalaning).

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy topshiriqlar

### 1. STRIDE qisqartmasi ma'nosi &lt;Badge type="tip" text="oson" />
STRIDE dagi har bir harf qaysi tahdid turini ifodalashini inglizcha va o'zbekcha yozib chiqing.

### 2. Red Team va Blue Team roli &lt;Badge type="tip" text="oson" />
Kiberxavfsizlik mashg'ulotida Red Team va Blue Team jamoalarining asosiy vazifasi nimalardan iborat ekanini tushuntiring.

### 3. Repudiation (Inkor etish) tahdidi &lt;Badge type="warning" text="o'rta" />
Xodim o'zi bajargan xavfli moliyaviy operatsiyani «bu ishni men qilganim yo'q» deb inkor etmasligi uchun axborot tizimida qanday choralar bo'lishi shart?

### 4. Elevation of Privilege ssenariysi &lt;Badge type="warning" text="o'rta" />
Kompaniyaning oddiy amaliyotchisi (intern) qanday qilib butun tizim boshqaruvchisi (Administrator) darajasiga ko'tarilib olishi mumkin? Bunga qanday xavfsizlik kamchiligi sabab bo'ladi?

### 5. Purple Team tushunchasi &lt;Badge type="warning" text="o'rta" />
Nima sababdan zamonaviy xavfsizlikda faqat Red Team yoki faqat Blue Team yetarli emas deb hisoblanadi va Purple Team joriy etiladi?

### 6. CTF Jeopardy toifalari &lt;Badge type="tip" text="oson" />
Capture The Flag (CTF) musobaqalarida eng keng tarqalgan 4 ta toifani (Web, Crypto, Forensic, Reverse) sanang va qisqacha ta'riflang.

### 7. WannaCry hujumi tahlili &lt;Badge type="warning" text="o'rta" />
2017-yilda dunyo bo'ylab 200 mingdan ortiq kompyuterni zararlagan WannaCry hujumi qanday qilib bir necha soatda butun dunyoga tarqaldi?

### 8. Base64 kodlash tabiati &lt;Badge type="warning" text="o'rta" />
Nima sababdan Base64 kiberxavfsizlikda shifrlash (encryption) emas, balki oddiy kodlash (encoding) deb yuritiladi?

### 9. Least Privilege tamoyili &lt;Badge type="danger" text="qiyin" />
Kompaniyada barcha yangi kelgan xodimlarga har ehtimolga qarshi «Administrator» huquqi berib qo'yilsa, bu STRIDE ning qaysi tahdidlariga to'g'ridan-to'g'ri eshik ochadi?

### 10. Korxona tahdid modeli (Threat Model) &lt;Badge type="info" text="bonus" />
Onlayn ta'lim platformasi (masalan, masofaviy maktab) uchun STRIDE modeli asosida to'liq xavflar matritsasini ishlab chiqing.

---

</div>

<div class="blk">

## <Icon name="file-text" /> O'z-o'zini tekshirish savollari

1. Threat Modeling nima uchun dastur yaratishdan oldin o'tkaziladi?
2. STRIDE modeli qaysi korporatsiya tomonidan ishlab chiqilgan?
3. Red Team a'zolari o'zlarini kimning o'rniga qo'yib ko'radi?
4. CTF musobaqasida «bayroq» (flag) nima vazifani bajaradi?
5. Tizimda admin imtiyozlarini noqonuniy oshirish qanday ataladi?

---

</div>

<div class="blk">

## <Icon name="file-text" /> Foydali manbalar

- Microsoft Threat Modeling Tool Documentation.
- OWASP Threat Dragon Project.
- CTFtime Global CTF Archive: `ctftime.org`

</div>

