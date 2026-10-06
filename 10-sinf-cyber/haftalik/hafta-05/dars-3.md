---
title: "Tarmoqlararo ekran va filtrlash (1-qism): Firewall turlari va ishlash prinsiplari"
description: "firewall, trusted va untrusted tarmoq, turlari, ACL, ALLOW, DENY, NAT, default-deny, UTM va NGFW"
dars: 3
hafta: 5
sinf: 10-sinf-cyber
---

# 15-dars. Tarmoqlararo ekran va filtrlash (1-qism): Firewall turlari va ishlash prinsiplari

**Manba:** O'quv qo'llanma, II bob, 2.4 «Tarmoqlararo ekran va filtrlash»; Uslubiy ko'rsatma, 2.4 (Windows Firewall); rasmiy o'quv dasturi.

## Dars rejasi (80 daqiqa)

1. **Takrorlash (8 daqiqa):** 14-dars: subnet va segmentatsiya
2. **Nazariy qism 1 (15 daqiqa):** Firewall nima, qayerda turadi, turlari
3. **Amaliyot 1 (15 daqiqa):** Windows Firewall holatini ko'rish va 80-port qoidasi
4. **Tanaffus (5 daqiqa).**
5. **Nazariy + amaliyot 2 (22 daqiqa):** Filtr mezonlari (IP, domen, port, protokol) va ACL misollari
6. **Xavfsizlik va xulosa (10 daqiqa):** Default-deny, xavfsiz bo'lmagan protokollar, UTM va NGFW
7. **Tezkor nazorat (5 daqiqa).**

**Kutiladigan natija:** Firewall ning vazifasini va trusted/untrusted tarmoqlar orasidagi o'rnini tushuntiradi; Firewall turlarini (paket filtri, holat inspektori, vositachi) OSI sathlari bilan moslaydi; ACL ko'rinishidagi ALLOW, DENY, NAT va default-deny qoidalarini o'qiydi va yozadi; Windows Firewall ni yoqish, o'chirish va port qoidasini yaratish bosqichlarini aytadi.

---

## Asosiy tushunchalar

- Firewall: trusted va untrusted tarmoqlar orasidagi trafikni filtrlaydi.
- Turlari: boshqariluvchi kommutator, paket filtri, holat inspektori, vositachi (proksi).
- Vositachi NAT orqali ichki manzillarni yashiradi; tatbiqiy proksi HTTP/FTP kontentini filtrlaydi.
- Filtr mezonlari: IP, domen, port, protokol.
- ACL qoidalari: ALLOW, DENY, NAT; default-deny eng xavfsiz yondashuv.
- UTM va NGFW: firewall, IDS/IPS, antivirus va ilova filtrini birlashtiradi.

---

## Dars mazmuni

### 1. Tarmoqlararo ekran va uning vazifasi

Tarmoqlararo ekran (firewall, brandmauer) — tarmoqqa kirayotgan va chiqayotgan trafikni nazorat qiluvchi apparat yoki dasturiy vosita. U trafikni qoidalar (filtrlar) bilan solishtirib, paketni o'tkazish yoki o'tkazmaslik haqida qaror qiladi. Asosiy vazifasi: **ishonchli (trusted)** va **ishonchsiz (untrusted)** tarmoqlar orasida «xavfsizlik devori» yaratish. Dasturiy firewall kompyuterga o'rnatiladi (uy, kichik ofis), apparat firewall esa tarmoq chegarasida turadi.

```bash
paket keldi
  qoidalar bilan solishtirish
    mos qoida bor  ->  ALLOW yoki DENY
    mos qoida yo'q ->  standart qoida (default)
```

Firewall tashqi hujumlardan, ruxsatsiz kirishdan va DoS hujumlaridan himoya qiladi, lekin foydalanuvchi e'tiborsizligini (95% hujum inson omiliga bog'liq) almashtirmaydi.

