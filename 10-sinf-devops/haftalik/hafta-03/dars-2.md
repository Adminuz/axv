# 8-dars. Kompyuter tarmoqlari asoslari: OSI 7 qatlamli modeli va TCP/IP steki

**Darsning maqsadi:** O'quvchilarga DevOps sohasining muhim ustuni bo'lgan kompyuter tarmoqlari asoslari, tarmoq turlari (LAN, WAN), tarmoq topologiyalari (Star, Mesh), ISO/OSI 7 qatlamli modeli va uning har bir bosqichi vazifasi, amaliy TCP/IP 4 qatlamli steki hamda ma'lumotlar enkapsulyatsiyasi (Data -> Segment -> Packet -> Frame -> Bits) tamoyillarini chuqur va tizimli o'rgatish.

**Vaqt taqsimoti:**
- O'tgan mavzuni takrorlash (Git branchlar va GitHub): 10 daqiqa
- Yangi mavzu: Tarmoq turlari, topologiyalar va nima uchun qatlamli model kerak: 20 daqiqa
- Yangi mavzu: OSI 7 qatlamli modeli va TCP/IP steki taqqosi, enkapsulyatsiya: 25 daqiqa
- Amaliy mashg'ulot (Tarmoq interfeyslarini tahlil qilish: `ip a`, `ip route` va qatlamlarni solishtirish): 20 daqiqa
- Dars xulosasi va tezkor nazorat: 5 daqiqa

---

## 1. Dars konspekti (Mentor uchun)

### 1.1. DevOps dunyosida tarmoqlarning o'rni
DevOps muhandisi har kuni serverlar, konteynerlar (Docker) va mikroxizmatlar (Kubernetes) o'rtasidagi aloqani sozlaydi. Agar tarmoq qanday ishlashini bilmasa, «serverga ulanib bo'lmayapti» yoki «port yopiq» kabi oddiy muammolarni ham yecha olmaydi.
- **LAN (Local Area Network)**: Cheklangan hududdagi (ofis, uy, maktab) kompyuterlarni bog'lovchi mahalliy tarmoq.
- **WAN (Wide Area Network)**: Shaharlar, davlatlar va qit'alarni birlashtiruvchi global tarmoq (eng yirik WAN — bu Internet).
- **Asosiy tarmoq qurilmalari**:
  - **Switch (Kommutator)**: Mahalliy tarmoq (LAN) ichida kompyuterlarni MAC-manzil bo'yicha bog'laydi (2-qatlam).
  - **Router (Marshrutizator)**: Turli tarmoqlarni o'zaro IP-manzil bo'yicha bog'laydi va ma'lumot yo'nalishini belgilaydi (3-qatlam).

### 1.2. OSI 7 qatlamli modeli (Open Systems Interconnection)
ISO tashkiloti tomonidan yaratilgan konseptual etalon model. U tarmoq orqali axborot uzatish jarayonini 7 ta mantiqiy bosqichga ajratadi:
1. **7. Application (Amaliy qatlam)**: Foydalanuvchi dasturlari bilan to'g'ridan-to'g'ri ishlaydi (HTTP, HTTPS, SSH, DNS, FTP).
2. **6. Presentation (Taqdimot qatlami)**: Ma'lumotlarni kodlash, siqish va shifrlash (TLS/SSL, ASCII, JSON, JPEG).
3. **5. Session (Sessiya qatlami)**: Ikkita tizim o'rtasida aloqa seansini ochish, ushlab turish va yopish.
4. **4. Transport (Transport qatlami)**: Ma'lumotlarni yaxlit yetkazib berish, portlar va oqimni boshqarish (TCP, UDP). Ma'lumot birligi: **Segment**.
5. **3. Network (Tarmoq qatlami)**: Global marshrutlash va mantiqiy manzillash (IP, ICMP, ARP). Ma'lumot birligi: **Paket (Packet)**.
6. **2. Data Link (Kanal qatlami)**: Bitta mahalliy tarmoqdagi qurilmalararo jismoniy uzatish (Ethernet, Wi-Fi, MAC manzil). Ma'lumot birligi: **Freym (Frame)**.
7. **1. Physical (Fizik qatlam)**: Elektr, optik yoki radio signallari (bitlar: 0 va 1 lar, kabellar, razyomlar).

### 1.3. TCP/IP steki: Amaliyotdagi Internet modeli
OSI — bu nazariy etalon bo'lsa, real Internet **TCP/IP** modeliga tayanadi. U 4 ta amaliy qatlamdan iborat:
1. **Application (Amaliy)**: OSI ning 7, 6, 5 qatlamlarini birlashtiradi (HTTP, SSH, DNS).
2. **Transport (Transport)**: TCP va UDP protokollari (OSI 4-qatlami).
3. **Internet (Tarmoq)**: IP (IPv4, IPv6) va ICMP (OSI 3-qatlami).
4. **Network Access (Tarmoqqa kirish)**: OSI ning 1 va 2 qatlamlarini (Ethernet, Wi-Fi) birlashtiradi.

