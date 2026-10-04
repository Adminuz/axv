---
title: "5-dars. CIA uchligi (2-qism): CIA buzilish ssenariylari va MITM hujumlari"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (Cyber)", "link": "/10-sinf-cyber/"}, "week": {"n": 2, "link": "/10-sinf-cyber/hafta-02/"}, "g": 5, "title": "CIA uchligi (2-qism): CIA buzilish ssenariylari va MITM hujumlari", "lead": "[!CAUTION]", "slide": "/slaydlar/10-sinf-cyber/hafta-02/dars-2.html", "tabs": [{"g": 4, "link": "/10-sinf-cyber/hafta-02/dars-1", "current": false}, {"g": 5, "link": "/10-sinf-cyber/hafta-02/dars-2", "current": true}, {"g": 6, "link": "/10-sinf-cyber/hafta-02/dars-3", "current": false}], "prev": {"g": 4, "title": "CIA uchligi (1-qism): konfidensiallik, yaxlitlik va foydalanuvchanlik tamoyillari", "link": "/10-sinf-cyber/hafta-02/dars-1"}, "next": {"g": 6, "title": "Xavfsizlikni anglash (1-qism): xavfsizlik tafakkuri va kuchli parollar siyosati", "link": "/10-sinf-cyber/hafta-02/dars-3"}}
---

---
title: "CIA uchligi (2-qism): CIA buzilish ssenariylari va MITM hujumlari"
description: "CIA mezonlarining buzilish holatlari, O'rtadagi odam (MITM) hujumi, arpspoof va Wireshark yordamida tarmoq tahlili"
dars: 2
hafta: 2
sinf: 10-sinf-cyber
---

<div class="blk">

## <Icon name="file-text" /> Reja

1. CIA mezonlarining buzilish holatlari (Sniffing, Tampering, Crash).
2. O'rtadagi odam (Man-in-the-Middle — MITM) hujumi mohiyati.
3. ARP protokoli va ARP Spoofing (kesh zaharlanishi) qanday sodir bo'ladi?
4. Laboratoriya muhiti tahlili: Kali Linux, arpspoof va Wireshark.
5. Shifrlanmagan HTTP trafigi xavfi va parollarning sizib chiqishi.
6. MITM dan himoyalanish strategiyalari: HTTPS, Statik ARP, DAI va VPN.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Nazariy qism

### 1. CIA uchligi qanday buziladi?

1. **Konfidensiallik buzilishi (Sniffing / O'g'irlash):**
   Foydalanuvchi shifrlanmagan tarmoqda ma'lumot uzatayotganda, buzg'unchi tarmoq trafigini tutib oladi va begona parollarni ochiq matnda o'qiydi.
2. **Yaxlitlik buzilishi (Tampering / Soxtalashtirish):**
   Hujumchi tarmoq orqali o'tayotgan fayl, xabar yoki pul o'tkazmasi summasini yo'lda o'zgartirib yuboradi.
