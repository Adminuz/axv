# 9-dars. IP manzillash, Subnetting va tarmoq diagnostikasi vositalari

**Darsning maqsadi:** O'quvchilarga IPv4 manzillash arxitekturasi, ommaviy (Public) va xususiy (Private) IP diapazonlari (RFC 1918), Subnetting (qism tarmoqlar) mantig'i, CIDR notatsiyasi (`/24`, `/16`), tarmoq va broadcast manzillarini hisoblash, IPv6 ning zamonaviy ahamiyati hamda server nosozliklarini aniqlashda qo'llaniladigan asosiy diagnostika vositalari (`ping`, `traceroute`, `ss`, `curl`) bilan ishlashni amaliy o'rgatish.

**Vaqt taqsimoti:**
- O'tgan mavzuni takrorlash (OSI va TCP/IP steki): 10 daqiqa
- Yangi mavzu: IPv4 tuzilishi, xususiy IP lar, CIDR va Subnet mask hisoblash: 25 daqiqa
- Yangi mavzu: Tarmoq diagnostikasi vositalari (`ping`, `traceroute`, `ss`, `curl`): 20 daqiqa
- Amaliy mashg'ulot (Subnet hisoblash va serverlar o'rtasida ulanishlarni diagnostika qilish): 20 daqiqa
- Dars xulosasi va tezkor nazorat: 5 daqiqa

---

## 1. Dars konspekti (Mentor uchun)

### 1.1. IPv4 manzillash tuzilishi
Har bir kompyuter, server yoki konteyner tarmoqda o'zining noyob **IP (Internet Protocol) manzili** ga ega bo'lishi kerak.
- **IPv4**: 32 bitli ikkilik sondan iborat bo'lib, o'qish qulay bo'lishi uchun 4 ta sakkiz bitlik bloklarga — **oktet**larga ajratiladi va nuqta bilan yoziladi.
  Masalan: `192.168.1.1`
  Ikkilikda: `11000000.10101000.00000001.00000001`
- Har bir oktet `0` dan `255` gacha bo'lgan qiymatni qabul qiladi. Jami nazariy manzillar soni: $2^{32} \approx 4.3 \text{ milliard}$.

