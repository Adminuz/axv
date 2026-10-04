# 4-dars. Excelda ma'lumotlar tahlili: Saralash, filtrlash va shartli formatlash

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga Microsoft Excel muhitida katta hajmdagi ma'lumotlar to'plamini tahlilga tayyorlash, bitta va ko'p darajali saralash (Sort), shartli va matnli filtrlash (Filter) hamda qoidalar asosida vizual ajratuvchi shartli formatlash (Conditional Formatting) usullarini o'rgatish.
- **Kutiladigan natija:** O'quvchilar ma'lumotlarni alifbo, son va sana bo'yicha saralay oladi; ko'p darajali saralashni qo'llay oladi; murakkab mezonlar bo'yicha filtrlashni va shartli formatlash orqali eng yuqori/past qiymatlar hamda anomaliyalarni vizual ajratishni biladi.
- **Vaqt taqsimoti:**
  - O'tgan haftani takrorlash: 10 daqiqa
  - Yangi mavzu: Saralash (Sort) va ko'p darajali tartiblash: 20 daqiqa
  - Filtrlash (Filter) va Shartli formatlash (Conditional Formatting): 25 daqiqa
  - Amaliy mashg'ulot (Real savdo datasetida mashq): 15 daqiqa
  - Nazorat savollari va dars yakuni: 10 daqiqa

---

## Mentor konspekti

### 1. Ma'lumotlarni saralash (Sort)
Ma'lumotlar tahlilida saralash — bu satrlarni ma'lum bir mantiqiy tartibda qayta joylashtirish jarayonidir.
- **Bitta ustun bo'yicha saralash:**
  - Matn: Alifbo tartibida (A → Z yoki Z → A).
  - Sonlar: O'sish tartibida (Smallest to Largest) yoki kamayish tartibida (Largest to Smallest).
  - Sanalar: Eng eskidan yangiga (Oldest to Newest) yoki teskarisi.
- **Ko'p darajali saralash (Multi-level Sort):**
  - Agar bir nechta ustun bo'yicha tartib kerak bo'lsa (masalan, avval *Viloyat* bo'yicha alifboda, keyin har bir viloyat ichida *Savdo summasi* bo'yicha kamayish tartibida), `Data > Sort > Add Level` tugmasi ishlatiladi.

