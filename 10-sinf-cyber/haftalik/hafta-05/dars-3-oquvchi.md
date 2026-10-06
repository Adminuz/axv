---
title: "Tarmoqlararo ekran va filtrlash (1-qism): Firewall turlari va ishlash prinsiplari"
description: "firewall, trusted va untrusted tarmoq, turlari, ACL, ALLOW, DENY, NAT, default-deny, UTM va NGFW"
dars: 3
hafta: 5
sinf: 10-sinf-cyber
---

# 15-dars. Tarmoqlararo ekran va filtrlash (1-qism): Firewall turlari va ishlash prinsiplari

> Mehmonxona kirish eshigida qo'riqchi bor: kimni kiritishni va kimni kiritmaslikni u hal qiladi. Tarmoqda bu vazifani firewall bajaradi.

## Dars xulosasi

- Firewall: trusted va untrusted tarmoqlar orasidagi trafikni filtrlaydi.
- Turlari: boshqariluvchi kommutator, paket filtri, holat inspektori, vositachi (proksi).
- Vositachi NAT orqali ichki manzillarni yashiradi; tatbiqiy proksi HTTP/FTP kontentini filtrlaydi.
- Filtr mezonlari: IP, domen, port, protokol.
- ACL qoidalari: ALLOW, DENY, NAT; default-deny eng xavfsiz yondashuv.
- UTM va NGFW: firewall, IDS/IPS, antivirus va ilova filtrini birlashtiradi.

## Qo'shimcha ma'lumot

### UTM va NGFW
UTM (Unified Threat Management) — perimetr himoyasining kompleks yechimi: firewall, IDS, antivirus, spamga qarshi modul. NGFW portlar bo'yicha filtrlashni, IPS ni va ilova sathidagi filtrlashni birlashtiradi.

### Tipik joylashuvlar
Perimetr (tarmoq chegarasida), ichki (segmentlar orasida) va shaxsiy (kompyuterda) firewall.

### Odatiy xatolar
Firewall ni «tezlik uchun» o'chirib qo'yish; tartibsiz qoidalar; default-deny ishlatmaslik.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Firewall | Tarmoqlararo ekran, xavfsizlik devori |
| Trusted tarmoq | Ishonchli (ichki) tarmoq |
| Untrusted tarmoq | Ishonchsiz (tashqi) tarmoq |
| ACL | Kirish boshqaruvi ro'yxati |
| Paket filtri | IP, port, protokol bo'yicha filtr |
| Stateful inspection | Ulanish holatini tekshirish |
| Proksi | Vositachi server |
| NAT | Manzil translyatsiyasi |
| UTM | Kompleks himoya qurilmasi |
| NGFW | Keyingi avlod firewall |

## Bilasizmi?

- Windows da firewall ni `netsh advfirewall set allprofiles state off` bilan o'chirish mumkin, lekin buni faqat sinov uchun qiling.
- Ko'p firewall lar tashqaridan kiruvchi ping ni standart bo'yicha taqiqlaydi.
- NGFW bir qurilmada firewall, IPS va ilova filtrini birlashtiradi.

## Topshiriqlar

### 1. Firewall ta'rifi · oson

Firewall nima? Bir jumlada yozing.

**Kutiladigan natija:** Aniq ta'rif.

### 2. Ko'rinishlar · oson

Apparat va dasturiy firewall ga bittadan misol yozing.

**Kutiladigan natija:** 2 misol.

### 3. Mezonlar · oson

Firewall filtr mezonlarini sanang.

**Kutiladigan natija:** 4 mezon.

### 4. Qoida turlari · oson

ALLOW, DENY va NAT nima qiladi?

**Kutiladigan natija:** 3 ta izoh.

### 5. Turni tanlang · o'rta

IP va port bo'yicha filtrlash uchun qaysi tur mos? Ilova kontenti uchun-chi?

**Kutiladigan natija:** 2 tur.

### 6. Qoidani o'qing · o'rta

`ALLOW IN ANY -> WebServer:443` nimani bildiradi?

**Kutiladigan natija:** Izoh.

### 7. Ping cheklovi · o'rta

`DENY IN ANY -> ANY (ICMP Echo Request)` nima qiladi? 12-dars bilan bog'lang.

**Kutiladigan natija:** Izoh.

### 8. Zaif protokollar · o'rta

Qaysi 3 ta protokolni taqiqlash tavsiya etiladi va nima uchun?

**Kutiladigan natija:** 3 protokol.

### 9. Default-deny qoidasi · qiyin

Kichik ofis uchun default-deny asosida 4 qatorli qoidalar to'plamini yozing.

**Kutiladigan natija:** 4 qator ACL.

### 10. Segment va firewall · qiyin

14-darsdagi 4 segmentdan serverlar segmentiga faqat o'qituvchilar segmentidan HTTPS ga ruxsat berish qoidasini yozing.

**Kutiladigan natija:** Qoida.

### 11. Xatoni toping · qiyin

Do'stingiz: «Firewall o'rnatdim, endi antivirus va ehtiyotkorlik kerak emas». Javob bering.

**Kutiladigan natija:** Rad etish.

### 12. Windows qoida · bonus

Laboratoriyada 80-port uchun kiruvchi qoida yaratib, ruxsat va taqiq holatlarida brauzerda sinang; hisobot yozing.

**Kutiladigan natija:** Skrinshotlar va hisobot.

## O'zingizni tekshiring

1. Firewall nima?
2. Trusted va untrusted tarmoq nima?
3. Firewall turlarini sanang.
4. ACL nima?
5. Default-deny nima?
6. NAT nima qiladi?
7. UTM va NGFW farqi nimada?

## Uyga vazifa

Firewall tushuntirishi, turlar jadvali va ACL yozish vazifalarini bajaring (25 daqiqa). To'liq shart: `uyga-vazifa.md`.
