# 7-dars. Ma’lumotlarni tozalash (Data Cleaning) va transformatsiya

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga ma’lumotlarni tozalash (Data Cleaning) tushunchasi, uning ma'lumotlar sifatidagi o'rni, Excel matn funksiyalari (`TRIM`, `CLEAN`, `PROPER`), `Text-to-Columns` va `Flash Fill` (Ctrl+E) vositalari, dublikatlarni o'chirish hamda Power Query muhitida birlamchi transformatsiya amallarini bajarishni o'rgatish.
- **Kutiladigan natija:** O'quvchilar iflos va tartibsiz ma'lumotlardagi xatoliklarni aniqlay oladi; ortiqcha bo'shliqlarni tozalash, matn registri va formatlarni to'g'rilashni biladi; bitta ustundagi to'liq ismni yoki manzilni alohida ustunlarga ajrata oladi.
- **Vaqt taqsimoti:**
  - O'tgan haftani takrorlash: 10 daqiqa
  - Yangi mavzu: Data Cleaning va Excel matn vositalari: 20 daqiqa
  - Text-to-Columns, Flash Fill va dublikatlar: 25 daqiqa
  - Power Query orqali tozalash amaliyoti: 15 daqiqa
  - Nazorat savollari va xulosa: 10 daqiqa

---

## Mentor konspekti

### 1. Ma’lumotlarni tozalash (Data Cleaning) nima?
Data Cleaning — bu tahlilga tayyor bo'lmagan xom ma'lumotlar to'plamidagi xatoliklar, noaniqliklar, takroriy yozuvlar (dublikatlar), ortiqcha bo'sh joylar va noto'g'ri formatlarni aniqlash hamda ularni to'g'rilash jarayonidir.
Tahlilchilar o'z vaqtlarining 70-80 foizini aynan ma'lumotlarni tozalashga sarflaydilar. Chunki **GIGO (Garbage In, Garbage Out)** qoidasiga ko'ra, xato ma'lumot asosida qabul qilingan har qanday strategik qaror korxona uchun katta zarar keltiradi.

### 2. Keng tarqalgan ma'lumot nuqsonlari va ularning yechimi
1. **Ortiqcha bo'shliqlar (Extra spaces):**
   - So'zlar orasida 2-3 tadan bo'sh joy bo'lishi yoki so'z oxirida bo'shliq qolib ketishi kompyuter uchun turli xil so'zdek tuyuladi (`"Olma "` $\neq$ `"Olma"`).
   - Yechim: `=TRIM(A2)` funksiyasi so'zlar orasidagi bittadan tashqari barcha ortiqcha bo'shliqlarni olib tashlaydi.
2. **Matn registri (Katta-kichik harflar):**
   - Birov `"toshkent"`, birov `"TOSHKENT"`, boshqasi esa `"Toshkent"` deb kiritgan.
   - Yechim: `=PROPER(A2)` har bir so'zning bosh harfini kattaga, qolganlarini kichikka aylantiradi.
3. **Takroriy yozuvlar (Duplicates):**
   - Tizimda bir xil xaridor yoki buyurtma ikki marta ro'yxatga olingan.
   - Yechim: `Data > Remove Duplicates` vositasi orqali barcha dublikat qatorlar bir zumda o'chiriladi.

