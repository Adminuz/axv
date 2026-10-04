---
title: "Tarmoq asoslari: mijoz-server arxitekturasi, topologiyalar, OSI va TCP/IP modellari"
description: "Kompyuter tarmoqlari tasnifi (LAN, WAN), tarmoq topologiyalari, OSI 7 sathi va TCP/IP modeli hamda tarmoq protokollari"
dars: 3
hafta: 3
sinf: 10-sinf-cyber
---

# 9-dars. Tarmoq asoslari: mijoz-server arxitekturasi, topologiyalar, OSI va TCP/IP modellari

## Dars rejasi (80 daqiqa)

1. **Kirish va takrorlash (10 daqiqa):** 1-bob xulosasi (Kiberxavfsizlikka kirish, CIA, STRIDE) va II bobga kirish.
2. **Nazariy qism (25 daqiqa):**
   - Kompyuter tarmoqlari tushunchasi va **Mijoz-Server (Client-Server)** arxitekturasi.
   - Tarmoqlarning hududiy tasnifi: PAN, LAN, MAN, WAN.
   - **Tarmoq topologiyalari:** Shina (Bus), Yulduz (Star), Halqa (Ring), Daraxt (Tree), To'liq bog'langan (Mesh) — afzallik va zaifliklari.
   - **OSI 7 sathli etalon modeli:**
     1. Fizik sath (Physical);
     2. Kanal sathi (Data Link);
     3. Tarmoq sathi (Network);
     4. Transport sathi (Transport);
     5. Seans sathi (Session);
     6. Taqdimot sathi (Presentation);
     7. Tadbiqiy sath (Application).
   - **TCP/IP modeli (4 ta sath):** Network Access, Internet, Transport, Application.
   - Protokollar steki: HTTP, DNS, TCP, UDP, IP, ICMP, ARP, Ethernet.
   - MAC manzil (48 bit apparat) va IP manzil (32 bit mantiqiy) farqi.
   - TCP (3-way handshake: SYN, SYN-ACK, ACK) va UDP (uzluksiz oqim) farqi.
3. **Amaliy laboratoriya mashg'uloti (30 daqiqa):**
   - Tarmoq konfiguratsiyasini terminalda ko'rish (`ipconfig /all` yoki `ip a`).
   - Ping va traceroute buyruqlari orqali tarmoq bog'lanishini tekshirish.
   - OSI sathlari bo'yicha paket enkapsulyatsiyasini Wiresharkda ko'rish.
4. **Mustaqil topshiriqlar va muhokama (10 daqiqa):** 10 ta amaliy vazifani yechish.
5. **Xulosa va baholash (5 daqiqa):** Dars xulosasi va 3-hafta yakuniy baholash mezonlari.

---

## Asosiy tushunchalar

- **Kompyuter tarmog'i:** Axborot, resurslar (fayllar, printerlar, internet) va xizmatlarni birgalikda almashish uchun aloqa kanallari orqali birlashtirilgan kompyuterlar tizimi.
- **Server:** Tarmoqda boshqa qurilmalarga ma'lum xizmatlarni (veb, ma'lumotlar bazasi, fayl, pochta) taqdim etuvchi markaziy kompyuter.
- **Mijoz (Client):** Serverdan xizmat yoki axborot so'rovchi ishchi stansiya yoki foydalanuvchi qurilmasi.
- **LAN (Local Area Network):** Kichik hududda (bino, maktab, ofis — diametri 2.5 km dan oshmaydigan) joylashgan lokal kompyuter tarmog'i.
- **WAN (Wide Area Network):** Katta geografik hududlarni, mamlakatlar va qit'alarni qamrab olgan global kompyuter tarmog'i (masalan, Internet).
- **Tarmoq topologiyasi:** Tarmoqdagi kompyuterlar va aloqa liniyalarining geometrik joylashuvi va o'zaro bog'lanish chizmasi.
- **OSI modeli (Open Systems Interconnection):** Tarmoqda ma'lumotlar uzatilishini standartlashtiruvchi 7 sathli nazariy etalon model.
- **TCP/IP modeli:** Zamonaviy internetning amaliy asosi bo'lgan 4 sathli protokollar steki.
- **MAC manzil (Media Access Control):** Tarmoq kartasiga (NIC) ishlab chiqaruvchi tomonidan berilgan 48 bitli (6 baytli) noyob fizik apparat manzili.
- **IP manzil:** Tarmoqdagi qurilmaga mantiqiy beriladigan unikal raqamli manzil (IPv4 — 32 bit, IPv6 — 128 bit).
- **TCP (Transmission Control Protocol):** Ma'lumotlarning yetib borishini 100% kafolatlovchi, 3 bosqichli qo'l berishishga (3-Way Handshake) asoslangan ishonchli protokol.
- **UDP (User Datagram Protocol):** Bog'lanish o'rnatmasdan, kafolatsiz ammo juda yuqori tezlikda ma'lumot uzatuvchi protokol (video oqimlar, DNS, onlayn o'yinlar).

