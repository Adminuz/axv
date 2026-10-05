---
title: "6-dars. Kompyuter xavfsizligi va antivirus dasturlari"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "8-sinf (Foundation)", "link": "/8-sinf-cs/"}, "week": {"n": 2, "link": "/8-sinf-cs/hafta-02/"}, "g": 6, "title": "Kompyuter xavfsizligi va antivirus dasturlari", "lead": "Kompyuterni kiberxatarlardan himoyalash, zararli dasturlar turlari, antiviruslarning ishlash sirlari hamda mustahkam parollar yaratish madaniyati.", "slide": "/slaydlar/8-sinf-cs/hafta-02/dars-3.html", "test": "/slaydlar/8-sinf-cs/hafta-02/dars-3-test.html", "tabs": [{"g": 4, "link": "/8-sinf-cs/hafta-02/dars-1", "current": false}, {"g": 5, "link": "/8-sinf-cs/hafta-02/dars-2", "current": false}, {"g": 6, "link": "/8-sinf-cs/hafta-02/dars-3", "current": true}], "prev": {"g": 5, "title": "Internet, brauzerlar va elektron pochta bilan ishlash", "link": "/8-sinf-cs/hafta-02/dars-2"}, "next": null}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Kompyuter xavfsizligi:** Qurilma apparati, operatsion tizim va saqlanayotgan shaxsiy ma'lumotlarni ruxsatsiz kirish, yo'qotish yoki zararlanishdan himoya qilish chora-tadbirlaridir.
- **CIA tamoyili:** Axborot xavfsizligining uchta asosi — Maxfiylik (Confidentiality), Yaxlitlik (Integrity) va Mavjudlik (Availability).
- **Zararli dasturlar (Malware):** Viruslar (fayllarga yopishuvchi), troyanlar (niqoblangan dasturlar), chuvalchanglar (tarmoq orqali o'zi tarqaluvchi), ayg'oqchi dasturlar (spyware) va tovlamachi shifrlash viruslari (ransomware).
- **Antivirus mexanizmlari:** Real vaqtda himoya (real-time), imzo tahlili (signature matching), evristik tahlil (xatti-harakatni tekshirish) va xavfli fayllarni karantinga olish.
- **Parol xavfsizligi:** Kamida 12 belgidan iborat, katta-kichik harflar, raqamlar va maxsus belgilar qatnashgan yagona parollar yaratish hamda 2FA (ikki bosqichli tasdiqlash) tizimini yoqish.
- **Tashqi xotira kibergigiyenasi:** Har qanday begona fleshkani kompyuterga ulagach, darhol antivirus orqali to'liq tekshirish va avtomatik ishga tushirishni bloklash.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Ransomware (Tovlamachi viruslar) qanday ishlaydi va undan qanday himoyalanish mumkin?

Ransomware — bugungi kunda dunyodagi eng xavfli kiberxatarlardan biridir.
- **Hujum mexanizmi:** Foydalanuvchi elektron pochtadagi shubhali ilovani ochganda yoki qaroqchi (pirat) o'yinni yuklab olganda virus ishga tushadi. U kompyuterdagi barcha fotosuratlar, oilaviy arxivlar, hujjatlar va ma'lumotlar bazalarini murakkab matematik kriptografik algoritmlar bilan shifrlab qulflaydi. Shundan so'ng ekranda banner paydo bo'ladi: «Fayllaringiz shifrlangan. 3 kun ichida 500 dollar to'lamasangiz, barcha ma'lumotlar o'chib ketadi».
- **Asosiy himoya usuli:** Hech qachon tovlamachilarga pul to'lamaslik kerak (chunki pul to'langanda ham kod berilmasligi 80% holatlarda kuzatiladi). Eng yagona va ishonchli himoya — **muntazam zaxira nusxa (Backup)** yaratishdir! Muhim fayllaringizni kompyuterga ulanmagan tashqi qattiq diskda yoki bulutda (Google Drive, OneDrive) saqlang.

### 2. Antivirus qanday qilib hali noma'lum yangi viruslarni aniqlaydi? Evristik tahlil

Ko'pchilik antivirus faqat o'z bazasida bor viruslarnigina taniydi deb o'ylaydi. Bu **imzo (signature)** tahlili deyiladi. Ammo dunyoda har kuni 400 000 dan ortiq yangi zararli kodlar yaratiladi.
- Yangi viruslarni aniqlash uchun zamonaviy antiviruslar **Evristik tahlil (Heuristic Analysis)** usulidan foydalanadi.
- Antivirus faylni alohida xavfsiz virtual muhitda («Sandbox» — qumdon) sinov tariqasida yurgizib ko'radi. Agar fayl Windows tizim papkalarini yashirincha o'zgartirishga, boshqa fayllarni shifrlashga yoki internetdagi noma'lum serverga parollarni yuborishga harakat qilsa, antivirus uni hali bazada yo'q bo'lsa ham xavfli deb hisoblaydi va bloklaydi.

