# 5-dars. Professional jadval tuzish, Tidy Data va Excel Table (Ctrl+T)

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga professional jadval tushunchasi, uning oddiy elektron jadvaldan farqi, zamonaviy ma'lumotlar muhandisligidagi Tidy Data (Tartibli ma'lumot) tamoyillari, ustun nomlash standartlari hamda rasmiy Excel Table (`Ctrl + T`) yaratish va strukturali havolalar (Structured References) bilan ishlashni o'rgatish.
- **Kutiladigan natija:** O'quvchilar tahlilga tayyor professional jadval arxitekturasini tushunadi; birlashtirilgan kataklar (Merged Cells) zararini biladi; rasmiy Excel Table yaratib, unda avtomatik Total Row va strukturali formulalarni qo'llay oladi.
- **Vaqt taqsimoti:**
  - O'tgan darsni takrorlash (Saralash va filtrlar): 10 daqiqa
  - Yangi mavzu: Professional jadval va Tidy Data tamoyillari: 25 daqiqa
  - Rasmiy Excel Table (Ctrl+T) va Structured References: 25 daqiqa
  - Amaliy mashg'ulot (Noto'g'ri jadvalni Tidy shaklga keltirish): 10 daqiqa
  - Nazorat savollari va xulosa: 10 daqiqa

---

## Mentor konspekti

### 1. Oddiy jadval vs Professional jadval
Oddiy foydalanuvchilar jadval tuzayotganda faqat inson ko'ziga chiroyli ko'rinishiga (rang-barang bezaklar, kataklarni birlashtirish) e'tibor qaratadilar. Biroq bunday jadvallarni keyinchalik Python, SQL yoki Power BI dasturlarida avtomatik tahlil qilib bo'lmaydi.
- **Oddiy jadval:** Inson o'qishi uchun vizual moslashtirilgan, ko'pincha birlashtirilgan kataklarga ega, hisoblash uchun noqulay.
- **Professional jadval:** Mashina va algoritmlar tahlili uchun optimallashtirilgan, qat'iy standartlarga ega tuzilma.

### 2. Tidy Data (Tartibli ma'lumot) tamoyillari
Ma'lumotlar tahlili olamida standart hisoblangan Tidy Data qoidalari:
1. **Har bir o'zgaruvchi — bitta ustun:** Masalan, `Yil`, `Oy`, `Summa` har biri alohida ustunda bo'lishi kerak.
2. **Har bir kuzatuv (hodisa) — bitta qator:** Har bir alohida xarid yoki tranzaksiya bitta satrni egallaydi.
3. **Har bir katak — bitta aniq qiymat:** Bitta katakka ikkita telefon raqami yoki "Tovar nomi va narxi" aralashtirib yozilmaydi.
4. **Birlashtirilgan kataklar (Merged Cells) — TAQIQLANADI!** Birlashtirilgan katak ustun bo'yicha saralash, filtrlash va formulalarni butunlay ishdan chiqaradi.

### 3. Ustun nomlari standarti
- Sarlavha doimo 1-qatorda bo'lishi lozim.
- Sarlavhalarda maxsus belgilar (`#`, `%`, `?`, `/`) ishlatmaslik, qisqa va tushunarli so'zlar tanlash tavsiya etiladi (masalan: `mijoz_id`, `mahsulot_nomi`, `savdo_summasi`).

### 4. Rasmiy Excel Table (`Ctrl + T`) imkoniyatlari
Oddiy kataklar diapazonini rasmiy Excel Table formatiga o'tkazish (`Ctrl + T` yoki `Insert > Table`):
- **Dinamik avtomatik kengayish:** Jadval oxiriga yangi qator yozsangiz, u avtomatik tarzda jadval tarkibiga kiradi, formulalar va formatlar yangi satrga o'zi ko'chadi.
- **Strukturali murojaat (Structured References):**
  Oddiy formulalar: `=B2*C2`
  Excel Table formulasi: `=[@Narx] * [@Miqdor]` (Bu formula nima hisoblanayotganini inson tili kabi tushunarli qiladi).
