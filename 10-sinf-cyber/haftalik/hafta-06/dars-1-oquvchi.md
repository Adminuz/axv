---
title: "Tarmoqlararo ekran va filtrlash (2-qism): Windows Defender Firewall va iptables da qoidalar yaratish"
description: "netsh advfirewall, profillar, iptables zanjirlari INPUT/OUTPUT/FORWARD, qoida tartibi, default-deny"
dars: 1
hafta: 6
sinf: 10-sinf-cyber
---

# 16-dars. Tarmoqlararo ekran va filtrlash (2-qism): Windows Defender Firewall va iptables da qoidalar yaratish

> Firewall nazariyasini bugun amalda sinaymiz: Windows da `netsh`, Linux da `iptables` bilan qoida yozamiz va xavfsiz tartibni o'rganamiz.

## Dars xulosasi

- Windows Firewall da 3 profil bor: Domain, Private, Public.
- `netsh advfirewall` bilan holat va qoidalar boshqariladi.
- iptables da 3 zanjir bor: INPUT, OUTPUT, FORWARD.
- `-A` qo'shadi, `-I` boshiga qo'yadi, `-D` o'chiradi, `-L` ko'rsatadi.
- Birinchi mos qoida ishlaydi: tartib muhim.
- `-P INPUT DROP` dan oldin SSH ga ruxsat bering.

## Qo'shimcha ma'lumot

### Profil
Windows qoidani tarmoq turiga qarab qo'llaydi: Public eng qattiq.

### conntrack
`ESTABLISHED,RELATED` mavjud ulanishlarga javoblarni o'tkazadi.

### REJECT
DROP dan farqli, yuboruvchiga rad xabarini qaytaradi.

### ufw
Ubuntu da iptables ustidagi oddiy qobiq.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Profil | Windows tarmoq rejimi |
| netsh | Windows tarmoq buyrug'i |
| iptables | Linux paket filtri |
| Zanjir | Qoidalar ro'yxati |
| ACCEPT | Ruxsat berish |
| DROP | Jimgina tashlash |
| Policy | Standart qoida |
| Loopback | Kompyuterning o'zi bilan aloqa |

## Bilasizmi?

- Windows Firewall qoidalari tarmoq profiliga qarab avtomatik almashadi.
- iptables o'rniga yangi Linux versiyalarida `nftables` ham ishlatiladi, mantiq o'xshash.
- Ubuntu da oddiyroq vosita bor: `ufw allow 22/tcp`.

## Topshiriqlar

### 1. Profillar · oson

Windows Firewall profillarini sanang.

**Kutiladigan natija:** Domain, Private, Public.

### 2. Zanjirlar · oson

iptables ning 3 zanjirini va vazifasini yozing.

**Kutiladigan natija:** INPUT, OUTPUT, FORWARD.

### 3. ALLOW/BLOCK · oson

`netsh` da ruxsat va taqiq qiymatlari qanday yoziladi?

**Kutiladigan natija:** `action=allow`, `action=block`.

### 4. -A va -I · oson

`-A` va `-I` farqini yozing.

**Kutiladigan natija:** `-A` oxiriga, `-I` boshiga.

### 5. Qoida o'qish · o'rta

`iptables -A INPUT -p tcp --dport 443 -j ACCEPT` nimani bildiradi?

**Kutiladigan natija:** Kiruvchi 443 (HTTPS) ga ruxsat.

### 6. DROP yoki REJECT · o'rta

DROP va REJECT ning farqini yozing.

**Kutiladigan natija:** DROP jim, REJECT rad javobi bilan.

### 7. Windows qoidasi · o'rta

3389 portiga kiruvchi TCP ni taqiqlovchi `netsh` qoidasini yozing.

**Kutiladigan natija:** `netsh advfirewall firewall add rule name="BlockRDP" dir=in action=block protocol=TCP localport=3389`

### 8. Tartib · o'rta

Qoidalar tartibi nega muhim? Misol keltiring.

**Kutiladigan natija:** Birinchi mos qoida ishlaydi; umumiy DROP birinchi bo'lsa ACCEPT ishlamaydi.

### 9. Default-deny · qiyin

Veb-server uchun (22, 80, 443) to'liq iptables qoidalarini yozing.

**Kutiladigan natija:** Loopback, ESTABLISHED, 22, 80, 443 ACCEPT; oxirida `-P INPUT DROP`.

### 10. O'zini bloklash · qiyin

Nega SSH ga ruxsatsiz `-P INPUT DROP` xavfli?

**Kutiladigan natija:** Joriy ulanish uziladi, serverga qayta kira olmaysiz.

### 11. Qoidani tekshirish · qiyin

Qoida ishlayotganini qanday tekshirasiz (Windows va Linux)?

**Kutiladigan natija:** `show rule` / `iptables -L -n -v` va brauzer yoki ping bilan sinov.

### 12. Hisobot · bonus

Laboratoriyada 1 ta qoida yaratib, sinab, hisobot yozing.

**Kutiladigan natija:** Qoida nomi, port, profil, natija.

## O'zingizni tekshiring

1. Windows Firewall profillari?
2. iptables zanjirlari?
3. `DROP` va `REJECT` farqi?
4. Qoida tartibi nega muhim?
5. `-P INPUT DROP` dan oldin nima kerak?
6. Qoida qanday saqlanadi?

## Uyga vazifa

Firewall qoidasini yarating va sinang (laboratoriyada). To'liq shart: `uyga-vazifa.md`.
