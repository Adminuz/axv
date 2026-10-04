# 6-dars. Excel formulalari: Nisbiy/absolut murojaatlar, shartli va qidiruv funksiyalari

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga Excelda formulalar tuzish mantiqi, nisbiy (`A1`) va absolut (`$A$1`) katak murojaatlari, asosiy statistik funksiyalar (`SUM`, `AVERAGE`, `COUNT`, `COUNTA`), shartli mantiqiy funksiyalar (`IF`, `COUNTIF`, `SUMIF`) hamda zamonaviy qidiruv va bog'lash vositasi bo'lgan `XLOOKUP` funksiyasini amalda qo'llashni o'rgatish.
- **Kutiladigan natija:** O'quvchilar formulada qachon `$` belgisini (F4) ishlatishni biladi; shartli hisob-kitoblarni bajara oladi; ikkita alohida jadvalni `XLOOKUP` orqali bog'lay oladi va formulalardagi xatolarni (`#VALUE!`, `#N/A`, `#DIV/0!`) to'g'rilash ko'nikmasiga ega bo'ladi.
- **Vaqt taqsimoti:**
  - O'tgan darsni takrorlash (Tidy Data va Excel Table): 10 daqiqa
  - Yangi mavzu: Nisbiy/absolut murojaatlar va statistik funksiyalar: 20 daqiqa
  - Shartli funksiyalar (`IF`, `COUNTIF`, `SUMIF`): 25 daqiqa
  - `XLOOKUP` va xatolarni tahlil qilish amaliyoti: 15 daqiqa
  - Nazorat savollari va hafta xulosasi: 10 daqiqa

---

## Mentor konspekti

### 1. Nisbiy va Absolut murojaatlar ($ belgisi va F4)
Formulalarni pastga yoki yonga nusxalaganda katak manzillarining harakati:
- **Nisbiy murojaat (Relative: `A1`):** Formulani pastga tortsangiz, u avtomatik ravishda `A2`, `A3`, `A4` bo'lib o'zgaradi.
- **Absolut murojaat (Absolute: `$A$1`):** Dollar belgisi ustun va qatorni "qotirib" (muzlatib) qo'yadi. Formulani qayerga nusxalasangiz ham, u faqat `A1` katagiga murojaat qiladi.
  - Masalan, QQS stavkasi yoki dollar kursi `H1` katagida turgan bo'lsa, barcha mahsulotlar formulasida `$H$1` deb yoziladi.
  - Tezkor tugma: `F4` (Windows) yoki `Command + T` (Mac).

### 2. Asosiy matematik va statistik funksiyalar
Barcha formulalar `=` belgisi bilan boshlanadi:
- `=SUM(C2:C20)` — berilgan diapazondagi barcha sonlar yig'indisi.
- `=AVERAGE(C2:C20)` — o'rtacha arifmetik qiymat.
- `=COUNT(C2:C20)` — faqat sonlar yozilgan kataklar sonini sanaydi.
- `=COUNTA(A2:A20)` — bo'sh bo'lmagan (matn yoki son) barcha kataklarni sanaydi.
- `=MIN(C2:C20)` va `=MAX(C2:C20)` — eng kichik va eng katta qiymatni topadi.

### 3. Shartli funksiyalar (Conditional Functions)
- **`IF(shart, to'g'ri_bo'lsa, noto'g'ri_bo'lsa)`:**
  `=IF(D2>=70, "O'tdi", "Yiqildi")`
- **`COUNTIF(diapazon, shart)`:**
  Shartga to'g'ri keluvchi kataklar sonini sanaydi.
  `=COUNTIF(E2:E50, "O'tdi")` — nechta o'quvchi o'tganini sanaydi.
- **`SUMIF(tekshirish_diapazoni, shart, [yig'indi_diapazoni])`:**
  Faqat tanlangan shartga mos qatorlarning qiymatini qo'shadi.
  `=SUMIF(B2:B50, "Olma", D2:D50)` — faqat "Olma" sotuvlari yig'indisini hisoblaydi.

