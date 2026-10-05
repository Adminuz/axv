---
title: "1-dars. Kiberxavfsizlik asoslari: axborot xavfsizligi, kiberjinoyat, kiberqonun, inson omili va aktivlar"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (Cyber)", "link": "/10-sinf-cyber/"}, "week": {"n": 1, "link": "/10-sinf-cyber/hafta-01/"}, "g": 1, "title": "Kiberxavfsizlik asoslari: axborot xavfsizligi, kiberjinoyat, kiberqonun, inson omili va aktivlar", "lead": "Kiberxavfsizlik asoslari: axborot xavfsizligi, kiberjinoyat, kiberqonun, inson omili va aktivlar", "slide": "/slaydlar/10-sinf-cyber/hafta-01/dars-1.html", "test": "/slaydlar/10-sinf-cyber/hafta-01/dars-1-test.html", "tabs": [{"g": 1, "link": "/10-sinf-cyber/hafta-01/dars-1", "current": true}, {"g": 2, "link": "/10-sinf-cyber/hafta-01/dars-2", "current": false}, {"g": 3, "link": "/10-sinf-cyber/hafta-01/dars-3", "current": false}], "prev": null, "next": {"g": 2, "title": "Kibertahdidlarning turlari (1-qism): zararli dasturlar va DoS/DDoS hujumlari", "link": "/10-sinf-cyber/hafta-01/dars-2"}}
---

---
title: "Kiberxavfsizlik asoslari: axborot xavfsizligi, kiberjinoyat, kiberqonun, inson omili va aktivlar"
description: "Kiberxavfsizlik va axborot xavfsizligi tushunchalari, Alisa-Bob-Tridi modeli, O'zbekiston kiberxavfsizlik qonuni, inson omili hamda himoya sohalari"
dars: 1
hafta: 1
sinf: 10-sinf-cyber
---

<div class="blk">

## <Icon name="file-text" /> Reja

1. Axborot xavfsizligi va kiberxavfsizlik tushunchalari hamda ularning o'zaro farqi.
2. Axborot xavfsizligining klassik timsollari: Alisa, Bob va Tridi modeli (AOB ssenariysi).
3. Aktiv, tahdid, zaiflik va kiberhujum tushunchalari.
4. O'zbekiston Respublikasining «Kiberxavfsizlik to'g'risida»gi O'RQ-764-sonli Qonuni.
5. Axborot xavfsizligida inson omili va xavfsizlik madaniyati.
6. Axborot xavfsizligining 5 ta sohasi: Tarmoq, Ilova, Ma'lumot, Qurilma va Bulut xavfsizligi.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Nazariy qism

### 1. Axborot xavfsizligi va Kiberxavfsizlik nima?

Raqamli dunyoda «axborot xavfsizligi» va «kiberxavfsizlik» so'zlari ko'p ishlatiladi, biroq ularning mohiyatida muhim farq bor:

- **Axborot xavfsizligi (Information Security):** Axborot qaysi ko'rinishda bo'lishidan qat'i nazar (qog'oz hujjatlar, arxivlar, xodimlar orasidagi og'zaki suhbatlar, kompyuter fayllari), unga ruxsatsiz kirish, nusxalash, o'zgartirish yoki yo'q qilishning oldini olish choralaridir.
- **Kiberxavfsizlik (Cybersecurity):** Aynan kibermakondagi — ya'ni kompyuterlar, serverlar, mobil qurilmalar, tarmoqlar va elektron ma'lumotlar bazalaridagi axborotni tashqi va ichki tahdidlardan himoyalash holatidir.

```
+-------------------------------------------------------------+
|              AXBOROT XAVFSIZLIGI (Keng qamrovli)            |
|  (Qog'oz hujjatlar, arxivlar, xodimlar suhbati, qonunlar)    |
|                                                             |
|       +---------------------------------------------+       |
|       |             KIBERXAVFSIZLIK                 |       |
|       |  (Raqamli ma'lumotlar, tarmoqlar, bulut,    |       |
|       |   operatsion tizimlar, smartfonlar, API)    |       |
|       +---------------------------------------------+       |
+-------------------------------------------------------------+
```

### 2. Axborot xavfsizligining timsollari: Alisa, Bob va Tridi

Kiberxavfsizlik va kriptografiya sohasida xavfsizlik ssenariylarini tushuntirish uchun an'anaviy ramziy qahramonlardan foydalaniladi:
- **Alisa (Alice):** Tizim egasi yoki xabar yuboruvchi qonuniy tomon (masalan, bank yoki veb-xizmat egasi).
- **Bob (Bob):** Qonuniy foydalanuvchi yoki mijoz (masalan, bank mijozi).
- **Tridi (Trudy / Eve):** Hujumchi (adversary / intruder), Alisa va Bob o'rtasidagi aloqaga xalaqit beruvchi, xabarlarni tutib oluvchi yoki buzuvchi uchinchi tomon.

