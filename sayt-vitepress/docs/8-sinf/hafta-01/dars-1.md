---
title: "1-dars. Internet qanday ishlaydi? DNS, hosting, domain. Front-end va Back-end"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "8-sinf", "link": "/8-sinf/"}, "week": {"n": 1, "link": "/8-sinf/hafta-01/"}, "g": 1, "title": "Internet qanday ishlaydi? DNS, hosting, domain. Front-end va Back-end", "lead": "Telegramda xabar yozasiz, YouTube'da video ochasiz: bir soniyada hammasi ekranda. Bu darsda \"parda ortiga\" kirib, brauzer, DNS va server qanday hamkorlik qilishini ko'ramiz.", "slide": "/slaydlar/8-sinf/hafta-01/dars-1.html", "test": "/slaydlar/8-sinf/hafta-01/dars-1-test.html", "tabs": [{"g": 1, "link": "/8-sinf/hafta-01/dars-1", "current": true}, {"g": 2, "link": "/8-sinf/hafta-01/dars-2", "current": false}, {"g": 3, "link": "/8-sinf/hafta-01/dars-3", "current": false}], "prev": null, "next": {"g": 2, "title": "HTML hujjat strukturasi. Teg, atribut, head, sarlavhalar", "link": "/8-sinf/hafta-01/dars-2"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Internet** — dunyodagi millionlab kompyuter, telefon va serverlarni bog'laydigan ulkan tarmoq.
- Har bir qurilmaning o'z **IP manzili** bor (masalan, `142.250.185.78`).
- **Server** — doim yoqilgan kompyuter, sayt fayllarini saqlaydi. **Klient** — so'rov yuboruvchi (sizning brauzeringiz).
- **DNS** — domen nomini IP manzilga aylantiradigan "telefon kitobi".
- **Domen** — saytning nomi, **hosting** — sayt fayllari turadigan joy. Ikkalasi ham kerak.
- Sahifa yo'li: brauzer → DNS → server → brauzer (so'rov va javob), keyin brauzer sahifani chizadi.
- **HTTPS** — himoyalangan HTTP: ma'lumot shifrlanadi.
- **Front-end** — ko'rinadigan qism (HTML, CSS, JS), **back-end** — serverdagi ko'rinmaydigan qism.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### Nega IP manzil bor, nomning o'zi yetmaydimi?
Kompyuterlar nom bilan emas, raqam bilan ishlaydi. Pochta ham shunday: xat "Jasur" nomiga emas, ko'cha va uy raqamiga yetkaziladi. Odam nomni yodlaydi, mashina esa raqamni. Ularni DNS "tarjima" qiladi. Shu sababli sizning telefoningizning ham, Google serverining ham o'z IP manzili bor.

### Domen qismlari
`www.mysite.uz` manzilini o'ngdan chapga o'qing:

