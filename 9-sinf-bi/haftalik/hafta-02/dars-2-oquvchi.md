# 5-dars. Professional jadval tuzish, Tidy Data va Excel Table (Ctrl+T)

> Chiroyli emas, aqlli jadvallar: ma'lumotlar gigiyenasi, Tidy Data tamoyillari va Excel Table vositasining barcha imkoniyatlari.

## Dars xulosasi

- Oddiy elektron jadval faqat inson ko'zi uchun chiroyli qilib tuziladi; professional jadval esa algoritmlar va tahliliy dasturlar (Power BI, Python, SQL) uchun optimallashtiriladi.
- Tidy Data (Tartibli ma'lumot) tamoyillari: har bir o'zgaruvchi — bitta ustun, har bir kuzatuv — bitta qator, har bir katak — bitta aniq qiymat.
- Professional tahlilda birlashtirilgan kataklar (Merged Cells) qat'iyan man etiladi, chunki ular saralash, filtr va formulalarni buzadi.
- Jadval ustunlari sarlavhasi qisqa, aniq va maxsus belgilarsiz (masalan, `snake_case` usulida) 1-qatorga yozilishi shart.
- Rasmiy Excel Table (`Ctrl + T`) oddiy diapazonga qaraganda dinamik avtomatik kengayish, strukturali havolalar va o'rnatilgan tahlil vositalariga ega.
- Strukturali havolalar (`[@Narx] * [@Miqdor]`) formulalarni inson tushunadigan aniq biznes mantiqiga aylantiradi.
- `Total Row` (Jami qatori) bitta harakat bilan jadval ostiga umumlashtiruvchi funksiyalarni (SUM, AVERAGE, COUNT) joylashtiradi.

---

## Qo'shimcha ma'lumot

### 1. Nega birlashtirilgan kataklar (Merge Cells) tahlilchining dushmani?
Ko'pincha yangi boshlovchilar bir xil viloyat yoki toifadagi yozuvlarni chiroyli ko'rsatish uchun 5 ta qatorni bitta katak qilib birlashtirishadi (Merge).
Natijada nima bo'ladi?
1. Kompyuter faqat eng yuqori chap katakda qiymat bor deb hisoblaydi, qolgan 4 ta qator esa texnik jihatdan bo'sh (NULL) bo'lib qoladi!
2. Filtr qo'llaganingizda faqat 1-qator chiqadi, qolgan 4 tasi yashirilib ketadi.
3. Saralash (Sort) mutlaqo ishlamaydi va Excel xatolik beradi.
Shuning uchun professional tahlilda har bir satrda tegishli toifa nomi to'liq yoziladi.

### 2. Oddiy diapazon vs Rasmiy Excel Table
| Xususiyat | Oddiy Diapazon (Range) | Rasmiy Jadval (Ctrl+T) |
|---|---|---|
| **Yangi qator qo'shilishi** | Qo'lda formatlanadi, formulalar ko'chmaydi | Avtomatik kengayadi, formulalar o'zi to'ldiriladi |
| **Formula ko'rinishi** | `=B2*C2` (noaniq kataklar) | `=[@Narx]*[@Miqdor]` (tushunarli ustunlar) |
| **Sarlavhalar** | Pastga aylantirganda ko'rinmay qoladi | Ustun harflari (A, B, C) o'rniga sarlavha chiqib turadi |
| **Jami hisoblash** | Har safar `=SUM(...)` yoziladi | `Total Row` belgisini qo'yish kifoya |

### 3. Tidy Data: Keng (Wide) va Uzun (Long) formatlar
Agar har bir oy alohida ustun bo'lsa (`Yanvar`, `Fevral`, `Mart`), bu "Wide" format deb ataladi. U hisobotni ko'rish uchun qulay, lekin PivotTable yoki ma'lumotlar bazasi uchun "Long" (Uzun) format kerak: bitta ustunda `Oy`, ikkinchi ustunda `Summa`. Long format ma'lumotlarni tahlil qilish uchun eng mos keluvchi Tidy shakldir.

---

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Tidy Data** | Har bir ustun bitta o'zgaruvchi, har bir qator bitta kuzatuv bo'lgan standart jadval shakli. |
| **Excel Table (Ctrl+T)** | Dinamik imkoniyatlarga ega rasmiy jadval formati. |
| **Structured Reference** | Formulalarda katak manzili o'rniga jadval ustunlari nomidan foydalanish usuli. |
| **Merged Cells** | Bir nechta katakni bitta qilib birlashtirish (tahlilda taqiqlangan amaliyot). |
| **Total Row** | Excel Table ostidagi avtomatik yig'indi va statistik hisoblashlar qatori. |
| **Header Row** | Jadvalning har bir ustunini aniqlovchi birinchi sarlavha qatori. |
| **Data Hygiene** | Ma'lumotlar to'plamini toza, xatosiz va bir xil formatda saqlash madaniyati. |
| **Wide Format** | Oylar yoki sanalar ustunlar bo'ylab gorizontal joylashgan keng format. |
| **Long Format** | Barcha parametrlar qatorlar bo'ylab vertikal joylashgan tahliliy format. |
| **Slicer (Kesuvchi)** | Excel jadvallari va PivotTable'larga ulanadigan interaktiv filtr tugmalari. |

---

## Bilasizmi?

- Tidy Data tamoyillari mashhur ma'lumotlar olimi Xedli Uikxem (Hadley Wickham) tomonidan 2014 yilda ishlab chiqilgan va butun jahon ma'lumotlar muhandisligi standartiga aylangan.
- Excel Table formati 2007 yilgi versiyada taqdim etilgan bo'lib, unga qadar barcha formulalarni qo'lda pastga tortib nusxalash talab etilar edi.
- Agar rasmiy jadval ichida turib `Tab` tugmasini bossangiz, Excel avtomatik ravishda yangi toza qator ochib beradi.
- Dunyodagi tahlilchilar vaqtining qariyb 30 foizi boshqalar tomonidan noto'g'ri birlashtirilgan (Merged) kataklarni tuzatishga sarflanadi.

---

## Topshiriqlar

### 1. Merged cells xatosini topish · oson
Nima sababdan professional jadvallarda bir xil viloyatga tegishli 4 ta qatorni bitta katakka birlashtirish (Merge Cells) taqiqlanadi?
**Kutiladigan natija:** Birlashtirilgan kataklarning tahlilga keltiradigan 2 ta asosiy zarari.

### 2. Excel Table yaratish · oson
Excelda 4 ta ustun (`Mahsulot`, `Narx`, `Miqdor`, `Holat`) va 4 ta qatordan iborat savdo ro'yxatini yozing. Uni `Ctrl + T` tugmasi orqali rasmiy jadvalga aylantiring.
**Kutiladigan natija:** Rasmiy Excel Table ko'rinishidagi jadval.

### 3. Sarlavhalarni to'g'rilash · oson
Quyidagi noto'g'ri ustun sarlavhalarini professional tahlil talablariga mos (qisqa, bo'sh joysiz) shaklga keltiring:
- "Mijozning to'liq familiyasi va ismi"
- "Tovar narxi (QQS bilan birga hisoblangan)"
- "Sotilgan sanasi / vaqti"
**Kutiladigan natija:** 3 ta standartlashtirilgan ustun nomi (masalan: `mijoz_fish`, `narx_qqs`, `sana`).

### 4. Total Row ni yoqish · oson
O'zingiz yaratgan rasmiy jadvalga `Table Design` menyusi orqali `Total Row` qo'shing va `Miqdor` ustuni ostida umumiy tovarlar sonini hisoblang.
**Kutiladigan natija:** Pastida Jami (Total) qatori chiqqan jadval.

### 5. Strukturali formula kiritish · o'rta
Rasmiy jadvalingizga `Summa` nomli yangi ustun qo'shing. Unda `=[@Narx] * [@Miqdor]` strukturali formulasini kiriting va barcha qatorlar avtomatik to'lganini tekshiring.
**Kutiladigan natija:** Strukturali formula orqali to'liq hisoblangan ustun.

### 6. Dinamik kengayishni sinash · o'rta
Rasmiy jadvalingizning eng pastki qatoriga yangi 5-mahsulot ma'lumotini yozing. Jadval o'z chegaralarini avtomatik kengaytirgani va `Summa` formulasini o'zi hisoblaganini kuzating.
**Kutiladigan natija:** Yangi qator qo'shilgan va formulasi avtomatik ishlagan jadval.

### 7. Keng (Wide) formatni tahlil qilish · o'rta
Quyidagi jadval nima sababdan Tidy Data talablariga mos kelmasligini tushuntiring:
`Xodim | Dushanba | Seshanba | Chorshanba`
Uni qanday qilib to'g'ri tahliliy (Long) shaklga keltirish mumkin?
**Kutiladigan natija:** Wide formatning kamchiligi va Long format ustunlari tuzilmasi.

### 8. Slicer (Interaktiv filtr) ulash · qiyin
Rasmiy jadvalingiz uchun `Table Design > Insert Slicer` menyusi orqali `Mahsulot` ustuni bo'yicha interaktiv tugmali filtr (Slicer) yarating va tugmalarni bosib tahlil qiling.
**Kutiladigan natija:** Jadval yonida ishlaydigan interaktiv Slicer bloki.

### 9. Tartibsiz hisobotni Tidy shaklga o'tkazish · qiyin
Sizga qog'ozda quyidagi hisobot berildi:
*Sarlavha 1-qator: "2026-yil savdolari". Sarlavha 2-qator: "Toshkent shahri". 3-qator: non — 4000 so'm (5 dona), sut — 9000 so'm (2 dona).*
Ushbu tartibsiz matnni to'liq Tidy Data qoidalariga mos jadval sifatida loyihalashtiring (barcha ustunlar va qatorlar).
**Kutiladigan natija:** Tidy formatdagi to'liq 4 ta ustunli jadval.

### 10. Mini-tadqiqot: Normalizatsiya va Tidy Data · bonus
Ma'lumotlar bazasidagi "Birinchi normal shakl" (1NF) va tahlildagi "Tidy Data" tushunchalari qanday umumiy qoidalarga ega? Qisqacha solishtirma xulosa yozing.
**Kutiladigan natija:** 1NF va Tidy Data bog'liqligi bo'yicha 5-8 jumlali tahlil.

---

## O'zingizni tekshiring

1. Oddiy elektron jadval va professional jadval o'rtasidagi asosiy farq nimada?
2. Tidy Data tamoyilining 3 ta asosiy qoidasini ayting.
3. Nima uchun rasmiy jadvallarda birlashtirilgan kataklar (Merged Cells) taqiqlanadi?
4. Excel Table formatiga o'tkazishning qanday tezkor tugmasi bor?
5. Strukturali murojaat (Structured Reference) oddiy katak formulasidan nimasi bilan farq qiladi?
6. Excel Table'dagi Total Row qanday imkoniyatlarni beradi?

---

## Uyga vazifa

Excelda 5 ta kitob haqida ma'lumotlar jadvalini tuzing (`Kitob nomi`, `Muallif`, `Janr`, `Narxi`, `Nashr yili`). Jadvalni `Ctrl + T` yordamida rasmiy jadvalga aylantiring, sarlavhalarini Tidy Data talablariga moslang va Total Row orqali kitoblarning o'rtacha narxini (`Average`) hisoblang.
