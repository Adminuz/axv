---
title: "Tarmoqlarda VPN qurish va shifrlash (2-qism): WireGuard va OpenVPN yordamida xavfsiz tunnel o'rnatish"
description: "WireGuard kalit juftlari, wg0.conf, OpenVPN (sertifikat, .ovpn), protokollarni solishtirish, xavfsiz sozlash"
dars: 3
hafta: 6
sinf: 10-sinf-cyber
---

# 18-dars. Tarmoqlarda VPN qurish va shifrlash (2-qism): WireGuard va OpenVPN yordamida xavfsiz tunnel o'rnatish

**Manba:** O'quv qo'llanma II bob «VPN vositalarining tasnifi» (OpenVPN, IKEv2/IPsec va WireGuard zamonaviy vositalar); rasmiy o'quv dasturi (IPsec, L2TP, OpenVPN va WireGuard farqlari). Sozlama fayllari va buyruqlar WireGuard/OpenVPN standart hujjatlaridan qo'shildi.

## Dars rejasi (80 daqiqa)

1. **Takrorlash (8 daqiqa):** 17-dars: VPN turlari, tunnel, IPsec
2. **Nazariy qism 1 (15 daqiqa):** WireGuard g'oyasi: kalit juftlari, Peer, AllowedIPs
3. **Amaliyot 1 (15 daqiqa):** `wg0.conf` yozish va `wg-quick up`
4. **Tanaffus (5 daqiqa).**
5. **Nazariy + amaliyot 2 (22 daqiqa):** OpenVPN: sertifikatlar, server va mijoz fayllari
6. **Xavfsizlik va xulosa (10 daqiqa):** Solishtirish, xavfsizlik qoidalari va xulosa
7. **Tezkor nazorat (5 daqiqa).**

**Kutiladigan natija:** WireGuard da kalit juftini yaratadi (`wg genkey`, `wg pubkey`); `wg0.conf` dagi Interface va Peer bo'limlarini tushuntiradi; `wg-quick up wg0` bilan tunnelni yoqadi va `wg show` bilan tekshiradi; OpenVPN ning sertifikat va `.ovpn` mijoz faylini tushuntiradi; WireGuard, OpenVPN va IPsec ni solishtirib, vaziyatga mos tanlaydi.

---

## Asosiy tushunchalar

- WireGuard: kalit juftlari, ochiq kalit almashinadi.
- `wg0.conf` da `[Interface]` va `[Peer]` bo'limlari bor.
- `wg-quick up wg0` yoqadi, `wg show` tekshiradi.
- OpenVPN sertifikatlar va `.ovpn` fayl bilan ishlaydi (1194).
- Protokolni vaziyatga qarab tanlang.
- Shaxsiy kalitni hech qachon tarqatmang.

---

## Dars mazmuni

### 1. WireGuard: kalitlar va Peer

**WireGuard** — zamonaviy, sodda va tez VPN. Har tomon (peer) **kalit jufti** yaratadi: shaxsiy (private) kalit sirda qoladi, ochiq (public) kalit ikkinchi tomonga beriladi. Parol yoki murakkab sertifikat tizimi yo'q: tomonlar bir-birining ochiq kalitini bilsa, tunnel quriladi. Kalitlar `wg genkey` va `wg pubkey` bilan yaratiladi. **Shaxsiy kalitni hech qachon yubormang** va GitHub ga qo'ymang.

```bash
umask 077
wg genkey | tee server.key | wg pubkey > server.pub
wg genkey | tee client.key | wg pubkey > client.pub
cat server.pub
```

`umask 077` kalit fayllarini faqat sizga ochiq qiladi. Ochiq (`.pub`) kalit xavfsiz bo'lishadi, `.key` fayl esa sir.

### 2. WireGuard sozlama fayli

Sozlama `/etc/wireguard/wg0.conf` da. **[Interface]** — shu tomonning o'zi: `PrivateKey`, tunnel ichidagi `Address` va server uchun `ListenPort` (odatda 51820/UDP). **[Peer]** — ikkinchi tomon: uning `PublicKey`, ruxsat etilgan manzillar `AllowedIPs` (qaysi trafik tunnelga yo'naladi) va mijozda `Endpoint` (server IP:port). Yoqish: `sudo wg-quick up wg0`, tekshirish: `sudo wg show`, o'chirish: `wg-quick down wg0`.

```ini
[Interface]
PrivateKey = <mijoz.key>
Address = 10.8.0.2/24

[Peer]
PublicKey = <server.pub>
Endpoint = 203.0.113.10:51820
AllowedIPs = 10.8.0.0/24
```

`203.0.113.10` — hujjatlarda ishlatiladigan namunaviy IP. `AllowedIPs = 0.0.0.0/0` butun trafikni tunnelga yo'naltiradi.

### 3. OpenVPN va protokol tanlash

