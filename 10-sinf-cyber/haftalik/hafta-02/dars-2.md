---
title: "CIA uchligi (2-qism): CIA buzilish ssenariylari va MITM hujumlari"
description: "CIA mezonlarining buzilish holatlari, O'rtadagi odam (MITM) hujumi, arpspoof va Wireshark yordamida tarmoq tahlili"
dars: 2
hafta: 2
sinf: 10-sinf-cyber
---

# 5-dars. CIA uchligi (2-qism): CIA buzilish ssenariylari va MITM hujumlari

## Dars rejasi (80 daqiqa)

1. **Kirish va takrorlash (10 daqiqa):** CIA uchligi (C, I, A) xususiyatlarini eslash va yangi dars maqsadlari.
2. **Nazariy qism (25 daqiqa):**
   - CIA uchligining real buzilish ssenariylari:
     - Konfidensiallik buzilishi: Ma'lumotlar o'g'irlanishi va sniffing;
     - Yaxlitlik buzilishi: Ma'lumotlarni soxtalashtirish (Tampering);
     - Foydalanuvchanlik buzilishi: Tizimning qulashi va to'xtab qolishi.
   - **O'rtadagi odam (Man-in-the-Middle — MITM) hujumi:**
     - ARP protokoli qanday ishlaydi va nima uchun unda autentifikatsiya yo'q?
     - ARP keshini zaharlash (ARP Poisoning / ARP Spoofing) mexanizmi.
     - Hujumchi qanday qilib trafik oqimining markaziga joylashadi?
   - Shifrlanmagan trafik xavfi (HTTP vs HTTPS).
   - MITM orqali sessiyalarni o'g'irlash (Session Hijacking) va SSL Strip hujumlari.
3. **Amaliy laboratoriya mashg'uloti (30 daqiqa):**
   - Virtual laboratoriya muhitida MITM ssenariysini tahlil qilish (Kali Linux va Wireshark).
   - `arpspoof` buyrug'i va paketlar oqimining yo'nalishini o'rganish.
   - Wiresharkda shifrlanmagan HTTP so'rovlar va parollarni kuzatish.
   - Himoya choralari: Statik ARP yozuvlari, Dynamic ARP Inspection (DAI), HTTPS Everywhere va VPN.
4. **Mustaqil topshiriqlar va muhokama (10 daqiqa):** 10 ta amaliy topshiriqni yechish.
5. **Xulosa va baholash (5 daqiqa):** Dars xulosasi va tezkor savol-javob.

---

## Asosiy tushunchalar

