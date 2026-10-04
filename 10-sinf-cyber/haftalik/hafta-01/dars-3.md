---
title: "Kibertahdidlarning turlari (2-qism): ijtimoiy muhandislik, fishing va email tahlili"
description: "Ijtimoiy muhandislik turlari (Spear, Whaling, BEC) hamda Thunderbird, MX Toolbox va VirusTotal yordamida fishing xabarlarini tahlil qilish"
dars: 3
hafta: 1
sinf: 10-sinf-cyber
---

# 3-dars. Kibertahdidlarning turlari (2-qism): ijtimoiy muhandislik, fishing va email tahlili

## Dars rejasi (80 daqiqa)

1. **Kirish va o'tgan mavzuni takrorlash (10 daqiqa):** Zararli dasturlar va DoS hujumlarini eslash, yangi mavzu maqsadlari.
2. **Nazariy qism (25 daqiqa):**
   - Ijtimoiy muhandislik (Social Engineering / Human Hacking) tushunchasi va psixologik manipulyatsiya.
   - Fishingning asosiy turlari:
     1. Ommaviy fishing (Mass Phishing);
     2. Maqsadli fishing (Spear Phishing);
     3. Katta ov / Rahbarlarga qaratilgan fishing (Whale Phishing);
     4. Korporativ pochtani egallash (Business Email Compromise — BEC);
     5. Klonlangan fishing va Domen soxtalashtirish (DNS / Domain Spoofing).
   - Elektron pochta sarlavhalari (Headers) tuzilishi: Return-Path, Received, Message-ID.
   - Pochtani himoyalashning 3 ustuni: SPF, DKIM va DMARC.
3. **Amaliy laboratoriya mashg'uloti (30 daqiqa):**
   - Thunderbird yordamida shubhali `.eml` faylini ochish va «View Message Source» orqali sarlavhalarni ajratib olish.
   - MX Toolbox platformasida email sarlavhalarini tahlil qilish (SPF, DKIM, DMARC tekshiruvi).
   - urlscan.io yordamida havolani xavfsiz tekshirish (domen va DNS yozuvlari).
   - VirusTotal platformasida shubhali ilovalarni (`testvirus.zip`) ochmasdan skanerlash.
4. **Mustaqil topshiriqlar va muhokama (10 daqiqa):** 10 ta amaliy vazifani yechish.
5. **Xulosa va baholash (5 daqiqa):** Olingan natijalarni sarhisob qilish, baholash va haftalik uy vazifasi.

---

## Asosiy tushunchalar

- **Ijtimoiy muhandislik (Social Engineering):** Inson psixologiyasi, his-tuyg'ulari (qo'rquv, qiziqish, shoshilinchlik, ochko'zlik, ishonch)dan foydalanib, odamlarni maxfiy ma'lumotlarni oshkor qilishga yoki xavfli harakatlarni bajarishga undovchi manipulyatsiya usullari majmui.
- **Fishing (Phishing):** Ijtimoiy muhandislikning eng keng tarqalgan turi bo'lib, buzg'unchilar soxta elektron xatlar, SMS (smishing) yoki veb-saytlar orqali foydalanuvchining login, parol va bank kartasi ma'lumotlarini o'g'irlashidir.
- **Spear Phishing:** Muayyan bir shaxsga yoki tashkilotga qaratilgan, oldindan o'rganilgan ma'lumotlar asosida juda ishonarli qilib tayyorlangan maqsadli fishing.
- **Whale Phishing (Whaling):** Katta tashkilot rahbarlari, direktorlar yoki boy shaxslarni nishonga oluvchi maxsus yuqori darajali fishing.
- **BEC (Business Email Compromise):** Buzg'unchi o'zini kompaniya direktori yoki yetkazib beruvchi hamkor deb tanishtirib, hisobchidan soxta hisob raqamga shoshilinch pul o'tkazishni talab qilishi.
- **Email Headers (Pochta sarlavhalari):** Elektron xatning texnik metama'lumotlari bo'lib, uning qaysi IP manzildan, qaysi serverlar orqali uzatilganini va qanchalik haqiqiyligini ko'rsatadi.
- **SPF (Sender Policy Framework):** Muayyan domen nomidan qaysi IP manzillar va serverlar elektron xat yuborishga vakolatli ekanligini ko'rsatuvchi DNS yozuvi.
- **DKIM (DomainKeys Identified Mail):** Xat jo'natuvchi domenga tegishli ekanligini va yo'lda o'zgartirilmaganligini tasdiqlovchi raqamli kriptografik imzo.
- **DMARC (Domain-based Message Authentication, Reporting, and Conformance):** Agar kelgan xat SPF yoki DKIM tekshiruvidan o'tmasa, uni nima qilish kerakligini (rad etish, karantinga olish yoki qabul qilish) belgilovchi qoida.
- **VirusTotal:** Yuklangan fayllar yoki URL manzillarni 70 dan ortiq antivirus va xavfsizlik dvigatellari yordamida onlayn tekshiruvchi global platforma.

