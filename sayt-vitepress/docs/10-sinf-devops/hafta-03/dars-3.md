---
title: "9-dars. IP manzillash, Subnetting va tarmoq diagnostikasi vositalari"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (DevOps)", "link": "/10-sinf-devops/"}, "week": {"n": 3, "link": "/10-sinf-devops/hafta-03/"}, "g": 9, "title": "IP manzillash, Subnetting va tarmoq diagnostikasi vositalari", "lead": "Tarmoq muhandisligi asoslari: IPv4 va IPv6, qism tarmoqlarni hisoblash (Subnetting, CIDR) hamda nosozliklarni aniqlovchi qurollar (ping, traceroute, ss, curl).", "slide": "/slaydlar/10-sinf-devops/hafta-03/dars-3.html", "tabs": [{"g": 7, "link": "/10-sinf-devops/hafta-03/dars-1", "current": false}, {"g": 8, "link": "/10-sinf-devops/hafta-03/dars-2", "current": false}, {"g": 9, "link": "/10-sinf-devops/hafta-03/dars-3", "current": true}], "prev": {"g": 8, "title": "Kompyuter tarmoqlari asoslari: OSI 7 qatlamli modeli va TCP/IP steki", "link": "/10-sinf-devops/hafta-03/dars-2"}, "next": null}
---

---

