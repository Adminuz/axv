---
title: "Tarmoq qurilmalari va xavfsizlik muammolari (1-qism): router, switch, hab va ularning zaifliklari"
description: "Tarmoq kabeli, tarmoq kartasi, hab, repitir, ko'prik, switch, router va gateway; zaiflik, tahdid va hujum tushunchalari; ichki va tashqi tahdidlar"
dars: 1
hafta: 4
sinf: 10-sinf-cyber
---

# 10-dars. Tarmoq qurilmalari va xavfsizlik muammolari (1-qism): router, switch, hab va ularning zaifliklari

**Manba:** O'quv qo'llanma, II bob, «Tarmoq qurilmalari va xavfsizlik muammolari» (ma'ruza mashg'uloti); O'quv dasturi, II bob.

## Dars rejasi (80 daqiqa)

1. **Takrorlash (8 daqiqa):** OSI 7 sathi, MAC va IP farqi (9-dars). Savol: «IP qaysi sathda, MAC qaysi sathda?»
2. **Nazariy qism 1 — qurilmalar (27 daqiqa):** tarmoq kabeli (3 tur), tarmoq kartasi (NIC), hab, repitir, ko'prik, switch, router, gateway. Har bir qurilma qaysi OSI sathida ishlashi.
3. **Tanaffus (5 daqiqa).**
4. **Nazariy qism 2 — xavfsizlik muammolari (20 daqiqa):** zaiflik / tahdid / hujum farqi, 5 ta sabab, ichki va tashqi tahdidlar, hujum turlari (razvedka, kirish, parol, MITM, DoS/DDoS, zararli dastur).
5. **Amaliyot (15 daqiqa):** «qurilmani aniqlang» va «tahdidni tasniflang» mashqlari (quyida).
6. **Xulosa va tezkor nazorat (5 daqiqa).**

**Kutiladigan natija:** o'quvchi har bir qurilmaning vazifasi va OSI sathini aytadi; hab bilan switch farqini xavfsizlik nuqtai nazaridan tushuntiradi; zaiflik, tahdid va hujumni aralashtirmaydi.

---

## Asosiy tushunchalar (qo'llanma bo'yicha)

- **Axborot uzatish muhiti:** kompyuterlar o'rtasida axborot almashinuvini ta'minlovchi aloqa kanallari (simli, kabelli yoki simsiz).
- **Tarmoq kabeli, 3 tur:** o'ralgan juft (twisted pair: ekranlangan STP va ekranlanmagan UTP), koaksial (coaxial), optik tolali (fiber optic).
- **Tarmoq kartasi (NIC):** kompyuterning tarmoqqa ulanishini ta'minlovchi apparat komponenti; kabelli, simsiz va USB ko'rinishlari bor; paketlarni uzatadi va qabul qiladi.
- **Hab (konsentrator):** 1-sath (fizik); bir portdan kelgan signalni qolgan barcha portlarga uzatadi.
- **Repitir:** 1-sath; signalni kuchaytirmaydi, balki asl ko'rinishida takrorlaydi (regeneratsiya).
- **Ko'prik (bridge):** 2-sath; freym sarlavhasidagi MAC-manzilni tekshirib segmentlarni birlashtiradi.
- **Switch (kommutator):** 2-sath; ma'lumotni faqat mo'ljallangan qabul qiluvchiga uzatadi.
- **Router (marshrutizator):** 3-sath; qabul qiluvchining IP manziliga va marshrutlash jadvaliga qarab paketni yo'naltiradi.
- **Gateway (shlyuz):** turli tarmoqlar o'rtasidagi aloqani tashkil qiluvchi nuqta/vosita (apparat yoki dasturiy).
- **Zaiflik:** «portlaganida» tizim xavfsizligini buzuvchi kamchilik, loyihalash yoki amalga oshirishdagi xato.
- **Tahdid:** axborot xavfsizligini buzishi mumkin bo'lgan yoki real xavf tug'diruvchi sharoit va omillar majmui.
- **Hujum:** hujumchiga operatsion muhitni boshqarish imkonini beruvchi xavfsizlik buzilishi.

