# 10-dars. Internet qanday ishlaydi? IP, hosting, domen, DNS, brauzer, HTTP/HTTPS

**Hafta:** 4 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + tadqiqot amaliyoti · **II-bob**, 4-dars (hafta ichida 1-dars)

> Manba: o'quv dasturi, 10-mavzu: «Internet tushunchasi va ma'lumot almashish jarayoni. IP-manzil, domen nomi va hosting tushunchalari. DNS vazifasi va domenni IP-manzilga bog'lash jarayoni. Brauzer va veb-sahifani ochish bosqichlari. HTTP va HTTPS protokollari hamda xavfsiz ulanish.» Dasturda boshqa tafsilot yo'q; quyidagi tushuntirishlar shu bandlarni sodda tilda ochib beradi.

## 1. Dars rejasi

**Maqsad:** o'quvchilar internetning ma'lumot almashish jarayonini (so'rov va javob) tushunadi; IP-manzil, domen, hosting va DNS ning vazifasini farqlaydi; brauzerda veb-sahifa ochilish bosqichlarini tartib bilan aytadi; HTTP va HTTPS farqini va xavfsiz ulanish belgisini biladi.

**Kutiladigan natija:**
- Internetni «tarmoqlar tarmog'i» deb ta'riflay oladi, mijoz (client) va server rolini ajratadi.
- IP-manzil, domen, hosting, DNS ni hayotiy o'xshatish bilan tushuntiradi.
- Havola (URL) tarkibini bo'laklarga ajratadi.
- Veb-sahifa ochilishining 5 bosqichini tartib bilan aytadi.
- HTTPS saytni brauzerdagi belgi orqali taniydi va parol kiritishdan oldin tekshiradi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va kirish | 9-dars (raqamli transformatsiya) ni qisqa takrorlash. Savol: «my.gov.uz ga kirganda kompyuteringiz 1 soniyada nima qiladi?» — o'quvchilar taxmin qiladi |
| 10–35 daq | Yangi mavzu | Internet, IP, domen, hosting, DNS, brauzer, HTTP/HTTPS |
| 35–40 daq | Tanaffus | Harakatli tanaffus |
| 40–65 daq | Amaliy mashg'ulot | Havola anatomiyasi, bosqichlarni tartiblash, HTTPS tekshiruvi, «DNS» rol o'yini |
| 65–75 daq | Tezkor nazorat | 5 ta savol + mini-viktorina |
| 75–80 daq | Xulosa va uyga vazifa | Xulosa, uyga vazifa yo'riqnomasi |

---

## 2. Dars konspekti

### 2.1. Internet nima va ma'lumot qanday almashiladi?

**Internet** — dunyo bo'ylab millionlab kompyuter, telefon va serverlarni bir-biriga ulaydigan global tarmoq. Shuning uchun uni «tarmoqlar tarmog'i» deb ataydilar.

Ma'lumot almashish doim bir xil qoida bo'yicha ketadi:
- **Mijoz (client)** — siz foydalanadigan qurilma (telefon, kompyuter) va unda ishlaydigan dastur (brauzer).
- **Server** — doim yoqilgan, internetga ulangan va so'ralgan ma'lumotni beradigan kompyuter.
- **So'rov (request)** — mijoz serverdan nimadir so'raydi.
- **Javob (response)** — server so'ralgan narsani qaytaradi.

> O'xshatish (qo'shimcha): restoranda siz (mijoz) ofitsiantga buyurtma berasiz (so'rov), oshxona (server) taomni tayyorlab beradi (javob).

### 2.2. IP-manzil

**IP-manzil (IP address)** — tarmoqdagi har bir qurilmaning noyob raqamli manzili. Internetda ma'lumot aynan shu manzil bo'yicha topiladi. Ko'rinishi: to'rtta son nuqta bilan ajratilgan (IPv4), har biri 0 dan 255 gacha.

```
192.168.1.10       <- uy Wi-Fi tarmog'idagi qurilma manzili (ichki manzil misoli)
203.0.113.5        <- ko'rgazma uchun ajratilgan namuna manzil
```

> O'xshatish: IP — uyning aniq pochta indeksi va raqami: manzilsiz xat yetib bormaydi.

Muammo: odam uchun `203.0.113.5` kabi raqamlarni yodlash qiyin. Shuning uchun domen nomi paydo bo'lgan.

### 2.3. Domen nomi

**Domen nomi (domain name)** — IP-manzil o'rniga ishlatiladigan, odam eslab qoladigan nom, masalan `my.gov.uz`, `wikipedia.org`.

Domen tuzilishi (o'ngdan chapga o'qiladi):

```
https://www.maktab.uz/kutubxona/kitoblar.html
  |      |    |     |      |
protokol sub- nom  zona   yo'l (sahifa manzili)
         domen
```

- **Zona (TLD):** `.uz` (O'zbekiston), `.com`, `.org`, `.edu`.
- **Domen nomi:** `maktab`.
- **Subdomen:** `www` yoki `mail` kabi old qism.
- **Yo'l:** serverdagi aniq sahifa.

Domenni **ro'yxatdan o'tkazish** kerak (har yili haq to'lanadi) — ikki kishi bir xil domenga ega bo'la olmaydi.

### 2.4. Hosting

**Hosting** — veb-sayt fayllari (HTML, rasm, video) saqlanadigan va internetga 24/7 ochiq turadigan server (yoki server joyini ijaraga berish xizmati).

> O'xshatish: **domen** — do'konning nomi (peshtaxta), **hosting** — do'konning o'zi (bino va javonlar), **IP** — do'konning aniq manzili.

Sayt kompyuteringizda emas, hosting serverida turadi; shuning uchun o'chirilgan kompyuter ham saytni ko'rsatishga xalaqit qilmaydi.

### 2.5. DNS

**DNS (Domain Name System)** — domen nomini IP-manzilga aylantiruvchi xizmat. Uni internetning «telefon kitobi» deb ataydilar: ismni (domen) qidirasiz, raqamni (IP) olasiz.

```
brauzer:  "my.gov.uz manzili qanday?"
DNS:      "203.0.113.5"   (namuna)
brauzer:  203.0.113.5 ga ulanadi
```

DNS javobi bo'lmasa, sayt ishlayotgan bo'lsa ham siz uni nom bilan topa olmaysiz.

### 2.6. Brauzer va veb-sahifaning ochilishi

**Brauzer** (Chrome, Edge, Firefox, Safari) — veb-sahifani so'raydigan va ko'rsatadigan dastur. Sahifa ochilishining 5 bosqichi:

1. Manzilni yozasiz yoki havolani bosasiz (`https://www.maktab.uz`).
2. Brauzer DNS dan domenga mos IP-manzilni so'raydi.
3. Brauzer shu IP dagi serverga ulanadi va sahifani so'raydi (HTTP/HTTPS so'rovi).
4. Server fayllarni (HTML, CSS, rasmlar) javob sifatida yuboradi.
5. Brauzer fayllarni yig'ib, sahifani ekranda chizadi.

### 2.7. HTTP va HTTPS

**Protokol** — ikki kompyuter bir-birini tushunishi uchun kelishilgan qoidalar to'plami.

- **HTTP (HyperText Transfer Protocol)** — veb-sahifalarni uzatish qoidalari. Ma'lumot shifrlanmagan holda ketadi: yo'ldagi begona odam o'qib olishi mumkin.
- **HTTPS (HTTP Secure)** — HTTP + shifrlash. Ma'lumot shifrlangan holda uzatiladi, server esa sertifikat orqali o'zini tasdiqlaydi. Brauzerda qulf belgisi va `https://` ko'rinadi.

| | HTTP | HTTPS |
|---|---|---|
| Shifrlash | yo'q | bor |
| Brauzerda | `http://`, ko'pincha «Xavfsiz emas» belgisi | `https://`, qulf belgisi |
| Qayerda kerak | ochiq, shaxsiy ma'lumotsiz sahifalar | parol, karta, shaxsiy ma'lumot kiritiladigan har qanday sahifa |

Muhim qoida: HTTPS saytning o'zi «yaxshi sayt» degani emas, faqat ulanish shifrlanganini bildiradi. Sayt manzilini (domen to'g'ri yozilganini) ham tekshiring.

### 2.8. Butun rasm

```
Siz -> brauzer -> DNS (nom -> IP) -> hosting serveri (HTTPS so'rov) -> javob -> brauzer sahifani chizadi
```

### 2.9. Ixtiyoriy demo (dasturda yo'q, mentor xohlasa)

Windows buyruq satrida (Win + R, `cmd`) domen IP ga qanday aylanishini ko'rsatish mumkin:

```
nslookup wikipedia.org
ping wikipedia.org
```

`nslookup` DNS javobini (IP-manzil) ko'rsatadi; `ping` serverga signal yuborib, javob kelishini tekshiradi. Natija har kuni va har joyda har xil bo'lishi mumkin. Maktab tarmog'ida buyruqlar cheklangan bo'lsa, o'tkazib yuboring.

---

## 3. Amaliy mashg'ulotlar

### 1-mashq (oson). Havola anatomiyasi
**Vazifa:** `https://www.kitobxona.uz/bolalar/ertaklar.html` havolasini bo'laklarga ajrating: protokol, subdomen, domen nomi, zona, yo'l.

**Yechim:**
- protokol: `https`
- subdomen: `www`
- domen nomi: `kitobxona`
- zona: `.uz`
- yo'l: `/bolalar/ertaklar.html`

### 2-mashq (oson). Bosqichlarni tartiblash
**Vazifa:** Quyidagi bosqichlarni to'g'ri tartibga soling: (a) brauzer sahifani chizadi, (b) DNS IP-manzilni qaytaradi, (c) server fayllarni yuboradi, (d) foydalanuvchi domenni yozadi, (e) brauzer serverga so'rov yuboradi.

**Yechim:** d → b → e → c → a. (Avval nom yoziladi, DNS manzil topadi, so'rov ketadi, server javob beradi, brauzer chizadi.)

### 3-mashq (o'rta). HTTPS tekshiruvi
**Vazifa:** Brauzerda 3 ta saytni oching (masalan, `my.gov.uz`, `wikipedia.org` va maktabingiz yoki sevimli saytingiz). Har biri uchun jadvalni to'ldiring: manzil `https://` bilan boshlanadimi? Qulf belgisi bormi?

**Yechim:** natija saytga bog'liq. Ko'pchilik zamonaviy saytlar HTTPS da. Muhimi — o'quvchi manzil satri chap qismidagi belgini topa olishi va izohlay olishi. Agar `http://` va «Xavfsiz emas» belgisi chiqsa, shu saytda parol kiritmaslik kerakligini aytsin.

### 4-mashq (o'rta). Rol o'yini: «DNS»
**Vazifa:** Sinfdagi bir o'quvchi — DNS (daftarida 5 ta domen va IP-raqam yozilgan «telefon kitobi»), ikkinchisi — brauzer, uchinchisi — server. Brauzer domenni so'raydi, DNS IP ni aytadi, brauzer serverga «so'rov» yozuvini topshiradi, server «sahifa» qog'ozini qaytaradi. Rollarni almashtirib 3 marta takrorlang.

**Yechim:** o'yin davomida tartib: so'rov → DNS → IP → server → javob. O'quvchilar DNS «qidiruv» vazifasini, serverning «javob» vazifasini farqlay olsin.

### 5-mashq (qiyin). Hayotiy o'xshatish jadvali
**Vazifa:** Domen, IP, hosting, DNS, brauzer, server uchun shahar hayotidan o'xshatish toping (masalan, do'kon, manzil, telefon kitobi) va jadval tuzing.

**Yechim:** (namuna) domen — do'kon nomi; IP — aniq manzil; hosting — do'kon binosi; DNS — telefon kitobi/navigator; brauzer — xaridor; server — sotuvchi. Boshqa mantiqli o'xshatishlar ham qabul.

---

## 4. Tezkor savollar (Checklist)

1. IP-manzil nima?
   - **Javob:** Tarmoqdagi qurilmaning noyob raqamli manzili.
2. Domen nomi nima uchun kerak?
   - **Javob:** IP-raqamlarni yodlash o'rniga odam uchun oson, eslab qoladigan nom bo'lishi uchun.
3. Hosting nima?
   - **Javob:** Sayt fayllari saqlanadigan va doim internetga ochiq turadigan server (yoki shu xizmat).
4. DNS ning vazifasi nima?
   - **Javob:** Domen nomini IP-manzilga aylantirish.
5. HTTP va HTTPS ning asosiy farqi nima?
   - **Javob:** HTTPS ma'lumotni shifrlaydi, HTTP shifrlamaydi.

## 5. Kuchli o'quvchi uchun qo'shimcha

- Bir saytga bir nechta domen bog'lash mumkinmi? (Ha: bir hosting, bir necha domen.)
- Bitta IP ga bir nechta sayt joylashishi mumkinmi? (Ha, bitta serverda bir necha sayt turishi mumkin.)

## 6. Mentor uchun eslatmalar

- Dasturda IPv6, portlar, sertifikat turlari yo'q: chuqurlashmang, faqat savol bo'lsa qisqa javob bering.
- IP raqamlari uchun namuna (`203.0.113.x`) ishlatilgan: bu aniq sayt emas, deb ayting.
- Maktab tarmog'ida ba'zi saytlar yopiq bo'lishi mumkin; zaxira sayt: o'quvchilarga ma'lum bo'lgan istalgan HTTPS sayt.
