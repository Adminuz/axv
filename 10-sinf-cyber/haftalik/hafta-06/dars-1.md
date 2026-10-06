---
title: "Tarmoqlararo ekran va filtrlash (2-qism): Windows Defender Firewall va iptables da qoidalar yaratish"
description: "netsh advfirewall, profillar, iptables zanjirlari INPUT/OUTPUT/FORWARD, qoida tartibi, default-deny"
dars: 1
hafta: 6
sinf: 10-sinf-cyber
---

# 16-dars. Tarmoqlararo ekran va filtrlash (2-qism): Windows Defender Firewall va iptables da qoidalar yaratish

**Manba:** O'quv qo'llanma II bob 2.4 (Windows Firewall, profillar Private/Public/Domain, Linux tarmoq xavfsizligi); Uslubiy ko'rsatma 2.4; rasmiy o'quv dasturi. `netsh` va `iptables` buyruq sintaksisi standart hujjatlardan qo'shildi.

## Dars rejasi (80 daqiqa)

1. **Takrorlash (8 daqiqa):** 15-dars: firewall turlari, ACL, default-deny
2. **Nazariy qism 1 (15 daqiqa):** Windows Defender Firewall: profillar, `netsh advfirewall`
3. **Amaliyot 1 (15 daqiqa):** Windows da 80-port uchun qoida yaratish va sinash
4. **Tanaffus (5 daqiqa).**
5. **Nazariy + amaliyot 2 (22 daqiqa):** iptables: zanjirlar, `-A`, `-I`, `-D`, `-L`, default-deny
6. **Xavfsizlik va xulosa (10 daqiqa):** Xavfsizlik: SSH ni yo'qotmaslik, qoida tartibi, saqlash
7. **Tezkor nazorat (5 daqiqa).**

**Kutiladigan natija:** Firewall profillarini (Domain, Private, Public) sanaydi; `netsh advfirewall` bilan holatni ko'radi va 80-port qoidasini yaratadi; iptables ning INPUT, OUTPUT, FORWARD zanjirlarini farqlaydi; `iptables -A` bilan ALLOW qoidalari va `-P INPUT DROP` bilan default-deny yozadi; Qoida tartibi (birinchi mos qoida ishlaydi) va SSH ni bloklab qo'yish xavfini tushuntiradi.

---

## Asosiy tushunchalar

- Windows Firewall da 3 profil bor: Domain, Private, Public.
- `netsh advfirewall` bilan holat va qoidalar boshqariladi.
- iptables da 3 zanjir bor: INPUT, OUTPUT, FORWARD.
- `-A` qo'shadi, `-I` boshiga qo'yadi, `-D` o'chiradi, `-L` ko'rsatadi.
- Birinchi mos qoida ishlaydi: tartib muhim.
- `-P INPUT DROP` dan oldin SSH ga ruxsat bering.

---

## Dars mazmuni

### 1. Windows Firewall va netsh advfirewall

Windows Firewall kiruvchi va chiquvchi trafikni filtrlaydi, portlar va protokollarni boshqaradi. Qoidalar **profilga** qarab qo'llanadi: **Domain** (korxona tarmog'i), **Private** (uy yoki ishonchli tarmoq), **Public** (kafe, aeroport, eng qattiq). Boshqarish: `firewall.cpl` (grafik) yoki administrator CMD da **`netsh advfirewall`**. Qoida yaratishda yo'nalish (`dir=in` kiruvchi, `dir=out` chiquvchi), harakat (`allow` yoki `block`), protokol va port ko'rsatiladi.

```bash
netsh advfirewall show allprofiles state
netsh advfirewall firewall add rule name="Web80" dir=in action=allow protocol=TCP localport=80
netsh advfirewall firewall show rule name="Web80"
netsh advfirewall firewall delete rule name="Web80"
```

`netsh` buyruqlari administrator CMD da bajariladi. Faqat laboratoriya kompyuterida sinang; firewall ni uzoq o'chirib qo'ymang.

### 2. iptables: zanjirlar va qoidalar

