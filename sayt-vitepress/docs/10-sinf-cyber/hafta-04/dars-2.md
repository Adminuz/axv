---
title: "11-dars. Tarmoq qurilmalari va xavfsizlik muammolari (2-qism): Wireshark yordamida tarmoq trafigini tahlil qilish"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (Cyber)", "link": "/10-sinf-cyber/"}, "week": {"n": 4, "link": "/10-sinf-cyber/hafta-04/"}, "g": 11, "title": "Tarmoq qurilmalari va xavfsizlik muammolari (2-qism): Wireshark yordamida tarmoq trafigini tahlil qilish", "lead": "Sayt ochish bir marta bosishga o'xshaydi, lekin ichkarida o'nlab paketlar uchib yuradi. Wireshark ularni ko'rinadigan qiladi.", "slide": "/slaydlar/10-sinf-cyber/hafta-04/dars-2.html", "test": "/slaydlar/10-sinf-cyber/hafta-04/dars-2-test.html", "tabs": [{"g": 10, "link": "/10-sinf-cyber/hafta-04/dars-1", "current": false}, {"g": 11, "link": "/10-sinf-cyber/hafta-04/dars-2", "current": true}, {"g": 12, "link": "/10-sinf-cyber/hafta-04/dars-3", "current": false}], "prev": {"g": 10, "title": "Tarmoq qurilmalari va xavfsizlik muammolari (1-qism): router, switch, hab va ularning zaifliklari", "link": "/10-sinf-cyber/hafta-04/dars-1"}, "next": {"g": 12, "title": "Tarmoq qurilmalari va xavfsizlik muammolari (3-qism): ping va traceroute buyruqlari bilan marshrutlarni tahlil qilish", "link": "/10-sinf-cyber/hafta-04/dars-3"}}
---

---
title: "Tarmoq qurilmalari va xavfsizlik muammolari (2-qism): Wireshark yordamida tarmoq trafigini tahlil qilish"
description: "Paket, Wireshark, capture, 3 panel, http va tls filtrlari"
dars: 2
hafta: 4
sinf: 10-sinf-cyber
---

