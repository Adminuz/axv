---
title: "Tarmoq qurilmalari va xavfsizlik muammolari (3-qism): ping va traceroute buyruqlari bilan marshrutlarni tahlil qilish"
description: "ping, RTT, packet loss, TTL, tracert/traceroute, hop, * * * va tracert flaglari"
dars: 3
hafta: 4
sinf: 10-sinf-cyber
---

# 12-dars. Tarmoq qurilmalari va xavfsizlik muammolari (3-qism): ping va traceroute buyruqlari bilan marshrutlarni tahlil qilish

**Manba:** Uslubiy ko'rsatma, II bob, 2.2 «Ping va traceroute buyruqlari bilan tarmoqni tahlil qilish»; O'quv qo'llanma (firewall: ICMP cheklovlari).

## Dars rejasi (80 daqiqa)

1. **Takrorlash (8 daqiqa):** Wireshark: 3 panel, `http`, `tls`. Router vazifasi.
2. **Nazariy qism 1 (15 daqiqa):** ping, RTT, latency, packet loss; natijani o'qish; TTL.
3. **Amaliyot 1 (15 daqiqa):** CMD/Terminal ochish, `ping google.com`, `ping daryo.uz`.
4. **Tanaffus (5 daqiqa).**
5. **Nazariy + amaliyot 2 (22 daqiqa):** traceroute/tracert, hop, `* * *`, flaglar (`-d`, `-h`, `-w`, `-4`, `-6`).
6. **Xavfsizlik va xulosa (10 daqiqa):** ICMP cheklovlari, hisobot.
7. **Tezkor nazorat (5 daqiqa).**

**Kutiladigan natija:** o'quvchi `ping` va `tracert/traceroute` ni bajaradi; RTT, packet loss, TTL va hopni izohlaydi; `* * *` bloklangan ICMP belgisi ekanini biladi; flaglardan foydalanadi.

---

## Asosiy tushunchalar (uslubiy ko'rsatma bo'yicha)

