# 15-dars. Responsiv dizayn va media so'rovlar

> Saytni telefoningizda ochdingiz-u, matn juda mayda, rasm ekrandan chiqib ketgan, uni ko'rish uchun barmoq bilan kattalashtirish kerak. Bu — moslashmagan sayt. Bugun sahifani har qanday ekranga «o'zi moslashadigan» qilishni o'rganasiz.

## Dars xulosasi

- **Responsiv dizayn** — bitta sahifa telefon, planshet va kompyuter ekraniga o'zini moslashtiradi.
- `<meta name="viewport" content="width=device-width, initial-scale=1.0">` — `<head>` da har doim bo'lishi shart.
- **Fluid layout** — `%`, `fr`, `max-width` kabi nisbiy o'lchamlar.
- **Media so'rov**: `@media (min-width: 768px) { ... }` — shart bajarilganda ishlaydigan qoidalar.
- **Breakpoint** — dizayn o'zgaradigan kenglik: 576, 768, 992, 1200 px.
- **Mobile-first** — avval telefon, keyin `min-width` bilan kattaroq ekranlar; **desktop-first** — teskarisi, `max-width` bilan.
- Rasmlar: `max-width: 100%; height: auto;`, ramkani to'ldirish uchun `object-fit: cover`.

## Qo'shimcha ma'lumot

### 1. Suv o'xshatishi
Responsiv sahifa — suvga o'xshaydi: stakanga quysangiz stakan shaklini, kosaga quysangiz kosa shaklini oladi. Sahifa ham ekran «idishi»ga qarab shaklini o'zgartiradi.

### 2. `min-width` va `max-width`ni adashtirmaslik
```css
@media (min-width: 768px) { ... }  /* 768 va undan KATTA — «kamida 768» */
@media (max-width: 767px) { ... }  /* 767 va undan KICHIK — «ko'pi bilan 767» */
```
Eslab qolish: **min** — «eng kami», ya'ni ekran shundan katta bo'lishi kerak.

### 3. Mobile-first namunasi
```css
.kartalar { display: grid; grid-template-columns: 1fr; gap: 16px; }  /* telefon */

@media (min-width: 768px) {                                      /* planshet */
  .kartalar { grid-template-columns: repeat(2, 1fr); }
}
@media (min-width: 992px) {                                      /* noutbuk */
  .kartalar { grid-template-columns: repeat(3, 1fr); }
}
```

### 4. Rasmlar
```css
img     { max-width: 100%; height: auto; }      /* toshmaydi, cho'zilmaydi */
.muqova { width: 100%; height: 200px; object-fit: cover; }  /* kesib to'ldiradi */
```

### 5. DevTools'da sinash
F12 → **Toggle device toolbar** (Ctrl+Shift+M). Yuqoridan iPhone, iPad yoki o'z kengligingizni tanlang va oynani sudrab breakpointlarni kuzating.

### 6. Odatiy xatolar
- `viewport` tegi unutilgan.
- `@media min-width: 768px` — qavslar yo'q, ishlamaydi.
- Media so'rov asosiy qoidadan **yuqorida** yozilgan — pastdagi qoida uni bosib o'tadi.
- Rasmga qat'iy `width: 800px` berilgan — telefonda gorizontal aylantirish paydo bo'ladi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Responsiv dizayn | Har qanday ekranga moslashadigan dizayn |
| Viewport | Brauzerdagi sahifa ko'rinadigan maydon |
| Fluid layout | Nisbiy o'lchamlardagi «oquvchan» maket |
| Flexible grid | `fr`/`%` dagi moslashuvchan to'r |
| Media so'rov (`@media`) | Shartga qarab ishlaydigan CSS qoidalari bloki |
| Breakpoint | Dizayn o'zgaradigan ekran kengligi |
| min-width | «Kamida shuncha keng bo'lsa» sharti |
| max-width | «Ko'pi bilan shuncha keng bo'lsa» sharti; elementda — kenglik chegarasi |
| Mobile-first | Avval telefon uchun yozish yondashuvi |
| Desktop-first | Avval kompyuter uchun yozish yondashuvi |
| object-fit | Rasm ramkani qanday to'ldirishi |

## Bilasizmi?