<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- Internetdagi har bir harakat paketlardan iborat.
- Paket ichida IP, protokol (TCP/UDP/ICMP) va ma'lumot bor.
- Wireshark paketlarni tutib, har qatlamini ochib ko'rsatadi.
- O'rnatishda Npcap majburiy.
- Faol interfeysni (yashil chiziq) tanlab, ko'k shark belgisini bosamiz.
- Oyna 3 qism: paketlar ro'yxati, Packet Details, Hex+ASCII.
- `http` filtri GET so'rovini, `tls` filtri TLS Handshake ni ko'rsatadi.
- Sayt ochilishi: DNS, TCP handshake, TLS, HTTP GET.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### Paket: pochta jo'natmasi
Paket konvertga o'xshaydi: tashqarida manzil (IP), ichida xat (data). Wireshark konvertni ochib, ichidagi har bir qatlamni ko'rsatadi. (Bu o'xshatish.)

### Uch panelni qanday o'qish
1. Yuqorisidan paketni tanlang (No., Time, Source, Destination, Protocol, Length, Info).
2. O'rtada qatlamlarni kengaytiring: Ethernet, IP, TCP/UDP, HTTP/DNS. TCP da SYN va ACK bayroqlari.
3. Pastda xom ko'rinish. Login/parol HTTP orqali ketsa, shu yerda ochiq ko'rinadi.

### HTTP va HTTPS
HTTP da so'rov ochiq. HTTPS da `tls` filtri bilan faqat TLS Handshake (Client Hello) ko'rinadi, keyingi aloqa shifrlangan.

### Etika
Faqat o'z kompyuteringiz yoki ruxsat berilgan laboratoriya trafigini tahlil qiling.

### Odatiy xatolar
- Npcap o'rnatilmagan.
- Noto'g'ri interfeys tanlangan.
- HTTPS paketida parolni qidirish: u shifrlangan.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Paket | Tarmoq orqali uzatiladigan ma'lumot bo'lagi |
| Wireshark | Paketlarni tutib tahlil qiluvchi bepul vosita |
| Capture | Paketlarni tutib olish jarayoni |
| Interfeys | Tarmoqqa ulanish nuqtasi (Wi-Fi, Ethernet, Loopback) |
| Filtr | Ko'rinadigan paketlarni tanlash qoidasi |
| GET | HTTP so'rovi turi, 7-sath |
| TLS Handshake | Shifrlangan aloqaning boshlanishi |
| SYN, ACK | TCP bayroqlari |
| Hex | Paketning 16 lik sanoq tizimidagi ko'rinishi |
| ASCII | Baytlarning matn ko'rinishi |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Wireshark paketlarni soniyasiga 100-1000 tagacha ko'rsatishi mumkin.
- Qo'llanmaga ko'ra Wireshark eng mashhur bepul tahlil vositalaridan biri.
- Rasmiy dasturiy vositalar ro'yxatida Wireshark va tcpdump bor.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Wireshark vazifasi <Badge type="tip" text="oson" />
Wireshark nima uchun kerak? Bir jumlada yozing.

**Kutiladigan natija:** Bir jumlali javob.

### 2. Npcap <Badge type="tip" text="oson" />
O'rnatishda Npcap ga nega ruxsat beriladi?

**Kutiladigan natija:** Qisqa javob.

### 3. Ustunlar <Badge type="tip" text="oson" />
Paketlar ro'yxati ustunlarini sanang.

**Kutiladigan natija:** 7 ta ustun nomi.

### 4. Panellar <Badge type="tip" text="oson" />
Uchta panelning vazifasini yozing.

**Kutiladigan natija:** 3 qatorli javob.

### 5. GET izlash <Badge type="warning" text="o'rta" />
http://example.com ni oching va http filtri bilan GET toping.

**Kutiladigan natija:** GET paketi skrinshoti.

### 6. TLS ni topish <Badge type="warning" text="o'rta" />
https saytni oching va tls filtrini qo'llang.

**Kutiladigan natija:** Client Hello topilgan skrinshot.

### 7. Bayroqlar <Badge type="warning" text="o'rta" />
TCP paketida SYN va ACK bayroqlarini toping.

**Kutiladigan natija:** Bayroqlar ro'yxati.

### 8. Bashorat <Badge type="warning" text="o'rta" />
Sayt ochilganda 4 bosqichni tartibda yozing.

**Kutiladigan natija:** DNS, TCP, TLS, GET.

### 9. Protokol hisoboti <Badge type="danger" text="qiyin" />
TCP, UDP, DNS, ICMP dan 3 tadan paket tahlil qiling.

**Kutiladigan natija:** Jadval: Source, Destination, Protocol, Info.

### 10. Ochiq va shifrlangan <Badge type="danger" text="qiyin" />
HTTP va HTTPS ning pastki paneldagi farqini yozing.

**Kutiladigan natija:** Qisqa tahlil.

### 11. Xatoni toping <Badge type="danger" text="qiyin" />
"tls filtri bilan parolni topaman" degan fikr nima uchun xato?

**Kutiladigan natija:** Sabab bilan javob.

### 12. ARP kuzatuvi <Badge type="info" text="bonus" />
Tarmoqda ARP paketlari keskin ko'paysa, nimani shubha qilasiz?

**Kutiladigan natija:** Shubha va chora.

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Wireshark nima?
2. HTTP uchun qaysi filtr?
3. TLS Handshake nimani bildiradi?
4. Pastki panel nimani ko'rsatadi?
5. GET qaysi sathda?
6. Sayt ochilish bosqichlari qanday?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Wireshark o'rnating, har bir protokol (TCP, UDP, DNS, ICMP) bo'yicha kamida 3 paketni tahlil qilib, fayl ko'rinishida hisobot saqlang. Vaqt: 25-30 daqiqa.

</div>

