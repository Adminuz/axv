# 2-dars. HTML hujjat strukturasi. Teg, atribut, head, sarlavhalar

**Hafta:** 1 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliyot · **I-bob**, 2-dars

> Dasturda «HTML hujjat strukturasi, asosiy teglar, atributlar» mavzusiga 2 dars ajratilgan (2–3). Bo'linish: 2-dars — struktura, `<head>`, sarlavhalar; 3-dars — matn teglari, `<a>`, block/inline.

## 1. Dars rejasi

**Maqsad:** o'quvchi to'g'ri tuzilgan HTML hujjat yozadi, `<head>` ichidagi asosiy teglarni va `<h1>–<h6>` ni qo'llaydi.

**Kutiladigan natija:**
- `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>` vazifalarini biladi.
- Teg, atribut, element, ichma-ich joylashtirish (nesting) tushunchalarini biladi.
- `<title>`, `<meta charset>`, `<meta viewport>`, `<meta description>`, `<meta author>` ni yoza oladi.
- Sarlavhalarni (`h1`–`h6`) mantiqiy tartibda ishlatadi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 | Takrorlash | 1-dars: so'rov yo'li, front/back; uyga vazifa tekshiruvi |
| 10–30 | Yangi mavzu 1 | HTML nima, teg, atribut, hujjat skeleti |
| 30–35 | Tanaffus | |
| 35–50 | Yangi mavzu 2 | `<head>` va `<meta>` teglari, sarlavhalar |
| 50–75 | Amaliyot | «Men haqimda» sahifasi |
| 75–80 | Tezkor nazorat va xulosa | |

## 2. Konspekt

### 2.1. Takrorlash (10 daqiqa)
Savollar: DNS nima? Brauzer serverdan nimani oladi? Server qayerda, brauzer qayerda? Uyga vazifani ko'rib chiqing. Ko'prik: «Server bizga HTML faylni beradi. Bugun shu faylni o'zimiz yozishni o'rganamiz.»

### 2.2. HTML nima?
**HTML (HyperText Markup Language)** — veb-sahifaning tuzilishini (skeletini) tavsiflaydigan belgilash tili. U dasturlash tili emas: hisoblamaydi, faqat brauzerga «bu sarlavha, bu abzats, bu rasm» deb aytadi. Inson tanasi bilan: HTML — suyaklar, CSS — kiyim va ko'rinish, JavaScript — harakat.

### 2.3. Teg va element
Teg — burchakli qavslar ichidagi buyruq: `<p>`. Ko'pchilik teglar juft: ochuvchi `<p>` va yopuvchi `</p>`. Ikkalasi va ichidagi matn birgalikda **element** deyiladi.

```html
<p>Bu abzats.</p>
```

Ba'zi teglar yopilmaydi (bo'sh teglar): `<br>`, `<img>`, `<meta>`, `<link>`.

**Ichma-ich joylashtirish (nesting):** teglar to'g'ri tartibda yopiladi, «matryoshka» kabi: oxirgi ochilgan birinchi yopiladi.

```html
<p>Bu <strong>muhim</strong> gap.</p>   <!-- to'g'ri -->
<p>Bu <strong>muhim gap.</p></strong>   <!-- XATO -->
```

### 2.4. Atribut
Atribut — tegga qo'shimcha ma'lumot beradi. Faqat ochuvchi tegda yoziladi: `nom="qiymat"`.

```html
<html lang="uz">
<p title="Salom!">Kursorni bosib turing</p>
```
Atribut nomlari kichik harfda, qiymat qo'shtirnoq ichida.

