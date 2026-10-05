---
title: "10-dars. Tarmoq qurilmalari va xavfsizlik muammolari (1-qism): router, switch, hab va ularning zaifliklari"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (Cyber)", "link": "/10-sinf-cyber/"}, "week": {"n": 4, "link": "/10-sinf-cyber/hafta-04/"}, "g": 10, "title": "Tarmoq qurilmalari va xavfsizlik muammolari (1-qism): router, switch, hab va ularning zaifliklari", "lead": "Maktab Wi-Fi'ingiz orqasida qaysi qurilmalar ishlaydi va ularning qaysi biri hujumchiga qulay? Bugun tarmoqning \"yo'l belgilari\"ni o'rganamiz.", "slide": "/slaydlar/10-sinf-cyber/hafta-04/dars-1.html", "test": "/slaydlar/10-sinf-cyber/hafta-04/dars-1-test.html", "tabs": [{"g": 10, "link": "/10-sinf-cyber/hafta-04/dars-1", "current": true}, {"g": 11, "link": "/10-sinf-cyber/hafta-04/dars-2", "current": false}, {"g": 12, "link": "/10-sinf-cyber/hafta-04/dars-3", "current": false}], "prev": null, "next": {"g": 11, "title": "Tarmoq qurilmalari va xavfsizlik muammolari (2-qism): Wireshark yordamida tarmoq trafigini tahlil qilish", "link": "/10-sinf-cyber/hafta-04/dars-2"}}
---

---
title: "Tarmoq qurilmalari va xavfsizlik muammolari (1-qism): router, switch, hab va ularning zaifliklari"
description: "Tarmoq kabeli, NIC, hab, repitir, ko'prik, switch, router, gateway; zaiflik, tahdid va hujum"
dars: 1
hafta: 4
sinf: 10-sinf-cyber
---

<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- Axborot uzatish muhiti: kabelli yoki simsiz aloqa kanallari.
- Uch kabel turi: o'ralgan juft (UTP/STP), koaksial, optik tola.
- Tarmoq kartasi (NIC) kompyuterni tarmoqqa ulaydi, paketlarni uzatadi va qabul qiladi.
- Hab va repitir 1-sathda, ko'prik va switch 2-sathda, router 3-sathda ishlaydi.
- Hab signalni hammaga beradi, switch faqat mo'ljallangan qabul qiluvchiga.
- Zaiflik, tahdid va hujum har xil tushunchalar.
- Ichki tahdid jinoyatlarning 80% ini tashkil etadi (qo'llanma bo'yicha).
- Hujumlar: razvedka, kirish, parol, MITM, DoS/DDoS, zararli dastur.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### Nega hab o'rniga switch?
Hab sinfda hammaga baqirib gapirgan o'qituvchiga o'xshaydi: hamma eshitadi. Switch esa har bir o'quvchiga alohida pichirlaydi. Shuning uchun switch unumdorlik va xavfsizlikni oshiradi.

### Router: yo'l ko'rsatuvchi
Router paketdagi qabul qiluvchi IP manzilga qaraydi va marshrutlash jadvali bilan solishtiradi. Jadvalda yo'l bo'lmasa, paket tashlab yuboriladi. Qo'shimcha funksiyalari: NAT, filtrlash, shifrlash, trafik boshqaruvi.

