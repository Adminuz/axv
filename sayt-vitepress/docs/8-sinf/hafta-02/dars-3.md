---
title: "6-dars. Forma elementlari va validatsiyasi: <form>, <input>, <label>, <select>, <textarea>"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "8-sinf", "link": "/8-sinf/"}, "week": {"n": 2, "link": "/8-sinf/hafta-02/"}, "g": 6, "title": "Forma elementlari va validatsiyasi: <form>, <input>, <label>, <select>, <textarea>", "lead": "Veb-sayt shunchaki gazeta emas, u foydalanuvchi bilan muloqot qiladigan tirik tizimdir. Ushbu darsda saytlarga login qilish, xabar yuborish, so'rovnomalar to'ldirish va forma ma'lumotlarini to'g'ri tekshirishni (validatsiya) o'rganamiz.", "slide": "/slaydlar/8-sinf/hafta-02/dars-3.html", "test": "/slaydlar/8-sinf/hafta-02/dars-3-test.html", "tabs": [{"g": 4, "link": "/8-sinf/hafta-02/dars-1", "current": false}, {"g": 5, "link": "/8-sinf/hafta-02/dars-2", "current": false}, {"g": 6, "link": "/8-sinf/hafta-02/dars-3", "current": true}], "prev": {"g": 5, "title": "Jadval teglari: <table>, <tr>, <td>, <th>, colspan va rowspan", "link": "/8-sinf/hafta-02/dars-2"}, "next": null}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- `<form>` — foydalanuvchidan ma'lumot qabul qilib, serverga uzatuvchi asosiy konteyner.
- `action` atributi ma'lumot qayerga yuborilishini, `method` esa yuborish usulini (`GET` yoki `POST`) belgilaydi.
- `GET` usulida ma'lumotlar URL manzil satrida ko'rinadi (qidiruv uchun), `POST` da esa xavfsiz holda so'rov tanasida yashirin ketadi (parol, ro'yxatdan o'tish uchun).
- `<label>` tegi kiritish maydoniga nom beradi; `for` va `id` orqali bog'lansa, yozuvni bosganda ham kursor avtomatik maydon ichiga o'tadi.
- `<input>` tegining turi `type` atributi bilan belgilanadi: `text`, `password`, `email`, `number`, `date`, `checkbox`, `radio`, `file`, `submit`.
- Bir nechta variantdan faqat bittasini tanlash uchun `type="radio"` ishlatiladi va ularning `name` atributi bir xil bo'lishi shart.
- Ko'p qatorli matn yozish uchun `<textarea>`, ochiluvchi tanlov ro'yxati uchun `<select>` va `<option>` qo'llaniladi.
- HTML5 validatsiya atributlari (`required`, `placeholder`, `min`, `max`, `pattern`) brauzerning o'zida xatolarni tekshirib beradi.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### Nega parollar hech qachon GET bilan yuborilmaydi?
Agar siz formaga `method="GET"` bersangiz, foydalanuvchi kiritgan har bir ma'lumot brauzerning yuqori qismidagi manzil satriga qo'shilib ketadi:
`https://sayt.uz/login?login=ali&parol=12345`
Bu manzil brauzer tarixida (history), server loglarida saqlanib qoladi va ortingizda turgan har qanday odam parolingizni ko'rib oladi! Shu sababli shaxsiy va maxfiy ma'lumotlar faqat va faqat `method="POST"` bilan yuboriladi.

### `<label>` ning sehri (Accessibility va qulaylik)
Ko'pchilik boshlovchilar shunchaki matn yozib, yoniga `<input>` qo'yishadi. Ammo `<label for="tel">Telefon:</label>` va `<input id="tel">` qilinsa, foydalanuvchi "Telefon:" so'zining ustiga bosganida ham kursor darhol kiritish katagiga tushadi. Ayniqsa smartfonlarda kichik checkbox yoki radio tugmalarni bosishda bu juda katta qulaylik yaratadi!

### `checkbox` va `radio` farqi
- **Checkbox (Kvadrat):** mustaqil tanlovlar. Foydalanuvchi 0 ta, 1 ta yoki barcha 5 ta variantni ham belgilashi mumkin (masalan: "Qaysi tillarni bilasiz?").
- **Radio (Dumaloq):** muqobil tanlovlar. Variantlardan faqat bittasi tanlanadi (masalan: "Jinsingiz: Erkak yoki Ayol"). Ularning `name` atributi bir xil bo'lsa, brauzer ularni bitta guruh deb tushunadi va birini tanlasangiz, ikkinchisi avtomatik o'chadi.

