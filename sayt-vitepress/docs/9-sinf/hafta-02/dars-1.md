---
title: "4-dars. Foydalanuvchi ssenariysi, User Flow va Customer Journey Map (CJM)"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf", "link": "/9-sinf/"}, "week": {"n": 2, "link": "/9-sinf/hafta-02/"}, "g": 4, "title": "Foydalanuvchi ssenariysi, User Flow va Customer Journey Map (CJM)", "lead": "Dizayn chiroyli tugmalardan emas, balki foydalanuvchining ilova ichida adashmay, o'z maqsadiga erishishidan boshlanadi. Ushbu darsda foydalanuvchi hikoyasi (ssenariy) yozish, harakatlar xaritasi (User Flow) va hissiyotlar yo'li (CJM)ni loyihalashni o'rganamiz.", "slide": "/slaydlar/9-sinf/hafta-02/dars-1.html", "tabs": [{"g": 4, "link": "/9-sinf/hafta-02/dars-1", "current": true}, {"g": 5, "link": "/9-sinf/hafta-02/dars-2", "current": false}, {"g": 6, "link": "/9-sinf/hafta-02/dars-3", "current": false}], "prev": null, "next": {"g": 5, "title": "Wireframe tushunchasi va Balsamiq dasturiga kirish", "link": "/9-sinf/hafta-02/dars-2"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Foydalanuvchi ssenariysi (User Scenario)** — muayyan personaning o'z maqsadiga yetish uchun ilovadan qanday foydalanishini ifodalovchi qisqa hayotiy hikoya.
- Har qanday yaxshi ssenariy 4 ta savolga javob beradi: Kim? Qayerda/qachon? Nima maqsad bilan? Qanday qadamlar bilan?
- **User Flow (Foydalanuvchi oqimi)** — ssenariydagi qadamlarning vizual blok-sxemasi (ekranlar, tugmalar va qaror qabul qilish nuqtalari).
- User Flow'da to'rtburchaklar ekranlarni, romblar qaror qabul qilish shartlarini (Ha / Yo'q), o'qlar esa harakat yo'nalishini bildiradi.
- User Flow foydalanuvchini ortiqcha bosqichlardan xalos qilishga va "tupik" (chiqib ketib bo'lmaydigan holatlar)ning oldini olishga xizmat qiladi.
- **Customer Journey Map (CJM)** — foydalanuvchining mahsulot bilan birinchi tanishuvidan to xarid/foydalanishgacha bo'lgan to'liq hissiy sayohati.
- CJM dagi eng muhim jihat — foydalanuvchining **og'riq nuqtalarini (pain points)** aniqlash va dizayn orqali ularga oson yechim topishdir.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### Ssenariy qanday qilib interfeys elementlariga aylanadi?
Ko'pincha boshlovchi dizaynerlar to'g'ridan-to'g'ri chiroyli ranglar va rasmlar chizishga kirishib ketishadi. Ammo ssenariy har bir tugma nima uchun kerakligini ko'rsatadi:
- Agar ssenariyda: "Ali qidiruvga o'z manzilini yozmoqda" deyilgan bo'lsa → ekranga **qidiruv qatori** kerak.
- Agar "Natijalar orasidan eng arzonini tanladi" deyilgan bo'lsa → natijalar ro'yxatida **narx va saralash (filter)** bo'lishi shart.
- Agar "Birgina bosish bilan buyurtma berdi" deyilgan bo'lsa → katta va qulay **harakatga chaqiruvchi tugma (CTA)** talab etiladi.

### User Flow tuzishdagi oltin qoidalar
1. **Bitta asosiy yo'l (Happy Path):** Avval foydalanuvchi hech qanday muammosiz to'g'ri maqsadga yetib boradigan eng qisqa yo'lni chizing.
2. **Kutilmagan holatlar (Edge Cases):** "Parol esdan chiqsa-chi?", "Internet uzilsa-chi?", "Savatda tovar qolmasa-chi?" kabi shartli romblarni qo'shing.
3. **Qadamlar sonini kamaytiring:** Har bir qo'shimcha bosqich yoki ortiqcha bosish (click) foydalanuvchilarning 10-20 foizini yo'qotishga olib keladi.

### CJM nima uchun kompaniyalar uchun million dollarlik vosita?
Customer Journey Map orqali kompaniyalar mijoz aynan qaysi soniyada ilovadan hafsalasi pir bo'lib, uni o'chirib tashlayotganini ko'rishadi. Masalan, taksi ilovasida "Manzilni kiritgandan so'ng haydovchi topilmadi" degan xabar mijozning eng og'riqli nuqtasi bo'lsa, dizayner unga boshqa tariflar yoki kutish vaqtini taklif qilish orqali mijozni saqlab qoladi.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| User Scenario | Foydalanuvchining ilovadan foydalanish hikoyasi |
| User Flow | Foydalanuvchi harakatlari va ekranlar ketma-ketligi blok-sxemasi |
| Happy Path | Foydalanuvchining to'siqlarsiz eng ideal va qisqa harakat yo'li |
| Decision Node (Romb) | User Flow da shartli qaror qabul qilish nuqtasi (Ha / Yo'q) |
| CJM (Customer Journey Map) | Mijozning mahsulot bilan muloqotidagi hissiy sayohati xaritasi |
| Pain Point (Og'riq nuqtasi) | Foydalanuvchi duch keladigan qiyinchilik, tushunmovchilik yoki to'siq |
| Touchpoint (Muloqot nuqtasi) | Foydalanuvchi brend yoki ilova bilan to'qnashadigan har qanday joy |
| CTA (Call to Action) | Foydalanuvchini asosiy amalni bajarishga undovchi tugma |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Amazon asoschisi Jeff Bezos o'z vaqtida veb-saytda "1-Click Ordering" (Bir bosishda buyurtma berish) User Flow'ini patentlagan va bu xususiyat kompaniyaga milliardlab dollar qo'shimcha daromad keltirgan.
- Yaxshi ishlab chiqilgan User Flow tufayli foydalanuvchi ilovada biror amalni bajarayotganda umuman o'ylanmaydi — bu UX sohasida "Don't Make Me Think" (Meni o'ylashga majbur qilma) qoidasi deb ataladi.
- CJM birinchi marta 1980-yillarda xizmat ko'rsatish sohasida paydo bo'lgan, ammo smartfonlar davrida raqamli ilovalarning eng muhim loyihalash quroliga aylandi.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Kundalik ssenariy yozing <Badge type="tip" text="oson" />
O'zingiz har kuni ishlatadigan biror mobil ilova (Telegram, Instagram yoki YouTube) orqali bitta vazifani bajarish ssenariysini 5-6 jumlada yozing (Kim? Qayerda? Nima maqsad? Qanday qadamlar?).

**Kutiladigan natija:** daftarda yoki Google Docs da yozilgan aniq ssenariy matni.

### 2. Oddiy User Flow (Choy tayyorlash) <Badge type="tip" text="oson" />
Ilovani chetga surib, hayotiy jarayon — "Choy damlash" uchun 4-5 qadamdan iborat blok-sxema chizing. Boshlanishi, harakatlari va yakuni bo'lsin.

**Kutiladigan natija:** to'rtburchaklar va o'qlardan iborat oddiy chizma (daftarda rasm yoki FigJam havolasi).

### 3. Ssenariydan UI elementlarini ajrating <Badge type="tip" text="oson" />
"Jasur onlayn pitsa buyurtma qilmoqda. U pitsa hajmini (kichik, o'rta, katta) tanladi, ustiga pishloq qo'shishni belgiladi va 'Buyurtma berish'ni bosdi." Ushbu ssenariy uchun qanday UI elementlari kerak bo'ladi?

**Kutiladigan natija:** kamida 4 ta interfeys elementi ro'yxati (masalan: radio tugma, checkbox, CTA tugmasi...).

### 4. Og'riq nuqtasini toping <Badge type="tip" text="oson" />
O'zingiz foydalangan biror sayt yoki ilovada sizni asabiylashtirgan, tushunarsiz bo'lgan bitta holatni (og'riq nuqtasi) yozing.

**Kutiladigan natija:** 2-3 jumlalik muammo tavsifi.

### 5. Parolni tiklash User Flow'i <Badge type="warning" text="o'rta" />
Foydalanuvchi parolini unutib qo'ydi. Uning parolini tiklash jarayoni (Login oynasi → "Parolni unutdingizmi?" → SMS kod kiritish → Yangi parol kiritish → Muvaffaqiyat) uchun User Flow chizing.

**Kutiladigan natija:** barcha qadamlar va o'tishlar to'g'ri ko'rsatilgan blok-sxema skrinshoti yoki chizmasi.

### 6. Shartli tarmoqlanish (Romb) bilan User Flow <Badge type="warning" text="o'rta" />
"Onlayn test topshirish" ilovasi uchun User Flow tuzing. Unda kamida bitta romb bo'lsin: "Barcha savollarga javob berildimi?". Agar Ha bo'lsa → Natijalar ekrani; Agar Yo'q bo'lsa → Javobsiz savollar ko'rsatilsin.

**Kutiladigan natija:** shartli shoxlanish (romb) to'g'ri ishlangan User Flow eskizi.

### 7. Tezkor ovqat buyurtma qilish ssenariysi <Badge type="warning" text="o'rta" />
Shoshilayotgan talaba uchun tushlik vaqtida kafedan oldindan pitsa buyurtma qilib, boriboq olib ketish ssenariysini yozing. Kontekst va cheklovlarni (vaqt ozligi, naqd pulsizlik) hisobga oling.

**Kutiladigan natija:** batafsil yozilgan foydalanuvchi hikoyasi (ssenariysi).

### 8. Mini Customer Journey Map (CJM) jadvali <Badge type="warning" text="o'rta" />
"Yangi poyabzal sotib olish" jarayoni uchun 4 ustunli CJM jadvalini tuzing: Bosqich | Foydalanuvchi harakati | Hissiy holati (+ / -) | Og'riq nuqtasi.

**Kutiladigan natija:** daftarda yoki jadval ko'rinishida to'ldirilgan CJM xaritasi.

### 9. "Mobile_Book" to'liq User Flow loyihasi <Badge type="danger" text="qiyin" />
Kitob qidirish, kitob haqida ma'lumot o'qish, tizimga kirish/kirmaslikni tekshirish va PDF yuklab olishni qamrab oluvchi to'liq User Flow chizing (FigJam, Miro yoki qog'ozda). Kamida 6 ta ekran va 2 ta qaror rombi bo'lsin.

**Kutiladigan natija:** to'liq va professional ko'rinishdagi blok-sxema (skrinshot yoki havola).

### 10. Og'riq nuqtasiga innovatsion dizayn yechimi <Badge type="danger" text="qiyin" />
Katta supermarket saytida foydalanuvchilar tovarlarni savatga solib, oxirgi bosqichda to'lov usuli murakkabligi sababli saytdan chiqib ketishmoqda. Siz UX dizayner sifatida bu muammoni qanday User Flow va UI yechimi bilan hal qilasiz? Tushuntiring va yangi oqim sxemasini chizing.

**Kutiladigan natija:** muammo tahlili, yangi User Flow va 1 sahifalik tavsif.

### 11. O'z startapingiz uchun to'liq CJM xaritasi <Badge type="info" text="bonus" />
O'zingiz o'ylab topgan yangi mobil ilova (masalan, maktab o'quvchilari uchun dars almashish ilovasi) uchun g'oyadan tortib to doimiy foydalanishgacha bo'lgan to'liq 5 bosqichli Customer Journey Map yarating.

**Kutiladigan natija:** ranglar, emotsiyalar va yechimlar ko'rsatilgan keng qamrovli CJM xaritasi (Figma/FigJam yoki chizilgan katta rasm).

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Foydalanuvchi ssenariysi (User Scenario) nega dizayn boshlanishidan oldin yozilishi kerak?
2. User Flow blok-sxemasida to'rtburchak va romb qanday ma'nolarni anglatadi?
3. "Happy Path" nima va u User Flow da qanday o'rin tutadi?
4. Customer Journey Map (CJM) odatiy User Flow'dan nima bilan farq qiladi?
5. "Og'riq nuqtasi" (Pain point) tushunchasini hayotiy misol bilan tushuntirib bering.

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

O'zingiz yoqtirgan biror xizmat (masalan, sevimli mobil banking yoki yetkazib berish ilovasi) orqali amal bajarish (masalan: telefon raqamga pul o'tkazish) ssenariysini yozing va uning kamida 5 ta qadamdan iborat User Flow sxemasini daftarga yoki onlayn doskaga chizing.

</div>

