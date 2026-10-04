---
title: "3-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "9-sinf", "link": "/9-sinf/"}, "n": 3, "bob": "I-bob · UX/UI dizayn nazariyasi va asoslari", "lessons": [{"g": 7, "title": "Axure RP: Dinamik panellar va interaktiv bog'lanishlar (Interactions)", "lead": "Statik chizmalardan chertiladigan (clickable) prototiplarga o'tish, Dinamik panellar va sahifalararo navigatsiya sirlari.", "link": "/9-sinf/hafta-03/dars-1", "slide": "/slaydlar/9-sinf/hafta-03/dars-1.html"}, {"g": 8, "title": "Foydalanuvchi formalari, kiritish maydonlari va xatoliklar dizayni (Form Wireframing)", "lead": "Kiritish elementlari (Input, Dropdown, Radio, Checkbox), maydon holatlari, inline validation va xatoliklardan qutqaruvchi qulay interfeyslar.", "link": "/9-sinf/hafta-03/dars-2", "slide": "/slaydlar/9-sinf/hafta-03/dars-2.html"}, {"g": 9, "title": "Wireframe loyihasini yakunlash, annotatsiyalar va Figmaga eksport", "lead": "Izohli simli ramkalar (Annotated wireframes), PNG/SVG/PDF eksport va Figmada UI dizayn uchun referens qatlamini sozlash.", "link": "/9-sinf/hafta-03/dars-3", "slide": "/slaydlar/9-sinf/hafta-03/dars-3.html"}]}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Har bir vazifa 20–30 daqiqa. Natijalarni daftarda yoki dizayn dasturida (Axure RP, Balsamiq, Figma) alohida papkada saqlang. Topshirish: keyingi dars boshida mentorga ko'rsating.

### 7-dars uchun (Axure RP: Dinamik panellar va interaksiyalar)
**1-topshiriq: «Chertiladigan kitob kartasi va tablar»** (20–25 daqiqa)
1. Axure RP (yoki bepul interaktiv analog)da 2 ta sahifa yarating: `Home_books` va `Book_details`.
2. `Home_books`dagi kitob kartasiga `OnClick` hodisasi orqali `Open Link` &rarr; `Book_details` amalini biriktiring.
3. `Book_details` sahifasida Dynamic Panel yarating va 2 ta State hosil qiling («Annotatsiya» va «Kitob haqida fikrlar»).
4. Yuqoridagi 2 ta tugmaga `Set Panel State` amalini bog'lab, tablarni bir-biriga almashtiruvchi interaktivlikni sozlang.
5. Loyihani Preview rejimida brauzerda tekshiring.

**Kutiladigan natija:** sahifalararo o'tuvchi va bitta ekranda tablarni yangilaydigan ishchi interaktiv prototip.
**Nimani topshirasiz:** prototipning qisqa video-yozuvi (screen record) yoki dastur fayli (`.rp`).

### 8-dars uchun (Formalar, kiritish maydonlari va xatoliklar dizayni)
**2-topshiriq: «Ro'yxatdan o'tish formasi va Error State»** (20–30 daqiqa)
1. «E-kutubxona» uchun ro'yxatdan o'tish formasining to'liq wireframe'ini chizing (Label, Input, Placeholder, Helper text va Submit tugmasi).
2. Quyidagi kiritish turlarini to'g'ri ishlating:
   - To'liq ism (`Text Field`);
   - Parol (`Password Field` + ko'zcha);
   - Sevimli janrlar (`Checkbox` — kamida 3 ta variant);
   - Bildirishnomalarni olish usuli (`Radio Button` — Email / SMS).
3. Ushbu formaning «Xatolik holati» (Error state)ni alohida chizing: noto'g'ri email kiritilganda maydon qanday ko'rinishi va tagidagi mikro-matn qanday yozilishini ko'rsating.

**Kutiladigan natija:** barcha element turlari to'g'ri tanlangan toza forma wireframe'i va uning xatolik holati.
**Nimani topshirasiz:** 2 ta ekran skrinshoti (boshlang'ich holat va xatolik holati).

### 9-dars uchun (Wireframe loyihasini yakunlash va Figmaga eksport)
**3-topshiriq: «E-kutubxona to'liq karkasi va Figma referens qatlami»** (25–30 daqiqa)
1. Hafta davomida yaratilgan barcha ekranlarni (`Home_books`, `Book_details`, `Register_modal`) tekshiring va kamida 3 ta blok ustiga raqamli annotatsiya (texnik izoh) yozing.
2. Loyihani toza PNG formatida eksport qiling.
3. Figma dasturida `Desktop 1440` o'lchamli Frame ochib, ushbu PNG rasmni joylang, Opacity darajasini `40%` ga tushiring va qatlamni qulflang (`Lock`).
4. Qulflangan karkas ustidan bitta kitob kartasining birinchi rangli UI variantini (fon, rasm o'rni, chiroyli tugma) chizib ko'ring.

**Kutiladigan natija:** dasturchilar uchun annotatsiyalangan wireframe va Figmada UI dizayn uchun tayyorlangan referens qatlam.
**Nimani topshirasiz:** Figmadagi loyiha havolasi (link) yoki eksport qilingan skrinshot.

</div>
