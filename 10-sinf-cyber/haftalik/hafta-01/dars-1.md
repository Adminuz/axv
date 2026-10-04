---
title: "Kiberxavfsizlik asoslari: axborot xavfsizligi, kiberjinoyat, kiberqonun, inson omili va aktivlar"
description: "Kiberxavfsizlik va axborot xavfsizligi tushunchalari, Alisa-Bob-Tridi modeli, O'zbekiston kiberxavfsizlik qonuni, inson omili hamda himoya sohalari"
dars: 1
hafta: 1
sinf: 10-sinf-cyber
---

# 1-dars. Kiberxavfsizlik asoslari: axborot xavfsizligi, kiberjinoyat, kiberqonun, inson omili va aktivlar

## Dars rejasi (80 daqiqa)

1. **Kirish va tashkiliy qism (10 daqiqa):** Kiberxavfsizlik kursi bilan tanishuv, dars qoidalari, maqsad va kutilmalar.
2. **Nazariy qism (25 daqiqa):** 
   - Axborot xavfsizligi va kiberxavfsizlik o'rtasidagi farq.
   - Axborot xavfsizligining klassik timsollari: Alisa, Bob va Tridi modeli (AOB ssenariysi).
   - Aktiv, tahdid, zaiflik va kiberhujum tushunchalari.
   - O'zbekiston Respublikasining 2022-yil 15-apreldagi «Kiberxavfsizlik to'g'risida»gi O'RQ-764-sonli qonuni.
   - Axborot xavfsizligida inson omili (eng zaif bo'g'in).
   - Axborot xavfsizligining 5 ta asosiy sohasi: Network, Application, Data, Endpoint, Cloud Security.
3. **Amaliy tahlil va mashg'ulot (30 daqiqa):**
   - Tashkilot aktivlarini inventarizatsiya qilish va xavf matritsasini tuzish.
   - Alisaning Onlayn Banki (AOB) xavfsizlik arxitekturasi tahlili.
4. **Mustaqil ish va muhokama (10 daqiqa):** O'quvchilar bilan situatsion kiberxavfsizlik holatlarini tahlil qilish.
5. **Xulosa va baholash (5 daqiqa):** Darsni yakunlash, tezkor savol-javob, uyga vazifa topshirish.

---

## Asosiy tushunchalar

- **Kibermakon (Cyberspace):** Axborot texnologiyalari yordamida yaratilgan virtual muhit.
- **Axborot xavfsizligi (Information Security):** Axborotning qog'oz, elektron yoki og'zaki bo'lishidan qat'i nazar, unga ruxsatsiz ta'sir etish yoki undan foydalanishning oldi olingan holati.
- **Kiberxavfsizlik (Cybersecurity):** Kibermakonda shaxs, jamiyat va davlat manfaatlarining tashqi va ichki tahdidlardan himoyalanganlik holati; elektron shakldagi barcha ma'lumotlar va axborot infratuzilmasi himoyasi.
- **Aktiv (Asset):** Tashkilot yoki shaxs uchun qadrli bo'lgan barcha axborot va resurslar (ma'lumotlar bazasi, serverlar, mijozlar shaxsiy ma'lumotlari).
- **Zaiflik (Vulnerability):** Tizim, dasturiy ta'minot yoki tashkiliy boshqaruvdagi xatolik yoki kamchilik bo'lib, hujumchiga tahdidni amalga oshirishga imkon beradi.
- **Kibertahdid (Cyber Threat):** Kibermakonda zarar yetkazishi mumkin bo'lgan potensial xavf, omil yoki shart-sharoitlar majmui.
- **Kiberhujum (Cyber Attack):** Kibermakonda apparat va dasturiy vositalardan foydalangan holda qasddan amalga oshiriladigan buzg'unchi harakat.
- **Kiberjinoyatchilik:** Axborotni o'g'irlash, buzish, o'zgartirish yoki tizimlarni ishdan chiqarish maqsadida texnik vositalardan foydalanib sodir etiladigan jinoiy harakatlar.
- **O'RQ-764:** O'zbekiston Respublikasining 2022-yil 15-aprelda qabul qilingan «Kiberxavfsizlik to'g'risida»gi Qonuni.

---

## Dars mazmuni

### 1. Axborot xavfsizligi va Kiberxavfsizlik farqi

