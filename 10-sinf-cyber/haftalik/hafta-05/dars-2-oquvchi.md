---
title: "IP-manzillash va qism tarmoqlar (subnets) (2-qism): CIDR, subnet maska hisoblash va tarmoq segmentatsiyasi"
description: "subnet mask, CIDR prefiks, tarmoq va broadcast manzil, hostlar soni, subnetlash, segmentatsiya"
dars: 2
hafta: 5
sinf: 10-sinf-cyber
---

# 14-dars. IP-manzillash va qism tarmoqlar (subnets) (2-qism): CIDR, subnet maska hisoblash va tarmoq segmentatsiyasi

> Bitta katta tarmoqda hamma bir-birini ko'radi. Bitta zararlangan kompyuter hammaga zarar yetkazishi mumkin. Subnetlar bu muammoni hal qiladi.

## Dars xulosasi

- Subnet mask tarmoq (1 bitlar) va host (0 bitlar) qismini ajratadi.
- CIDR prefiks: 255.255.255.0 = /24, 255.255.0.0 = /16.
- Subnetda birinchi manzil tarmoq, oxirgisi broadcast; hostlar soni 2^h - 2.
- 192.168.10.0/24 ni 4 ga bo'lish: 4 ta /26, har birida 62 host.
- Segmentatsiya tarmoqni mustaqil bo'limlarga ajratadi.
- Usullar: fizik, mantiqiy (VLAN, IP subnetlash), xavfsizlik segmentatsiyasi.

## Qo'shimcha ma'lumot

### Bitlar qarz olish
Prefiksga n bit qo'shsangiz 2^n ta subnet hosil bo'ladi, har birida host bitlar n taga kamayadi.

### Qadam usuli
Subnetlar orasidagi qadam = 256 - maskaning oxirgi oktet qiymati. /26 uchun 256 - 192 = 64.

### Odatiy xatolar
Hostlar sonidan 2 ni ayirishni unutish; subnet chegarasiga tushmaydigan manzilni tarmoq manzili deb yozish.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Subnet mask | Tarmoq va host qismini ajratuvchi qiymat |
| CIDR | Prefiks bilan manzil yozuvi (/24) |
| Prefiks | Tarmoq qismi bitlari soni |
| Tarmoq manzili | Subnetdagi birinchi manzil |
| Broadcast | Subnetdagi oxirgi manzil |
| Host | Tarmoqdagi qurilma |
| Subnet | Katta tarmoqning qismi |
| Segmentatsiya | Tarmoqni bo'limlarga ajratish |
| VLAN | Mantiqiy virtual lokal tarmoq |

## Bilasizmi?

- /30 subnet faqat 2 host beradi: ikki router orasidagi ulanish uchun qulay.
- 192.168.10.0/24 ni 8 ga bo'lsa, har biri 30 host sig'diradi.
- Segmentatsiya xatolarni tez topishga ham yordam beradi.

## Topshiriqlar

### 1. Maska yozuvi · oson

255.255.255.0 ni prefiks ko'rinishida yozing.

**Kutiladigan natija:** /24

### 2. Prefiks maskasi · oson

/16 ga mos maskani yozing.

**Kutiladigan natija:** 255.255.0.0

### 3. Tarmoq va broadcast · oson

Subnetdagi birinchi va oxirgi manzil nima deb ataladi?

**Kutiladigan natija:** Ikki atama.

### 4. Segmentatsiya maqsadi · oson

Segmentatsiyaning 3 ta maqsadini yozing.

**Kutiladigan natija:** 3 band.

### 5. Hostlar soni · o'rta

/27 va /28 da hostlar sonini hisoblang.

**Kutiladigan natija:** Ikki son.

### 6. Subnetlar soni · o'rta

/24 tarmoqdan 8 ta subnet olish uchun nechta bit kerak va yangi prefiks nima?

**Kutiladigan natija:** 3 bit va prefiks.

### 7. Maska hisobi · o'rta

/27 ning maskasini o'nlik ko'rinishda yozing.

**Kutiladigan natija:** 255.255.255.224

### 8. Birinchi 3 subnet · o'rta

192.168.1.0/27 dan boshlab dastlabki 3 ta subnetni yozing.

**Kutiladigan natija:** 3 manzil.

### 9. Manzil joyi · qiyin

10.0.0.200/26 qaysi subnetda? Tarmoq va broadcast ni toping.

**Kutiladigan natija:** Tarmoq va broadcast.

### 10. Maktab rejasi · qiyin

192.168.30.0/24 dan 4 segment (sinf 50 qurilma, o'qituvchilar 20, ma'muriyat 10, server 5) uchun mos prefikslarni tanlang.

**Kutiladigan natija:** Moslash va izoh.

### 11. Xatoni toping · qiyin

Do'stingiz: «/24 da 256 ta host bo'ladi». Javob bering.

**Kutiladigan natija:** Rad etish va to'g'ri son.

### 12. ipaddress skripti · bonus

Python da `ipaddress` bilan 10.0.0.0/24 ni /27 larga bo'lib, har subnet va hostlar sonini chiqaring.

**Kutiladigan natija:** 8 qator chiqish.

## O'zingizni tekshiring

1. Subnet mask nima?
2. /24 qaysi maskaga teng?
3. Hostlar soni qanday hisoblanadi?
4. Tarmoq va broadcast farqi?
5. 4 subnet uchun nechta bit kerak?
6. /26 da nechta host?
7. Segmentatsiya nima uchun kerak?

## Uyga vazifa

Subnetlash, prefikslar jadvali va maktab segmentatsiyasi rejasini bajaring (25 daqiqa). To'liq shart: `uyga-vazifa.md`.
