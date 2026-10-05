---
title: "10-dars. Internet qanday ishlaydi? IP, hosting, domen, DNS, brauzer, HTTP/HTTPS"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "8-sinf (Foundation)", "link": "/8-sinf-cs/"}, "week": {"n": 4, "link": "/8-sinf-cs/hafta-04/"}, "g": 10, "title": "Internet qanday ishlaydi? IP, hosting, domen, DNS, brauzer, HTTP/HTTPS", "lead": "Siz brauzerga manzil yozasiz va bir soniyada sahifa ochiladi. Bu orada IP, DNS, hosting va HTTPS qanday ishlaydi? Bugun internetning «ichki dunyosi»ga kiramiz.", "slide": "/slaydlar/8-sinf-cs/hafta-04/dars-1.html", "test": null, "tabs": [{"g": 10, "link": "/8-sinf-cs/hafta-04/dars-1", "current": true}], "prev": null, "next": null}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Internet** — dunyo bo'ylab qurilmalar va serverlarni bog'laydigan global tarmoq («tarmoqlar tarmog'i»).
- Ma'lumot almashish: **mijoz** (siz) **so'rov** yuboradi, **server** **javob** qaytaradi.
- **IP-manzil** — har bir qurilmaning noyob raqamli manzili (masalan, `203.0.113.5` kabi).
- **Domen nomi** — IP o'rniga ishlatiladigan eslab qolish oson nom (`my.gov.uz`).
- **Hosting** — sayt fayllari saqlanadigan va doim ochiq turadigan server.
- **DNS** — domen nomini IP-manzilga aylantiruvchi «telefon kitobi».
- Sahifa ochilishi: manzil yoziladi → DNS IP topadi → serverga so'rov → server javob → brauzer sahifani chizadi.
- **HTTP** ma'lumotni shifrlamaydi, **HTTPS** shifrlaydi (qulf belgisi).

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Nega domen kerak, IP ning o'zi yetmaydimi?

Telefoningizda do'stingizning raqami emas, ismi saqlanadi: raqamni yodlash qiyin. Internetda ham shunday: `203.0.113.5` ni emas, `maktab.uz` ni eslab qolasiz. Domen — odamlar uchun, IP — kompyuterlar uchun. Ikkalasini DNS bog'laydi.

### 2. Domen, hosting va IP: uchlik

Tasavvur qiling, siz do'kon ochmoqchisiz:
- **Domen** — do'kon peshtaxtasidagi nom.
- **Hosting** — do'kon binosi va javonlar (fayllar shu yerda turadi).
- **IP-manzil** — do'konning aniq ko'cha manzili.
- **DNS** — nomni eshitib, manzilni aytib beradigan navigator.

Ularsiz sayt ishlamaydi: nom bor, bino yo'q bo'lsa ham, bino bor, nom yo'q bo'lsa ham mijoz kirolmaydi.

### 3. Havola (URL) tarkibi

```
https://www.maktab.uz/kutubxona/kitoblar.html
```

- `https` — protokol (qanday qoida bilan bog'lanamiz).
- `www` — subdomen.
- `maktab` — domen nomi.
- `.uz` — zona (O'zbekiston).
- `/kutubxona/kitoblar.html` — serverdagi aniq sahifa yo'li.

### 4. HTTP vs HTTPS: xat va yopiq konvert

HTTP — ochiq otkritka: yo'ldagi har kim o'qiy oladi. HTTPS — muhrlangan konvert: ichini faqat qabul qiluvchi ochadi. Parol, karta raqami yoki shaxsiy ma'lumot kiritadigan sahifada doim `https://` va qulf belgisini tekshiring.

Eslatma: qulf belgisi saytning ishonchli ekanini emas, faqat ulanish shifrlanganini bildiradi. Soxta sayt ham HTTPS bo'lishi mumkin, shuning uchun domen yozilishini ham diqqat bilan o'qing (`my.gov.uz` va `my-gov.uz.xyz` — turli saytlar).

### 5. Odatiy xatolar

- «Internet = Wi-Fi» deb o'ylash. Wi-Fi — qurilmani tarmoqqa ulaydigan usul, internet esa butun global tarmoq.
- «Brauzer = internet». Brauzer — internetdagi sahifalarni ko'rsatadigan dastur.
- «Sayt mening kompyuterimda turadi». Yo'q, hosting serverida turadi.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Internet** | Dunyo bo'ylab qurilmalar va serverlarni bog'laydigan global tarmoq |
| **Server** | So'ralgan ma'lumotni beradigan, doim yoqilgan kompyuter |
| **Mijoz (client)** | Server xizmatidan foydalanadigan qurilma yoki dastur |
| **IP-manzil** | Tarmoqdagi qurilmaning noyob raqamli manzili |
| **Domen nomi** | IP o'rniga ishlatiladigan odam uchun qulay sayt nomi |
| **Hosting** | Sayt fayllari saqlanadigan va internetga ochiq turadigan server xizmati |
| **DNS** | Domen nomini IP-manzilga aylantiradigan tizim |
| **Brauzer** | Veb-sahifalarni so'rab, ekranda ko'rsatadigan dastur |
| **HTTP** | Veb-sahifa uzatish qoidalari (shifrsiz) |
| **HTTPS** | HTTP ning shifrlangan, xavfsiz varianti |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Internetning ishlashi uchun sizdan juda uzoqda joylashgan serverlar kerak: bir sahifa ma'lumoti ko'pincha bir necha tarmoq tugunlaridan o'tib keladi.
- Domen nomlarida bosh va kichik harf farq qilmaydi: `Maktab.UZ` va `maktab.uz` bir xil manzil.
- `www` yozish ko'p saytlarda shart emas: u shunchaki subdomen.
- Brauzer ko'pincha oxirgi tashrif qilingan saytlarning IP-manzilini eslab qoladi, shuning uchun ikkinchi marta sahifa tezroq ochiladi (bu keshlash deb ataladi).

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Havola anatomiyasi <Badge type="tip" text="oson" />
`https://www.kitobxona.uz/bolalar/ertaklar.html` havolasini bo'laklarga ajrating: protokol, subdomen, domen nomi, zona, yo'l.

**Kutiladigan natija:** besh qismning to'g'ri yozilgan ro'yxati.

### 2. Kim nima? <Badge type="tip" text="oson" />
Quyidagilarni mos juftlang: IP, domen, hosting, DNS, brauzer — va ma'nolar: «nomni raqamga aylantiradi», «sahifani ko'rsatadi», «sayt fayllari saqlanadi», «raqamli manzil», «eslab qolish oson nom».

**Kutiladigan natija:** 5 ta to'g'ri juftlik.

### 3. Bosqichlarni tartiblang <Badge type="tip" text="oson" />
Quyidagi bosqichlarni to'g'ri tartibga qo'ying: brauzer sahifani chizadi; DNS IP topadi; siz domenni yozasiz; server fayllarni yuboradi; brauzer serverga so'rov yuboradi.

**Kutiladigan natija:** 5 qadamli to'g'ri ketma-ketlik.

### 4. Aniqlash: HTTP yoki HTTPS? <Badge type="tip" text="oson" />
Uyda brauzerda 3 ta saytni oching va har biri uchun yozing: manzil `https://` bilan boshlanadimi, qulf belgisi bormi.

**Kutiladigan natija:** 3 qatorli jadval (sayt, https bormi, qulf bormi).

### 5. Bu nima qiladi? <Badge type="warning" text="o'rta" />
Bashorat qiling: foydalanuvchi `maktab.uz` ni yozdi, lekin DNS xizmati vaqtincha ishlamayapti, server esa to'liq sog'lom. Sahifa ochiladimi? Nima uchun?

**Kutiladigan natija:** 2–3 jumlali izoh (nom bo'yicha topilmaydi, IP bilan ochilishi mumkin).

### 6. Xatoni toping <Badge type="warning" text="o'rta" />
Do'stingiz aytdi: «Saytim kompyuterimda saqlanadi, kompyuterni o'chirsam ham hamma kira oladi». Uning xatosi nimada? To'g'ri javobni yozing.

**Kutiladigan natija:** hosting haqida 2–3 jumlali tuzatma.

### 7. Parol kiritish xavfsizmi? <Badge type="warning" text="o'rta" />
Uchta vaziyatni baholang: (a) `http://` sayt, "Xavfsiz emas" belgisi bor, kartani kiritish so'raladi; (b) `https://` sayt, qulf bor, manzil `my.gov.uz`; (c) `https://` sayt, qulf bor, lekin manzil `my-gov.uz.xyz`. Qaysi birida va nima uchun ehtiyot bo'lasiz?

**Kutiladigan natija:** har bir holat uchun 1–2 jumlali xulosa.

### 8. «DNS» rol o'yini <Badge type="warning" text="o'rta" />
Uch kishi (do'st, oila a'zosi) bilan o'ynang: biri — brauzer, biri — DNS (daftarida 5 domen va IP namunasi yozilgan), biri — server. Rollarni almashtirib 3 marta takrorlang.

**Kutiladigan natija:** o'yin natijasi va nimani tushunganingiz haqida 3 jumla.

### 9. Mini-diagramma chizing <Badge type="danger" text="qiyin" />
Qog'ozga (yoki kompyuterda) «Sahifa qanday ochiladi?» sxemasini chizing: siz, brauzer, DNS, server va strelkalar bilan so'rov va javob yo'nalishi.

**Kutiladigan natija:** 5 ta elementli, strelkalar yo'nalishi to'g'ri sxema.

### 10. Boshqa domen zonalari <Badge type="danger" text="qiyin" />
5 ta turli domen zonasini (`.uz`, `.com`, `.org`, `.edu` va boshqa) topib, har birining qanday saytlarda uchrashini yozing.

**Kutiladigan natija:** 5 qatorli jadval (zona, sayt misoli).

### 11. Hosting va domen tadqiqoti <Badge type="danger" text="qiyin" />
Qiziqarli bitta saytni tanlang. Uning domen nomi, zonasi, HTTPS ekani va saytda qanday ma'lumotlar turishini yozib, "Bu sayt qaysi xizmatni ko'rsatadi?" degan savolga javob bering.

**Kutiladigan natija:** bir sahifalik qisqa tavsif.

### 12. Do'stga tushuntiring <Badge type="info" text="bonus" />
Internet nima ekanini va sahifa qanday ochilishini 5 daqiqada 10 yoshli ukangizga o'xshatish (restoran, pochta, telefon kitobi) yordamida tushuntiring va u nimani tushunganini so'rang.

**Kutiladigan natija:** tushuntirishning 4–5 jumlali yozma konspekti.

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Mijoz va server o'rtasida ma'lumot qanday almashiladi?
2. IP-manzil bilan domen nomining farqi nima?
3. Hosting nimani saqlaydi?
4. DNS qanday vazifani bajaradi?
5. Brauzerda sahifa ochilishining bosqichlarini sanang.
6. HTTP va HTTPS qanday farq qiladi?
7. Qulf belgisi nimani kafolatlaydi, nimani kafolatlamaydi?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

«Internet yo'li» mini-loyihasi (20–30 daqiqa): sevimli saytingizni tanlang, uning havolasini bo'laklarga ajrating (protokol, domen, zona, yo'l), HTTPS ekanini tekshiring va sahifa ochilish bosqichlarini 5 jumlada o'z so'zingiz bilan yozing. Batafsil: `uyga-vazifa.md`.

</div>

