---
title: "Xavfsizlikni anglash (1-qism): xavfsizlik tafakkuri va kuchli parollar siyosati"
description: "Security Mindset tamoyillari (Adversarial va Defensive thinking) hamda Nmap va Hydra yordamida zaifliklar va parollarni tekshirish"
dars: 3
hafta: 2
sinf: 10-sinf-cyber
---

# 6-dars. Xavfsizlikni anglash (1-qism): xavfsizlik tafakkuri va kuchli parollar siyosati

## Reja
1. Xavfsizlik tafakkuri (Security Mindset) nima va u nima uchun kerak?
2. Bryus Shnayerning xavfsizlik tafakkuri haqidagi qarashlari.
3. Xavfsizlik tafakkurining 5 ta tamoyili (What could go wrong, Adversarial, Defensive, Assume breach, Know assets).
4. Zaif parollar va ochiq portlar xavfi: Brute-force va Dictionary hujumlari.
5. Laboratoriya vositalari: Nmap (portlar skaneri) va Hydra (parol sinovi).
6. Kuchli parollar yaratish va Parol menejerlari (Bitwarden) bilan ishlash.

---

## Nazariy qism

### 1. Xavfsizlik tafakkuri nima?

**Xavfsizlik tafakkuri (Security Mindset)** — bu har qanday tizim, dastur, qoida yoki jarayonga «Bunda nima buzilishi mumkin?», «Buni qanday aldash mumkin?» degan savollar bilan yondashish ko'nikmasidir.

| Vaziyat | Oddiy foydalanuvchi | Xavfsizlik tafakkuriga ega mutaxassis |
|---|---|---|
| **Wi-Fi tarmog'i** | «Wi-Fi ga parol qo'yilgan, demak xavfsiz.» | «WPA2 yoki WPA3 ishlatilganmi? Routerning admin paroli o'zgartirilganmi? WPS o'chirilganmi?» |
| **Veb-sayt login formasi** | «Login va parolni kiritadigan joy.» | «Brute-force dan himoya bormi? Parol xeshlanib saqlanadimi? XSS zaifligi yo'qmi?» |
| **Pochta xati** | «Kompaniya direktori yozibdi, faylni ochay.» | «Jo'natuvchi domeni haqiqiymi? SPF/DKIM to'g'rimi? Nega rahbar favqulodda pul so'ramoqda?» |

> «Xavfsizlik o'ziga xos fikrlash tarzini talab qiladi. Yaxshi mutaxassislar do'konga kirsa qanday o'g'irlik qilish mumkinligini, kompyuter ko'rsa qanday zaiflik borligini o'ylamasdan turolmaydilar.» — **Bryus Shnayer**

### 2. Xavfsizlik tafakkurining 5 ta tamoyili

