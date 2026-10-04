# 8-dars. Foydalanuvchi formalari, kiritish maydonlari va xatoliklar dizayni (Form Wireframing)

**Hafta:** 3 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + dizayn amaliyoti · **I-bob**, 8-dars

## 1. Dars rejasi

**Maqsad:** o'quvchilarda veb va mobil interfeyslarda axborot yig'ishning asosiy vositasi bo'lgan formalar (Forms), kiritish maydonlari (Text Field, Text Area, Password Field, Droplist/Select, Checkbox, Radio Button), ularning vizual holatlari (Default, Focus, Filled, Disabled) hamda xatolik holatlari (Error/Validation) va muvaffaqiyat (Success) xabarlarini Balsamiq va Axure RP dasturlarida loyihalash ko'nikmalarini shakllantirish.

**Kutiladigan natija:**
- Formalarning UX dizayndagi ahamiyatini va foydalanuvchi charchashini (Form Fatigue) kamaytirish qoidalarini tushuntira oladi.
- Kiritish elementlari turlarini (Input, Dropdown, Radio, Checkbox) vazifasiga qarab to'g'ri tanlay oladi.
- Maydonlarning turli holatlarini (Default, Active/Focus, Error, Success, Disabled) wireframe'da ifodalaydi.
- Xatolik xabarlarini (Inline Validation) to'g'ri joylashtirishni va mikro-matnlar (Microcopy) yozishni biladi.
- «E-kutubxona» uchun to'liq «Ro'yxatdan o'tish (Sign Up)» va «Kitob qidirish / Filtr» formasi wireframe'ini yaratadi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va kirish | O'tgan darsni takrorlash (Interactions, Dynamic Panel). Muammo: «Nega odamlar uzoq va tushunarsiz formalarni to'ldirishdan voz kechishadi va bu biznesga qanday zarar keltiradi?» |
| 10–30 daq | Yangi mavzu: Nazariya | Formalar anatomiyasi (Label, Input, Placeholder, Helper text, Validation), kiritish elementlari klassifikatsiyasi va xatoliklar UX dizayni |
| 30–35 daq | Tanaffus | Harakatli tanaffus |
| 35–65 daq | Amaliy mashg'ulot | Balsamiq va Axure RP da «Ro'yxatdan o'tish» shakli, xatolik holati (Qizil chegara, tushunarli izoh) va filtr blokini yasash |
| 65–75 daq | Tezkor nazorat | 5 ta savol-javob va dizaynlarning tahlili |
| 75–80 daq | Xulosa va uyga vazifa | Muhim xulosalar va uyga vazifa yo'riqnomasi |

---

## 2. Dars konspekti

### 2.1. Formalar anatomiyasi va UX qoidalari

**Forma (Form)** — bu foydalanuvchidan ma'lumot qabul qilish, ro'yxatdan o'tkazish, to'lovni amalga oshirish yoki qidiruvni boshqarish uchun xizmat qiluvchi asosiy interfeys blokidir.

Forma elementining tarkibiy qismlari:
1. **Label (Yorliq / Nom):** Maydon nima uchun kerakligini bildiradi (masalan: «Elektron pochta»). Doim maydonning tepasida yoki chapida turishi lozim.
2. **Input Field (Kiritish maydoni):** Foydalanuvchi ma'lumot yozadigan chegara bilan o'ralgan blok.
3. **Placeholder (Vaqtincha matn / Namuna):** Maydon ichida och kulrangda turadigan namuna (masalan: `ism@pochta.uz`). Hech qachon Label o'rnini bosmasligi kerak, chunki yozish boshlanganda u yo'qoladi.
4. **Helper text (Yordamchi matn):** Maydon ostidagi qo'shimcha tushuntirish (masalan: «Parol kamida 8 ta belgidan iborat bo'lsin»).
5. **Call-to-Action (CTA / Boshqaruv tugmasi):** Formani jo'natuvchi asosiy tugma («Ro'yxatdan o'tish», «Kirish»).

```
+--------------------------------------------------------------+
| Label:          Elektron pochta manzili                      |
| Input Box:     [ ism@domen.uz                    ]          |
| Helper text:    Tasdiqlash kodi shu manzilga yuboriladi      |
+--------------------------------------------------------------+
```

### 2.2. Kiritish elementlari turlari