### Zaiflik, tahdid, hujum farqi
Eshigi qulflanmagan uy: qulflanmaganlik zaiflik. Atrofda aylanayotgan o'g'ri tahdid. O'g'ri kirsa, bu hujum. (Bu o'xshatish tushuntirish uchun.)

### Odatiy xatolar
- Switch to'liq xavfsiz deb o'ylash: u MAC-manzilni almashtirish hujumiga zaif.
- Router 2-sathda deb adashish: u IP bilan, ya'ni 3-sathda ishlaydi.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Hab | Signalni barcha portlarga uzatuvchi 1-sath qurilmasi |
| Repitir | Signalni asl ko'rinishida takrorlaydi (regeneratsiya) |
| Ko'prik | MAC bo'yicha segmentlarni birlashtiradi (2-sath) |
| Switch | MAC bo'yicha faqat qabul qiluvchiga uzatadi (2-sath) |
| Router | IP va marshrutlash jadvaliga qarab yo'naltiradi (3-sath) |
| Gateway | Tarmoqlar orasidagi aloqa nuqtasi, apparat yoki dasturiy |
| NIC | Tarmoq kartasi, tarmoqqa ulash komponenti |
| Zaiflik | Tizim xavfsizligini buzadigan kamchilik |
| Tahdid | Xavfsizlikka xavf solishi mumkin bo'lgan omillar |
| Hujum | Zaiflikdan foydalanib bajarilgan buzilish |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Optik tolada axborot yorug'lik bilan uzatiladi, shuning uchun u o'nlab km masofaga yetadi.
- Qo'llanmada o'quv xonasida kamida 2-3 router va 2 switch bo'lishi yozilgan.
- Hab bugun deyarli switch bilan almashtirilgan.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Qurilma-sath juftligi <Badge type="tip" text="oson" />
Hab, repitir, switch, router ni OSI sathiga mos qo'ying.

**Kutiladigan natija:** 4 qurilma va 3 sath juftligi.

### 2. Kabel turlari <Badge type="tip" text="oson" />
Uch kabel turini va har birining bitta xususiyatini yozing.

**Kutiladigan natija:** 3 qatorli jadval.

### 3. Zaiflikmi yoki hujummi <Badge type="tip" text="oson" />
"Maktab routerida admin paroli o'zgartirilmagan" nimaga misol?

**Kutiladigan natija:** Zaiflik, sabab bilan.

### 4. Hab qulayligi <Badge type="tip" text="oson" />
Nega hab bilan o'ralgan tarmoqda boshqalar trafigini ko'rish osonroq?

**Kutiladigan natija:** 1-2 jumlali tushuntirish.

### 5. Switch va ko'prik <Badge type="warning" text="o'rta" />
Farqini yozing.

**Kutiladigan natija:** Bitta oqim va ko'p oqim farqi.

### 6. Router yo'l topmasa <Badge type="warning" text="o'rta" />
Marshrutlash jadvalida yo'l bo'lmasa nima bo'ladi?

**Kutiladigan natija:** Aniq javob.

### 7. Tahdidni tasniflang <Badge type="warning" text="o'rta" />
Ishdan ketgan xodim diskka hali kira oladi. Ichkimi, tashqimi?

**Kutiladigan natija:** Tasnif va sabab.

### 8. Gateway turlari <Badge type="warning" text="o'rta" />
Gatewayning 3 turini sanang.

**Kutiladigan natija:** 3 ta nom va sath.

### 9. Maktab tarmog'i <Badge type="danger" text="qiyin" />
3 xonali maktab uchun tarmoq sxemasini chizing: switch, router, gateway.

**Kutiladigan natija:** Sxema va qisqa izoh.

### 10. Hujum zanjiri <Badge type="danger" text="qiyin" />
Razvedka, kirish, zararli dastur bosqichlarini tartiblang.

**Kutiladigan natija:** Tartib va izoh.

### 11. Xatoni toping <Badge type="danger" text="qiyin" />
"Router 2-sathda MAC ga qaraydi, switch 3-sathda IP ga qaraydi." Nechta xato?

**Kutiladigan natija:** Xatolar ro'yxati va to'g'rilangan gap.

### 12. Switch zaifligi <Badge type="info" text="bonus" />
Qo'llanmada boshqariluvchi switchning afzallik va kamchiliklari qanday sanalgan?

**Kutiladigan natija:** Ikkita ro'yxat.

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Hab va switch farqi nima?
2. Router qaysi sathda va nimaga qaraydi?
3. Optik tolaning ustunligi nima?
4. Zaiflik va tahdid farqi?
5. Ichki tahdid ulushi qancha?
6. Passiv va aktiv razvedka farqi?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Maktab yoki uyingizdagi tarmoq sxemasini chizing (qurilmalar va ularning sathi) va har bir qurilmaning bitta xavfini yozing. Vaqt: 20-30 daqiqa.

</div>