- Internet millionlab marshrutizatorlardan (router) iborat ulkan tarmoq.
- **ping**: tarmoqdagi boshqa qurilmaga kichik «echo» paketini yuboradi va javob vaqtini (**RTT**, Round-trip time) o'lchaydi. Qurilma faolligini, javob vaqtini (**latency**) va paket yo'qolishini (**packet loss**) ko'rsatadi.
- **traceroute / tracert**: paketlar internet bo'ylab qanday yo'l (**hop**) bilan borishini ko'rsatadi. Har bir hop router bo'lib, paketni keyingi bosqichga yuboradi. Har hop uchun javob vaqti (odatda 3 marta o'lchanadi) va hop IP/host nomi ko'rsatiladi. Kechikish va muammo qayerdaligini aniqlashda yordam beradi.
- Windows: `tracert`; Linux/Mac: `traceroute`. IPv6 uchun `ping6`.

---

## Dars mazmuni

### 1. Tayyorgarlik

Windows: Win+R, `cmd`, Enter. Linux/Mac: Terminal.

### 2. Ping

```bash
ping google.com
ping daryo.uz
```

**google.com natijasi (qo'llanmadagi misol):**

| Ko'rsatkich | Qiymat | Xulosa |
|---|---|---|
| O'rtacha vaqt | 163 ms | Katta: O'zbekistondan Google ga 30-60 ms kutiladi. Paketlar Yevropa yoki Rossiya orqali aylanib kelayotganini taxmin qilish mumkin |
| Yo'qotish | 0% | Barcha xabarlar yetib bordi; aloqa sekin bo'lsa-da barqaror |
| TTL | 105 | Paket 23 ta router (hop) dan o'tgan (128-105=23). Windows server TTL ni 128, Linux 64 qilib jo'natadi |

**daryo.uz natijasi (qo'llanmadagi misol):**

| Ko'rsatkich | Qiymat | Xulosa |
|---|---|---|
| O'rtacha vaqt | 14 ms | Juda tez: server O'zbekiston ichida yoki yaqinida |
| Yo'qotish | 25% (1 paket) | ICMP server yoki provayder tomonidan bloklangan bo'lishi mumkin. Xavfli emas, sayt «men tirikman» xabariga javob bermayapti |
| TTL | 110 | 18 ta hop |

`ping` IPv4 uchun; IPv6 tarmog'ida `ping6`.

### 3. Traceroute

```bash
tracert google.com      # Windows
traceroute google.com   # Linux / macOS
```

**google.com yo'li (qo'llanmadagi misol, 13 hop):**

```
1   172.16.4.1         uyingizdagi Wi-Fi router
2   195.158.2.217      mahalliy provayder (Toshkent yoki viloyat uzeli)
3-4 10.x.x.x           provayder ichidagi marshrutizatorlar
5   84.54.64.157       O'zbekistonning asosiy internet uzeli (TAS-IX yoki UzTelecom)
6-7 84.54.64.x         O'zbekiston ichi, chiqish nuqtasi
8-9 195.69.189.x       Rossiya yoki Yevropa tranzit uzeli
10  195.69.189.105     Google tarmog'iga kirish nuqtasi (Frankfurt yoki London atrofida)
11-12 142.251.x.x      Google ichidagi marshrutizatorlar
13  142.251.140.174    Google serverining o'zi
```

13 bosqich, o'rtacha 100 ms atrofida: odatiy holat (O'zbekistondan Google gacha 10-15 bosqich).

**daryo.uz yo'li:** 1-4 hop uy routeri va provayder; **5-18 hop `* * *`** (routerlar ICMP ga javob bermagan); 19-hopda server o'zi javob berdi. Bu oddiy holat: ko'p provayderlar traceroute so'rovini bloklaydi. Oxirgi hopda server javob bergani uning faol va yaqin ekanini bildiradi.

### 4. Tracert flaglari (2.1-jadval)

| Flag | Nima qiladi | Qachon | Misol |
|---|---|---|---|
| `-d` | DNS nomlarini izlamaydi, faqat IP | Tezlik kerak, DNS sekin | `tracert -d google.com` |
| `-h 15` | Maksimal hop sonini belgilaydi (standart 30) | Uzoq serverlar | `tracert -h 20 facebook.com` |
| `-w 1000` | Har hopga kutish vaqti, ms (standart 4000) | Internet sekin | `tracert -w 1000 yandex.ru` |
| `-4` | Faqat IPv4 | IPv6 bilan muammo | `tracert -4 google.com` |
| `-6` | Faqat IPv6 | IPv6 borligini sinash | `tracert -6 google.com` |

### 5. Xavfsizlik nuqtai nazari

- Firewall qoidalarida ko'pincha tashqaridan kiruvchi ping taqiqlanadi: `DENY IN ANY -> ANY (ICMP Echo Request)` (O'quv qo'llanma). Shuning uchun ping javobsiz qolishi hujum belgisi emas.
- Razvedka (11 dars Wireshark, 10 dars hujum tasnifi) uchun ping ham ishlatiladi: faol hostlarni aniqlash (ping sweep) keyingi mavzularda.
- Wiresharkda ping paketlari ICMP sifatida ko'rinadi: ikki darsni bog'lash mumkin.

---

## Amaliy mashg'ulot (hujjat bo'yicha)

Har bir o'quvchi 4 ta turli saytga `ping` va `tracert` yuborsin. Tezlikni oshirish uchun tegishli flaglardan foydalansin. Natijalarni jadvalga joylab, hisobot tayyorlasin.

---

## Mustaqil topshiriqlar

### 1. Ping nima beradi · oson
`ping` buyrug'i qanday 3 narsani ko'rsatadi?
**Yechim:** qurilma faol yoki faol emasligi; javob vaqti (latency, RTT); paket yo'qolishi (packet loss).

### 2. RTT · oson
RTT ning to'liq nomi va ma'nosi?
**Yechim:** Round-trip time, paket borib-kelish vaqti.

### 3. Buyruqlar · oson
Windows, Linux/Mac da marshrut kuzatish buyruqlari qanday?
**Yechim:** Windows `tracert`, Linux/Mac `traceroute`.

### 4. Hop · oson
Hop nima?
**Yechim:** yo'ldagi router/marshrutlovchi, paketni keyingi bosqichga yuboradi.

### 5. TTL hisobi · o'rta
Ping javobida TTL=110 (Windows server). Paket nechta hopdan o'tgan?
**Yechim:** 128-110=18 hop.

### 6. Natijani izohlang · o'rta
`ping` natijasi: 200 ms, 0% yo'qotish. Bu nimani bildiradi?
**Yechim:** barcha paketlar yetib bordi, aloqa barqaror, lekin vaqt katta (kutilgan 30-60 ms dan ancha ko'p): paketlar uzoq yo'ldan aylanib kelayotgan bo'lishi mumkin.

### 7. Yulduzchalar · o'rta
tracert da 5-18 hoplarda `* * *` chiqdi, 19-da server javob berdi. Server o'chiqmi?
**Yechim:** yo'q. Routerlar ICMP ga javob bermagan (provayderlar bloklaydi), server esa faol.

### 8. Flag tanlang · o'rta
Internet sekin, har hopga 1 soniya kutish va DNS siz natija kerak. Qanday buyruq?
**Yechim:** `tracert -d -w 1000 google.com`.

### 9. To'rt sayt hisoboti · qiyin
4 ta saytga ping va tracert yuboring; jadval: sayt, o'rtacha ms, yo'qotish %, TTL, hop soni.
**Yechim:** natijalar o'quvchiga bog'liq; jadval 4 qator, 5 ustun; hop soni TTL dan (128 yoki 64 asosida) yoki tracert dan olinadi; ikkalasi mos kelishini tekshiring.

### 10. Marshrutni izohlash · qiyin
tracert natijasidan o'z yo'lingizni yozing: uy routeri, provayder, O'zbekiston uzeli, tashqi tranzit, manzil.
**Yechim:** namuna: 1-hop uy routeri (192.168.x.x yoki 172.16.x.x), 2-4 provayder, keyin O'zbekiston uzeli, tashqi tranzit uzellar va oxirgi hopda server. Har hop uchun IP va taxminiy rolni ko'rsatish.

### 11. Xatoni toping · qiyin
Do'stingiz: «daryo.uz da 25% yo'qotish bor, demak hujum ostida». Javob bering.
**Yechim:** xato: bu ko'pincha ICMP server yoki provayder tomonidan bloklangani belgisi; xavfli holat emas.

### 12. Wireshark + ping · bonus
Wireshark capture ishga tushirib, `ping` yuboring va `icmp` paketlarini toping. Echo so'rovi va javobini ajrating.
**Yechim:** Wiresharkda `icmp` protokoli ostida Echo (ping) request va reply juftliklari ko'rinadi (Source/Destination teskari).

---

## Tezkor savol-javob

1. **Savol:** Ping nimani o'lchaydi? **Javob:** RTT, echo paketi borib-kelish vaqtini.
2. **Savol:** Linux uchun boshlang'ich TTL? **Javob:** 64 (Windows 128).
3. **Savol:** `* * *` nimani bildiradi? **Javob:** Router ICMP ga javob bermagan.
4. **Savol:** `-d` flagi? **Javob:** DNS nomlarini izlamaydi.
5. **Savol:** IPv6 uchun ping? **Javob:** `ping6`.

---

## Mentor uchun eslatma

- Qiymatlar (163 ms, 14 ms, TTL 105/110, 13 hop) qo'llanmadagi misollar; o'quvchilarning natijalari boshqacha bo'ladi.
- Hujjatda TTL hisobi (128 yoki 64 dan ayirish) taxminiy usul sifatida berilgan; aniq OT ni TTL dan aniqlashga ishonmang.
- Windows nomi: hujjatda «CMD yoki Powershell»; hujjatdagi `ping6` eslatmasini aytib o'ting.
- Bu dars bilan 4-hafta tugaydi; 5-haftada IP-manzillash va qism tarmoqlar boshlanadi.
