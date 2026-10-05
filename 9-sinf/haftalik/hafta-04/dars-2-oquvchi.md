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

1. **Monoxromatik to'rtburchaklar · oson**  
   Figma'da 4 ta to'rtburchak chizing va bitta rangning (masalan binafsha) 4 xil och-to'q soyasini bering.

2. **Komplementar juftlik · oson**  
   Rang g'ildiragidan foydalanib quyidagi ranglarning qarama-qarshi (komplementar) juftini toping:  
   a) Ko'k &rarr; ?  
   b) Qizil &rarr; ?  
   c) Sariq &rarr; ?

3. **HEX kodlarini aniqlash · oson**  
   Figma'da «Eyedropper» (pipetka &mdash; `I` tugmasi) orqali sevimli ilovangiz logotipining asosiy rang HEX kodini aniqlang.

4. **Kontrastli tugma · oson**  
   To'q ko'k (`#0D47A1`) fonga ega tugma chizing va uning ichiga oq (`#FFFFFF`) matn bilan `"Boshlash"` deb yozing.

5. **60-30-10 qoidasi sxemasi · o'rta**  
   Figma'da 3 ta doira chizing: 60% lik doiraga och kulrang fon, 30% lik doiraga oq karta rangi, 10% lik doiraga yorqin yashil aksent rangini bering.

6. **WebAIM tekshiruvi · o'rta**  
   Sariq fonga oq matn yozilgan tugma va to'q kulrang fonga oq matn yozilgan tugmaning kontrast nisbatini solishtiring. Nega birinchisidan foydalanish taqiqlanadi?

7. **Ta'lim platformasi palitrasi · o'rta**  
   Maktab o'quvchilari uchun ta'lim ilovasi dizayniga mos 3 ta rang (Fon: `#F8FAFC`, Asosiy matn: `#1E293B`, Aksent: `#3B82F6`) tanlang va kichik test oynasini chizing.

8. **Tungi rejim (Dark mode) palitrasi · o'rta**  
   Kunduzgi rejimdagi oq fonli kartani qorong'i rejimga (`#121212` fon, `#1E1E1E` karta, `#E0E0E0` matn) o'tkazing.

9. **Madaniy farqlar tahlili · qiyin**  
   Qizil rangning Yevropa moliya bozorlaridagi ma'nosi (pasayish / xavf) va Xitoy moliya bozorlaridagi ma'nosi (o'sish / omad) nima uchun farqlanishini va dizayner bundan qanday xulosa chiqarishi kerakligini yozma bayon qiling.

10. **Mahsulot kartasi (Product Card) · bonus**  
    Figma'da to'liq mahsulot kartasini chizing: Mahsulot rasmi, Nomi, Narxi, Chegirma tegi (qizil), «Savatga qo'shish» tugmasi (aksent brend rangi) va barcha WCAG kontrast talablariga rioya qiling.