---

## Dars mazmuni

### 1. Ijtimoiy muhandislik va psixologik tuzoqlar

Kiberjinoyatchilar ko'pincha texnik himoyani buzishga urinmaydi, balki to'g'ridan-to'g'ri inson psixologiyasiga zarba beradi. Asosiy psixologik tuzoqlar:
1. **Shoshilinchlik va qo'rquv:** «Hisobingiz bloklandi — 24 soat ichida kirmasangiz pulingiz kuyadi!»
2. **Kutilmagan mukofot yoki foyda:** «Tabriklaymiz, siz 10 million so'm yutib oldingiz! Pulingizni olish uchun kartangizni tasdiqlang.»
3. **Rahbariyat nomidan bosim:** «Men bosh direktorman. Zudlik bilan ushbu ilovani tekshirib natijasini ayting.»
4. **Qiziqish (Curiosity):** «Xodimlar oylik maoshlari to'liq ro'yxati (yashirin hujjat).zip».

### 2. Fishing elektron xatining anatomiyasi

Keling, amaliy ssenariydagi soxta xabarni ko'rib chiqaylik:

```email
From: "UzSanoat Bank" <support@uzsanoat-secure.com>
To: student@example.com
Subject: Hisobingiz bloklandi — Darhol qayta tiklang
Date: Mon, 10 Nov 2025 09:12:01 +0500

Hurmatli mijoz,
Sizning hisobingizda shubhali harakatlar aniqlandi. Xavfsizlik uchun hisobingizni
hozirgacha faollashtirish uchun iltimos quyidagi havolani bosib, bank ma'lumotlaringizni tasdiqlang:
http://uzsanoat-bank.verify-secure-login.com/confirm

Agar 24 soat ichida tasdiqlanmasa, hisobingiz bloklanadi.
Rahmat.
```

**Buzg'unchi belgilari tahlili:**
1. **Yuboruvchi domeni:** `support@uzsanoat-secure.com` — rasmiy bank domeni emas, yaqinda ochilgan shubhali domen.
2. **Psixologik bosim:** «Hisobingiz bloklandi», «Darhol», «24 soat ichida».
3. **Soxta havola:** `verify-secure-login.com` — asosiy domen bu, `uzsanoat-bank` esa odamlarni aldash uchun oldiga qo'yilgan subdomen!
4. **Protokol:** `http://` — banklar hech qachon shifrlanmagan HTTP orqali ma'lumot so'ramaydi, faqat `https://` bo'lishi kerak.

---

### 3. Pochtani himoyalashning 3 ustuni (SPF, DKIM, DMARC)

```
        +-------------------------------------------------------+
        |                 EMAIL XAVFSIZLIK TRIADASI             |
        +-------------------------------------------------------+
        |  SPF   -->  IP manzil ruxsatini tekshiradi             |
        |  DKIM  -->  Raqamli imzo orqali yaxlitlikni tasdiqlaydi|
        |  DMARC -->  Soxta xatlarni bloklash siyosatini yuritadi |
        +-------------------------------------------------------+
```

