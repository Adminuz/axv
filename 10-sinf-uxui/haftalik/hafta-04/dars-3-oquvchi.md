# 12-dars. Figma / Adobe XD da interaktiv Wireframe yaratish

> Uy qurishdan oldin chizma chiziladi. Sayt qurishdan oldin esa wireframe: sahifaning karkasi. Bugun uni Figmada chizamiz va tugmalarni bosib ekranlar orasida yuramiz.

## Dars xulosasi

- Wireframe: veb-sahifaning «chizmasi», uning asosiy tuzilishi va joylashuvi. Uni interfeys xaritasi, ya'ni GPS deb tasavvur qiling.
- U dizaynni «taxminlar o'yini»ga aylantirmaydi: avval tuzilma va user flow, keyin chiroyli grafika.
- Wireframe past detallashgan (low-fidelity): rang, shrift va rasm chalg'itmasligi uchun ishlatilmaydi.
- Qo'llanish: ko'chmas mulk, e-commerce, portfolio saytlari; har birida o'z maslahatlari bor.
- Vositalar: qog'oz va qalam, Figma; Webflow keyingi, ishlab chiqish bosqichiga o'tishda qulay.
- Figmada 7 bosqich: fayl, Frame, header va navigatsiya, asosiy elementlar, tekislash, ekranlar orasidagi linklar, tekshirish.
- Interaktiv linklar yordamida user flowni ko'rsatish mumkin.

## Qo'shimcha ma'lumot

### Wireframe va prototip: farqi nimada?

10-darsda ko'rdingiz: qora-oq wireframe — past detallashgan (low-fidelity) prototip. Bugun unga **interaktivlik** qo'shamiz: tugma bosilganda keyingi ekran ochiladi. Shunda wireframe «rasm»dan «kichik o'yin»ga aylanadi va 11-darsdagi user flowni o'zingiz sinab ko'rasiz.

### Nega rangsiz?

Rangli maketni ko'rganda odamlar «ko'k yoqmadi» deb bahslashadi, tuzilma haqida esa gapirmaydi. Kulrang karkasda esa savol bitta: «Tugma qayerda turishi kerak?». Shuning uchun hujjat: ranglar, shriftlar va rasmlar chalg'itmaydi, e'tibor asosiy mazmunda qoladi.

### Uch yo'nalish: nimaga e'tibor berish kerak

- **Ko'chmas mulk:** qidiruv va filtr intuitiv bo'lsin; obyekt ro'yxati, galereya va xarita muhim. Sahifani ortiqcha elementlar bilan to'ldirmang.
- **E-commerce:** mahsulot vitrinasi, sodda menyu va oson checkout. Checkoutni keraksiz bosqichlar bilan murakkablashtirmang.
- **Portfolio:** eng kuchli loyihalarni bosh sahifada ajrating; tashrifchi sizga oson yetib borsin.

### Figmada ishlash tartibi (7 qadam)

```text
1) Yangi fayl  ->  2) Frame  ->  3) Header + navigatsiya  ->  4) Oddiy shakllar
   ->  5) Tekislash va oraliqlar  ->  6) Ekranlar orasida linklar  ->  7) Tekshirish
```

Muhim: 4-bosqichda minimalizm. Qanchalik oddiy bo'lsa, o'zgartirish shunchalik oson. 5-bosqichda 3-haftadagi 8pt tizimi va grid g'oyasini qo'llang.

### Odatiy xatolar

