---
title: "9-dars. Wireframe loyihasini yakunlash, annotatsiyalar va Figmaga eksport"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf", "link": "/9-sinf/"}, "week": {"n": 3, "link": "/9-sinf/hafta-03/"}, "g": 9, "title": "Wireframe loyihasini yakunlash, annotatsiyalar va Figmaga eksport", "lead": "Izohli simli ramkalar (Annotated wireframes), PNG/SVG/PDF eksport va Figmada UI dizayn uchun referens qatlamini sozlash.", "slide": "/slaydlar/9-sinf/hafta-03/dars-3.html", "tabs": [{"g": 7, "link": "/9-sinf/hafta-03/dars-1", "current": false}, {"g": 8, "link": "/9-sinf/hafta-03/dars-2", "current": false}, {"g": 9, "link": "/9-sinf/hafta-03/dars-3", "current": true}], "prev": {"g": 8, "title": "Foydalanuvchi formalari, kiritish maydonlari va xatoliklar dizayni (Form Wireframing)", "link": "/9-sinf/hafta-03/dars-2"}, "next": null}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Annotated Wireframe:** Faqat chizma emas, balki har bir blok va tugmaning qanday ishlashini dasturchilarga tushuntiruvchi raqamli eslatmalar to'plami.
- **Eksport formatlari:** PNG (tezkor ko'rish va taqdimot), SVG (vektorli aniqlik va masshtab), PDF (mijozga topshiriladigan rasmiy loyiha hujjati).
- **Referens qatlami (Reference Layer):** Wireframeni Figmaga olib o'tib, uning shaffofligini 30-40% qilib qulflash va ustidan pikselma-piksel UI dizayn chizish.
- **«Online books / E-kutubxona» loyihasi:** Bosh sahifa (Home), Kitob tafsilotlari (Details), Ro'yxatdan o'tish (Sign Up) va Qidiruv ekranlarini to'liq yagona karkasga jamlash.
- **I-bob yakuni:** Wireframing bosqichi tugab, keyingi darslardan ranglar, shriftlar va kompozitsiya (UI dizayn asoslari) olamiga qadam qo'yiladi.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Nega dasturchilar «Izohli wireframe»ni yaxshi ko'rishadi?

Dasturchi rasmga qarab faqat ko'rinishni tushunishi mumkin, lekin mantiqni bilmaydi:
- Tugma bosilganda yangi sahifa ochiladimi yoki modal oynachami?
- Qidiruv maydoni qanday ishlaydi?
- Agar internet uzilsa nima ko'rinadi?
Annotatsiyalar barcha shu savollarga oldindan javob beradi va dizayner bilan dasturchi o'rtasidagi ortiqcha tortishuv va tushunmovchiliklarning oldini oladi.

### 2. Figmaga qanday qilib to'g'ri o'tkaziladi?

1. Axure RP yoki Balsamiq'da loyihani toza PNG yoki SVG holatida kompyuterga saqlang.
2. Figma dasturida yangi fayl oching va klaviaturada `F` tugmasini bosib, `Desktop` (1440x1024) frame'ini tanlang.
3. Rasmni Frame ichiga joylashtiring.
4. O'ng paneldagi `Layer` bo'limida Opacity (shaffoflik)ni `40%` ga tushiring va qulf (`Padlock / Lock`) belgisini bosing.
5. Endi siz bemalol ushbu karkas ustidan haqiqiy UI ranglari, shriftlari va chiroyli tugmalarini chizishingiz mumkin!

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Annotated wireframe** | Dasturchi va jamoa uchun harakatlar va cheklovlar yozilgan izohli karkas |
| **Reference Layer** | UI dizayn chizish uchun fon sifatida qo'yiladigan shaffof karkas qatlami |
| **SVG (Scalable Vector Graphics)** | Kattalashtirilganda sifati buzilmaydigan vektorli rasm formati |
| **PDF Specification** | Loyihaning barcha sahifalari va texnik izohlarini jamlagan rasmiy elektron kitob |
| **Hand-off** | Dizayner tomonidan tayyorlangan loyihani dasturchilarga topshirish jarayoni |
| **Opacity** | Element yoki qatlamning shaffoflik darajasi (foizda) |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- 📐 **Arxitektura o'xshashligi:** Wireframe xuddi binoning chizmasi (cherteji) kabidir. Qanday qilib quruvchilar chizmasiz bino qura olmasa, tajribali dasturchilar ham wireframesiz loyiha boshlamaydilar.
- 🚀 **Vaqtni tejash:** Wireframe ustida qilingan 1 soatlik puxta annotatsiya dasturchilarning kamida 20 soatlik keraksiz kod yozishining oldini oladi!

---

</div>

<div class="blk">

## <Icon name="file-text" /> Savollar va topshiriqlar

### 1-topshiriq <Badge type="tip" text="oson" />
Izohli simli ramka (Annotated wireframe) nima va uning oddiy wireframerdan farqi nimada?

### 2-topshiriq <Badge type="tip" text="oson" />
Wireframe eksportida PNG va SVG formatlarining farqini ayting. Qaysi biri vektor hisoblanadi?

### 3-topshiriq <Badge type="tip" text="oson" />
Figmaga yuklangan wireframeni nega qulflab (`Lock`) qo'yish kerak?

### 4-topshiriq <Badge type="warning" text="o'rta" />
«E-kutubxona» veb-saytining bosh sahifasidagi Qidiruv maydoni uchun 2 ta aniq texnik annotatsiya (izoh) yozing.

### 5-topshiriq <Badge type="warning" text="o'rta" />
Dasturchiga loyihani topshirish (Design hand-off) paytida PDF formatdagi spetsifikatsiyaning qanday afzalliklari bor?

### 6-topshiriq <Badge type="warning" text="o'rta" />
Agar mijoz: «Men dasturlashni tushunmayman, menga telefonimda ochib ko'rishim uchun yuboring» desa, unga qaysi formatda va qanday taqdim etgan ma'qul?

### 7-topshiriq <Badge type="warning" text="o'rta" />
«Kitob tafsilotlari» sahifasidagi «Kitobni yuklab olish» tugmasi uchun quyidagi holatlar bo'yicha annotatsiya tuzing:
1. Ro'yxatdan o'tgan foydalanuvchi bosganda nima bo'ladi?
2. Mehmon (ro'yxatdan o'tmagan) foydalanuvchi bosganda nima bo'ladi?

### 8-topshiriq <Badge type="danger" text="qiyin" />
To'liq veb-sayt tuzilmasi: «E-kutubxona» loyihasining 4 ta sahifasini (Home, Katalog, Tafsilotlar, Ro'yxatdan o'tish) o'zaro bog'lovchi xarita (Site Map) sxemasini daftaringizda chizing.

### 9-topshiriq <Badge type="danger" text="qiyin" />
Figma dasturida referens qatlami ustiga yangi Frame chizishda Auto Layout vositasi nima uchun muhim bo'lishi mumkinligini tushuntiring.

### 10-topshiriq <Badge type="danger" text="qiyin" />
Keng tarqalgan xatolik: Ko'p dizaynerlar wireframe chizib bo'lgach, uni darhol tashlab yuborishadi yoki unga qaramay yangi UI chizishadi. Bu nima uchun noto'g'ri va nima uchun wireframe'ga sodiq qolish kerak?

### 11-topshiriq <Badge type="info" text="bonus" />
Axure RP yoki Balsamiq'da tayyorlagan «E-kutubxona» wireframingizni PNG ko'rinishida eksport qiling, Figma dasturiga import qiling va uning ustiga kitob kartasining birinchi rangli UI variantini chizib ko'ring.

---

</div>

<div class="blk">

## <Icon name="file-text" /> O'z-o'zini tekshirish savollari

1. Texnik annotatsiyada nimalar yozilishi shart?
2. Vektorli SVG formatining dizayn uchun qanday qulayligi bor?
3. Referens qatlami nima maqsadda ishlatiladi?
4. Wireframe bosqichidan so'ng qaysi dizayn bosqichi boshlanadi?
5. Axure RP va Balsamiq dasturlarining qaysi biri tezkor eskizlar uchun, qaysi biri esa chuqur mantiq uchun ko'proq mos keladi?

</div>

