---
title: "Tarmoq qurilmalari va xavfsizlik muammolari (3-qism): ping va traceroute buyruqlari bilan marshrutlarni tahlil qilish"
description: "ping, RTT, packet loss, TTL, tracert, hop va flaglar"
dars: 3
hafta: 4
sinf: 10-sinf-cyber
---

# 12-dars. Tarmoq qurilmalari va xavfsizlik muammolari (3-qism): ping va traceroute buyruqlari bilan marshrutlarni tahlil qilish

> Siz yuborgan paket sayt serveriga yetguncha nechta routerdan o'tadi? Ikki kichik buyruq bu savolga javob beradi.

## Dars xulosasi

- ping qurilma faolligini, javob vaqtini va paket yo'qolishini ko'rsatadi.
- RTT: paket borib-kelish vaqti.
- TTL dan hop sonini taxminan hisoblash mumkin (128 yoki 64 dan ayirib).
- tracert (Windows) va traceroute (Linux/Mac) paket yo'lini ko'rsatadi.
- Hop: yo'ldagi router.
- * * * ko'pincha ICMP bloklanganini bildiradi.
- tracert flaglari: -d, -h, -w, -4, -6.
- IPv6 uchun ping6.

## Qo'shimcha ma'lumot

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

## Atamalar lug'ati

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

## Bilasizmi?

- Qo'llanmada O'zbekistondan Google ga 30-60 ms kutilishi yozilgan.
- Traceroute har hop uchun odatda 3 marta vaqt o'lchaydi.
- Ko'p mahalliy saytlar ping ga javob bermaydi.

## Topshiriqlar

### 1. Ping beradi · oson
ping qanday 3 ma'lumot beradi?

**Kutiladigan natija:** 3 band.

### 2. RTT · oson
RTT nima?

**Kutiladigan natija:** To'liq nom va ma'no.

### 3. Buyruqlar · oson
Windows va Linux uchun marshrut buyruqlari?

**Kutiladigan natija:** 2 buyruq.

### 4. Hop · oson
Hop nima?

**Kutiladigan natija:** Bir jumla.

### 5. TTL hisobi · o'rta
TTL=110 (Windows) bo'lsa, nechta hop?

**Kutiladigan natija:** Hisob va javob.

### 6. Natijani izohlash · o'rta
200 ms, 0% yo'qotish nimani bildiradi?

**Kutiladigan natija:** Izoh.

### 7. Yulduzchalar · o'rta
tracert da * * * chiqdi. Server o'chiqmi?

**Kutiladigan natija:** Sabab.

### 8. Flag tanlash · o'rta
DNS siz va 1 soniya kutish bilan tracert buyrug'ini yozing.

**Kutiladigan natija:** tracert -d -w 1000 ... shaklidagi buyruq.

### 9. To'rt sayt jadvali · qiyin
4 saytga ping va tracert yuborib, jadval tuzing.

**Kutiladigan natija:** 4 qator: ms, yo'qotish, TTL, hop.

### 10. Yo'lni tahlil qilish · qiyin
Marshrutingizni uy routeridan serverigacha rollar bilan yozing.

**Kutiladigan natija:** Hop ro'yxati.

### 11. Xatoni toping · qiyin
"25% yo'qotish = hujum" degan fikrni baholang.

**Kutiladigan natija:** Sabab bilan rad etish.

### 12. Wireshark + ping · bonus
Wireshark ishlatib, ping ning ICMP paketlarini toping.

**Kutiladigan natija:** Echo so'rovi va javobi.

## O'zingizni tekshiring

1. ping nima o'lchaydi?
2. TTL dan hop soni qanday topiladi?
3. * * * nimani bildiradi?
4. tracert -d nima qiladi?
5. IPv6 uchun ping qanday?
6. Linux da marshrut buyrug'i?

## Uyga vazifa

4 ta turli saytga ping va tracert yuboring (flaglardan foydalaning), natijalarni jadvalga yozing. Vaqt: 25 daqiqa.