- **MITM (Man-in-the-Middle — O'rtadagi odam):** Ikki tomon (masalan, Bob va bank serveri) o'rtasidagi aloqa kanaliga suqilib kirib, ular bilmagan holda barcha uzatilayotgan ma'lumotlarni ushlab oluvchi, o'quvchi yoki o'zgartiruvchi xavfli kiberhujum turi.
- **ARP (Address Resolution Protocol):** Lokal tarmoqda (LAN) mantiqiy IP manzilni (masalan, `192.168.1.5`) fizik apparat manziliga — MAC manzilga (`00:1A:2B:3C:4D:5E`) aylantirib beruvchi tarmoq protokoli.
- **ARP Spoofing (ARP zaharlanishi):** Hujumchi tarmoqqa qalbaki ARP javoblarini (ARP Reply) yuborib, kompyuterlarni «Shlyuz (router) menman!» deb aldashi va barcha tarmoq trafigini o'zidan o'tkazishi.
- **Sniffing (Trafikni tutib olish):** Tarmoq kabeli yoki Wi-Fi orqali o'tayotgan barcha paketlarni maxsus dasturlar (Wireshark, tcpdump) yordamida yozib olish va tahlil qilish jarayoni.
- **Tampering (Ma'lumotlarni qalbakilashtirish):** Tranzitdagi ma'lumotlarni o'zgartirish orqali tizim yaxlitligiga (Integrity) putur yetkazish.
- **DAI (Dynamic ARP Inspection):** Tarmoq kommutatorlarida (Switch) soxta ARP paketlarini avtomatik bloklovchi xavfsizlik texnologiyasi.

---

## Dars mazmuni

### 1. CIA mezonlarining real buzilish ssenariylari

1. **Konfidensiallik buzilishi:**
   - Shifrlanmagan ochiq Wi-Fi (masalan, kafedagi parolsiz Wi-Fi) orqali Bob o'z login va parolini HTTP saytga kiritdi.
   - Tridi Wireshark dasturi orqali barcha paketlarni tutib olib, Bobning parolini ochiq matnda o'qidi.
2. **Yaxlitlik buzilishi:**
   - Bob Alisaning serveridan dastur yuklab olmoqda.
   - Tridi tarmoq o'rtasiga joylashib, qonuniy dastur faylini o'zining troyan dasturiga almashtirib yubordi. Bob qonuniy dastur o'rniga troyanni o'rnatdi.
3. **Foydalanuvchanlik buzilishi:**
   - Tridi shlyuz (gateway) IP manzilini soxtalashtirib, Bob yuborgan barcha paketlarni qora tuynuk kabi yutib yubordi va internetni to'xtatib qo'ydi.

---

### 2. O'rtadagi odam (MITM) hujumi qanday ishlaydi?

Lokal tarmoqda kompyuterlar bir-biri bilan IP manzil orqali emas, balki tarmoq kartasining MAC manzili orqali gaplashadi.

```
ODATIY HOLAT:
[ Bob (172.16.4.65) ] <--------------------------> [ Router / Shlyuz (172.16.5.97) ]
(Trafik to'g'ridan-to'g'ri o'tadi)

MITM HUJUMI HOLATI:
[ Bob (172.16.4.65) ]
        |
        v (Bob Tridini router deb o'ylaydi)
[ Tridi / Kali Linux (172.16.7.120) ]  <-- Barcha trafikni o'qiydi va o'zgartiradi
        |
        v (Tridi Bobning nomidan so'rov yuboradi)
[ Router / Server (172.16.5.97) ]
```

1. Hujumchi (Kali Linux) Bobga qarab: «Router (172.16.5.97) menman, mening MAC manzilimga yubor!» deb doimiy ARP xabarlarini yuboradi.
2. Xuddi shu paytda routerga qarab: «Bob (172.16.4.65) menman, xabarlarni menga yubor!» deydi.
3. Natijada Bob va Router bir-biri bilan bevosita emas, balki Tridi orqali aloqa qila boshlaydi.

---

## Amaliy laboratoriya mashg'uloti

> [!CAUTION]
> Ushbu amaliy mashg'ulot faqat laboratoriya muhitidagi sinov virtual mashinalarida (VirtualBox / VMware) o'tkaziladi. Begona tarmoqlarda ARP spoofing qilish qonuniy javobgarlikka olib keladi.

### 1-qadam: Laboratoriya muhiti IP konfiguratsiyasi
- **Hujumchi (Kali Linux):** `172.16.7.120`
- **Qurbon (Windows 10):** `172.16.4.65`
- **Shlyuz / Maqsadli server (Ubuntu):** `172.16.5.97`

### 2-qadam: Paketlarni yo'naltirish (IP Forwarding) va arpspoof
Kali Linux tizimida paketlar Tridi orqali uzilib qolmasdan o'tishi uchun marshrutlash yoqiladi:
```bash
# Kali Linux terminalida:
echo 1 > /proc/sys/net/ipv4/ip_forward

# Qurbon va Shlyuz o'rtasida ARP zaharlashni boshlash
sudo arpspoof -i eth0 -t 172.16.5.97 -r 172.16.4.65
```

### 3-qadam: Wireshark yordamida trafikni tahlil qilish
1. Kali Linuxda Wireshark dasturini ishga tushiring:
   ```bash
   sudo wireshark &
   ```
2. `eth0` interfeysini tanlang va paketlarni yozishni (Capture) boshlang.
3. Filtr maydoniga `http` yoki `arp` yozing.
4. Windows mashinasida biror shifrlanmagan HTTP saytga kirib, login va parol kiritilganda Wiresharkda quyidagilar ko'rinadi:
   - `POST /login.php HTTP/1.1`
   - Ochiq matnda uzatilgan foydalanuvchi nomi va paroli (`username=admin&password=MySecretPassword`).

### 4-qadam: MITM dan himoyalanish choralari
1. **Statik ARP jadvallari:** Tarmoqdagi muhim shlyuzlarning MAC manzilini qo'lda o'zgarmas qilib yozib qo'yish (`arp -s 172.16.5.97 00-11-22-33-44-55`).
2. **Faqat HTTPS / HSTS dan foydalanish:** Ma'lumotlar shifrlangan bo'lsa, Tridi ularni tutib olsa ham o'qiy olmaydi.
3. **VPN (Virtual Private Network):** Barcha trafikni shifrlangan xavfsiz tunnel ichidan o'tkazish.
4. **DAI (Dynamic ARP Inspection):** Tarmoq switchlarida qalbaki ARP Reply paketlarini filtrlovchi uskunaviy himoya.

---

## Mustaqil topshiriqlar

### 1. ARP protokolining zaifligi · oson
Nima sababdan klassik ARP protokoli buzg'unchi tomonidan osonlikcha aldanishi (zaharlanishi) mumkin? Unda qanday xavfsizlik mexanizmi yetishmaydi?
**Yechim:** ARP protokoli 1980-yillarda tarmoq ishonchli muhit deb hisoblangan davrda yaratilgan bo'lib, unda hech qanday autentifikatsiya (tasdiqlash) yoki shifrlash yo'q. Kompyuter o'zi so'ramagan bo'lsa ham kelgan har qanday «ARP Reply» javobiga ishonadi va o'zining kesh jadvalini yangilayveradi.

### 2. IP Forwarding buyrug'ining roli · oson
Kali Linuxda MITM o'tkazilayotganda nima uchun `echo 1 > /proc/sys/net/ipv4/ip_forward` buyrug'i bajarilishi shart? Agar bu bajarilmasa nima yuz beradi?
**Yechim:** Agar bu parametr yoqilmasa, Kali Linux qurbondan kelgan paketlarni keyingi manzilga (shlyuzga) uzatmaydi va o'zida to'xtatadi. Natijada qurbonning interneti butunlay uzilib qoladi va hujum MITM emas, balki oddiy DoS hujumiga aylanib qoladi (hujum fosh bo'ladi).

### 3. MITM ning CIA ga ta'siri · o'rta
MITM hujumi muvaffaqiyatli amalga oshganda CIA uchligining qaysi mezonlari buzilishi mumkin? Har biriga misol keltiring.
**Yechim:**
- Konfidensiallik (Confidentiality): Hujumchi o'tayotgan barcha parollar va shaxsiy ma'lumotlarni o'qiydi (Sniffing);
- Yaxlitlik (Integrity): Hujumchi paketlar tarkibidagi ma'lumotlarni (masalan, to'lov summasi yoki yuklanayotgan faylni) yo'lda o'zgartirishi mumkin (Tampering);
- Foydalanuvchanlik (Availability): Hujumchi ma'lum paketlarni qasddan bloklab, xizmatni to'xtatishi mumkin.

### 4. HTTPS protokoli MITM ga qarshi qanday himoya qiladi? · o'rta
Agar Bob HTTPS protokoli orqali bank saytiga kirayotgan bo'lsa, Tridi arpspoof orqali trafikni o'zidan o'tkazgan taqdirda ham parolni o'g'irlay oladimi?
**Yechim:** O'g'irlay olmaydi. Chunki HTTPS da barcha ma'lumotlar Bob va haqiqiy bank serveri o'rtasida TLS orqali shifrlanadi. Tridi shifrlangan matnni ko'radi, ammo shaxsiy shifrlash kalitiga ega bo'lmagani uchun parolni o'qiy olmaydi yoki o'zgartira olmaydi.

### 5. SSL ogohlantirishini e'tiborsiz qoldirish xatosi · o'rta
Brauzerda «Sertifikat ishonchsiz, davom etasizmi?» degan qizil ogohlantirish chiqqanda foydalanuvchi nima sababdan «Baribir davom etish» tugmasini bosmasligi kerak?
**Yechim:** Ushbu ogohlantirish tarmoqda kimdir (masalan, Tridi) oraga suqilib, soxta o'zining SSL sertifikatini taqdim etayotganidan (MITM / SSL Proxy) dalolat beradi. Agar foydalanuvchi baribir davom etsa, Tridi shifrlashni o'zida yechib, barcha parollarni qo'lga kiritadi.

### 6. Wireshark da parolni aniqlash belgisi · oson
Wireshark dasturida tutib olingan HTTP paketlari ichida foydalanuvchi kiritgan ma'lumotlar odatda qaysi HTTP so'rov metodi orqali uzatiladi?
**Yechim:** `POST` metodi orqali (`POST /login`, `POST /auth`).

### 7. Statik ARP jadvali sozlamasi · o'rta
Kichik ofisda routerga qaratilgan ARP Spoofing hujumlarini oldini olish uchun har bir kompyuterda qanday amaliy sozlama bajarilishi mumkin?
**Yechim:** Shlyuzning IP manzili va uning haqiqiy MAC manzilini har bir kompyuterda statik (o'zgarmas) qilib ro'yxatdan o'tkazish (`arp -s <IP> <MAC>`). Bunda kompyuter kelgan qalbaki dinamik ARP xabarlariga e'tibor bermaydi.

### 8. Dynamic ARP Inspection (DAI) qanday ishlaydi? · qiyin
Katta korporativ tarmoqlarda har bir kompyuterga qo'lda statik ARP yozish imkonsiz. Tarmoq switchlaridagi DAI texnologiyasi soxta ARP paketlarini qanday aniqlaydi?
**Yechim:** DAI tarmoq kommutatorida (Switch) DHCP Snooping ma'lumotlar bazasiga tayanadi. Switch har bir portdan kelayotgan ARP javobidagi IP va MAC manzilni o'zining ishonchli DHCP jadvali bilan solishtiradi. Agar mos kelmasa, qalbaki ARP paketini darhol tashlab yuboradi (drop) va portni xavfsizlik sababli o'chiradi.

### 9. VPN ning ochiq Wi-Fi da MITM ga qarshi afzalligi · o'rta
Kafedagi xavfli, parolsiz Wi-Fi tarmog'iga ulanishga majbur bo'lgan talabaga nima sababdan VPN ni yoqish qat'iy tavsiya etiladi?
**Yechim:** VPN foydalanuvchi qurilmasi va xavfsiz VPN serveri o'rtasida to'liq shifrlangan tunnel hosil qiladi. Hatto kafedagi xaker ARP Spoofing qilib paketlarni tutib olgan taqdirda ham, u faqat tushunarsiz VPN shifrlangan paketlarini ko'radi va birorta ham sayt nomini yoki parolni o'g'irlay olmaydi.

### 10. Meterpreter teskari shell ssenariysi tahlili · bonus
Buzg'unchi `msfvenom` orqali `malware.exe` yaratdi va uni MITM orqali qurbon kompyuteriga yuklatdi. Ushbu zararli dastur ishga tushganda nega bevosita 4444 portga teskari ulanish (Reverse TCP) qiladi va bu oddiy xavfsizlik devorlarini (Firewall) qanday aylanib o'tadi?
**Yechim:** Odatda tarmoqlararo ekranlar (Firewall) tashqaridan ichkariga keluvchi kiruvchi (Inbound) ulanishlarni qat'iy bloklaydi, ammo ichkaridan tashqariga chiquvchi (Outbound) ulanishlarga (internetga chiqishga) ruxsat beradi. Reverse TCP ulanishda zararlangan qurbonning o'zi tashqaridagi xaker serveriga ulanadi, natijada firewall bu ulanishni oddiy chiqish trafigi deb o'ylab to'xtatmaydi.

---

## Tezkor savol-javob

1. **Savol:** MITM qisqartmasi nimani anglatadi?
   **Javob:** Man-in-the-Middle (O'rtadagi odam).
2. **Savol:** ARP protokoli nima vazifani bajaradi?
   **Javob:** IP manzilni MAC manzilga bog'laydi.
3. **Savol:** Kali Linuxda ARP zaharlash qaysi buyruq yordamida amalga oshiriladi?
   **Javob:** `arpspoof`.
4. **Savol:** MITM hujumidan himoyalanishning eng ishonchli 2 ta usuli nima?
   **Javob:** HTTPS (shifrlangan aloqa) va VPN dan foydalanish.

---

## Mentor uchun eslatma

- Darsda MITM arxitekturasini doskada yoki slaydda Alisa, Bob va Tridi timsollarida aniq ko'rsating: Bob o'zini Alisa bilan gaplashyapman deb o'ylaydi, ammo o'rtada Tridi turibdi.
- O'quvchilarga ochiq jamoat Wi-Fi tarmoqlarida parollarni kiritish qanchalik xatarli ekanligini ta'kidlang.
