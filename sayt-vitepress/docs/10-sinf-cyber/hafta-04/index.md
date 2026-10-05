---
title: "4-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "10-sinf (Cyber)", "link": "/10-sinf-cyber/"}, "n": 4, "bob": "II-bob · Kompyuter tarmoqlari va Internet xavfsizligi", "lessons": [{"g": 10, "title": "Tarmoq qurilmalari va xavfsizlik muammolari (1-qism): router, switch, hab va ularning zaifliklari", "lead": "Maktab Wi-Fi'ingiz orqasida qaysi qurilmalar ishlaydi va ularning qaysi biri hujumchiga qulay? Bugun tarmoqning \"yo'l belgilari\"ni o'rganamiz.", "link": "/10-sinf-cyber/hafta-04/dars-1", "slide": "/slaydlar/10-sinf-cyber/hafta-04/dars-1.html", "test": "/slaydlar/10-sinf-cyber/hafta-04/dars-1-test.html"}, {"g": 11, "title": "Tarmoq qurilmalari va xavfsizlik muammolari (2-qism): Wireshark yordamida tarmoq trafigini tahlil qilish", "lead": "Sayt ochish bir marta bosishga o'xshaydi, lekin ichkarida o'nlab paketlar uchib yuradi. Wireshark ularni ko'rinadigan qiladi.", "link": "/10-sinf-cyber/hafta-04/dars-2", "slide": "/slaydlar/10-sinf-cyber/hafta-04/dars-2.html", "test": "/slaydlar/10-sinf-cyber/hafta-04/dars-2-test.html"}, {"g": 12, "title": "Tarmoq qurilmalari va xavfsizlik muammolari (3-qism): ping va traceroute buyruqlari bilan marshrutlarni tahlil qilish", "lead": "Siz yuborgan paket sayt serveriga yetguncha nechta routerdan o'tadi? Ikki kichik buyruq bu savolga javob beradi.", "link": "/10-sinf-cyber/hafta-04/dars-3", "slide": "/slaydlar/10-sinf-cyber/hafta-04/dars-3.html", "test": "/slaydlar/10-sinf-cyber/hafta-04/dars-3-test.html"}], "test": "/slaydlar/10-sinf-cyber/hafta-04/hafta-test.html"}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Ushbu haftada o'tilgan darslar bo'yicha mustaqil amaliy uyga vazifalar (har biri 20-30 daqiqa).

---

### 10-dars. Tarmoq qurilmalari va xavfsizlik muammolari (1-qism)
1. Maktab yoki uyingizdagi tarmoq sxemasini chizing: kompyuter, switch, router, gateway va internet. Har bir qurilma yoniga OSI sathini yozing.
2. Hab, switch va router uchun jadval tuzing: qaysi sathda, nimaga qaraydi, ma'lumotni qayerga beradi.
3. Quyidagi 5 holatni zaiflik, tahdid yoki hujum deb tasniflang va ichki yoki tashqi ekanini yozing: (a) yangilanmagan brauzer; (b) ishdan ketgan xodim diskka kira oladi; (c) tayyor skript bilan sinab ko'ruvchi notanish shaxs; (d) server DDoS ostida; (e) shifrlanmagan protokol ma'lumotni oshkor qiladi.

---

### 11-dars. Wireshark yordamida tarmoq trafigini tahlil qilish
1. Kompyuteringizga Wiresharkni o'rnating (Npcap bilan) va faol interfeysni tanlab, capture boshlang. Oynaning 3 panelini skrinshotda belgilang.
2. `http` va `tls` filtrlari bilan har birida GET so'rovi va TLS Client Hello paketini toping.
3. TCP, UDP, DNS va ICMP protokollari bo'yicha kamida 3 tadan paketni tahlil qilib (Source, Destination, Protocol, Info), natijalarni fayl ko'rinishida saqlang va hisobot tayyorlang.
4. Sayt ochilishini 4 bosqichda o'z so'zlaringiz bilan yozing.

---

### 12-dars. Ping va traceroute buyruqlari bilan marshrutlarni tahlil qilish
1. 4 ta turli saytga `ping` yuboring. Jadval: sayt, o'rtacha ms, yo'qotish %, TTL, taxminiy hop soni (128 yoki 64 dan ayirib).
2. Shu saytlarga `tracert` (Linux/Mac: `traceroute`) yuboring; kamida bittasida flaglardan foydalaning (`-d`, `-h`, `-w`).
3. Bitta marshrutni hop-hop izohlang: uy routeri, provayder, O'zbekiston uzeli, tashqi tranzit, manzil.
4. `* * *` chiqqan bo'lsa, buning mumkin bo'lgan sababini yozing.

---

</div>
