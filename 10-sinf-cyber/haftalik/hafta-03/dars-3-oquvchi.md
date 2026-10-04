---
title: "Tarmoq asoslari: mijoz-server arxitekturasi, topologiyalar, OSI va TCP/IP modellari"
description: "Kompyuter tarmoqlari tasnifi (LAN, WAN), tarmoq topologiyalari, OSI 7 sathi va TCP/IP modeli hamda tarmoq protokollari"
dars: 3
hafta: 3
sinf: 10-sinf-cyber
---

# 9-dars. Tarmoq asoslari: mijoz-server arxitekturasi, topologiyalar, OSI va TCP/IP modellari

## Reja
1. Kompyuter tarmoqlari tushunchasi va Mijoz-Server (Client-Server) arxitekturasi.
2. Tarmoqlarning hududiy turlari: PAN, LAN, MAN, WAN.
3. Tarmoq topologiyalari (Shina, Yulduz, Halqa, Daraxt, Mesh) va ularning afzallik hamda kamchiliklari.
4. OSI 7 sathli etalon modeli va ma'lumotlar birligi (PDU).
5. TCP/IP modeli (4 ta sath) va asosiy protokollar.
6. MAC manzil va IP manzil farqi, TCP va UDP protokollarining ishlashi.

---

## Nazariy qism

### 1. Kompyuter tarmoqlari va Mijoz-Server modeli

