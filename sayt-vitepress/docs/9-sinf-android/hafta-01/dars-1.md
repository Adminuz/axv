---
title: "1-dars. Android nima va uning rivojlanish tarixi"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (Android)", "link": "/9-sinf-android/"}, "week": {"n": 1, "link": "/9-sinf-android/hafta-01/"}, "g": 1, "title": "Android nima va uning rivojlanish tarixi", "lead": "Android nima va uning rivojlanish tarixi: mobil OS tarixi, Google, versiyalar va O'zbekiston ekotizimi", "slide": "/slaydlar/9-sinf-android/hafta-01/dars-1.html", "test": "/slaydlar/9-sinf-android/hafta-01/dars-1-test.html", "tabs": [{"g": 1, "link": "/9-sinf-android/hafta-01/dars-1", "current": true}, {"g": 2, "link": "/9-sinf-android/hafta-01/dars-2", "current": false}, {"g": 3, "link": "/9-sinf-android/hafta-01/dars-3", "current": false}], "prev": null, "next": {"g": 2, "title": "Android tizimi va uning arxitekturasi", "link": "/9-sinf-android/hafta-01/dars-2"}}
---

Bugungi darsda biz dunyodagi eng ommabop mobil operatsion tizim — **Android** bilan tanishamiz. Uning qanday yaratilgani, Google qanday qilib uni global ekotizimga aylantirgani, versiyalarning qiziqarli nomlari va O'zbekistondagi mobil dasturlash imkoniyatlarini o'rganamiz.

---

<div class="blk">

## <Icon name="file-text" /> Asosiy tushunchalar

- **Android** — sensorli ekranli mobil qurilmalar va gadjetlar uchun yaratilgan, Linux yadrosiga asoslangan ochiq kodli operatsion tizim.
- **AOSP (Android Open Source Project)** — Androidning hamma uchun ochiq va bepul bo'lgan manba kodi.
- **Andy Rubin** — Android Inc. asoschisi va Android tizimining "otasi" deb ataluvchi muhandis.
- **HTC Dream (T-Mobile G1)** — 2008-yilda dunyoga taqdim etilgan eng birinchi tijoriy Android smartfoni.
- **Material Design / Material You** — Google tomonidan ishlab chiqilgan, zamonaviy va chiroyli foydalanuvchi interfeysi dizayn tizimi.
- **Firmware qobig'i (Skin)** — ishlab chiqaruvchilar (Samsung, Xiaomi) tomonidan AOSP ustiga qurilgan shaxsiy interfeys (One UI, HyperOS).

---

</div>

<div class="blk">

## <Icon name="file-text" /> 1. Androidning yaratilishi: Kameralardan smartfonlar sari

2003-yilda AQSHning Palo-Alto shahrida to'rt nafar muhandis — **Andy Rubin, Rich Miner, Nick Sears va Chris White** — kichik bir startapga asos solishdi va uni **Android Inc.** deb atashdi. 

Qiziq tomoni shundaki, ular boshida smartfonlar uchun emas, balki **raqamli fotoapparatlar** uchun aqlli operatsion tizim qilmoqchi bo'lishgan. Dastlabki g'oya shunday edi: fotokamera suratga oladi, uni darhol internet orqali kompyuterga yoki bulutga uzatadi.

Biroq ko'p o'tmay, raqamli kameralar bozori qisqarib, mobil telefonlar bozori esa portlash darajasida o'sib borayotgani ma'lum bo'ldi. Jamoa darhol yo'nalishni o'zgartirdi va smartfonlar uchun operatsion tizim yaratishga kirishdi.

### Google sotib olishi (2005)
2005-yilning iyul oyida **Google** kompaniyasi Android Inc.ni sotib oldi. Bu butun IT industriyasi uchun tarixiy burilish nuqtasi bo'ldi. Google bu tizimni bepul va ochiq qilib, barcha telefon ishlab chiqaruvchilariga tarqatishni rejalashtirdi. 2007-yilda **Open Handset Alliance** ittifoqi tuzildi va 2008-yil 23-sentabrda dunyodagi birinchi Android smartfoni — **HTC Dream** rasman taqdim etildi.

