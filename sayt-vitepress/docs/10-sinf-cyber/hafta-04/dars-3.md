---
title: "12-dars. Tarmoq qurilmalari va xavfsizlik muammolari (3-qism): ping va traceroute buyruqlari bilan marshrutlarni tahlil qilish"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (Cyber)", "link": "/10-sinf-cyber/"}, "week": {"n": 4, "link": "/10-sinf-cyber/hafta-04/"}, "g": 12, "title": "Tarmoq qurilmalari va xavfsizlik muammolari (3-qism): ping va traceroute buyruqlari bilan marshrutlarni tahlil qilish", "lead": "Siz yuborgan paket sayt serveriga yetguncha nechta routerdan o'tadi? Ikki kichik buyruq bu savolga javob beradi.", "slide": "/slaydlar/10-sinf-cyber/hafta-04/dars-3.html", "test": "/slaydlar/10-sinf-cyber/hafta-04/dars-3-test.html", "tabs": [{"g": 10, "link": "/10-sinf-cyber/hafta-04/dars-1", "current": false}, {"g": 11, "link": "/10-sinf-cyber/hafta-04/dars-2", "current": false}, {"g": 12, "link": "/10-sinf-cyber/hafta-04/dars-3", "current": true}], "prev": {"g": 11, "title": "Tarmoq qurilmalari va xavfsizlik muammolari (2-qism): Wireshark yordamida tarmoq trafigini tahlil qilish", "link": "/10-sinf-cyber/hafta-04/dars-2"}, "next": null}
---

---
title: "Tarmoq qurilmalari va xavfsizlik muammolari (3-qism): ping va traceroute buyruqlari bilan marshrutlarni tahlil qilish"
description: "ping, RTT, packet loss, TTL, tracert, hop va flaglar"
dars: 3
hafta: 4
sinf: 10-sinf-cyber
---

<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- ping qurilma faolligini, javob vaqtini va paket yo'qolishini ko'rsatadi.
- RTT: paket borib-kelish vaqti.
- TTL dan hop sonini taxminan hisoblash mumkin (128 yoki 64 dan ayirib).
- tracert (Windows) va traceroute (Linux/Mac) paket yo'lini ko'rsatadi.
- Hop: yo'ldagi router.
- * * * ko'pincha ICMP bloklanganini bildiradi.
- tracert flaglari: -d, -h, -w, -4, -6.
- IPv6 uchun ping6.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### RTT: to'p otish
Devorga to'p otib, qaytib kelguncha o'tgan vaqtni o'lchang: bu RTT. (O'xshatish.)

### TTL qanday ishlaydi
Qo'llanma bo'yicha Windows server TTL ni 128, Linux esa 64 qilib jo'natadi. Natijada TTL=105 bo'lsa, 128-105=23 hop.

### Qo'llanmadagi ikki misol
- google.com: 163 ms, 0% yo'qotish, TTL=105, 13 hop.
- daryo.uz: 14 ms, 25% yo'qotish, TTL=110, 5-18 hoplarda `* * *`.

### Nega * * * xavfli emas?
Ko'p provayderlar traceroute va ping so'rovlarini bloklaydi. Oxirgi hopda server javob bersa, u faol.

### Odatiy xatolar
- Linux da `tracert` yozish.
- Paket yo'qolishini hujum deb o'ylash.
- Barcha natijalarni bir martalik o'lchovga asoslab xulosa qilish.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| ping | Echo paketini yuboruvchi buyruq |
| RTT | Round-trip time, borib-kelish vaqti |
| Latency | Javob vaqti, kechikish |
| Packet loss | Paket yo'qolishi |
| TTL | Paket umri, hop hisobiga yordam beradi |
| Hop | Yo'ldagi router |
| tracert | Windows marshrut kuzatuvi |
| traceroute | Linux/Mac marshrut kuzatuvi |
| ICMP | Ping ishlatadigan protokol |
| ping6 | IPv6 uchun ping |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Qo'llanmada O'zbekistondan Google ga 30-60 ms kutilishi yozilgan.
- Traceroute har hop uchun odatda 3 marta vaqt o'lchaydi.
- Ko'p mahalliy saytlar ping ga javob bermaydi.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Ping beradi <Badge type="tip" text="oson" />
ping qanday 3 ma'lumot beradi?

**Kutiladigan natija:** 3 band.

### 2. RTT <Badge type="tip" text="oson" />
RTT nima?

**Kutiladigan natija:** To'liq nom va ma'no.

### 3. Buyruqlar <Badge type="tip" text="oson" />
Windows va Linux uchun marshrut buyruqlari?

**Kutiladigan natija:** 2 buyruq.

### 4. Hop <Badge type="tip" text="oson" />
Hop nima?

**Kutiladigan natija:** Bir jumla.

### 5. TTL hisobi <Badge type="warning" text="o'rta" />
TTL=110 (Windows) bo'lsa, nechta hop?

**Kutiladigan natija:** Hisob va javob.

### 6. Natijani izohlash <Badge type="warning" text="o'rta" />
200 ms, 0% yo'qotish nimani bildiradi?

**Kutiladigan natija:** Izoh.

### 7. Yulduzchalar <Badge type="warning" text="o'rta" />
tracert da * * * chiqdi. Server o'chiqmi?

**Kutiladigan natija:** Sabab.

### 8. Flag tanlash <Badge type="warning" text="o'rta" />
DNS siz va 1 soniya kutish bilan tracert buyrug'ini yozing.

**Kutiladigan natija:** tracert -d -w 1000 ... shaklidagi buyruq.

### 9. To'rt sayt jadvali <Badge type="danger" text="qiyin" />
4 saytga ping va tracert yuborib, jadval tuzing.

**Kutiladigan natija:** 4 qator: ms, yo'qotish, TTL, hop.

### 10. Yo'lni tahlil qilish <Badge type="danger" text="qiyin" />
Marshrutingizni uy routeridan serverigacha rollar bilan yozing.

**Kutiladigan natija:** Hop ro'yxati.

### 11. Xatoni toping <Badge type="danger" text="qiyin" />
"25% yo'qotish = hujum" degan fikrni baholang.

**Kutiladigan natija:** Sabab bilan rad etish.

### 12. Wireshark + ping <Badge type="info" text="bonus" />
Wireshark ishlatib, ping ning ICMP paketlarini toping.

**Kutiladigan natija:** Echo so'rovi va javobi.

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. ping nima o'lchaydi?
2. TTL dan hop soni qanday topiladi?
3. * * * nimani bildiradi?
4. tracert -d nima qiladi?
5. IPv6 uchun ping qanday?
6. Linux da marshrut buyrug'i?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

4 ta turli saytga ping va tracert yuboring (flaglardan foydalaning), natijalarni jadvalga yozing. Vaqt: 25 daqiqa.

</div>

