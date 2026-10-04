---
title: "4-dars. Excelda ma'lumotlar tahlili: Saralash, filtrlash va shartli formatlash"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (BI)", "link": "/9-sinf-bi/"}, "week": {"n": 2, "link": "/9-sinf-bi/hafta-02/"}, "g": 4, "title": "Excelda ma'lumotlar tahlili: Saralash, filtrlash va shartli formatlash", "lead": "Tartibsiz jadvallardan qimmatli tushunchalarga: Excelda ma'lumotlarni saralash, aqlli filtrlar va shartli formatlash yordamida anomaliyalarni topish sirlari.", "slide": "/slaydlar/9-sinf-bi/hafta-02/dars-1.html", "tabs": [{"g": 4, "link": "/9-sinf-bi/hafta-02/dars-1", "current": true}, {"g": 5, "link": "/9-sinf-bi/hafta-02/dars-2", "current": false}, {"g": 6, "link": "/9-sinf-bi/hafta-02/dars-3", "current": false}], "prev": null, "next": {"g": 5, "title": "Professional jadval tuzish, Tidy Data va Excel Table (Ctrl+T)", "link": "/9-sinf-bi/hafta-02/dars-2"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- Saralash (Sort) ma'lumotlar to'plamini alifbo (A-Z), sonlar (o'sish/kamayish) yoki sanalar bo'yicha mantiqiy tartibga soladi.
- Ko'p darajali saralash (Multi-level Sort) orqali avval asosiy toifa, so'ngra ichki ko'rsatkichlar bo'yicha ketma-ket tartib o'rnatiladi.
- Filtrlash (Filter) katta hajmdagi ma'lumotlar ichidan faqat belgilangan shartlarga mos keluvchi qatorlarni ajratib ko'rsatadi (qolganlari o'chmaydi, faqat yashiriladi).
- Sonli filtrlar orqali `Greater than`, `Between`, `Top 10` kabi maxsus mezonlar bo'yicha ma'lumotlarni ajratish mumkin.
- Shartli formatlash (Conditional Formatting) katakdagi qiymatga qarab rang, fon va belgilarni avtomatik o'zgartiradi.
- Shartli formatlash qoidalari (Highlight Cells Rules, Top/Bottom Rules, Data Bars, Color Scales) tendensiyalar va xatolarni ko'z bilan bir zumda ilg'ash imkonini beradi.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Nega saralashda bitta katak emas, butun jadval belgilanadi?
Katta xato: agar siz faqat bitta ustunni belgilab saralash tugmasini bossangiz, Excel faqat o'sha ustundagi raqamlarni aralashtirib yuborishi mumkin! Natijada o'quvchining ismi uning bahosi bilan mos kelmay qoladi.
Doimo bitta katakni bosib saralang yoki butun jadvalni tanlang — shunda Excel avtomatik ravishda butun qatorni (Row) o'zgartirmasdan birgalikda siljitadi.

### 2. AutoFilter tezkor tugmalari
Excelda ish unumdorligini oshirish uchun quyidagi tugmalarni yodda tuting:
- `Ctrl + Shift + L` — Filtrlash tugmalarini bir bosishda yoqish yoki o'chirish.
- `Alt + Down Arrow` — Tanlangan sarlavhadagi filtr menyusini sichqonchasiz ochish.
- `Space` — Filtr ro'yxatidagi katakchani belgilash yoki belgini olib tashlash.

### 3. Shartli formatlashda Color Scales (Ranglar shkalasi)
Color Scales ma'lumotlar to'plamini "issiqlik xaritasi" (Heatmap) ko'rinishida taqdim etadi. Masalan, eng yuqori sotuvlar to'q yashil, o'rtacha ko'rsatkichlar sariq, eng past yoki xavfli ko'rsatkichlar esa qizil rang bilan belgilanadi. Bu usul katta hisobotlarda qaysi filiallar yaxshi yoki yomon ishlayotganini 1 soniyada ko'rish imkonini beradi.

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Sort (Saralash)** | Ma'lumotlarni ma'lum bir ustun qiymatlari bo'yicha o'sish yoki kamayish tartibida joylashtirish. |
| **Multi-level Sort** | Bir nechta ustunlar ketma-ketligi bo'yicha ko'p bosqichli saralash amali. |
| **Filter (Filtrlash)** | Shartga mos qatorlarni ko'rsatib, mos kelmaganlarini vaqtincha yashirish funksiyasi. |
| **AutoFilter** | Ustun sarlavhalarida ochiluvchi ro'yxat (dropdown) hosil qiluvchi tezkor filtr rejimi. |
| **Conditional Formatting** | Katak formatini (rang, shrift, fon) undagi qiymatga qarab avtomatik o'zgartirish. |
| **Highlight Cells Rules** | Belgilangan sondan katta, kichik yoki oraliqda bo'lgan kataklarni ajratish qoidalari. |
| **Data Bars** | Katak ichida qiymat miqdoriga mos mini-ustunli diagramma chizish usuli. |
| **Color Scales** | Qiymatlar darajasini ranglar gradienti (issiqlik xaritasi) orqali ifodalash. |
| **Duplicate Values** | Ma'lumotlar to'plamida aynan takrorlangan bir xil yozuvlar. |
| **Top/Bottom Rules** | Eng yuqori yoki eng past n ta qiymatni/foizni avtomatik aniqlovchi qoidalar. |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Excelda bir vaqtning o'zida **64 tagacha** turli ustun bo'yicha ko'p darajali saralashni amalga oshirish mumkin.
- Shartli formatlash qoidalari dinamik ishlaydi: agar katakdagi qiymatni o'zgartirsangiz, uning rangi ham darhol yangilanadi.
- `Alt + A + S + S` tugmalar birikmasi Excelda to'liq saralash (Sort) muloqot oynasini ochadi.
- Katta banklarda shubhali va firibgarlik ehtimoli bo'lgan tranzaksiyalarni dastlabki tahlilda darhol ajratish uchun maxsus shartli formatlash qoidalaridan foydalaniladi.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Oddiy saralash <Badge type="tip" text="oson" />
Kompyuteringizda 5 ta shahar va ularning aholisi sonini yozing. Shaharlarni aholisi eng ko'pidan eng kamiga qarab saralang.
**Kutiladigan natija:** Kamayish tartibida saralangan 5 ta qatordan iborat jadval.

### 2. Alifbo tartibida tartiblash <Badge type="tip" text="oson" />
Sinfdoshlaringizdan 6 nafarining familiyasini tartibsiz yozing va ularni `A dan Z gacha` alifbo bo'yicha tartiblang.
**Kutiladigan natija:** To'g'ri alifbo tartibidagi ro'yxat.

### 3. Oddiy sonli filtr <Badge type="tip" text="oson" />
Savdo ro'yxatida `Mahsulot` va `Narx` ustunlari bor. Narxi 50 000 so'mdan qimmat bo'lgan tovarlarni `Number Filters > Greater Than` yordamida filtrlang.
**Kutiladigan natija:** Faqat narxi 50 000 dan oshiq tovarlar ko'rinib turgan jadval.

### 4. Dublikatlarni rang bilan ajratish <Badge type="tip" text="oson" />
Ro'yxatdagi 8 ta telefon raqami ichida takrorlangan raqamlarni `Conditional Formatting > Highlight Cells Rules > Duplicate Values` orqali qizil rang bilan ajrating.
**Kutiladigan natija:** Takroriy qiymatlari qizil rangda ajratilgan ro'yxat.

### 5. Ko'p darajali saralash <Badge type="warning" text="o'rta" />
Do'kondagi mahsulotlar jadvali berilgan: `Bo'lim`, `Mahsulot nomi`, `Narxi`.
Jadvalni shunday saralangki, avval bo'limlar bo'yicha alifboda, har bir bo'lim ichida esa narxlar bo'yicha eng arzonidan eng qimmatiga qarab tartiblansin.
**Kutiladigan natija:** 2 darajali saralangan jadval holati.

### 6. Matnli filtr qo'llash <Badge type="warning" text="o'rta" />
Xodimlar ro'yxatidan familiyasi "Qodir" so'zi bilan boshlanuvchi barcha xodimlarni `Text Filters > Begins With...` orqali filtrlab ajrating.
**Kutiladigan natija:** Faqat "Qodir..." bilan boshlanuvchi xodimlar ko'rsatilgan jadval.

### 7. Oraliq bo'yicha filtrlash <Badge type="warning" text="o'rta" />
O'quvchilar imtihon ballari jadvalidan 70 balldan 85 ballgacha bo'lgan o'quvchilarni `Between` filtri yordamida ajratib oling.
**Kutiladigan natija:** 70–85 ball oralig'idagi o'quvchilar ro'yxati.

### 8. Data Bars va Color Scales qo'llash <Badge type="danger" text="qiyin" />
10 ta viloyat bo'yicha paxta hosildorligi jadvaliga:
- Hosildorlik ustuniga yashil rangli `Data Bars` qo'shing;
- Rejaning bajarilish foizi ustuniga `3-Color Scale` (yashil-sariq-qizil) qo'llang.
**Kutiladigan natija:** Ikki xil grafik formatlash qo'llangan vizual jozibali jadval.

### 9. Top 10% qoidasi <Badge type="danger" text="qiyin" />
Kompaniyaning 20 nafar sotuvchisi erishgan tushumlar ro'yxatidan eng yuqori natija ko'rsatgan 10% xodimlarni (Top 10%) avtomatik to'q yashil fonda ko'rsatuvchi shartli formatlash qoidasini yarating.
**Kutiladigan natija:** Eng yaxshi xodimlar avtomatik ajratilgan jadval.

### 10. Mini-tadqiqot: Savdo hisobotidagi anomaliyalar <Badge type="info" text="bonus" />
Internetdan yoki tasavvuringizdan 15 qatordan iborat "Elektronika do'koni savdosi" datasetini tuzing. Unda saralash, bir nechta filtrlar va shartli formatlash yordamida qaysi mahsulot eng kam sotilayotgani va qaysi kunda kutilmagan savdo sakrashi (anomaliya) bo'lganini aniqlang.
**Kutiladigan natija:** Jadval va uning asosida yozilgan 4-5 jumlalik tahliliy hisobot.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Bitta ustunni saralashda nima uchun "Expand the selection" (Tanlovni kengaytirish) taklif qilinadi?
2. `Ctrl + Shift + L` tugmalar birikmasi qanday amalni bajaradi?
3. Filtrlash orqali yashirilgan qatorlarni qanday qilib yana ko'rinadigan qilish mumkin?
4. Shartli formatlash oddiy katakni bo'yashdan nimasi bilan ustun turadi?
5. Data Bars qanday hollarda tahlilchiga qulaylik yaratadi?
6. Qaysi shartli formatlash qoidasi aynan takrorlangan qiymatlarni aniqlashga yordam beradi?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Excel dasturida 8 nafar xaridorning ma'lumotlari jadvalini tuzing (`Ism`, `Tovar`, `Summa`, `Shahar`). Jadvalni avval Shahar bo'yicha alifboda, keyin Summa bo'yicha kamayish tartibida saralang. 1 000 000 so'mdan katta xaridlarga shartli formatlash orqali yashil rang bering.

</div>