**Alisaning Onlayn Banki (AOB) ssenariysi:**
- Bob Alisaning onlayn banki orqali hisobini tekshiradi va to'lovlarni amalga oshiradi.
- Bob uchun xavfsizlik muammosi — uning balansi va parolini Tridi bilib olmasligi va mablag'lari xavfsiz bo'lishi.
- Alisa uchun xavfsizlik muammosi — tizim to'xtovsiz ishlashi, mijozlar balansi buzilmasligi va bank obro'si saqlanishi.
- Tridining maqsadi — Bob yoki Alisaning zaifliklaridan foydalanib mablag'larni o'g'irlash yoki tizimni ishdan chiqarish.

### 3. Asosiy kiberxavfsizlik atamalari

| Atama | Ta'rif | Misol |
|---|---|---|
| **Aktiv (Asset)** | Tashkilot yoki shaxs uchun qadrli bo'lgan barcha ma'lumot va resurslar | Mijozlar bazasi, serverlar, shaxsiy fotosuratlar |
| **Zaiflik (Vulnerability)** | Tizim yoki xavfsizlik boshqaruvidagi kamchilik yoki xato | Dasturda yangilanish yo'qligi, ochiq port, oddiy parol |
| **Kibertahdid (Threat)** | Aktivlarga zarar yetkazishi mumkin bo'lgan potensial xavf | Ransomware virusi, xakerlar guruhi, toshqin |
| **Kiberhujum (Attack)** | Zaiflikdan foydalanib aktivga zarar yetkazish harakati | Parolni tanlash (brute-force), veb-saytga DoS hujumi |

### 4. O'zbekiston Respublikasining «Kiberxavfsizlik to'g'risida»gi Qonuni

2022-yil 15-aprelda O'zbekiston Respublikasining **«Kiberxavfsizlik to'g'risida»gi O'RQ-764-sonli Qonuni** qabul qilindi.
- Qonun kibermakonda shaxs, jamiyat va davlat manfaatlarini himoya qilishni huquqiy jihatdan kafolatlaydi.
- Davlat organlari, banklar va kritik infratuzilma tashkilotlariga o'z tizimlarini kiberxavfsizlik ekspertizasidan o'tkazish majburiyati yuklatilgan.
- Kiberjinoyatlar (ruxsatsiz kirish, ma'lumotlarni o'g'irlash, zararli dastur yaratish) Jinoyat kodeksi bo'yicha jiddiy javobgarlikka sabab bo'ladi.

### 5. Inson omili — eng zaif zanjir

Zamonaviy tizimlarda eng kuchli shifrlash va eng qimmatli tarmoq himoyasi o'rnatilgan bo'lsa ham, kiberhujumlarning 95 foizi inson xatosi tufayli yuz beradi:
- Oddiy va bir xil parollardan foydalanish;
- Shubhali havolalarni tekshirmasdan bosish;
- Xavfsizlik sertifikati ogohlantirishlarini e'tiborsiz qoldirish;
- Shaxsiy ma'lumotlarni ijtimoiy tarmoqlarda ochiq qoldirish.

Shuning uchun xavfsizlik faqat dasturiy ta'minot emas, balki **xavfsizlik madaniyati** va **ogohlikdir**.

### 6. Axborot xavfsizligining 5 ta sohasi

1. **Tarmoq xavfsizligi (Network Security):** Tarmoq infratuzilmasi, routerlar, firewall va VPN xizmatlarini himoya qilish.
2. **Ilova xavfsizligi (Application Security):** Dasturlar va saytlarni yaratish jarayonida xatolik va zaifliklardan xoli qilish.
3. **Ma'lumotlar xavfsizligi (Data Security):** Ma'lumotlarni shifrlash, zaxiralash va sizib chiqishdan himoya qilish (DLP).
4. **Qurilma xavfsizligi (Endpoint Security):** Kompyuterlar, noutbuklar va telefonlarni antivirus va xavfsizlik tizimlari bilan jihozlash.
5. **Bulut xavfsizligi (Cloud Security):** Bulutli serverlar va virtual muhitdagi ma'lumotlarni himoyalash.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy laboratoriya

Kichik tashkilot (masalan, maktab elektron jurnali yoki kichik kafe buyurtma tizimi) misolida aktivlarni aniqlash va xavflarni tahlil qilish:

1. **Aktivlarni aniqlash:** Tizimda qanday ma'lumotlar va qurilmalar bor? (Baho bazasi, o'quvchilar pasport ma'lumotlari, Wi-Fi router).
2. **Zaifliklarni ko'rib chiqish:** Routerda standart admin paroli o'zgartirilmaganmi? Parollar ochiq matnda saqlanadimi?
3. **Himoya rejasini tuzish:** Parol siyosatini kuchaytirish, 2FA yoqish, ma'lumotlar bazasini shifrlash.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy topshiriqlar

### 1. Xavfsizlik turlarini ajratish &lt;Badge type="tip" text="oson" />
Kompaniya ofisidagi arxiv xonasi kalit bilan qulflangan, ammo server xonasining Wi-Fi tarmog'i parolsiz ochiq qoldirilgan. Ushbu holatda axborot xavfsizligi va kiberxavfsizlik qay darajada ta'minlanganligini izohlang.

### 2. Alisa, Bob va Tridi ssenariysi &lt;Badge type="tip" text="oson" />
Elektron tijorat saytida Bob Alisadan krossovka buyurtma qilmoqda. Tridi ularning aloqasini kuzatib, Bobning yetkazib berish manzilini o'z manziliga o'zgartirib qo'ydi. Bu yerda Tridi qanday xatti-harakat qildi va qanday xavfsizlik xususiyati buzildi?

### 3. Kiberxavfsizlik to'g'risidagi qonun &lt;Badge type="warning" text="o'rta" />
O'zbekiston Respublikasining O'RQ-764-sonli Qonuni talablariga ko'ra, davlat organlari va muhim axborot infratuzilmasi tashkilotlari kiberhujum yuz berganda nima qilishi shart?

### 4. Aktivlar qiymati tahlili &lt;Badge type="warning" text="o'rta" />
Tibbiy klinikaning serverida quyidagilar saqlanadi:
a) Bemorlarning to'liq kasallik tarixi va laboratoriya testlari;
b) Klinika xodimlarining tushlik navbatchilik jadvali;
c) Kutish zalidagi mehmon Wi-Fi paroli.
Ushbu 3 aktivni xavflilik darajasi (kritik, o'rta, past) bo'yicha taqsimlang va sababini tushuntiring.

### 5. Inson omili tahlili &lt;Badge type="warning" text="o'rta" />
Kompaniyada 50 000 dollarlik zamonaviy tarmoqlararo ekran (Firewall) o'rnatilgan. Buxgalter elektron pochtasiga kelgan «Shoshilinch soliq hisoboti» degan faylni ochib, kompyuterini virus bilan zararladi. Nima sababdan qimmatbaho texnika bu vaziyatda yordam bermadi?

### 6. Zaiflik va tahdidni farqlash &lt;Badge type="tip" text="oson" />
Quyidagi ikki jumlani o'qing va qaysi biri zaiflik, qaysi biri tahdid ekanini aniqlang:
1. «Veb-serverda 4 yildan beri yangilanmagan dastur ishlamoqda.»
2. «Buzg'unchi avtomatlashtirilgan dastur yordamida veb-server portlarini skaner qilmoqda.»

### 7. Axborot xavfsizligi sohalari &lt;Badge type="warning" text="o'rta" />
Quyidagi choralarni axborot xavfsizligining 5 ta sohasiga (Tarmoq, Ilova, Ma'lumot, Qurilma, Bulut) moslang:
a) Xodimlarning noutbuklariga BitLocker shifrlashini o'rnatish;
b) Saytdagi login formasida SQL inyeksiya zaifligini yopish;
c) AWS S3 xotirasiga kirish huquqlarini cheklash;
d) Routerda portlarni filtrlash qoidalarini yozish.