- `uz` — yuqori daraja domeni (mamlakat yoki tur: `uz`, `com`, `org`);
- `mysite` — asosiy nom (uni siz tanlaysiz);
- `www` — subdomen (saytning bo'limi yoki xizmati).

Domen pulga olinadi va har yili to'lanadi. To'lov to'xtasa, nom boshqa odamga o'tib ketishi mumkin.

### Domen va hosting: do'kon misoli
Domen — do'konning nomi va manzili. Hosting — do'konning o'zi (bino, javonlar, tovar). Manzil bor, bino yo'q bo'lsa, mijoz bo'sh joyga keladi. Bino bor, manzilni hech kim bilmasa, hech kim kirmaydi. Hosting turlari: shared hosting, VPS, cloud, static hosting (Netlify, Vercel). Hozircha nomlarini bilish yetarli.

### Brauzer sahifani qanday oladi?
`https://mysite.uz` yozib Enter bosganingizda:

1. Brauzer DNS'dan `mysite.uz` ning IP manzilini so'raydi.
2. DNS IP manzilni qaytaradi.
3. Brauzer shu IP dagi serverga **so'rov (request)** yuboradi.
4. Server HTML, CSS, JS va rasmlarni **javob (response)** sifatida yuboradi.
5. Brauzer fayllarni o'qib, sahifani ekranga chizadi.

Odatiy xato: "brauzer sahifani internetdan butun holda oladi" deb o'ylash. Aslida u bir nechta alohida fayl oladi va ularni o'zi yig'adi.

### Front-end va back-end: restoran
Zal, menyu, ofitsiant — front-end: mijoz hammasini ko'radi. Oshxona va ombor — back-end: mijoz ko'rmaydi, ammo ovqat shu yerda tayyorlanadi. **Full-stack** dasturchi ikkala qismni ham biladi. Instagram'da like bosish tugmasi — front-end, like'ni hisoblash va saqlash — back-end.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Internet | Dunyo bo'ylab qurilmalarni bog'laydigan tarmoq |
| IP manzil | Qurilmaning raqamli manzili (`142.250.185.78`) |
| Server | Doim yoqilgan, sayt fayllarini saqlaydigan kompyuter |
| Klient | So'rov yuboruvchi qurilma yoki brauzer |
| DNS | Domen nomini IP manzilga aylantiradigan tizim |
| Domen | Saytning internetdagi nomi (`google.com`) |
| Hosting | Sayt fayllari saqlanadigan joy (server) |
| Request / Response | So'rov / javob |
| HTTP / HTTPS | Brauzer va server muloqot qoidalari / ularning himoyalangan varianti |
| Front-end | Brauzerda ishlaydigan, ko'rinadigan qism |
| Back-end | Serverda ishlaydigan, ko'rinmaydigan qism |
| Full-stack | Ikkala qismni ham biladigan dasturchi |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Dunyoda 5 milliarddan ortiq odam internetdan foydalanadi.
- IP manzilni yodlash o'rniga domen ishlatilgani uchun `youtube.com` ni eslab qolish oson.
- Birinchi veb-sayt 1991-yilda ishga tushgan va u saytning o'zi haqida edi.
- Brauzerda bitta sahifa ochilganda ko'pincha o'nlab, ba'zan yuzlab fayl yuklanadi.
- Serverlar uyda emas, maxsus markazlarda (data center) turadi va ular to'xtamay ishlaydi.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Domenni qismlarga ajrating <Badge type="tip" text="oson" />
`www.kun.uz` manzilini subdomen, asosiy nom va yuqori daraja domeniga ajrating. Xuddi shuni yana ikkita sayt uchun bajaring.

**Kutiladigan natija:** uchta saytning to'g'ri ajratilgan qismlari.

### 2. Bu kim: klient yoki server? <Badge type="tip" text="oson" />
Quyidagilarning har biri klientmi yoki servermi, yozing: sizning telefoningiz; Chrome brauzeri; YouTube videolarini saqlaydigan kompyuter; maktab saytini ishlatib turgan kompyuter.

**Kutiladigan natija:** to'rt javob, har biriga bitta jumlalik sabab.

### 3. So'rov yo'li chizmasi <Badge type="tip" text="oson" />
Daftarga to'rtta quti chizing: Brauzer, DNS, Server, Brauzer. O'qlar bilan ulang va har bir o'qqa nima yuborilishini yozing.

**Kutiladigan natija:** to'g'ri tartibdagi to'rt bosqich va o'qlar ustidagi yozuvlar.

### 4. Domen yoki hosting? <Badge type="tip" text="oson" />
Quyidagilar domenga yoki hostingga tegishlimi: `mysite.uz`; saytning rasm fayllari; yillik to'lanadigan nom; fayllar saqlanadigan kompyuter.

**Kutiladigan natija:** to'rt javob va bir jumlalik izoh.

### 5. Xatoni toping <Badge type="warning" text="o'rta" />
Do'stingiz aytdi: "DNS saytni brauzerga yuboradi, serverga umuman kerak emas". Bu gapdagi xatoni toping va to'g'ri variantini 2-3 jumlada yozing.

**Kutiladigan natija:** DNS nima qilishi va sahifani aslida kim yuborishi tushuntirilgan.

### 6. Bashorat qiling <Badge type="warning" text="o'rta" />
Agar DNS bir soatga ishlamay qolsa, `youtube.com` yozganingizda nima bo'ladi? IP manzilni qo'lda yozsangiz-chi? Ikkala holatni yozing va sabab keltiring.

**Kutiladigan natija:** ikki holat uchun asoslangan javob.

### 7. DevTools tadqiqoti <Badge type="warning" text="o'rta" />
Ixtiyoriy saytni oching, `F12` (Mac: `Cmd+Option+I`) → **Network** bo'limini tanlang va sahifani yangilang. Nechta fayl yuklanganini sanang va kamida uch xil turini (html, css, js, rasm) toping.

**Kutiladigan natija:** fayllar soni va uch xil turdagi fayl nomlari.

### 8. Front yoki back? <Badge type="warning" text="o'rta" />
Telegram yoki Instagram uchun 5 tadan funksiya tanlang va har birini front-end yoki back-end ga ajrating. Sabab yozing.

**Kutiladigan natija:** 10 ta funksiya, har biriga qisqa sabab.

### 9. Sevimli sayt tahlili <Badge type="danger" text="qiyin" />
Sevimli saytingizni tanlang va yozing: (a) domeni qanday tuzilgan; (b) kamida 3 ta front-end va 3 ta back-end funksiyasi; (c) agar terminal bor bo'lsa, `nslookup` bilan IP manzilini toping.

**Kutiladigan natija:** yarim sahifalik tahlil.

### 10. Sahifa yo'lini tushuntiring <Badge type="danger" text="qiyin" />
Do'stingizga (internetni bilmaydigan odam) `https://mysite.uz` yozilganda nima bo'lishini tushuntiruvchi bir sahifalik qo'llanma yozing. Atamalarni (DNS, IP, server, request, response) qo'llang, ammo ularni sodda so'z bilan izohlang.

**Kutiladigan natija:** 5 qadam, barcha atamalar sodda tushuntirilgan.

### 11. HTTPS qidiruvi <Badge type="danger" text="qiyin" />
Uchta saytni oching: biri HTTPS bilan boshlansa, uni va qulf belgisini toping. Brauzer HTTP (qulfsiz) saytga nima deb ogohlantiradi? Nega parol kiritiladigan joyda faqat HTTPS bo'lishi kerak? Natijani yozing.

**Kutiladigan natija:** ko'rilgan saytlar ro'yxati va sababning 2-3 jumlalik izohi.

### 12. Birinchi sahifa: salom.html <Badge type="info" text="bonus" />
Kod muharririda `salom.html` nomli fayl yarating. Unga `<!DOCTYPE html>`, `<html>`, `<body>` ichida `h1` va `p` yozing. Brauzerda oching, so'ng `h1` matnini o'z ismingizga almashtiring va sahifani yangilang.

**Kutiladigan natija:** brauzerda sizning ismingiz yozilgan sahifa.

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Internet nima va u qanday qurilmalarni bog'laydi?
2. IP manzil nima uchun kerak?
3. DNS qanday vazifani bajaradi?
4. Domen va hosting o'rtasidagi farq nima?
5. Enter bosilgandan keyin sahifa ekranda paydo bo'lgunga qadar nechta qadam bo'ladi va ular qaysilar?
6. HTTP va HTTPS orasidagi asosiy farq nima?
7. Tugma rangini va parol tekshirishni qaysi tomon (front-end yoki back-end) bajaradi?
8. Full-stack dasturchi kim?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

**«Mening internetim»** (20–30 daqiqa, daftarda yoki matn faylida):

1. O'zingiz yoqtirgan 3 ta saytni yozing va har birining domenini qismlarga (nom va zona) ajrating.
2. Bitta saytni tanlab, sahifa ochilguncha bo'ladigan bosqichlarni o'z so'zingiz bilan 5 ta gapda yozing (brauzer, DNS, server).
3. O'sha saytdan front-end va back-end ga 2 tadan misol yozing.

</div>