<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- IPv4 manzili 32 bitdan iborat bo'lib, nuqta bilan ajratilgan 4 ta oktet (0–255) ko'rinishida yoziladi.
- Butun dunyoda cheklangan IPv4 manzillarini tejash uchun RFC 1918 standarti bo'yicha xususiy (Private) diapazonlar (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) ajratilgan.
- IP manzil doimo Tarmoq (Network ID) va Xost (Host ID) qismlaridan iborat bo'lib, ularning chegarasini Subnet Mask (yoki `/24` kabi CIDR notatsiyasi) belgilaydi.
- Har qanday subnetda ikkita manzil zaxiralangan bo'ladi: birinchisi tarmoq identifikatori (Network ID), oxirgisi esa umumiy chaqiriq (Broadcast ID).
- IPv6 — 128 bitli zamonaviy manzil bo'lib, u manzillar tugash muammosini butunlay hal qiladi.
- Server nosozliklarini aniqlashda (troubleshooting) `ping` (kechikish va aloqa), `traceroute` (yo'ldagi routerlar), `ss` (ochiq portlar) va `curl` (HTTP javoblari) vositalari qo'llaniladi.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. CIDR va Subnetting nima uchun kerak?
Katta bir tashkilotda 500 ta kompyuter bo'lsa, ularni bitta umumiy tarmoqqa joylashtirish xavfli va samarasizdir (chunki barcha efir trafigi — broadcast barcha kompyuterlarga borib tarmoqni sekinlashtiradi).
Subnetting — bu katta tarmoqni kichik, xavfsiz va boshqariladigan mustaqil qismlarga (masalan: `Buxgalteriya tarmog'i`, `Dasturchilar tarmog'i`, `Serverlar tarmog'i`) ajratish jarayonidir.
- `/24`: 254 ta xost (standart ofis).
- `/25`: 126 ta xost.
- `/26`: 62 ta xost.
- `/27`: 30 ta xost.
- `/28`: 14 ta xost.
- `/30`: Atigi 2 ta xost (ikkita router orasidagi to'g'ridan-to'g'ri nuqta-nuqta ulanish).

### 2. NAT (Network Address Translation) mo''jizasi
Qanday qilib butun uyingizdagi 10 ta telefon va noutbuk bitta internet provayder kabeli orqali ishlaydi?
Router ichida **NAT** xizmati ishlaydi:
- Har bir qurilma uy ichida `192.168.1.X` xususiy manziliga ega.
- Tashqi internetga so'rov yuborilganda, router ularning xususiy manzilini o'zining yagona ommaviy (Public) IP siga almashtiradi va qaysi port orqali qaysi telefonga javob qaytarishni o'z jadvalida eslab qoladi.

### 3. TTL (Time to Live) va Traceroute qanday ishlaydi?
Agar tarmoqda marshrut aylana bo'lib qolsa (loop), paketlar abadiy aylanib yuravermasligi uchun har bir IP paketida **TTL (Time to Live)** degan hisoblagich bo'ladi (masalan, 64).
- Har bir oraliq routerdan o'tganda TTL qiymati 1 taga kamayadi.
- TTL `0` ga teng bo'lganda, oxirgi router paketni yo'q qiladi va jo'natuvchiga «Vaqt tugadi» (ICMP Time Exceeded) xabarini yuboradi.
- `traceroute` dasturi aynan shu xususiyatdan foydalanadi: avval TTL=1 bilan paket yuboradi (birinchi router fosh bo'ladi), keyin TTL=2 yuboradi (ikkinchi router fosh bo'ladi) va hokazo, oxirgi manzilgacha bo'lgan barcha serverlar zanjirini aniqlaydi!

### 4. Curl — DevOps'ning eng sevimli quroli
Serverda brauzer bo'lmagani sababli API va veb-xizmatlarni test qilish uchun `curl` ishlatiladi:
- `curl -I https://api.uz` — faqat sarlavhalarni tekshirish.
- `curl -X POST -d '{"user":"ali"}' -H "Content-Type: application/json" https://api.uz/login` — JSON ma'lumot jo'natish.
- `curl -o fayl.zip https://sayt.uz/fayl.zip` — fayllarni terminal orqali yuklab olish.

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **IPv4** | 32 bitli, to'rtta son bilan ifodalanadigan internet protokoli manzili. |
| **IPv6** | 128 bitli, cheksiz resursga ega zamonaviy internet protokoli manzili. |
| **Subnet Mask** | IP manzilning qaysi qismi tarmoqqa, qaysi qismi xostga tegishli ekanini ko'rsatuvchi bitlar niqobi. |
| **CIDR (Slash notatsiyasi)** | Tarmoq maskasidagi birlar sonini ifodalovchi qisqa yozuv (masalan: `/24`). |
| **Network ID** | Qism tarmoqning birinchi va rasmiy manzili (qurilmalarga berilmaydi). |
| **Broadcast ID** | Tarmoqdagi barcha qurilmalarga bir vaqtda xabar uzatuvchi eng oxirgi manzil. |
| **NAT** | Xususiy IP manzillarni ommaviy IP manzilga aylantiruvchi tarmoq texnologiyasi. |
| **Ping** | ICMP protokoli orqali masofaviy server bilan aloqa sifati va kechikishini tekshiruvchi utilita. |
| **Traceroute** | Ma'lumot paketi manzilga yetguncha bosib o'tgan barcha routerlar yo'nalishini aniqlovchi vosita. |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- IPv4 manzillari jami 4 294 967 296 tani tashkil etadi va ularning rasmiy zahirasi 2011-yilda to'liq tugagan deb e'lon qilingan.
- IPv6 manzillarining soni $3.4 \times 10^{38}$ ta bo'lib, bu raqam Yer yuzidagi barcha atomlar soniga yaqinlashadi.
- `ping` utilitasi suvosti kemalarining sonar tovush signali (ping-pong aks sadosi) sharafiga shunday nomlangan.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Masofaviy serverga ping yuborish <Badge type="tip" text="oson" />
`ping -c 4 1.1.1.1` (Cloudflare DNS) buyrug'i orqali aloqani tekshiring va o'rtacha kechikish vaqtini aniqlang.
**Kutiladigan natija:** 4 ta paket yuboriladi va o'rtacha `rtt avg` millisekundlarda ko'rinadi.

### 2. Ommaviy IP manzilni aniqlash <Badge type="tip" text="oson" />
`curl ifconfig.me` buyrug'i yordamida uyingiz yoki maktabingizning tashqi Internetdagi ommaviy (Public) IP manzilini toping.
**Kutiladigan natija:** Ekranga tashqi dunyoga ko'rinuvchi ommaviy IP chiqadi.

### 3. Veb-sayt sarlavhalarini o'qish <Badge type="tip" text="oson" />
`curl -I https://github.com` buyrug'ini bajaring va HTTP javob kodini (200, 301) hamda server turini aniqlang.
**Kutiladigan natija:** HTTP status kodi va sarlavhalar ro'yxati chiqadi.

### 4. /24 tarmoqda xostlar sonini hisoblash <Badge type="tip" text="oson" />
`/24` prefiksli tarmoqda nechta foydalanish mumkin bo'lgan xost mavjudligini formula orqali hisoblang.
**Kutiladigan natija:** $2^8 - 2 = 254$ ta xost ekanligi tasdiqlanadi.

### 5. Tarmoq marshrutini kuzatish <Badge type="warning" text="o'rta" />
`tracepath 8.8.8.8` buyrug'ini ishga tushiring va paketingiz manzilga yetguncha necha ta oraliq routerdan o'tganini hisoblang.
**Kutiladigan natija:** Qadam-baqadam oraliq serverlar ro'yxati aks etadi.

### 6. Ochiq portlarni filtrlab topish <Badge type="warning" text="o'rta" />
`sudo ss -tulpn | grep -E "22|80|443"` buyrug'i yordamida tizimda SSH (22) yoki veb-portlar ochiq ekanini tekshiring.
**Kutiladigan natija:** Ochiq portlar va ularni ushlab turgan jarayonlar ko'rinadi.

### 7. /25 qism tarmoq parametrlarini aniqlash <Badge type="warning" text="o'rta" />
`192.168.1.0/25` tarmog'ining maskasini, Network manzilini, Broadcast manzilini va ishlatiladigan diapazonini hisoblang.
**Kutiladigan natija:** Maska: `255.255.255.128`, Network: `.0`, Broadcast: `.127`, Diapazon: `.1 - .126`.

### 8. Veb-serverga to'liq ma'lumot so'rovi yuborish <Badge type="warning" text="o'rta" />
`curl -v https://httpbin.org/get` buyrug'ini bajaring va undagi DNS qidirish, TCP ulanish va TLS qo'l siqishi bosqichlarini kuzating.
**Kutiladigan natija:** `* Connected to ...`, `* TLS handshake` kabi tafsilotlar chiqadi.

### 9. /28 qism tarmoq hisob-kitobi <Badge type="danger" text="qiyin" />
Kichik ma'lumotlar markazi uchun `10.0.0.16/28` tarmog'i ajratildi. Ushbu tarmoqqa nechta server ulash mumkinligini va uning oxirgi ishchi IP manzilini aniqlang.
**Kutiladigan natija:** $2^4 - 2 = 14$ ta server, oxirgi ishchi IP: `10.0.0.30` (Broadcast: `10.0.0.31`).

### 10. Paketlar yo'qolishini (Packet loss) tekshirish <Badge type="danger" text="qiyin" />
`ping -c 20 -i 0.2 8.8.8.8` buyrug'i orqali tezkor 20 ta paket yuboring va bitta ham paket yo'qolmaganini (0% loss) tasdiqlang.
**Kutiladigan natija:** Tarmoq barqarorligi tahlili amalga oshiriladi.

### 11. Shaxsiy qism tarmoq rejasini tuzish (Tadqiqot) <Badge type="info" text="bonus" />
Tashkilotda 3 ta bo'lim mavjud: Dasturchilar (50 ta xost), Ma'muriyat (25 ta xost), Serverlar (10 ta xost). Ularning barchasini bitta `192.168.1.0/24` tarmog'i ichida eng tejamkor qilib taqsimlang (VLSM).
**Kutiladigan natija:** /26 (62 xost), /27 (30 xost), /28 (14 xost) qism tarmoqlari mukammal rejalashtiriladi.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Ommaviy (Public) va xususiy (Private) IP manzillarning asosiy farqi nimada?
2. Subnetting nima va u DevOps infratuzilmasida nima uchun qo'llaniladi?
3. `/24` bilan `/26` prefikslarining xostlar soni bo'yicha qanday farqi bor?
4. `ping` buyrug'i serverga javob bermasa, bu server 100% o'chirilganligini anglatadimi? (Firewall/ICMP bloklanishi mumkinmi?)
5. `curl -I` natijasidagi HTTP 200, 301 va 404 status kodlari nimani bildiradi?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. O'z kompyuteringizda `ping -c 5 8.8.8.8` buyrug'ini bajarib, minimal, o'rtacha va maksimal kechikish vaqtlarini yozib oling.
2. `curl ifconfig.me` orqali tashqi ommaviy IP manzilingizni aniqlang.
3. `192.168.50.0/26` tarmog'i uchun quyidagi 4 ta parametrni hisoblab konspekt daftaringizga yozing:
   - Tarmoq maskasi
   - Maksimal foydalanuvchilar soni
   - Tarmoq manzili (Network ID)
   - Efir manzili (Broadcast ID)
*(Kutiladigan vaqt: 25 daqiqa)*

</div>

