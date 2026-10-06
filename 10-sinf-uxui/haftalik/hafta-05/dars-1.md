# 13-dars. Semantik HTML5 teglari va accessibility (WCAG) asoslari

**Fan:** Advanced UX/UI dizayn va Advanced Front-end
**Sinf:** 10-sinf
**Hafta:** 5-hafta, 1-dars (umumiy 13-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** `_matn/oquv-qollanma.txt`, V bob, 5.1 «Semantik HTML va accessibility» (semantik va non-semantik teglar, landmarklar, ARIA, anti-patternlar). WCAG tamoyillari (POUR, kontrast, alt) hujjatda alohida berilmagan, rejadagi mavzu bo'yicha qo'shildi.

---

## Darsning maqsadi

O'quvchi semantik va non-semantik teglar farqini biladi, sahifa tuzilmasini `header`, `nav`, `main`, `section`, `article`, `aside`, `footer` bilan yozadi, sarlavhalar iyerarxiyasini to'g'ri qo'llaydi, ARIA ni faqat kerak bo'lganda ishlatadi va WCAG ning 4 tamoyilini (POUR), `alt` matn va kontrast talabini tushuntiradi.

## Kutiladigan natija

- Semantik va non-semantik teglarni farqlaydi va 4 ta foydasini (accessibility, usability, maintainability, SEO) aytadi;
- Maket `div` larini `header`, `nav`, `main`, `section`, `footer` ga almashtiradi;
- Sarlavhalar iyerarxiyasini (`h1`–`h6`) va `alt` matnini to'g'ri qo'yadi;
- ARIA qoidasini («avval semantik HTML») va WCAG ning POUR tamoyillarini ayta oladi.

## Kerakli jihozlar

- Har bir o'quvchi uchun kompyuter, brauzer va matn muharriri (VS Code yoki oddiy Notepad)
- Brauzer DevTools yoki Lighthouse (Accessibility bo'limi) tekshiruv uchun
- Proyektor/monitor; zaxira: A4 qog'oz va qalam (teglar sxemasi uchun)

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 00–08 | Takrorlash | 12-dars: wireframe; header, menyu va footer qismlari |
| 08–22 | Yangi mavzu 1 | Semantik va non-semantik teglar, 4 ta foyda |
| 22–32 | Yangi mavzu 2 | Sahifa tuzilmasi: landmark teglar, sarlavhalar iyerarxiyasi |
| 32–38 | Tanaffus + mini-quiz | Slayddagi `.quiz` |
| 38–50 | Yangi mavzu 3 | ARIA va WCAG (POUR), `alt`, kontrast |
| 50–75 | Amaliyot | Maktab sayti wireframe ni semantik HTML ga o'tkazish |
| 75–80 | Xulosa | Tezkor nazorat, uyga vazifa |

---

## Konspekt (mentor aytadigan matn)

### 1. Semantik va non-semantik teglar

Semantik HTML (semantic markup) — kontentning ma'nosini va rolini aniq ifodalovchi teglardan foydalanish. Teg semantik bo'ladi, agar u ichidagi kontentga ma'no qo'shsa. Zamonaviy HTML da taxminan 30–40 semantik element bor: `h1`, `p`, `ul`, `table`, `figure`, `header`, `main`, `aside`, `nav`, `footer`. `div`, `span`, `br` esa non-semantik: ular ma'no bildirmaydi va asosan CSS bilan maket uchun ishlatiladi. Foydalari: **accessibility** (ekran o'qiydigan qurilmalar uchun), **usability**, **maintainability** (kodni qo'llab-quvvatlash) va **SEO**.

Ikkala variant ekranda bir xil ko'rinishi mumkin, lekin faqat ikkinchisi ekran o'qiydigan qurilma va qidiruv tizimiga sahifa tuzilmasini aytib beradi.

### 2. Landmark teglar va sarlavhalar iyerarxiyasi

Landmark teglar sahifaning «xaritasi»: `header` (yuqori qism), `nav` (asosiy navigatsiya), `main` (asosiy kontent, sahifada bitta), `aside` (qo'shimcha blok), `footer` (pastki qism). `section` — ma'noli guruh va odatda o'z sarlavhasi bo'ladi; `article` — mustaqil kontent (yangilik, post). Sarlavhalar iyerarxiyasi: sahifada bitta `h1`, undan keyin `h2`, `h3` tartib bilan, sakrashsiz. Navigatsiya havolalarini `nav` ichida `ul` ro'yxati qilib yozing. Boshqa sahifaga o'tkazish uchun `a`, amal bajarish uchun `button` ishlating.

Sahifada bitta `h1` va `main` bo'ladi. `h2` dan keyin to'g'ridan-to'g'ri `h4` yozmang: sarlavhalar iyerarxiyasi sakramasin.

### 3. ARIA, WCAG tamoyillari va alt matn

ARIA (Accessible Rich Internet Applications) `role` va `aria-*` atributlari bilan elementning maqsadini tushuntiradi. Qoida: **avval semantik HTML**, ARIA faqat mos teg bo'lmaganda. `nav`, `main`, `header` allaqachon o'z roliga ega, ortiqcha `role` qo'shmang. WCAG (Web Content Accessibility Guidelines) 4 tamoyilga tayanadi — **POUR**: Perceivable (sezish mumkin: `alt`, kontrast), Operable (boshqarish mumkin: klaviatura bilan), Understandable (tushunarli), Robust (mustahkam: to'g'ri HTML). Rasmga `alt` yoziladi, matn va fon kontrasti oddiy matn uchun kamida 4.5:1 bo'lishi tavsiya etiladi.

Bezak (dekorativ) rasmga `alt=""` yoziladi: ekran o'qiydigan qurilma uni o'tkazib yuboradi. `div` dan tab yasalganda ARIA kerak; tayyor `button` bo'lsa, ARIA kerak emas.

---

## Kod namunasi

Semantik sahifa skeleti (maktab sayti):

```html
<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <title>Maktab sayti</title>
</head>
<body>
  <header>
    <nav>
      <ul>
        <li><a href="/">Bosh sahifa</a></li>
        <li><a href="/qabul">Qabul</a></li>
        <li><a href="/aloqa">Aloqa</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <h1>Maktab yangiliklari</h1>
    <article>
      <h2>Olimpiada g'oliblari</h2>
      <p>Matn...</p>
    </article>
  </main>
  <footer>Aloqa: info@maktab.uz</footer>
</body>
</html>
```

Kontentni guruhlash:

```html
<section class="faq">
  <h2>Semantik HTML nima?</h2>
  <p>Bu kontent haqida ma'no beradigan HTML.</p>
</section>
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Teg juftlash
Quyidagilarni mos tegga bog'lang: yuqori qism; asosiy navigatsiya; asosiy kontent; pastki qism.

**Kutiladigan natija:** `header`, `nav`, `main`, `footer`.

**Yechim:** (a) `header`; (b) `nav`; (c) `main`; (d) `footer`.

### 2-topshiriq (o'rta). div ni almashtiring
`<div id="header">`, `<div id="content">`, `<div id="footer">` ni semantik teglarga almashtiring.

**Kutiladigan natija:** `header`, `main`, `footer`.

**Yechim:** `<header>...</header>`, `<main>...</main>`, `<footer>...</footer>`.

### 3-topshiriq (qiyin). Maktab sayti, semantik
12-darsdagi maktab sayti wireframe ini semantik HTML ga o'tkazing: header + nav, main (h1, 3 ta yangilik article), footer.

**Kutiladigan natija:** To'g'ri tuzilgan `index.html`, bitta `h1`, `nav` ichida `ul`.

**Yechim:** Kod namunasiga qarang: `header > nav > ul`, `main > h1 + article*3`, `footer`. Barcha rasmlarga mazmunli `alt`.

### 4-topshiriq (qo'shimcha). ARIA ni tekshiring
`<nav role="navigation">` yozilgan. Bu to'g'rimi? Sababini yozing.

**Kutiladigan natija:** ARIA ortiqcha.

**Yechim:** `nav` allaqachon `navigation` roliga ega; ortiqcha `role` kodni chalkashtiradi.

---

## Tezkor nazorat (dars oxirida)

1. Semantik HTML nima? — Kontent ma'nosini va rolini ifodalovchi teglardan foydalanish.
2. Semantikaning 4 foydasi? — Accessibility, usability, maintainability, SEO.
3. `main` sahifada nechta bo'ladi? — Bitta.
4. ARIA qachon kerak? — Mos semantik teg bo'lmaganda, masalan `div` dan tab yasalganda.
5. POUR nima? — WCAG ning 4 tamoyili: Perceivable, Operable, Understandable, Robust.

## Keng tarqalgan xatolar

- Hamma narsa uchun `div` va `span` ishlatish (div-sho'rva).
- Ma'nosiz ichma-ich `section` yozish.
- `article` yoki `aside` ni faqat bezak uchun ishlatish.
- Ortiqcha ARIA rollarini qo'shish (`nav role="navigation"`).
- `alt` yozmaslik yoki `alt="rasm"` kabi ma'nosiz matn yozish.
- Sarlavhalarni o'lchami uchun tanlash (`h4` ni kichik shrift uchun).

## Bilasizmi? (Internetdan, qo'shimcha)

- Zamonaviy HTML da taxminan 30–40 semantik element bor.
- Ekran o'qiydigan qurilma foydalanuvchiga sarlavhalar ro'yxatini ko'rsata oladi: shuning uchun `h1`–`h6` tartibi muhim.
- Google Search Central ham ma'noli sarlavhalar va iyerarxik tuzilmani tavsiya qiladi.
