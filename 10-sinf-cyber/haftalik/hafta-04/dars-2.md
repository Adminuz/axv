---
title: "Tarmoq qurilmalari va xavfsizlik muammolari (2-qism): Wireshark yordamida tarmoq trafigini tahlil qilish"
description: "Paket tushunchasi, Wireshark o'rnatish, interfeys tanlash, capture, 3 panel, http va tls filtrlari, sayt ochilish bosqichlari"
dars: 2
hafta: 4
sinf: 10-sinf-cyber
---

# 11-dars. Tarmoq qurilmalari va xavfsizlik muammolari (2-qism): Wireshark yordamida tarmoq trafigini tahlil qilish

**Manba:** Uslubiy ko'rsatma, II bob, 2.1 «Wireshark bilan tarmoq paketlarini tahlil qilish»; O'quv dasturi (ta'lim maqsadlari: Wireshark yordamida paketlarni kuzatadi va asosiy protokollarni aniqlaydi).

## Dars rejasi (80 daqiqa)

1. **Takrorlash (8 daqiqa):** 10-dars: hab, switch, router; OSI sathlari. Savol: «Hab bilan o'ralgan tarmoqda boshqa kompyuter trafigini ko'rish nega osonroq?»
2. **Nazariy qism 1 (15 daqiqa):** paket nima, paket ichida nimalar bor (IP, protokol, ma'lumot), OSI 7 sathidan o'tishi, Wireshark nima.
3. **Amaliyot 1 (17 daqiqa):** Wireshark o'rnatish (Npcap), interfeys tanlash, capture boshlash, 3 panelni tanishish.
4. **Tanaffus (5 daqiqa).**
5. **Amaliyot 2 (20 daqiqa):** `http` filtri (GET), `tls` filtri (Client Hello), TCP/UDP/DNS/ICMP paketlari.
6. **Tahlil va xavfsizlik (10 daqiqa):** sayt ochilish bosqichlari; ochiq HTTP va shifrlangan HTTPS; himoya nuqtai nazari.
7. **Xulosa va tezkor nazorat (5 daqiqa).**

**Kutiladigan natija:** o'quvchi Wiresharkni o'rnatib, capture qiladi; 3 panelni tushuntiradi; `http` va `tls` filtrlarini qo'llaydi; «sayt ochdim» o'rniga «DNS so'rov, TCP handshake, TLS, HTTP GET» deb aniq tushuntiradi.

---

## Asosiy tushunchalar (uslubiy ko'rsatma bo'yicha)

- Internetdagi har bir harakat (sayt ochish, video ko'rish, ping jo'natish) minglab **paketlardan** iborat. Paket ichida manzillar (IP), protokol (TCP/UDP/ICMP) va ma'lumot (data) bo'ladi.
- Har bir paket OSI modelining 7 sathidan o'tadi: fizik, kanal (Ethernet, MAC), tarmoq (IP, marshrutlash), transport (TCP/UDP, portlar), seans, taqdimot, tadbiqiy (HTTP, DNS, HTTPS).
- **Wireshark** paketlarni «ushlab» olib, har bir qatlamini ochib ko'rsatadi; paketlarni kuzatish, filtrlash va tahlil qilish uchun eng mashhur bepul vositalardan biri.
- **Capture**: paketlarni tutib olish jarayoni. **Filtr**: ko'rinadigan paketlarni protokol bo'yicha tanlash.

---

## Dars mazmuni

### 1. Wireshark o'rnatish (1-qadam)

1. `wireshark.org` saytiga kiriladi.
2. «Download» bosilib, Windows yoki macOS uchun versiya tanlanadi.
3. O'rnatishda **WinPcap/Npcap** ni o'rnatishga ruxsat berish majburiy.
4. Wireshark ishga tushiriladi, asosiy oyna ochiladi.

### 2. Interfeys tanlash va capture (2-qadam)

- Interfeyslar ro'yxati chiqadi (Wi-Fi, Ethernet, Loopback).
- Faol internetga ulangan interfeys yonida **yashil grafik chiziq** bo'ladi: ustiga ikki marta bosiladi.
- Yuqoridagi ko'k «shark» belgisi (Start capturing packets) bosiladi: paketlar soniyada 100-1000 ta tezlikda oqadi.

### 3. Oynaning 3 qismi

```
+-------------------------------------------------------------+
| 1. YUQORI PANEL: paketlar ro'yxati                          |
|    No. | Time | Source | Destination | Protocol | Length | Info |
+-------------------------------------------------------------+
| 2. O'RTA PANEL: Packet Details                              |
|    Ethernet > IP > TCP/UDP > HTTP/DNS (kengaytiriladi)      |
|    TCP bayroqlari: SYN, ACK                                 |
+-------------------------------------------------------------+
| 3. PASTKI PANEL: Hex + ASCII                                |
|    Login/parol HTTP orqali ketsa, shu yerda ochiq ko'rinadi |
+-------------------------------------------------------------+
```

### 4. HTTP (3-qadam)

Brauzerda `http://example.com` ochiladi, Wiresharkda capture to'xtatiladi (qizil kvadrat). Filtr maydoniga `http` yoziladi va Enter bosiladi. HTTP GET (yoki POST) so'rovi topilib, ustiga bosiladi, pastda «Packet Details» ochiladi. Demak, sayt ochilganda brauzer serverga **GET** so'rovi jo'natadi: bu **7-sathda (Application)** bo'ladi.

### 5. HTTPS (4-qadam)

Capture qayta ishga tushiriladi, brauzerda biror **https** sayt ochiladi, Stop bosiladi, filtrga `tls` yoziladi. Natijada **TLS Handshake** (Client Hello) ko'rinadi: aloqa shifrlangan davom etadi, ma'lumotni o'rtada turib o'qib bo'lmaydi.

### 6. Boshqa protokollar

Xuddi shu holatda TCP, UDP, DNS, ICMP paketlarini ham tahlil qilish mumkin.

### 7. Asosiy xulosa

Dars oxirida o'quvchi «sayt ochdim» demaydi, balki: **«brauzer DNS so'rov jo'natdi, TCP handshake amalga oshirildi, TLS shifrlanishi boshlandi, HTTP GET so'rovi yuborildi»** deb tushuntiradi. Hujjat bo'yicha bu kiberxavfsizlik mutaxassisi uchun eng muhim ko'nikmalardan biri.

### 8. Xavfsizlik nuqtai nazari

- Hab va MITM kontekstida: Uslubiy ko'rsatma 1-bobida arpspoof bilan o'rtadagi odam hujumi ko'rsatilgan; Wiresharkda ARP paketlari ko'payishi va HTTP so'rovlar ochiq matnda kelishi aniq ko'rinadi. Bu darsda hujum bajarilmaydi, faqat kuzatish va tahlil.
- Himoya: HTTPS (TLS) ma'lumotni shifrlaydi.
- Qoida (mentor qo'shimchasi, hujjatda yo'q): faqat o'z kompyuteringiz yoki ruxsat berilgan laboratoriya trafigini tahlil qiling.

---

## Amaliy mashg'ulot (hujjat bo'yicha)

O'z kompyuteringizda Wiresharkni o'rnating va interfeys tanlash amalyotlarini bajaring. Har bir protokol bo'yicha kamida 3 tadan paketni tahlil qiling va natijalarni fayl ko'rinishida saqlab, hisobot tayyorlang.

---

## Mustaqil topshiriqlar

### 1. Wireshark nima · oson
Wireshark nima va nima uchun kerak? Bitta jumlada yozing.
**Yechim:** tarmoq paketlarini ushlab (capture), har bir qatlamini ochib ko'rsatadigan, kuzatish, filtrlash va tahlil qilish uchun mo'ljallangan eng mashhur bepul vosita.

### 2. Npcap · oson
O'rnatishda Npcap ga nega ruxsat berish kerak?
**Yechim:** hujjatda bu majburiy deb yozilgan (WinPcap/Npcap paket tutish uchun zarur).

### 3. Ustunlarni nomlang · oson
Paketlar ro'yxati panelining ustunlarini ayting.
**Yechim:** No., Time, Source, Destination, Protocol, Length, Info.

### 4. Qaysi panel · oson
Quyidagilarni mos panelga qo'ying: (a) Ethernet/IP/TCP sarlavhalari; (b) hex va ASCII; (c) paketlar ro'yxati.
**Yechim:** (a) o'rta panel (Packet Details); (b) pastki panel; (c) yuqori panel.

### 5. HTTP GET izlash · o'rta
`http://example.com` ni oching, `http` filtri bilan GET so'rovini toping. U qaysi OSI sathida?
**Yechim:** filtrga `http` yozilib, GET qatori tanlanadi; Packet Details ochiladi; bu 7-sath (Application).

### 6. HTTPS va TLS · o'rta
Biror https saytni oching, `tls` filtrini qo'llang. Nimani ko'rdingiz va bu nimani bildiradi?
**Yechim:** TLS Handshake (Client Hello) ko'rinadi; aloqa shifrlangan davom etadi, o'rtada turib o'qib bo'lmaydi.

### 7. Bayroqlarni toping · o'rta
TCP paketini kengaytirib, qaysi bayroqlarni ko'rdingiz?
**Yechim:** SYN, ACK (handshake paketlarida).

### 8. Sayt ochilish bosqichlari · o'rta
Sayt ochilganda tarmoqda nima bo'lishini 4 bosqichda yozing.
**Yechim:** 1) DNS so'rov; 2) TCP handshake; 3) TLS shifrlash boshlanishi (HTTPS bo'lsa); 4) HTTP GET so'rovi yuboriladi.