1. **Text Field (Matn maydoni):** Bir qatorli matn (Ism, familiya, telefon raqami).
2. **Password Field:** Kiritilayotgan belgilar yashirin nuqtalar (`••••••`) ko'rinishida bo'ladigan maydon, ko'z belgisi (Show/Hide) bilan jihozlanadi.
3. **Text Area (Ko'p qatorli matn):** Katta xabar, sharh yoki yetkazib berish manzili uchun kengayuvchi maydon.
4. **Dropdown / Droplist (Ochiluvchi ro'yxat):** Ko'p variantlardan faqat bittasini tanlash kerak bo'lganda (masalan: Davlat yoki Shahar tanlash).
5. **Radio Button (Radio tugma):** Bir nechta (odatda 2–4 ta) ko'rinib turgan variantdan FAQAT BITTASINI tanlash (masalan: Jinsi: Erkak / Ayol; Yetkazib berish: Kuryer / Olib ketish).
6. **Checkbox (Belgilash katakchasi):** Bir nechta variantdan bir vaqtning o'zida bir nechtasini tanlash (masalan: Janrlar: Detektiv, Fantastika, Tarixiy) yoki bitta shartga rozilik berish («Qoidalarga roziman»).

### 2.3. Maydon holatlari va xatoliklar dizayni (Validation UX)

Kiritish maydoni hayotiy siklida 5 ta holatdan o'tadi:
1. **Default (Boshlang'ich):** Foydalanuvchi hali tegmagan sokin holat.
2. **Focus / Active (Aktiv):** Kursor maydonga tushgan, chegara chizig'i qalinlashgan yoki ajratilgan.
3. **Filled (To'ldirilgan):** Ma'lumot kiritib bo'lingan.
4. **Error (Xatolik):** Foydalanuvchi xato kiritganda chegara rangi o'zgaradi va tagida xatoning sababi yoziladi.
5. **Success (To'g'ri):** Ma'lumot to'g'ri kiritilganda yashil belgi yoki tasdiq chiqadi.
6. **Disabled (Nofaol):** Hozircha to'ldirib bo'lmaydigan kulrang maydon.

**Xatolik xabarlarini ko'rsatish qoidasi (Inline Validation):**
- Xatolikni forma oxirida emas, bevosita xato qilingan maydon ostida ko'rsatish lozim.
- Tushunarli tilda yozish kerak: «Xato!» deb baqirish emas, balki «Elektron pochtada @ belgisi kiritilmadi» deb yechimni tushuntirish lozim.

---

## 3. Amaliy mashg'ulot

### 1-mashq. «Ro'yxatdan o'tish» formasi wireframe'i
**Vazifa:** Axure RP yoki Balsamiq dasturida «E-kutubxona» foydalanuvchisi uchun ro'yxatdan o'tish oynasini quyidagi elementlar bilan chizing:
- Sarlavha: «E-kutubxonaga a'zo bo'lish»
- Maydonlar: To'liq ism, Email, Parol (ko'z belgisi bilan), Sevimli janr (Checkbox'lar), «Foydalanish shartlariga roziman» (Checkbox), «A'zo bo'lish» (Asosiy CTA tugma).

**Yechim:**
1. Maydon markaziga `Rectangle` (kengligi 400px, balandligi 500px) joylashtiriladi.
2. Har bir maydon uchun tepasiga `Label` (Shrift 14px, Bold), tagiga `Text Field` (Balandligi 40px, chegarasi 1px kulrang) qo'yiladi.
3. Parol maydoni ichiga o'ng tomonga kichik ko'zcha belgisi (Eye icon) chiziladi.
4. Janrlar uchun 3 ta `Checkbox`: «Badiiy adabiyot», «IT va Dasturlash», «Tarix».
5. Pastda qora/to'q kulrang fonli «A'zo bo'lish» (Button) va tagida «Akkauntingiz bormi? Kirish» havolasi joylashtiriladi.

---

### 2-mashq. Xatolik (Error State) holatini modellashtirish
**Vazifa:** Yuqoridagi formaning «Noto'g'ri email kiritildi» holatidagi ko'rinishini loyihalang.

**Yechim:**
1. Email maydoni chegarasi to'q/qizil rangga o'zgartiriladi (yoki wireframeda qalinroq va `!` belgisi bilan ajratiladi).
2. Maydon tagidagi yordamchi matn o'rniga «Iltimos, to'g'ri email manzilini kiriting (masalan: user@gmail.com)» degan ogohlantirish yozuvi qo'yiladi.
3. Tugma nofaol (Disabled) holatga keltiriladi yoki bosilganda maydonga e'tibor qaratiladi.

---

## 4. Tezkor savollar (Checklist)

1. Radio Button va Checkbox o'rtasidagi asosiy farq nimada?
   - **Javob:** Radio Button bir nechta variantdan faqat bittasini tanlash uchun, Checkbox esa bir nechta variantni bir vaqtda tanlash yoki shartga rozilik berish uchun ishlatiladi.
2. Placeholder nima va nega u Label o'rnini bosa olmaydi?
   - **Javob:** Placeholder — maydon ichidagi namuna matn. Foydalanuvchi yozishni boshlaganda u o'chib ketadi, natijada inson nima yozayotganini esidan chiqarib qo'yishi mumkin.
3. Inline validation nima uchun kerak?
   - **Javob:** Xatoni butun formani yuborgandan keyin emas, darhol kiritish paytida maydon ostida ko'rsatib, foydalanuvchining vaqtini tejaydi.
4. Input maydonining 5 ta holatini ayting.
   - **Javob:** Default, Focus, Filled, Error, Disabled.
5. Form Fatigue (formalardan charchash) nima va uni qanday kamaytirish mumkin?
   - **Javob:** Juda ko'p va keraksiz maydonlar bo'lganda foydalanuvchi formani to'ldirishdan voz kechadi. Faqat eng zarur ma'lumotlarni so'rash orqali maydonlar sonini qisqartirish kerak.
