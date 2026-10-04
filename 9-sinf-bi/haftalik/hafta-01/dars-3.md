# 3-dars. BI tizimlari turlari, mutaxassislik rollari va Excel analitik platformasi

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga BI tizimlarining to'rt asosiy turi (Operatsional, Strategik, Self-Service, Integratsiyalashgan), BI jamoasidagi asosiy mutaxassislik rollari (Data Analyst, Data Engineer, BI Developer, Business User) hamda ma'lumotlar tahlilining fundamental platformasi sifatida Microsoft Excel muhitining o'rni va asosiy tuzilishini tushuntirish.
- **Kutiladigan natija:** O'quvchilar BI tizimi turlarini maqsadiga qarab farqlay oladi; sohadagi rollarning vazifalarini biladi; Excel dasturining ishchi tuzilishi (Workbook, Worksheet, Row, Column, Cell) va asosiy ma'lumot turlarini amalda to'g'ri qo'llay oladi.
- **Vaqt taqsimoti:**
  - O'tgan mavzuni takrorlash (Katta to'rtlik va ETL): 10 daqiqa
  - Yangi mavzu: BI tizimlari turlari va rollar: 20 daqiqa
  - Excel fundamental analitik vosita sifatida: 25 daqiqa
  - Amaliy mashg'ulot (Excelda ma'lumotlar kiritish va formatlash): 15 daqiqa
  - Tezkor nazorat va hafta sarhisobi: 10 daqiqa

---

## Mentor konspekti

### 1. BI tizimlarining to'rt asosiy turi
Tashkilotlarning maqsadlari va qaror qabul qilish tezligiga qarab BI tizimlari 4 turga bo'linadi:
1. **Operatsional BI (Operational BI):**
   - Kundalik jarayonlar ustidan tezkor nazorat o'rnatish uchun xizmat qiladi.
   - Real vaqt yoki yaqin real vaqt rejimidagi ma'lumotlarga tayanadi.
   - Misollar: Call-markaz monitoringi, ombordagi qoldiqlar, kunlik savdo kassa paneli.
2. **Strategik BI (Strategic BI):**
   - Yuqori boshqaruv bo'g'ini uchun uzoq muddatli maqsadlarni belgilashga xizmat qiladi.
   - Yillik va choraklik rejalashtirish, asosiy KPI ko'rsatkichlari, moliyaviy samaradorlik tahlili.
3. **Self-Service BI (Mustaqil tahlil):**
   - Dasturchi bo'lmagan xodimlarga (marketing mutaxassislari, savdo menejerlari, HR) mustaqil hisobot va grafiklar yaratish imkonini beradi.
   - IT bo'limiga bo'lgan qaramlikni kamaytiradi. Vositalar: Power BI Desktop, Tableau.
4. **Integratsiyalashgan BI (Embedded BI):**
   - Analitika alohida dasturda emas, balki xodim ishlayotgan korporativ tizim (CRM, ERP yoki mobil ilova) ichiga bevosita joylashtiriladi.

### 2. BI tizimidagi mutaxassislik rollari
BI loyihasida muvaffaqiyatga erishish uchun bir nechta mutaxassislar hamkorlikda ishlaydi:
- **Ma’lumotlar muhandisi (Data Engineer):** Infratuzilma "poydevori". Ma'lumot quvurlarini (ETL/ELT) quradi, Data Warehouse va Data Lake tizimlarini boshqaradi.
- **Ma’lumotlar tahlilchisi (Data Analyst):** BI ning "ko'zlari va miyasi". Ma'lumotlarni tahlil qiladi, qonuniyatlarni topadi, hisobotlar va dashboardlar yaratadi.
- **BI Dasturchi (BI Developer):** Dashboardlarni texnik ishlab chiquvchi, semantik model (DAX, SQL) va interfeysni loyihalashtiruvchi mutaxassis.
- **Biznes foydalanuvchisi / Rahbar (Business User / Executive):** Natijalarni ko'rib, strategik va operatsion qarorlarni qabul qiluvchi shaxs.

### 3. Excel — Ma'lumotlar bilan ishlashning fundamental vositasi
Ko'plab tahlilchilar o'z faoliyatini aynan Excel orqali boshlaydi. Nega?
- **Analitik fikrlashni shakllantiradi:** Jadval, qator, ustun va kataklar orqali mantiqiy tuzilmani tushunishni o'rgatadi.
- **Ishchi tuzilma:**
  - *Workbook (Ishchi kitob):* Butun fayl (`.xlsx`).
  - *Worksheet (Ishchi varaq):* Kitob ichidagi alohida varaqlar.
  - *Row (Qator):* Raqamlar bilan belgilanadi (1, 2, 3...).
  - *Column (Ustun):* Lotin harflari bilan belgilanadi (A, B, C...).
  - *Cell (Katak):* Ustun va qator kesishmasi (masalan, `B4`, `D12`).
