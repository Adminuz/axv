# 6-hafta: Uyga vazifa

**Fan:** Kiberxavfsizlik  
**Sinf:** 10-sinf  
**Hafta:** 6-hafta  
**Topshirish muddati:** Keyingi darsga qadar (7-hafta, 1-dars)

---

## Topshiriq 1: Firewall qoidalari · qiyin

1. Laboratoriyada `Web80` qoidasini yaratib, sinab va o'chirib, 3 qatorli hisobot yozing.
2. Virtual Linux da loopback, ESTABLISHED, 22 va 80 ga ruxsat beruvchi iptables qoidalarini yozing (ishga tushirishdan oldin mentorga ko'rsating).
3. `DROP` ni ACCEPT dan oldin qo'yish xatosini 3 jumlada tushuntiring.

---

## Topshiriq 2: VPN va IPsec · o'rta

1. Ikki ofis orasida tunnel chizmasini chizing va qismlarini belgilang.
2. VPN turlari (4 ta) uchun har biriga bittadan hayotiy misol yozing.
3. IPsec transport va tunnel rejimi farqini 4 jumlada yozing.

---

## Topshiriq 3: WireGuard va OpenVPN · oson

1. VM da WireGuard kalit juftini yarating va namunaviy `wg0.conf` yozing (haqiqiy kalitni yubormang).
2. `.ovpn` fayl qatorlarini daftarga izohlab yozing.
3. WireGuard, OpenVPN va IPsec ni 3 ustunli jadvalda solishtiring.

---

## Baholash mezoni

| Mezon | Ball |
|---|---|
| 16-dars: Firewall qoidalarini yaratish | 3 |
| 17-dars: VPN va IPsec tushunchalari | 3 |
| 18-dars: WireGuard va OpenVPN sozlash | 2 |
| Toza, o'z vaqtida va mustaqil bajarilgan | 2 |
| **Jami** | **10** |
| Bonus: bonus darajadagi topshiriq | +2 |

---

## Mentor uchun

**Tekshirish:**
- 16-dars: -P INPUT DROP dan oldin nima kerak?? Javobi: SSH (22) ga ruxsat.
- 17-dars: IPsec rejimlari?? Javobi: Transport va tunnel.
- 18-dars: Tunnelni qanday tekshirasiz?? Javobi: wg show va ping.

**Keng tarqalgan xatolar:**
- 16-dars: Umumiy DROP ni konkret ACCEPT dan oldin qo'yish.
- 17-dars: VPN va shifrlashni bir narsa deb o'ylash: VPN tunnel + shifr + autentifikatsiya.
- 18-dars: Shaxsiy kalitni boshqaga yuborish yoki GitHub ga qo'yish.
