# 15-dars. SEO tamoyillari va meta teglarni to'g'ri qo'llash

> Yaxshi sayt ham topilmasa, ko'rinmaydi. Bugun sahifani qidiruv va ulashishga tayyorlaymiz.

## Dars xulosasi

- SEO — saytni qidiruvda yaxshi topiladigan qilish: kontent, tuzilma, texnik tomon.
- Semantik HTML, bitta `h1`, `alt` SEO ga yordam beradi.
- `head` da: `charset`, `viewport`, `title`, `description`; `html` da `lang`.
- `title` va `description` har sahifada takrorlanmas bo'lsin.
- Open Graph ulashish kartochkasini, `canonical` asosiy manzilni boshqaradi.
- `robots` va sitemap robotga yo'l ko'rsatadi.

## Qo'shimcha ma'lumot

### title uzunligi
Qidiruv natijasida uzun `title` kesiladi, shuning uchun taxminan 60 belgigacha yozish tavsiya etiladi.

### Robots tavsiya
`robots.txt` robotlarga tavsiya beradi, maxfiy sahifalarni himoyalash uchun parol kerak.

### Ulashish kartochkasi
`og:image` bo'lmasa, Telegram yoki Facebook da havola oddiy ko'rinadi va bosilish kamayadi.

### Odatiy xatolar
Hamma sahifada bir xil `title`; `viewport` yo'q; `lang` yo'q.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| SEO | Qidiruv tizimlari uchun optimallashtirish |
| meta | Sahifa haqida ma'lumot beruvchi teg |
| title | Sahifa sarlavhasi |
| description | Qisqa tavsif |
| viewport | Mobil ko'rinish sozlamasi |
| Open Graph | Ulashish kartochkasi teglari |
| canonical | Asosiy manzil ko'rsatkichi |
| robots | Indekslash ko'rsatmasi |
| sitemap | Sahifalar ro'yxati |

## Bilasizmi?

- Qidiruv natijasida odatda `title` sarlavha, `description` esa tavsif bo'ladi, lekin Google ularni o'zgartirishi mumkin.
- `robots.txt` robotlarga tavsiya beradi, uni yashirish vositasi deb bo'lmaydi.
- Lighthouse da SEO bo'limi mavjud va uni bepul ishlatish mumkin.

## Topshiriqlar

### 1. SEO ta'rifi · oson

SEO nima va nima uchun kerak? 2 jumlada yozing.

**Kutiladigan natija:** Qidiruvda topilish uchun optimallashtirish.

### 2. Teglarni nomlang · oson

`charset`, `viewport`, `title`, `description` vazifasini yozing.

**Kutiladigan natija:** 4 ta to'g'ri vazifa.

### 3. lang · oson

`html` ga o'zbek tilini bildiruvchi atribut yozing.

**Kutiladigan natija:** `lang="uz"`.

### 4. Sarlavha · oson

Sahifada nechta `h1` bo'lishi tavsiya etiladi?

**Kutiladigan natija:** Bitta.

### 5. title yozing · o'rta

Qabul sahifasi uchun 60 belgigacha `title` yozing.

**Kutiladigan natija:** Aniq va qisqa `title`.

### 6. description yozing · o'rta

Qabul sahifasi uchun 150–160 belgilik tavsif yozing.

**Kutiladigan natija:** Mazmunli `description`.

### 7. viewport · o'rta

Mobil moslik uchun `viewport` ni yozing.

**Kutiladigan natija:** `width=device-width, initial-scale=1`.

### 8. Xatoni toping · o'rta

Barcha sahifalarda `<title>Sayt</title>` yozilgan. Nima xato?

**Kutiladigan natija:** `title` takrorlanmas bo'lishi kerak.

### 9. To'liq head · qiyin

3 sahifa uchun to'liq `head` yozing.

**Kutiladigan natija:** Har sahifada o'z meta teglari.

### 10. Open Graph · qiyin

Qabul sahifasi uchun `og:` teglarini yozing.

**Kutiladigan natija:** `og:title`, `og:description`, `og:image`.

### 11. Lighthouse SEO · qiyin

Lighthouse SEO hisobotini oling va 2 ta tavsiyani bajaring.

**Kutiladigan natija:** Ball oshgan hisobot.

### 12. robots.txt · bonus

`/admin/` ni yopuvchi va sitemap ni ko'rsatuvchi `robots.txt` yozing.

**Kutiladigan natija:** 3 qatorli fayl.

## O'zingizni tekshiring

1. SEO nima?
2. `head` dagi 4 asosiy teg?
3. `title` va `description` qanday bo'lishi kerak?
4. `viewport` nima uchun?
5. Open Graph nima?
6. `canonical` va `robots` farqi?

## Uyga vazifa

Maktab saytiga meta teglar qo'shing va Lighthouse SEO ni ishga tushiring (25 daqiqa). To'liq shart: `uyga-vazifa.md`.