**OpenVPN** — keng tarqalgan, TLS asosidagi VPN. Autentifikatsiya **sertifikatlar** (CA, server va mijoz) yoki login orqali; standart port 1194 (UDP yoki TCP). Mijozga sozlama `.ovpn` fayl beriladi, ishga tushirish: `sudo openvpn --config client.ovpn`. U turli tarmoqlarda moslashuvchan, lekin sozlash WireGuard dan murakkabroq. **IPsec/IKEv2** — korporativ va mobil muhitda keng ishlatiladi. Tanlov: sodda va tez kerak — WireGuard; moslashuvchanlik va keng qo'llab-quvvatlash — OpenVPN; filiallar va qurilma qo'llab-quvvatlashi — IPsec.

```ini
client
dev tun
proto udp
remote vpn.example.uz 1194
ca ca.crt
cert client.crt
key client.key
```

`ca`, `cert`, `key` — sertifikat fayllari; ularni xavfsiz yetkazing va shaxsiy kalitni saqlang. `vpn.example.uz` namunaviy nom.

---

## Amaliy mashg'ulot

Laboratoriyada ikki VM (yoki bitta VM da test) tayyorlang. Ikkala tomonda `wg genkey | wg pubkey` bilan kalit jufti yarating, `wg0.conf` fayllarini yozing (server `10.8.0.1/24`, mijoz `10.8.0.2/24`), `wg-quick up wg0` bilan yoqing va `wg show`, `ping 10.8.0.1` bilan tekshiring. OpenVPN uchun `.ovpn` faylining har qatori nimani anglatishini daftarga yozing. Haqiqiy kalitlarni hisobotga qo'ymang.

---

## Mustaqil topshiriqlar

### 1. Kalit turlari · oson
WireGuard da qaysi kalit sir, qaysi biri beriladi?
**Yechim:** Private sir; public beriladi.

### 2. Buyruqlar · oson
Kalit yaratuvchi 2 ta buyruqni yozing.
**Yechim:** `wg genkey`, `wg pubkey`.

### 3. Bo'limlar · oson
`wg0.conf` ning 2 bo'limini yozing.
**Yechim:** [Interface], [Peer].

### 4. Portlar · oson
WireGuard va OpenVPN odatiy portlarini yozing.
**Yechim:** 51820/UDP va 1194.

### 5. AllowedIPs · o'rta
`AllowedIPs = 10.8.0.0/24` va `0.0.0.0/0` farqini yozing.
**Yechim:** Faqat tunnel tarmog'i va butun trafik.

### 6. Tekshirish · o'rta
Tunnel ishlayotganini qanday tekshirasiz?
**Yechim:** `wg show` va `ping`.

### 7. OpenVPN fayli · o'rta
`.ovpn` dagi `remote`, `ca`, `cert`, `key` ma'nosi?
**Yechim:** Server, CA, mijoz sertifikati va kaliti.

### 8. Firewall · o'rta
Serverda qaysi portni ochish kerak (WireGuard)?
**Yechim:** UDP 51820.

### 9. Protokol tanlash · qiyin
Uydan ishlovchi xodim uchun protokol tanlang va asoslang.
**Yechim:** WireGuard yoki OpenVPN.

### 10. Xato qidirish · qiyin
Handshake bo'lmasa, 3 ta ehtimoliy sabab yozing.
**Yechim:** Noto'g'ri kalit, port yopiq, Endpoint xato.

### 11. Kalit sizib chiqdi · qiyin
Shaxsiy kalit sizib chiqsa nima qilinadi?
**Yechim:** Yangi kalit va Peer larni yangilash.

### 12. Mini-laboratoriya · bonus
Ikki VM orasida tunnel quring va hisobot yozing.
**Yechim:** Ishlaydigan ping va skrinshot.

---

## Tezkor savol-javob

1. **Savol:** WireGuard da qaysi kalit sir? **Javob:** Shaxsiy (private).
2. **Savol:** `[Peer]` nima? **Javob:** Tunneldagi ikkinchi tomon.
3. **Savol:** `AllowedIPs` nima? **Javob:** Tunnelga yo'naladigan manzillar.
4. **Savol:** OpenVPN porti? **Javob:** 1194 (UDP yoki TCP).
5. **Savol:** Tunnelni qanday tekshirasiz? **Javob:** `wg show` va `ping`.

---

## Mentor uchun eslatma

- Amaliyot faqat virtual mashinada; haqiqiy kalitlarni hisobotga yoki GitHub ga qo'ymaslikni qat'iy ayting.
- VM yo'q bo'lsa, `wg genkey` va fayllar tuzilishini ko'rsatib, tunnelni bitta mashinada loopback bilan namoyish qiling.
- Qo'llanmada WireGuard/OpenVPN konkret sozlamalari yo'q; buyruqlar va fayllar rasmiy hujjatlardan qo'shildi.
- IP lar (203.0.113.x, 10.8.0.x) va `vpn.example.uz` namunaviy.
- Keyingi dars: shifrlangan trafikni tahlil qilish va oraliq nazorat.