Ko'pincha bu ikki tushuncha bir xil ma'noda ishlatiladi, biroq ularning qamrovi turlicha:
- **Axborot xavfsizligi:** Axborotning har qanday shaklini — qog'ozdagi shartnomalar, xodimlarning og'zaki sirlari, doskadagi chizmalar, arxiv jildlari va elektron ma'lumotlarni ruxsatsiz kirishdan, o'g'irlanishdan va yo'qotishdan himoya qiladi.
- **Kiberxavfsizlik:** Aynan kibermakondagi, ya'ni raqamli/elektron formatdagi ma'lumotlar, tarmoqlar, serverlar, kompyuterlar va mobil qurilmalarni himoyalash bilan shug'ullanadi. Kiberxavfsizlik axborot xavfsizligining eng yirik va tez rivojlanayotgan qismidir.

```
+-------------------------------------------------------------+
|              AXBOROT XAVFSIZLIGI (Keng qamrovli)            |
|  (Qog'oz hujjatlar, arxivlar, xodimlar suhbati, qonunlar)    |
|                                                             |
|       +---------------------------------------------+       |
|       |             KIBERXAVFSIZLIK                 |       |
|       |  (Raqamli ma'lumotlar, tarmoqlar, bulut,    |       |
|       |   operatsion tizimlar, smartfonlar, API)    |       |
|       +---------------------------------------------+       |
+-------------------------------------------------------------+
```

### 2. Axborot xavfsizligining klassik timsollari: Alisa, Bob va Tridi

Kriptografiya va axborot xavfsizligi fanida aloqa ishtirokchilarini tushunish uchun ramziy qahramonlardan foydalaniladi:
- **Alisa (Alice):** Tizim egasi yoki xabar yuboruvchi qonuniy tomon (masalan, bank yoki xizmat ko'rsatuvchi kompaniya).
- **Bob (Bob):** Qonuniy mijoz yoki xabarni qabul qiluvchi tomon (masalan, bank mijozi).
- **Tridi / Eva (Trudy / Eve):** Hujumchi (intruder / adversary / eavesdropper), qonuniy faoliyatga xalaqit beruvchi, xabarlarni tutib oluvchi, o'zgartiruvchi yoki o'g'irlovchi tomon.

**Alisaning Onlayn Banki (AOB) ssenariysi:**
- Alisa onlayn bank xizmatini yuritadi.
- Bob bank mijozi bo'lib, o'z hisob raqamidagi balansni ko'rish va to'lovlarni amalga oshirishni xohlaydi.
- Tridi esa Bob va Alisa o'rtasidagi aloqani tutib olishga, Bobning balansini ko'rishga yoki o'zgartirishga harakat qiladi.
- **Alisaning xavfsizlik muammosi:** Bank serverlarining to'xtovsiz ishlashi, mijozlar pullari xavfsizligi va obro'ni saqlash.
- **Bobning xavfsizlik muammosi:** Parolining o'g'irlanmasligi, shaxsiy hisobidagi mablag'ning daxlsizligi.
- **Tridining niyati:** Moliyaviy foyda olish, ma'lumotlarni o'g'irlash yoki tizimni obro'sizlantirish.

### 3. Axborot xavfsizligida inson omili

Zamonaviy texnologiyalar eng murakkab shifrlash algoritmlari (AES-256, RSA-4096) va zamonaviy tarmoqlararo ekranlar bilan himoyalangan bo'lishi mumkin. Biroq kiberhujumlarning 90-95 foizi tizimdagi eng zaif bo'g'in — **inson omili** sababli muvaffaqiyatli yakunlanadi.
- Foydalanuvchi qanchalik murakkab SSL/TLS sertifikatiga ega saytga kirsa ham, brauzer bergan «Sertifikat ishonchsiz, davom etasizmi?» ogohlantirishini e'tiborsiz qoldirib «Baribir o'tish» tugmasini bossa, MITM hujumi amalga oshadi.
- Xodimlar oson esda qoladigan parollarni («123456», «qwerty», «Admin@2025») tanlashadi yoki parollarni stikerga yozib monitorda qoldirishadi.
- Shubhali elektron xatlardagi havolalarni tekshirmasdan bosishadi.
Xavfsizlik tenglamasidan inson xatosini bartaraf etish yoki ularni muntazam o'qitish (Security Awareness) har qanday texnik himoyadan muhimroqdir.

### 4. Axborot xavfsizligining 5 ta sohasi

1. **Tarmoq xavfsizligi (Network Security):** Kompyuter tarmog'i infratuzilmasini ruxsatsiz kirishdan, paketlarni ushlab qolishdan va DoS hujumlaridan himoya qilish (Firewall, IDS/IPS, VPN, marshrutlash filtrlari).
2. **Ilova xavfsizligi (Application Security):** Dasturiy ta'minotni uning butun hayotiy siklida (SDLC: loyihalash, kod yozish, testlash, qo'llab-quvvatlash) xatolik va zaifliklardan himoya qilish (Code review, SAST/DAST, Penetration testing).
3. **Ma'lumotlar xavfsizligi (Data Security):** Ma'lumotlarni saqlash holatida ham (Data at Rest), uzatish jarayonida ham (Data in Transit) shifrlash, kirish huquqlarini cheklash va DLP (Data Loss Prevention) tizimlari orqali himoya qilish.
4. **Qurilma / So'nggi nuqta xavfsizligi (Endpoint Security):** Foydalanuvchilarning noutbuklari, ish stansiyalari, smartfonlari va serverlarini himoya qilish (Antivirus, EDR — Endpoint Detection and Response, MDM).
5. **Bulut xavfsizligi (Cloud Security):** AWS, Google Cloud, Azure yoki mahalliy bulut provayderlarida joylashgan virtual infratuzilma, ma'lumotlar va ilovalarni himoyalash, umumiy mas'uliyat modeli (Shared Responsibility Model).

