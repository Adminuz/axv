---
title: "9-dars. Simulyator va Emulator haqida tushuncha (1-qism)"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (Android)", "link": "/9-sinf-android/"}, "week": {"n": 3, "link": "/9-sinf-android/hafta-03/"}, "g": 9, "title": "Simulyator va Emulator haqida tushuncha (1-qism)", "lead": "Simulyator va Emulator haqida tushuncha (1-qism): Simulyator vs Emulyator farqi, AVD yaratish va CPU virtualizatsiyasi", "slide": "/slaydlar/9-sinf-android/hafta-03/dars-3.html", "tabs": [{"g": 7, "link": "/9-sinf-android/hafta-03/dars-1", "current": false}, {"g": 8, "link": "/9-sinf-android/hafta-03/dars-2", "current": false}, {"g": 9, "link": "/9-sinf-android/hafta-03/dars-3", "current": true}], "prev": {"g": 8, "title": "Android Studio va Android SDK bilan tanishuv (3-qism)", "link": "/9-sinf-android/hafta-03/dars-2"}, "next": null}
---

Bugungi darsda biz mobil ilovalarni sinovdan o'tkazishning eng ajoyib vositasi — **Android Emulator** bilan tanishamiz. Qanday qilib kompyuter ichida haqiqiy smartfonni ishga tushirish, simulyator va emulyatorning farqi hamda protsessor virtualizatsiyasi nima ekanini bilib olamiz.

---

<div class="blk">

## <Icon name="file-text" /> Asosiy tushunchalar

- **Emulyator (Emulator)** — haqiqiy telefonning apparat ta'minotini (protsessor, xotira, sensorlar) kompyuter ichida to'liq dasturiy modellashtiruvchi virtual qurilma.
- **Simulyator (Simulator)** — apparatni emas, faqat tashqi dasturiy qoidalar va interfeysni taqlid qiluvchi yengil vosita.
- **AVD (Android Virtual Device)** — Android Studio'da yaratiladigan virtual smartfon yoki planshet profili.
- **CPU Virtualizatsiyasi (Intel VT-x / AMD-V)** — kompyuter protsessorining virtual tizimlarni yuqori tezlikda ishlatishini ta'minlovchi apparat texnologiyasi.
- **Extended Controls** — emulyatorning GPS, batareya zaryadi, qo'ng'iroq va SMS xabarlarini taqlid qiluvchi maxsus boshqaruv paneli.

---

</div>

<div class="blk">

## <Icon name="file-text" /> 1. Simulyator va Emulyator: Asosiy farq nima?

Ko'pincha bu ikki so'z adashtiriladi, lekin ular texnik jihatdan mutlaqo boshqa-boshqa vositalardir:

```
+-----------------------------------------------------------+
| SIMULYATOR (Simulator)                                    |
| - Faqat dasturiy qobiqni taqlid qiladi                    |
| - Kompyuterning o'z protsessorida to'g'ridan-to'g'ri ishlaydi |
| - Apparatdagi haqiqiy xatolarni (kam xotira, datchik) ko'rsatolmaydi |
+-----------------------------------------------------------+
| EMULYATOR (Emulator - Android AVD)                        |
| - Telefon apparatini (CPU, RAM, datchiklar) to'liq modellashtiradi |
| - Ichida to'laqonli Android operatsion tizimi yuklanadi   |
| - Haqiqiy smartfondagi natijani 99% aniqlikda beradi      |
+-----------------------------------------------------------+
```

---

</div>

<div class="blk">

## <Icon name="file-text" /> 2. AVD (Android Virtual Device) qanday yaratiladi?

Android Studio'ning yuqori o'ng burchagidagi **Device Manager** tugmasini bosib, yangi virtual qurilma yaratishingiz mumkin:
1. **Device tanlash:** Telefon modeli (masalan, Pixel 8);
2. **System Image tanlash:** Android versiyasi (masalan, Android 14 UpsideDownCake). Har doim **Google APIs** yozuvi bo'lgan tasvirni tanlash tavsiya etiladi;
3. **Xotira va grafika:** Emulyatorga kamida 2 GB (2048 MB) RAM va apparat tezlatgichi (Hardware GLES 2.0) beriladi;
4. **Finish:** Virtual qurilma tayyor! Yashil "Play" tugmasi bosilsa, ekranda haqiqiy smartfon oynasi paydo bo'ladi.

---

</div>

<div class="blk">

## <Icon name="file-text" /> 3. Protsessor virtualizatsiyasi nega kerak?

Emulyator kompyuter ichida boshqa operatsion tizimni yurgizgani sababli, u protsessordan maxsus apparat yordamini talab qiladi:
- **Intel protsessorlarida:** `Intel VT-x` texnologiyasi;
- **AMD protsessorlarida:** `AMD-V` texnologiyasi;
- **Apple Silicon (M1/M2/M3):** Apple Hypervisor.