1. **What could go wrong? (Nima noto'g'ri bo'lishi mumkin?):** Har qanday yangi funksiya yoki tizimni baholashda eng yomon ssenariyni ko'z oldiga keltirish.
2. **Adversarial thinking (Hujumchi kabi fikrlash):** Tizimni buzish, cheklovlarni aylanib o'tish va zaif bo'g'inni topishga intilish.
3. **Defensive thinking (Himoyachi kabi fikrlash):** Tizimni bir necha himoya qatlamlari bilan o'rab chiqish (Defense-in-Depth).
4. **Assume breach (Tizim allaqachon buzilgan deb hisoblash):** Ichki tarmoqqa allaqachon virus kirgan degan faraz bilan har bir so'rovni alohida tekshirish (Zero Trust).
5. **Know your assets (O'z aktivlaringni aniq bilish):** Himoyalash kerak bo'lgan barcha serverlar, parollar va ma'lumotlar ro'yxatini to'liq bilish.

---

### 3. Zaif parollar va ochiq portlar xavfi

Kiberhujumchilar ko'pincha tizimga oson yo'l bilan kirishadi:
- **Zaif parollar:** `123456`, `admin`, `password`, `qwerty` — bunday parollar maxsus lug'atlar (`rockyou.txt`) yordamida bir necha soniyada topiladi.
- **Ochiq qoldirilgan portlar:** Serverda keraksiz ishlayotgan xizmatlar (masalan, 21-port FTP, 23-port Telnet, 3389-port RDP).

---

## Amaliy laboratoriya

> [!CAUTION]
> Ushbu laboratoriya ishlari faqat o'quv virtual muhitida (masalan, 172.16.4.65) o'tkaziladi.

### 1-qadam: Nmap bilan ochiq portlarni aniqlash
Kali Linux terminalida sinov kompyuterining barcha portlarini tekshirish:
```bash
sudo nmap -sV -p- --open 172.16.4.65
```

### 2-qadam: Hydra orqali zaif parolni sinash
Masofaviy ish stoli (RDP) uchun zaif parolni `rockyou.txt` lug'ati orqali aniqlash:
```bash
hydra -l windows -P /usr/share/wordlists/rockyou.txt -t 4 -V -f rdp://172.16.4.65
```

### 3-qadam: Kuchli parol mezonlari
- Kamida 12-16 ta belgi;
- Katta va kichik harflar, raqamlar va maxsus belgilar (`Maktab@2025!Uz`);
- Parol menejeri (Bitwarden, KeePass) orqali boshqarish.

---

## Amaliy topshiriqlar

### 1. Xavfsizlik tafakkurining 5 tamoyili <Badge type="tip" text="oson" />
Xavfsizlik tafakkurini tashkil etuvchi 5 ta tamoyilni (What could go wrong, Adversarial, Defensive, Assume breach, Know assets) daftaringizga yozing va qisqacha izohlang.

### 2. Oddiy odam va mutaxassis nigohi <Badge type="tip" text="oson" />
Do'kondagi ochiq, bepul Wi-Fi ga oddiy foydalanuvchi qanday ko'z bilan qaraydi va kiberxavfsizlik mutaxassisi qanday ko'z bilan qaraydi?

### 3. Nmap buyrug'i tahlili <Badge type="warning" text="o'rta" />
`sudo nmap -sV -p- --open 192.168.1.100` buyrug'idagi har bir parametrning (`-sV`, `-p-`, `--open`) vazifasini tushuntiring.

### 4. Brute-force va Dictionary farqi <Badge type="warning" text="o'rta" />
To'liq brute-force hujumi bilan lug'at (Dictionary) hujumi o'rtasidagi asosiy farq nimada? Nima sababdan lug'at hujumi ancha tez natija beradi?

### 5. Parol menejerlari afzalligi <Badge type="warning" text="o'rta" />
Nima sababdan kiberxavfsizlik mutaxassislari barcha parollarni bitta Parol menejeriga (masalan, Bitwarden) ishonib saqlashni tavsiya qilishadi?

### 6. Hydra dasturidagi -f parametri <Badge type="tip" text="oson" />
Hydra dasturida `-f` kaliti nima vazifani bajaradi va u nima uchun foydali?

### 7. RDP 3389-portining xavfi <Badge type="warning" text="o'rta" />
Nima uchun Windows tizimidagi Masofaviy ish stoli (RDP — 3389 port) to'g'ridan-to'g'ri ochiq internetga ulanmasligi kerak?

### 8. haveibeenpwned xizmati tahlili <Badge type="warning" text="o'rta" />
haveibeenpwned.com veb-sayti parollarning sizib chiqqanligini qanday tekshiradi va u xavfsizmi?

### 9. Account Lockout siyosati <Badge type="danger" text="qiyin" />
Kompaniya domenida «Ketma-ket 5 marta noto'g'ri kiritilganda hisob 15 daqiqaga bloklansin» qoidasi o'rnatildi. Bu qoida Hydra va brute-force hujumlarini qanday qilib butunlay befoyda qiladi?

### 10. CTF va kiberko'nikmalar <Badge type="info" text="bonus" />
CTF (Capture The Flag) musobaqalari nima va ular o'quvchilarda xavfsizlik tafakkurini shakllantirishda nima sababdan eng samarali usul hisoblanadi?

---

## O'z-o'zini tekshirish savollari

1. Security Mindset tushunchasini Bryus Shnayer qanday ta'riflagan?
2. Dunyoda kiberxavfsizlik bo'yicha necha million mutaxassis yetishmaydi?
3. Nmap skaneri nima uchun qo'llaniladi?
4. `rockyou.txt` fayli nima?
5. Parol menejeridan foydalanishning asosiy talabi nima?

---

## Foydali manbalar

- Nmap Reference Guide: `nmap.org/book/man.html`
- Bitwarden Open Source Password Manager: `bitwarden.com`
- Have I Been Pwned password check: `haveibeenpwned.com/Passwords`
