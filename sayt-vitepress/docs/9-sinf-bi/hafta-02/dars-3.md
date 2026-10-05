---
title: "6-dars. Excel formulalari: Nisbiy/absolut murojaatlar, shartli va qidiruv funksiyalari"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (BI)", "link": "/9-sinf-bi/"}, "week": {"n": 2, "link": "/9-sinf-bi/hafta-02/"}, "g": 6, "title": "Excel formulalari: Nisbiy/absolut murojaatlar, shartli va qidiruv funksiyalari", "lead": "Hisob-kitoblar qudrati: formulalarda absolut va nisbiy manzillar, mantiqiy shartlar (IF, SUMIF, COUNTIF) hamda mukammal XLOOKUP qidiruv mexanizmi.", "slide": "/slaydlar/9-sinf-bi/hafta-02/dars-3.html", "test": "/slaydlar/9-sinf-bi/hafta-02/dars-3-test.html", "tabs": [{"g": 4, "link": "/9-sinf-bi/hafta-02/dars-1", "current": false}, {"g": 5, "link": "/9-sinf-bi/hafta-02/dars-2", "current": false}, {"g": 6, "link": "/9-sinf-bi/hafta-02/dars-3", "current": true}], "prev": {"g": 5, "title": "Professional jadval tuzish, Tidy Data va Excel Table (Ctrl+T)", "link": "/9-sinf-bi/hafta-02/dars-2"}, "next": null}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- Barcha Excel formulalari `=` (tenglik) belgisi bilan boshlanadi.
- Nisbiy murojaat (`A1`) formulani pastga yoki yonga tortganda katak manzillarini birgalikda siljitadi.
- Absolut murojaat (`$A$1`, F4 tugmasi) katak manzilini muzlatib qo'yadi va formulani ko'chirganda manzil o'zgarmaydi.
- Asosiy statistik funksiyalar: `SUM` (yig'indi), `AVERAGE` (o'rtacha qiymat), `COUNT` (sonli kataklar soni), `COUNTA` (bo'sh bo'lmagan kataklar soni), `MIN` va `MAX`.
- Shartli funksiyalar: `IF` (mantiqiy tarmoqlanish), `COUNTIF` (shartga mos qatorlarni sanash), `SUMIF` (shartga mos qatorlarni qo'shish).
- `XLOOKUP` zamonaviy funksiyasi bir jadvaldagi ma'lumotni kalit ustun orqali boshqa jadvaldan tezkor va xatosiz qidirib topish imkonini beradi.
- Formulalardagi keng tarqalgan xatolar: `#VALUE!` (matn va son aralashishi), `#N/A` (qiymat topilmasligi), `#REF!` (katak o'chirilishi), `#DIV/0!` (nolga bo'lish).

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. F4 tugmasining sehrli imkoniyatlari
Formulada katak manzilini yozgandan keyin `F4` tugmasini ketma-ket bosish orqali manzil turini o'zgartirish mumkin:
1. `A1` — Nisbiy (nusxalanganda qator ham, ustun ham o'zgaradi).
2. `$A$1` — To'liq absolut (qator ham, ustun ham qotirilgan).
3. `A$1` — Aralash (qator qotirilgan, ustun erkin).
4. `$A1` — Aralash (ustun qotirilgan, qator erkin).

### 2. COUNT vs COUNTA farqi
Ko'pchilik yangi tahlilchilar xodimlarning ismlarini sanash uchun `=COUNT(A2:A20)` deb yozib, natija `0` chiqqanda hayron qolishadi!
- `COUNT` — faqat raqamlar yozilgan kataklarni taniydi.
- `COUNTA` (Count All) — katakda matn, belgi yoki raqam bo'lishidan qat'i nazar, bo'sh bo'lmagan barcha yozuvlarni sanaydi. Shuning uchun ismlar, shaharlar va telefonlarni sanashda doim `COUNTA` ishlatiladi.

### 3. Nega XLOOKUP VLOOKUP'dan ancha ustun?
O'n yillar davomida Excelda `VLOOKUP` ishlatilgan, ammo uning jiddiy kamchiliklari bor edi:
1. `VLOOKUP` faqat o'ng tomonga qaray oladi. Agar qidirilayotgan kalit ID o'ngda, kerakli ma'lumot chapda bo'lsa, u ishlamaydi.
2. `VLOOKUP` ustun raqamini (1, 2, 3...) talab qiladi. Agar jadvalga yangi ustun qo'shilsa, barcha formulalar buzilib ketadi.
`XLOOKUP` da esa bu muammolar yo'q: u chapga ham, o'ngga ham qidiradi, ustun raqamini talab qilmaydi va qiymat topilmaganda o'rniga nima chiqishini (`[if_not_found]`) bitta argument bilan hal qiladi!

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Relative Reference (Nisbiy)** | Formulani nusxalaganda avtomatik siljiydigan katak manzili (`A1`). |
| **Absolute Reference (Absolut)** | Formulani nusxalaganda o'zgarmay qotib turadigan manzil (`$A$1`). |
| **SUM** | Berilgan kataklar oralig'idagi barcha sonlarning umumiy yig'indisi. |
| **AVERAGE** | Berilgan oraliqdagi sonlarning o'rtacha arifmetik qiymatini hisoblovchi funksiya. |
| **COUNT** | Diapazondagi faqat sonli qiymatga ega kataklar sonini hisoblaydi. |
| **COUNTA** | Diapazondagi bo'sh bo'lmagan barcha (matn va sonli) kataklarni sanaydi. |
| **IF** | Berilgan mantiqiy shart to'g'ri (TRUE) yoki noto'g'ri (FALSE) ekanligiga qarab harakat qiladi. |
| **COUNTIF** | Faqat berilgan shartga to'g'ri keluvchi kataklar sonini hisoblovchi funksiya. |
| **SUMIF** | Faqat belgilangan mezonni qanoatlantiruvchi qatorlar qiymatini qo'shuvchi funksiya. |
| **XLOOKUP** | Bitta jadvaldagi kalit orqali ikkinchi jadvaldan kerakli ma'lumotni tortib keluvchi funksiya. |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Excel formulalarida funksiya nomlari lotin harflarida katta yoki kichik yozilishidan qat'i nazar bir xil ishlaydi (masalan: `=sum(A1:A5)` va `=SUM(A1:A5)`).
- Excelda bir formulaning ichiga 64 tagacha ichma-ich `IF` operatorini joylashtirish mumkin, ammo zamonaviy tahlilda buning o'rniga `IFS` yoki `SWITCH` funksiyalaridan foydalanish tavsiya etiladi.
- Excel formulasidagi xatoni bosqichma-bosqich tekshirish uchun `Formulas > Evaluate Formula` vositasi mavjud bo'lib, u formulani qadamma-qadam ochib beradi.
- Zamonaviy `XLOOKUP` funksiyasi Microsoft tomonidan 2019 yilda e'lon qilingan va Excelning eng mashhur yangilanishlaridan biriga aylangan.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Nisbiy va absolut manzil <Badge type="tip" text="oson" />
Formuladagi `$B$5` va `B5` o'rtasidagi farqni tushuntiring. Formulani 2 qator pastga nusxalasak, ularning har biri qanday ko'rinishga keladi?
**Kutiladigan natija:** Ikkala manzilning nusxalangandan keyingi holati haqida qisqa javob.

### 2. SUM va AVERAGE qo'llash <Badge type="tip" text="oson" />
Excelda 5 ta fandan olgan baholaringizni yozing (`85`, `90`, `78`, `95`, `88`). Formulalar yordamida:
- Ularning umumiy yig'indisini (`SUM`);
- O'rtacha bahoingizni (`AVERAGE`) hisoblang.
**Kutiladigan natija:** Baholar jadvali va ikkita tayyor formula natijasi.

### 3. COUNT va COUNTA ni tekshirish <Badge type="tip" text="oson" />
Bitta ustunda 4 ta o'quvchi ismi va 3 ta raqam bor (jami 7 ta qator). Ushbu ustunga `=COUNT()` va `=COUNTA()` formulalarini qo'llaganingizda qanday natijalar chiqadi?
**Kutiladigan natija:** Ikkala funksiyaning natijaviy sonlari va nima sababdan shunday bo'lgani.

### 4. Oddiy IF funksiyasi <Badge type="tip" text="oson" />
Katakda harorat qiymati (`B2=32`) yozilgan. Agar harorat 30 dan katta bo'lsa "Issiq", aks holda "Mo'tadil" deb chiqaruvchi formula yozing.
**Kutiladigan natija:** To'g'ri tuzilgan `IF` formulasi.

### 5. Absolut manzil bilan hisoblash <Badge type="warning" text="o'rta" />
Do'konda tovarlar narxi dollarda ko'rsatilgan. `H1` katagida dollar kursi: `12 800` yozilgan.
Barcha tovarlarning so'mdagi narxini hisoblovchi formulani yozing (absolut murojaatdan foydalaning).
**Kutiladigan natija:** Kurs qotirilgan (`$H$1`) to'g'ri formula.

### 6. COUNTIF bilan davomatni sanash <Badge type="warning" text="o'rta" />
Sinf davomati jadvalida o'quvchilar holati "Bor" yoki "Yo'q" deb belgilangan. Bir kunda darsga nechta o'quvchi kelganini hisoblovchi `COUNTIF` formulasini yozing.
**Kutiladigan natija:** Shartli hisoblash formulasi.

### 7. SUMIF bilan toifaviy daromad <Badge type="warning" text="o'rta" />
Kompaniyaning 10 ta sotuv tranzaksiyasi jadvalidan faqat "Noutbuk" mahsulotidan tushgan umumiy summani hisoblovchi `SUMIF` formulasini tuzing.
**Kutiladigan natija:** `SUMIF` ning 3 ta argumenti to'g'ri qo'llangan formula.

### 8. XLOOKUP orqali narxni topish <Badge type="danger" text="qiyin" />
`A` ustunida Mahsulot ID si (`ID-105`) berilgan. Narxlar ro'yxati `Narxlar` varag'idagi `A` ustunida (ID) va `B` ustunida (Narx) joylashgan.
`XLOOKUP` orqali narxni asosiy jadvalga tortib keluvchi formulani yozing. Agar ID topilmasa, "Mavjud emas" deb chiqsin.
**Kutiladigan natija:** To'liq 4 argumentli `XLOOKUP` formulasi.

### 9. Formula xatoligini tuzatish <Badge type="danger" text="qiyin" />
Foydalanuvchi quyidagi formulani yozdi va `#VALUE!` xatosini oldi:
`=A2 * B2`, bunda A2 katagida `15 dona`, B2 da esa `4000` yozilgan edi.
Ushbu xatolik sababini tushuntiring va uni tuzatishning to'g'ri yo'lini ko'rsating.
**Kutiladigan natija:** Xatolik tahlili va to'g'rilangan amaliy yechim.

### 10. Mini-loyiha: Baholash tizimi formulalari <Badge type="info" text="bonus" />
O'quv markazi uchun 8 nafar o'quvchining sinov ballari jadvalini tuzing:
- O'rtacha ballni hisoblang (`AVERAGE`);
- Eng yuqori ballni toping (`MAX`);
- `IF` orqali 70 dan yuqori ballga "Grant", aks holda "Kontrakt" yozing;
- `COUNTIF` orqali nechta o'quvchi "Grant" olganini alohida katakda hisoblang.
**Kutiladigan natija:** Barcha 4 ta formulani o'z ichiga olgan to'liq ishchi hisobot.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Formulalarda absolut murojaat (`$A$1`) qachon va nima uchun qo'llaniladi?
2. `COUNT` va `COUNTA` funksiyalarining eng asosiy farqi nimada?
3. `IF` funksiyasining sintaksisi qanday 3 ta argumentdan iborat?
4. `SUMIF` funksiyasidagi uchinchi argument nima vazifani bajaradi?
5. `XLOOKUP` funksiyasining `VLOOKUP` ga nisbatan qanday afzalliklari bor?
6. Excelda `#DIV/0!` xatoligi nimani bildiradi va u qachon yuz beradi?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Excelda 6 ta o'quvchining 3 ta imtihon bo'yicha ballari jadvalini tuzing.
1. Har bir o'quvchining umumiy yig'indisini (`SUM`) va o'rtacha ballini (`AVERAGE`) hisoblang.
2. `IF` yordamida o'rtacha bali 80 dan oshganlarga "A'lochi", qolganlarga "Yaxshi" deb belgilang.
3. `COUNTIF` orqali sinfda nechta "A'lochi" borligini hisoblang.

</div>

