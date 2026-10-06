---
title: "IP-manzillash va qism tarmoqlar (subnets) (1-qism): IPv4 va IPv6 arxitekturasi, sinflar"
description: "IPv4, IPv6, sarlavhalar, manzil turlari, A-E sinflari, IANA va RIR, shaxsiy diapazonlar"
dars: 1
hafta: 5
sinf: 10-sinf-cyber
---

# 13-dars. IP-manzillash va qism tarmoqlar (subnets) (1-qism): IPv4 va IPv6 arxitekturasi, sinflar

**Manba:** O'quv qo'llanma, II bob, 2.3 «IP-manzillash va qismtarmoqlar (subnets)»; Uslubiy ko'rsatma, 2.3 (statik va dinamik IP sozlash); rasmiy o'quv dasturi.

## Dars rejasi (80 daqiqa)

1. **Takrorlash (8 daqiqa):** 4-hafta: ping, traceroute va TTL
2. **Nazariy qism 1 (15 daqiqa):** IPv4 va IPv6: format, hajm, manzil turlari
3. **Amaliyot 1 (15 daqiqa):** Windows da `ipconfig` bilan o'z IP, maska va shlyuzni topish
4. **Tanaffus (5 daqiqa).**
5. **Nazariy + amaliyot 2 (22 daqiqa):** Sarlavhalar, A-E sinflari, tarqatilish zanjiri
6. **Xavfsizlik va xulosa (10 daqiqa):** Xavfsizlik: IP protokolining zaifliklari (spoofing), xulosa
7. **Tezkor nazorat (5 daqiqa).**

**Kutiladigan natija:** IPv4 (32 bit) va IPv6 (128 bit) formatini va hajmini farqlaydi; IPv4 va IPv6 sarlavhasining asosiy maydonlarini sanaydi; IP manzilning sinfini (A, B, C, D, E) birinchi oktet bo'yicha aniqlaydi; IP manzillar tarqatilish zanjirini (IANA, RIR, LIR/ISP) va shaxsiy diapazonlarni aytadi.

---

## Asosiy tushunchalar

- IPv4: 32 bit, to'rt o'nlik son; IPv6: 128 bit, sakkiz o'n oltilik blok.
- IPv4 manzillar 2011-yilda tugagan; vaqtincha yechim NAT, uzoq muddatli IPv6.
- IPv4 sarlavhasi 20-60 bayt (TTL bor), IPv6 asosiy sarlavhasi 40 bayt (Hop limit).
- Manzil turlari: IPv4 unicast, broadcast, multicast; IPv6 unicast, multicast, anycast.
- IP sinflari A-E; hozir CIDR, lekin sinflar subnetlashni tushunish uchun kerak.
- Tarqatish: IANA, RIR, LIR/ISP, tashkilot, foydalanuvchi; shaxsiy diapazonlar 10/8, 172.16/12, 192.168/16.

---

## Dars mazmuni

### 1. IPv4 va IPv6 tarmoq protokoli

IP protokoli har bir qurilmaga noyob manzil beradi. **IPv4** 32 bitli manzil ishlatadi: to'rtta o'nlik son (0-255), nuqta bilan ajratiladi, masalan `197.0.0.1`. Manzillar soni 2^32 (4 294 967 296) ta, ular 2011-yilda tugagan. **IPv6** 128 bitli: sakkizta o'n oltilik blok, ikki nuqta bilan ajratiladi, masalan `2600:1400:d:5a3::3bd4`. Ketma-ket nol bloklarni `::` bilan qisqartirish mumkin. Vaqtincha yechim sifatida NAT ishlatiladi.

```bash
# IPv4: 4 ta o'nlik son (0-255)
197.0.0.1

# IPv6: 8 ta o'n oltilik blok
2600:1400:000d:05a3:0000:0000:0000:3bd4

# IPv6 qisqartirilgan yozuvi
2600:1400:d:5a3::3bd4
```

`::` manzilda faqat bir marta ishlatiladi: ketma-ket nol bloklarni almashtiradi.

### 2. IPv4 va IPv6 sarlavhalari

IPv4 sarlavhasi 20-60 bayt: Version, IHL, ToS, Total length, Identification, Flags, Fragment offset, **TTL**, Protocol, Header checksum, Source va Destination address, Options. IPv6 asosiy sarlavhasi atigi 40 bayt: Version, Traffic class, Flow label, Payload length, Next header, **Hop limit** (IPv4 dagi TTL ga mos), Source va Destination address. Qo'shimcha funksiyalar Extension headerlar orqali ulanadi. Ikkalasida paketning maksimal uzunligi 65 535 bayt.

```bash
IPv4 sarlavha (20-60 bayt):
  Version, IHL, ToS, Total length
  Identification, Flags, Fragment offset
  TTL, Protocol, Header checksum
  Source address, Destination address, Options

IPv6 sarlavha (40 bayt):
  Version, Traffic class, Flow label
  Payload length, Next header, Hop limit
  Source address, Destination address
```

TTL (IPv4) va Hop limit (IPv6) bir xil vazifani bajaradi: paket cheksiz aylanmasligi uchun router sonini cheklaydi.

### 3. IP manzil sinflari va tarqatilishi

IPv4 manzillar A, B, C, D, E sinflariga bo'lingan: A (1-126), B (128-191), C (192-223) birinchi oktet bo'yicha; D (224-239) multicast uchun, E (240-255) tajriba uchun. Hozir sinflar o'rniga CIDR ishlatiladi, lekin sinflar subnetlashni tushunish va imtihonlar uchun muhim. Manzillar 5 bosqichda tarqatiladi: IANA, RIR, LIR/ISP, tashkilotlar, foydalanuvchilar. O'zbekiston RIPE NCC hududida. Ichki tarmoqlarda shaxsiy diapazonlar: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`.

```bash
Sinf  Birinchi oktet  Vazifa
A     1 - 126         juda yirik tarmoqlar
B     128 - 191       o'rta tarmoqlar
C     192 - 223       kichik tarmoqlar
D     224 - 239       multicast
E     240 - 255       tajriba

