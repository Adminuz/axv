# 6-dars. Filtrlash, qidiruv va tartiblash

> Yuz minglab ma'lumotlar ichidan foydalanuvchiga aynan kerakli bitta yangilikni 10 millisoniyada topib berish — haqiqiy backend ustasining mahoratidir! Ushbu darsda biz `django-filter` kutubxonasini o'rganamiz, to'liq matnli qidiruv va moslashuvchan saralash tizimini NewsPortal ga ulaymiz.

## Dars xulosasi

- Katta hajmdagi ma'lumotlar bazasida **Filtrlash**, **Qidiruv** va **Tartiblash** mexanizmlari server unumdorligini va foydalanuvchi tajribasini ta'minlovchi asosiy omildir.
- **Filtrlash (Filtering)** &mdash; aniq mezonlar (status, kategoriya, muallif, sana) bo'yicha ma'lumotlarni saralaydi.
- **`django-filter`** kutubxonasi yordamida URL query-parametrlarini (`?category=1&status=published`) to'g'ridan-to'g'ri Django ORM so'rovlariga xavfsiz bog'lash mumkin.
- **Matnli qidiruv (`SearchFilter`)** &mdash; `?search=matn` parametri orqali bir vaqtning o'zida sarlavha (`title`), qisqa mazmun (`excerpt`) va matn (`body`) ichidan kalit so'zlarni topadi.
- **Tartiblash (`OrderingFilter`)** &mdash; natijalarni sana, ko'rishlar soni yoki alifbo tartibida o'sish (`?ordering=title`) va kamayish (`?ordering=-published_at`) bo'yicha taxlaydi.
- `apps/news/filters.py` dagi `PostFilter` orqali sanalar oralig'ini (`published_from`, `published_to`) qidirish imkoniyati yaratiladi.

## Qo'shimcha ma'lumot

### 1. Kutubxona analogiyasi: Kartoteka, Katalog va Qidiruv

Katta shahar kutubxonasini tasavvur qiling:
- **Filtrlash:** Siz kutubxonachiga: "Menga faqat 2024-yildan keyin chop etilgan, o'zbek tilidagi, dasturlashga oid kitoblarni bering", deysiz. Kutubxonachi millionta kitob orasidan faqat shu mezonlarga mos 50 tasini ajratadi.
- **Qidiruv:** Siz: "Kitobning nomi esimda yo'q, lekin ichida 'neyron tarmoqlari' degan so'z bor edi", deysiz. Kutubxonachi kompyuter qidiruviga shu so'zni kiritadi va kitoblar matnini tahlil qiladi.
- **Tartiblash:** Siz: "Bu kitoblarni menga eng yangisidan boshlab, yillari bo'yicha taxlab bering", deysiz.

Mana shu uchta amal birgalikda API ga bitta satrda yuboriladi:
`GET /api/v1/posts/?category=2&search=neyron&ordering=-published_at`

### 2. URL Query Parametrlari qanday tuziladi?

URL manzilida asosiy yo'ldan keyin so'roq belgisi (`?`) qo'yiladi va parametrlar `kalit=qiymat` shaklida yoziladi.
Bir nechta parametrlar ampersand (`&`) belgisi bilan bog'lanadi:
- `?status=published` &mdash; bitta filtr;
- `?status=published&category=1` &mdash; ikkita filtr bir vaqtda;
- `?tags=1&tags=3` &mdash; ko'p tanlovli filtr (ManyToMany teglar uchun);
- `?ordering=-created_at,title` &mdash; avval sana bo'yicha kamayish, teng bo'lsa sarlavha bo'yicha o'sish.

### 3. PostgreSQL da to'liq matnli qidiruv (Full-Text Search)

