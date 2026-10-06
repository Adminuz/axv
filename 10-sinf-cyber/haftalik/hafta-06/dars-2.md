---
title: "Tarmoqlarda VPN qurish va shifrlash (1-qism): VPN arxitekturasi, tunnellash va IPsec protokoli"
description: "VPN maqsadi, shifrlash, tunnellash va inkapsulyatsiya, VPN turlari, IPsec transport va tunnel rejimlari"
dars: 2
hafta: 6
sinf: 10-sinf-cyber
---

# 17-dars. Tarmoqlarda VPN qurish va shifrlash (1-qism): VPN arxitekturasi, tunnellash va IPsec protokoli

**Manba:** O'quv qo'llanma II bob: «Shifrlash tushunchasi», «Tunellash tushunchasi», «VPN vositasi va uning asosiy maqsadi», 2.2-jadval, «VPN vositalarining tasnifi»; rasmiy o'quv dasturi. IPsec ESP/AH, IKE tafsilotlari standart bilimdan qo'shildi.

## Dars rejasi (80 daqiqa)

1. **Takrorlash (8 daqiqa):** 16-dars: firewall qoidalari
2. **Nazariy qism 1 (15 daqiqa):** IP ning ochiqligi, shifrlash turlari
3. **Amaliyot 1 (15 daqiqa):** Tunnellash: paketni paket ichiga o'rash chizmasi
4. **Tanaffus (5 daqiqa).**
5. **Nazariy + amaliyot 2 (22 daqiqa):** VPN turlari va OSI sathlari bo'yicha protokollar (2.2-jadval)
6. **Xavfsizlik va xulosa (10 daqiqa):** IPsec rejimlari, xavfsizlik va xulosa
7. **Tezkor nazorat (5 daqiqa).**

**Kutiladigan natija:** IP paketlari ochiq uzatilishi va VPN nima uchun kerakligini tushuntiradi; Simmetrik va assimetrik shifrlashni farqlaydi; Tunnellash va inkapsulyatsiyani chizadi; Remote Access va Site-to-Site VPN ni ajratadi; IPsec ning transport va tunnel rejimlarini solishtiradi.

---

## Asosiy tushunchalar

- IP paketlari ochiq uzatiladi, konfidensiallik yo'q.
- Shifrlash simmetrik (bir kalit) va assimetrik (kalit jufti) bo'ladi.
- Tunnellash — paketni boshqa paket ichiga o'rash (inkapsulyatsiya).
- VPN = tunnel + shifrlash + autentifikatsiya + yaxlitlik.
- Turlari: Remote Access, Site-to-Site, Client-Based, Clientless.
- IPsec: transport (hostlar) va tunnel (filiallar) rejimlari.

---

## Dars mazmuni

### 1. IP ochiqligi va shifrlash

**IP protokoli konfidensiallikni ta'minlamaydi**: paketlar ochiq holda uzatiladi, ularni yo'ldagi istalgan router yoki sniffer o'qiy oladi. Parollar va maxfiy trafik oshkor bo'lishi mumkin. Yechim: **shifrlash** (plaintext → ciphertext) va VPN. Shifrlash 2 xil: **simmetrik** (bir kalit ham yopadi, ham ochadi; tez, katta hajm uchun) va **assimetrik** (ochiq va shaxsiy kalit jufti; autentifikatsiyani kuchaytiradi). Shifrlash maxfiylikdan tashqari yaxlitlik va manba haqiqiyligini ham tekshiradi.

```python
kalit = 3
matn = "SALOM"
shifr = "".join(chr((ord(c) - 65 + kalit) % 26 + 65) for c in matn)
asl = "".join(chr((ord(c) - 65 - kalit) % 26 + 65) for c in shifr)
print(shifr, asl)
```

Bu faqat g'oyani ko'rsatuvchi qadimiy Sezar shifri; real tizimlar AES kabi algoritmlarni ishlatadi.

Bir kalit yopadi va ochadi — bu simmetrik shifrlash. Real himoyada Sezar shifri ishlatilmaydi.

### 2. Tunnellash va VPN tushunchasi

**Tunnellash** — bir protokol ma'lumotini boshqa protokol ichiga joylab, alohida mantiqiy kanal orqali uzatish. Asl paket tashqi ko'rinishda boshqa protokolga o'xshaydi, qabul qiluvchi uni qayta ochadi. Bu **inkapsulyatsiya**. **VPN** (virtual xususiy tarmoq) — inkapsulyatsiya, autentifikatsiya, shifrlash va yaxlitlik nazorati asosida vaqtinchalik himoyalangan kanal. Ijaraga olingan doimiy liniyadan farqli, tunnel faqat seans davrida quriladi, shuning uchun arzonroq.

```text
[Tashqi IP sarlavha][Tunnel sarlavhasi][ Shifrlangan asl paket ]
      Internet ko'radi          ichkarida: asl IP + ma'lumot
```

Tunnel odatda shifrlanadi yoki autentifikatsiya bilan himoyalanadi, lekin tunnelning o'zi har doim ham shifrlamaydi.

### 3. VPN turlari, IPsec transport va tunnel rejimi