### 8. Kiberjinoyat motivatsiyalari &lt;Badge type="warning" text="o'rta" />
Kiberjinoyatchilarni kiberhujumlar uyushtirishga undovchi 4 ta asosiy sababni yozing va har biriga real hayotdan misol keltiring.

### 9. Xavfsizlik madaniyati so'rovnomasi &lt;Badge type="danger" text="qiyin" />
Kichik tashkilot xodimlarining kiberxavfsizlikka oid ogohligini tekshirish uchun 5 ta savoldan iborat qisqa audit so'rovnomasini tuzing.

### 10. Alisa va Bob himoya strategiyasi &lt;Badge type="info" text="bonus" />
Alisaning Onlayn Bankiga Tridi millionlab noto'g'ri parollarni kiritib Bobning akkauntini buzishga urinmoqda (brute-force). Tizim xavfsizlik muhandisi sifatida ushbu hujumni to'xtatish uchun kamida 3 ta texnik himoya chorasini taklif qiling.

---

</div>

<div class="blk">

## <Icon name="file-text" /> O'z-o'zini tekshirish savollari

1. Kiberxavfsizlik va axborot xavfsizligi o'rtasidagi asosiy farq nima?
2. Alisa, Bob va Tridi modellari kimlarni ifodalaydi?
3. Nima sababdan inson xavfsizlik tizimidagi eng zaif nuqta hisoblanadi?
4. O'zbekiston Respublikasining kiberxavfsizlik to'g'risidagi qonuni qachon qabul qilingan?
5. Axborot xavfsizligining 5 ta sohasi qaysilar?

---

</div>

<div class="blk">

## <Icon name="file-text" /> Foydali manbalar

- O'zbekiston Respublikasining «Kiberxavfsizlik to'g'risida»gi O'RQ-764-sonli Qonuni (lex.uz).
- UZCERT Kiberxavfsizlik hodisalariga chora ko'rish xizmati hisobotlari.
- NIST Cybersecurity Framework asoslari.

</div>

