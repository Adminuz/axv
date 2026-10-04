# 8-dars. Kompyuter tarmoqlari asoslari: OSI 7 qatlamli modeli va TCP/IP steki

> Internet qanday ishlaydi: LAN va WAN tarmoqlari, OSI 7 qatlamli etalon modeli, amaliy TCP/IP steki va ma'lumotlar sayohati (enkapsulyatsiya).

---

## Dars xulosasi

- Kompyuter tarmoqlari masofasiga ko'ra ikkita asosiy toifaga bo'linadi: LAN (cheklangan mahalliy tarmoq) va WAN (global xalqaro tarmoq — Internet).
- Tarmoqdagi qurilmalarni bog'lash uchun Switch (LAN ichida MAC manzil bo'yicha) va Router (tarmoqlararo IP manzil bo'yicha) xizmat qiladi.
- ISO/OSI 7 qatlamli modeli — bu ma'lumot uzatish jarayonini standartlashtiruvchi nazariy etalon arxitekturadir.
- OSI qatlamlari: 1-Fizik, 2-Kanal (Data Link), 3-Tarmoq (Network), 4-Transport, 5-Sessiya, 6-Taqdimot, 7-Amaliy (Application).
- Real Internet amaliyotida 4 qatlamli **TCP/IP** modeli qo'llaniladi: Network Access, Internet (IP), Transport (TCP/UDP), Application (HTTP, DNS, SSH).
- Enkapsulyatsiya jarayonida ma'lumot yuqoridan pastga tushar ekan, har bir qatlamda o'z sarlavhasini oladi: Data → Segment → Paket → Freym → Bitlar.
- Linuxda tarmoq interfeyslari, MAC va IP manzillarini ko'rish uchun `ip a`, marshrutlarni aniqlash uchun `ip route` buyruqlari ishlatiladi.

---

## Qo'shimcha ma'lumot

### 1. Nega OSI 7 ta qatlamga ajratilgan?
Tasavvur qiling, pochtadan xat jo'natyapsiz:
1. Siz xat matnini yozasiz (Application).
2. Xatni konvertga solib manzilni yozasiz (Transport & Network).
3. Pochtachi uni mashinaga yuklaydi (Data Link).
4. Mashina yo'ldan yuradi (Physical).
Agar avtomobil yo'li buzilsa, xat matnini qayta yozish shart emas — shunchaki boshqa mashina yoki samolyot tanlanadi. Tarmoqlarda ham xuddi shunday: agar kabel (1-qatlam) o'rniga Wi-Fi ishlatilsa, brauzeringizdagi veb-sayt (7-qatlam) kodini o'zgartirish talab qilinmaydi! Har bir qatlam mustaqil ishlaydi.

### 2. MAC manzil va IP manzil farqi
- **MAC manzil (Media Access Control)**: Tarmoq kartasi (NIC) ishlab chiqaruvchisi tomonidan mikrosxemaga muhrlangan fizik «pasport raqami» (masalan: `00:1A:2B:3C:4D:5E`). U dunyoda yagona bo'lib, faqat bitta mahalliy tarmoq (LAN) ichida kompyuterni topishga xizmat qiladi (2-qatlam).
- **IP manzil (Internet Protocol)**: Tarmoq provayderi yoki router tomonidan beriladigan mantiqiy «pochta indeksi va xonadon raqami» (masalan: `192.168.1.50`). U butun dunyo bo'ylab global marshrutlash uchun kerak bo'ladi (3-qatlam).

### 3. Paket sayohati: Enkapsulyatsiyaning jonli misoli
Siz Telegram'da do'stingizga «Salom» deb yozdingiz:
1. **Application (7)**: `Salom` matni olinadi.
2. **Transport (4)**: Unga TCP sarlavhasi (Telegram porti) ulanadi → **Segment**.
3. **Network (3)**: Unga do'stingizning serveri IP manzili ulanadi → **Paket**.
4. **Data Link (2)**: Unga uyingizdagi Wi-Fi routerining MAC manzili ulanadi → **Freym**.
5. **Physical (1)**: Freym antenna orqali radio-to'lqin (bitlar) bo'lib havoga tarqaladi.
Router xabarni qabul qilib, uni optik tolali kabel orqali yorug'lik signallariga aylantirib okeanlar osha serverga yetkazadi!

### 4. Switch va Routerning DevOps'dagi o'rni
- Agar bitta server xonasidagi (data center) 50 ta server o'zaro aloqa qilishi kerak bo'lsa, ular **Switch** ga ulanadi.
- Agar shu serverlar tashqi dunyodagi mijozlar so'rovini qabul qilishi yoki bulutga ulanishi kerak bo'lsa, tarmoq oldiga **Router** va **Firewall** (xavfsizlik devori) qo'yiladi.

---

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **LAN (Local Area Network)** | Cheklangan geografik hududdagi (uy, bino, ma'lumotlar markazi) mahalliy kompyuterlar tarmog'i. |
| **WAN (Wide Area Network)** | Katta masofalarni, mamlakatlar va qit'alarni qamrab oluvchi global tarmoq (Internet). |
| **OSI modeli** | Tarmoq aloqasini 7 ta mantiqiy qatlamga ajratib standartlashtiruvchi xalqaro etalon model. |
| **TCP/IP steki** | Zamonaviy Internetning amaliy asosi bo'lgan 4 qatlamli protokollar to'plami. |
| **Enkapsulyatsiya** | Yuqori qatlam ma'lumotiga quyi qatlam xizmat sarlavhasini (Header) qo'shib borish jarayoni. |
| **Dekapsulyatsiya** | Qabul qilingan paketdan sarlavhalarni bosqichma-bosqich yechib, asl ma'lumotni ilovaga yetkazish. |
| **MAC Address** | Qurilmaning tarmoq adapteriga ishlab chiqaruvchi tomonidan berilgan 48-bitlik fizik identifikator. |
| **Switch** | Mahalliy tarmoqda (LAN) freymlarni faqat qabul qiluvchi qurilma MAC manziliga yo'naltiruvchi kommutator. |
| **Router** | Turli tarmoqlar o'rtasida paketlarni eng optimal yo'l orqali marshrutlovchi qurilma. |

---

## Bilasizmi?

- Internetning dastlabki asosi bo'lgan ARPANET tarmog'ida 1969-yil 29-oktyabrda birinchi marta «LOGIN» so'zi yuborilgan, ammo tizim «LO» harflaridan so'ng qulab tushgan.
- Butun dunyo qit'alari o'rtasidagi Internet trafigining 99% dan ortig'i sun'iy yo'ldoshlar orqali emas, balki okean tubiga yotqizilgan ulkan suvosti optik tolali kabellari orqali uzatiladi.
- Har bir kompyuterda mavjud bo'lgan `127.0.0.1` (localhost) IP manzili ma'lumotni tashqi tarmoqqa chiqarmasdan, kompyuterning o'ziga qaytaruvchi maxsus «qaytarma halqa» (loopback) hisoblanadi.

---

## Topshiriqlar

### 1. Tarmoq interfeyslarini ko'rish · oson
Terminalda `ip a` buyrug'ini ishga tushiring va kompyuteringizdagi faol tarmoq kartasi nomini aniqlang.
**Kutiladigan natija:** `eth0`, `enp0s3` yoki `wlan0` kabi interfeys nomi chiqadi.

### 2. MAC manzilni aniqlash · oson
`ip a` natijasidan `link/ether` qatorini toping va qurilmangizning 48-bitlik fizik MAC manzilini daftaringizga yozing.
**Kutiladigan natija:** `aa:bb:cc:dd:ee:ff` ko'rinishidagi 12 ta o'n oltilik belgi aniqlanadi.

### 3. Mahalliy IP manzilni topish · oson
Interfeys ostidagi `inet` bilan boshlanuvchi qatordan shaxsiy IPv4 manzilingizni aniqlang.
**Kutiladigan natija:** `192.168.x.x` yoki `10.0.x.x` shaklidagi manzil ko'rinadi.

### 4. Standart shlyuzni (Gateway) ko'rish · oson
`ip route` buyrug'i orqali marshrutizatoringizning (Default Gateway) IP manzilini toping.
**Kutiladigan natija:** «default via [IP_manzil]» qatori orqali router manzili ma'lum bo'ladi.

### 5. Loopback interfeysini tahlil qilish · o'rta
`ip a show lo` buyrug'ini bajaring va nima uchun `127.0.0.1` manzili va `lo` interfeysi mavjudligini tushuntirib bering.
**Kutiladigan natija:** Mahalliy dasturlar bir-biri bilan tarmoqsiz aloqa qilishi uchun zarur ekanligi tushuniladi.

### 6. Ochiq portlarni tinglovchi xizmatlarni topish · o'rta
`sudo ss -tulpn` buyrug'i orqali tizimda qaysi portlar ochiq ekanini va ular qaysi transport protokoliga (TCP/UDP) tegishli ekanini aniqlang.
**Kutiladigan natija:** Portlar ro'yxati (masalan: 22 - SSH, 53 - DNS) va ularning holati aks etadi.

### 7. OSI qatlamlari bo'yicha PDU nomlarini solishtirish · o'rta
1, 2, 3 va 4-qatlamlardagi ma'lumotlar birligi (PDU) nomlarini jadval ko'rinishida yozing.
**Kutiladigan natija:** Bitlar (1), Freym (2), Paket (3), Segment (4) taqqosi hosil qilinadi.

### 8. Tarmoq qurilmalari darajalarini belgilash · o'rta
Hub, Switch va Router qurilmalari OSI ning aynan qaysi qatlamlarida ishlashini tahlil qiling.
**Kutiladigan natija:** Hub (1-fizik), Switch (2-kanal), Router (3-tarmoq) ekani asoslanadi.

### 9. Enkapsulyatsiya ssenariysini tahlil qilish · qiyin
Brauzerda oddiy veb-sahifa ochilganda, so'rovning Application qatlamidan to kabelgacha qanday sarlavhalar bilan o'ralishini chizma ko'rinishida tasvirlang.
**Kutiladigan natija:** HTTP so'rovi + TCP port + IP manzil + MAC manzil zanjiri tahlil qilinadi.

### 10. Tarmoq kartasi statistikasini ko'rish · qiyin
`ip -s link` buyrug'i orqali qabul qilingan (RX) va uzatilgan (TX) baytlar hamda xatolar (errors) sonini tahlil qiling.
**Kutiladigan natija:** Jismoniy tarmoq kartasi orqali o'tgan trafik hajmi ko'rinadi.

### 11. Wireshark bilan paketlarni tutish (Tadqiqot) · bonus
Agar tizimingizda Wireshark yoki `tcpdump` o'rnatilgan bo'lsa, `sudo tcpdump -c 5` orqali tarmoq kartasidan o'tayotgan 5 ta jonli paket sarlavhalarini ko'ring.
**Kutiladigan natija:** Jonli tarmoq paketlarining tuzilishi amalda kuzatiladi.

---

## O'zingizni tekshiring

1. LAN bilan WAN ning asosiy farqlari nimada?
2. Nima uchun kompyuterga ham MAC manzil, ham IP manzil kerak?
3. OSI 7 qatlamli modelining 4-qatlamida (Transport) qaysi asosiy protokollar ishlaydi?
4. Enkapsulyatsiya va dekapsulyatsiya jarayonlarini hayotiy misol bilan tushuntirib bering.
5. TCP/IP modelida OSI ning qaysi qatlamlari birlashtirilgan?

---

## Uyga vazifa

1. O'z kompyuteringizda `ip a` va `ip route` buyruqlarini bajaring.
2. Interfeys nomi, shaxsiy IP manzili, MAC manzili va router (Gateway) manzilini daftaringizga chizib, tarmoq xaritasini hosil qiling.
3. OSI ning 7 ta qatlami nomlarini va har bir qatlamda ishlovchi kamida bittadan protokolni jadval ko'rinishida yozing (taxminiy vaqt: 25 daqiqa).