### 2. Tarmoqlararo ekran turlari

Firewall lar filtrlash texnologiyasi va OSI sathi bo'yicha tasniflanadi. **Kanal sathi:** boshqariluvchi kommutator (MAC, port bo'yicha). **Tarmoq sathi:** paket filtri (IP, port, protokol bo'yicha; IP almashtirish hujumiga zaif). **Seans sathi:** holat inspektori (stateful inspection) ulanish holatini kuzatadi, vositachi esa seans sathidagi (SOCKS5) bo'ladi. **Tatbiqiy sath:** tatbiqiy vositachi (proksi: HTTP/HTTPS, FTP), ilova kontenti bo'yicha filtrlaydi. Vositachi NAT orqali ichki manzillarni yashiradi.

```bash
Kanal sathi    boshqariluvchi kommutator (MAC, port)
Tarmoq sathi   paket filtri (IP, port, protokol)
Seans sathi    holat inspektori, SOCKS5 vositachisi
Tatbiqiy sath  HTTP/HTTPS, FTP proksi
```

Vositachida trafik qo'shimcha qurilmada qayta ishlanadi, shuning uchun unumdorlikni hisobga olish kerak; holat inspektori vositachisiz ishlaydi, tezlikni pasaytirmaydi.

### 3. Filtrlash qoidalari (ACL)

Filtrlash qoidalari firewall ning eng muhim qismi, ular **ACL (Access Control List)** deb ataladi. Mezonlar: IP manzil, domen nomi, port, protokol. Qoidalar kiruvchi va chiquvchi bo'ladi. Asosiy turlar: `ALLOW` (ruxsat), `DENY` (taqiq), `NAT` (manzil almashtirish). Eng xavfsiz yondashuv — **default-deny**: avval hammasi taqiqlanadi, keyin faqat kerakli xizmatlarga ruxsat beriladi. TFTP, Telnet, SNMP v1/v2, SMB, NetBIOS kabi zaif protokollar taqiqlanadi.

```bash
ALLOW IN ANY -> WebServer:80
ALLOW IN ANY -> WebServer:443
DENY  IN ANY -> InternalNet:22
DENY  IN ANY -> ANY (ICMP Echo Request)
NAT   OUT InternalNet -> Internet

DENY ALL
ALLOW kerakli_portlar
```

Windows da: `netsh advfirewall set allprofiles state on` yoqadi, `off` o'chiradi. Qoida: `firewall.cpl` > Qo'shimcha parametrlar > Kiruvchi qoidalar > Yangi qoida.

---

## Amaliy mashg'ulot

Windows da firewall holatini ko'ring (`netsh advfirewall show allprofiles state`), `firewall.cpl` orqali Qo'shimcha parametrlarni oching va 80-port uchun kiruvchi qoida yarating (faqat laboratoriya muhitida). Natijani va yaratilgan qoidani qisqa hisobotga yozing.

---

## Mustaqil topshiriqlar

### 1. Firewall ta'rifi · oson
Firewall nima? Bir jumlada yozing.
**Yechim:** Trafikni qoidalar bo'yicha nazorat qilib, ishonchli va ishonchsiz tarmoqlar orasida filtr bo'ladigan apparat yoki dasturiy vosita.

### 2. Ko'rinishlar · oson
Apparat va dasturiy firewall ga bittadan misol yozing.
**Yechim:** Dasturiy: Windows Firewall; apparat: tarmoq chegarasidagi firewall qurilmasi (UTM/NGFW).

### 3. Mezonlar · oson
Firewall filtr mezonlarini sanang.
**Yechim:** IP manzil, domen nomi, port, protokol.

### 4. Qoida turlari · oson
ALLOW, DENY va NAT nima qiladi?
**Yechim:** ALLOW ruxsat beradi, DENY taqiqlaydi, NAT ichki manzilni tashqi manzilga almashtiradi.

### 5. Turni tanlang · o'rta
IP va port bo'yicha filtrlash uchun qaysi tur mos? Ilova kontenti uchun-chi?
**Yechim:** Paket filtri (tarmoq sathi); tatbiqiy proksi (tatbiqiy sath).

### 6. Qoidani o'qing · o'rta
`ALLOW IN ANY -> WebServer:443` nimani bildiradi?
**Yechim:** Istalgan tashqi manbadan web-serverning 443 (HTTPS) portiga kirishga ruxsat.

### 7. Ping cheklovi · o'rta
`DENY IN ANY -> ANY (ICMP Echo Request)` nima qiladi? 12-dars bilan bog'lang.
**Yechim:** Tashqaridan kelgan ping so'rovlarini bloklaydi; shu sababli ping javobsiz qolishi hujum belgisi emas.

### 8. Zaif protokollar · o'rta
Qaysi 3 ta protokolni taqiqlash tavsiya etiladi va nima uchun?
**Yechim:** Telnet, TFTP, SNMP v1/v2 (yoki SMB, NetBIOS): ma'lumotni himoyasiz uzatadi yoki zaif.

### 9. Default-deny qoidasi · qiyin
Kichik ofis uchun default-deny asosida 4 qatorli qoidalar to'plamini yozing.
**Yechim:** DENY ALL; ALLOW IN ANY -> WebServer:443; ALLOW IN ANY -> WebServer:80; NAT OUT InternalNet -> Internet.

### 10. Segment va firewall · qiyin
14-darsdagi 4 segmentdan serverlar segmentiga faqat o'qituvchilar segmentidan HTTPS ga ruxsat berish qoidasini yozing.
**Yechim:** ALLOW 192.168.10.64/26 -> 192.168.10.192/26:443; boshqa hammasi DENY.

### 11. Xatoni toping · qiyin
Do'stingiz: «Firewall o'rnatdim, endi antivirus va ehtiyotkorlik kerak emas». Javob bering.
**Yechim:** Xato: firewall faqat trafikni filtrlaydi; 95% hujum inson omiliga bog'liq, shuning uchun antivirus va ehtiyotkorlik ham zarur.

### 12. Windows qoida · bonus
Laboratoriyada 80-port uchun kiruvchi qoida yaratib, ruxsat va taqiq holatlarida brauzerda sinang; hisobot yozing.
**Yechim:** Taqiq holatida sahifa ochilmaydi, qoida o'chirilgach ochiladi; hisobotda qoida nomi, port va profil ko'rsatiladi.

---

## Tezkor savol-javob

1. **Savol:** Firewall nima? **Javob:** Trafikni qoidalar bo'yicha nazorat qiluvchi apparat yoki dasturiy vosita.
2. **Savol:** ACL nima? **Javob:** Kirish boshqaruvi ro'yxati: ALLOW va DENY qoidalari to'plami.
3. **Savol:** Paket filtri nimaga qaraydi? **Javob:** IP manzil, port va protokolga.
4. **Savol:** Default-deny nima? **Javob:** Hammasini taqiqlab, faqat kerakli xizmatlarga ruxsat berish.
5. **Savol:** NAT nima qiladi? **Javob:** Ichki manzillarni tashqi tomondan yashiradi va bitta manzil orqali chiqaradi.

---

## Mentor uchun eslatma

- Firewall sozlashni faqat laboratoriya kompyuterida bajaring; ish kompyuterida firewall ni uzoq o'chirib qo'ymang.
- Windows interfeysi rus tilida bo'lsa, qo'llanmadagi nomlarni (Дополнительные параметры, Правила для входящих подключений) ko'rsatib o'ting.
- `netsh` buyruqlari administrator CMD da bajariladi.
- Iptables bilan qoidalar yaratish 16-darsda o'tiladi.
- ICMP (ping) cheklovi 12-dars bilan bog'lanadi: `DENY IN ANY -> ANY (ICMP Echo Request)`.
