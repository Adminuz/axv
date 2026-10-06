# 15-dars. SEO tamoyillari va meta teglarni to'g'ri qo'llash

**Fan:** Advanced UX/UI dizayn va Advanced Front-end
**Sinf:** 10-sinf
**Hafta:** 5-hafta, 3-dars (umumiy 15-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** `_matn/oquv-qollanma.txt`, V bob, 5.1 (`title`, `viewport`, semantik HTML ning SEO ga foydasi). `description`, canonical, Open Graph, `robots`, sitemap rejadagi mavzu bo'yicha standart bilimdan qo'shildi.

---

## Darsning maqsadi

O'quvchi SEO nima ekanini va semantik HTML bilan aloqasini tushuntiradi, `head` ga `charset`, `viewport`, `title`, `description`, `lang`, canonical va Open Graph teglarini to'g'ri yozadi, `robots` va sitemap vazifasini biladi.

## Kutiladigan natija

- SEO ning maqsadini va 3 ta asosiy omilini (kontent, tuzilma, texnik) ayta oladi;
- `head` ga `charset`, `viewport`, `title`, `description` yozadi;
- Har sahifaga takrorlanmas `title` va `description` beradi;
- Open Graph, canonical va `robots` vazifasini tushuntiradi.

## Kerakli jihozlar

- Har bir o'quvchi uchun kompyuter, brauzer va matn muharriri
- Brauzer DevTools va Lighthouse (SEO bo'limi)
- Proyektor/monitor; zaxira: A4 qog'oz (qidiruv natijasi eskizi uchun)

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 00–08 | Takrorlash | 14-dars: forma, validatsiya, xato xabarlari |
| 08–22 | Yangi mavzu 1 | SEO nima va nima uchun kerak |
| 22–32 | Yangi mavzu 2 | `head` teglari: `charset`, `viewport`, `title`, `description` |
| 32–38 | Tanaffus + mini-quiz | Slayddagi `.quiz` |
| 38–50 | Yangi mavzu 3 | Open Graph, canonical, `robots`, sitemap |
| 50–75 | Amaliyot | Maktab saytiga meta teglar qo'shish va Lighthouse |
| 75–80 | Xulosa | Tezkor nazorat, uyga vazifa |

---

## Konspekt (mentor aytadigan matn)

### 1. SEO asoslari

SEO (Search Engine Optimization) — saytni qidiruv tizimlarida (masalan Google) yaxshiroq topiladigan qilish. Qidiruv roboti sahifani o'qiydi, mazmunini tushunadi va saralaydi. Unga yordam beradigan uchta narsa: foydali **kontent**, ma'noli **tuzilma** (semantik teglar, bitta `h1`, `alt`) va **texnik** tomon (tezlik, mobil moslik, to'g'ri meta teglar). 13-darsda o'rgangan semantik HTML shu yerda to'g'ridan-to'g'ri foyda beradi. SEO natijani kafolatlamaydi, lekin sahifani tushunarli qiladi.

Bitta `h1`, mazmunli `alt` va ketma-ket sarlavhalar robot va foydalanuvchiga bir xil yordam beradi.

### 2. `head` dagi asosiy teglar

`head` ichidagi teglar brauzer va qidiruv robotiga sahifa haqida ma'lumot beradi. `meta charset="UTF-8"` — o'zbek harflari to'g'ri ko'rinishi uchun. `meta name="viewport"` — mobil qurilmada sahifa kengligini moslaydi. `title` — brauzer yorlig'i va qidiruv natijasidagi sarlavha: har sahifada takrorlanmas va aniq bo'lsin (taxminan 60 belgigacha). `meta name="description"` — qidiruv natijasidagi qisqa tavsif (taxminan 150–160 belgi). `html lang="uz"` esa tilni bildiradi.

`title` va `description` har sahifada har xil bo'lsin. Barcha sahifaga bir xil matn yozish — keng tarqalgan xato.

### 3. Open Graph, canonical, `robots`, sitemap

Open Graph (`og:title`, `og:description`, `og:image`) havola Telegram yoki Facebook da ulashilganda chiqadigan kartochkani boshqaradi. `link rel="canonical"` bir xil kontentli bir necha manzil bo'lsa, asosiy manzilni ko'rsatadi. `meta name="robots"` robotga sahifani indekslash yoki indekslamaslikni aytadi (`noindex`). `robots.txt` va `sitemap.xml` saytning ildizida turadi: birinchisi robotga qayerga kirish mumkinligini, ikkinchisi sahifalar ro'yxatini beradi.

`noindex` yozilgan sahifa qidiruvda chiqmaydi. Uni bosh sahifaga tasodifan qo'yib yubormang.

---

## Kod namunasi

To'liq `head`:

```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Qabul 2026 | 1-maktab</title>
  <meta name="description" content="1-maktabga qabul: hujjatlar, muddatlar va ariza formasi.">
  <link rel="canonical" href="https://maktab.uz/qabul">
  <meta property="og:title" content="Qabul 2026">
  <meta property="og:description" content="Hujjatlar va muddatlar.">
  <meta property="og:image" content="https://maktab.uz/qabul.jpg">
</head>
```

robots.txt namunasi:

```text
User-agent: *
Disallow: /admin/
Sitemap: https://maktab.uz/sitemap.xml
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). title va description
Maktab bosh sahifasi uchun `title` va `description` yozing.

**Kutiladigan natija:** Ikkala teg bor, matn aniq.

**Yechim:** `<title>1-maktab | Bosh sahifa</title>` va `<meta name="description" content="...">`.

### 2-topshiriq (o'rta). head ni to'ldiring
`head` ga `charset`, `viewport`, `title`, `description` qo'shing va `html` ga `lang="uz"` yozing.

**Kutiladigan natija:** To'liq `head`.

**Yechim:** Namunaviy kodga qarang.

### 3-topshiriq (qiyin). Maktab sayti uchun SEO
3 sahifa (bosh, qabul, aloqa) uchun takrorlanmas `title`/`description`, Open Graph va canonical yozing; Lighthouse SEO hisobotini oling.

**Kutiladigan natija:** Har sahifada boshqa `title`; Lighthouse SEO ball oshgan.

**Yechim:** Har sahifaga o'z `title` va `description`, `og:` va `canonical`; hisobotda tavsiyalar bajarilgan.

### 4-topshiriq (qo'shimcha). noindex
`noindex` qachon kerak? Misol keltiring.

**Kutiladigan natija:** Indekslash kerak bo'lmagan sahifa.

**Yechim:** Rahmat sahifasi yoki admin panel kabi sahifalar qidiruvda chiqmasligi kerak.

---

## Tezkor nazorat (dars oxirida)

1. SEO nima? — Saytni qidiruv tizimlarida yaxshi topiladigan qilish.
2. `title` va `description` farqi? — `title` — sarlavha, `description` — qisqa tavsif.
3. `viewport` nima uchun? — Mobil qurilmada sahifa kengligini moslash uchun.
4. Open Graph nima? — Ulashilgan havola kartochkasini boshqaruvchi teglar.
5. `canonical` nima? — Asosiy manzilni ko'rsatadi.

## Keng tarqalgan xatolar

- Barcha sahifaga bir xil `title` yozish.
- `description` ni yozmaslik yoki juda uzun yozish.
- `viewport` ni unutish (mobilda mayda ko'rinadi).
- `html` ga `lang` yozmaslik.
- `noindex` ni tasodifan qoldirish.
- Kalit so'zlarni ortiqcha takrorlash.

## Bilasizmi? (Internetdan, qo'shimcha)

- Qidiruv natijasida odatda `title` sarlavha, `description` esa tavsif bo'ladi, lekin Google ularni o'zgartirishi mumkin.
- `robots.txt` robotlarga tavsiya beradi, uni yashirish vositasi deb bo'lmaydi.
- Lighthouse da SEO bo'limi mavjud va uni bepul ishlatish mumkin.