Linux da paketlarni filtrlash yadro darajasida ishlaydi, uni **`iptables`** boshqaradi. Asosiy `filter` jadvalida 3 zanjir bor: **INPUT** (shu kompyuterga kelayotgan), **OUTPUT** (shu kompyuterdan chiqayotgan), **FORWARD** (orqali o'tayotgan). Qoida: `-A` (oxiriga qo'shish), `-I` (boshiga qo'yish), `-D` (o'chirish), `-L` (ro'yxat). Mezonlar: `-p tcp`, `--dport 80`, `-s` manba IP. Harakat `-j`: `ACCEPT` (ruxsat), `DROP` (jimgina tashlash), `REJECT` (rad javobi bilan). Buyruqlar `sudo` bilan beriladi.

```bash
sudo iptables -L -n -v --line-numbers
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
```

2–3-qatorlar: lokal (loopback) va allaqachon o'rnatilgan ulanishlarga ruxsat. Busiz ichki aloqa va javoblar to'xtab qoladi.

### 3. Qoida tartibi va default-deny

iptables da **birinchi mos kelgan qoida** ishlaydi, shuning uchun tartib hal qiluvchi: umumiy `DROP` ni konkret `ACCEPT` dan oldin qo'ysangiz, ruxsat ishlamaydi. **Default-deny** ni `-P INPUT DROP` (policy) bilan o'rnatamiz: hamma narsa taqiqlanadi, ruxsat berilganlari bundan mustasno. Muhim ogohlantirish: masofadan (SSH) ishlayotgan bo'lsangiz, avval `--dport 22` ga **ruxsat bering**, keyin policy ni `DROP` qiling, aks holda o'zingizni serverdan chiqarib yuborasiz. Qoidalar qayta ishga tushganda yo'qoladi: `iptables-save` bilan saqlanadi.

```bash
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -P INPUT DROP
sudo iptables -D INPUT 4
sudo iptables-save > rules.v4
```

Avval ruxsat, keyin `-P INPUT DROP`. Tajribani virtual mashinada qiling; xato bo'lsa `sudo iptables -F` va `-P INPUT ACCEPT` bilan qaytarasiz.

---

## Amaliy mashg'ulot

Laboratoriya kompyuterida administrator CMD da `netsh advfirewall show allprofiles state` ni bajaring, `Web80` nomli 80-port kiruvchi qoidasini yarating, `show rule` bilan tekshiring va keyin o'chiring. Virtual Linux mashinada `iptables -L -n -v` ni ko'ring, loopback, ESTABLISHED, 22 va 80 portlariga ruxsat yozing va oxirida `-P INPUT DROP` ni sinang. Natijani qisqa hisobotga yozing.

---

## Mustaqil topshiriqlar

### 1. Profillar · oson
Windows Firewall profillarini sanang.
**Yechim:** Domain, Private, Public.

### 2. Zanjirlar · oson
iptables ning 3 zanjirini va vazifasini yozing.
**Yechim:** INPUT, OUTPUT, FORWARD.

### 3. ALLOW/BLOCK · oson
`netsh` da ruxsat va taqiq qiymatlari qanday yoziladi?
**Yechim:** `action=allow`, `action=block`.

### 4. -A va -I · oson
`-A` va `-I` farqini yozing.
**Yechim:** `-A` oxiriga, `-I` boshiga.

### 5. Qoida o'qish · o'rta
`iptables -A INPUT -p tcp --dport 443 -j ACCEPT` nimani bildiradi?
**Yechim:** Kiruvchi 443 (HTTPS) ga ruxsat.

### 6. DROP yoki REJECT · o'rta
DROP va REJECT ning farqini yozing.
**Yechim:** DROP jim, REJECT rad javobi bilan.

### 7. Windows qoidasi · o'rta
3389 portiga kiruvchi TCP ni taqiqlovchi `netsh` qoidasini yozing.
**Yechim:** `netsh advfirewall firewall add rule name="BlockRDP" dir=in action=block protocol=TCP localport=3389`

### 8. Tartib · o'rta
Qoidalar tartibi nega muhim? Misol keltiring.
**Yechim:** Birinchi mos qoida ishlaydi; umumiy DROP birinchi bo'lsa ACCEPT ishlamaydi.

### 9. Default-deny · qiyin
Veb-server uchun (22, 80, 443) to'liq iptables qoidalarini yozing.
**Yechim:** Loopback, ESTABLISHED, 22, 80, 443 ACCEPT; oxirida `-P INPUT DROP`.

### 10. O'zini bloklash · qiyin
Nega SSH ga ruxsatsiz `-P INPUT DROP` xavfli?
**Yechim:** Joriy ulanish uziladi, serverga qayta kira olmaysiz.

### 11. Qoidani tekshirish · qiyin
Qoida ishlayotganini qanday tekshirasiz (Windows va Linux)?
**Yechim:** `show rule` / `iptables -L -n -v` va brauzer yoki ping bilan sinov.

### 12. Hisobot · bonus
Laboratoriyada 1 ta qoida yaratib, sinab, hisobot yozing.
**Yechim:** Qoida nomi, port, profil, natija.

---

## Tezkor savol-javob

1. **Savol:** Windows Firewall profillari? **Javob:** Domain, Private, Public.
2. **Savol:** iptables zanjirlari? **Javob:** INPUT, OUTPUT, FORWARD.
3. **Savol:** `DROP` va `REJECT` farqi? **Javob:** DROP jimgina tashlaydi; REJECT rad javobini yuboradi.
4. **Savol:** Qoida tartibi nega muhim? **Javob:** Birinchi mos qoida ishlaydi.
5. **Savol:** `-P INPUT DROP` dan oldin nima kerak? **Javob:** SSH (22) ga ruxsat.

---

## Mentor uchun eslatma

- Firewall sozlashni faqat laboratoriya kompyuteri yoki virtual mashinada bajaring.
- `netsh` buyruqlari administrator CMD da ishlaydi; interfeys rus tilida bo'lsa nomlarni ko'rsatib o'ting.
- `iptables -P INPUT DROP` dan oldin 22-portga ruxsat bo'lishini tekshiring; masofaviy VM da buni o'quvchilarga alohida eslating.
- iptables qoidalari qayta ishga tushganda yo'qoladi: `iptables-save` ni ko'rsating.
- Qo'llanmada konkret iptables buyruqlari yo'q; ular standart hujjatlardan qo'shildi, mavzuning umumiy mantiqi (ALLOW/DENY, profillar) qo'llanmaga tayanadi.