SQLite dastlabki ishlab chiqish uchun qulay bo'lsa-da, u faqat oddiy matnli `LIKE '%so'z%'` tekshiruvini bajaradi. Bu esa millionlab ma'lumotlarda sekin ishlaydi.
Haqiqiy ishlab chiqarishda (Production) esa PostgreSQL ning o'rnatilgan Full-Text Search imkoniyati ishga tushiriladi:
- So'zlarning o'zagini ajratadi (masalan: "dasturchilar", "dasturlash", "dasturchi" so'zlarining barchasini "dastur" o'zagi bo'yicha topadi);
- Xato yozilgan harflarni (typo) tushunadi;
- Eng mos keladigan maqolalarni birinchi o'ringa chiqaradi (relevance ranking).

### 4. Dasturchilar ko'p yo'l qo'yadigan xatolar

- **Xato 1: SQL Injection xavfi bo'lgan qo'lda filtrlash.** Ba'zi dasturchilar `Post.objects.raw(f"SELECT * FROM news_post WHERE title = '{q}'")` deb yozishadi. Bu o'ta xavfli! `django-filter` va DRF esa barcha kiruvchi parametrlarni avtomatik tarzda tozalaydi va himoyalaydi.
- **Xato 2: Qidiruv maydonlariga indeks qo'yishni unutish.** Agar modelda `title` va `status` bo'yicha doimiy filtr bo'lsa, modelning `Meta.indexes` qismiga ushbu maydonlar kiritilishi shart. Aks holda baza har safar butun jadvalni boshidan oxirigacha titkilab chiqadi (Full Table Scan).

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Query Parameters** | URL manzilining oxirida `?` belgisidan so'ng uzatiladigan qo'shimcha parametrlar. |
| **Filtering (Filtrlash)** | Ma'lumotlarni berilgan aniq shartlar (tenglik, kattalik, kiritilganlik) bo'yicha saralab olish. |
| **SearchFilter** | Berilgan matnni bir nechta ustunlar ichidan qidirib topuvchi DRF filtri. |
| **OrderingFilter** | Natijalar tartibini foydalanuvchi xohishiga ko'ra o'sish yoki kamayish tartibida belgilovchi filtr. |
| **django-filter** | Django va DRF uchun moslashuvchan va kuchli filtrlash vositalarini beruvchi mashhur kutubxona. |
| **FilterSet** | Muayyan model uchun qaysi maydonlar qanday usulda filtrlanishini belgilovchi deklarativ sinf. |
| **gte (Greater Than Equal)** | "Katta yoki teng" solishtirish operatori (`>=`). |
| **lte (Less Than Equal)** | "Kichik yoki teng" solishtirish operatori (`<=`). |
| **IsoDateTimeFilter** | ISO 8601 xalqaro standartidagi sanalar (`2026-10-04T12:00:00`) bo'yicha filtrlash maydoni. |
| **Indexes (Indekslar)** | Ma'lumotlar bazasida qidiruv va tartiblash tezligini yuzlab barobar oshiruvchi maxsus ko'rsatkichlar. |

## Bilasizmi?

- Google qidiruv tizimi dunyodagi eng katta va eng tezkor filtrlash arxitekturasiga ega bo'lib, u sekundiga 100 000 dan ortiq murakkab so'rovlarga 0.2 soniya ichida javob qaytaradi!
- Indekslar ma'lumotlar bazasida xuddi kitobning oxiridagi mundarija kabi ishlaydi: kitobning har bir sahifasini o'qib chiqmasdan, mundarijadan kerakli mavzu qaysi sahifadaligini darhol bilib olasiz.
- DRF ning Browsable API interfeysi `django-filter` ulangan paytda ekranning o'ng tomonida avtomatik "Filters" tugmachasini ochadi va siz brauzerning o'zida shaklni to'ldirib so'rov yuborishingiz mumkin.

## Topshiriqlar

### 1. URL parametrlarini tahlil qilish · oson
Quyidagi URL qanday natijalarni qaytarishini tahlil qiling:
`GET /api/v1/posts/?category=2&ordering=-created_at`
1. Qaysi kategoriya tanlangan?
2. Maqolalar qanday tartibda saralangan?
**Kutiladigan natija:** Ikkala savolga aniq va qisqa javob.

### 2. Qidiruv so'rovi tuzish · oson
"Python dasturlash" so'zlari qatnashgan barcha yangiliklarni qidirish uchun `posts` endpointiga qanday URL so'rovi yuboriladi?
**Kutiladigan natija:** To'g'ri `?search=...` havolasi.

### 3. gte va lte ma'nosi · oson
Django ORM va `django-filter` da `gte` va `lte` qisqartmalari qanday inglizcha so'zlardan olingan va ular qanday matematik belgilarga (`>=`, `<=`, `>`, `<`) mos keladi?
**Kutiladigan natija:** Inglizcha ochilishi va matematik belgilari.

### 4. Tartiblash belgisi · oson
`OrderingFilter` da `?ordering=title` bilan `?ordering=-title` o'rtasidagi farq nimada? Minus (`-`) belgisi nima vazifani bajaradi?
**Kutiladigan natija:** Ikki xil tartiblash yo'nalishining farqi.

### 5. PostFilter klassini yozish · o'rta
`apps/news/filters.py` faylida `PostFilter` klassini yozing:
- `category` (aniq tenglik);
- `status` (aniq tenglik);
- `published_from` (`published_at` bo'yicha `gte`);
- `published_to` (`published_at` bo'yicha `lte`).
**Kutiladigan natija:** To'liq sintaksis bilan yozilgan `PostFilter` klassi.

### 6. ViewSetda filtr parametrlarini birlashtirish · o'rta
`PostViewSet` ichida bir vaqtning o'zida ham maxsus filtr (`PostFilter`), ham qidiruv (`title`, `body`), ham tartiblash (`created_at`, `published_at`) ishlashi uchun qaysi 4 ta sinf o'zgaruvchisi (atributi) qanday qiymatlar bilan yozilishi kerak?
**Kutiladigan natija:** ViewSet ichidagi 4 ta atribut kodlari.

### 7. Ko'p tegli (ManyToMany) filtrlash · o'rta
Foydalanuvchi bir vaqtning o'zida ham "AI" (ID: 1), ham "Python" (ID: 3) teglari bor maqolalarni ko'rmoqchi.
Ushbu so'rov URL parametrlarida qanday ifodalanadi? `django-filter` buni qanday qabul qiladi?
**Kutiladigan natija:** URL ko'rinishi va tushuntirish.

### 8. Kod tahlili: Xatoni topish · o'rta
Boshlovchi dasturchi quyidagi kodni yozdi:
```python
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    search_fields = ["title", "body"]
    ordering_fields = ["created_at"]