Agar kompyuteringiz BIOS sozlamalarida virtualizatsiya yoqilmagan bo'lsa, emulyator juda sekin ishlaydi yoki umuman ochilmaydi.

---

</div>

<div class="blk">

## <Icon name="file-text" /> 4. Emulyatorning yashirin imkoniyatlari (Extended Controls)

Emulyator oynasi yonidagi uch nuqta `...` tugmasini bossangiz, qiziqarli imkoniyatlar ochiladi:
- **GPS koordinatalari:** Xaritadan Samarqand, Parij yoki Nyu-Yorkni tanlasangiz, virtual telefon o'sha yerda turgandek bo'ladi!
- **Telefon qo'ng'irog'i:** Emulyatorga virtual raqamdan qo'ng'iroq qilish yoki SMS jo'natish mumkin;
- **Batareya darajasi:** Zaryadni 5% qilib qo'yib, ilovangiz kam quvvatda o'zini qanday tutishini tekshirish mumkin;
- **Ekranni aylantirish:** Ekranni 90 darajaga aylantirib, gorizontal rejimni sinash mumkin.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy topshiriqlar

1. **Simulyator va Emulyator farqini yozing** `· oson`  
   Ushbu ikki tushuncha o'rtasidagi eng muhim 2 ta farqni daftaringizga yozing.

2. **AVD qisqartmasi nimani anglatadi?** `· oson`  
   AVD so'zining to'liq inglizcha va o'zbekcha tarjimasini bayon qiling.

3. **Pixel modelini tanlash** `· oson`  
   Android Studio'da AVD yaratayotganda qaysi mashhur Google smartfoni modeli tavsiya etiladi?

4. **Nima uchun Google APIs tanlanadi?** `· o'rta`  
   Tizim tasvirini (System Image) yuklab olayotganda oddiy AOSP o'rniga nega "Google APIs" varianti tanlanishi kerak?

5. **Intel VT-x / AMD-V vazifasi** `· o'rta`  
   Kompyuter protsessoridagi apparat virtualizatsiyasi nima uchun emulyator tezligiga to'g'ridan-to'g'ri ta'sir qiladi?

6. **BIOS xatoligi ssenariysi** `· o'rta`  
   Agar emulyator "VT-x is disabled in BIOS" xatosi bilan ochilmasa, uni tuzatish uchun nima qilish kerakligini bosqichma-bosqich yozing.

7. **GPS simulyatsiyasini tushuntiring** `· o'rta`  
   Emulyatorda turib boshqa shaharning GPS koordinatalarini qanday kiritish mumkinligini yozing.

8. **Virtual qurilma va real smartfon taqqoslashi** `· qiyin`  
   Ilovani virtual emulyatorda tekshirishning 2 ta afzalligi va 2 ta kamchiligini (haqiqiy smartfonga nisbatan) taqqoslang.

9. **Gorizontal rejim (Landscape) testi** `· qiyin`  
   Ekranni aylantirganda ilovangizdagi matn yoki dizayn buzilib ketmasligi uchun emulyatorning qaysi tugmasi orqali test o'tkaziladi?

10. **Tadqiqotchi dasturchi** `· bonus`  
    Agar kompyuterning operativ xotirasi (RAM) 4 GB bo'lsa va emulyator kompyuterni qotirib qo'ysa, dasturchi ilovani testlash uchun qanday muqobil yo'ldan (USB orqali real telefon ulash) foydalanishi mumkin?

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Android Emulator dunyodagi eng mashhur virtualizatsiya tizimlaridan biri hisoblangan **QEMU** negizida ishlaydi.
- Emulyator orqali hatto smartfonning barmoq izi skanerini (Fingerprint) ham sichqoncha yordamida simulyatsiya qilish mumkin!

---

</div>

<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- Emulyator haqiqiy telefon apparatini kompyuterda to'liq modellashtiradi, simulyator esa faqat interfeysni taqlid qiladi.
- AVD Manager orqali istalgan o'lchamli va versiyali virtual telefon yaratish mumkin.
- Protsessor virtualizatsiyasi (Intel VT-x / AMD-V) emulyatorning tezkor ishlashi uchun majburiydir.
- Extended Controls paneli orqali GPS, batareya va qo'ng'iroqlarni sinash mumkin.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Emulyator simulyatordan qaysi jihati bilan ustun?
2. AVD qanday yaratiladi?
3. Protsessor virtualizatsiyasi yoqilmasa nima bo'ladi?
4. Emulyatorning yon panelidagi uch nuqta qanday ataladi?
5. Emulyator ichida qaysi operatsion tizim yuklanadi?

</div>

