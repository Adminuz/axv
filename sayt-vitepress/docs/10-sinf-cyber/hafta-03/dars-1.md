---
title: "7-dars. Xavfsizlikni anglash (2-qism): raqamli gigiyena, brauzer xavfsizligi va 2FA"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (Cyber)", "link": "/10-sinf-cyber/"}, "week": {"n": 3, "link": "/10-sinf-cyber/hafta-03/"}, "g": 7, "title": "Xavfsizlikni anglash (2-qism): raqamli gigiyena, brauzer xavfsizligi va 2FA", "lead": "", "slide": "/slaydlar/10-sinf-cyber/hafta-03/dars-1.html", "tabs": [{"g": 7, "link": "/10-sinf-cyber/hafta-03/dars-1", "current": true}, {"g": 8, "link": "/10-sinf-cyber/hafta-03/dars-2", "current": false}, {"g": 9, "link": "/10-sinf-cyber/hafta-03/dars-3", "current": false}], "prev": null, "next": {"g": 8, "title": "Xavfsizlikni anglash (3-qism): tahdidlarni modellashtirish, Red/Blue Team va CTF", "link": "/10-sinf-cyber/hafta-03/dars-2"}}
---

---
title: "Xavfsizlikni anglash (2-qism): raqamli gigiyena, brauzer xavfsizligi va 2FA"
description: "Raqamli gigiyena asoslari, xavfsiz brauzer kengaytmalari (uBlock, Cookie AutoDelete, ClearURLs), 1.1.1.1 DNS hamda Telegramda 2FA va maxfiylik"
dars: 1
hafta: 3
sinf: 10-sinf-cyber
---

<div class="blk">

## <Icon name="file-text" /> Reja

1. Raqamli gigiyena (Digital Hygiene) tushunchasi va 4 ta asosiy qoida.
2. Brauzer xavfsizligi va kuzatuvchi trekerlar (Cookies, Fingerprinting) xavfi.
3. 4 ta muhim brauzer kengaytmasi: HTTPS Everywhere, uBlock Origin, Cookie AutoDelete, ClearURLs.
4. DNS xizmatini xavfsiz qilish: 1.1.1.1 va DNS-over-HTTPS (DoH).
5. Ikki bosqichli autentifikatsiya (2FA) va uning turlari.
6. Telegram messenjerida 5 bosqichli xavfsizlik va maxfiylik sozlamalari.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Nazariy qism

### 1. Raqamli gigiyena nima?

**Raqamli gigiyena (Digital Hygiene)** — bu internet va elektron qurilmalarda shaxsiy maʼlumotlar, pullar va obro'ni himoya qilish uchun har kuni ongli ravishda amal qilinadigan oddiy va muntazam odatlar majmuidir.

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

### 2. Xavfsiz brauzerni tayyorlash

Ko'pchilik brauzerlar birlamchi holatda barcha reklamalarga va trekerlarga ruxsat beradi. Brauzerni xavfsiz qilish uchun 4 ta kengaytma tavsiya etiladi:
- **HTTPS Everywhere:** Saytlarni majburan shifrlangan (`https://`) holatga o'tkazadi.
- **uBlock Origin:** Zararli reklamalar, josuslik trekerlari va og'ir skriptlarni bloklaydi.
- **Cookie AutoDelete:** Sayt oynasi yopilishi bilan undan qolgan barcha kuzatuvchi kukilarni o'chiradi.
- **ClearURLs:** Havolalardagi shaxsiy kuzatuv kodlarini (`?utm_source=...`) tozalaydi.

---

### 3. DNS xavfsizligi: 1.1.1.1

Siz qaysi saytlarga kirayotganingizni mahalliy provayder ko'ra olmasligi uchun kompyuteringizda yoki routeringizda xavfsiz DNS xizmatidan foydalanish lozim:
- Asosiy DNS: `1.1.1.1`
- Muqobil DNS: `1.0.0.1`

Brauzerda **DNS-over-HTTPS (DoH)** ni yoqish orqali barcha qidiruvlar to'liq shifrlanadi.

---

### 4. Telegram messenjerida 5 bosqichli xavfsizlik

1. **Maxfiylik:** Telefon raqami, oxirgi kirgan vaqt va profil rasmini «Mening kontaktlarim» yoki «Hech kim» qilib qo'yish.
2. **Ikki bosqichli autentifikatsiya (2FA):** Maxsus murakkab bulutli parol o'rnatish.
3. **Faol seanslar:** `Qurilmalar` bo'limiga kirib, o'zingizga tegishli bo'lmagan barcha begona kompyuter va telefonlarni o'chirib tashlash.
4. **Guruhlar:** «Meni guruhlarga kim qo'shishi mumkin?» bandini «Mening kontaktlarim» qilib cheklash.
5. **Xabarlarni avtomatik o'chirish:** Shaxsiy chatlarda xabarlarni 1 oy yoki 1 yilda avtomatik tozalashni yoqish.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy laboratoriya