---

</div>

<div class="blk">

## <Icon name="file-text" /> 2. Versiyalar tarixi: Shirinliklar davri va raqamlar

Android versiyalari uzoq vaqt davomida alifbo tartibida shirinliklar nomi bilan atalgan. Har bir yangi versiya tizimni tezroq va xavfsizroq qilib bordi:

| Versiya | Nomi | Chiqqan yili | Asosiy yangiligi |
|---|---|---|---|
| 1.5 | **Cupcake** | 2009 | Ekran klaviaturasi va vidjetlar |
| 1.6 | **Donut** | 2009 | Har xil ekran o'lchamlari va qidiruv tizimi |
| 2.2 | **Froyo** | 2010 | JIT kompilyator (tezlik 2-5x oshdi), Wi-Fi tarqatish |
| 2.3 | **Gingerbread** | 2010 | NFC moduli, batareya optimallashuvi |
| 4.0 | **Ice Cream Sandwich** | 2011 | Yangi Holo interfeysi, tugmasiz ekranlar |
| 4.4 | **KitKat** | 2013 | 512MB xotirada ham tez ishlash, "OK Google" |
| 5.0 | **Lollipop** | 2014 | **Material Design** tamoyili, 64-bitlik arxitektura |
| 7.0 | **Nougat** | 2016 | Ekranni ikkiga bo'lish (Split-screen) |
| 8.0 | **Oreo** | 2017 | Project Treble (yangilanishlarni tezlashtirish) |
| 9.0 | **Pie** | 2018 | Imo-ishoralar (gestures) bilan boshqarish |
| 10 | **Android 10** | 2019 | Tungi rejim (Dark Mode), raqamli nomlashga o'tildi |
| 12 | **Android 12** | 2021 | **Material You** (dinamik ranglar palitrasi) |
| 14 | **Android 14** | 2023 | Ultra HDR, batareya xavfsizligi, sun'iy intellekt |
| 15 | **Android 15** | 2024–2025 | Maxfiy bo'lim (Private Space), Gemini AI integratsiyasi |

---

</div>

<div class="blk">

## <Icon name="file-text" /> 3. Ochiq manba (AOSP) va dunyo brendlari

Androidning kodi barcha uchun ochiq bo'lgani sababli, har bir smartfon ishlab chiqaruvchi kompaniya o'zining shaxsiy interfeysini yaratishi mumkin:
- **Samsung:** One UI interfeysi;
- **Xiaomi:** MIUI va zamonaviy HyperOS;
- **Google Pixel:** Toza Android ("Stock Android");
- **Honor / OnePlus:** MagicOS / OxygenOS.

---

</div>

<div class="blk">

## <Icon name="file-text" /> 4. O'zbekistonda Android mobil ilovalari

Bugungi kunda O'zbekiston aholisining 80 foizdan ortig'i Android smartfonlaridan foydalanadi. Shu sababli mobil dasturchilik eng talab yuqori bo'lgan kasblardan biridir:
- **Moliya va to'lovlar:** Click, Payme, Uzum Bank, Apelsin;
- **Transport va logistika:** Yandex Go, MyTaxi;
- **Ta'lim va davlat xizmatlari:** eMaktab, MyGov, EduOn;
- **Savdo va yetkazib berish:** Uzum Market, Express24.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy topshiriqlar

1. **Smartfoningiz versiyasini aniqlang** `· oson`  
   Shaxsiy smartfoningizning «Sozlamalar» (Settings) -> «Telefon haqida» (About phone) bo'limiga kiring. Android versiyangiz, telefon modeli va operativ xotira (RAM) hajmini daftaringizga yozing.

2. **Android Easter Egg animatsiyasini toping** `· oson`  
   Sozlamalardagi «Android versiyasi» yozuvi ustiga tez-tez 3-4 marta bosing. Ekranda paydo bo'lgan sirli interaktiv o'yin yoki animatsiyani oching va unda nima tasvirlanganini tasvirlang.

