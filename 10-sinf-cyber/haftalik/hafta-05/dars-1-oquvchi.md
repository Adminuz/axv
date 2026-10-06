---
title: "IP-manzillash va qism tarmoqlar (subnets) (1-qism): IPv4 va IPv6 arxitekturasi, sinflar"
description: "IPv4, IPv6, sarlavhalar, manzil turlari, A-E sinflari, IANA va RIR, shaxsiy diapazonlar"
dars: 1
hafta: 5
sinf: 10-sinf-cyber
---

# 13-dars. IP-manzillash va qism tarmoqlar (subnets) (1-qism): IPv4 va IPv6 arxitekturasi, sinflar

> Telefoningiz, noutbukingiz, printer: har birining tarmoqda o'z «uy manzili» bor. Bugun bu manzillar qanday tuzilishini o'rganamiz.

## Dars xulosasi

- IPv4: 32 bit, to'rt o'nlik son; IPv6: 128 bit, sakkiz o'n oltilik blok.
- IPv4 manzillar 2011-yilda tugagan; vaqtincha yechim NAT, uzoq muddatli IPv6.
- IPv4 sarlavhasi 20-60 bayt (TTL bor), IPv6 asosiy sarlavhasi 40 bayt (Hop limit).
- Manzil turlari: IPv4 unicast, broadcast, multicast; IPv6 unicast, multicast, anycast.
- IP sinflari A-E; hozir CIDR, lekin sinflar subnetlashni tushunish uchun kerak.
- Tarqatish: IANA, RIR, LIR/ISP, tashkilot, foydalanuvchi; shaxsiy diapazonlar 10/8, 172.16/12, 192.168/16.

## Qo'shimcha ma'lumot

### Nega IPv6 sarlavhasi soddaroq?
Asosiy sarlavha 40 bayt, ixtiyoriy funksiyalar Extension headerlarga o'tkazilgan. Router kamroq ish bajaradi.

### Public va private IP
Public IP internetda ko'rinadi. Private IP lokal router tarqatadi va NAT orqali internetga chiqadi.

### Odatiy xatolar
Subnet maskani IP manzil deb o'ylash; `::` ni ikki marta ishlatish; shaxsiy IP ni internetda ko'rinadi deb hisoblash.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| IPv4 | 32 bitli IP manzil |
| IPv6 | 128 bitli IP manzil |
| NAT | Ichki manzilni tashqi manzilga almashtirish |
| Unicast | Birdan bitta |
| Multicast | Birdan guruhga |
| Anycast | Eng yaqin qabul qiluvchiga (IPv6) |
| IANA | IP manzillarni global boshqaruvchi tashkilot |
| RIR | Mintaqaviy internet registri |
| ISP | Internet provayder |
| Private IP | Ichki tarmoq manzili |

## Bilasizmi?

- IPv4 da manzil maydoni 2^32, IPv6 da 2^128.
- IPv6 1995-yilda aniqlangan, lekin standart sifatida 2017-yilda qabul qilingan.
- RIPE NCC Yevropa, Yaqin Sharq va Markaziy Osiyoni boshqaradi.

## Topshiriqlar

### 1. IPv4 formati · oson

IPv4 manzil necha bit va qanday yoziladi?

**Kutiladigan natija:** 32 bit, to'rt o'nlik son nuqta bilan.

### 2. IPv6 formati · oson

IPv6 manzil necha bit va qanday yoziladi?

**Kutiladigan natija:** 128 bit, sakkiz blok.

### 3. Manzil turlari · oson

IPv4 va IPv6 manzil turlarini sanang.

**Kutiladigan natija:** IPv4: 3 tur, IPv6: 3 tur.

### 4. Zanjir · oson

IP manzillar tarqatilish 5 bosqichini yozing.

**Kutiladigan natija:** 5 bosqich tartibi.

### 5. Sinflarni aniqlash · o'rta

Sinfini toping: 12.1.1.1, 150.5.5.5, 195.3.3.3, 225.0.0.1.

**Kutiladigan natija:** 4 ta sinf.

### 6. Shaxsiy yoki umumiy · o'rta

Qaysilari shaxsiy: 192.168.5.4, 8.8.8.8, 172.16.3.3, 10.20.30.40?

**Kutiladigan natija:** Shaxsiy manzillar ro'yxati.

### 7. IPv6 qisqartirish · o'rta

`fe80:0000:0000:0000:0202:b3ff:fe1e:8329` ni qisqartiring.

**Kutiladigan natija:** Qisqa yozuv.

### 8. Sarlavha maydoni · o'rta

IPv4 da TTL, IPv6 da qaysi maydon xuddi shu vazifani bajaradi va nima uchun kerak?

**Kutiladigan natija:** Hop limit va sababi.

### 9. Statik yoki DHCP · qiyin

Maktab web-serveri, ofis noutbuki va videokamera uchun statik yoki dinamik IP ni asoslang.

**Kutiladigan natija:** 3 qarorning sababi bilan.

### 10. Xatoni toping · qiyin

Do'stingiz: «192.168.1.5 manzilni internetdagi har kim ko'ra oladi». Javob bering.

**Kutiladigan natija:** Sabab bilan rad etish.

### 11. IP xavfsizligi · qiyin

IP protokoli nega yuboruvchini tasdiqlamaydi va bu qanday hujumga olib keladi?

**Kutiladigan natija:** Sabab va hujum nomi.

### 12. Mini hisobot · bonus

O'z uyingiz tarmog'ining IP, maska, shlyuz, sinf va IP turi (statik/dinamik) bilan qisqa hisobot yozing.

**Kutiladigan natija:** 1 sahifalik hisobot.

## O'zingizni tekshiring

1. IPv4 va IPv6 farqi nima?
2. IPv4 manzillari qachon tugadi?
3. IPv4 sarlavhasining o'lchami qancha?
4. IPv6 da TTL ning o'rnini nima bosadi?
5. C sinf diapazoni qanday?
6. IANA nima qiladi?
7. Shaxsiy IP diapazonlarini ayting.

## Uyga vazifa

`ipconfig` natijasi, IPv4/IPv6 jadvali va 5 manzil sinfini aniqlash vazifalarini bajaring (25 daqiqa). To'liq shart: `uyga-vazifa.md`.