**Kompyuter tarmog'i** — ma'lumotlarni almashish, resurslardan (fayllar, printerlar, internet) birgalikda foydalanish maqsadida aloqa kanallari orqali birlashtirilgan qurilmalar to'plamidir.
- **Server:** Tarmoqda xizmatlarni (veb-sayt, ma'lumotlar bazasi, fayllar) taqdim etuvchi kuchli kompyuter.
- **Mijoz (Client):** Serverga so'rov yuboruvchi foydalanuvchi kompyuteri yoki mobil qurilmasi.

### 2. Tarmoqlarning hududiy turlari
- **PAN (Personal Area Network):** 10 metrgacha bo'lgan shaxsiy tarmoq (Bluetooth naushnik, smartfon).
- **LAN (Local Area Network):** 2.5 km gacha bo'lgan bino, maktab yoki ofis tarmog'i.
- **MAN (Metropolitan Area Network):** Butun shahar bo'ylab yoyilgan tarmoq.
- **WAN (Wide Area Network):** Davlatlar va butun dunyoni qamragan global tarmoq (Internet).

---

### 3. Tarmoq topologiyalari

```
+--------------------------------------------------------------------------+
|                          TARMOQ TOPOLOGIYALARI                           |
+--------------------------------------------------------------------------+
| 1. Shina (Bus)       -> Bitta umumiy magistral kabel. Kabel uzilsa tizim  |
|                         to'xtaydi.                                       |
| 2. Yulduz (Star)     -> Barcha qurilmalar markaziy Switch ga ulangan.     |
|                         (Eng mashhur va qulay topologiya).               |
| 3. Halqa (Ring)      -> Paketlar doira bo'ylab aylanadi.                  |
| 4. To'liq bog'langan -> Har bir qurilma boshqasi bilan alohida ulangan    |
|    (Full Mesh)          (Eng ishonchli, ammo qimmat).                     |
+--------------------------------------------------------------------------+
```

---

### 4. OSI 7 sathi va TCP/IP modeli

Tarmoqda ma'lumot qanday qilib bir kompyuterdan ikkinchisiga yetib borishini standartlashtirish uchun **OSI (Open Systems Interconnection)** modeli ishlab chiqilgan:

```
OSI MODELI (7 sath)                 TCP/IP (4 sath)       PROTOKOLLAR
====================                 ===============       ===========
7. Tadbiqiy (Application)  \
6. Taqdimot (Presentation)  > ---->  Tadbiqiy (App)        HTTP, HTTPS, DNS, SSH, FTP
5. Seans (Session)         /
4. Transport (Transport) --------->  Transport             TCP, UDP
3. Tarmoq (Network) -------------->  Internet (Tarmoq)     IP (IPv4, IPv6), ICMP, ARP
2. Kanal (Data Link)      \  ----->  Tarmoqqa kirish       Ethernet, Wi-Fi (802.11),
1. Fizik (Physical)       /          (Network Access)      Kabel, Signal, MAC
```

**PDU (Protocol Data Unit):**
- Transport sathi: **Segment** (TCP) yoki **Datagram** (UDP);
- Tarmoq sathi: **Paket (Packet)**;
- Kanal sathi: **Kadr (Frame)**;
- Fizik sath: **Bitlar (Bits)**.

---

### 5. TCP va UDP solishtiruvi

| Mezon | TCP | UDP |
|---|---|---|
| **Bog'lanish** | Ulanish o'rnatiladi (3-Way Handshake) | Ulanishsiz (Connectionless) |
| **Ishonchlilik** | 100% kafolatlangan (paket yo'qolsa qaytariladi) | Kafolat yo'q (yo'qolsa o'tib ketadi) |
| **Tezlik** | Sekinroq, nazorat qilinadi | Juda tez, yengil |
| **Qo'llanishi** | Veb (HTTP/HTTPS), Fayllar (FTP), Email | Jonli efir (Streaming), DNS, O'yinlar |

---

## Amaliy laboratoriya

### 1-qadam: Tarmoq parametrlarini tekshirish
- Windows: Buyruqlar satrida `ipconfig /all` buyrug'ini tering.
- Linux / macOS: Terminalda `ip a` yoki `ifconfig` buyrug'ini tering.
- O'z kompyuteringizning **IPv4 manzili**, **MAC manzili** (Physical Address) va **Default Gateway** (router) manzilini toping.

### 2-qadam: Tarmoq aloqasini tekshirish (Ping)
```bash
ping -c 4 1.1.1.1
```
Natijada paketlar yo'qolishi (loss) 0% ekanligini va javob vaqtini (ms) tekshiring.

### 3-qadam: Marshrutni kuzatish (Traceroute)
- Windows: `tracert daryo.uz`
- Linux: `traceroute daryo.uz`
So'rovingiz maqsadli serverga borguncha nechta oraliq routerdan (hop) o'tishini tahlil qiling.

---

## Amaliy topshiriqlar

### 1. MAC va IP manzil farqi <Badge type="tip" text="oson" />
Nima sababdan kompyuterga ham fizik MAC manzil, ham mantiqiy IP manzil kerak? Nima uchun butun dunyoda faqat bittasi bilan ishlab bo'lmaydi?

### 2. TCP 3-Way Handshake <Badge type="tip" text="oson" />
TCP protokoli ulanish o'rnatayotganda qanday 3 ta paketdan (SYN, SYN-ACK, ACK) foydalanadi va ular qanday tartibda almashinadi?

### 3. UDP ning ustunligi <Badge type="warning" text="o'rta" />
Nima sababdan jonli video qo'ng'iroqlarda (Zoom, Telegram) yoki onlayn o'yinlarda TCP o'rniga UDP protokoli tanlanadi?

### 4. Transport sathining vazifasi <Badge type="warning" text="o'rta" />
OSI modelining 4-sathi (Transport sathi) qanday asosiy vazifani bajaradi va unda dasturlarni farqlash uchun qaysi manzil turi (identifikator) ishlatiladi?

### 5. Yulduz topologiyasi zaifligi <Badge type="warning" text="o'rta" />
Yulduz (Star) topologiyasi keng tarqalgan, ammo uning yagona zaif nuqtasi (Single Point of Failure) qayerda joylashgan va u ishdan chiqsa nima yuz beradi?

### 6. PDU birliklari mosligi <Badge type="tip" text="oson" />
Quyidagi sathlarga mos ma'lumotlar birligi (PDU) nomlarini ayting:
1. Fizik sath; 2. Kanal sathi; 3. Tarmoq sathi; 4. Transport sathi.

### 7. Enkapsulyatsiya mohiyati <Badge type="warning" text="o'rta" />
Foydalanuvchi saytga so'rov yuborganda ma'lumot qanday qilib 7-sathdan 1-sathgacha tushadi va har bir sathda unga nima qo'shiladi?

### 8. Ping va ICMP protokoli <Badge type="warning" text="o'rta" />
`ping` buyrug'i qaysi tarmoq protokoli yordamida ishlaydi va uning natijasidagi TTL (Time to Live) parametri nimani anglatadi?

### 9. Mesh topologiyasining o'rni <Badge type="danger" text="qiyin" />
Nima sababdan harbiy va bank tizimlarining eng muhim serverlari o'rtasida Mesh (To'liq bog'langan) topologiyasi qo'llaniladi? Uning asosiy kamchiligi nima?

### 10. OSI sathlaridagi xavflar xaritasi <Badge type="info" text="bonus" />
OSI ning 4 ta sathi (Fizik, Kanal, Tarmoq, Tadbiqiy) bo'yicha eng ko'p uchraydigan 1 tadan kiberhujum turini yozing.

---

## O'z-o'zini tekshirish savollari

1. LAN va WAN qanday farqlanadi?
2. Nima uchun Yulduz topologiyasining markazida Switch turadi?
3. OSI modelining 7 ta sathi nomlarini ketma-ket aytib bering.
4. HTTP va DNS protokollari qaysi sathga tegishli?
5. MAC manzil necha bitdan iborat?

---

## Foydali manbalar

- Cisco Networking Academy: Introduction to Networks.
- Cloudflare Learning Center: What is the OSI Model?