3. **Android Inc. asoschilari ro'yxati** `· oson`  
   2003-yilda kompaniyaga asos solgan to'rt nafar muhandisning to'liq ism-familiyalarini yozing.

4. **Ilk Android smartfoni xususiyatlari** `· oson`  
   HTC Dream (T-Mobile G1) telefonining kamida 4 ta muhim apparat xususiyatini sanab bering.

5. **Shirinliklar nomlari ketma-ketligi** `· o'rta`  
   Android 1.5 dan Android 9.0 gacha bo'lgan barcha shirinlik nomlarini alifbo tartibida (C harfidan P harfigacha) to'liq yozib chiqing.

6. **Material Design va Material You farqi** `· o'rta`  
   Android 5.0 da kiritilgan Material Design va Android 12 da kiritilgan Material You dizayn falsafalarining o'zaro asosiy farqini tushuntiring.

7. **AOSP nima va u kompaniyalarga nima beradi?** `· o'rta`  
   Nima uchun Samsung va Xiaomi noldan yangi operatsion tizim yaratmasdan, aynan Androiddan foydalanadi? Fikringizni asoslang.

8. **O'zbekistondagi 3 ta mobil ilovani tahlil qiling** `· o'rta`  
   O'zingiz eng ko'p ishlatadigan 3 ta mahalliy mobil ilovani tanlang. Ular sizga qanday qulaylik yaratishi va qaysi funksiyalari yoqishini yozing.

9. **Versiyalar yangilanishi muammosi (Fragmentatsiya)** `· qiyin`  
   Nima uchun yangi Android versiyasi chiqqanda, u hamma telefonlarga bir vaqtda yetib bormaydi? Bu muammoning texnik sabablarini tushuntiring.

10. **Kelajak smartfoni konsepsiyasi** `· qiyin`  
    Siz Android tizimini rivojlantiruvchi bosh muhandis bo'lsangiz, kelgusi Android 16 versiyasiga qanday yangi va foydali funksiya qo'shgan bo'lar edingiz? (Kamida 1 sahifalik taklif tayyorlang).

11. **Tadqiqotchi dasturchi** `· bonus`  
    Kompaniyangiz uchun yangi mobil ilova yaratishni rejalashtiryapsiz. Ushbu ilova uchun qaysi eng minimal Android versiyasini (Min SDK) tanlagan bo'lar edingiz va nega? Global qurilmalar statistikasi asosida javob bering.

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- **Mashhur yashil robotcha (Bugdroid)** logotipini dizayner Irina Blok chizgan. U ushbu robotchaning dizayn g'oyasini xalqaro hojatxona eshiklaridagi erkak va ayol belgilaridan ilhomlanib yaratgan!
- 2005-yilda Google Android Inc. kompaniyasini bor-yo'g'i **50 million dollarga** sotib olgan. Bugun esa Android dunyodagi 3 milliarddan ortiq faol qurilmalarda ishlamoqda va bu Googlening eng muvaffaqiyatli xaridlaridan biri hisoblanadi.

---

</div>

<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- Android — Linux yadrosiga qurilgan, ochiq kodli va modulli operatsion tizimdir.
- Tizim 2003-yilda Andy Rubin tomonidan boshlanib, 2005-yilda Google tasarrufiga o'tgan va 2008-yilda HTC Dream orqali bozorga kirib kelgan.
- Bugungi kunda Android nafaqat smartfonlarda, balki planshetlar, televizorlar, soatlar va avtomobillarda ham keng qo'llaniladi.
- O'zbekiston raqamli iqtisodiyotida Android dasturchilariga bo'lgan talab juda yuqori.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Android operatsion tizimi qaysi operatsion tizim yadrosiga asoslangan?
2. 2008-yilda chiqarilgan birinchi Android smartfoni qanday nomlangan?
3. Nima uchun Android 10 dan boshlab shirinlik nomlaridan voz kechildi?
4. AOSP qisqartmasi nimani anglatadi?
5. Material You dizayn tizimining asosiy yangiligi nima?

</div>