---

## Dars mazmuni

### 1. Tarmoq kabellari

| Kabel | Tuzilishi | Xususiyati (qo'llanma bo'yicha) |
|---|---|---|
| O'ralgan juft (UTP/STP) | 2 ta mis sim bir-biriga o'ralgan, bir necha juftlik umumiy g'ilofda (2 yoki 4 juft) | Eng arzon va eng ko'p tarqalgan; egiluvchan; 100 Mbit/s (1000 Mbit/s ustida ishlanmoqda) |
| Koaksial | Markaziy mis sim, dielektrik, sim to'qima (ekran), tashqi qoplama | Himoyalangan; 500 Mbit/s gacha; km masofa; ruxsatsiz mexanik ulanish qiyin; qimmat (1,5-3 barobar), ta'mirlash murakkab |
| Optik tolali | Shaffof shisha tola (1-10 mkm) | Axborot elektr signali emas, yorug'lik bilan; o'nlab km; 10 Gbit/s gacha |

### 2. Tarmoq kartasi (NIC)

Network Interface Card = network adapter = LAN adapter (bir xil ma'noda). Vazifasi: kompyuterni tarmoqqa ulash, paketlarni uzatish/qabul qilish, ma'lumotni analogdan raqamliga va aksincha aylantirish. Ko'rinishlari: kabelli, simsiz, USB. (9-darsdagi MAC manzil aynan NIC ga beriladi.)

### 3. Hab, repitir, ko'prik, switch, router: 3 sathga bo'lib o'rganish

```
OSI sath            Qurilma            Nimaga qaraydi?            Ma'lumotni qayerga beradi?
-------------------------------------------------------------------------------------------
3  Tarmoq           Router             IP manzil + marshrut jadvali   Eng yaxshi yo'lga
2  Kanal            Switch, Ko'prik    MAC manzil                     Faqat mo'ljallangan portga
1  Fizik            Hab, Repitir       Hech narsaga (signal)          Barcha portlarga (hab)
```

**Hab.** 1-sathda ishlaydi. Bir portdan kelgan signalni qolgan barcha portlarga qayta uzatadi. Jismonan «yulduz», lekin mantiqan umumiy shina: o'tkazuvchanlik barcha qurilmalar o'rtasida bo'linadi, yarim dupleks rejim. Hozir deyarli to'liq switch almashtirgan.

**Repitir.** 1-sath. Signalni kuchaytirmaydi, regeneratsiya qiladi: kirishda qabul qiladi, asl ko'rinishini aniqlaydi, chiqishda aniq nusxasini qayta yaratadi. Dastlab koaksial/shina Ethernetda uzun segmentlarni ulash uchun. Hab = ko'p portli repitir (kelgan portdan tashqari hammasiga).

**Ko'prik.** 2-sath. Freym sarlavhasidagi MAC ni tekshiradi: manzil shu segmentga tegishli bo'lsa to'g'ri segmentga uzatadi, bo'lmasa hech narsa qilmaydi. Ko'prik va switch farqi: ko'prik bir vaqtda faqat bitta oqimni va faqat ikki port orasida (ketma-ket), switch esa bir vaqtda ko'p oqimni (parallel).

**Switch.** 2-sath. Habdan farqi: trafikni faqat bevosita mo'ljallangan qabul qiluvchiga uzatadi. Natija: unumdorlik va xavfsizlik oshadi, chunki boshqalar o'zlariga mo'ljallanmagan ma'lumotni olmaydi (va bunga ruxsat ham yo'q). Boshqariluvchi switch MAC-manzil, port va freym sarlavhasi bo'yicha filtrlay oladi, ammo kamchiligi: **MAC-manzilni almashtirish hujumiga zaif**.

**Router.** 3-sath. Marshrutlash jadvali va administrator qoidalari asosida segmentlar o'rtasida paket uzatadi; turli arxitekturadagi tarmoqlarni bog'laydi. Qabul qiluvchi IP ga qaraydi; jadvalda yo'l bo'lmasa **paket tashlab yuboriladi**. Qo'shimcha funksiyalari: NAT, filtrlash (kirish-chiqish nazorati), shifrlash/deshifrlash, trafikni boshqarish.

**Gateway.** Turlari: (1) tarmoq shlyuzi, 3-4 sathlar, ichki va global tarmoq orasidagi trafikni nazorat qiluvchi nuqta; (2) kompaniya uchun internet-shlyuz, 7-sath, HTTP(S) orqali veb-resurslardan foydalanishni cheklash; (3) oraliq gateway, tunel zanjirlarini qo'llab-quvvatlaydigan router yoki OT. Apparat yoki dasturiy bo'lishi mumkin.

### 4. Tarmoq xavfsizligi muammolari

**Uch tushuncha (aralashtirmang):**

| Tushuncha | Savol | Misol (mentor misoli, hujjatda yo'q, tushuntirish uchun) |
|---|---|---|
| Zaiflik | «Qayerda kamchilik bor?» | Yangilanmagan brauzer, noto'g'ri sozlangan router |
| Tahdid | «Nima xavf solishi mumkin?» | Ichkaridagi xafa xodim, tashqi hujumchi |
| Hujum | «Nima sodir bo'ldi?» | Zaiflikdan foydalanib tizimga kirish |

**Tarmoq xavfsizligi muammolari sabablari (qo'llanmada 5 ta):**
1. Qurilma yoki dasturning noto'g'ri sozlanishi (shifrlanmagan protokol maxfiy ma'lumotni oshkor qiladi);
2. Tarmoqni xavfsiz bo'lmagan tarzda, zaif loyihalash (firewall, IDS, VPN noto'g'ri qo'llansa, tarmoq zaif bo'ladi);
3. Tug'ma texnologik zaiflik (qurilma/dastur ma'lum hujumni bartaraf eta olmaydi, masalan yangilanmagan brauzer);
4. Foydalanuvchilarning e'tiborsizligi (ma'lumot yo'qolishi, sirqib chiqishi);
5. Foydalanuvchilarning qasddan harakati (ishdan ketgan xodimning taqsimlangan diskka kirishi saqlanib qolishi).

**Tahdid turlari:**
- **Ichki tahdidlar:** kompyuter/internetga aloqador jinoyatlarning 80% ini tashkil etadi (qo'llanma bo'yicha); xafa yoki g'araz niyatli xodimlar, ko'pincha imtiyozli foydalanuvchilar.
- **Tashqi tahdidlar:** mavjud zaiflik orqali; **tizimlashgan** (yuqori malakali, zaiflikni tez topadi) va **tizimlashmagan** (malakasiz, tayyor skript va vositalar bilan).

**Tarmoq hujumlari tasnifi:**
- **Razvedka:** aktiv (portlar va OT skanerlash, paket yuborish) va passiv (trafikdan axborot yig'ish, `sniffer` dasturi);
- **Kirish hujumlari:** ruxsatsiz foydalanish, qo'pol kuch, imtiyozni orttirish, MITM;
- **Parolga qaratilgan:** lug'at, qo'pol kuch, gibrid, Rainbow jadvali;
- **MITM (o'rtada turgan odam):** aloqaga suqilib kiradi, soxta xabar yuborishi mumkin;
- **DoS/DDoS:** xizmatni cheklash; DDoS zombi kompyuterlar orqali; ma'lumot o'g'irlanmasa ham tashkilot ishi to'xtaydi;
- **Zararli dasturlar:** virus, troyan, adware, spyware, rootkit, backdoor, mantiqiy bomba, botnet, ransomware.

**Qurilma va xavf bog'lanishi (dars xulosasi):** hab trafikni hammaga uzatgani uchun passiv razvedka (sniffer) uchun qulay; switch trafikni ajratadi, lekin MAC almashtirish hujumiga zaif; router/gateway perimetr nazorati nuqtasi, noto'g'ri sozlansa butun tarmoq zaif.

---

## Amaliyot (15 daqiqa, daftarda/jadvalda)

**A. «Qurilmani aniqlang».** Jadval: qurilma, OSI sath, nimaga qaraydi. Mentor sinfga stsenariylar o'qiydi, o'quvchilar qurilmani topadi.

**B. «Tahdidni tasniflang».** Har bir holat uchun: zaiflikmi, tahdidmi yoki hujummi; ichkimi yoki tashqimi.

---

## Mustaqil topshiriqlar

### 1. Qurilmani sathga moslash · oson
Quyidagilarni OSI sathiga mos qo'ying: hab, switch, router, repitir.
**Yechim:** hab va repitir: 1-sath (fizik); switch: 2-sath (kanal); router: 3-sath (tarmoq).

### 2. Uch kabel turi · oson
Tarmoq kabellarining 3 turini va har birining bittadan asosiy xususiyatini yozing.
**Yechim:** o'ralgan juft (UTP/STP): arzon va eng tarqalgan; koaksial: ekranli, himoyalangan, 500 Mbit/s gacha, qimmat; optik tola: yorug'lik bilan, o'nlab km va 10 Gbit/s gacha.

### 3. Zaiflik, tahdid yoki hujum · oson
«Maktab routerida administrator paroli o'zgartirilmagan» gap nimaga misol?
**Yechim:** Zaiflik (noto'g'ri sozlash). Hali hech kim bundan foydalanmagan, shuning uchun bu hujum emas; kimdir foydalansa, hujum bo'ladi. Foydalanishi mumkin bo'lgan shaxs yoki omil esa tahdid.

### 4. Hab nima uchun xavfli · oson
Nega hab bilan o'ralgan tarmoqda boshqa kompyuterlar trafigini ko'rish ehtimoli yuqori?
**Yechim:** hab bir portdan kelgan signalni qolgan barcha portlarga uzatadi (1-sath, umumiy muhit), shuning uchun har bir qurilma boshqalarga mo'ljallangan ma'lumotni ham oladi; passiv razvedka (sniffer) uchun qulay.

### 5. Switch va ko'prik · o'rta
Switch va ko'prik farqini ayting.
**Yechim:** ikkalasi 2-sathda MAC bilan ishlaydi. Ko'prik bir vaqtda faqat bitta oqimni va ikki port orasida (ketma-ket), switch bir vaqtda ko'p portlar orasida bir nechta oqimni (parallel) uzatadi; switch ko'pportli ko'prik sifatida qaraladi.

### 6. Router yo'lni topa olmasa · o'rta
Router paketni olganda marshrutlash jadvalida qabul qiluvchi uchun yo'l bo'lmasa nima bo'ladi? U qaysi manzilga qaraydi?
**Yechim:** paket tashlab yuboriladi. Router qabul qiluvchining IP manziliga qaraydi va marshrutlash jadvali bilan solishtiradi.

### 7. Ichki va tashqi tahdid · o'rta
Quyidagilarni tasniflang: (a) ishdan ketgan xodim diskka hali kira oladi; (b) tayyor skript bilan sinab ko'ruvchi notanish shaxs; (c) yuqori malakali guruh zaiflikni topdi.
**Yechim:** (a) ichki (qasddan harakat sababi bilan bog'liq); (b) tashqi tizimlashmagan; (c) tashqi tizimlashgan.

### 8. Repitir va hab bog'lanishi · o'rta
Hab repitirdan nimasi bilan farq qiladi?
**Yechim:** vazifasi fizik jihatdan o'xshash (signalni takrorlash), ammo hab ko'p portli: tiklangan signalni kelgan portdan tashqari barcha faol portlarga uzatadi; repitir odatda ikki portli.

### 9. Maktab tarmog'ini loyihalash · qiyin
Maktabda 3 xona va internet bor. Qaysi qurilmalarni qaysi joyga qo'yasiz? Hab o'rniga nega switch tanlanadi? Gateway/router qayerda?
**Yechim:** (namunaviy) har xonada switch (trafikni faqat mo'ljallangan qabul qiluvchiga beradi, unumdorlik va xavfsizlik oshadi), switchlar maktab routeriga ulanadi; router/gateway ichki tarmoq va internet chegarasida (NAT, filtrlash, trafikni nazorat). Hab ishlatilmaydi: umumiy muhit va passiv razvedka xavfi.

### 10. Hujum zanjirini tuzish · qiyin
Razvedka, kirish va zararli dastur bosqichlarini mantiqiy tartibda joylashtiring va har birini bir jumla bilan tushuntiring.
**Yechim:** 1) razvedka: tarmoq, tizim, tashkilot haqida axborot yig'ish (aktiv/passiv); 2) kirish: ruxsatsiz foydalanish, parol hujumi, MITM; 3) zararli dastur: kirgandan keyin virus/troyan/backdoor/ransomware orqali nazoratni qo'lga olish yoki ma'lumotni o'g'irlash.

### 11. Xatoni toping · qiyin
Do'stingiz aytdi: «Router 2-sathda ishlaydi va MAC manzilga qarab paketni yo'naltiradi. Switch esa 3-sathda IP ga qaraydi. Hab trafikni faqat kerakli portga beradi». Nechta xato bor, to'g'rilang.
**Yechim:** uchala gapda ham xato. Router 3-sathda ishlaydi va qabul qiluvchining IP manziliga (marshrutlash jadvaliga) qaraydi; switch 2-sathda ishlaydi va MAC bilan faqat mo'ljallangan qabul qiluvchiga uzatadi; hab 1-sathda ishlaydi va signalni barcha portlarga uzatadi.

### 12. Switch zaifligini tushuntirish · bonus
Boshqariluvchi kommutatorning afzalliklari va kamchiliklari qo'llanmada qanday sanalgan? Nega "MAC almashtirish" xavfli?
**Yechim:** afzalligi: guruh qurilmalarini boshqarish qulayligi, lokal tarmoq unumdorligining oshishi, MAC/port/sarlavha bo'yicha filtrlash. Kamchiligi: funksionallik cheklangan, fizik rekonfiguratsiya noqulay, MAC-manzilni almashtirish hujumiga zaif (hujumchi boshqa qurilma manzilini taqlid qilib filtrdan o'tishi mumkin).

---

## Tezkor savol-javob

1. **Savol:** Qaysi qurilma signalni barcha portlarga uzatadi? **Javob:** Hab (1-sath).
2. **Savol:** Router qaysi sathda? **Javob:** 3-sath (tarmoq), IP manzilga qaraydi.
3. **Savol:** Zaiflik va hujum farqi? **Javob:** zaiflik kamchilik, hujum esa undan foydalanish.
4. **Savol:** Ichki tahdidlar jinoyatlarning qancha qismini tashkil etadi (qo'llanma bo'yicha)? **Javob:** 80%.

---

## Mentor uchun eslatma

- Hujjatda fizik rasmlar bor (2.7-2.13), slaydda ularning o'rniga sxemalar berilgan; imkon bo'lsa sinfga haqiqiy kabel/switch/router ko'rsating (qo'llanmada o'quv xonasida 2-3 router va 2 switch bo'lishi yozilgan).
- «Misol» deb belgilangan jadvaldagi hayotiy misollar mentor tomonidan tushuntirish uchun qo'shilgan, hujjatdagi ta'rif emas.
- Hujjat nomuvofiqligi: dasturda «repetir/hab», qo'llanmada «repitir/konsentrator». Dars davomida ikkala nomni ayting.
- Amaliy hujum buyruqlari (arpspoof va h.k.) bu darsda o'tilmaydi, faqat nazariy tasniflash; amaliy laboratoriya keyingi haftalarda.