### 1.4. Enkapsulyatsiya va Dekapsulyatsiya (Paket sayohati)
- **Enkapsulyatsiya (Jo'natishda)**: Yuqori qatlamdan tushgan ma'lumotga har bir quyi qatlam o'zining xizmat sarlavhasini (Header) qo'shadi:
  - Application: `Data` (HTML yoki matn).
  - Transport: `TCP Header + Data` = **Segment** (port raqamlari qo'shiladi).
  - Network: `IP Header + Segment` = **Paket** (jo'natuvchi va qabul qiluvchi IP manzillari).
  - Data Link: `Frame Header + Packet + Frame Trailer` = **Freym** (MAC manzillar va CRC xatolik tekshiruvi).
  - Physical: Freym `0` va `1` bitlar oqimiga aylanib kabeldan uzatiladi.
- **Dekapsulyatsiya (Qabul qilishda)**: Qabul qiluvchi kompyuter har bir qatlamda o'z sarlavhasini tekshirib yechib oladi va sof ma'lumotni ilovaga yetkazadi.

---

## 2. Amaliy topshiriqlar va yechimlari (Mentor uchun)

### 1-topshiriq. Tizim tarmoq interfeyslarini tahlil qilish
Linuxda `ip a` (yoki `ip addr show`) buyrug'ini bering. Tizimingizdagi lokal qaytish (`lo` - loopback) interfeysi va asosiy tarmoq kartasi (masalan, `eth0` yoki `enp0s3`) nomlarini, ularning MAC va IP manzillarini aniqlang.

**Yechim:**
```bash
ip a
# Tahlil:
# 1: lo — loopback interfeysi (127.0.0.1)
# 2: eth0 (yoki enp3s0) — fizik/virtual tarmoq interfeysi
#    link/ether aa:bb:cc:dd:ee:ff — 2-qatlam MAC manzili
#    inet 192.168.1.50/24 — 3-qatlam IPv4 manzili
```

### 2-topshiriq. Tarmoq shlyuzini (Default Gateway) aniqlash
`ip route` (yoki `ip r`) buyrug'i yordamida tashqi dunyoga (Internetga) chiquvchi asosiy yo'naltiruvchi (router/gateway) IP manzilini toping.

**Yechim:**
```bash
ip route
# Masalan: default via 192.168.1.1 dev eth0 proto dhcp metric 100
# Demak, Default Gateway (Router) manzili: 192.168.1.1
```

### 3-topshiriq. Ochiq portlar va transport qatlamini tekshirish
`ss -tulpn` buyrug'i orqali tizimda qaysi xizmatlar TCP yoki UDP orqali qaysi portlarni tinglayotganini (LISTEN) aniqlang.

**Yechim:**
```bash
sudo ss -tulpn
# Natijada Netid (tcp/udp), Local Address:Port (masalan, *:22 SSH uchun, *:80 Nginx uchun) va Process nomi aks etadi.
```

### 4-topshiriq. Qatlamlar bo'yicha ma'lumot uzatish tahlili
O'quvchiga quyidagi savol beriladi: Foydalanuvchi brauzerda `https://google.com` ga kirganda, OSI modelining 7, 4, 3 va 2-qatlamlarida qanday ma'lumotlar qo'shiladi?

**Yechim:**
- 7-qatlam (Application): HTTP GET so'rovi va TLS shifrlangan ma'lumot.
- 4-qatlam (Transport): Manba va manzil portlari (masalan, manzil porti `443`).
- 3-qatlam (Network): Foydalanuvchi IP manzili va Google serveri IP manzili.
- 2-qatlam (Data Link): Kompyuterning tarmoq kartasi MAC manzili va Router (Default Gateway) MAC manzili.

---

## 3. Tezkor nazorat savollari (Dars yakuni)

1. **OSI modeli nima uchun aynan 7 qatlamga bo'lingan?**
   *Javob:* Tarmoq texnologiyalarini standartlashtirish, turli ishlab chiqaruvchilar qurilmalarining bir-biri bilan muammosiz ishlashini ta'minlash va har bir qatlamni mustaqil yangilash imkonini berish uchun.
2. **Switch (kommutator) bilan Router (marshrutizator) OSI modelining qaysi qatlamlarida ishlaydi?**
   *Javob:* Switch 2-qatlamda (Data Link — MAC manzil bo'yicha), Router esa 3-qatlamda (Network — IP manzil bo'yicha) ishlaydi.
3. **Enkapsulyatsiya jarayonida ma'lumotlar birligi (PDU) qanday nomlanadi?**
   *Javob:* 4-qatlamda — Segment, 3-qatlamda — Paket, 2-qatlamda — Freym, 1-qatlamda — Bitlar.
4. **TCP/IP modelida OSI ning qaysi qatlamlari yagona «Application» qatlamiga birlashtirilgan?**
   *Javob:* 7 (Application), 6 (Presentation) va 5 (Session) qatlamlari.