```
Lekin brauzerda `?search=python` deb yozsa ham, qidiruv umuman ishlamayapti, barcha maqolalar chiqyapti. Nima sababdan? Qaysi sozlama unutilgan?
**Kutiladigan natija:** Xatolik sababi (`DEFAULT_FILTER_BACKENDS` yoki `filter_backends` unutilgani) va uni to'g'rilash yo'li.

### 9. Mini-loyiha: Do'kon mahsulotlari filtri · qiyin
Elektron do'kon uchun `Product` modeli mavjud (maydonlar: `name`, `price`, `rating`, `in_stock`, `category`).
1. Foydalanuvchilar narx oralig'i (`min_price`, `max_price`), minimal reyting (`min_rating`) va faqat mavjud mahsulotlar (`in_stock=true`) bo'yicha qidira olishi uchun `ProductFilter` yozing.
2. Nomi bo'yicha qidiruv va narx bo'yicha saralash sozlamalarini ko'rsating.
**Kutiladigan natija:** To'liq FilterSet va ViewSet kodi.

### 10. Starts-with va Exact qidiruv turlari · qiyin
DRF `search_fields` da maydon oldiga maxsus belgilar qo'yilishi mumkin:
- `search_fields = ['^title', '=status']`
1. `^` belgisi qanday qidiruvni anglatadi?
2. `=` belgisi qanday ishlaydi?
3. Nima uchun telefon raqami yoki pasport seriyasini qidirganda belgisiz emas, aynan `=` (exact) qo'yish maqsadga muvofiq?
**Kutiladigan natija:** Qidiruv prefikslari tahlili va amaliy sababi.

### 11. Baza unumdorligi: B-Tree va GIN indekslar · qiyin
Katta ma'lumotlar bazasida millionlab qatorlar bor bo'lganda:
1. Nega oddiy sonli va sanali ustunlar uchun B-Tree indekslari ishlatiladi?
2. Matnli qidiruv uchun nima sababdan GIN (Generalized Inverted Index) indekslari talab qilinadi?
3. Django modelida `models.Index` orqali qanday qilib ushbu indekslar e'lon qilinadi?
**Kutiladigan natija:** Indekslash mexanizmi va model kodi namunalari.

### 12. Bonus tadqiqot: Elasticsearch va DRF integratsiyasi · bonus
Juda yirik tizimlarda (Amazon, Uzum Market) relyatsion baza qidiruvi yetarli bo'lmay qoladi va maxsus qidiruv serverlari (Elasticsearch / MeiliSearch) ishlatiladi.
1. Elasticsearch nima va u qanday qilib millisoniyalarda millionlab tovarlar orasidan qidiradi?
2. `django-elasticsearch-dsl-drf` kutubxonasi yordamida DRF va Elasticsearch qanday bog'lanadi?
**Kutiladigan natija:** Elasticsearch va DRF integratsiyasi bo'yicha mustaqil tadqiqot.

## O'zingizni tekshiring

1. Filtrlash, qidiruv va tartiblash jarayonlarining bir-biridan qanday farqlari bor?
2. `django-filter` kutubxonasini Django loyihasiga qanday ulaymiz?
3. `search_fields` va `ordering_fields` qanday vazifalarni bajaradi?
4. URL da sanalar oralig'ini qidirish uchun `IsoDateTimeFilter` qanday parametrlar qabul qiladi?
5. URL dagi `-created_at` belgisi natijalarni qanday tartibda joylashtiradi?
6. Nima uchun filtrlash amallari har doim backend bazasida bajarilishi shart?

## Uyga vazifa

1. `src/apps/news/filters.py` faylini konspektdagi namuna asosida shakllantiring.
2. `PostViewSet` ga `filterset_class`, `search_fields` va `ordering_fields` ni bog'lang.
3. Postman yoki brauzer orqali quyidagi so'rovlarni amalda sinab ko'ring va natijalar to'g'ri qaytayotganiga ishonch hosil qiling:
   - `GET /api/v1/posts/?status=published`
   - `GET /api/v1/posts/?search=texnologiya`
   - `GET /api/v1/posts/?ordering=-published_at`