- «Responsive web design» atamasini 2010-yilda veb-dizayner Ethan Marcotte o'z maqolasida taklif qilgan.
- Bugun internetdagi tashriflarning yarmidan ko'pi mobil qurilmalardan bo'ladi — shuning uchun ko'p jamoalar dizaynni telefondan boshlaydi.
- Google qidiruvi saytlarni baholashda asosan ularning mobil versiyasiga qaraydi (mobile-first indexing).
- Bootstrap'ning breakpointlari (576, 768, 992, 1200 px) — keyinchalik o'rganadigan freymvorkingizda ham aynan shu raqamlarni ko'rasiz.

## Topshiriqlar

### 1. Viewport · oson
Sahifangiz `<head>` qismiga `viewport` meta tegini qo'shing va DevTools'da telefon rejimida tegli va tegsiz holatni solishtiring.
**Kutiladigan natija:** tegsiz sahifa mayda ko'rinadi.

### 2. Rang almashadi · oson
Fon telefonda sariq, 768px dan kengda ko'k bo'lsin.
**Kutiladigan natija:** oyna kengligi o'zgarganda fon almashadi.

### 3. Toshmaydigan rasm · oson
Katta rasmga `max-width: 100%; height: auto;` bering va oynani toraytiring.
**Kutiladigan natija:** rasm ekrandan chiqmaydi.

### 4. Markazdagi konteyner · oson
`.konteyner { width: 90%; max-width: 1000px; margin: 0 auto; }` yozing va keng/tor oynada kuzating.
**Kutiladigan natija:** kengda 1000px, torda 90%.

### 5. Shrift o'lchami · o'rta
`h1` telefonda 28px, 992px dan kengda 44px bo'lsin.
**Kutiladigan natija:** sarlavha kattalashadi.

### 6. 1 → 2 → 3 ustun · o'rta
6 ta kartani mobile-first usulida 1, 2 va 3 ustunga moslang.
**Kutiladigan natija:** 3 ta breakpoint skrinshoti.

### 7. min yoki max? · o'rta
`@media (max-width: 600px)` va `@media (min-width: 600px)` qachon ishlashini 400px, 600px va 900px ekran uchun yozing.
**Kutiladigan natija:** 6 ta javob.

### 8. Bir xil muqovalar · o'rta
Turli o'lchamdagi 3 ta rasmni `height: 200px; object-fit: cover;` bilan bir xil ko'rinishga keltiring.
**Kutiladigan natija:** rasmlar cho'zilmagan, teng balandlikda.

### 9. Menyu yo'nalishi · qiyin
Header menyusi telefonda ustun (`column`), 768px dan kengda qator (`row`) bo'lsin.
**Kutiladigan natija:** menyu yo'nalishi o'zgaradi.

### 10. Moslashuvchan maket · qiyin
14-darsdagi maketni moslang: telefonda 1 ustun, 768px dan boshlab sidebar chapda.
**Kutiladigan natija:** ikki xil maket skrinshoti.

### 11. Xatoni toping · qiyin
```css
@media (min-width: 768px) { .kartalar { grid-template-columns: repeat(2, 1fr); } }
.kartalar { display: grid; grid-template-columns: 1fr; }
```
Nega planshetda ham 1 ustun? Tuzating.
**Kutiladigan natija:** media so'rov pastga ko'chirilgan.

### 12. Sayt «ovchisi» · bonus
3 ta mashhur saytni DevTools'ning telefon rejimida oching va ular qaysi breakpointlarda o'zgarishini yozing.
**Kutiladigan natija:** jadval va skrinshotlar.

## O'zingizni tekshiring

1. Responsiv dizayn nima va nega kerak?
2. `viewport` meta tegi nima qiladi?
3. Fluid layout'da qanday birliklar ishlatiladi?
4. `@media (min-width: 992px)` qachon ishlaydi?
5. Breakpoint nima? 3 ta misol keltiring.
6. Mobile-first va desktop-first farqi?
7. Rasm konteynerdan chiqmasligi uchun nima yoziladi?

## Uyga vazifa

Kartalar sahifasini mobile-first usulida 1 → 2 → 3 ustunga moslashtiring va menyuni telefonda ustun qiling. 20–30 daqiqa. Batafsil — haftalik uyga vazifada.