---

## Amaliy mashg'ulot

### 1-topshiriq: Tashkilot aktivlari va tahdidlarini tasniflash (AOB modeli misolida)

Har bir guruh yoki o'quvchi kichik tashkilot (masalan, «Maktab kutubxonasi» yoki «Onlayn do'kon») aktivlari ro'yxatini shakllantiradi va quyidagi jadvalni to'ldiradi:

| Aktiv nomi | Aktiv turi (Apparat / Dastur / Ma'lumot) | Potensial tahdid | Mumkin bo'lgan zaiflik | Himoya chorasi |
|---|---|---|---|---|
| Foydalanuvchilar parollari bazasi | Ma'lumot (Data) | Hujumchi tomonidan bazani o'g'irlash | Parollar ochiq matnda saqlanishi | Argon2/bcrypt bilan xeshlash, tuz (salt) qo'shish |
| Veb-server (Nginx/Apache) | Apparat-dasturiy | DoS/DDoS hujumi | So'rovlar soniga cheklov yo'qligi | Rate limiting, WAF (Web Application Firewall) |
| Xodim kompyuteri | Qurilma (Endpoint) | Fishing xati orqali troyan yuqishi | Xodimda xavfsizlik madaniyati pastligi | EDR/Antivirus, xodimlarni o'qitish (Awareness) |

---

## Mustaqil topshiriqlar

### 1. Kiberxavfsizlik va axborot xavfsizligi farqi · oson
Kompaniya ofisidagi arxiv xonasi kalit bilan qulflangan, ammo server xonasining Wi-Fi tarmog'i parolsiz ochiq qoldirilgan. Ushbu holatda qaysi xavfsizlik sohalari qanday darajada ta'minlangan?
**Yechim:** Arxiv xonasi qulflangani — bu jismoniy va axborot xavfsizligining an'anaviy choralari (qog'oz hujjatlar himoyasi). Ammo ochiq Wi-Fi — kiberxavfsizlikning jiddiy buzilishi bo'lib, hujumchiga tarmoqqa kirish, paketlarni sniffer qilish va ichki serverlarga hujum uyushtirish imkonini beradi. Demak, axborot xavfsizligining jismoniy qismi qisman ta'minlangan, ammo kiberxavfsizlik nol darajada.