### 2.5. Hujjat skeleti
```html
<!DOCTYPE html>
<html lang="uz">
  <head>
    <meta charset="UTF-8">
    <title>Mening sahifam</title>
  </head>
  <body>
    <h1>Salom!</h1>
  </body>
</html>
```
- `<!DOCTYPE html>` — brauzerga: «bu zamonaviy HTML5 hujjat». Teg emas, e'lon.
- `<html lang="uz">` — butun hujjat; `lang` — til (o'zbek).
- `<head>` — sahifa haqidagi xizmat ma'lumotlari. Ekranda ko'rinmaydi (faqat `<title>` brauzer yorlig'ida chiqadi).
- `<body>` — ekranda ko'rinadigan hamma narsa.

Kod yozish odati: ichma-ich teglar 2 ta bo'sh joy (probel) bilan suriladi (indent). Bu kodni o'qishni osonlashtiradi.

### 2.6. `<head>` ichidagi teglar
| Teg | Vazifasi |
|---|---|
| `<title>` | Brauzer yorlig'idagi va qidiruvdagi sarlavha |
| `<meta charset="UTF-8">` | Harflar kodlanishi; o'zbekcha `o'`, `g'`, `sh` harflari va kirill to'g'ri chiqishi uchun |
| `<meta name="viewport" content="width=device-width, initial-scale=1.0">` | Telefonda sahifa to'g'ri masshtabda ko'rinishi uchun |
| `<meta name="description" content="...">` | Sahifaning qisqa tavsifi (qidiruvda ko'rinadi) |
| `<meta name="keywords" content="...">` | Kalit so'zlar (hozir qidiruv tizimlari deyarli e'tibor bermaydi, ammo dasturda bor) |
| `<meta name="author" content="...">` | Muallif |
| `<link>`, `<style>`, `<script>` | CSS va JavaScript ulash. Hozircha faqat nomini bilamiz, CSS va JS bobida o'tiladi |

### 2.7. Sarlavha teglari `<h1>`–`<h6>`
`h1` — eng katta va muhim, `h6` — eng kichik. Qoidalar:
- Sahifada odatda bitta `<h1>` (asosiy sarlavha).
- Tartibni buzmang: `h1` → `h2` → `h3` (h1 dan keyin darrov h4 emas).
- Sarlavhani matnni kattalashtirish uchun emas, **mazmun darajasi** uchun ishlating (kattalikni keyin CSS beradi). Bu qidiruv tizimlari va ekran o'quvchilar uchun muhim.

```html
<h1>Mening shahrim</h1>
<h2>Tarixi</h2>
<h2>Diqqatga sazovor joylar</h2>
<h3>Masjidlar</h3>
```

### 2.8. Abzats `<p>` va qator uzish `<br>`
`<p>` — abzats. Brauzer kodagi bir nechta probel va yangi qatorlarni bitta probelga aylantiradi, shuning uchun yangi qator uchun `<p>` yoki `<br>` kerak.

## 3. Kod namunalari

**Namuna 1 — to'liq skelet (ishlaydi, `index.html` ga saqlanadi):**
```html
<!DOCTYPE html>
<html lang="uz">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Mening birinchi veb-sahifam">
    <meta name="author" content="Ismingiz">
    <title>Mening birinchi sahifam</title>
  </head>
  <body>
    <h1>Salom, men Aziz!</h1>
    <p>Men 8-sinfda o'qiyman va sayt yasashni o'rganyapman.</p>
  </body>
</html>
```

**Namuna 2 — sarlavhalar ierarxiyasi:**
```html
<h1>Sevimli o'yinlarim</h1>
<h2>Kompyuter o'yinlari</h2>
<h3>Minecraft</h3>
<h2>Maydon o'yinlari</h2>
<h3>Futbol</h3>
```

**Namuna 3 — tipik xatolar:**
```html
<!-- 1. Yopilmagan teg -->
<p>Matn

<!-- 2. Noto'g'ri tartibda yopish -->
<p><strong>Matn</p></strong>

<!-- 3. Atribut qiymati qo'shtirnoqsiz -->
<html lang=uz>

<!-- 4. <head> dagi narsa <body> ichida -->
<body><title>Sarlavha</title></body>
```

## 4. Amaliy topshiriqlar

### Oson — Skeletni yozish
`sahifa.html` yarating. Ko'rmasdan (yoki namunaga qarab) `<!DOCTYPE html>`, `html`, `head`, `body`, `title` ni yozing. `<title>` ga ismingizni, `<body>` ga `<h1>` bilan «Salom, ...!» yozing.
**Kutiladigan natija:** brauzer yorlig'ida ism, sahifada katta sarlavha.
**Yechim:** Namuna 1 dan `meta`larsiz variant.

### O'rta — «Men haqimda»
Yuqoridagi faylga qo'shing: `<meta charset>`, `viewport`, `description`, `author`; `<h1>` (ism), uchta `<h2>` («Men haqimda», «Qiziqishlarim», «Maqsadlarim») va har birining ostida kamida 1 ta `<p>`. Qiziqishlar `<h2>` ostida ichki `<h3>` bilan 2 ta qiziqish.
**Kutiladigan natija:** ierarxiyali sahifa; o'zbekcha harflar (`o'`, `g'`) to'g'ri ko'rinadi.
**Yechim namunasi:**
```html
<!DOCTYPE html>
<html lang="uz">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Aziz haqida qisqacha">
    <meta name="author" content="Aziz">
    <title>Men haqimda</title>
  </head>
  <body>
    <h1>Aziz</h1>
    <h2>Men haqimda</h2>
    <p>Men 14 yoshdaman, Toshkentda yashayman.</p>
    <h2>Qiziqishlarim</h2>
    <h3>Futbol</h3>
    <p>Haftada ikki marta o'ynayman.</p>
    <h3>Dasturlash</h3>
    <p>Hozir HTML o'rganyapman.</p>
    <h2>Maqsadlarim</h2>
    <p>Mustaqil sayt yasash.</p>
  </body>
</html>
```

### Qiyin (kuchli o'quvchi uchun) — Xatoni top
Quyidagi kodda kamida 6 ta xato bor. Topib to'g'rilang.
```html
<html lang=uz>
  <body>
    <title>Test</title>
    <h1>Mening saytim
    <p>Birinchi abzats
    <h4>Kichik sarlavha</h4>
    <p><strong>Muhim matn</p></strong>
  </body>
</html>
```
**Yechim:** `<!DOCTYPE html>` yo'q; `lang=uz` qo'shtirnoqsiz; `<head>` yo'q va `<title>` `<body>` ichida; `<meta charset>` yo'q; `<h1>` yopilmagan; `<p>` yopilmagan; `h1` dan keyin `h4` (sarlavha tartibi); `strong`/`p` noto'g'ri tartibda yopilgan.

## 5. Tezkor nazorat
1. Qaysi qism ekranda ko'rinmaydi: `<head>` yoki `<body>`? *(`<head>`; faqat `<title>` yorliqda ko'rinadi.)*
2. `<meta charset="UTF-8">` nima uchun kerak? *(Harflar to'g'ri ko'rinishi uchun.)*
3. Atribut nima? Bitta misol keltiring. *(Tegga qo'shimcha ma'lumot: `lang="uz"`.)*
4. Nega `h1` dan keyin darrov `h4` yozmaymiz? *(Mazmun ierarxiyasi buziladi.)*
5. `<br>` ni nima uchun yopmaymiz? *(Bo'sh teg, ichiga matn olmaydi.)*

## 6. Uyga vazifa
`uyga-vazifa.md` dagi 2-topshiriq.