### `placeholder` va `value` o'rtasidagi farq
- `placeholder="Ismingizni yozing"` — kiritish maydonidagi och kulrang shaffof yo'riqnoma. Foydalanuvchi yozishni boshlashi bilan o'chib ketadi.
- `value="Toshkent"` — maydonning ichiga oldindan yozib qo'yilgan haqiqiy matn. Foydalanuvchi uni o'chirib o'zgartirishi mumkin, aks holda shu qiymat serverga jo'natiladi.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| `<form>` | Foydalanuvchi ma'lumotlarini yig'uvchi shakl |
| `action` | Forma ma'lumotlari yuboriladigan server manzili |
| `method` | Ma'lumotlarni yuborish protokoli usuli (`GET` / `POST`) |
| `<input>` | Har xil turdagi ma'lumot kiritish maydoni (void element) |
| `<label>` | Kiritish maydonining rasmiy matnli nomi |
| `placeholder` | Kiritish maydonidagi maslahat / yo'riqnoma yozuvi |
| `required` | Maydonni to'ldirishni majburiy qiluvchi validatsiya atributi |
| `checkbox` | Ko'p tanlovli kvadrat katakcha |
| `radio` | Faqat bitta tanlovli dumaloq tugma |
| `<textarea>` | Ko'p qatorli matn kiritish maydoni |
| `<select>` / `<option>` | Ochiluvchi tanlov ro'yxati (dropdown) |
| Validatsiya | Kiritilgan ma'lumotlarning to'g'riligini tekshirish jarayoni |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Birinchi HTML formalar 1993-yilda paydo bo'lgan va internetni faqat o'qiladigan "elektron kutubxona"dan odamlar muloqot qiladigan interaktiv olamga aylantirgan.
- Bugungi kunda dunyodagi eng mashhur forma — bu Google qidiruv tizimining bosh sahifasidagi bittagina oddiy `input` va `button` dan iborat formadir!
- HTML5 da `type="color"` mavjud bo'lib, uni qo'ysangiz brauzer butun ranglar palitrasini ochib beradi.
- `autocomplete="off"` atributi brauzerga ilgari kiritilgan maxfiy so'zlarni eslab qolmaslikni buyuradi.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Oddiy qidiruv formasi <Badge type="tip" text="oson" />
Google qidiruviga o'xshash bir qatorli qidiruv formasi tuzing: bitta `type="text"` (placeholder: "Qidirish...") va "Topish" tugmasi bo'lsin. `method="GET"` qo'llang.

**Kutiladigan natija:** kiritilgan so'z bilan ishlaydigan oddiy qidiruv qatori.

### 2. Parolli kirish maydoni <Badge type="tip" text="oson" />
Foydalanuvchi o'z parolini kiritishi uchun `type="password"` maydoni va unga bog'langan `<label>` yarating. Maydonga `required` atributini bering.

**Kutiladigan natija:** kiritilgan belgilar yashirin chiqadigan va bo'sh yuborib bo'lmaydigan parol maydoni.

### 3. Raqam va sana kiritish <Badge type="tip" text="oson" />
O'quvchining yoshi (`type="number"`, `min="10" max="18"`) va tug'ilgan kuni (`type="date"`) so'raladigan 2 ta maydondan iborat forma tuzing.

**Kutiladigan natija:** faqat belgilangan yosh oralig'ini qabul qiluvchi va kalendar ochuvchi forma.

### 4. Qiziqishlar ro'yxati (`checkbox`) <Badge type="tip" text="oson" />
Foydalanuvchidan qaysi sport turlarini yoqtirishini so'rovchi kamida 4 ta `checkbox` (Futbol, Shaxmat, Suzish, Tennis) dan iborat blok tuzing.

**Kutiladigan natija:** bir vaqtning o'zida bir nechta katakchani belgilash mumkin bo'lgan ro'yxat.

### 5. Yagona tanlov (`radio`) <Badge type="warning" text="o'rta" />
O'quvchidan ta'lim tilini tanlashni so'rang: O'zbek tili, Rus tili, Ingliz tili. Tanlovlardan faqat bittasini tanlash mumkin bo'lsin (`name` atributiga e'tibor bering).