### 2. Alisa, Bob va Tridi ssenariysida rol tahlili · oson
Elektron tijorat saytida Bob Alisadan krossovka buyurtma qilmoqda. Tridi ularning aloqasini kuzatib, Bobning yetkazib berish manzilini o'z manziliga o'zgartirib qo'ydi. Bu yerda Tridi qanday xatti-harakat qildi?
**Yechim:** Tridi bu yerda faol hujumchi (Active attacker) sifatida ishtirok etdi. U nafaqat xabarni o'qidi (passiv tinglash), balki ma'lumotlar yaxlitligini buzdi (o'zgartirdi) va tranzaksiyani soxtalashtirdi.

### 3. O'zbekiston kiberxavfsizlik qonuni tahlili · o'rta
O'RQ-764-sonli Qonunga ko'ra, davlat organlari va kritik axborot infratuzilmasi subyektlarining asosiy majburiyatlari nimalardan iborat?
**Yechim:** Qonunga ko'ra:
1. Axborot tizimlarining kiberxavfsizligini doimiy ta'minlash va monitoring olib borish;
2. Kiberxavfsizlik talablariga muvofiqlik bo'yicha ekspertizadan o'tish;
3. Kiberhujumlar va hodisalar to'g'risida vakolatli organga (Kiberxavfsizlik markaziga) xabar berish;
4. Xodimlarning kiberxavfsizlik savodxonligini oshirish.

### 4. Aktivlar qiymatini aniqlash · o'rta
Tibbiy klinikaning serverida quyidagilar saqlanadi:
a) Bemorlarning to'liq kasallik tarixi va qon tahlillari;
b) Klinikaning dushanba kungi xodimlar navbatchilik jadvali;
c) Klinikaning Wi-Fi mehmon paroli.
Ushbu aktivlarni xavflilik darajasi bo'yicha saralang va asoslang.
**Yechim:**
1-darajali (Kritik aktiv): Bemorlarning kasallik tarixi (konfidensial tibbiy ma'lumotlar, oshkor bo'lishi qonuniy javobgarlik va katta zararga olib keladi).
2-darajali: Navbatchilik jadvali (ichki operatsion ma'lumot, o'g'irlansa ham katta ziyon yetkazmaydi).
3-darajali: Wi-Fi mehmon paroli (ommaviy foydalanish uchun mo'ljallangan, tarmoq izolatsiya qilingan bo'lsa xavfi past).

### 5. Inson omilining texnik choralardan ustunligi · o'rta
Kompaniyada 50 ming dollarlik yangi avlod tarmoqlararo ekrani (NGFW) o'rnatilgan. Buxgalterga «Direktordan: shoshilinch hisobotni to'ldiring» mavzusidagi xat keldi va buxgalter faylni ochib, parolini kiritdi. Nima uchun qimmatbaho texnika yordam bermadi?
**Yechim:** Tarmoqlararo ekranlar tarmoq trafigini va standart hujum imzolarini tekshiradi. Ammo ijtimoiy muhandislik orqali foydalanuvchining o'zi ixtiyoriy ravishda ma'lumot kiritganda yoki shifrlangan qonuniy kanal orqali faylni yuklab olganda, texnik vosita inson xatosini to'xtata olmaydi. Himoyaning eng muhim bo'g'ini xodimning hushyorligidir.

### 6. Zaiflik va tahdid o'rtasidagi farq · oson
«Tizimda parolsiz ochilgan Telnet xizmati bor» va «Xaker parolni bilmasdan tizimga ulanishga harakat qilmoqda». Bulardan qaysi biri zaiflik, qaysi biri tahdid?
**Yechim:** «Parolsiz ochilgan Telnet xizmati» — bu tizimdagi zaiflik (vulnerability). «Xakerning tizimga kirishga urinishi» — bu kibertahdid yoki kiberhujum (threat/attack).

### 7. Axborot xavfsizligi sohalarini ajratish · o'rta
Quyidagi vazifalar axborot xavfsizligining qaysi sohasiga tegishli ekanini aniqlang:
a) Xodimlarning noutbuklariga BitLocker o'rnatish;
b) Kompaniya veb-saytidagi SQL inyeksiyani tuzatish;
c) AWS S3 baketiga ommaviy kirishni yopish;
d) Routerda 22-portni faqat VPN foydalanuvchilari uchun ochish.
**Yechim:**
a) Endpoint Security (Qurilma xavfsizligi)
b) Application Security (Ilova xavfsizligi)
c) Cloud Security (Bulut xavfsizligi)
d) Network Security (Tarmoq xavfsizligi)

