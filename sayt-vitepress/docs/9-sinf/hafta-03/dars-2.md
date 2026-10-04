---
title: "8-dars. Foydalanuvchi formalari, kiritish maydonlari va xatoliklar dizayni (Form Wireframing)"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf", "link": "/9-sinf/"}, "week": {"n": 3, "link": "/9-sinf/hafta-03/"}, "g": 8, "title": "Foydalanuvchi formalari, kiritish maydonlari va xatoliklar dizayni (Form Wireframing)", "lead": "Kiritish elementlari (Input, Dropdown, Radio, Checkbox), maydon holatlari, inline validation va xatoliklardan qutqaruvchi qulay interfeyslar.", "slide": "/slaydlar/9-sinf/hafta-03/dars-2.html", "tabs": [{"g": 7, "link": "/9-sinf/hafta-03/dars-1", "current": false}, {"g": 8, "link": "/9-sinf/hafta-03/dars-2", "current": true}, {"g": 9, "link": "/9-sinf/hafta-03/dars-3", "current": false}], "prev": {"g": 7, "title": "Axure RP: Dinamik panellar va interaktiv bog'lanishlar (Interactions)", "link": "/9-sinf/hafta-03/dars-1"}, "next": {"g": 9, "title": "Wireframe loyihasini yakunlash, annotatsiyalar va Figmaga eksport", "link": "/9-sinf/hafta-03/dars-3"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Formalar (Forms):** Foydalanuvchidan ma'lumot olish (ro'yxatdan o'tish, qidiruv, to'lov) uchun xizmat qiluvchi asosiy muloqot ko'prigi.
- **Forma anatomiyasi:** Label (doimiy nom) + Input (kiritish qutisi) + Placeholder (namuna matn) + Helper text (tushuntirish) + CTA (harakat tugmasi).
- **Elementlar farqi:** Radio Button (faqat 1 ta tanlov), Checkbox (bir nechta tanlov yoki rozilik), Dropdown (uzun ro'yxatdan 1 ta tanlov).
- **Maydon holatlari:** Default, Focus (kursorda), Filled (to'ldirilgan), Error (xato), Success (tasdiqlangan), Disabled (nofaol).
- **Inline Validation:** Xatolikni forma jo'natilgandan keyin emas, balki maydon tagida darhol, tushunarli va yordam beruvchi ohangda ko'rsatish.
- **Form Fatigue (Charchoq):** Juda ko'p va keraksiz maydonlar so'rash mijozlarning saytni tark etishiga sabab bo'ladi. Kamroq maydon — ko'proq natija.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Nega «Placeholder» hech qachon «Label» o'rnini bosa olmaydi?

Ba'zi tajribasiz dizaynerlar joyni tejash uchun maydon tepasiga yozuv (Label) qo'ymasdan, faqat maydon ichiga kulrang matn (Placeholder) yozib qo'yishadi.
Nega bu katta UX xatosi?
1. Foydalanuvchi maydon ustiga chertib yozishni boshlaganda Placeholder yo'qolib ketadi.
2. Agar biror narsa chalg'itsa, inson: «Men bu maydonga telefon raqamimni yozyapmanmi yoki pasport seriyamnimi?» deb ikkilanib qoladi.
3. Kognitiv yuklama ortadi va xatolar ko'payadi.
4. **Oltin qoida:** Har doim maydon tepasida aniq va tushunarli Label bo'lishi shart!

### 2. Mikro-matnlar (Microcopy) san'ati

Xatolik yuz berganda kompyuterning odam bilan qanday gaplashishi foydalanuvchi tajribasini belgilaydi:
- **Yomon mikro-matn:** `«Xatolik! 400 Bad Request. Ma'lumot noto'g'ri.»` (Inson o'zini aybdor va nochor his qiladi).
- **Yaxshi mikro-matn:** `«Elektron pochtada @ belgisi tushib qoldi. Masalan: misol@gmail.com»` (Tizim do'stona tarzda xatoni va uning yechimini ko'rsatadi).

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Label** | Kiritish maydonining tepasida yoki yonida turuvchi rasmiy nomi |
| **Input Field** | Ma'lumot kiritiladigan to'rtburchak maydon |
| **Placeholder** | Maydon ichida foydalanuvchiga yordam tariqasida ko'rinib turadigan xira namuna matn |
| **Radio Button** | Bir nechta o'zaro bir-birini istisno qiluvchi variantdan faqat bittasini tanlash tugmasi |
| **Checkbox** | Bir vaqtning o'zida bir nechta mustaqil variantni tanlash yoki shartga rozilik bildirish katakchasi |
| **Dropdown (Select)** | Ochiluvchi ro'yxat bo'lib, ko'p sonli variantlar mavjud bo'lganda joyni tejash uchun ishlatiladi |
| **Inline Validation** | Ma'lumot kiritilishi bilanoq xato yoki to'g'rilikni maydon tagida darhol xabar qilish |
| **CTA (Call to Action)** | Asosiy harakatni bajaruvchi ko'zga tashlanuvchi tugma (masalan: «Yuborish») |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- 📉 **Expedia tajribasi:** Dunyoga mashhur sayohat portali Expedia o'zining to'lov formasidan bittagina keraksiz maydonni («Kompaniya nomi») olib tashlaganida, uning yillik daromadi birdaniga 12 million dollarga oshgan! Chunki odamlar bu maydonga nima yozishni bilmay, to'lovni bekor qilib chiqib ketishayotgan edi.
- 👁️ **Paroldagi ko'zcha:** Parol maydonidagi «Ko'z» (Show/Hide) belgisining qo'shilishi foydalanuvchilarning ro'yxatdan o'tishdagi xatolarini 40% ga kamaytirgan.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Savollar va topshiriqlar

### 1-topshiriq <Badge type="tip" text="oson" />
Formaning 4 ta asosiy qismini sanab bering va ularning vazifasini tushuntiring.

### 2-topshiriq <Badge type="tip" text="oson" />
Radio Button va Checkbox elementlari qachon ishlatiladi? Har biriga bittadan real misol keltiring.

### 3-topshiriq <Badge type="tip" text="oson" />
Kiritish maydoni (Text Field) qanday 5 ta asosiy holatda bo'lishi mumkin?

### 4-topshiriq <Badge type="warning" text="o'rta" />
Nima uchun maydon ichidagi Placeholder yozuvini maydon sarlavhasi (Label) o'rnida ishlatish noto'g'ri hisoblanadi?

### 5-topshiriq <Badge type="warning" text="o'rta" />
«Parol o'ylab toping» maydoni uchun yaxshi va tushunarli Helper text (yordamchi matn) hamda xatolik matniga misol yozing.

### 6-topshiriq <Badge type="warning" text="o'rta" />
Foydalanuvchi yashash viloyatini tanlashi kerak (O'zbekistonda 12 viloyat, Toshkent shahri va Qoraqalpog'iston). Bu yerda qaysi kiritish elementini (Radio, Checkbox yoki Dropdown) tanlagan ma'qul va nega?

### 7-topshiriq <Badge type="warning" text="o'rta" />
Form Fatigue (formalardan charchash) nima va dizayner uning oldini olish uchun nimalarga e'tibor qaratishi kerak?

### 8-topshiriq <Badge type="danger" text="qiyin" />
Ko'p bosqichli forma (Multi-step form / Wizard) nima? Nega 15 ta savoldan iborat bitta uzun sahifani 3 ta alohida bosqichga (1-qadam, 2-qadam, 3-qadam) bo'lish foydalanuvchiga ancha yengil tuyuladi?

### 9-topshiriq <Badge type="danger" text="qiyin" />
Mobil ekranda klaviatura ochilganda maydon pastda qolib, to'silib qolmasligi uchun UX dizayner wireframe yaratishda nimani hisobga olishi kerak?

### 10-topshiriq <Badge type="danger" text="qiyin" />
Keys: «Yetkazib berish buyurtmasi». Foydalanuvchi manzil, telefon, to'lov turi (Naqd / Karta) va yetkazish vaqtini tanlashi lozim. Ushbu forma uchun barcha kerakli elementlar va ularning turlari ko'rsatilgan karkas sxemasini daftarda chizing.

### 11-topshiriq <Badge type="info" text="bonus" />
Balsamiq yoki Axure RP dasturida «E-kutubxonaga kirish (Login)» modal oynasi wireframe'ini yarating. Unda: Email maydoni, Parol maydoni (ko'zcha bilan), «Meni eslab qol» (Checkbox), «Kirish» (CTA) va «Parolni unutdingizmi?» havolasi bo'lsin. Shuningdek, «Parol noto'g'ri kiritildi» degan qizil xatolik holatini ham chizing.

---

</div>

<div class="blk">

## <Icon name="file-text" /> O'z-o'zini tekshirish savollari

1. Inline validation va an'anaviy xatolik xabarining farqi nimada?
2. Kiritish maydonidagi Disabled (nofaol) holat nima uchun kerak?
3. Dropdown ro'yxatida tanlovlar soni 3 tadan kam bo'lsa, qaysi elementni ishlatish qulayroq?
4. Nima uchun yordamchi matnlar xushmuomala va yechim ko'rsatuvchi bo'lishi kerak?
5. Formaning oxirgi Submit tugmasi qanday vizual ajralib turishi lozim?

</div>

