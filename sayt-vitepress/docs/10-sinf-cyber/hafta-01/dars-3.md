---
title: "3-dars. Kibertahdidlarning turlari (2-qism): ijtimoiy muhandislik, fishing va email tahlili"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (Cyber)", "link": "/10-sinf-cyber/"}, "week": {"n": 1, "link": "/10-sinf-cyber/hafta-01/"}, "g": 3, "title": "Kibertahdidlarning turlari (2-qism): ijtimoiy muhandislik, fishing va email tahlili", "lead": "Kibertahdidlarning turlari (2-qism): ijtimoiy muhandislik, fishing turlari va elektron pochta xavfsizligi tahlili", "slide": "/slaydlar/10-sinf-cyber/hafta-01/dars-3.html", "test": "/slaydlar/10-sinf-cyber/hafta-01/dars-3-test.html", "tabs": [{"g": 1, "link": "/10-sinf-cyber/hafta-01/dars-1", "current": false}, {"g": 2, "link": "/10-sinf-cyber/hafta-01/dars-2", "current": false}, {"g": 3, "link": "/10-sinf-cyber/hafta-01/dars-3", "current": true}], "prev": {"g": 2, "title": "Kibertahdidlarning turlari (1-qism): zararli dasturlar va DoS/DDoS hujumlari", "link": "/10-sinf-cyber/hafta-01/dars-2"}, "next": null}
---

---
title: "Kibertahdidlarning turlari (2-qism): ijtimoiy muhandislik, fishing va email tahlili"
description: "Ijtimoiy muhandislik turlari (Spear, Whaling, BEC) hamda Thunderbird, MX Toolbox va VirusTotal yordamida fishing xabarlarini tahlil qilish"
dars: 3
hafta: 1
sinf: 10-sinf-cyber
---

<div class="blk">

## <Icon name="file-text" /> Reja

1. Ijtimoiy muhandislik (Social Engineering) tushunchasi va psixologik usullar.
2. Fishing turlari: Ommaviy fishing, Spear Phishing, Whaling va BEC.
3. Elektron pochta xavfsizligi asoslari: Sarlavhalar (Headers), SPF, DKIM va DMARC.
4. Thunderbird dasturida xat manbasini (Message Source) ko'rish.
5. MX Toolbox orqali pochta sarlavhalarini onlayn tahlil qilish.
6. urlscan.io va VirusTotal platformalari yordamida xavfsiz tekshiruv.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Nazariy qism

### 1. Ijtimoiy muhandislik nima?