### 8. Kiberjinoyat motivatsiyalari tahlili · o'rta
Kiberjinoyatchilar nima sababdan tizimlarga hujum qiladi? Asosiy 4 ta motivatsiyani sanang.
**Yechim:**
1. Moliyaviy foyda (to'lov talab qilish, karta pullarini o'g'irlash);
2. Sanoat yoki davlat josusligi (raqobatchi sirlarini yoki davlat ma'lumotlarini o'g'irlash);
3. Xaktivizm / Siyosiy sabablar (siyosiy yoki ijtimoiy g'oyalarni bildirish, saytlarni defacing qilish);
4. Shaxsiy obro' va psixologik motivatsiya (o'z mahoratini ko'rsatish, tizimni sinab ko'rish).

### 9. Tashkilot xavfsizlik madaniyati audit savolnomasi tuzish · qiyin
Kichik IT kompaniyada xodimlarning kiberxavfsizlik madaniyatini tekshirish uchun 5 ta nazorat savolidan iborat so'rovnoma ishlab chiqing.
**Yechim:**
1. Noutbukdan uzoqlashganda `Win + L` (ekranni qulflash) bosiladimi?
2. Barcha hisoblar (pochta, GitHub, GitLab) uchun 2FA yoqilganmi?
3. Shubhali elektron pochta manzili yoki kutilmagan ilova kelganda kimga xabar beriladi?
4. Ish kompyuteriga shaxsiy USB fleshkalarini ulashga ruxsat bormi?
5. Har xil saytlar uchun parollar qanday boshqariladi (parol menejeri bormi)?

### 10. Alisa va Bob ssenariysida himoyachi kabi fikrlash · bonus
AOB onlayn bank tizimiga Tridi doimiy ravishda noto'g'ri parollarni kiritib, Bobning hisobini topishga urinmoqda (brute-force). Himoyachi sifatida ushbu muammoni hal qilish uchun 3 ta texnik yechim taklif qiling.
**Yechim:**
1. **Account Lockout Policy:** Ketma-ket 5 marta noto'g'ri kiritilganda hisobni 15 daqiqaga bloklash;
2. **CAPTCHA va Rate Limiting:** 3 marta noto'g'ri urinishdan so'ng reCAPTCHA ko'rsatish va IP bo'yicha so'rovlar chastotasini cheklash;
3. **MFA / Push bildirishnoma:** Har bir kirish urinishida Bobning telefoniga tasdiqlash kodi yoki xabar yuborish.

---

## Tezkor savol-javob

1. **Savol:** Axborot xavfsizligi va kiberxavfsizlikning asosiy farqi nimada?
   **Javob:** Axborot xavfsizligi barcha turdagi axborotlarni (qog'oz, og'zaki, jismoniy, raqamli) qamrab oladi, kiberxavfsizlik esa faqat kibermakondagi elektron ma'lumotlar va axborot tizimlarini himoyalaydi.
2. **Savol:** Nega inson omili kiberxavfsizlikdagi eng zaif zanjir hisoblanadi?
   **Javob:** Texnik vositalar qanchalik mukammal bo'lmasin, insonlar aldanishi, chalg'ishi, qoidalarni buzishi yoki e'tiborsizlik bilan xatoga yo'l qo'yishi mumkin.
3. **Savol:** O'zbekiston kiberxavfsizlik qonuni qachon qabul qilingan va uning raqami qanday?
   **Javob:** 2022-yil 15-aprelda qabul qilingan, O'RQ-764-sonli Qonun.
4. **Savol:** Alisa va Bob timsollari nimani ifodalaydi?
   **Javob:** Qonuniy aloqa qiluvchi ikki tomonni (yuboruvchi va qabul qiluvchi).

---

## Mentor uchun eslatma

- Darsni quruq qonuniy moddalarni o'qish bilan emas, real hayotiy voqealar (Alisa, Bob, Tridi onlayn banki) misolida boshlang.
- O'quvchilarga xavfsizlik bu faqat dasturchi yoki xakerning ishi emas, balki har qanday kompyuter foydalanuvchisining kundalik madaniyati ekanligini uqtiring.
- Keyingi darsda zararli dasturlar tahlil qilinishini aytib, o'quvchilarda qiziqish uyg'oting.