VPN turlari: **Remote Access** (xodim ofis resurslariga masofadan ulanadi), **Site-to-Site** (filiallar tarmog'i birlashadi, odatda IPsec), **Client-Based** (qurilmada mijoz dasturi) va **Clientless** (brauzer, SSL/TLS). OSI bo'yicha: seans — SOCKS, transport — SSH va SSL/TLS, tarmoq — **IPsec (ESP)**, kanal — L2TP va PPTP. **IPsec** 2 rejimda ishlaydi: **transport** (hostlar orasida, faqat ma'lumot qismi shifrlanadi, masalan L2TP ni himoyalash) va **tunnel** (butun paket sarlavhasi bilan shifrlanib, yangi paket ichiga joylanadi; filiallar orasida).

```python
def rejim(ulanish):
    if ulanish == "host-host":
        return "transport"
    if ulanish == "ofis-ofis":
        return "tunnel"
    return "noma'lum"

print(rejim("ofis-ofis"))
```

PPTP (MPPE/RC4) eskirgan va zaif hisoblanadi; zamonaviy amaliyotda IPsec/IKEv2, OpenVPN va WireGuard ishlatiladi.

---

## Amaliy mashg'ulot

Daftarda ikki ofis (Toshkent va Samarqand) va ular orasidagi internetni chizing, tunnel paketining qismlarini belgilang. Keyin 2.2-jadvaldagi protokollarni OSI sathlari bo'yicha qayta yozing va har biriga qaysi VPN turi mosligini ko'rsating. Ixtiyoriy: Wireshark da oddiy HTTP va HTTPS paketlarini solishtirib, ma'lumot ochiq yoki shifrlanganini ko'ring (faqat o'z tarmog'ingizda).

---

## Mustaqil topshiriqlar

### 1. IP muammosi · oson
IP protokolining xavfsizlikdagi 2 ta kamchiligini yozing.
**Yechim:** Shifrlash yo'q (ochiq paketlar); marshrutlash/DoS hujumlariga zaif.

### 2. VPN ta'rifi · oson
VPN ni o'z so'zingiz bilan ta'riflang.
**Yechim:** Himoyalangan vaqtinchalik kanal.

### 3. Shifr turlari · oson
Simmetrik va assimetrik shifrlashni solishtiring.
**Yechim:** 1 kalit va kalit jufti.

### 4. VPN turlari · oson
4 ta VPN turini sanang.
**Yechim:** Remote Access, Site-to-Site, Client-Based, Clientless.

### 5. Remote yoki Site · o'rta
Ikki filial bog'lanadi: qaysi tur?
**Yechim:** Site-to-Site.

### 6. OSI sathlari · o'rta
IPsec, L2TP va SSH qaysi sathga tegishli?
**Yechim:** IPsec — tarmoq, L2TP — kanal, SSH — transport.

### 7. Inkapsulyatsiya · o'rta
Inkapsulyatsiyani misol bilan tushuntiring.
**Yechim:** Asl paket yangi sarlavha ichida.

### 8. Tunnel shifrlaydimi · o'rta
Tunnel har doim shifrlaydimi?
**Yechim:** Yo'q, lekin odatda shifrlanadi.

### 9. IPsec rejimi · qiyin
Host-host va ofis-ofis uchun rejimlarni tanlang va asoslang.
**Yechim:** Transport va tunnel.

### 10. Tunnel chizmasi · qiyin
Tunnel paketining qismlarini chizib bering.
**Yechim:** Tashqi sarlavha + tunnel + shifrlangan paket.

### 11. Protokol tanlash · qiyin
Nega zamonaviy tizimlar PPTP o'rniga IPsec yoki WireGuard ishlatadi?
**Yechim:** PPTP shifri (RC4) zaif.

### 12. Wireshark · bonus
HTTP va HTTPS paketini solishtiring.
**Yechim:** HTTP ochiq, HTTPS shifrlangan.

---

## Tezkor savol-javob

1. **Savol:** IP protokoli nega xavfsiz emas? **Javob:** Paketlar ochiq uzatiladi, konfidensiallik yo'q.
2. **Savol:** Simmetrik shifrlash nima? **Javob:** Bitta kalit ham shifrlaydi, ham deshifrlaydi.
3. **Savol:** Tunnellash nima? **Javob:** Paketni boshqa protokol ichiga o'rab uzatish.
4. **Savol:** Site-to-Site VPN nima? **Javob:** Ikki yoki ko'p filial tarmog'ini bog'laydi.
5. **Savol:** IPsec rejimlari? **Javob:** Transport va tunnel.

---

## Mentor uchun eslatma

- Dars nazariy: chizma va muhokama muhim, tunnel paketini doskada chizing.
- Sezar shifri faqat g'oya uchun; real tizimlar AES ishlatishini ayting.
- Qo'llanmada IPsec batafsil sozlanmaydi, faqat rejimlar tushuntiriladi; ESP/AH va IKE tafsilotlari qo'shimcha bilim (standart).
- Wireshark namoyishi faqat o'z tarmog'ida; boshqalar trafigini tinglash taqiqlanishini ta'kidlang.
- Keyingi dars: WireGuard va OpenVPN amaliyoti.
