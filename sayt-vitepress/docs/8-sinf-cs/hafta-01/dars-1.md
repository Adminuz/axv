---
title: "1-dars. Zamonaviy kompyuterlar va ularning arxitekturasi"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "8-sinf (Foundation)", "link": "/8-sinf-cs/"}, "week": {"n": 1, "link": "/8-sinf-cs/hafta-01/"}, "g": 1, "title": "Zamonaviy kompyuterlar va ularning arxitekturasi", "lead": "Har kuni foydalanadigan kompyuteringiz aslida qanday ishlaydi? Ushbu darsda kompyuterning «ichki dunyosi»ga sayohat qilamiz: protsessor, tezkor xotira, fon Neyman arxitekturasi va kompyuterning yashirin texnik parametrlarini ochishni o'rganamiz.", "slide": "/slaydlar/8-sinf-cs/hafta-01/dars-1.html", "test": "/slaydlar/8-sinf-cs/hafta-01/dars-1-test.html", "tabs": [{"g": 1, "link": "/8-sinf-cs/hafta-01/dars-1", "current": true}, {"g": 2, "link": "/8-sinf-cs/hafta-01/dars-2", "current": false}, {"g": 3, "link": "/8-sinf-cs/hafta-01/dars-3", "current": false}], "prev": null, "next": {"g": 2, "title": "Operatsion tizimlar va Windows muhitida ishlash", "link": "/8-sinf-cs/hafta-01/dars-2"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Kompyuter** — axborotni kiritish, saqlash, qayta ishlash va chiqarib beruvchi universal elektron qurilma.
- **Asosiy turlari:** Desktop (ish stoli kompyuteri), Laptop (noutbuk), Monoblok, Server va Superkompyuter.
- **Fon Neyman arxitekturasi:** har qanday kompyuter 4 ta tayanch blokdan iborat: protsessor (CPU), xotira (RAM/ROM), kiritish qurilmalari va chiqarish qurilmalari.
- **CPU (Markaziy protsessor)** — kompyuterning «miyasi». Uning asosiy kuchi takt chastotasi (GHz) va yadrolar soniga (Cores) bog'liq.
- **RAM (Tezkor xotira)** — dasturlar ishlab turishi uchun vaqtinchalik juda tezkor xotira. Kompyuter o'chirilganda undagi barcha narsa o'chadi.
- **SSD va HDD (Doimiy xotira)** — fayllarni doimiy saqlovchi xotira. SSD mikrochiplarda ishlaydi va mexanik HDD dan 5–30 baravar tezroq ishlaydi.
- **Ona plata (Motherboard)** — barcha qismlarni bir-biriga ulab, elektr quvvati va ma'lumot almashinuv shinalari bilan ta'minlovchi bosh plata.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### Kompyuter va inson tanasi: ajoyib o'xshatish
Kompyuterning qismlarini yaxshiroq tushunish uchun ularni inson a'zolari bilan taqqoslash mumkin:
- **CPU (Protsessor):** Inson miyasi. Barcha hisoblashlar, mantiqiy qarorlar va buyruqlar shu yerda paydo bo'ladi.
- **RAM (Tezkor xotira):** Insonning qisqa muddatli xotirasi. Masalan, sizga aytilgan 7 xonali telefon raqamini hozir eslab turasiz, lekin 2 soatdan keyin unutasiz.
- **SSD/HDD (Doimiy xotira):** Insonning uzoq muddatli xotirasi yoki qalin daftari. O'rganilgan bilimlar, bolalik xotiralari yillar davomida saqlanadi.
- **Ona plata:** Asab tizimi va qon tomirlari. Miyadan chiqqan signallar va ozuqa barcha a'zolarga aynan shu orqali yetkaziladi.
- **Kiritish qurilmalari (Klaviatura, sichqoncha):** Ko'z, quloq, qo'l teginishi. Atrofdan axborot qabul qiladi.
- **Chiqarish qurilmalari (Monitor, dinamik):** Ovoz va yuz harakatlari. Ichki natijani tashqariga bildiradi.

### Nega kompyuter o'chganda ochilgan dasturlar yopiladi?
Ko'pchilik boshlang'ich o'rganuvchilar Word faylida matn yozib, saqlash (Ctrl+S) tugmasini bosmasdan kompyuterni o'chirib qo'yishadi va hamma yozganlari yo'qolganidan xafa bo'lishadi. 
Buning sababi — siz dasturni ochganingizda u **RAM (operativ xotira)** ichida ishlaydi. RAM juda tez ishlaydi, lekin u «uchuvchan» xotiradir: unga elektr toki kelib tursagina ma'lumotni ushlab turadi. Tok uzilishi bilan RAM ichidagi hamma narsa bo'shab qoladi. Faqat `Saqlash` (Save) buyrug'ini berganingizdagina ma'lumot RAM dan doimiy diskka (SSD yoki HDD ga) ko'chiriladi.

### Protsessordagi takt chastotasi (GHz) nima?
Protsessor sekundiga millionlab va milliardlab mayda qadamlarni bajaradi. Har bir qadam **takt** deyiladi. 
Agar protsessorning ko'rsatkichida `3.5 GHz` deb yozilgan bo'lsa, bu protsessor birgina sekund ichida 3 milliard 500 million marta elektr amalini bajara oladi deganidir. Protsessorda yadrolar qancha ko'p bo'lsa, u bir vaqtning o'zida shuncha ko'p vazifani (masalan, o'yin o'ynash, fonda musiqa tinglash va fayl yuklash) bir-biriga xalaqit bermasdan parallel bajara oladi.

### Odatiy xato: RAM bilan doimiy diskni adashtirish
Ko'pincha yangi boshlovchilar telefon yoki kompyuter sotib olayotganda: «Menda 512 GB operativ xotira bor» deb aytishadi. Bu mutlaqo noto'g'ri! 
512 GB — bu **doimiy xotira (SSD yoki xotira kartasi)**, ya'ni rasm, kino va o'yinlar saqlanadigan joy. Operativ xotira (RAM) esa odatda 8 GB, 16 GB yoki 32 GB bo'ladi. RAM hajmi kompyuter bir vaqtda qancha dasturni qotmasdan ochib tura olishini belgilaydi.

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **CPU (Central Processing Unit)** | Markaziy protsessor — barcha arifmetik va mantiqiy amallarni bajaruvchi asosiy hisoblash mikrosxemasi. |
| **RAM (Random Access Memory)** | Tezkor xotira — kompyuter yoqiq bo'lgan paytda ishlayotgan dastur va ma'lumotlarni saqlovchi vaqtinchalik xotira. |
| **ROM (Read Only Memory)** | Doimiy xotira — kompyuterni ishga tushirish uchun zarur tizim dasturlarini o'zida saqlovchi mikrosxema. |
| **Motherboard (Ona plata)** | Barcha kompyuter komponentlarini birlashtiruvchi markaziy elektron plata. |
| **SSD (Solid State Drive)** | Qattiq jismli disk — flesh-xotira chiplari asosida ishlovchi o'ta tezkor doimiy saqlash qurilmasi. |
| **HDD (Hard Disk Drive)** | Qattiq magnit disk — aylanuvchi magnit plastinkalar asosida ishlovchi an'anaviy xotira qurilmasi. |
| **GPU (Graphics Processing Unit)** | Grafik protsessor (videokarta) — tasvir, video va 3D grafikalarni ekranga chiqaruvchi qurilma. |
| **Takt chastotasi** | Protsessorning bir sekundda bajara oladigan sikllari (amallari) soni, gigagersda (GHz) o'lchanadi. |
| **Task Manager** | Windows operatsion tizimining joriy yuklama va kompyuter parametrlarini ko'rsatuvchi dispetcheri. |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

1. Dunyodagi ilk elektron kompyuterlardan biri hisoblangan **ENIAC** (1945-yil) taxminan 27 tonna og'irlikda bo'lgan va butun bir katta xonani (167 kvadrat metr) egallagan. Bugungi kunda cho'ntagingizdagi oddiy smartfon ENIAC dan millionlab marta kuchliroq!
2. Jon fon Neyman 1945-yilda taklif qilgan kompyuter arxitekturasi prinsiplari oradan 80 yildan ortiq vaqt o'tgan bo'lsa-da, bugungi kunda ham dunyodagi deyarli barcha kompyuter, noutbuk va smartfonlarning asosi hisoblanadi.
3. Zamonaviy mikroprotsessorlar ichida inson soch tolasidan minglab marta ingichka bo'lgan **milliardlab tranzistorlar** (masalan, zamonaviy chiplarda 15–50 milliard tranzistor) joylashgan.
4. Kompyuterdagi qattiq disk (HDD) plastinkasi daqiqasiga 5400 yoki 7200 marta aylanadi — bu poyga avtomobili motorining aylanish tezligiga teng!

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Qurilmalarni saralash <Badge type="tip" text="oson" />
Quyida berilgan qurilmalarni ikki guruhga ajrating: **Kiritish qurilmalari** va **Chiqarish qurilmalari**.
Ro'yxat: Monitor, klaviatura, sichqoncha, printer, veb-kamera, dinamik (kolonka), skaner, proyektor, naushnik, mikrofon.
**Kutiladigan natija:** 10 ta qurilma daftarga ikkita alohida ustun shaklida to'g'ri guruhlanadi.

### 2. Task Manager'ni ochish <Badge type="tip" text="oson" />
Klaviaturadagi qisqa tugmalar orqali Windows Vazifalar boshqaruvchisini (Task Manager) oching va o'z kompyuteringizning operativ xotirasi (RAM) hajmini aniqlang.
**Kutiladigan natija:** Qaysi tugmalar bosilgani va ekranda ko'ringan RAM hajmi (masalan, 8 GB yoki 16 GB) yoziladi.

### 3. Kompyuter turlarini taqqoslash <Badge type="tip" text="oson" />
Statsionar kompyuter (Desktop) va Noutbukning (Laptop) 2 tadan ustunligi hamda kamchiligini yozing.
**Kutiladigan natija:** Jadvalda har ikkala kompyuter turining o'lcham, qulaylik va yangilash imkoniyatlari bo'yicha farqi ko'rsatiladi.

### 4. Fon Neyman modelini chizish <Badge type="tip" text="oson" />
Daftaringizga fon Neyman kompyuter arxitekturasining 4 ta asosiy blokini (CPU, Xotira, Kiritish, Chiqarish) va ularni bog'lovchi tizimli shinani blok-sxema sifatida chizing.
**Kutiladigan natija:** To'g'ri o'qlar va blok nomlari ko'rsatilgan sxema chizmasi.

### 5. dxdiag orqali videokartani aniqlash <Badge type="warning" text="o'rta" />
`Win + R` tugmalarini bosing, `dxdiag` buyrug'ini kiriting va ochilgan oynaning «Display» bo'limidan o'z kompyuteringizdagi videokartaning (GPU) aniq nomini va ishlab chiqaruvchisini (Intel, AMD, Nvidia) toping.
**Kutiladigan natija:** Videokarta modeli va ishlab chiqaruvchi nomi to'liq yoziladi.

### 6. msinfo32 hisoboti <Badge type="warning" text="o'rta" />
`msinfo32` buyrug'i orqali tizim haqidagi ma'lumotlarni oching. Protsessoringizning takt chastotasini va jismoniy yadrolar sonini (Cores) aniqlang.
**Kutiladigan natija:** Protsessor nomi, chastotasi (GHz) va yadrolar soni qayd etiladi.

### 7. RAM va SSD farqini tahlil qilish <Badge type="warning" text="o'rta" />
Nima uchun kompyuterga bir vaqtning o'zida ham RAM, ham SSD kerak? Nega barcha ma'lumotlarni faqat bitta turdagi xotirada saqlab bo'lmaydi?
**Kutiladigan natija:** Xotira narxi, tezligi va uchuvchanlik xususiyati asosida 3-4 jumlalik tushuntirish yoziladi.

### 8. Kompyuter xarid qilish ssenariysi <Badge type="warning" text="o'rta" />
Siz do'stingizga dasturlash va o'qish uchun noutbuk tanlashda yordam bermoqchisiz. Quyidagi ikki variantdan qaysi birini tanlaysiz va nima uchun?
- A variant: Intel Core i3, 4 GB RAM, 1 TB HDD.
- B variant: Intel Core i5, 16 GB RAM, 512 GB SSD.
**Kutiladigan natija:** Dasturchi uchun B varianti nima sababdan afzal ekanligi RAM va SSD tezligi misolida asoslanadi.

### 9. Superkompyuterlar bo'yicha kichik tadqiqot <Badge type="danger" text="qiyin" />
Internet yoki ma'lumotnomalardan foydalanib, hozirgi kunda dunyodagi eng kuchli superkompyuterlardan biri haqida ma'lumot to'plang (masalan, Frontier yoki Fugaku). U qayerda joylashgan va qanday vazifalarni bajaradi?
**Kutiladigan natija:** Superkompyuter nomi, mamlakati va qaysi sohalarda ishlatilishi haqida qisqacha ma'lumotnoma.

### 10. Protsessor arxitekturasi va kesh xotira <Badge type="danger" text="qiyin" />
Protsessor ichida RAM dan ham tezroq ishlaydigan **L1, L2, L3 kesh xotira (Cache)** mavjud. Task Manager yoki internetdan kesh xotira nima uchun kerakligini va uning vazifasini aniqlang.
**Kutiladigan natija:** Kesh xotiraning CPU va RAM o'rtasidagi ko'prik vazifasini o'tashi haqida aniq xulosa.

### 11. Kelajak kompyuterlari: Kvant kompyuteri nima? <Badge type="info" text="bonus" />
An'anaviy kompyuterlar ma'lumotni bit (0 yoki 1) ko'rinishida saqlaydi. Kvant kompyuterlarida esa **kubit (qubit)** ishlatiladi. Kubitning an'anaviy bitdan asosiy sehrli farqi nima va u qanday yangi imkoniyatlar ochadi?
**Kutiladigan natija:** Kubitning bir vaqtning o'zida ham 0, ham 1 holatida (superpozitsiya) bo'la olishi haqida tushuntirish.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Zamonaviy kompyuterlarning qanday asosiy turlarini bilasiz?
2. Jon fon Neyman arxitekturasi qaysi 4 ta asosiy blokdan iborat?
3. Protsessorning (CPU) asosiy vazifasi nima va uning kuchi nimalarga bog'liq?
4. Operativ xotira (RAM) bilan doimiy xotira (SSD/HDD) o'rtasidagi 2 ta tub farqni ayting.
5. Nima uchun zamonaviy kompyuterlarda HDD o'rniga SSD o'rnatilmoqda?
6. Ona plata (Motherboard) kompyuterda qanday rolni bajaradi?
7. Windowsda kompyuter parametrlarini ko'rish uchun qaysi dastur va buyruqlar ishlatiladi?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Uyda yoki maktabdagi kompyuterda `Ctrl + Shift + Esc` (Task Manager) va `Win + R` → `msinfo32` orqali o'z kompyuteringiz xususiyatlarini aniqlang va daftaringizga quyidagi ma'lumotlarni yozing:
1. Kompyuter turi va operatsion tizim nomi.
2. Protsessor modeli, chastotasi va yadrolari soni.
3. O'rnatilgan operativ xotira (RAM) hajmi.
4. Doimiy xotira turi (SSD yoki HDD) va bo'sh joy miqdori.
5. Kompyuteringizga ulangan 2 ta kiritish va 2 ta chiqarish qurilmasi.
Vazifani bajarishga 20 daqiqa vaqt ajrating.

</div>