### 3. Karantin nima va u faylni o'chirishdan nimasi bilan farq qiladi?

Antivirus shubhali faylni topganda uni darhol o'chirib tashlamay, ko'pincha **Karantin (Quarantine)**ga joylaydi:
- Karantin — bu diskdagi maxsus shifrlangan va izolyatsiya qilingan xavfsiz papka.
- Undagi fayl boshqa hech qanday dastur bilan aloqa qila olmaydi va operatsion tizimga zarar yetkazolmaydi.
- Agar antivirus tasodifan kerakli ishchi faylingizni xato qilib xavfli deb gumon qilgan bo'lsa («False Positive»), siz karantinga kirib o'sha faylni qayta tiklashingiz mumkin.

### 4. 2FA (Ikki bosqichli autentifikatsiya) nima uchun 100% zarur?

Tasavvur qiling, uyingizning eshigida ikkita qulf bor: bittasi oddiy kalit (parol), ikkinchisi esa faqat sizning qo'lingizdagi telefonga keladigan bir martalik SMS kod.
- Agar biror firibgar sizning kalitingizni ko'rib olib nusxasini yasasa ham (parolingizni o'g'irlasa ham), u uyingizga kira olmaydi, chunki ikkinchi kalit (telefoningiz) sizning yoningizda bo'ladi.
- Ayniqsa, Telegram, Google va ijtimoiy tarmoqlarda 2FA funksiyasini yoqib qo'yish akkauntingizni o'g'irlanishdan 99.9% himoya qiladi.

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Kompyuter xavfsizligi** | Tizim, apparat va ma'lumotlarni ruxsatsiz aralashuv hamda yo'qotishdan asrash choralari |
| **Malware** | Foydalanuvchiga yoki tizimga zarar yetkazish uchun mo'ljallangan har qanday zararli dasturiy ta'minot |
| **Klassik virus** | Boshqa dastur va fayllarga yopishib, o'z kodini ko'paytiruvchi zararli dastur |
| **Troyan (Trojan)** | Foydali dastur yoki o'yin qiyofasida yashiringan, tizimni masofadan boshqarishga imkon beruvchi kod |
| **Ransomware** | Foydalanuvchi fayllarini shifrlab qulflab, ochish evaziga tovlamachilik bilan to'lov talab qiluvchi virus |
| **Spyware** | Foydalanuvchi amallarini, klaviatura tugmalarini (keylogger) pinhona kuzatuvchi ayg'oqchi dastur |
| **Antivirus** | Zararli dasturlarni topuvchi, xolislovchi va yo'q qiluvchi maxsus himoya dasturi |
| **Karantin (Quarantine)** | Shubhali fayllarni operatsion tizimdan to'liq ajratib saqlovchi xavfsiz izolyatsiya muhiti |
| **2FA (Two-Factor Auth)** | Akkauntga kirishda paroldan tashqari ikkinchi tasdiqlash omilini talab qiluvchi xavfsizlik tizimi |
| **Zaxira nusxa (Backup)** | Ma'lumotlar yo'qolishining oldini olish uchun fayllarni boshqa xavfsiz xotiraga ko'chirib saqlash |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

