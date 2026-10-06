---
title: "IP-manzillash va qism tarmoqlar (subnets) (2-qism): CIDR, subnet maska hisoblash va tarmoq segmentatsiyasi"
description: "subnet mask, CIDR prefiks, tarmoq va broadcast manzil, hostlar soni, subnetlash, segmentatsiya"
dars: 2
hafta: 5
sinf: 10-sinf-cyber
---

# 14-dars. IP-manzillash va qism tarmoqlar (subnets) (2-qism): CIDR, subnet maska hisoblash va tarmoq segmentatsiyasi

**Manba:** O'quv qo'llanma, II bob, 2.3 «Qism tarmoq maskalari (Subnet Mask) va tarmoq segmentatsiyasi»; Uslubiy ko'rsatma, 2.3; rasmiy o'quv dasturi.

## Dars rejasi (80 daqiqa)

1. **Takrorlash (8 daqiqa):** 13-dars: IPv4, IPv6, sinflar
2. **Nazariy qism 1 (15 daqiqa):** Subnet mask va CIDR prefiks, tarmoq va host qismi
3. **Amaliyot 1 (15 daqiqa):** 192.168.10.0/24 ni 4 ta subnetga bo'lish
4. **Tanaffus (5 daqiqa).**
5. **Nazariy + amaliyot 2 (22 daqiqa):** Hostlar sonini hisoblash, `ipaddress` bilan tekshirish
6. **Xavfsizlik va xulosa (10 daqiqa):** Segmentatsiya va xavfsizlik, xulosa
7. **Tezkor nazorat (5 daqiqa).**

**Kutiladigan natija:** Subnet maskani CIDR prefiksiga o'tkazadi (255.255.255.0 = /24); Tarmoq, broadcast manzillar va hostlar sonini (2^h - 2) hisoblaydi; Berilgan tarmoqni talab qilingan sondagi teng subnetlarga bo'ladi; Segmentatsiya turlarini va uning xavfsizlikdagi foydasini tushuntiradi.

---

## Asosiy tushunchalar

- Subnet mask tarmoq (1 bitlar) va host (0 bitlar) qismini ajratadi.
- CIDR prefiks: 255.255.255.0 = /24, 255.255.0.0 = /16.
- Subnetda birinchi manzil tarmoq, oxirgisi broadcast; hostlar soni 2^h - 2.
- 192.168.10.0/24 ni 4 ga bo'lish: 4 ta /26, har birida 62 host.
- Segmentatsiya tarmoqni mustaqil bo'limlarga ajratadi.
- Usullar: fizik, mantiqiy (VLAN, IP subnetlash), xavfsizlik segmentatsiyasi.

---

## Dars mazmuni

### 1. Subnet mask va CIDR prefiks

Subnet mask 32 bitli qiymat: manzilning qaysi qismi **tarmoq**, qaysi qismi **host** ekanini ko'rsatadi. Maskadagi `1` bitlar tarmoq qismini, `0` bitlar host qismini bildiradi. Bu qiymat CIDR ko'rinishida (prefiks) qisqa yoziladi: `255.255.255.0` = `/24`, `255.255.0.0` = `/16`. Maska tarmoqni kichik bo'limlarga ajratadi, marshrutlashni soddalashtiradi va xavfsizlikni oshiradi.

```bash
255.255.255.0   = /24
255.255.0.0     = /16
255.255.255.192 = /26

192.168.10.5/24
  tarmoq qismi: 192.168.10
  host qismi:   5
```

Prefiks (masalan, /24) — maskadagi birlar soni. Qancha ko'p bit tarmoqqa ajratilsa, shuncha kichik subnet hosil bo'ladi.

### 2. Tarmoq, broadcast va hostlar soni

Subnetdagi birinchi manzil (host qismi to'liq 0) — **tarmoq manzili**, oxirgi (host qismi to'liq 1) — **broadcast**. Ular qurilmaga berilmaydi, shuning uchun hostlar soni `2^h - 2` (h — host bitlar soni). Misol: `192.168.10.0/24` ni 4 ta teng subnetga bo'lish uchun 2 qo'shimcha bit kerak (2^2 = 4), prefiks `/24` + 2 = `/26`. Har subnetda 2^6 - 2 = 62 host.

```bash
192.168.10.0/26    hostlar .1 - .62     broadcast .63
192.168.10.64/26   hostlar .65 - .126   broadcast .127
192.168.10.128/26  hostlar .129 - .190  broadcast .191
192.168.10.192/26  hostlar .193 - .254  broadcast .255
```

Subnetlar 64 qadam bilan boshlanadi (2^6 = 64): 0, 64, 128, 192.

### 3. Tarmoq segmentatsiyasi

Segmentatsiya — tarmoqni kichik, mustaqil bo'limlarga (segmentlarga) ajratish. Har segment alohida boshqariladi va o'zaro aloqasi cheklangan. Maqsad: xavfsizlikni oshirish, trafikni optimallashtirish, resurslarni ajratish, xatoni tez topish. Usullar: fizik, mantiqiy (VLAN va IP subnetlash), xavfsizlik segmentatsiyasi. Misol: o'quvchilar, o'qituvchilar va serverlar alohida subnetda bo'lsa, bitta zararlangan kompyuter hammasiga tarqala olmaydi.