- **Total Row (Jami qatori):** Bitta belgi bilan jadval ostiga `Total Row` qo'shiladi va har bir ustun ostida `SUM`, `AVERAGE`, `COUNT` funksiyalarini menyudan tanlash mumkin.
- **Slicer (Kesuvchi) ulash:** Jadvalga interaktiv filtr tugmalarini ulash imkoniyati paydo bo'ladi.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Tidy Data qoidalarini tekshirish (oson)
Quyidagi jadval nima sababdan Tidy Data talablariga zid ekanligini 3 ta sabab bilan tushuntiring:
- A ustunida 1-qatordan 3-qatortacha birlashtirilgan (Merged) "Oziq-ovqat" sarlavhasi bor.
- C ustunida bitta katakka "Anvar, +998901234567, Toshkent" deb yozilgan.
- Jadval o'rtasidagi 5-qator butunlay bo'sh qoldirilgan.

**Yechim:**
1. Merged Cells (kataklar birlashtirilgani) qoidaga zid, har bir satrda toifa takrorlanishi kerak.
2. Bitta katakka uch xil atribut (Ism, Telefon, Shahar) yozilgan, har biri alohida ustun bo'lishi shart.
3. Jadval orasida bo'sh qator bo'lmasligi lozim, bu avtomatik tahlilni to'xtatib qo'yadi.

### 2-topshiriq. Rasmiy Excel Table yaratish (o'rta)
Savdo diapazoni berilgan: `Sana`, `Mahsulot`, `Narx`, `Miqdor`.
1. Diapazonni `Ctrl + T` yordamida rasmiy jadvalga aylantiring.
2. Yangi ustun qo'shing va sarlavhasiga `Jami` deb yozing.
3. Strukturali havola orqali formulani kiriting: `=[@Narx]*[@Miqdor]`.
4. `Table Design` menyusidan `Total Row` ni yoqing va Jami ustuniga yig'indini (`SUM`) qo'ying.

**Yechim:**
1. Diapazon tanlanadi va `Ctrl + T` bosiladi, "My table has headers" belgilanadi.
2. E ustuniga `Jami` deb yozilganda jadval avtomatik kengayadi.
3. E2 katagiga `=[@Narx]*[@Miqdor]` yozilib Enter bosilganda barcha qatorlarga formula o'zi avtomatik to'ldiriladi.
4. `Table Design > Total Row` belgilanadi, E ustunining pastki katagida `Sum` tanlanadi.

### 3-topshiriq. Xato formatlangan hisobotni rekonstruksiya qilish (qiyin)
Buxgalteriya tayyorlagan hisobotda oylar ustunlar bo'yicha yozilgan: `Mahsulot | Yanvar | Fevral | Mart`.
1. Nega bu format tahlil uchun (PivotTable va SQL uchun) noqulay (Wide format)?
2. Ushbu jadvalni qanday qilib Tidy Data shakliga keltirish mumkin?

**Yechim:**
1. Bu "Wide" (keng) format bo'lib, oylar ustun sarlavhasiga aylanib ketgan. Agar yangi oy qo'shilsa, yangi ustun ochishga to'g'ri keladi va formulalar buziladi.
2. Tidy shaklida 3 ta aniq ustun bo'lishi kerak: `Mahsulot`, `Oy`, `Savdo summasi`. Har bir oy alohida qator sifatida qayd etiladi. Bu esa ma'lumotlarni cheksiz kengaytirish va PivotTable'da osongina guruhlash imkonini beradi.

---

## Tezkor nazorat savollari

1. Nima uchun professional jadvallarda kataklarni birlashtirish (Merge Cells) taqiqlanadi?
   - *Javob:* Chunki birlashtirilgan kataklar ustun bo'yicha saralash, filtrlash va formulalarni to'g'ri nusxalashni buzadi.
2. `Ctrl + T` tugmasi oddiy kataklar bilan solishtirganda qanday asosiy qulaylikni beradi?
   - *Javob:* Dinamik kengayish, strukturali formulalar, avtomatik formatlash va Total Row.
3. Strukturali havola (Structured Reference) nima?
   - *Javob:* Katak manzillari (`B2*C2`) o'rniga ustun nomlaridan foydalanish (`[@Narx]*[@Miqdor]`).

---

## Uyga vazifa

Excelda o'zingiz o'qiydigan 6 ta fan bo'yicha jadval tuzing (`Fan nomi`, `O'qituvchi`, `Haftalik soat`, `Bahoyingiz`). Jadvalni `Ctrl + T` orqali rasmiy jadvalga aylantiring, dizaynini o'zgartiring va Total Row orqali jami haftalik dars soatlarini hisoblang.