1. **SPF:** Xat yuborilgan IP manzil haqiqatan ham ushbu domen egasiga tegishlimi?
2. **DKIM:** Xat yo'lda o'zgartirilmaganmi va jo'natuvchi domenga mansub kriptografik kalit bilan imzolanganmi?
3. **DMARC:** Agar SPF yoki DKIM «FAIL» bersa, xatni nima qilish kerak? (`p=reject` — to'liq rad etish, `p=quarantine` — spamga tashlash).

---

## Amaliy laboratoriya mashg'uloti

### 1-qadam: Thunderbird da xat sarlavhalarini ochish
1. Thunderbird dasturida xatni tanlang.
2. Klaviaturada `Ctrl + U` (yoki menyudan **View -> Message Source**) tugmasini bosing.
3. Quyidagi asosiy sarlavhalarni tekshiring:
   - `Received: from ... [IP manzil]` — xat aslida qaysi serverdan jo'natilgan?
   - `Authentication-Results:` — SPF va DKIM tekshiruv natijalari nima deydi?
   - `Return-Path:` — javob xati qayerga qaytadi?

### 2-qadam: MX Toolbox yordamida tahlil
1. `mxtoolbox.com/EmailHeaders.aspx` manziliga o'ting.
2. Thunderbird dan ko'chirilgan to'liq sarlavha matnini joylashtiring va **Analyze** tugmasini bosing.
3. Natijada yuboruvchining IP manzili, geolokatsiyasi, SPF va DMARC holati jadvalda ko'rsatiladi.

### 3-qadam: urlscan.io da havolani tekshirish
1. Xatdagi havolani o'z brauzeringizda **OCHMANG!**
2. Havoladan nusxa oling va `urlscan.io` qidiruv joyiga joylashtiring.
3. Tizim havolani sandbox ichida ochadi, ekranning skrinshotini oladi va uning qaysi IP ga ulanganini yoki domenda DNS xatosi borligini ko'rsatadi.

### 4-qadam: VirusTotal yordamida ilovani skanerlash
1. Xatda biriktirilgan shubhali `testvirus.zip` faylini kompyuterga saqlang, ammo **OCHMANG!**
2. `virustotal.com/gui/home/upload` saytiga kiring.
3. Faylni yuklang. 70 dan ortiq antivirus dvigatellari (Kaspersky, Microsoft Defender, Bitdefender, ESET) fayl ichida troyan yoki zararli skript bor-yo'qligi bo'yicha hisobot taqdim etadi.

---

## Mustaqil topshiriqlar

### 1. Phishing va oddiy spam farqi · oson
Spam elektron xat bilan fishing xati o'rtasidagi asosiy farq nimada?
**Yechim:** Spam — bu foydalanuvchiga uning roziligisiz yuborilgan ommaviy reklama xatlaridir (u zarar yetkazmasligi mumkin). Fishing esa firibgarlik maqsadida yuborilgan bo'lib, uning aniq niyati — foydalanuvchini aldab shaxsiy login, parol yoki bank kartasi ma'lumotlarini o'g'irlashdir.

### 2. URL subdomen tuzilishi tahlili · oson
Foydalanuvchiga quyidagi havola keldi: `http://payme.uz.security-check-login.com/pay`. Ushbu havolaning haqiqiy asosiy domeni qaysi va u nega xavfli?
**Yechim:** Bu havolaning haqiqiy domeni oxirgi nuqtadan oldingi nom — `security-check-login.com` hisoblanadi. `payme.uz` esa buzg'unchi tomonidan odamlarni chalg'itish uchun yaratilgan oddiy subdomendir. Bu soxta phishing sayti.

### 3. SPF tekshiruvining vazifasi · o'rta
Nima sababdan SPF yozuvi mavjud bo'lmagan domen nomidan buzg'unchilar osonlikcha xat soxtalashtirib yubora oladi?
**Yechim:** Elektron pochta protokoli (SMTP) dastlab yuboruvchi manzilini tekshirish mexanizmisiz yaratilgan. Agar domenda SPF yozuvi bo'lmasa, qabul qiluvchi pochta serveri xat haqiqiy bank serveridan keldimi yoki xakerning serveridan keldimi, bila olmaydi va uni qabul qiladi.

### 4. DMARC siyosati darajalari · o'rta
DMARC yozuvidagi `p=none`, `p=quarantine` va `p=reject` qiymatlarining farqini tushuntiring. Qaysi biri eng yuqori himoyani ta'minlaydi?
**Yechim:**
- `p=none`: Xat qabul qilinadi, faqat domen egasiga tahlil uchun hisobot yuboriladi (monitoring).
- `p=quarantine`: Shubhali soxta xat foydalanuvchining «Spam» yoki karantin jildiga tashlanadi.
- `p=reject`: Eng yuqori himoya — soxta xat server tomonidan darhol rad etiladi va foydalanuvchiga umuman yetib bormaydi.

### 5. Spear Phishing va Whaling taqqoslovi · o'rta
Nima sababdan Whaling hujumlarida buzg'unchilar oddiy xodimlarga emas, aynan bosh buxgalter yoki bosh direktorga nishon oladi?
**Yechim:** Chunki rahbarlar va bosh buxgalterlar katta moliyaviy mablag'larni boshqarish, millionlab pul o'tkazmalarini imzolash va korporativ maxfiy ma'lumotlarga to'liq kirish huquqiga (imtiyoziga) ega. Bitta muvaffaqiyatli whaling hujumi xakerga ulkan moddiy manfaat keltiradi.

### 6. Shubhali xat ilovasi xavfsizligi · oson
Sizga kutilmagan manzildan `hisob-faktura.pdf.exe` nomli fayl keldi. Windows tizimida nima uchun bu fayl xavfli va nima sababdan oxiridagi kengaytmani ko'rish muhim?
**Yechim:** Windows tizimida standart sozlamalar bo'yicha ma'lum fayl kengaytmalari yashiriladi. Foydalanuvchi faqat `hisob-faktura.pdf` deb o'ylab, PDF ochilmoqda deb o'ylaydi, aslida esa bu `.exe` bo'lib, ishga tushuvchi zararli dastur (troyan) hisoblanadi.

### 7. Thunderbird da Message Source tahlili · qiyin
Thunderbird da ochilgan xat sarlavhasida `Received: from mail.attacker-server.ru [185.220.101.5]` va `From: ceo@company.uz` yozuvi ko'rindi. Bu ma'lumot nimani fosh qiladi?
**Yechim:** Bu xatning soxtalashtirilganini (Email Spoofing) fosh qiladi. Xat matnida yuboruvchi sifatida O'zbekistondagi kompaniya direktori ko'rsatilgan bo'lsa-da, haqiqiy texnik uzatish Rossiyadagi shubhali IP manzildagi serverdan amalga oshirilgan.

### 8. urlscan.io va VirusTotal platformalari roli · o'rta
Nima sababdan shubhali havolalarni shaxsiy brauzerda ochmasdan, urlscan.io yoki VirusTotal orqali tekshirish talab etiladi?
**Yechim:** Shaxsiy brauzerda ochilganda, sayt brauzer zaifliklaridan (Drive-by download) foydalanib kompyuterga zararli skript yuklashi yoki foydalanuvchi ma'lumotlarini o'g'irlashi mumkin. urlscan.io va VirusTotal esa xavfsiz izolyatsiya qilingan serverlarda (Sandbox) tekshiruv o'tkazadi va foydalanuvchi kompyuteriga hech qanday xavf yetkazmaydi.

### 9. BEC (Business Email Compromise) dan himoyalanish · qiyin
Buxgalterga kompaniya rahbaridan: «Shoshilinch! Yangi hamkorga 50 000 dollar to'lovni o'tkazing, rekvizitlar ilovada» degan xat keldi. Buxgalter pulni o'tkazishdan oldin qanday xavfsizlik chorasini ko'rishi shart?
**Yechim:** Buxgalter hech qachon faqat elektron xatga tayanmasligi kerak. U muqobil aloqa kanali orqali (masalan, telefon orqali qo'ng'iroq qilib yoki shaxsan kabinetiga kirib) rahbar bilan bog'lanishi va bu to'lov haqiqatan ham u tomonidan buyurilganligini tasdiqlashi (Out-of-band verification) shart.

### 10. Korxona kiberxavfsizlik himoya siyosati ishlab chiqish · bonus
Kompaniyada xodimlarni fishingga tushib qolmasligi uchun tashkiliy va texnik chora-tadbirlar rejasini (kamida 4 ta chora) tuzing.
**Yechim:**
1. Korporativ pochtada DMARC (`p=reject`), SPF va DKIM siyosatlarini majburiy joriy etish;
2. Pochtani avtomatlashtirilgan spam-filtr va Antivirus tekshiruvidan (masalan, SpamAssassin, Microsoft Defender for Office 365) o'tkazish;
3. Barcha tashqi kelgan xatlarga katta qizil yozuv bilan: `[DIQQAT: Ushbu xat tashqaridan kelgan]` ogohlantirishini qo'yish;
4. Xodimlar uchun har oy simulyatsion fishing mashg'ulotlarini o'tkazish va zaif xodimlarni qayta o'qitish.

---

## Tezkor savol-javob

1. **Savol:** Fishing hujumining asosiy maqsadi nima?
   **Javob:** Insonlarni aldab, shaxsiy ma'lumotlar, parollar yoki bank kartasi ma'lumotlarini o'g'irlash.
2. **Savol:** SPF nimani tekshiradi?
   **Javob:** Xat yuborgan server IP manzili haqiqatan ham ushbu domen egasi tomonidan ruxsat etilganligini.
3. **Savol:** Shubhali faylni kompyuterda ochmasdan qayerda tekshirish mumkin?
   **Javob:** VirusTotal platformasida.
4. **Savol:** BEC hujumida hujumchi kimning nomidan ish ko'radi?
   **Javob:** Tashkilot rahbari yoki ishonchli biznes hamkori nomidan.

---

## Mentor uchun eslatma

- Darsda o'quvchilarga haqiqiy fishing xabari misolini (Thunderbird yoki brauzerda) ko'rsatib, domen nomidagi soxtalikni o'zlari topishlariga imkon bering.
- MX Toolbox va VirusTotal platformalarining jonli namoyishini o'tkazing.
- O'quvchilarga 1-hafta uy vazifasini topshirish tartibini tushuntiring.