1. **Ilk kompyuter virusi:** 1986-yilda ikki pokistonlik aka-uka Amjad va Basit Farooq Alvi tomonidan «Brain» nomli birinchi shaxsiy kompyuter virusi yaratilgan. U moslashuvchan disklar (floppy disk) orqali tarqalgan.
2. **Eng mashhur parollar:** Har yili e'lon qilinadigan «Eng ko'p buzilgan parollar» reytingida hali ham `123456`, `password`, `12345678` va `qwerty` so'zlari birinchi o'rinlarda turadi. Bunday parollar bir necha millisoniyada buziladi!
3. **WannaCry epidemiyasi:** 2017-yilda «WannaCry» shifrlash virusi dunyoning 150 dan ortiq davlatidagi 200 000 dan ortiq kompyuterlarni (jumladan, kasalxonalar, banklar va temir yo'llarni) bir necha soat ichida ishdan chiqargan.
4. **Kunlik tahdidlar:** Dunyo bo'ylab kiberxavfsizlik laboratoriyalari har kuni o'rtacha 450 000 ta yangi zararli dastur namunalarini qayd etadi.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Windows Security holatini tekshirish <Badge type="tip" text="oson" />
Kompyuteringizda `Win + I` tugmalarini bosib Sozlamalarga kiring. «Privacy & security» bo'limidan «Windows Security»ni oching. Tizimdagi «Virus & threat protection» va «Firewall & network protection» bo'limlarida yashil tasdiq belgisi (himoya yoqilganligi) borligini tekshiring.
**Kutiladigan natija:** O'quvchi operatsion tizimning xavfsizlik markazini ochadi va barcha himoya qatlamlari faol ekanligiga ishonch hosil qiladi.

### 2. Tezkor skanerlash (Quick scan) o'tkazish <Badge type="tip" text="oson" />
Windows Security oynasida «Virus & threat protection» bo'limiga kiring va «Quick scan» tugmasini bosing. Tekshiruv davomida nechta fayl tekshirilgani va necha soniya vaqt ketganini daftaringizga yozib oling.
**Kutiladigan natija:** Tezkor skanerlash jarayoni muvaffaqiyatli yakunlanadi, fayllar soni va sarflangan vaqt qayd etiladi.

### 3. Antivirus bazasi yangilanishini tekshirish <Badge type="tip" text="oson" />
«Virus & threat protection» sahifasini pastroqqa tushiring va «Virus & threat protection updates» bandini toping. «Check for updates» (Yangilanishlarni tekshirish) tugmasini bosing va kompyuterga eng oxirgi viruslar bazasi yuklanganini tasdiqlang.
**Kutiladigan natija:** Antivirus bazasi oxirgi versiyagacha yangilanadi va oxirgi yangilanish vaqti ko'rsatiladi.

### 4. Parol kuchini tekshirish <Badge type="tip" text="oson" />
Quyidagi parollarni zaif, o'rta yoki kuchli toifaga ajrating va sababini tushuntiring:
1. `jasur2010`
2. `Admin123!`
3. `J@sur#K!ber_8Sinf`
4. `qwertyuiop`
**Kutiladigan natija:** 1 va 4 zaif (oson topiladi, oddiy so'zlar); 2 o'rta (standart andoza); 3 kuchli (17 belgi, aralash belgilar, ma'noli ibora).

### 5. Fleshkani xavfsiz skanerlash amaliyoti <Badge type="warning" text="o'rta" />
Kompyuteringizga USB fleshka ulang. «This PC» oynasida fleshka belgisini toping, sichqonchaning o'ng tugmasini bosib kontekst menyusidan «Scan with Microsoft Defender»ni ishga tushiring. Tekshiruv natijasi qanday bo'lganini ko'ring.
**Kutiladigan natija:** O'quvchi alohida tashqi xotira diskini to'g'ri skanerlashni o'rganadi.

### 6. Shubhali faylni karantinga yuborish mexanizmini tahlil qilish <Badge type="warning" text="o'rta" />
Windows Security sozlamalaridagi «Protection history» (Himoya tarixi) bo'limiga kiring. Agar avval kompyuteringizda biror shubhali fayl bloklangan bo'lsa, uning nomi va amal turi (Quarantine/Removed) bilan tanishing. Karantindagi fayl nega kompyuterga zarar yetkaza olmasligini daftaringizga 2 ta gap bilan izohlang.
**Kutiladigan natija:** O'quvchi karantin funksiyasining izolyatsiya qilish mohiyatini tushuntirib bera oladi.

### 7. Parol boshqaruvchi (Password Manager) tamoyili <Badge type="warning" text="o'rta" />
Brauzerlarda (Chrome, Edge) o'rnatilgan parollarni saqlash tizimi qanday ishlashini o'rganing (`Settings -> Autofill and passwords -> Password Manager`). Unda parollarni ko'rish uchun nima sababdan Windows foydalanuvchisi paroli yoki PIN-kodi talab qilinishini aniqlang.
**Kutiladigan natija:** Parol menejerining shaxsiy ma'lumotlarni qanday himoyalashi va asosiy master-parol roli tushuntiriladi.

### 8. Shaxsiy 2FA himoyasini tahlil qilish <Badge type="warning" text="o'rta" />
O'zingiz foydalanadigan Telegram yoki Google hisobingiz xavfsizlik sozlamalariga kiring (`Settings -> Privacy and Security -> Two-Step Verification`). 2FA yoqilganligini tekshiring. Agar yoqilmagan bo'lsa, ota-onangiz yoki ustozingiz nazoratida ikkinchi bosqichli parolni o'rnating.
**Kutiladigan natija:** O'quvchining shaxsiy akkauntida 2FA himoyasi faollashtiriladi.

### 9. Ransomware hujumi keysi (Muammoli vaziyat) <Badge type="danger" text="qiyin" />
Kompaniya xodimi pochtasiga kelgan «Hisob-faktura_№45.pdf.exe» nomli faylni ochdi. 10 daqiqadan so'ng barcha kompyuterlardagi Word va Excel fayllar kengaytmasi `.locked` ga o'zgarib qoldi.
1. Xodim qanday xatoga yo'l qo'ydi?
2. Nima sababdan fayl nomi `.pdf.exe` shaklida edi?
3. Kompaniyani ushbu falokatdan qanday qutqarish mumkin (eng to'g'ri chora nima)?
**Kutiladigan natija:**
1. Xodim xatdagi noma'lum `.exe` ijrochi faylini ochib yubordi.
2. Jinoyatchi faylni PDF qilib ko'rsatish uchun ikki tomonlama kengaytma niqobidan foydalangan.
3. To'lov to'lamaslik, tizimni tozalash va oldindan olingan zaxira nusxalarni (backup) tiklash kerakligi ta'kidlanadi.

### 10. Shaxsiy kiberxavfsizlik qoidalari kodeksi <Badge type="danger" text="qiyin" />
O'zingiz, sinfdoshlaringiz va oilangiz uchun «Kompyuterda xavfsiz ishlashning 7 ta oltin qoidasi» nomli mini-yo'riqnoma tuzing. Unda fleshkalar, parollar, Wi-Fi tarmoqlari, antivirus yangilanishi va shubhali havolalar bo'yicha aniq tavsiyalar bo'lsin.
**Kutiladigan natija:** O'quvchi barcha o'rganilgan nazariy va amaliy bilimlarni jamlab, mukammal xavfsizlik yo'riqnomasini ishlab chiqadi.

### 11. Xavfsizlik algoritmi: Parol murakkabligini hisoblovchi mantiq <Badge type="info" text="bonus" />
Tasavvur qiling, siz dasturchisiz. Foydalanuvchi kiritgan parolni tekshirib, unga 1 dan 10 gacha ball beruvchi algoritm loyihasini ishlab chiqing:
- Uzunligi 8 belgidan kam bo'lsa: 1 ball.
- 12 belgidan uzun bo'lsa: +3 ball.
- Katta harflar bo'lsa: +2 ball.
- Raqamlar bo'lsa: +2 ball.
- Maxsus belgilar bo'lsa: +3 ball.
Ushbu mantiq bo'yicha o'z parolingizni baholab ko'ring.
**Kutiladigan natija:** O'quvchi algoritmik yondashuv orqali parol sifatini raqamli baholash mantiqini tuzadi va tahlil qiladi.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Zararli dasturlar (Malware) tushunchasiga nimalar kiradi va ular kompyuterga qanday yo'llar bilan yuqadi?
2. Klassik virus bilan troyan oti (Trojan Horse) o'rtasidagi asosiy farq nimada?
3. Ransomware qanday ishlaydi va nima uchun zaxira nusxa (backup) eng yaxshi himoya hisoblanadi?
4. Antivirusning evristik tahlil (Heuristic Analysis) usuli qanday afzallikka ega?
5. Antivirusdagi karantin (Quarantine) papkasi nima uchun kerak?
6. Kuchli parol yaratishning 4 ta asosiy talabini sanab bering.
7. Ikki bosqichli autentifikatsiya (2FA) nima uchun faqat bitta paroldan ko'ra ancha xavfsizroq?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. **Nazariy takrorlash:** Dars konspekti va kiberxavfsizlik atamalarini o'qib chiqing.
2. **Kompyuterni tekshirish:** Uy kompyuteringizda Microsoft Defender (yoki o'rnatilgan antivirus) orqali to'liq skanerlash (Full scan) o'tkazing.
3. **Akkauntlarni tekshirish:** O'zingiz foydalanadigan barcha akkauntlar (Google, Telegram, o'yin profillari) parolini tekshirib chiqing, zaiflarini yangilang va 2FA himoyasini yoqing.
4. **Zaxira nusxa:** Eng muhim hujjatlaringiz va oilaviy fotosuratlaringizning zaxira nusxasini fleshkaga yoki bulutli xotiraga nusxalang.

</div>