Shaxsiy (private) diapazonlar:
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

Shaxsiy manzillar internetga to'g'ridan-to'g'ri chiqmaydi: NAT orqali global tarmoqqa ulanadi. A-E chegaralari standart bo'yicha berilgan, qo'llanmada ular rasmda ko'rsatilgan.

---

## Amaliy mashg'ulot

Har bir o'quvchi `ipconfig` (Linux: `ip a`) bilan o'z IPv4 manzili, subnet maskasi va shlyuzini topadi, sinfini aniqlaydi, shaxsiy diapazonga tegishliligini tekshiradi. Keyin ikkita qo'shni kompyuter bir-biriga `ping` yuboradi (uslubiy ko'rsatmada statik IP misoli: 192.168.50.10).

---

## Mustaqil topshiriqlar

### 1. IPv4 formati · oson
IPv4 manzil necha bit va qanday yoziladi?
**Yechim:** 32 bit; to'rtta 0-255 oralig'idagi son nuqta bilan ajratiladi, masalan 197.0.0.1.

### 2. IPv6 formati · oson
IPv6 manzil necha bit va qanday yoziladi?
**Yechim:** 128 bit; sakkizta o'n oltilik blok ikki nuqta bilan, masalan 2600:1400:d:5a3::3bd4.

### 3. Manzil turlari · oson
IPv4 va IPv6 manzil turlarini sanang.
**Yechim:** IPv4: unicast, broadcast, multicast. IPv6: unicast, multicast, anycast.

### 4. Zanjir · oson
IP manzillar tarqatilish 5 bosqichini yozing.
**Yechim:** IANA, RIR, LIR/ISP, tashkilotlar, foydalanuvchilar.

### 5. Sinflarni aniqlash · o'rta
Sinfini toping: 12.1.1.1, 150.5.5.5, 195.3.3.3, 225.0.0.1.
**Yechim:** A, B, C, D (multicast).

### 6. Shaxsiy yoki umumiy · o'rta
Qaysilari shaxsiy: 192.168.5.4, 8.8.8.8, 172.16.3.3, 10.20.30.40?
**Yechim:** 192.168.5.4, 172.16.3.3 va 10.20.30.40 shaxsiy; 8.8.8.8 umumiy.

### 7. IPv6 qisqartirish · o'rta
`fe80:0000:0000:0000:0202:b3ff:fe1e:8329` ni qisqartiring.
**Yechim:** fe80::202:b3ff:fe1e:8329

### 8. Sarlavha maydoni · o'rta
IPv4 da TTL, IPv6 da qaysi maydon xuddi shu vazifani bajaradi va nima uchun kerak?
**Yechim:** Hop limit; paket tarmoqda cheksiz aylanib yurmasligi uchun.

### 9. Statik yoki DHCP · qiyin
Maktab web-serveri, ofis noutbuki va videokamera uchun statik yoki dinamik IP ni asoslang.
**Yechim:** Web-server va kamera statik (doimiy manzil kerak), noutbuk DHCP (qulay, to'qnashuv yo'q).

### 10. Xatoni toping · qiyin
Do'stingiz: «192.168.1.5 manzilni internetdagi har kim ko'ra oladi». Javob bering.
**Yechim:** Xato: bu shaxsiy manzil, internetga to'g'ridan-to'g'ri chiqmaydi; NAT orqali router umumiy manzili ko'rinadi.

### 11. IP xavfsizligi · qiyin
IP protokoli nega yuboruvchini tasdiqlamaydi va bu qanday hujumga olib keladi?
**Yechim:** IP protokoli funksionallik uchun yaratilgan, autentifikatsiya yo'q; natija: IP spoofing, DDoS va MITM xavfi.

### 12. Mini hisobot · bonus
O'z uyingiz tarmog'ining IP, maska, shlyuz, sinf va IP turi (statik/dinamik) bilan qisqa hisobot yozing.
**Yechim:** Hisobotda ipconfig natijasi, sinf, shaxsiy diapazon va statik yoki dinamik ekanligi bo'lishi kerak.

---

## Tezkor savol-javob

1. **Savol:** IPv4 va IPv6 farqi nima? **Javob:** IPv4 32 bitli (4 ta o'nlik son), IPv6 128 bitli (8 ta o'n oltilik blok).
2. **Savol:** IPv4 manzillar qachon tugadi? **Javob:** 2011-yilda; vaqtincha yechim NAT.
3. **Savol:** Hop limit nima? **Javob:** IPv6 dagi TTL: paket o'tadigan router sonini cheklaydi.
4. **Savol:** C sinf birinchi oktet diapazoni? **Javob:** 192-223.
5. **Savol:** O'zbekiston qaysi RIR hududida? **Javob:** RIPE NCC.

---

## Mentor uchun eslatma

- Sinf diapazonlari (A 1-126, B 128-191, C 192-223) qo'llanmada rasm ko'rinishida; mentor standart qiymatlarni aytadi. 127 loopback uchun ajratilganini eslatib o'ting.
- `ipconfig` natijasi har kompyuterda boshqacha: o'quvchi o'z qiymatini yozadi.
- Statik IP sozlashni faqat laboratoriya kompyuterida bajaring, ulanish uzilmasligi uchun avval eski sozlamani yozib oling.
- IP spoofing: IP protokoli yuboruvchini tasdiqlamaydi, shu sababli qo'shimcha himoya (firewall, VPN) kerak.