### 2. Ma'lumotlarni filtrlash (Filter)
Filtrlash — katta jadvaldan faqat bizga kerakli shartga mos keluvchi satrlarni ko'rsatib, qolganlarini vaqtincha yashirish mexanizmidir (ma'lumot o'chib ketmaydi).
- **AutoFilter (Ctrl + Shift + L):** Sarlavhalarga ochiluvchi strelka (dropdown) qo'shadi.
- **Sonli filtrlar (Number Filters):**
  - *Greater than...* (Falonchi sondan katta)
  - *Between...* (Oraliqdagi sonlar)
  - *Top 10...* (Eng yuqori 10 ta yoki eng past 10 ta ko'rsatkich)
  - *Above Average* (O'rtacha qiymatdan yuqori)
- **Matnli filtrlar (Text Filters):** *Begins with*, *Contains* (ichida bor), *Ends with*.

### 3. Shartli formatlash (Conditional Formatting)
Shartli formatlash — kataklardagi qiymatlarga qarab ularning rangi, shrifti yoki fonini avtomatik o'zgartirish usulidir. Bu vosita tahlilchiga quruq raqamlarga qarash o'rniga, tendensiyalar va anomaliyalarni ko'z bilan bir zumda ilg'ab olish imkonini beradi.
- **Highlight Cells Rules:** `Greater than`, `Less than`, `Between`, `Duplicate Values` (takroriy qiymatlarni qizil bilan ajratish).
- **Top/Bottom Rules:** Eng yuqori 10% yoki o'rtachadan past natijalarni belgilash.
- **Data Bars va Color Scales:** Katak ichida mini-gistogramma yoki "issiq-sovuq" (yashil-sariq-qizil) issiqlik xaritasi (Heatmap) yaratish.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Ko'p darajali saralash (oson)
Maktab o'quvchilari ro'yxati berilgan: `Sinf`, `F.I.Sh.`, `Chorak balli`.
Jadvalni shunday saralangki, avval sinflar bo'yicha (9A, 9B, 9C...), har bir sinf ichida esa o'quvchilar balli bo'yicha eng yuqoridan eng pastga qarab joylashsin.

**Yechim:**
1. Jadval ichidagi istalgan katakka bosiladi.
2. `Data` menyusidan `Sort` oynasi ochiladi.
3. 1-daraja (Sort by): `Sinf`, Order: `A to Z`.
4. `Add Level` tugmasi bosiladi va 2-daraja (Then by): `Chorak balli`, Order: `Largest to Smallest` tanlanadi.
5. `OK` bosiladi.

### 2-topshiriq. Savdo filtri va oraliq tahlil (o'rta)
Kompaniyaning 100 ta savdo tranzaksiyasi jadvalidan quyidagi shartlarga mos buyurtmalarni ajrating:
- Mahsulot toifasi: faqat "Elektronika";
- Savdo summasi: 1 000 000 so'mdan 5 000 000 so'mgacha bo'lgan oraliqda;
- Holati: faqat "Yetkazildi".

**Yechim:**
1. `Ctrl + Shift + L` bilan filtrlash yoqiladi.
2. "Toifa" ustunida faqat "Elektronika" belgilanadi.
3. "Savdo summasi" ustuni filtridan `Number Filters > Between...` tanlanadi: `is greater than or equal to: 1000000` va `is less than or equal to: 5000000` kiritiladi.
4. "Holat" ustunida faqat "Yetkazildi" tanlanadi.

### 3-topshiriq. Shartli formatlash bilan anomaliyalarni topish (qiyin)
Ombor qoldiqlari jadvalida `Mahsulot nomi`, `Qoldiq soni`, `Minimal me'yor` ustunlari bor.
1. Qoldiq soni 10 tadan kam qolgan tovarlarni qizil rang bilan (Light Red Fill with Dark Red Text) ajrating.
2. Dublikat (takrorlangan) mahsulot nomlarini sariq rang bilan belgilang.
3. Qoldiq soni ustuniga `Data Bars` (gradientli to'ldirish) qo'shing.

**Yechim:**
1. "Qoldiq soni" ustunini belgilab, `Home > Conditional Formatting > Highlight Cells Rules > Less Than...` tanlanadi, qiymatga `10` yoziladi va qizil format tanlanadi.
2. "Mahsulot nomi" ustunini belgilab, `Conditional Formatting > Highlight Cells Rules > Duplicate Values...` tanlanadi va Yellow Fill tanlanadi.
3. "Qoldiq soni" ustuniga `Conditional Formatting > Data Bars > Gradient Fill (Green)` qo'llaniladi.

---

## Tezkor nazorat savollari

1. Filtrlash (Filter) qo'llanilganda shartga to'g'ri kelmagan qatorlar o'chib ketadimi?
   - *Javob:* Yo'q, ular o'chmaydi, faqat vaqtincha ekrandan yashiriladi.
2. Nima sababdan ko'p darajali saralash (Multi-level Sort) kerak bo'ladi?
   - *Javob:* Chunki birinchi ustunda bir xil qiymatlar (masalan, bir xil shahar) ko'p bo'lsa, ularning ichki tartibini ikkinchi ustun (masalan, sana yoki summa) bo'yicha tartiblash uchun.
3. Shartli formatlashdagi "Color Scales" (Ranglar shkalasi) qanday vizual effekt beradi?
   - *Javob:* Kichik va katta qiymatlarni harorat xaritasi (Heatmap) kabi yashildan qizilgacha bo'lgan ranglar gradientida ko'rsatadi.

---

## Uyga vazifa

Excelda 10 ta xaridordan iborat savdo jadvalini yarating. Jadvalga `F.I.Sh.`, `Mahsulot`, `Summa`, `To'lov turi` ustunlarini kiriting. Shartli formatlash orqali 500 000 so'mdan ortiq xaridlarni yashil rang bilan, naqd to'lovlarni esa ko'k rang bilan ajratib ko'rsating.