### 1.2. Ommaviy (Public) va Xususiy (Private) IP manzillar
Dunyo bo'yicha IPv4 manzillari tugab qolgani sababli, **RFC 1918** standarti bo'yicha maxsus xususiy manzillar ajratilgan:
1. **A sinf**: `10.0.0.0 – 10.255.255.255` (Katta korxonalar va ma'lumotlar markazlari).
2. **B sinf**: `172.16.0.0 – 172.31.255.255` (O'rta kompaniyalar, Docker konteynerlari standart tarmog'i).
3. **C sinf**: `192.168.0.0 – 192.168.255.255` (Uy va kichik ofis Wi-Fi tarmoqlari).
Xususiy IP lar Internetda to'g'ridan-to'g'ri marshrutlanmaydi. Ular routerdagi **NAT (Network Address Translation)** texnologiyasi orqali yagona ommaviy IP ga aylanib tashqariga chiqadi.

### 1.3. Subnet Mask va CIDR notatsiyasi
IP manzil doimo ikki qismdan iborat: **Tarmoq qismi (Network ID)** va **Xost qismi (Host ID)**.
Tarmoq qismi qayerda tugab, xost qismi qayerdan boshlanishini **Subnet Mask (Tarmoq maskasi)** belgilaydi.
- Standart maska: `255.255.255.0`
- **CIDR (Classless Inter-Domain Routing)**: Maskadagi birlar (`1`) sonini ifodalovchi qisqa yozuv:
  `255.255.255.0` = 24 ta bir = `/24`
- **Xostlarni hisoblash formulasi**: $N = 2^H - 2$
  (bu yerda $H$ — xost bitlari soni, ya'ni $32 - \text{CIDR}$).
  Masalan, `/24` uchun: $32 - 24 = 8$ bit. Xostlar: $2^8 - 2 = 256 - 2 = \mathbf{254 \text{ ta}}$.
  - Nega `-2` qilinadi?
    1. Eng birinchi manzil (`.0`) — **Tarmoq manzili (Network ID)** uchun band.
    2. Eng oxirgi manzil (`.255`) — **Efir manzili (Broadcast ID)** uchun band.

### 1.4. IPv6 ga qisqa nazar
IPv4 tugashi muammosini hal qiluvchi 128-bitli zamonaviy manzil:
- Masalan: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- 16-lik sanoq tizimida yoziladi va ikki nuqta `:` bilan ajratiladi.
- Manzillar soni $2^{128}$ ta (dunyodagi har bir qum zarrasiga milliardlab IP berishga yetadi).

### 1.5. DevOps uchun tarmoq diagnostikasi vositalari
Serverlar orasida aloqa yo'qolganda muammoni topish (troubleshooting) zanjiri:
1. `ping [manzil]` — ICMP Echo protokoli orqali masofaviy server tirikmi yoki yo'qmi, paketlar yo'qolishi (packet loss) va kechikish vaqti (RTT — round-trip time) ni o'lchaydi:
   - `ping -c 4 8.8.8.8` (4 ta paket yuborish).
2. `traceroute [manzil]` (yoki `tracepath`) — paket masofaviy serverga yetib borguncha necha ta oraliq routerdan (hops) o'tganini va qaysi routerda uzilish bo'layotganini aniqlaydi (TTL asosida).
3. `ss` (Socket Statistics) — serverdagi ochiq portlarni tekshirish:
   - `ss -tulpn` — TCP va UDP bo'yicha qaysi jarayon qaysi portni tinglayotganini ko'rsatadi.
4. `curl [URL]` — veb-serverga HTTP so'rovi yuborish:
   - `curl -I https://google.com` — veb-sahifa yuklamasdan faqat HTTP status kodini (200 OK, 301, 404, 500) va sarlavhalarini ko'rsatadi.
   - `curl -v https://api.site.uz` — SSL qo'l siqishi (handshake) va to'liq muloqotni ko'rsatadi.

---

## 2. Amaliy topshiriqlar va yechimlari (Mentor uchun)

### 1-topshiriq. Internet aloqasini va kechikishni (RTT) tekshirish
`ping` buyrug'i yordamida Google DNS serveri (`8.8.8.8`) bilan aloqani 4 ta paket bilan tekshiring va o'rtacha kechikish vaqtini aniqlang.

**Yechim:**
```bash
ping -c 4 8.8.8.8
# Natija tahlili:
# 4 packets transmitted, 4 received, 0% packet loss, time 3004ms
# rtt min/avg/max/mdev = 15.2/18.4/22.1/2.3 ms
# 0% paket yo'qolishi va o'rtacha 18.4 ms kechikish — mukammal aloqa!
```

### 2-topshiriq. Tarmoq marshrutini kuzatish (Traceroute)
O'z kompyuteringizdan to `google.com` gacha bo'lgan yo'lda necha ta oraliq tugun (router) borligini `tracepath` yoki `traceroute` bilan aniqlang.

**Yechim:**
```bash
tracepath google.com
# Yoki:
traceroute -n google.com
# Chiqishda har bir router IP si va unga ketgan millisekundlar ko'rinadi (odatda 8-15 ta oraliq qadam).
```

### 3-topshiriq. Veb-server holati va HTTP statusini tekshirish
`curl -I` yordamida ommaviy veb-saytning sarlavhalarini o'qing va uning javob kodini aniqlang.

**Yechim:**
```bash
curl -I https://www.google.com
# Natija:
# HTTP/2 200 (yoki 301 Moved Permanently)
# content-type: text/html; charset=ISO-8859-1
# server: gws
```

### 4-topshiriq. Subnet hisoblash amaliyoti
Berilgan IP manzil: `192.168.10.45/26`. Ushbu qism tarmoqning maskasini, tarmoq manzilini (Network ID), efir manzilini (Broadcast ID) va ulash mumkin bo'lgan maksimal xostlar sonini hisoblang.

**Yechim:**
- CIDR: `/26` → 26 ta bir: `11111111.11111111.11111111.11000000`
- Subnet mask: `255.255.255.192`
- Qolgan xost bitlari soni: $32 - 26 = 6$ bit.
- Maksimal xostlar soni: $2^6 - 2 = 64 - 2 = \mathbf{62 \text{ ta xost}}$.
- Blok hajmi: 64.
- Tarmoq manzillari bloklari: `.0`, `.64`, `.128`, `.192`.
- `192.168.10.45` birinchi blokda joylashgan:
  - **Tarmoq manzili (Network ID)**: `192.168.10.0`
  - **Efir manzili (Broadcast ID)**: `192.168.10.63`
  - **Ishlatilishi mumkin bo'lgan diapazon**: `192.168.10.1` dan `192.168.10.62` gacha.

---

## 3. Tezkor nazorat savollari (Dars yakuni)

1. **RFC 1918 bo'yicha xususiy (Private) IP manzillar qanday maqsadlarda ishlatiladi?**
   *Javob:* Tashkilotlar, ma'lumotlar markazlari va uy tarmoqlarida ichki kompyuterlarga IP tarqatish uchun. Ular global Internetda to'g'ridan-to'g'ri ko'rinmaydi va ommaviy IP manzillarni tejashga xizmat qiladi.
2. **Nima uchun har qanday qism tarmoqda (subnet) 2 ta manzil foydalanuvchilar kompyuterlariga berilmaydi?**
   *Javob:* Eng birinchi manzil butun tarmoq identifikatori (Network ID), eng oxirgi manzil esa barcha kompyuterlarga xabar yuboruvchi efir (Broadcast) uchun zaxiralangan.
3. **`ping` va `traceroute` buyruqlari qaysi tarmoq protokoliga tayanib ishlaydi?**
   *Javob:* **ICMP (Internet Control Message Protocol)** protokoliga tayanadi.
4. **`curl -I` bayrog'i nima vazifani bajaradi?**
   *Javob:* Sahifaning asosiy tanasini (HTML) yuklab olmasdan, faqatgina uning HTTP sarlavhalari (Headers) va holat kodini ekranga chiqaradi.