### 1-qadam: uBlock Origin va ClearURLs ni o'rnatish
Chrome Web Store yoki Firefox Add-ons do'konidan kengaytmalarni o'rnating va faollashtiring.

### 2-qadam: 1.1.1.1 DNS sozlamasini tekshirish
Tarmoq kartasida DNS manzilini `1.1.1.1` va `1.0.0.1` qilib sozlang. Brauzerda `https://1.1.1.1/help` manzilini ochib, DoH ishlayotganini («Yes») tekshiring.

### 3-qadam: Telegramda 2FA ni yoqish
`Sozlamalar -> Maxfiylik va xavfsizlik -> Ikki bosqichli autentifikatsiya` ga kirib, kamida 12 belgili kuchli bulutli parol o'rnating.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy topshiriqlar

### 1. Raqamli gigiyena tushunchasi &lt;Badge type="tip" text="oson" />
Raqamli gigiyena nima va nima sababdan u insonning shaxsiy gigiyenasi kabi har kuni muntazam bajarilishi shart bo'lgan odat hisoblanadi?

### 2. Tracking Cookies xavfi &lt;Badge type="tip" text="oson" />
Nima sababdan veb-saytlarning kuzatuvchi kuki (Tracking Cookie) fayllari foydalanuvchi shaxsiy daxlsizligiga tahdid soladi?

### 3. uBlock Origin afzalligi &lt;Badge type="warning" text="o'rta" />
uBlock Origin kengaytmasi nima sababdan kiberxavfsizlik mutaxassislari tomonidan oddiy reklama to'suvchi dasturlarga qaraganda ko'proq tavsiya etiladi?

### 4. ClearURLs mexanizmi &lt;Badge type="warning" text="o'rta" />
Ijtimoiy tarmoqlardan nusxalangan uzun havolalardagi `?utm_source=...` va `?fbclid=...` yozuvlari nimani anglatadi va ClearURLs ularni nima uchun tozalaydi?

### 5. DNS-over-HTTPS (DoH) roli &lt;Badge type="warning" text="o'rta" />
Oddiy shifrlanmagan DNS so'rovi bilan DoH o'rtasidagi asosiy xavfsizlik farqi nimada? Provayder nimani ko'ra olmaydi?

### 6. SMS orqali 2FA zaifligi &lt;Badge type="warning" text="o'rta" />
Nima sababdan faqat SMS-kod orqali tasdiqlanadigan 2FA kiberxavfsizlikda zaif hisoblanadi va uning o'rniga nima tavsiya etiladi?

### 7. Telegramda telefon raqamini yashirish &lt;Badge type="tip" text="oson" />
Telegramda telefon raqamini «Hech kim» yoki «Mening kontaktlarim» qilib qo'yish qanday xavfning (OSINT) oldini oladi?

### 8. Faol seanslar (Active Sessions) tahlili &lt;Badge type="warning" text="o'rta" />
Telegramda faol seanslarni tekshirganingizda, o'zingiz tanimaydigan boshqa shahar yoki noma'lum qurilma paydo bo'lganini ko'rdingiz. Bu nimani anglatadi va qanday choralar ko'rish lozim?

### 9. Guruhlarga qo'shilish cheklovi &lt;Badge type="tip" text="oson" />
Nima uchun Telegramda «Meni guruhlarga kim qo'shishi mumkin?» bandini «Mening kontaktlarim» qilib qo'yish kiberxavfsizlik talabi hisoblanadi?

### 10. Shaxsiy raqamli gigiyena rejasi &lt;Badge type="info" text="bonus" />
O'zingizning shaxsiy smartfoningiz va kompyuteringiz xavfsizligini ta'minlash bo'yicha 5 ta banddan iborat muntazam tekshiruv rejasini ishlab chiqing.

---

</div>

<div class="blk">

## <Icon name="file-text" /> O'z-o'zini tekshirish savollari

1. Raqamli gigiyenaning 4 ta asosiy qoidasi nimalardan iborat?
2. Kuki (Cookie) nima va Cookie AutoDelete unga qanday ta'sir qiladi?
3. 1.1.1.1 DNS xizmati qaysi xalqaro kompaniyaga tegishli?
4. Nima uchun bir xil parollardan foydalanish xavfli?
5. Telegramda hisobni firibgarlardan himoyalashning eng samarali usuli nima?

---

</div>

<div class="blk">

## <Icon name="file-text" /> Foydali manbalar

- Cloudflare 1.1.1.1 Help: `1.1.1.1/help`
- Electronic Frontier Foundation (EFF): Surveillance Self-Defense Guide.

</div>