---

## Dars mazmuni

### 1. Tarmoq topologiyalari va ularning zaifliklari

```
+--------------------------------------------------------------------------+
|                          TARMOQ TOPOLOGIYALARI                           |
+--------------------------------------------------------------------------+
| 1. Shina (Bus)       -> Yagona markaziy kabel. Kabel uzilsa tarmoq o'ladi.|
| 2. Yulduz (Star)     -> Barcha kompyuterlar markaziy Switch ga ulangan.   |
| 3. Halqa (Ring)      -> Paketlar aylanma yo'nalishda bittadan o'tadi.     |
| 4. To'liq bog'langan -> Har bir qurilma boshqasi bilan to'g'ridan-to'g'ri |
|    (Full Mesh)          ulangan (eng ishonchli, ammo eng qimmat).         |
+--------------------------------------------------------------------------+
```

Zamonaviy lokal tarmoqlarda (LAN) asosan **Yulduz (Star)** topologiyasi qo'llaniladi. Uning markazida Switch (kommutator) turadi. Agar bitta kompyuter kabeli uzilsa, qolgan tarmoq uzluksiz ishlayveradi.

---

### 2. OSI 7 sathi va TCP/IP modeli taqqoslovi

Ma'lumot uzatish jarayonida har bir sath o'zining sarlavhasini (Header) qo'shadi — bu **Enkapsulyatsiya (Encapsulation)** deb ataladi:

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