```bash
192.168.10.0/26    kompyuter sinfi
192.168.10.64/26   o'qituvchilar
192.168.10.128/26  ma'muriyat
192.168.10.192/26  serverlar
```

Segmentlar orasidagi aloqa firewall qoidalari bilan boshqariladi (15-dars).

---

## Amaliy mashg'ulot

Har bir o'quvchi 192.168.10.0/24 ni 4 ta subnetga bo'ladi (jadval: tarmoq, hostlar, broadcast) va natijani `ipaddress` bilan tekshiradi. Keyin maktab uchun 4 segmentli reja tuzadi: sinf, o'qituvchilar, ma'muriyat, serverlar.

---

## Mustaqil topshiriqlar

### 1. Maska yozuvi · oson
255.255.255.0 ni prefiks ko'rinishida yozing.
**Yechim:** /24 (24 ta birlik bit).

### 2. Prefiks maskasi · oson
/16 ga mos maskani yozing.
**Yechim:** 255.255.0.0

### 3. Tarmoq va broadcast · oson
Subnetdagi birinchi va oxirgi manzil nima deb ataladi?
**Yechim:** Birinchisi tarmoq manzili, oxirgisi broadcast.

### 4. Segmentatsiya maqsadi · oson
Segmentatsiyaning 3 ta maqsadini yozing.
**Yechim:** Xavfsizlik, trafik optimallashtirish, resurslarni ajratish (yoki xatoni tez aniqlash).

### 5. Hostlar soni · o'rta
/27 va /28 da hostlar sonini hisoblang.
**Yechim:** /27: 2^5 - 2 = 30; /28: 2^4 - 2 = 14.

### 6. Subnetlar soni · o'rta
/24 tarmoqdan 8 ta subnet olish uchun nechta bit kerak va yangi prefiks nima?
**Yechim:** 3 bit (2^3 = 8); /27.

### 7. Maska hisobi · o'rta
/27 ning maskasini o'nlik ko'rinishda yozing.
**Yechim:** 3 bit = 128+64+32 = 224; 255.255.255.224.

### 8. Birinchi 3 subnet · o'rta
192.168.1.0/27 dan boshlab dastlabki 3 ta subnetni yozing.
**Yechim:** 192.168.1.0/27, 192.168.1.32/27, 192.168.1.64/27 (qadam 32).

### 9. Manzil joyi · qiyin
10.0.0.200/26 qaysi subnetda? Tarmoq va broadcast ni toping.
**Yechim:** Qadam 64: 192 <= 200 < 256; tarmoq 10.0.0.192, broadcast 10.0.0.255.

### 10. Maktab rejasi · qiyin
192.168.30.0/24 dan 4 segment (sinf 50 qurilma, o'qituvchilar 20, ma'muriyat 10, server 5) uchun mos prefikslarni tanlang.
**Yechim:** Teng /26 (62 host) hammasiga yetadi; tejash uchun /26, /27, /28, /29 ni ishlatish mumkin.

### 11. Xatoni toping · qiyin
Do'stingiz: «/24 da 256 ta host bo'ladi». Javob bering.
**Yechim:** Xato: 256 manzil bor, lekin tarmoq va broadcast ni ayirsak 254 host.

### 12. ipaddress skripti · bonus
Python da `ipaddress` bilan 10.0.0.0/24 ni /27 larga bo'lib, har subnet va hostlar sonini chiqaring.
**Yechim:** for s in ipaddress.ip_network('10.0.0.0/24').subnets(new_prefix=27): print(s, s.num_addresses-2) — 8 qator, har birida 30.

---

## Tezkor savol-javob

1. **Savol:** Subnet mask nima? **Javob:** Manzilning tarmoq va host qismini ajratuvchi 32 bitli qiymat.
2. **Savol:** /26 maskasi qanday? **Javob:** 255.255.255.192.
3. **Savol:** Nega hostlar soni 2^h - 2? **Javob:** Tarmoq va broadcast manzillar qurilmaga berilmaydi.
4. **Savol:** 4 subnet uchun nechta bit kerak? **Javob:** 2 bit (2^2 = 4).
5. **Savol:** Segmentatsiyaning maqsadi? **Javob:** Xavfsizlik, trafik optimallashtirish, resurslarni ajratish, xatoni tez topish.

---

## Mentor uchun eslatma

- Hisobni avval daftarda qo'lda bajartiring, keyin `ipaddress` bilan tekshiring.
- O'quvchilar ko'pincha broadcast va tarmoq manzilini host deb hisoblaydi: 2^h - 2 ning sababini alohida tushuntiring.
- `ipaddress` moduli qo'llanmada yo'q, tekshirish vositasi sifatida qo'shimcha berilgan.
- VLAN faqat tilga olinadi, batafsil keyingi mavzularda.
