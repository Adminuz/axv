# 6-dars. Kompyuter xavfsizligi va antivirus dasturlari

**Hafta:** 2 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliy mashg'ulot · **I-bob**, 6-dars

## 1. Dars rejasi

**Maqsad:** o'quvchilarda kompyuter va axborot xavfsizligi tushunchalari, zararli dasturlar (malware: virus, trojan, spyware, ransomware, worm), antivirus tizimlarining ishlash mexanizmlari (skanerlash, karantin, real-vaqt himoyasi), kuchli parollar yaratish va 2FA (ikki bosqichli autentifikatsiya) hamda tashqi xotira (fleshka) va internetdan xavfsiz foydalanish bo'yicha mustahkam ko'nikmalarni shakllantirish.

**Kutiladigan natija:**
- Kompyuter xavfsizligi va kibergigiyena asosiy tamoyillarini tushuntira oladi.
- Zararli dasturlar tasnifini (virus, troyan oti, ayg'oqchi dastur, shifrlash virusi/tovlamachi) biladi va ularning xavfini farqlaydi.
- Antivirus dasturlari (Windows Defender va boshqalar) qanday ishlashini (imzo tahlili, evristik tahlil, karantin) tushunadi va amalda skanerlashni bajara oladi.
- Xavfsiz va buzilmas parol tuzish qoidalariga rioya qiladi, 2FA tizimining mohiyatini tushunadi.
- Fleshka, elektron pochta va internetdan foydalanishda xavfsizlik choralarini to'g'ri qo'llaydi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va kirish | O'tgan darsni takrorlash (brauzerlar va email). Muammoli vaziyat: «Kompyuter to'satdan qotib, barcha fayllar ochilmay qolsa yoki ekranda pul talab qilinsa, nima qilish kerak?» |
| 10–30 daq | Yangi mavzu: Nazariya | Zararli dasturlar (Malware) turlari, antiviruslarning ishlash tamoyillari, parollar madaniyati va 2FA, fleshkalar xavfsizligi |
| 30–35 daq | Tanaffus | Harakatli tanaffus |
| 35–65 daq | Amaliy mashg'ulot | Windows Security orqali tezkor va to'liq skanerlash, fleshkani tekshirish, parol kuchini baholash algoritmi |
| 65–75 daq | Tezkor nazorat | 5 ta savol-javob va vaziyatli (case-study) tahlil |
| 75–80 daq | Xulosa va uyga vazifa | Muhim qoidalarni jamlash va uyga vazifani tushuntirish |

---

## 2. Dars konspekti

### 2.1. Kompyuter xavfsizligi va kibergigiyena tushunchasi

**Kompyuter xavfsizligi (Computer Security)** — bu kompyuter apparat vositalari, dasturiy ta'minot va unda saqlanayotgan shaxsiy ma'lumotlarni ruxsatsiz kirish, o'g'irlanish, buzilish yoki yo'qotilishdan himoya qilish choralari majmuasidir.

Axborot xavfsizligining 3 ta klassik ustuni (CIA triada):
1. **Maxfiylik (Confidentiality):** Ma'lumotlarni faqat ruxsati bor insonlar ko'ra olishi (parol, shifrlash).
2. **Yaxlitlik (Integrity):** Ma'lumotlarning buzilmasdan, ruxsatsiz o'zgartirilmasdan asl holicha saqlanishi.
3. **Mavjudlik (Availability):** Kerakli paytda tizim va ma'lumotlarga to'siqsiz kirish imkoniyatining bo'lishi.

### 2.2. Zararli dasturlar (Malware) turlari

Zararli dasturiy ta'minot (**Malware** — Malicious Software) — kompyuter tizimiga zarar yetkazish, shaxsiy ma'lumotlarni o'g'irlash yoki foydalanuvchini boshqarishdan mahrum qilish maqsadida yozilgan dasturlardir.

Asosiy turlari:
1. **Klassik viruslar (Virus):** Boshqa qonuniy fayllar yoki dasturlarga yopishib olib, ular ishga tushganda o'z kodini ko'paytiruvchi va tizimni zararlaydigan dasturlar.
2. **Chuvalchanglar (Worm):** Foydalanuvchining aralashuvisiz, lokal tarmoq yoki internet orqali o'z-o'zidan bir kompyuterdan ikkinchisiga tarqaluvchi zararli dasturlar.
3. **Troyan oti (Trojan Horse):** O'zini foydali yoki bepul o'yin/dastur qilib ko'rsatib, kompyuterga yashirin kirib oluvchi va jinoyatchiga tizimni masofadan boshqarish imkonini beruvchi zararli kod.
4. **Ayg'oqchi dasturlar (Spyware):** Foydalanuvchining klaviaturada nimalarni terayotganini (login, parol, karta raqami) yashirincha yozib olib, tajovuzkorga jo'natuvchi dasturlar (Keyloggerlar).
5. **Tovlamachi / Shifrlash viruslari (Ransomware):** Kompyuterdagi barcha fotosurat, hujjat va fayllarni shifrlab (qulflab) qo'yib, ularni ochish uchun foydalanuvchidan kriptovalyutada to'lov talab qiluvchi eng xavfli viruslar (masalan: WannaCry).
6. **Reklama dasturlari (Adware):** Ekranda doimiy ravishda noqulay va keraksiz reklama bannerlarini chiqarib chalg'ituvchi dasturlar.

### 2.3. Antivirus dasturlari va ularning ishlash mexanizmi

**Antivirus** — bu zararli dasturlarni aniqlash, ularning faoliyatini to'xtatish, zararlangan fayllarni davolash yoki o'chirish uchun xizmat qiluvchi himoya dasturidir.

Eng mashhur antiviruslar:
- **Windows Security (Microsoft Defender):** Windows 10 va 11 tizimlariga integratsiya qilingan, bepul va yetarli darajada kuchli antivirus.
- **Kaspersky, ESET NOD32, Bitdefender, Avast, Norton:** Kengaytirilgan imkoniyatlarga ega tijoriy antivirus majmualari.

Antivirusning ishlash bosqichlari:
1. **Real vaqt rejimida himoya (Real-time Protection):** Har safar biror dastur ishga tushganda yoki fayl yuklanganda, antivirus uni fonda tekshiradi.
2. **Imzo (Signature) tahlili:** Antivirus bazasidagi ma'lum viruslarning raqamli izlari (xesh kodlari) bilan yangi fayllarni solishtirish.
3. **Evristik tahlil (Heuristic Analysis):** Dasturning shubhali xatti-harakatlarini (masalan, tizim registrini o'zgartirish, tizim fayllarini shifrlashga urinish) tahlil qilib, hali bazada yo'q yangi viruslarni aniqlash.
4. **Karantin (Quarantine):** Shubhali faylni maxsus izolyatsiyalangan papkaga ko'chirib, uning ishlashini to'liq bloklash.
5. **Doimiy yangilanish (Definitions Update):** Har kuni dunyoda minglab yangi viruslar paydo bo'ladi. Shu sababli antivirus bazasi muntazam ravishda yangilanib turishi shart.

### 2.4. Parol madaniyati va 2FA (Ikki bosqichli himoya)

- **Kuchli parol qoidalari:**
  - Kamida 12 ta belgidan iborat bo'lishi kerak.
  - Katta va kichik harflar (`A-Z`, `a-z`), raqamlar (`0-9`) va maxsus belgilar (`!@#$%^&*`) aralashmasi bo'lishi lozim.
  - Ism, tug'ilgan sana, `123456`, `qwerty` yoki telefon raqami kabi oson topiladigan so'zlardan foydalanmaslik.
  - Turli xil saytlar uchun bitta paroldan foydalanmaslik (har bir xizmat uchun alohida parol).
- **2FA (Two-Factor Authentication / Ikki bosqichli autentifikatsiya):**
  - Akkauntga kirishda faqat login va parolni bilish yetarli emas. Tizim ikkinchi omilni — telefoningizga kelgan bir martalik SMS kodni yoki autentifikator ilovasidagi (Google Authenticator) 6 xonali kodni talab qiladi.
  - 2FA yoqilgan bo'lsa, hatto parolingiz o'g'irlangan taqdirda ham jinoyatchi hisobingizga kira olmaydi.

### 2.5. Fleshka va tashqi xotira xavfsizligi

USB fleshkalar orqali virus yuqishining oldini olish qoidalari:
1. Fleshkani kompyuterga ulagach, darhol unga kirmasdan, sichqonchaning o'ng tugmasini bosib «Scan with Microsoft Defender» (Antivirus bilan tekshirish) amalini bajaring.
2. Windows tizimida **Autorun (Avto-ishga tushirish)** funksiyasi o'chirilgan bo'lishi kerak (zamonaviy Windows versiyalarida xavfsizlik uchun u avtomatik bloklanadi).
3. Fleshkada g'alati `.lnk` (yorliq / shortcut) yoki `.vbs` kengaytmali fayllar paydo bo'lsa, ularni aslo bosmang.

---

## 3. Amaliy topshiriqlar va yechimlari

### 1-topshiriq. Windows Security dasturini ishga tushirish va tezkor skanerlash
**Vazifa:** Windows 10/11 tizimida o'rnatilgan Microsoft Defender dasturini oching, oxirgi tekshiruv vaqtini ko'ring va «Quick scan» (Tezkor skanerlash) amalini bajaring.
**Yechim:**
- `Win + S` qidiruviga «Windows Security» yoki «Xavfsizlik» deb yozib dastur ochiladi.
- «Virus & threat protection» (Viruslar va tahdidlardan himoyalanish) bo'limi tanlanadi.
- «Quick scan» tugmasi bosiladi. Antivirus tizimning eng nozik joylarini (xotira, tizim papkalari) 1-3 daqiqa ichida tekshiradi va natijani ko'rsatadi.

### 2-topshiriq. Fleshkani antivirus orqali maxsus tekshirish
**Vazifa:** Tashqi USB fleshkani kompyuterga ulang va faqat shu fleshkaning o'zini antivirus orqali to'liq tekshirish usulini ko'rsating.
**Yechim:**
- «This PC» (Mening kompyuterim) oynasi ochiladi.
- Ulangan USB fleshka belgisi ustiga sichqonchaning o'ng tugmasi bosiladi.
- Kontekst menyusidan «Scan with Microsoft Defender...» tanlanadi.
- Tekshiruv yakunlanib, «No current threats» (Tahdidlar aniqlanmadi) xabari olingach, fleshkadan xavfsiz foydalanish mumkin.

### 3-topshiriq. Kuchli va esda qoladigan parol yaratish
**Vazifa:** O'zingiz uchun buzilmas, kamida 12 belgidan iborat, katta-kichik harf, raqam va maxsus belgi qatnashgan kuchli parol formulasini ishlab chiqing (Masalan, shior yoki jumlalar asosida).
**Yechim:**
- Oddiy so'zlardan qochish uchun ibora tanlanadi: *«Men maktabda 8-sinfda o'qiyman va ITni sevaman!»*
- Har bir so'zning bosh harfi olinadi: `M m 8-s o' v IT s!` -> `Mm8-so'vITs!`
- Parol shakli: `Mm8@sov_IT#2026` (15 ta belgi, esda qolishi oson, lekin maxsus dasturlar bilan ham yillab buzib bo'lmaydi).

---

## 4. Tezkor nazorat savollari (javoblari bilan)

1. **Savol:** Ransomware (shifrlash virusi) kompyuterga qanday zarar keltiradi?
   **Javob:** U kompyuterdagi barcha fotosuratlar, hujjatlar va fayllarni shifrlab qulflab qo'yadi va ochish uchun foydalanuvchidan to'lov (tovlamachilik) talab qiladi.
2. **Savol:** Troyan oti (Trojan Horse) virusidan nima bilan farqlanadi?
   **Javob:** Virus boshqa fayllarni zararlab o'zini ko'paytiradi. Troyan esa foydali dastur niqobi ostida tizimga kirib, tajovuzkorga masofadan boshqarish imkonini beradi (o'zini ko'paytirmaydi).
3. **Savol:** Antivirusdagi «Karantin» (Quarantine) nima vazifani bajaradi?
   **Javob:** Karantin shubhali yoki zararlangan faylni maxsus xavfsiz izolyatsiyaga olib, uning tizimga ta'sir o'tkazishini to'xtatadi.
4. **Savol:** 2FA (Ikki bosqichli autentifikatsiya) nima uchun kerak?
   **Javob:** Agar parol o'g'irlansa ham, ikkinchi omil (telefon orqali tasdiqlash) bo'lmasa begona shaxs akkauntga kira olmaydi.
5. **Savol:** Nima uchun kompyuterga yangi ulangan fleshkani darhol ochmasdan, avval skaner qilish kerak?
   **Javob:** Begona kompyuterlardan fleshkaga yashirin avto-ishga tushuvchi viruslar yozilgan bo'lishi mumkin. Skanerlash ularni aniqlab zararsizlantiradi.
