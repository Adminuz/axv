# 11-dars. UI elementlarida rang nazariyasi

> Nega ayrim ilovalar ko'zni quvontiradi, boshqalari esa 5 soniyada charchatadi? Ushbu darsda ranglar g'ildiragi, 4 xil rang palitrasi, 60-30-10 qoidasi va WCAG kontrast talablarini o'rganamiz.

## Dars xulosasi

- **Rang g'ildiragi (Color Wheel)** &mdash; asosiy, ikkilamchi va oraliq ranglarning aylana shaklidagi uyg'unlik xaritasi.
- **4 asosiy palitra turi:**
  1. **Monoxromatik:** Bitta rangning och va to'q tuslari (eng toza, xavfsiz).
  2. **Analog:** G'ildirakda yonma-yon turgan ranglar (tabiiy, tinchlantiruvchi).
  3. **Komplementar (Qo'shimcha):** Bir-biriga qarama-qarshi turgan ranglar (maksimal kontrast, masalan: ko'k va to'q sariq).
  4. **Triadik:** Teng masofadagi 3 rang (boy va dinamik).
- **60-30-10 qoidasi:** 60% &mdash; dominant fon rangi, 30% &mdash; ikkilamchi struktura rangi, 10% &mdash; yorqin aksent (CTA tugma) rangi.
- **WCAG kontrasti:** Matn va fon orasidagi kontrast oddiy matn uchun kamida **4.5:1**, yirik sarlavhalar uchun kamida **3:1** bo'lishi shart.

## Qo'shimcha ma'lumot

### Nega Facebook va Telegram ko'k rangda?
Rang psixologiyasida ko'k rang ishonchlilik, xavfsizlik va barqarorlik hissini uyg'otadi. Yashil &mdash; o'sish, muvaffaqiyat va moliya (Spotify, Uzum Bank). Qizil &mdash; tezlik, e'tibor va ishtaha (YouTube, Netflix, KFC).

### HEX va HSB rang modellari
- **HEX (`#1877F2`):** Veb va UI dasturlashda ishlatiladigan 16-lik tizimdagi rang kodi.
- **HSB (Hue, Saturation, Brightness):** Dizaynerlar uchun eng qulay model: Hue (rangning o'zi: 0–360°), Saturation (to'yinganlik: 0–100%), Brightness (yorqinlik: 0–100%).

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Color Palette | Ranglar palitrasi &mdash; interfeysda ishlatiladigan tanlangan ranglar to'plami |
| Monochromatic | Monoxromatik (bitta rangning soyalari) |
| Complementary | Komplementar (qarama-qarshi kontrast ranglar) |
| Accent Color | Aksent (e'tiborni tortuvchi asosiy tugma yoki havola rangi) |
| Contrast Ratio | Kontrast nisbati &mdash; matn va fon yorqinligi farqi (4.5:1) |
| WCAG | Web Content Accessibility Guidelines &mdash; qulaylik va ochiqlik standartlari |

## Bilasizmi?

- Dunyo aholisining qariyb 8% erkaklari va 0.5% ayollarida rang ajrata olmaslik (daltonizm) xususiyati bor. Shu sababli muhim ma'lumotlarni faqat rang bilan emas, matn yoki belgi bilan ham ifodalash kerak.
- Yirik kompaniyalar (Google, Apple) interfeys ranglarini tanlashda yuzlab A/B testlar o'tkazib, tugma rangining 1% o'zgarishi daromadga qanday ta'sir qilishini o'rganadilar.

## Topshiriqlar

### 1. Monoxromatik to'rtburchaklar · oson

Figma'da 4 ta to'rtburchak chizing va bitta rangning (masalan, binafsha) 4 xil och-to'q soyasini bering. HSB da faqat S va B ni o'zgartiring.

**Kutiladigan natija:** 4 ta bir oilaviy rang: ton (H) bir xil, to'yinganlik va yorqinlik har xil.

### 2. Komplementar juftlik · oson

Rang g'ildiragi bo'yicha qarama-qarshi juftini toping: a) ko'k; b) qizil; c) sariq.

**Kutiladigan natija:** 3 ta juftlik va har birining g'ildirakdagi o'rni chizilgan.

### 3. Pipetka bilan HEX · oson

Figma'da pipetka (`I` tugmasi) bilan sevimli ilovangiz logotipining asosiy HEX rangini aniqlang.

**Kutiladigan natija:** logotip skrinshoti va uning HEX kodi yozilgan rangli to'rtburchak.

### 4. Kontrastli tugma · oson

To'q ko'k fonli tugma chizing va ichiga oq matn bilan «Boshlash» deb yozing.

**Kutiladigan natija:** matn uzoqdan ham aniq o'qiladigan tugma.

### 5. 60-30-10 sxemasi · o'rta

3 ta doira chizing: 60% li doiraga och kulrang fon, 30% li doiraga oq karta rangi, 10% li doiraga yorqin aksent rang bering. Keyin shu ranglar bilan kichik ekran chizing.

**Kutiladigan natija:** sxema va ekran: aksent rang faqat asosiy tugma va havolalarda.

### 6. Kontrastni o'lchang · o'rta

Sariq fonga oq matnli va to'q kulrang fonga oq matnli tugmalarni kontrast tekshiruvchi vosita bilan o'lchang. Nega birinchisini ishlatib bo'lmaydi?

**Kutiladigan natija:** ikki nisbat yozilgan va WCAG 4.5:1 talabi bilan solishtirilgan.

### 7. Palitrani aniqlang · o'rta

Uchta mashhur ilovaning (masalan, Telegram, Spotify, Instagram) bosh ekranini ko'rib, har birida qaysi palitra turi (monoxromatik, analog, komplementar, triadik) ishlatilganini aniqlang.

**Kutiladigan natija:** 3 qatorli jadval: ilova, asosiy ranglar, palitra turi va qisqa sabab.

### 8. Tungi rejim · o'rta

Oq fonli kartani tungi rejimga o'tkazing: fon juda to'q kulrang, karta biroz ochroq, matn och kulrang bo'lsin.

**Kutiladigan natija:** kunduzgi va tungi nusxa yonma-yon; ikkalasida ham matn aniq o'qiladi.

### 9. Madaniy farqlar · qiyin

Qizil rang Yevropa moliya bozorida pasayish, Xitoyda esa o'sish va omadni bildiradi. Xalqaro ilova uchun dizayner bundan qanday xulosa chiqarishi kerak?

**Kutiladigan natija:** 4-5 jumlalik javob: auditoriyani bilish, faqat rangga tayanmaslik (ikonka, matn ham qo'shish).

### 10. Xatoni toping · qiyin

Bitta ekranda 7 xil yorqin rang, och sariq fonda oq matn va 5 ta bir xil rangli tugma bor. Kamida 3 ta xatoni toping va tuzatilgan variantni chizing.

**Kutiladigan natija:** xatolar ro'yxati (ko'p rang, past kontrast, CTA ajralmaydi) va 60-30-10 ga mos tuzatilgan ekran.

### 11. Brend rangi tanlash · qiyin

Maktab kutubxonasi ilovasi uchun bitta asosiy brend rangini tanlang. Nega aynan shu rang? Unga mos monoxromatik va komplementar yordamchi ranglarni toping.

**Kutiladigan natija:** asosiy rang, 3 ta soya, 1 ta komplementar rang va 2-3 jumlalik asos.

### 12. Mahsulot kartasi · bonus

To'liq mahsulot kartasini chizing: rasm, nomi, narxi, qizil chegirma tegi va brend rangidagi «Savatga qo'shish» tugmasi. Barcha matnlar WCAG talabiga mos bo'lsin.

**Kutiladigan natija:** 60-30-10 ga mos, kontrasti tekshirilgan, chiroyli karta.

## O'zingizni tekshiring

1. Rang palitrasining 4 turini sanang.
2. Monoxromatik va analog palitra farqi nima?
3. Komplementar ranglar g'ildirakda qanday joylashadi?
4. 60-30-10 qoidasida har bir ulush nimaga beriladi?
5. WCAG bo'yicha oddiy va katta matn uchun minimal kontrast qancha?
6. Nega interfeysda bitta asosiy brend rangi tanlanadi?

## Uyga vazifa

«60-30-10 rang palitrasi va kontrast»: o'z brendingiz uchun 3 ta rang tanlang, «Mahsulot kartasi»ni chizing va tugma kontrasti kamida 4.5:1 ekanini tekshiring (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