- **Ma'lumot turlari (Data Types):**
  - Matn (Text): So'zlar, ismlar, toifalar.
  - Son (Number): Butun va o'nlik sonlar.
  - Valyuta (Currency): Pul birliklari ($ yoki so'm).
  - Sana/Vaqt (Date/Time): Kalendar sanalari.
  - Foiz (Percentage): Ulushlar va o'sish sur'atlari.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. BI turlarini vaziyatga moslashtirish (oson)
Quyidagi vaziyatlarga mos BI turini (Operatsional, Strategik, Self-Service, Embedded) tanlang:
1. Ombor mudiri har soatda omborda nechta quti mahsulot qolganini ko'rib turadi.
2. Kompaniya bosh direktori kelasi 3 yillik investitsiya rejasini tuzish uchun bozor ulushini tahlil qilmoqda.
3. Marketing xodimi Power BI orqali IT dasturchilarga murojaat qilmasdan yangi reklama hisobotini mustaqil tuzdi.
4. Xodim CRM dasturidan chiqmasdan mijoz kartochkasi ichida uning xarid grafigini ko'rmoqda.

**Yechim:**
1. Operatsional BI (chunki real vaqt monitoringi).
2. Strategik BI (chunki uzoq muddatli yillik strategiya).
3. Self-Service BI (chunki IT xodimisiz mustaqil hisobot yaratildi).
4. Integratsiyalashgan (Embedded) BI (chunki boshqa dastur interfeysi ichiga o'rnatilgan).

### 2-topshiriq. Kasbiy rollar mas'uliyati (o'rta)
Kompaniyada yangi savdo dashboardi yaratilmoqda. Quyidagi vazifalarni mos mutaxassisga (Data Engineer, Data Analyst, BI Developer, Business User) biriktiring:
- A: PostgreSQL bazasidagi ma'lumotlarni har kecha tozalab, Data Warehouse'ga yuklovchi avtomatik skript yozish.
- B: Savdo natijalarini o'rganib, nima sababdan Andijon filialida sotuvlar tushib ketganini tahlil qilish va xulosa chiqarish.
- C: Power BI Desktop'da murakkab DAX o'lchovlari bilan interaktiv dashboard dizaynini texnik kodlash.
- D: Tayyor dashboarddagi ko'rsatkichlarga qarab, Andijon filialiga yangi menejer tayinlash to'g'risida buyruq chiqarish.

**Yechim:**
- A — Data Engineer (ma'lumot infratuzilmasi va ETL quvuri).
- B — Data Analyst (tahlil va sabab-oqibat xulosalari).
- C — BI Developer (dashboardni texnik ishlab chiqish).
- D — Business User / Rahbar (boshqaruv qarorini qabul qilish).

### 3-topshiriq. Excelda ma'lumotlar strukturasini loyihalash (qiyin)
Maktab o'quv markazi uchun "Kurslar va to'lovlar" hisobotini tayyorlash kerak.
1. Excelda qanday ustunlar bo'lishi kerak?
2. Har bir ustun uchun qaysi ma'lumot turi (Text, Number, Date, Currency) to'g'ri keladi?
3. Bitta namunaviy qator yozib ko'rsating.

**Yechim:**
1. Kerakli ustunlar: `O'quvchi ID`, `F.I.Sh.`, `Kurs nomi`, `To'lov sanasi`, `To'lov summasi`, `Chegirma foizi`.
2. Ma'lumot turlari:
   - `O'quvchi ID`: Text (chunki raqam sifatida hisob-kitob qilinmaydi, masalan `ST-104`).
   - `F.I.Sh.`: Text.
   - `Kurs nomi`: Text.
   - `To'lov sanasi`: Date (masalan `2026-10-04`).
   - `To'lov summasi`: Currency (masalan `450 000 so'm`).
   - `Chegirma foizi`: Percentage (masalan `10%`).
3. Namunaviy yozuv: `["ST-101", "Alisher Navoiy", "Python Asoslari", "2026-10-01", 500000, 0.10]`.

---

## Tezkor nazorat savollari

1. Nima uchun Self-Service BI korxonalarda katta inqilob yaratdi?
   - *Javob:* Chunki oddiy menejerlar IT mutaxassislarining navbatini kutmasdan, kerakli hisobotlarni o'zlari mustaqil yarata oladigan bo'ldi.
2. Data Engineer va Data Analyst rollari o'rtasidagi asosiy farq nima?
   - *Javob:* Data Engineer ma'lumotlarni yig'ish va saqlash infratuzilmasini quradi, Data Analyst esa tayyor ma'lumotlardan biznes uchun tushuncha (insight) chiqaradi.
3. Excel katakchasi (Cell) qanday nomlanadi?
   - *Javob:* Ustun harfi va qator raqami birikmasi bilan (masalan: `A1`, `C15`).

---

## Uyga vazifa

Kompyuteringizda Microsoft Excel (yoki Google Sheets) dasturini oching. O'zingizning oilaviy haftalik xarajatlaringiz bo'yicha 5 ta qatordan iborat jadval tuzing. Jadvalda matn, sana, raqam va valyuta formatlaridan to'g'ri foydalaning.
