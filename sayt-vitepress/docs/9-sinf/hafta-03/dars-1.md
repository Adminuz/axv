---
title: "7-dars. Axure RP: Dinamik panellar va interaktiv bog'lanishlar (Interactions)"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf", "link": "/9-sinf/"}, "week": {"n": 3, "link": "/9-sinf/hafta-03/"}, "g": 7, "title": "Axure RP: Dinamik panellar va interaktiv bog'lanishlar (Interactions)", "lead": "Statik chizmalardan chertiladigan (clickable) prototiplarga o'tish, Dinamik panellar va sahifalararo navigatsiya sirlari.", "slide": "/slaydlar/9-sinf/hafta-03/dars-1.html", "tabs": [{"g": 7, "link": "/9-sinf/hafta-03/dars-1", "current": true}, {"g": 8, "link": "/9-sinf/hafta-03/dars-2", "current": false}, {"g": 9, "link": "/9-sinf/hafta-03/dars-3", "current": false}], "prev": null, "next": {"g": 8, "title": "Foydalanuvchi formalari, kiritish maydonlari va xatoliklar dizayni (Form Wireframing)", "link": "/9-sinf/hafta-03/dars-2"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Interaktiv Wireframe:** Sahifadagi tugma, havola yoki bloklar foydalanuvchi chertishiga (Click) javob beradigan, harakatdagi karkas model.
- **Interactions tuzilishi:** Trigger (hodisa — `OnClick`, `OnMouseEnter`) &rarr; Action (harakat — `Open Link`, `Set Panel State`) &rarr; Target (ta'sir qiluvchi nishon).
- **Dynamic Panel (Dinamik panel):** Bir joyning o'zida bir nechta holatlarni (States) saqlay oluvchi konteyner. Tablar, modal oynalar va slayderlar yaratishda tengsiz vosita.
- **Sahifalararo bog'lanish:** `Home_books` sahifasidan `Book_details` sahifasiga `Open Link` orqali to'g'ridan-to'g'ri o'tishni loyihalash.
- **Preview (Ko'rib chiqish):** Yaratilgan interaktiv tizimni brauzerda haqiqiy dastur kabi sinab ko'rish imkoniyati.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Nega professional dizaynerlar Axure RP dan foydalanishadi?

Bugungi kunda Figma eng ommabop dizayn dasturi hisoblanadi. Ammo murakkab mantiqiy tizimlar (bank ilovalari, soliq portallari, yirik CRM tizimlari) loyihalashda Axure RP hali ham yetakchi hisoblanadi. Chunki:
- Axure RP da dasturlash kodini yozmasdan turib haqiqiy o'zgaruvchilar (Variables) va shartli tarmoqlanishlar (`if / else`) tuzish mumkin.
- Bitta ekranda o'nlab har xil holatlarni Dinamik Panellar yordamida sahifani ko'paytirmasdan boshqarish mumkin.

### 2. Dinamik panellarning hayotiy analogiyasi

Dinamik panelni xuddi ko'p sahifali kitobcha yoki bir xil ramka ichidagi suratlar to'plamiga qiyoslash mumkin:
- Ramka bitta o'lchamda turadi;
- Siz «Keyingi» yoki «Tavsif» tugmasini bosganingizda, ramka ichidagi rasm boshqasiga almashadi.
- Bu foydalanuvchiga butun sahifani qayta ochmasdan, tezkor va silliq interfeys taqdim etadi.

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Interactions** | Foydalanuvchi harakatiga tizimning javob qaytarish mexanizmi |
| **Trigger (Event)** | Interaktivlikni ishga tushiruvchi hodisa (`OnClick`, `OnHover`) |
| **Action** | Hodisa yuz berganda bajariladigan aniq buyruq (`Open Link`, `Show/Hide`) |
| **Dynamic Panel** | Bir nechta holatni (states) o'z ichiga olgan dinamik konteyner |
| **State** | Dinamik panelning ma'lum bir ko'rinish holati |
| **Preview** | Loyihalashtirilgan prototipni brauzerda interaktiv tarzda sinash rejimi |
| **Breadcrumb (Non ushoqlari)** | Foydalanuvchi saytning qaysi bo'limida turganini ko'rsatuvchi navigatsiya zanjiri |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- 💡 **Birinchi prototiplar:** Dastlabki dasturiy prototiplar 1980-yillarda HyperCard dasturida yaratilgan bo'lib, o'shanda ham kartochkalar o'rtasida havolalar orqali o'tish tamoyili qo'llanilgan!
- ⚡ **Xatolarni erta topish:** Dasturchi kod yozishni boshlashidan oldin interaktiv prototipda xatoni tuzatish dastur tayyor bo'lgandan keyin tuzatishdan ko'ra 100 baravar arzonroq tushadi.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Savollar va topshiriqlar

### 1-topshiriq <Badge type="tip" text="oson" />
Statik wireframe va interaktiv prototip o'rtasidagi asosiy farqni bitta jumla bilan tushuntiring.

### 2-topshiriq <Badge type="tip" text="oson" />
Axure RP dasturida `OnClick` va `OnMouseEnter` hodisalarining farqi nimada? Har biriga bittadan misol keltiring.

### 3-topshiriq <Badge type="tip" text="oson" />
Quyidagi harakatlardan qaysi biri sahifalararo o'tish uchun ishlatiladi: `Set Panel State`, `Open Link`, `Show/Hide`?

### 4-topshiriq <Badge type="warning" text="o'rta" />
«E-kutubxona» veb-sayti uchun `Home` sahifasidan `Book_details` sahifasiga o'tish harakatini qadam-baqadam yozib chiqing (Qaysi element bosiladi, qanday hodisa bo'ladi, qayerga o'tiladi?).

### 5-topshiriq <Badge type="warning" text="o'rta" />
Dinamik panel (Dynamic Panel) nima va nima uchun bitta ekranda tablarni ko'rsatishda yangi sahifa ochmasdan dinamik panel ishlatish qulayroq?

### 6-topshiriq <Badge type="warning" text="o'rta" />
Kitob sahifasida 3 ta tab mavjud: «Annotatsiya», «Muallif haqida» va «Fikrlar». Bu tizimni Dinamik Panel yordamida loyihalash uchun nechta State kerak bo'ladi va har bir State ichida nimalar joylashadi?

### 7-topshiriq <Badge type="warning" text="o'rta" />
Mobil ilovada pastki navigatsiya paneli (Bottom Navigation: Bosh sahifa, Qidiruv, Profil) mavjud. Buni Axure RP da qanday qilib qotirib qo'yish (Pin to Browser) mumkin?

### 8-topshiriq <Badge type="danger" text="qiyin" />
Modal oyna (Popup) qanday ishlaydi? «Kirish» tugmasi bosilganda fonning qorayishi va markazda login oynasi chiqishi uchun qanday hodisa va amallardan foydalanish zarurligini sxematik ko'rsating.

### 9-topshiriq <Badge type="danger" text="qiyin" />
Agar foydalanuvchi sahifani pastga aylantirsa (scroll qilsa), sahifaning yuqori qismidagi Header elementi yo'qolib ketmasdan doimiy ko'rinib turishi uchun qanday sozlama qo'llaniladi?

### 10-topshiriq <Badge type="danger" text="qiyin" />
Keys: Foydalanuvchi «Savatchaga qo'shish» tugmasini bosganda, savatchadagi son 0 dan 1 ga o'zgarishi va ekranning yuqori burchagida «Kitob savatchaga qo'shildi» degan qisqa xabar 3 soniya ko'rinib, so'ng o'zi yo'qolishi kerak. Buni interaktivlik mantiqi asosida loyihalang.

### 11-topshiriq <Badge type="info" text="bonus" />
Axure RP (yoki bepul onlayn analogida) 2 ta ekrandan iborat interaktiv kitob ilovasi karkasini yasang: Bosh sahifadagi kitob rasmini bosganda batafsil sahifa ochilsin, batafsil sahifadagi «Orqaga» tugmasi bosilganda yana bosh sahifaga qaytsin. Natijani brauzerda tekshiring.

---

</div>

<div class="blk">

## <Icon name="file-text" /> O'z-o'zini tekshirish savollari

1. Trigger, Action va Target tushunchalari nima?
2. Nega tablarni almashtirish uchun butunlay yangi sahifa yaratish tavsiya etilmaydi?
3. Dynamic Panel ichidagi holatlar (States) qanday boshqariladi?
4. Axure RP loyihasini brauzerda sinab ko'rish uchun qaysi tugma yoki qisqa klavish bosiladi?
5. Interaktiv wireframe dasturchilar jamoasiga qanday yordam beradi?

</div>