**Ijtimoiy muhandislik (Social Engineering / Human Hacking)** — bu kompyuter tizimlaridagi texnik zaifliklarga emas, balki inson psixologiyasiga (ishonuvchanlik, qo'rquv, qiziqish, shoshilinchlik) tayanib amalga oshiriladigan firibgarlikdir.

Buzg'unchilar quyidagi his-tuyg'ulardan foydalanadilar:
- **Qo'rquv va shoshilinchlik:** «24 soat ichida kirmasangiz hisobingiz bloklanadi!»
- **Ochko'zlik va qiziqish:** «Siz 10 000 000 so'm yutdingiz! Yutuqni olish uchun kartangizni kiriting.»
- **Rahbariyat obro'si:** «Men bosh direktorman, zudlik bilan ushbu ilovani tekshiring!»

### 2. Fishingning asosiy turlari

```
+--------------------------------------------------------------------------+
|                            FISHING TURLARI                               |
+--------------------------------------------------------------------------+
| 1. Ommaviy fishing (Mass Phishing) -> Millionlab odamlarga bir xil xat  |
| 2. Spear Phishing -> Aniq bir xodim yoki tashkilotga moslashtirilgan     |
| 3. Whaling -> Kompaniya rahbarlari va boy shaxslarga qaratilgan         |
| 4. BEC (Business Email Compromise) -> Direktor nomidan moliyaviy hiyla   |
| 5. Smishing / Vishing -> SMS va telefon qo'ng'iroqlari orqali aldov     |
+--------------------------------------------------------------------------+
```

### 3. Fishing xatini qanday aniqlash mumkin?

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

### 4. Pochtani himoyalash mexanizmlari (SPF, DKIM, DMARC)

1. **SPF (Sender Policy Framework):** Domen egasi DNS tizimida qaysi server IP manzillari xat jo'nata olishini belgilab qo'yadi.
2. **DKIM (DomainKeys Identified Mail):** Xatga maxsus raqamli kriptografik imzo qo'yiladi. Xat yo'lda o'zgartirilmaganligi kafolatlanadi.
3. **DMARC:** Agar xat SPF yoki DKIM tekshiruvidan o'tmasa, uni rad etish (`p=reject`) yoki karantinga olish (`p=quarantine`) siyosatini boshqaradi.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy laboratoriya

### 1-qadam: Thunderbird da xat sarlavhalarini ochish
1. Thunderbird dasturida xatni tanlang.
2. Klaviaturada `Ctrl + U` (yoki menyudan **View -> Message Source**) tugmasini bosing.
3. Sarlavhalardagi `Received: from ...` qatoridan yuboruvchining haqiqiy IP manzilini toping.

### 2-qadam: MX Toolbox vositasida tahlil qilish
1. Brauzerda `mxtoolbox.com/EmailHeaders.aspx` manzilini oching.
2. Thunderbird dan ko'chirilgan sarlavhalarni joylashtiring va **Analyze** tugmasini bosing.
3. SPF, DKIM va DMARC natijalarini o'rganing.

### 3-qadam: urlscan.io yordamida havolani tekshirish
1. Xatdagi havolani o'z brauzeringizda **OCHMANG!**
2. Havolani `urlscan.io` saytiga kiriting va xavfsiz sandbox muhitida tekshiring.

### 4-qadam: VirusTotal platformasida faylni skanerlash
1. Xatdagi ilovani (`testvirus.zip`) kompyuterga saqlang, lekin **OCHMANG!**
2. `virustotal.com` saytiga yuklab, 70 dan ortiq antiviruslarning xulosasini ko'ring.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy topshiriqlar

### 1. Phishing va oddiy spam farqi &lt;Badge type="tip" text="oson" />
Oddiy reklama spami bilan kiberfishing o'rtasidagi asosiy farq nimada? Maqsad va xavf jihatidan tushuntiring.

### 2. Havola domenini tahlil qilish &lt;Badge type="tip" text="oson" />
Quyidagi havolani o'rganing: `http://payme.uz.security-check-login.com/pay`. Ushbu havoladagi haqiqiy asosiy domen qaysi va `payme.uz` so'zi qanday maqsadda qo'yilgan?

### 3. SPF yozuvining roli &lt;Badge type="warning" text="o'rta" />
Nima sababdan SPF yozuvi mavjud bo'lmagan domen nomidan buzg'unchilar osonlikcha xat soxtalashtirib yubora oladi?

### 4. DMARC siyosati darajalari &lt;Badge type="warning" text="o'rta" />
DMARC yozuvidagi `p=none`, `p=quarantine` va `p=reject` qiymatlarining bir-biridan farqini tushuntiring. Qaysi biri eng yuqori himoya hisoblanadi?

### 5. Spear Phishing va Whaling taqqoslovi &lt;Badge type="warning" text="o'rta" />
Nima sababdan Whaling hujumlarida buzg'unchilar oddiy xodimlarga emas, aynan bosh buxgalter yoki bosh direktorga nishon oladi?

### 6. Shubhali fayl kengaytmasi &lt;Badge type="tip" text="oson" />
Sizga kutilmagan manzildan `hisob-faktura.pdf.exe` nomli fayl keldi. Windows tizimida nima uchun bu fayl xavfli va nima sababdan kengaytmalarni ko'rsatish rejimini yoqish muhim?

### 7. Thunderbird da manba tahlili &lt;Badge type="danger" text="qiyin" />
Thunderbird da ochilgan xat sarlavhasida `Received: from mail.attacker-server.ru [185.220.101.5]` va `From: ceo@company.uz` yozuvi ko'rindi. Bu ma'lumot nimani fosh qiladi?

### 8. Sandbox tekshiruvining afzalligi &lt;Badge type="warning" text="o'rta" />
Nima sababdan shubhali havolalarni shaxsiy brauzerda ochmasdan, urlscan.io yoki VirusTotal orqali tekshirish talab etiladi?

### 9. BEC (Business Email Compromise) dan himoya &lt;Badge type="danger" text="qiyin" />
Buxgalterga kompaniya rahbaridan: «Shoshilinch! Yangi hamkorga 50 000 dollar to'lovni o'tkazing, rekvizitlar ilovada» degan xat keldi. Buxgalter pulni o'tkazishdan oldin qanday xavfsizlik chorasini ko'rishi shart?

### 10. Tashkilot xavfsizlik chorasi &lt;Badge type="info" text="bonus" />
Kompaniyada xodimlarni fishingga tushib qolmasligi uchun tashkiliy va texnik chora-tadbirlar rejasini (kamida 4 ta chora) tuzing.

---

</div>

<div class="blk">

## <Icon name="file-text" /> O'z-o'zini tekshirish savollari

1. Ijtimoiy muhandislik qanday insoniy his-tuyg'ularga tayanadi?
2. Spear phishing va ommaviy phishing farqi nimada?
3. SPF va DKIM nima uchun birgalikda ishlatiladi?
4. DMARC siyosati nimani belgilaydi?
5. Nima uchun shubhali xat ilovalarini to'g'ridan-to'g'ri kompyuterda ochish xavfli?

---

</div>

<div class="blk">

## <Icon name="file-text" /> Foydali manbalar

- MX Toolbox Email Header Analyzer: `mxtoolbox.com/EmailHeaders.aspx`
- VirusTotal File & URL Scanner: `virustotal.com`
- URLScan.io Sandbox Scanner: `urlscan.io`

</div>