- Wireframega rang va chiroyli rasm qo'yib vaqt yo'qotish.
- Frame o'lchamini o'ylamasdan tanlash.
- Elementlarni ko'z bilan tekislash (vositalardan foydalanmaslik).
- Linkni o'rnatib, uni Present rejimida sinamaslik.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Wireframe | Veb-sahifaning chizmasi: asosiy tuzilma va joylashuv |
| Low-fidelity design | Past detallashgan dizayn: oddiy shakllar, rang va grafikasiz |
| Layout | Sahifa tartibi, elementlar joylashuvi |
| Structure | Sahifa va mazmun tuzilmasi |
| Frame (Artboard) | Figmada ish maydoni (sahifa/ekran o'lchami) |
| Header | Sahifaning yuqori qismi: logo, menyu |
| CTA | Foydalanuvchini harakatga undovchi element, odatda tugma |
| Wireflow | Wireframe va flowchartning aralashmasi |
| Interaktiv link | Elementni bosganda boshqa ekranga o'tishni ta'minlovchi bog'lanish |
| Webflow | Loyihani ishlab chiqish bosqichiga o'tkazishda qulay vosita |
| Figma | Wireframe va dizayn yaratish dasturi |

## Bilasizmi?

- Figma brauzerda ishlaydi, shuning uchun bir fayl ustida bir necha kishi bir vaqtda ishlay oladi.
- «Wireframe» ingliz tilida «wire» (sim) va «frame» (karkas) so'zlaridan tuzilgan: simdan yasalgan karkas modeliga o'xshatiladi.
- Hujjat eslatadi: qog'oz va ruchka bilan boshlash hali ham ajoyib usul.
- Hujjatga ko'ra, yaxshi wireframe sehrli darajadagi intuitiv xarid tajribasiga yo'l ochadi.

## Topshiriqlar

### 1. Ta'rif · oson
Wireframe nima? 1–2 jumlada o'z so'zlaringiz bilan yozing va «GPS» o'xshatishini izohlang.

**Kutiladigan natija:** ta'rifda «tuzilma va joylashuv» g'oyasi, o'xshatish mantiqli.

### 2. Ortiqchasini toping · oson
Qaysi biri wireframega mos kelmaydi: (a) menyu uchun to'rtburchaklar; (b) rasm joyi uchun kulrang blok; (c) 6 xil shrift va gradient fon; (d) CTA tugmasi shakli.

**Kutiladigan natija:** to'g'ri harf va 1 jumlalik sabab.

### 3. Qadamlar tartibi · oson
Aralash qadamlarni tartiblang: Tekshirish; Frame yaratish; Linklar o'rnatish; Yangi fayl; Tekislash; Header yaratish; Asosiy elementlar.

**Kutiladigan natija:** 7 qadam to'g'ri tartibda.

### 4. Ikki ekran · oson
O'zingiz tanlagan sayt (masalan, Telegram yoki maktab sayti) uchun qaysi ikki ekran wireframe qilinishini yozing va ular orasidagi o'tish qaysi tugma bilan bo'lishini aniqlang.

**Kutiladigan natija:** 2 ekran nomi, tugma nomi.

### 5. Maslahatlarni moslang · o'rta
Sayt turiga moslang: (a) filtr va qidiruvni intuitiv qiling; (b) checkoutni qisqa tuting; (c) eng yaxshi loyihalarni bosh sahifada ko'rsating.

**Kutiladigan natija:** ko'chmas mulk, e-commerce, portfolio.

### 6. Taqqoslash jadvali · o'rta
Wireframe va 10-darsdagi rangli interaktiv prototipni 3 mezon bo'yicha taqqoslang: ko'rinish, o'zgartirish osonligi, qachon qo'llanadi.

**Kutiladigan natija:** 2 ustunli, 3 qatorli jadval.

### 7. Bashorat qiling · o'rta
Figmada CTA tugmasini ikkinchi Frame'ga bog'ladingiz, lekin Present rejimida tugmani bosganda hech narsa bo'lmayapti. Ehtimoliy sabablarni 2 ta yozing.

**Kutiladigan natija:** link tugmaga emas, boshqa elementga berilgan; link o'rnatilmagan yoki noto'g'ri Frame tanlangan; Present rejimida emas.

### 8. Xatoni toping · o'rta
Dizayner e-commerce wireframe'iga checkoutda 9 ta majburiy bosqich qo'ydi. Nega bu yomon va qanday tuzatiladi?

**Kutiladigan natija:** hujjat: checkoutni keraksiz bosqichlar bilan murakkablashtirmaslik kerak; bosqichlar qisqartiriladi.

### 9. Header va navigatsiya · qiyin
Online do'kon bosh sahifasi uchun header'ni to'rtburchaklar bilan chizing: logo joyi, 4 ta menyu, qidiruv. 10-darsdagi qoidalarni qo'llang (logotip qayerda, qidiruv qayerda?).

**Kutiladigan natija:** logotip yuqori chapda, qidiruv yuqori o'ngda va yashirilmagan; elementlar tekislangan.

### 10. Maktab sayti: 2 ekran · qiyin
Figmada 2 Frame yarating: «Bosh sahifa» va «Qabul». Bosh sahifada header, katta rasm joyi, CTA «Qabul», 3 yangilik bloki, footer. «Qabul» ekranida sarlavha va 3 maydonli forma. CTA ni «Qabul» ekraniga bog'lang va Present rejimida sinang.

**Kutiladigan natija:** 2 Frame, faqat oddiy qora-oq/kulrang shakllar, ishlaydigan interaktiv o'tish.

### 11. Wireflow chizing · qiyin
Yuqoridagi ikki ekranni o'qlar bilan bog'langan wireflow ko'rinishida joylashtiring va «Qabul» ekranidan orqaga qaytish uchun yana bitta link qo'shing.

**Kutiladigan natija:** o'qlar bilan bog'langan ikki ekran, qaytish linki ishlaydi.

### 12. Bonus: ikki xil bosh sahifa · bonus
Portfolio saytingiz bosh sahifasini 5 daqiqada ikki xil joylashuvda chizing va qaysi biri “eng kuchli loyiha”ni yaxshiroq ajratganini tushuntiring.

**Kutiladigan natija:** ikki variant va 2–3 jumlalik tanlov izohi.

## O'zingizni tekshiring

1. Wireframe nima va dizayn jarayonida qanday rol o'ynaydi?
2. Wireframingning asosiy maqsadi nima?
3. Nega wireframeda ranglar, shriftlar va grafikalar ishlatilmaydi?
4. E-commerce wireframe'ida qaysi elementlar eng muhim?
5. Wireflow nima va oddiy wireframe'dan farqi?
6. Figmada wireframe yaratishning birinchi uchta bosqichini sanang.
7. Ekranlar orasida aloqa qaysi bosqichda va nima uchun o'rnatiladi?
8. Wireframe jamoa bilan muloqotni nega yengillashtiradi?

## Uyga vazifa

O'zingiz yaratmoqchi bo'lgan ilova yoki sayt uchun Figmada 3 ekranli wireframe tayyorlang (kamida 1 ta CTA va 2 ta interaktiv link, faqat qora-oq/kulrang shakllar), Present rejimida sinab ko'ring va 3 jumlada «qaysi qaror eng qiyin bo'ldi?» deb yozing (20–30 daqiqa). Figma bo'lmasa, A4 da 3 ekranni chizib, o'qlar bilan bog'lang.
