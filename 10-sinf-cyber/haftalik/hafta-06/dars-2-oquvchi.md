---
title: "Tarmoqlarda VPN qurish va shifrlash (1-qism): VPN arxitekturasi, tunnellash va IPsec protokoli"
description: "VPN maqsadi, shifrlash, tunnellash va inkapsulyatsiya, VPN turlari, IPsec transport va tunnel rejimlari"
dars: 2
hafta: 6
sinf: 10-sinf-cyber
---

# 17-dars. Tarmoqlarda VPN qurish va shifrlash (1-qism): VPN arxitekturasi, tunnellash va IPsec protokoli

> Ochiq internetda paketlarni hamma o'qiy oladi. Bugun VPN, tunnellash va IPsec qanday himoya qilishini o'rganamiz.

## Dars xulosasi

- IP paketlari ochiq uzatiladi, konfidensiallik yo'q.
- Shifrlash simmetrik (bir kalit) va assimetrik (kalit jufti) bo'ladi.
- Tunnellash — paketni boshqa paket ichiga o'rash (inkapsulyatsiya).
- VPN = tunnel + shifrlash + autentifikatsiya + yaxlitlik.
- Turlari: Remote Access, Site-to-Site, Client-Based, Clientless.
- IPsec: transport (hostlar) va tunnel (filiallar) rejimlari.

## Qo'shimcha ma'lumot

### ESP
IPsec ning shifrlash va yaxlitlik komponenti.

### L2TP
Kanal sathi tunneli; shifrni IPsec ta'minlaydi.

### PPTP
Eski, MPPE/RC4 asosida; zaif.

### SSL/TLS VPN
Brauzer orqali, qo'shimcha dastursiz.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| VPN | Virtual xususiy tarmoq |
| Tunnel | Himoyalangan mantiqiy kanal |
| Inkapsulyatsiya | Paketni paket ichiga o'rash |
| Plaintext | Ochiq matn |
| Ciphertext | Shifrlangan matn |
| IPsec | Tarmoq sathi VPN protokoli |
| Transport rejim | Hostlar orasida IPsec |
| Tunnel rejim | Butun paketni o'rovchi IPsec |

## Bilasizmi?

- IPsec transport rejimi L2TP kabi tunnellarni himoyalash uchun ishlatilishi mumkin.
- Clientless VPN brauzer orqali SSL/TLS bilan ishlaydi, qo'shimcha dastur kerak emas.
- Doimiy ajratilgan liniya ijaraga olishdan ko'ra vaqtinchalik tunnel arzonroq.

## Topshiriqlar

### 1. IP muammosi · oson

IP protokolining xavfsizlikdagi 2 ta kamchiligini yozing.

**Kutiladigan natija:** Shifrlash yo'q (ochiq paketlar); marshrutlash/DoS hujumlariga zaif.

### 2. VPN ta'rifi · oson

VPN ni o'z so'zingiz bilan ta'riflang.

**Kutiladigan natija:** Himoyalangan vaqtinchalik kanal.

### 3. Shifr turlari · oson

Simmetrik va assimetrik shifrlashni solishtiring.

**Kutiladigan natija:** 1 kalit va kalit jufti.

### 4. VPN turlari · oson

4 ta VPN turini sanang.

**Kutiladigan natija:** Remote Access, Site-to-Site, Client-Based, Clientless.

### 5. Remote yoki Site · o'rta

Ikki filial bog'lanadi: qaysi tur?

**Kutiladigan natija:** Site-to-Site.

### 6. OSI sathlari · o'rta

IPsec, L2TP va SSH qaysi sathga tegishli?

**Kutiladigan natija:** IPsec — tarmoq, L2TP — kanal, SSH — transport.

### 7. Inkapsulyatsiya · o'rta

Inkapsulyatsiyani misol bilan tushuntiring.

**Kutiladigan natija:** Asl paket yangi sarlavha ichida.

### 8. Tunnel shifrlaydimi · o'rta

Tunnel har doim shifrlaydimi?

**Kutiladigan natija:** Yo'q, lekin odatda shifrlanadi.

### 9. IPsec rejimi · qiyin

Host-host va ofis-ofis uchun rejimlarni tanlang va asoslang.

**Kutiladigan natija:** Transport va tunnel.

### 10. Tunnel chizmasi · qiyin

Tunnel paketining qismlarini chizib bering.

**Kutiladigan natija:** Tashqi sarlavha + tunnel + shifrlangan paket.

### 11. Protokol tanlash · qiyin

Nega zamonaviy tizimlar PPTP o'rniga IPsec yoki WireGuard ishlatadi?

**Kutiladigan natija:** PPTP shifri (RC4) zaif.

### 12. Wireshark · bonus

HTTP va HTTPS paketini solishtiring.

**Kutiladigan natija:** HTTP ochiq, HTTPS shifrlangan.

## O'zingizni tekshiring

1. IP nega xavfsiz emas?
2. Simmetrik va assimetrik shifr?
3. Tunnellash nima?
4. VPN turlari?
5. IPsec rejimlari?
6. PPTP nega zaif?

## Uyga vazifa

VPN va IPsec bo'yicha chizma va qisqa konspekt (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