### 9. Protokol hisoboti · qiyin
TCP, UDP, DNS, ICMP bo'yicha kamida 3 tadan paketni tanlab, har biri uchun Source, Destination, Protocol, Info ni jadvalga yozing.
**Yechim:** natija o'quvchining paketlariga bog'liq; jadval 4 protokol x 3 paket = 12 qatordan iborat bo'lishi, har bir qatorda 4 ustun to'ldirilishi kerak. Tekshiring: ICMP paketlarini olish uchun ping yuboring, DNS uchun sayt nomini oching.

### 10. Ochiq va shifrlangan taqqoslash · qiyin
HTTP va HTTPS paketlarining pastki panelda (hex+ASCII) farqini tushuntiring. Nega HTTP orqali login/parol yuborish xavfli?
**Yechim:** HTTP da ma'lumot shifrlanmagan, login/parol ASCII ko'rinishda ochiq ko'rinishi mumkin; HTTPS da TLS shifrlaydi, o'qib bo'lmaydi. Hab yoki MITM orqali trafikni ushlagan shaxs ochiq HTTP ma'lumotini o'qiy oladi.

### 11. Xatoni toping · qiyin
Do'stingiz: «Wiresharkda tls filtrini yozdim, parolni topaman». Nima xato?
**Yechim:** TLS trafikni shifrlaydi; filtr faqat TLS paketlarini ko'rsatadi (Handshake), ma'lumotni ochmaydi. Bundan tashqari faqat o'zingizning trafikingizni tahlil qilish mumkin.

