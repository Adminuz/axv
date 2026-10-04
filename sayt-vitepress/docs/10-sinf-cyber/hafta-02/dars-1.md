---
title: "4-dars. CIA uchligi (1-qism): konfidensiallik, yaxlitlik va foydalanuvchanlik tamoyillari"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (Cyber)", "link": "/10-sinf-cyber/"}, "week": {"n": 2, "link": "/10-sinf-cyber/hafta-02/"}, "g": 4, "title": "CIA uchligi (1-qism): konfidensiallik, yaxlitlik va foydalanuvchanlik tamoyillari", "lead": "", "slide": "/slaydlar/10-sinf-cyber/hafta-02/dars-1.html", "tabs": [{"g": 4, "link": "/10-sinf-cyber/hafta-02/dars-1", "current": true}, {"g": 5, "link": "/10-sinf-cyber/hafta-02/dars-2", "current": false}, {"g": 6, "link": "/10-sinf-cyber/hafta-02/dars-3", "current": false}], "prev": null, "next": {"g": 5, "title": "CIA uchligi (2-qism): CIA buzilish ssenariylari va MITM hujumlari", "link": "/10-sinf-cyber/hafta-02/dars-2"}}
---

---
title: "CIA uchligi (1-qism): konfidensiallik, yaxlitlik va foydalanuvchanlik tamoyillari"
description: "Axborot xavfsizligining oltin uchligi — Confidentiality, Integrity, Availability tamoyillari va ularning real hayotiy ahamiyati"
dars: 1
hafta: 2
sinf: 10-sinf-cyber
---

<div class="blk">

## <Icon name="file-text" /> Reja

1. Axborot xavfsizligining poydevori: CIA triadasi tushunchasi.
2. Confidentiality (Konfidensiallik / Maxfiylik): ruxsatsiz o'qishdan himoyalanish.
3. Integrity (Yaxlitlik): ruxsatsiz o'zgartirish va buzilishdan himoyalanish.
4. Availability (Foydalanuvchanlik): uzluksiz xizmat ko'rsatish va zaxira tizimlari.
5. Alisaning Onlayn Banki (AOB) ssenariysida CIA tahlili.
6. Amaliy laboratoriya: Fayl yaxlitligini SHA-256 xesh qiymati orqali tekshirish.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Nazariy qism

### 1. CIA Triadasi nima?

Kiberxavfsizlik sohasidagi har qanday qoida, algoritm yoki himoya vositasi uchta asosiy mezonni ta'minlashga xizmat qiladi. Bular xalqaro miqyosda **CIA triadasi (CIA uchligi)** deb yuritiladi:

```
                      +-------------------+
                      |         C         |
                      |  Confidentiality  |
                      |   (Maxfiylik)     |
                      +---------+---------+
                               / \
                              /   \
                             /     \
                            /       \
                           /         \
        +-----------------+           +-----------------+
        |        I        |-----------|        A        |
        |    Integrity    |           |  Availability   |
        |   (Yaxlitlik)   |           | (Foydalanuvchan)|
        +-----------------+-----------+-----------------+
```

### 2. CIA uchligining batafsil tavsifi

| Mezon | Asosiy maqsadi | Buzilish holati | Himoya vositalari |
|---|---|---|---|
| **Confidentiality (Maxfiylik)** | Axborotni ruxsatsiz **o'qishdan** himoyalash | Parollarni o'g'irlash, ma'lumotlar sizib chiqishi | Shifrlash (AES, RSA), kirish huquqlari (ACL), 2FA |
| **Integrity (Yaxlitlik)** | Axborotni ruxsatsiz **o'zgartirishdan** himoyalash | Balansni soxtalashtirish, loglarni o'chirish | Xesh funksiyalari (SHA-256), raqamli imzo |
| **Availability (Foydalanuvchanlik)** | Tizimni ruxsatsiz **to'xtatishdan** himoyalash | DoS/DDoS hujumlari, server qulashi, tok o'chishi | Zaxira serverlar, Load balancer, UPS, Backup |

---

### 3. Alisaning Onlayn Banki (AOB) misolida CIA

1. **Konfidensiallik:** Bob o'z balansida qancha mablag' borligini Tridi bilishini istamaydi. Bank Bobning ma'lumotlarini qat'iy maxfiy saqlaydi.
2. **Yaxlitlik:** Bob 100 000 so'm o'tkazmoqchi bo'lganida, Tridi summani yo'lda 10 000 000 so'mga aylantirib qo'ya olmasligi kerak.
3. **Foydalanuvchanlik:** Bob do'konda turib to'lov qilmoqchi bo'lganida, bank serveri ishlamay qolmasligi lozim.

### 4. Turli sohalarda ustuvorlik

- **Favqulodda xizmatlar (Tez yordam, 103):** 1-o'rinda **Availability (Foydalanuvchanlik)** — qo'ng'iroq bir daqiqa ham uzilmasligi kerak.
- **Bank va moliya sektori:** 1-o'rinda **Integrity (Yaxlitlik)** — hisob-kitoblar va mablag'lar 1 tiyinga ham adashmasligi shart.
- **Harbiy va davlat sirlari:** 1-o'rinda **Confidentiality (Maxfiylik)** — sirlar dushman qo'liga tushmasligi mutlaq shart.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy laboratoriya

### Fayl yaxlitligini SHA-256 xeshi orqali tekshirish

