# 5-hafta: Uyga vazifa

**Fan:** Advanced UX/UI dizayn va Advanced Front-end  
**Sinf:** 10-sinf  
**Hafta:** 5-hafta  
**Topshirish muddati:** Keyingi darsga qadar (6-hafta, 1-dars)

---

## Topshiriq 1: Maktab sayti, 3 sahifa · qiyin

Maktab sayti uchun 3 ta HTML sahifa yozing: `index.html`, `qabul.html`, `aloqa.html`.

- Har sahifada semantik tuzilma: `header` + `nav` (`ul` ichida havolalar), `main` (bitta `h1`), `footer`.
- `index.html` da kamida 3 ta `article` va 2 ta rasm; barcha rasmlarga mazmunli `alt`.
- `qabul.html` da qabul formasi: ism, email, telefon (`pattern="\+998[0-9]{9}"`), sinf (`min`/`max`), rozilik (`checkbox`), `submit` tugmasi.
- Har maydonda `label` (`for` = `id`), `required` va telefon uchun tushunarli xato xabari (`aria-describedby`).

---

## Topshiriq 2: Meta teglar va SEO · o'rta

Har sahifaning `head` ida:

- `meta charset`, `viewport`, `html lang="uz"`;
- takrorlanmas `title` (taxminan 60 belgigacha) va `description` (taxminan 150–160 belgi);
- `canonical` va Open Graph (`og:title`, `og:description`).

---

## Topshiriq 3: Tahlil · oson

Lighthouse (Accessibility va SEO) ni ishga tushiring. `tahlil.txt` faylida (har biri 2–3 jumla):

1. Qaysi 2 ta xatoni topdingiz va qanday tuzatdingiz?
2. Semantik teglar va meta teglar sahifaga nima berdi?

---

## Baholash mezoni

| Mezon | Ball |
|---|---|
| Semantik sahifa (landmark, bitta `h1`, `alt`) | 3 |
| Qabul formasi va validatsiya | 3 |
| Meta teglar va SEO (3 sahifa) | 2 |
| tahlil.txt: 2 savolga javob | 2 |
| **Jami** | **10** |
| Bonus: Lighthouse Accessibility va SEO ≥ 90 | +2 |

---

## Mentor uchun

**Tekshirish:**
- Sahifalarni brauzerda oching, DevTools da `main` va `h1` sonini tekshiring.
- Formani bo'sh va noto'g'ri qiymat bilan yuborib, brauzer xabarini ko'ring; faqat klaviatura bilan to'ldirib ko'ring.
- `view-source` da `title` va `description` har sahifada har xilligini tekshiring.

**Keng tarqalgan xato:** `label` o'rniga faqat `placeholder`; `for` va `id` mos emas; hamma sahifada bir xil `title`; `viewport` unutilgan.