### 3. Matnni ustunlarga ajratish: Text-to-Columns va Flash Fill
- **Text-to-Columns (Matnni ustunlarga bo'lish):**
  - Agar bitta katakda `"Anvar Qodirov, Toshkent"` kabi ma'lumot bo'lsa, `Data > Text to Columns` orqali uni ajratuvchi belgi (vergul, bo'sh joy yoki nuqta-vergul) asosida alohida ustunlarga bo'lish mumkin.
- **Flash Fill (Ctrl + E):**
  - Excelning eng aqlli sun'iy intellekt vositasi. Siz yangi ustunning 1-qatoriga namunani yozasiz (masalan, to'liq ismdan faqat ismni ajratib yozasiz) va `Ctrl + E` tugmasini bossangiz, Excel qolgan yuzlab qatorlarni namuna asosida o'zi to'ldirib beradi!

### 4. Power Query orqali professional tozalash
Power Query — Excel va Power BI ning rasmiy ETL (Extract, Transform, Load) vositasi bo'lib, barcha tozalash qadamlarini (Applied Steps) xotirada saqlaydi:
- `Transform > Format > Trim & Clean`
- `Transform > Split Column by Delimiter`
- `Home > Remove Rows > Remove Duplicates` (Katta-kichik harfni inobatga olmaslik uchun: `Comparer.OrdinalIgnoreCase`)
- `Transform > Replace Values` (`null` qiymatlarni `0` yoki `"Noma'lum"` bilan almashtirish).
Manba yangilansa, `Refresh` tugmasi bilan butun tozalash jarayoni avtomatik qayta bajariladi.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. TRIM va PROPER funksiyalarini qo'llash (oson)
Jadvalda ismlar quyidagicha xato kiritilgan:
- A2: `"  alisher   navoiy  "`
- A3: `"BOBUR   MIRZO "`
Yangi ustunda formulalar orqali ushbu ismlarni ortiqcha bo'shliqlarsiz va to'g'ri bosh harflar bilan ko'rinishga keltiring.

**Yechim:**
Formula `B2` katagiga yoziladi:
`=PROPER(TRIM(A2))`
Natija:
- B2: `"Alisher Navoiy"`
- B3: `"Bobur Mirzo"`

### 2-topshiriq. Flash Fill (Ctrl + E) bilan telefon kodlarini ajratish (o'rta)
A ustunida telefon raqamlari yozilgan: `+998901234567`, `+998935554433`, `+998971112233`.
1. B ustuniga `Kompaniya kodi` sarlavhasini yozing.
2. B2 katagiga namuna sifatida birinchi raqamning kodini: `90` deb yozing va Enter bosing.
3. `Ctrl + E` tugmasini bosing va natijani tekshiring.

**Yechim:**
`Ctrl + E` bosilganda Excel naqshni darhol ilg'aydi va B3 ga `93`, B4 ga `97` qiymatlarini avtomatik to'ldirib beradi.

### 3-topshiriq. Text-to-Columns va Bo'sh qiymatlarni tozalash (qiyin)
Mijozlar to'plamida manzil va to'lov quyidagicha aralash kelgan: `"Toshkent - 150000; Samarqand - ; Buxoro - 85000"`.
1. Ma'lumotlarni shahar va summa bo'yicha alohida ustunlarga ajrating.
2. Bo'sh summalarni (Samarqand filialidagi to'lov yo'q katakni) `Find & Replace` orqali `0` raqamiga almashtiring.
3. Takroriy shaharlar bo'lsa, `Remove Duplicates` orqali tozalang.

**Yechim:**
1. Diapazon tanlanib, `Data > Text to Columns` orqali Delimiter: `-` (defis) tanlanadi va 2 ta ustunga bo'linadi.
2. Summa ustunidagi bo'sh kataklar belgilanadi yoki `Ctrl + H` (Find & Replace) orqali bo'sh joylar `0` ga almashtiriladi.
3. `Data > Remove Duplicates` bosilib, Shahar ustuni bo'yicha dublikatlar o'chiriladi.

---

## Tezkor nazorat savollari

1. `TRIM` funksiyasi qanday bo'shliqlarni olib tashlaydi va qaysilarini qoldiradi?
   - *Javob:* So'z boshidagi, oxiridagi va so'zlar orasidagi ortiqcha bo'shliqlarni olib tashlaydi, faqat bitta bo'shliqni qoldiradi.
2. `Flash Fill` (Tezkor to'ldirish) qaysi klaviatura birikmasi bilan ishga tushadi?
   - *Javob:* `Ctrl + E`.
3. Power Query'da bajarilgan tozalash amallarining an'anaviy Exceldan asosiy afzalligi nima?
   - *Javob:* Barcha amallar `Applied Steps` bo'lib saqlanadi va yangi ma'lumot kelganda bitta `Refresh` tugmasi bilan butun tozalash avtomatik takrorlanadi.

---

## Uyga vazifa

Excelda 8 nafar insonning ismi, familiyasi va yashash shahri aralash yozilgan jadval tuzing (masalan: `"jasur olimov, toshkent"`). Formulalar yoki `Flash Fill` yordamida ismni, familiyani va shaharni 3 ta alohida toza ustunga ajratib, bosh harflarini to'g'rilang.
