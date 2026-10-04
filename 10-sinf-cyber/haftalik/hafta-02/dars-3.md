---
title: "Xavfsizlikni anglash (1-qism): xavfsizlik tafakkuri va kuchli parollar siyosati"
description: "Security Mindset tamoyillari (Adversarial va Defensive thinking) hamda Nmap va Hydra yordamida zaifliklar va parollarni tekshirish"
dars: 3
hafta: 2
sinf: 10-sinf-cyber
---

# 6-dars. Xavfsizlikni anglash (1-qism): xavfsizlik tafakkuri va kuchli parollar siyosati

## Dars rejasi (80 daqiqa)

1. **Kirish va takrorlash (10 daqiqa):** MITM va CIA triadasi bo'yicha tezkor savol-javob, yangi dars maqsadlari.
2. **Nazariy qism (25 daqiqa):**
   - **Xavfsizlik tafakkuri (Security Mindset):** nima uchun oddiy dasturchi va xavfsizlik muhandisi tizimga turlicha qaraydi?
   - Bryus Shnayerning xavfsizlik tafakkuri haqidagi qarashlari.
   - Xavfsizlik tafakkurining 5 ta tamoyili:
     1. *What could go wrong?* (Nima noto'g'ri bo'lishi mumkin?);
     2. *Adversarial thinking* (Hujumchi kabi fikrlash);
     3. *Defensive thinking* (Himoyachi kabi fikrlash);
     4. *Assume breach* (Tizim allaqachon buzilgan deb faraz qilish);
     5. *Know your assets* (O'z aktivlaringni aniq bilish).
   - Dunyodagi «ko'nikmalar bo'shlig'i» (Skills Gap — 2.72 million mutaxassis yetishmovchiligi).
   - Zaif parollar xavfi: Brute-force va Dictionary (lug'at) hujumlari.
   - Kuchli parol mezonlari va Parol menejerlari (Bitwarden, KeePass).
3. **Amaliy laboratoriya mashg'uloti (30 daqiqa):**
   - Nmap vositasi yordamida tarmoqdagi ochiq portlar va xizmatlarni skanerlash (`nmap -sV -p- --open <IP>`).
   - Hydra vositasi orqali zaif parolni lug'at hujumi yordamida sinash (`hydra -l windows -P rockyou.txt ...`).
   - Parol xavfsizligini tekshirish (Kaspersky Password Checker, haveibeenpwned.com).
4. **Mustaqil topshiriqlar va muhokama (10 daqiqa):** 10 ta amaliy vazifani yechish.
5. **Xulosa va baholash (5 daqiqa):** Dars natijalari va haftalik xulosa.

---

## Asosiy tushunchalar

- **Xavfsizlik tafakkuri (Security Mindset):** Har qanday dastur, tizim, tarmoq yoki inson harakatini potensial zaiflik va xavf-xatar nuqtai nazaridan baholash, tizimning eng zaif bo'g'inini oldindan ko'ra bilish qobiliyati.
- **Hujumchi kabi fikrlash (Adversarial Thinking):** «Bu tizimni qanday qilib buzish, qoidalarni qanday aylanib o'tish va himoyani aldash mumkin?» deb fikrlash.
- **Himoyachi kabi fikrlash (Defensive Thinking):** Tizimni qatlamli himoya (Defense-in-Depth) bilan loyihalash, xatolik ehtimolini minimal darajaga tushirish va «buzilgan taqdirda ham zarar cheklansin» tamoyiliga tayanish.
- **Assume Breach (Buzilgan deb hisoblash):** Ichki tarmoq yoki server allaqachon buzg'unchi nazorati ostida degan faraz bilan har bir so'rovni qat'iy tekshirish (Zero Trust arxitekturasi).
- **Brute-Force hujumi:** Barcha mumkin bo'lgan belgilar kombinatsiyalarini ketma-ket avtomatik sinab ko'rish orqali parolni topish usuli.
- **Lug'at hujumi (Dictionary Attack):** Oldindan tayyorlangan eng mashhur parollar ro'yxati (masalan, `rockyou.txt` — 14 millionta parol) orqali tezkor tekshiruv.
- **Nmap (Network Mapper):** Tarmoqdagi kompyuterlar, ochiq portlar, ishlayotgan xizmatlar va operatsion tizim turlarini skanerlovchi global standart vosita.
- **Hydra:** Tarmoq protokollari (SSH, FTP, RDP, HTTP, Telnet) orqali parollarni juda tezkor lug'at hujumi bilan tekshiruvchi vosita.

---

## Dars mazmuni

### 1. Oddiy foydalanuvchi vs Xavfsizlik tafakkuri

| Holat | Oddiy foydalanuvchi | Xavfsizlik tafakkuriga ega mutaxassis |
|---|---|---|
| **Wi-Fi tarmog'i** | «Wi-Fi ga parol qo'yilgan, demak xavfsiz.» | «WPA2 yoki WPA3 ishlatilganmi? Routerning admin paroli o'zgartirilganmi? WPS o'chirilganmi? Izolatsiya bormi?» |
| **Veb-sayt login formasi** | «Login va parolni kiritadigan joy.» | «SQL Injection bormi? Brute-force dan rate-limiting himoyasi bormi? Parol xeshlanib saqlanadimi?» |
| **Pochta xati** | «Kompaniya direktori yozibdi, faylni ochay.» | «Jo'natuvchi domeni haqiqiymi? SPF/DKIM to'g'rimi? Nega rahbar favqulodda pul so'ramoqda?» |

> «Xavfsizlik o'ziga xos fikrlash tarzini talab qiladi. Yaxshi mutaxassislar do'konga kirsa qanday o'g'irlik qilish mumkinligini, kompyuter ko'rsa qanday zaiflik borligini o'ylamasdan turolmaydilar.» — **Bryus Shnayer**

---

### 2. Zaif parollar va portlar muammosi

Kiberjinoyatchilar ko'pincha murakkab ekspluatlar yaratishga vaqt sarflamaydi. Eng keng tarqalgan zaiflik — bu **standart zaif parollar** va **ochiq qoldirilgan xizmat portlari**:
- `admin / admin`, `123456`, `qwerty`, `password` kabi parollar Hydra yordamida bir necha soniyada topiladi.
- Serverlarda keraksiz ochiq qoldirilgan portlar:
  - 21 — FTP (shifrlanmagan fayl almashinuvi);
  - 23 — Telnet (shifrlanmagan ochiq buyruqlar satri);
  - 3389 — RDP (masofaviy ish stoli, ochiq qolsa butun dunyo xakerlari sinab ko'radi);
  - 445 — SMB (EternalBlue va ransomware hujumlari nishoni).

---

## Amaliy laboratoriya mashg'uloti

> [!CAUTION]
> Ushbu mashg'ulot faqat o'quv laboratoriyasi virtual mashinalarida (masalan, 172.16.4.65) o'tkaziladi. Begona IP manzillarni skanerlash va parollarni sinash noqonuniy hisoblanadi.

### 1-qadam: Nmap yordamida ochiq portlarni aniqlash
Kali Linux terminalida nishon mashinani (masalan, Windows 10 yoki Ubuntu server) to'liq skanerlash:
```bash
sudo nmap -sV -p- --open 172.16.4.65
```
**Buyruq parametrlari:**
- `-sV`: Portda ishlayotgan xizmatning versiyasini aniqlash (Service Version);
- `-p-`: Barcha 65535 ta portni to'liq tekshirish;
- `--open`: Faqat ochiq (open) bo'lgan portlarni ko'rsatish.

### 2-qadam: Hydra yordamida zaif parolni aniqlash
Windows RDP (3389-port) xizmati uchun `rockyou.txt` lug'ati yordamida parolni tekshirish:
```bash
hydra -l windows -P /usr/share/wordlists/rockyou.txt -t 4 -V -f rdp://172.16.4.65
```
**Parametrlar:**
- `-l windows`: Foydalanuvchi nomi (`windows`);
- `-P ...`: Parollar lug'ati fayli yo'li;
- `-t 4`: 4 ta parallel oqimda sinash;
- `-V`: Har bir sinovni ekranda batafsil ko'rsatish;
- `-f`: To'g'ri parol topilishi bilan dasturni to'xtatish.

### 3-qadam: Kuchli parol mezonlari va parol menejeri
1. **Parol uzunligi:** Kamida 12-16 ta belgi bo'lishi shart;
2. **Kombinatsiya:** Katta harf (A-Z), kichik harf (a-z), sonlar (0-9) va maxsus belgilar (`!@#$%^&*`);
3. **Unikallik:** Har bir veb-sayt uchun alohida boshqa parol!
4. **Parol menejeri (Bitwarden / KeePass):** Faqat bitta asosiy (Master) parolni yodda saqlash, qolgan barcha saytlar uchun 20-25 belgili tasodifiy murakkab parollarni menejerga ishonish.

---

## Mustaqil topshiriqlar

### 1. Xavfsizlik tafakkurining 5 tamoyili · oson
Xavfsizlik tafakkurini tashkil etuvchi 5 ta asosiy tamoyilni sanang va har birining ma'nosini bitta jumla bilan yozing.
**Yechim:**
1. What could go wrong? — tizimda qanday kutilmagan xatolik yuz berishi mumkinligini doimiy baholash;
2. Adversarial thinking — hujumchi nuqtai nazaridan tizim zaifliklarini izlash;
3. Defensive thinking — qatlamli himoya mexanizmlarini loyihalash;
4. Assume breach — tizim ichkarisiga allaqachon buzg'unchi kirgan degan faraz bilan harakat qilish;
5. Know your assets — nimalarni himoya qilish kerakligini aniq inventarizatsiya qilish.

### 2. Oddiy odam va mutaxassis nigohi · oson
Do'kondagi bepul jamoat Wi-Fi tarmog'iga oddiy odam qanday qaraydi va kiberxavfsizlik mutaxassisi qanday ko'z bilan qaraydi?
**Yechim:** Oddiy odam: «Zo'r, bepul internet bor, paroli ham yo'q, xohlagancha ishlatish mumkin» deb qaraydi. Mutaxassis esa: «Bu tarmoq shifrlanmagan, oraga suqilish (MITM) hujumi bo'lishi mumkin, shaxsiy hisoblarimni ochmasligim yoki albatta VPN yoqishim kerak» deb baholaydi.

### 3. Nmap buyrug'i tahlili · o'rta
`sudo nmap -sV -p- --open 192.168.1.100` buyrug'idagi har bir parametrning (`-sV`, `-p-`, `--open`) texnik vazifasini tushuntiring.
**Yechim:**
- `-sV`: Har bir ochiq portda qaysi dastur va uning qaysi versiyasi ishlayotganini aniqlaydi;
- `-p-`: Standart 1000 ta port emas, balki 1 dan 65535 gacha bo'lgan barcha portlarni tekshiradi;
- `--open`: Yopiq yoki filtrlangan portlarni tashlab yuborib, faqat xavfli ochiq portlarni ko'rsatadi.

### 4. Brute-force va Dictionary farqi · o'rta
Parolni aniqlashda to'liq Brute-force hujumi bilan Lug'at (Dictionary) hujumi o'rtasidagi asosiy farq nimada? Qaysi biri tezroq ishlaydi?
**Yechim:** Brute-force barcha matematik kombinatsiyalarni (aaaa, aaab...) ko'r-ko'rona sinab chiqadi, bu yillar davom etishi mumkin. Lug'at hujumi esa faqat odamlar real hayotda ishlatadigan millionlab eng ommabop parollar ro'yxatini (`rockyou.txt`) sinaydi. Lug'at hujumi yuzlab barobar tezroq ishlaydi, chunki odamlar ko'pincha mantiqiy so'zlarni tanlashadi.

### 5. Parol menejerlarining xavfsizligi · o'rta
Nima sababdan kiberxavfsizlik mutaxassislari barcha parollarni bitta Parol menejeriga (masalan, Bitwarden) ishonib saqlashni tavsiya qilishadi? Bu xavfli emasmi?
**Yechim:** Inson miyasi har xil saytlar uchun 50 ta murakkab 20 belgili parolni yodda tuta olmaydi va oson parollarni qayta ishlatishga majbur bo'ladi. Parol menejeri barcha parollarni AES-256 bilan shifrlangan omborda saqlaydi va faqat bitta kuchli asosiy parolni (Master Password + 2FA) bilish kifoya. Bu har bir saytga o'ziga xos va buzib bo'lmas parollar qo'yish imkonini beradi.

### 6. Hydra dagi -f parametri · oson
Hydra dasturida `-f` kaliti nima vazifani bajaradi va u nima uchun foydali?
**Yechim:** `-f` (fast / found) parametri to'g'ri login va parol topilishi bilanoq skanerlashni to'xtatadi. Bu tarmoqdagi qolgan millionlab so'rovlarni ortiqcha sarflamaslik va vaqtni tejash uchun xizmat qiladi.

### 7. RDP 3389-portining xavfi · o'rta
Nima uchun Windows tizimidagi Masofaviy ish stoli (RDP — 3389 port) to'g'ridan-to'g'ri internetga ochiq qoldirilmasligi kerak?
**Yechim:** Butun dunyodagi avtomatlashtirilgan botlar va skanerlar 3389-portni tinimsiz izlaydi. Agar port ochiq bo'lsa, xakerlar Hydra kabi vositalar orqali parollarni sinay boshlaydi yoki BlueKeep kabi RDP zaifliklaridan foydalanib, kompyuterga to'liq egalik qilib olishadi. RDP faqat ichki tarmoq yoki VPN orqali ochilishi kerak.

### 8. haveibeenpwned.com xizmati mexanizmi · o'rta
haveibeenpwned.com veb-sayti parollarning sizib chiqqanligini qanday tekshiradi va u xavfsizmi?
**Yechim:** Sayt dunyo bo'ylab yuz bergan yirik ma'lumotlar o'g'irlanishlaridagi (baza sizib chiqishlaridagi) milliardlab parollarning xesh bazasini yig'ib boradi. Tekshirishda sayt foydalanuvchining asl parolini so'ramaydi, balki k-Anonymity modeli orqali xeshning boshlang'ich 5 ta belgisini jo'natib tekshiradi. Bu foydalanuvchi maxfiyligini 100% ta'minlaydi.

### 9. Account Lockout siyosati kuchi · qiyin
Kompaniya domenida «Ketma-ket 5 marta noto'g'ri kiritilganda hisob 15 daqiqaga bloklansin» qoidasi o'rnatildi. Bu qoida Hydra va brute-force hujumlarini qanday qilib butunlay befoyda qiladi?
**Yechim:** Hydra sekundiga 100-200 ta parol sinashga mo'ljallangan. Ushbu qoida qo'yilgach, 5 ta urinishdan keyin hisob bloklanadi. Buzg'unchi 1000 ta parol sinashi uchun endi 50 soat kutishi kerak bo'ladi, 1 millionta parolni sinash esa yuzlab yillarni talab qiladi.

### 10. CTF (Capture The Flag) va xavfsizlik tafakkuri · bonus
CTF musobaqalari nima va ular o'quvchilarda xavfsizlik tafakkurini shakllantirishda nima sababdan eng samarali usul hisoblanadi?
**Yechim:** CTF — bu kiberxavfsizlik bo'yicha amaliy musobaqa bo'lib, unda qatnashchilar maxsus zaif tizimlardan «bayroq» (flag — sirli matn) ni topishlari kerak. Bu musobaqada o'quvchi bir vaqtning o'zida ham buzg'unchi kabi zaiflik qidiradi, ham himoyachi kabi tizim tuzilishini tahlil qiladi. Real muammolarni yechish ko'nikmasi shakllanadi.

---

## Tezkor savol-javob

1. **Savol:** Nmap qanday vosita?
   **Javob:** Tarmoqdagi kompyuterlar, ochiq portlar va xizmatlarni skanerlovchi vosita.
2. **Savol:** Dunyo bo'yicha eng mashhur parollar lug'ati qaysi?
   **Javob:** `rockyou.txt`.
3. **Savol:** Kuchli parol kamida necha belgidan iborat bo'lishi kerak?
   **Javob:** Kamida 12-16 belgidan.
4. **Savol:** Bryus Shnayer fikricha xavfsizlik mutaxassisi dunyoga qanday qaraydi?
   **Javob:** Doimo tizimlardagi zaifliklar va «nima buzilishi mumkin?» degan savol nuqtai nazaridan qaraydi.

---

## Mentor uchun eslatma

- Darsda o'quvchilarga Nmap va Hydra buyruqlari sintaksisini terminalda tushuntiring.
- Parol menejerlaridan foydalanish bo'yicha shaxsiy tajribangizni ulashing (Bitwarden misolida).
- 2-hafta yakunlangani sababli haftalik baholash qaydnomasini to'ldirishga tayyorgarlik ko'ring.