3. **Foydalanuvchanlik buzilishi (Denial of Service / To'xtatish):**
   Hujumchi tarmoq shlyuzini soxtalashtirib, paketlarni yo'q qiladi yoki serverni soxta so'rovlar bilan to'ldirib xizmatni to'xtatadi.

---

### 2. O'rtadagi odam (MITM) hujumi nima?

**MITM (Man-in-the-Middle)** — ikki qonuniy tomon (masalan, Bob va bank serveri) o'rtasidagi aloqa kanaliga buzg'unchi (Tridi) yashirincha suqilib kirishi va barcha o'tadigan axborotni o'zidan o'tkazishidir.

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

### 3. ARP Spoofing qanday ishlaydi?

Lokal tarmoqda (LAN) qurilmalar bir-birini IP manzil orqali emas, tarmoq kartasining **MAC manzili** orqali taniydi. Buni **ARP (Address Resolution Protocol)** ta'minlaydi.

- ARP protokoli 1980-yillarda yaratilgan bo'lib, unda hech qanday **parol yoki tasdiqlash yo'q**.
- Hujumchi kompyuterga qarab: «Men routerman, mening MAC manzilimga yoz!» deb soxta ARP xabarlar yuborishi mumkin.
- Natijada qurbon kompyuteri router deb o'ylab, barcha ma'lumotlarni to'g'ridan-to'g'ri xakerga yuboradi.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy laboratoriya

> Ushbu amaliy mashg'ulot faqat laboratoriya sinov virtual mashinalarida (VirtualBox / VMware) o'tkaziladi. Begona tarmoqlarda sinash qonunan taqiqlanadi!

### Laboratoriya tahlili: arpspoof va Wireshark

1. **IP Forwarding yoqish:** Paketlar Kali orqali to'xtab qolmasdan o'tishi kerak:
   ```bash
   echo 1 > /proc/sys/net/ipv4/ip_forward
   ```
2. **ARP zaharlashni boshlash:**
   ```bash
   sudo arpspoof -i eth0 -t 172.16.5.97 -r 172.16.4.65
   ```
3. **Wireshark da paketlarni kuzatish:**
   - Wiresharkda `http` filtri qo'yiladi.
   - Agar qurbon HTTP (shifrlanmagan) saytga login-parol kiritsa, `POST /login` so'rovida login va parol ochiq matnda ko'rinadi.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy topshiriqlar

### 1. ARP protokoli zaifligi &lt;Badge type="tip" text="oson" />
Nima sababdan klassik ARP protokoli buzg'unchi tomonidan osonlikcha aldanishi (zaharlanishi) mumkin? Unda qanday xavfsizlik yetishmaydi?

### 2. IP Forwarding buyrug'i &lt;Badge type="tip" text="oson" />
Kali Linuxda MITM o'tkazilayotganda nima uchun `echo 1 > /proc/sys/net/ipv4/ip_forward` buyrug'i bajarilishi shart? Agar bu yoqilmasa nima yuz beradi?

### 3. MITM ning CIA ga ta'siri &lt;Badge type="warning" text="o'rta" />
MITM hujumi muvaffaqiyatli amalga oshganda CIA uchligining qaysi mezonlari qanday buzilishi mumkin? Har biriga misol keltiring.

### 4. HTTPS va MITM &lt;Badge type="warning" text="o'rta" />
Agar foydalanuvchi HTTPS protokoli orqali saytga kirayotgan bo'lsa, xaker tarmoq o'rtasida turib uning parolini o'g'irlay oladimi? Nima uchun?

### 5. SSL ogohlantirishining xavfi &lt;Badge type="warning" text="o'rta" />
Brauzerda «Sertifikat ishonchsiz, davom etasizmi?» degan ogohlantirish chiqqanda nima sababdan «Baribir davom etish» tugmasini bosmaslik kerak?

### 6. Wireshark da parollarni qidirish &lt;Badge type="tip" text="oson" />
Wireshark dasturida tutib olingan HTTP paketlari ichida foydalanuvchi kiritgan login-parol odatda qaysi HTTP metodi orqali uzatiladi?

### 7. Statik ARP himoyasi &lt;Badge type="warning" text="o'rta" />
Kichik ofisda routerga qaratilgan ARP Spoofing hujumlarini oldini olish uchun har bir kompyuterda qanday amaliy sozlama bajarilishi mumkin?

### 8. Dynamic ARP Inspection (DAI) &lt;Badge type="danger" text="qiyin" />
Katta korporativ tarmoqlarda har bir kompyuterga qo'lda yozish imkonsiz. Tarmoq switchlaridagi DAI texnologiyasi soxta ARP paketlarini qanday aniqlaydi va bloklaydi?

### 9. Ochiq Wi-Fi va VPN roli &lt;Badge type="warning" text="o'rta" />
Kafedagi parolsiz ochiq Wi-Fi tarmog'iga ulanishga majbur bo'lganda nima sababdan VPN ni yoqish MITM hujumidan 100% himoya qiladi?

### 10. Reverse TCP va Firewall tahlili &lt;Badge type="info" text="bonus" />
Metasploit zararli dasturlari nega bevosita teskari ulanish (Reverse TCP) qiladi va bu oddiy xavfsizlik devorlarini (Firewall) qanday aylanib o'tadi?

---

</div>

<div class="blk">

## <Icon name="file-text" /> O'z-o'zini tekshirish savollari

1. MITM hujumi qanday tarmoqlarda eng oson amalga oshiriladi?
2. IP manzil va MAC manzil o'rtasidagi farq nima?
3. Wireshark da paketlarni qanday filtr bilan qidirish mumkin?
4. Nima uchun shifrlanmagan HTTP bugungi kunda taqiqlangan hisoblanadi?
5. Tarmoq switchlarida ARP himoyasi uchun qanday texnologiya mavjud?

---

</div>

<div class="blk">

## <Icon name="file-text" /> Foydali manbalar

- Wireshark Official User Guide: `wireshark.org/docs/`
- OWASP: Man-in-the-Middle Attack overview.

</div>