### 4. Qidiruv va bog'lash funksiyasi: XLOOKUP
Eski `VLOOKUP` funksiyasi faqat o'ng tomonga qidirar edi va ustun o'zgarsa buzilar edi. Zamonaviy `XLOOKUP` esa juda qulay:
`=XLOOKUP(qidirilayotgan_qiymat, qidiruv_ustuni, natija_ustuni, [topilmasa_nima_chiqsin])`
Misol: Mijoz ID si (`A2`) bo'yicha mijozlar bazasidan uning telefon raqamini topib keltirish:
`=XLOOKUP(A2, Mijozlar!A:A, Mijozlar!C:C, "Mijoz topilmadi")`

### 5. Formulalardagi keng tarqalgan xatoliklar
- `#VALUE!` — matematik amalga matn aralashib ketdi.
- `#N/A` — qidirilgan qiymat jadvalda mavjud emas.
- `#REF!` — formula havola qilgan katak yoki ustun o'chirilgan.
- `#DIV/0!` — son nolga bo'lindi.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Absolut murojaat bilan QQS hisoblash (oson)
Jadvalda `Mahsulot`, `Baza narxi`, `Jami narx` ustunlari bor.
`F1` katagida QQS stavkasi: `0.12` (12%) yozilgan.
Barcha tovarlar uchun Jami narxni hisoblovchi formulani yozing va absolut murojaatni qo'llang.

**Yechim:**
Formula `C2` katagiga yoziladi:
`=B2 + (B2 * $F$1)` yoki `=B2 * (1 + $F$1)`
Formulani pastga tortganda `B2` o'zgaradi, lekin `$F$1` o'zgarmaydi.

### 2-topshiriq. IF va COUNTIF orqali sarhisob (o'rta)
O'quvchilar imtihon natijalari jadvali berilgan (`Ism`, `Ball`).
1. `Natija` ustunida balli 60 dan yuqori yoki teng bo'lsa "Muvaffaqiyatli", aks holda "Qayta topshirish" deb chiqaruvchi `IF` formulasini yozing.
2. Pastki alohida katakda nechta o'quvchi "Muvaffaqiyatli" o'tganini `COUNTIF` orqali hisoblang.

**Yechim:**
1. `C2` katagiga: `=IF(B2>=60, "Muvaffaqiyatli", "Qayta topshirish")`
2. Alohida katakka: `=COUNTIF(C2:C25, "Muvaffaqiyatli")`

### 3-topshiriq. XLOOKUP orqali narxlarni bog'lash (qiyin)
Sizda ikkita alohida jadval bor:
- 1-jadval (Buyurtmalar): `Buyurtma_ID`, `Mahsulot_Kodi`, `Miqdor`
- 2-jadval (Narxlar ro'yxati): `Mahsulot_Kodi`, `Mahsulot_Nomi`, `Narxi`
Buyurtmalar jadvaliga `Narxi` va `Jami summa` ustunlarini qo'shing va `XLOOKUP` orqali 2-jadvaldan narxni tortib keling.

**Yechim:**
1. Buyurtmalar jadvalidagi `D2` (Narxi) katagiga formula:
   `=XLOOKUP(B2, Narxlar!A:A, Narxlar!C:C, 0)`
2. `E2` (Jami summa) katagiga:
   `=C2 * D2` (Miqdor * Narxi).

---

## Tezkor nazorat savollari

1. Formulada nima uchun `$` belgisi ishlatiladi va uni qaysi tezkor tugma qo'yadi?
   - *Javob:* Katak manzilini nusxalashda qotirish (absolut qilish) uchun, tezkor tugma `F4`.
2. `COUNT` va `COUNTA` funksiyalari o'rtasidagi farq nimada?
   - *Javob:* `COUNT` faqat sonli kataklarni sanaydi, `COUNTA` esa bo'sh bo'lmagan barcha (matnli va sonli) kataklarni sanaydi.
3. `XLOOKUP` funksiyasi `VLOOKUP` ga nisbatan qanday 2 ta asosiy afzallikka ega?
   - *Javob:* Chap tomondagi ustunlarga ham qidira oladi va ustun raqamini sanashni talab qilmaydi.

---

## Uyga vazifa

Excelda 7 ta mahsulotdan iborat jadval tuzing: `Nomi`, `Kategoriya`, `Narxi`, `Sotilgan soni`.
1. `SUMIF` orqali faqat "Ichimliklar" kategoriyasiga tegishli tovarlar tushumini hisoblang.
2. `IF` funksiyasi yordamida sotilgan soni 50 tadan oshsa "Ommabop", kam bo'lsa "Oddiy" degan belgi chiqaring.