### 12. Tarmoq kuzatuv rejasi · bonus
Maktab Wi-Fi tarmog'ida G'ayrioddiy ARP paketlari ko'payganini ko'rdingiz. Nima deb o'ylaysiz va nima qilasiz?
**Yechim:** bu o'rtadagi odam (MITM, arpspoof) hujumi belgisi bo'lishi mumkin (Uslubiy ko'rsatma 1-bob); administratorga xabar berish, ochiq HTTP dan voz kechib HTTPS ishlatish.

---

## Tezkor savol-javob

1. **Savol:** HTTP ni ko'rish uchun filtr? **Javob:** `http`.
2. **Savol:** HTTPS boshlanishini ko'rish uchun filtr? **Javob:** `tls`.
3. **Savol:** Qaysi interfeysni tanlaymiz? **Javob:** Yonida yashil grafik chiziq bo'lgan faol interfeys.
4. **Savol:** Pastki panel nima beradi? **Javob:** Paketning hex va ASCII ko'rinishi.
5. **Savol:** GET qaysi sathda? **Javob:** 7-sath (Application).

---

## Mentor uchun eslatma

- Hujjatda ko'rsatilgan rasmlar (2.1-2.5) o'rnida slaydda sxemalar berilgan; imkon bo'lsa jonli Wireshark oynasini proyektorda ko'rsating (dasturlar ro'yxatida Wireshark, tcpdump bor).
- Hujjat Wireshark filtrlaridan faqat `http` va `tls` ni aniq ko'rsatadi; `dns`, `tcp`, `udp`, `icmp` filtrlari protokol nomi bilan yoziladi (tegishli protokollar tahlili hujjatda bor, filtr yozuvi mentor aniqlashtirishi).
- Etik qoida (faqat o'z trafik) mentor qo'shimchasi: hujjatda alohida band sifatida yo'q.
- Bu darsda hujum buyruqlari (arpspoof va h.k.) bajarilmaydi.