### 3. PDU (Protocol Data Unit) — ma'lumotlar birligi
- **Tadbiqiy sath:** Data (Ma'lumot);
- **Transport sathi:** Segment (TCP) yoki Datagram (UDP);
- **Tarmoq sathi:** Packet (IP paket);
- **Kanal sathi:** Frame (Kadr / Freym);
- **Fizik sath:** Bits (0 va 1 lar oqimi).

---

### 4. TCP vs UDP taqqoslash

| Xususiyat | TCP (Transmission Control Protocol) | UDP (User Datagram Protocol) |
|---|---|---|
| **Bog'lanish turi** | Ulanish o'rnatiladi (Connection-oriented) | Ulanish o'rnatilmaydi (Connectionless) |
| **Ishonchlilik** | Yuqori: har bir paket yetib borgani tekshiriladi | Kafolat yo'q: paket yo'qolsa qayta so'ralmaydi |
| **Qo'l berishish** | 3-Way Handshake (SYN -> SYN-ACK -> ACK) | Yo'q, to'g'ridan-to'g'ri oqim yuboriladi |
| **Tezlik** | Sarlavhalar katta, sekinroq | Juda tez, yengil |
| **Qo'llanishi** | Veb (HTTP/HTTPS), Fayl yuklash (FTP), Pochta (SMTP) | Jonli video (Streaming), DNS, Ovozli qo'ng'iroq (VoIP), O'yinlar |

---

## Amaliy laboratoriya mashg'uloti

### 1-qadam: Tarmoq sozlamalarini ko'rish
Kompyuteringizning IP va MAC manzilini aniqlang:
- **Windows (CMD):**
  ```cmd
  ipconfig /all
  ```
  Quyidagilarni toping:
  - *IPv4 Address*: Kompyuteringizning mantiqiy manzili;
  - *Physical Address (MAC)*: Tarmoq kartangizning 48 bitli apparat manzili (`XX-XX-XX-XX-XX-XX`);
  - *Default Gateway*: Mahalliy routerning IP manzili.
- **Linux / macOS:**
  ```bash
  ip a
  # yoki
  ifconfig
  ```

### 2-qadam: Tarmoq aloqasini tekshirish (Ping)
DNS serveri va internetga ulanishni tekshirish:
```bash
ping -c 4 1.1.1.1
```
TTL (Time to Live) va paketlar yo'qolishi (0% loss) ko'rsatkichlarini o'rganing.

### 3-qadam: Marshrutni kuzatish (Traceroute)
Sizning so'rovingiz saytga yetib borguncha nechta routerdan (hop) o'tishini ko'rish:
- **Windows:** `tracert daryo.uz`
- **Linux / macOS:** `traceroute daryo.uz`

---

## Mustaqil topshiriqlar

### 1. MAC manzil va IP manzil farqi · oson
Nima sababdan kompyuterga ham MAC manzil, ham IP manzil kerak? Faqat bittasi bilan internetda ishlash mumkin emasmi?
**Yechim:** MAC manzil apparat darajasida (lokal tarmoqda, kabel yoki Wi-Fi orqali) aynan qaysi fizik qurilmaga ma'lumot berilishini ta'minlaydi. IP manzil esa global tarmoqda (internetda) marshrutlash (yo'naltirish) uchun kerak. Agar faqat MAC bo'lsa, butun dunyodagi milliardlab kompyuterlar ichidan yo'nalish topib bo'lmaydi (chunki MAC geografik tuzilishga ega emas).

### 2. TCP 3-Way Handshake bosqichlari · oson
TCP protokoli ulanish o'rnatishda qanday 3 ta xabardan foydalanadi va ular qanday ketma-ketlikda yuboriladi?
**Yechim:**
1. Mijoz serverga `SYN` (Synchronize) paketini yuboradi («Men ulanmoqchiman»);
2. Server mijozga `SYN-ACK` (Synchronize-Acknowledge) javobini qaytaradi («Qabul qildim, men ham tayyorman»);
3. Mijoz serverga `ACK` (Acknowledge) paketini yuboradi («Tasdiqlayman, ma'lumot uzatishni boshladik»).

### 3. UDP ning afzalligi · o'rta
Nima sababdan onlayn video qo'ng'iroqlarda (Zoom, Telegram qo'ng'iroq) yoki onlayn o'yinlarda TCP o'rniga UDP protokolidan foydalaniladi?
**Yechim:** Jonli ovoz va video muloqotda asosiy talab — bu minimal kechikish (real-time tezlik). Agar bitta kadr yoki tovush paketi yo'qolsa, TCP uni qayta so'rab 1 soniya kutib turadi va efir qotadi. UDP esa yo'qolgan paketni tashlab yuborib, darhol keyingi yangi kadrni uzatadi, natijada aloqa uzluksiz davom etadi.

### 4. OSI modelidagi Transport sathi vazifasi · o'rta
OSI modelining 4-sathi (Transport sathi) qanday asosiy vazifani bajaradi va unda qaysi manzil turi (identifikator) ishlatiladi?
**Yechim:** Transport sathi ma'lumotlarni oxirgi nuqtadan oxirgi nuqtaga (End-to-End) uzatishni boshqaradi, katta ma'lumotlarni segmentlarga bo'ladi va xatoliklarni tekshiradi. Ushbu sathda qaysi dasturga ma'lumot borishini ko'rsatuvchi **Port raqamlari** (masalan, 80, 443, 22) ishlatiladi.

### 5. Yulduz (Star) topologiyasining zaif nuqtasi · o'rta
Yulduz topologiyasi juda qulay va keng tarqalgan, ammo uning yagona zaif nuqtasi (Single Point of Failure) qayerda joylashgan?
**Yechim:** Markaziy kommutatorda (Switch yoki Routerda). Agar kompyuterlardan biri buzilsa boshqalarga ta'sir qilmaydi, ammo markaziy Switch ishdan chiqsa, butun tarmoqdagi barcha kompyuterlar bir zumda aloqasiz qoladi.

### 6. PDU birliklarini moslash · oson
Quyidagi sathlarga mos Protocol Data Unit (PDU) nomlarini moslang:
1. Fizik sath; 2. Kanal sathi; 3. Tarmoq sathi; 4. Transport sathi.
**Yechim:**
1. Fizik sath — Bit (Bits);
2. Kanal sathi — Kadr (Frame);
3. Tarmoq sathi — Paket (Packet);
4. Transport sathi — Segment (TCP) / Datagram (UDP).

### 7. Enkapsulyatsiya jarayoni · o'rta
Foydalanuvchi veb-saytga so'rov yuborganda ma'lumot qanday qilib 7-sathdan 1-sathgacha tushadi? Bu jarayon qanday ataladi?
**Yechim:** Bu jarayon **Enkapsulyatsiya (Encapsulation)** deb ataladi. Ma'lumot (Data) Transport sathida TCP sarlavhasini olib Segmentga aylanadi, Tarmoq sathida IP sarlavhasini olib Paketga aylanadi, Kanal sathida MAC sarlavhasini olib Kadrga aylanadi va Fizik sathda 0 va 1 signallari (bitlar) ko'rinishida kabel yoki to'lqin orqali uzatiladi.

### 8. Ping va ICMP protokoli tahlili · o'rta
`ping` buyrug'i tarmoqda qaysi protokol yordamida ishlaydi va uning TTL parametri nimani anglatadi?
**Yechim:** `ping` buyrug'i **ICMP (Internet Control Message Protocol)** protokoli orqali ishlaydi (Echo Request va Echo Reply). TTL (Time to Live) — paket yo'lda nechta routerdan (hop) o'tishi mumkinligini cheklovchi hisoblagich bo'lib, har bir routerdan o'tganda 1 ga kamayadi. Bu paketning tarmoqda cheksiz aylanib qolishining (looping) oldini oladi.

### 9. Mesh (To'liq bog'langan) topologiyasi xavfsizligi · qiyin
Nima sababdan harbiy va bank tizimlarining kritik serverlari o'rtasida Mesh (To'liq bog'langan) topologiyasi qo'llaniladi? Uning kamchiligi nimada?
**Yechim:** Mesh topologiyasida har bir tugun barcha boshqa tugunlar bilan to'g'ridan-to'g'ri alohida kabel bilan bog'langan. Hatto bir nechta kabel uzilib yoki routerlar portlab ketsa ham, ma'lumot boshqa aylanma yo'llar orqali yetib boradi (maksimal ishonchlilik). Kamchiligi — juda katta miqdorda kabel va qimmat portlar talab qilinishi.

### 10. OSI sathlaridagi xavfsizlik tahdidlari xaritasi · bonus
OSI ning 4 ta sathi (Fizik, Kanal, Tarmoq, Tadbiqiy) bo'yicha eng mashhur 1 tadan kiberhujum turini ko'rsating.
**Yechim:**
1. Fizik sath: Kabelni jismoniy kesish, uskunani o'g'irlash yoki apparat ushlagich (Hardware Keylogger) ulash;
2. Kanal sathi (Data Link): ARP Spoofing va MAC Flooding hujumlari;
3. Tarmoq sathi (Network): IP Spoofing va ICMP (Ping) Flood DoS hujumi;
4. Tadbiqiy sath (Application): SQL Injection, Cross-Site Scripting (XSS) va HTTP Slowloris.

---

## Tezkor savol-javob

1. **Savol:** OSI modeli necha sathdan iborat?
   **Javob:** 7 ta sathdan.
2. **Savol:** IP qaysi sathda ishlaydi?
   **Javob:** 3-sath — Tarmoq sathi (Network layer).
3. **Savol:** TCP va UDP ning eng katta farqi nimada?
   **Javob:** TCP ma'lumotning yetib borishini kafolatlaydi (ulanishli), UDP esa kafolat bermaydi ammo ancha tez ishlaydi (ulanishsiz).
4. **Savol:** Tarmoqdagi kompyuterning apparat manzili nima deyiladi?
   **Javob:** MAC manzil.

---

## Mentor uchun eslatma

- Darsda o'quvchilarga `ipconfig /all` va `traceroute` buyruqlarini o'z kompyuterlarida bajartirib ko'ring.
- Paketning 7-sathdan 1-sathgacha qanday «konvert ichiga konvert» qilib solinishini (enkapsulyatsiya) vizual chizib bering.
- 3-hafta yakunlangani munosabati bilan barcha o'quvchilarning 1-9 darslar bo'yicha o'zlashtirishini sarhisob qiling.