**Kutiladigan natija:** faqat bitta variantni tanlashga imkon beruvchi 3 ta radio tugma.

### 6. Xatoni toping va tushuntiring <Badge type="warning" text="o'rta" />
Quyidagi kodda nima uchun ikkala radio tugmani ham birdaniga tanlab bo'lyapti? Xatoni to'g'rilang:
```html
<input type="radio" name="til1"> O'zbekcha
<input type="radio" name="til2"> Ruscha
```

**Kutiladigan natija:** xatoning sababi yozilgan va to'g'rilangan kod.

### 7. Ochiluvchi menyu (`<select>`) <Badge type="warning" text="o'rta" />
O'zbekistonning kamida 5 ta viloyati ro'yxatidan iborat `<select>` menyusini tuzing. Dastlabki tanlov sifatida "Toshkent shahri" tanlangan (`selected`) tursin.

**Kutiladigan natija:** bosganda 5 ta viloyat ro'yxati ochiladigan qulay tanlov oynasi.

### 8. Fikr va takliflar maydoni (`<textarea>`) <Badge type="warning" text="o'rta" />
Maktab oshxonasi haqida o'quvchilar fikrini qabul qiluvchi forma tuzing. Unda o'quvchi ismi, sinfi va 5 qatorli `<textarea>` bo'lsin.

**Kutiladigan natija:** ko'p qatorli matn yozish imkonini beruvchi fikr-mulohaza maydoni.

### 9. To'liq ro'yxatdan o'tish (Sign Up) sahifasi <Badge type="danger" text="qiyin" />
Katta IT-kursga yozilish sahifasini yarating. Unda:
- Ism va familiya (`required`);
- Email va telefon raqam;
- Maxfiy parol (kamida 8 belgi);
- Kurs yo'nalishi (`<select>`: Frontend, Backend, Dizayn);
- Dars vaqti (`radio`: Ertalab, Tushdan keyin, Kechki);
- Foydalanish qoidalariga rozilik (`checkbox` va `required`);
- "Yuborish" va "Tozalash" tugmalari.

**Kutiladigan natija:** to'liq validatsiyaga ega, barcha zamonaviy elementlar qatnashgan ro'yxatdan o'tish formasi.

### 10. Maxsus HTML5 inputlar laboratoriyasi <Badge type="danger" text="qiyin" />
Kamida 5 ta noodatiy input turlarini sinab ko'ring: `type="color"`, `type="range"`, `type="file"`, `type="time"`, `type="url"`. Har birining yoniga nima vazifa bajarishini yozing.

**Kutiladigan natija:** zamonaviy HTML5 interaktiv elementlari bilan boyitilgan tajriba sahifasi.

### 11. O'quvchilar testi (Quiz) formasi <Badge type="info" text="bonus" />
HTML mavzusiga oid 3 ta test savolidan iborat forma tuzing. Har bir savol ostida 4 tadan javob varianti (`radio` bilan) bo'lsin. Forma oxirida "Javoblarni tekshirish" tugmasi bo'lsin.

**Kutiladigan natija:** haqiqiy onlayn test sinovi ko'rinishidagi interaktiv veb-forma.

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. `<form>` tegining `action` atributi bo'sh qolsa nima sodir bo'ladi?
2. Nima uchun login va parol shakllarida faqat `POST` metodi ishlatilishi shart?
3. `<label>` ning `for` atributi qaysi atribut bilan bog'lanishi kerak?
4. Radio tugmalar guruhida nima uchun `name` atributi bir xil bo'lishi talab etiladi?
5. `required` atributining foydalanuvchi va server uchun qanday foydasi bor?
6. `<textarea>` tegi nima uchun `<input>` dan farqli o'laroq yopiluvchi tegga (`</textarea>`) ega?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

O'zingiz yoqtirgan biror xizmat (masalan, yetkazib berish xizmati, internet-do'kon yoki kutubxona) uchun buyurtma berish formasini yarating. Unda xaridorning shaxsiy ma'lumotlari, yetkazib berish sanasi, to'lov turi (`radio`), mahsulot haqida qo'shimcha izoh (`<textarea>`) va yuborish tugmasi bo'lsin.

</div>

