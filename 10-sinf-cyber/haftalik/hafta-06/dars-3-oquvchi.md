---
title: "Tarmoqlarda VPN qurish va shifrlash (2-qism): WireGuard va OpenVPN yordamida xavfsiz tunnel o'rnatish"
description: "WireGuard kalit juftlari, wg0.conf, OpenVPN (sertifikat, .ovpn), protokollarni solishtirish, xavfsiz sozlash"
dars: 3
hafta: 6
sinf: 10-sinf-cyber
---

# 18-dars. Tarmoqlarda VPN qurish va shifrlash (2-qism): WireGuard va OpenVPN yordamida xavfsiz tunnel o'rnatish

> Nazariyadan amaliyotga: bugun WireGuard bilan haqiqiy tunnel quramiz va OpenVPN sozlamasini o'qiymiz.

## Dars xulosasi

- WireGuard: kalit juftlari, ochiq kalit almashinadi.
- `wg0.conf` da `[Interface]` va `[Peer]` bo'limlari bor.
- `wg-quick up wg0` yoqadi, `wg show` tekshiradi.
- OpenVPN sertifikatlar va `.ovpn` fayl bilan ishlaydi (1194).
- Protokolni vaziyatga qarab tanlang.
- Shaxsiy kalitni hech qachon tarqatmang.

## Qo'shimcha ma'lumot

### Handshake
Tunnel tomonlari kalitlar bilan tanishgan lahza; `wg show` da ko'rinadi.

### Full tunnel
`AllowedIPs = 0.0.0.0/0`: butun trafik VPN orqali.

### Split tunnel
Faqat kerakli tarmoqlar VPN orqali yuboriladi.

### Sertifikat
OpenVPN da tomonlarning shaxsini tasdiqlaydi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| WireGuard | Zamonaviy sodda VPN |
| OpenVPN | TLS asosidagi VPN |
| Peer | Ikkinchi tomon |
| AllowedIPs | Tunnelga yo'naladigan IP lar |
| Endpoint | Server IP:port |
| wg-quick | WireGuard boshqaruv buyrug'i |
| .ovpn | OpenVPN mijoz fayli |
| Handshake | Kalit tasdiqlash lahzasi |

## Bilasizmi?

- WireGuard kodi juda qisqa: tekshirish va xavfsizlik auditi osonroq.
- OpenVPN TCP 443 portida ham ishlay oladi, ba'zi tarmoqlarda bu ulanishga yordam beradi.
- Ko'p mobil qurilmalar IKEv2/IPsec ni qo'llab-quvvatlaydi.

## Topshiriqlar

### 1. Kalit turlari · oson

WireGuard da qaysi kalit sir, qaysi biri beriladi?

**Kutiladigan natija:** Private sir; public beriladi.

### 2. Buyruqlar · oson

Kalit yaratuvchi 2 ta buyruqni yozing.

**Kutiladigan natija:** `wg genkey`, `wg pubkey`.

### 3. Bo'limlar · oson

`wg0.conf` ning 2 bo'limini yozing.

**Kutiladigan natija:** [Interface], [Peer].

### 4. Portlar · oson

WireGuard va OpenVPN odatiy portlarini yozing.

**Kutiladigan natija:** 51820/UDP va 1194.

### 5. AllowedIPs · o'rta

`AllowedIPs = 10.8.0.0/24` va `0.0.0.0/0` farqini yozing.

**Kutiladigan natija:** Faqat tunnel tarmog'i va butun trafik.

### 6. Tekshirish · o'rta

Tunnel ishlayotganini qanday tekshirasiz?

**Kutiladigan natija:** `wg show` va `ping`.

### 7. OpenVPN fayli · o'rta

`.ovpn` dagi `remote`, `ca`, `cert`, `key` ma'nosi?

**Kutiladigan natija:** Server, CA, mijoz sertifikati va kaliti.

### 8. Firewall · o'rta

Serverda qaysi portni ochish kerak (WireGuard)?

**Kutiladigan natija:** UDP 51820.

### 9. Protokol tanlash · qiyin

Uydan ishlovchi xodim uchun protokol tanlang va asoslang.

**Kutiladigan natija:** WireGuard yoki OpenVPN.

### 10. Xato qidirish · qiyin

Handshake bo'lmasa, 3 ta ehtimoliy sabab yozing.

**Kutiladigan natija:** Noto'g'ri kalit, port yopiq, Endpoint xato.

### 11. Kalit sizib chiqdi · qiyin

Shaxsiy kalit sizib chiqsa nima qilinadi?

**Kutiladigan natija:** Yangi kalit va Peer larni yangilash.

### 12. Mini-laboratoriya · bonus

Ikki VM orasida tunnel quring va hisobot yozing.

**Kutiladigan natija:** Ishlaydigan ping va skrinshot.

## O'zingizni tekshiring

1. WireGuard da qaysi kalit sir?
2. `[Peer]` nima?
3. `AllowedIPs` nima?
4. OpenVPN porti?
5. Tunnelni qanday tekshirasiz?
6. Protokolni qanday tanlaysiz?

## Uyga vazifa

WireGuard fayllarini yozing va tunnelni sinang (30 daqiqa). To'liq shart: `uyga-vazifa.md`.
