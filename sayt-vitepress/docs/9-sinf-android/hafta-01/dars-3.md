---
title: "3-dars. Androidning imkoniyatlari va qo‘llanilish sohalari"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (Android)", "link": "/9-sinf-android/"}, "week": {"n": 1, "link": "/9-sinf-android/hafta-01/"}, "g": 3, "title": "Androidning imkoniyatlari va qo‘llanilish sohalari", "lead": "Androidning imkoniyatlari va qo‘llanilish sohalari: smartfon, planshet, WearOS, Android Auto, Android TV va IoT", "slide": "/slaydlar/9-sinf-android/hafta-01/dars-3.html", "test": "/slaydlar/9-sinf-android/hafta-01/dars-3-test.html", "tabs": [{"g": 1, "link": "/9-sinf-android/hafta-01/dars-1", "current": false}, {"g": 2, "link": "/9-sinf-android/hafta-01/dars-2", "current": false}, {"g": 3, "link": "/9-sinf-android/hafta-01/dars-3", "current": true}], "prev": {"g": 2, "title": "Android tizimi va uning arxitekturasi", "link": "/9-sinf-android/hafta-01/dars-2"}, "next": null}
---

Bugungi darsda biz Android tizimining faqat telefonlar bilan cheklanib qolmaydigan ulkan imkoniyatlarini kashf qilamiz. Android aqlli soatlarda, tezyurar avtomobillarda, ulkan televizorlarda va hatto tibbiy uskunalarda qanday ishlashini o'rganamiz.

---

<div class="blk">

## <Icon name="file-text" /> Asosiy tushunchalar