Har qanday raqamli fayl o'zining noyob matematik xesh qiymatiga ega bo'ladi. Agar fayl ichidagi bitta harf yoki tinish belgisi o'zgarsa ham, uning SHA-256 xeshi butunlay yangilanadi.

#### Windows tizimida (PowerShell / CMD):
```powershell
# 1. Sinov faylini yaratamiz
"Hisob raqam: 202080001000, Summa: 500000 UZS" | Out-File -FilePath tolov.txt

# 2. Asl xesh qiymatini chiqaramiz
CertUtil -hashfile tolov.txt SHA256

# 3. Faylni tahrirlab summani o'zgartiramiz
"Hisob raqam: 202080001000, Summa: 999999 UZS" | Out-File -FilePath tolov.txt

# 4. Qayta xesh olamiz va farqni solishtiramiz
CertUtil -hashfile tolov.txt SHA256
```

#### Linux / macOS tizimida:
```bash
echo "Hisob raqam: 202080001000, Summa: 500000 UZS" > tolov.txt
sha256sum tolov.txt

echo "Hisob raqam: 202080001000, Summa: 999999 UZS" > tolov.txt
sha256sum tolov.txt
```

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy topshiriqlar

### 1. CIA atamalarini tushunish &lt;Badge type="tip" text="oson" />
CIA uchligidagi uchta harf nimani anglatadi? Har birining o'zbekcha va inglizcha nomlarini hamda qisqa ta'rifini yozing.

### 2. Konfidensiallik va yaxlitlik chegarasi &lt;Badge type="tip" text="oson" />
Hujumchi shifrlangan xatni o'qiy olmadi, ammo uning ichidagi ba'zi baytlarni tasodifiy o'zgartirib yubordi. Bu yerda CIA ning qaysi jihati buzildi va qaysi biri saqlanib qoldi?

### 3. Favqulodda xizmatlar tahlili &lt;Badge type="warning" text="o'rta" />
Nima sababdan tez tibbiy yordam (103) yoki qutqaruv xizmatlarining axborot tizimida eng asosiy e'tibor Foydalanuvchanlikka (Availability) qaratiladi?

### 4. Xesh qiymati orqali tekshirish &lt;Badge type="warning" text="o'rta" />
Dastur yuklab olish saytida dastur fayli yonida uning SHA-256 xesh kodi ko'rsatilgan. Nima uchun xavfsizlik mutaxassislari faylni ishga tushirishdan oldin xeshni solishtirishni maslahat berishadi?

### 5. Bankda Yaxlitlikning ahamiyati &lt;Badge type="warning" text="o'rta" />
Tasavvur qiling, bank ma'lumotlar bazasida konfidensiallik saqlanmoqda (begonalar ko'rmaydi), ammo yaxlitlik buzildi. Bu qanday fojiali oqibatlarga olib kelishi mumkin?

### 6. DoS hujumi va CIA &lt;Badge type="tip" text="oson" />
DDoS hujumi uyushtirilgan vaqtda CIA uchligining qaysi ustuni bevosita zarba ostida qoladi va buziladi?

### 7. Shifrlashning vazifasi &lt;Badge type="warning" text="o'rta" />
Kriptografik shifrlash usullari (masalan, AES-256) CIA uchligining asosan qaysi mezonini ta'minlash uchun xizmat qiladi?

### 8. CIA muvozanati muammosi &lt;Badge type="danger" text="qiyin" />
Agar kompaniya konfidensiallikni 100% ga oshirish uchun xodimlarga har bir bosgan tugmasi uchun SMS-kod va 100 belgili parol talab qilsa, bu CIA ning qaysi komponentiga qanday zarar yetkazadi?

### 9. Kasalxona tizimida ssenariy tahlili &lt;Badge type="danger" text="qiyin" />
Kasalxona kompyuterida bemorlarning operatsiya ro'yxati saqlanadi.
a) Ro'yxatni buzg'unchi o'g'irlab internetga chiqarsa nima buziladi?
b) Bemorning operatsiya qilinadigan a'zosi nomini o'zgartirib qo'yilsa nima buziladi?
c) Kompyuterlar tok o'chgani sababli o'chib qolsa nima buziladi?

### 10. Zaxiralash (Backup) ning roli &lt;Badge type="info" text="bonus" />
Tashkilotda har kuni zaxira nusxa (Backup) olish amaliyoti yo'lga qo'yilgan. Ushbu chora CIA ning qaysi 2 ta mezonini qayta tiklashga xizmat qiladi va nima sababdan?

---

</div>

<div class="blk">

## <Icon name="file-text" /> O'z-o'zini tekshirish savollari

1. CIA modeli qachondan beri axborot xavfsizligining asosi hisoblanadi?
2. Ma'lumotlarni ruxsatsiz o'qishdan qaysi tamoyil himoya qiladi?
3. SHA-256 xesh kodining uzunligi necha belgidan iborat?
4. Qaysi holatda Yaxlitlik buzilgan hisoblanadi?
5. Foydalanuvchanlikni saqlab qolish uchun serverlarda qanday texnologiyalar qo'llaniladi?

---

</div>

<div class="blk">

## <Icon name="file-text" /> Foydali manbalar

- NIST SP 800-53: Security and Privacy Controls for Information Systems.
- ISO/IEC 27001: Information Security Management Systems.

</div>