- **Multitasking (Ko'p vazifalilik)** — bir vaqtning o'zida bir nechta dasturni parallel ishlatish imkoniyati (Split-screen va Picture-in-Picture).
- **Wear OS** — aqlli soatlar (Smartwatch) uchun maxsus moslashtirilgan Android operatsion tizimi.
- **Android Auto** — smartfonni avtomobil multimedia monitoriga ulab, navigatsiya va musiqadan xavfsiz foydalanish tizimi.
- **Android Automotive OS (AAOS)** — avtomobilning o'ziga to'liq o'rnatilgan, mashina qismlarini boshqaruvchi mustaqil operatsion tizim.
- **Android TV / Google TV** — katta ekranli televizorlar va multimedia pristavkalari uchun mo'ljallangan tizim.
- **IoT (Internet of Things — Buyumlar Interneti)** — internetga ulangan turli xil aqlli texnika va maishiy qurilmalar (muzlatgichlar, terminallar, kiosklar).

---

</div>

<div class="blk">

## <Icon name="file-text" /> 1. Androidning zamonaviy texnik imkoniyatlari

### Ko'p vazifalilik (Multitasking)
Zamonaviy Android qurilmalari kompyuterlar kabi bir vaqtning o'zida bir nechta vazifani bajara oladi:
- **Split-Screen:** Ekranni ikkiga bo'lib, bir vaqtda ikkita ilovani (masalan, darslik va tarjimonni) ishlatish;
- **Picture-in-Picture (PiP):** Video tomosha qilayotganda yoki navigatsiyadan foydalanayotganda video kichik suzuvchi oynaga aylanadi;
- **Moslashuvchan ekranlar (Foldable UI):** Buklanuvchi telefonlar (Galaxy Fold) ochilganda kichik ekrandan ulkan planshet rejimiga avtomatik o'tish.

### Sun'iy intellekt va on-device hisoblash
Android 14 va 15 versiyalarida sun'iy intellekt (Gemini Nano) bevosita telefonning o'zida ishlaydi. Ovozni matnga aylantirish, fotosuratlarni qayta ishlash yoki matnlarni umumlashtirish internet talab qilmaydi va foydalanuvchi ma'lumotlari to'liq maxfiy qoladi.

---

</div>

<div class="blk">

## <Icon name="file-text" /> 2. Androidning asosiy qo'llanilish sohalari

| Qurilma toifasi | Android varianti | Boshqaruv usuli | Asosiy vazifasi |
|---|---|---|---|
| **Smartfon va planshetlar** | Standart Android | Sensorli ekran (Touch) | Muloqot, internet, o'yinlar, barcha turdagi ilovalar |
| **Aqlli soatlar** | **Wear OS** | Kichik ekran, tugma, ovoz | Puls, qadamlar, sport, tezkor bildirishnomalar |
| **Avtomobillar** | **Android Auto / AAOS** | Ovozli boshqaruv, katta ekran | Navigatsiya, musiqa, avtomobil tizimlari nazorati |
| **Televizorlar** | **Android TV** | Masofaviy pult (D-pad), ovoz | Filmlar, seriallar, YouTube, katta ekranda hordiq |
| **Savdo va sanoat** | **Android IoT / Embedded** | Sensor, shtrix-kod skaneri | Aqlli kassa, to'lov terminallari (POS), interaktiv kiosklar |

---

</div>

<div class="blk">

## <Icon name="file-text" /> 3. Dizayn va interfeys farqlari

Har bir qurilma uchun ilova yaratishda dasturchi uning o'ziga xos jihatlarini hisobga olishi shart:
- **Aqlli soatda:** Ekran juda kichik (1.3 dyuym). Matnlar minimal, tugmalar katta va doiraviy bo'lishi kerak. Batareyani tejash uchun qora fon afzal.
- **Televizorda:** Foydalanuvchi ekrandan 3 metr uzoqda o'tiradi va sensorli bosish imkoniyati yo'q. Barcha menyular pult tugmalari bilan boshqarilishi va shriftlar juda yirik bo'lishi shart.
- **Avtomobilda:** Haydovchining diqqatini yo'ldan chalg'itmaslik — birinchi qoida! Shu sababli boshqaruv asosan ovoz orqali amalga oshiriladi.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy topshiriqlar

1. **Smartfoningizda Split-Screen rejimini sinab ko'ring** `· oson`  
   Smartfoningizda ekranni ikkiga bo'lish (Split-screen) funksiyasini yoqing. Yuqori qismda veb-brauzerni, pastki qismda esa «Kalkulyator» yoki «Eslatmalar» ilovasini ochib ko'ring. Tajribangizni yozing.

2. **Wear OS qanday vazifalarni bajaradi?** `· oson`  
   Aqlli soatlarning kamida 4 ta muhim vazifasini sanab bering.

3. **Android TV boshqaruvi** `· oson`  
   Nima uchun oddiy smartfon ilovasini o'zgartirishsiz televizorga o'rnatib bo'lmaydi? Boshqaruvdagi asosiy farq nimada?

4. **Android Auto va Android Automotive OS farqi** `· o'rta`  
   Ushbu ikki tizim o'rtasidagi farqni tushuntiring: qaysi biri smartfonga bog'liq va qaysi biri avtomobilning mustaqil bort kompyuterida ishlaydi?

5. **Qurilmalar interfeysi taqqoslash jadvali** `· o'rta`  
   Smartfon, Wear OS soati va Android TV uchun mos bo'lgan shrift o'lchamlari va boshqaruv xususiyatlarini aks ettiruvchi taqqoslash jadvali tuzing.

6. **On-device sun'iy intellekt afzalliklari** `· o'rta`  
   Nima uchun sun'iy intellekt hisob-kitoblarining internet serverida emas, balki telefon protsessorining o'zida bajarilishi xavfsizlik va tezlik uchun foydali?

7. **Kundalik hayotdagi Android IoT qurilmalari** `· o'rta`  
   Shahringizdagi do'konlar, dorixonalar yoki bankomatlarda Android asosida ishlaydigan qanday qurilmalarni (Smart POS, kassa apparati, navbat kioski) ko'rdingiz? Ularning ishlashini tavsiflang.

8. **Aqlli soat uchun ilova g'oyasi** `· qiyin`  
   Maktab o'quvchilari uchun Wear OS aqlli soatlarida ishlaydigan yangi foydali ilova g'oyasini o'ylab toping (masalan, "Dars jadvali va qo'ng'iroq taymeri"). Unda qanday ekranlar bo'lishini chizib ko'rsating.

9. **Avtomobil xavfsizligi va UI cheklovlari** `· qiyin`  
   Google nima sababdan avtomobil harakatlanayotgan paytda Android Auto ekranida YouTube yoki film tomosha qilishni qat'iy taqiqlaydi? Dasturchi ushbu cheklovni chetlab o'tishga haqqi bormi?

10. **Tadqiqotchi dasturchi** `· bonus`  
    Agar siz Android dasturchisi bo'lsangiz, kelgusida qaysi yo'nalish uchun ilovalar yaratishni tanlagan bo'lar edingiz: klassik smartfonlarmi, aqlli soatlarmi, avtomobillarmi yoki IoT tizimlarimi? Tanlovingiz sabablarini asoslang.

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- NASA kosmik agentligi Android smartfonlarini koinotga yo'llagan! 2013-yilda ular oddiy Android telefonini sun'iy yo'ldoshning "miyasi" sifatida kosmosga uchirib, uning radiatsiya va og'ir sharoitlarda ishlashini sinovdan o'tkazgan.
- Bugungi kunda dunyodagi ko'plab elektrmobillar (masalan, Polestar va yangi Volvo modellari) Android Automotive OS tizimida ishlaydi va mashinaning barcha funksiyalarini boshqaradi.

---

</div>

<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- Android — bu faqat smartfonlar operatsion tizimi emas, balki kiyiladigan gadjetlar (Wear OS), avtomobillar (Android Auto/AAOS), televizorlar (Android TV) va IoT qurilmalarini qamrab oluvchi ulkan ekotizimdir.
- Har bir qurilma o'zining ekran o'lchami va boshqaruv mexanizmiga (sensor, pult, ovoz) ega bo'lib, dasturchidan moslashuvchan dizayn talab etadi.
- Androidning ochiqligi tufayli har qanday yangi aqlli texnika uchun ixtisoslashgan operatsion tizim yaratish mumkin.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Ekranni ikkiga bo'lib, ikkita ilovani bir vaqtda ishlatish qanday ataladi?
2. Aqlli soatlar uchun mo'ljallangan maxsus Android tizimi qanday nomlanadi?
3. Android TV interfeysining smartfon interfeysidan 2 ta asosiy farqini ayting.
4. Android Auto va Android Automotive OS o'rtasidagi asosiy farq nima?
5. Buyumlar interneti (IoT) tushunchasi nimani anglatadi?

</div>

