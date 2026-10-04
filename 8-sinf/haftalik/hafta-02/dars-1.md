# 4-dars. Rasm va ro'yxat teglari: `<img>`, `<figure>`, `<ul>`, `<ol>`, `<dl>`

**Hafta:** 2 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliyot · **I-bob**, 4-dars

## 1. Dars rejasi

**Maqsad:** o'quvchi HTML sahifaga to'g'ri yo'l (nisbiy va mutlaq) bilan rasm qo'yishni, rasmlarni `<figure>` bilan semantik izohlashni hamda tartibli, tartibsiz va ta'rif ro'yxatlarini (shu jumladan ichma-ich) yaratishni o'rganadi.

**Kutiladigan natija:**
- `<img>` tegining asosiy atributlarini (`src`, `alt`, `width`, `height`, `title`) biladi va to'g'ri qo'llaydi.
- Nisbiy (`images/foto.jpg`, `../foto.jpg`) va mutlaq (`https://...`) yo'llar farqini tushunadi.
- Rasmlarni semantik jihatdan `<figure>` va `<figcaption>` bilan o'rashni biladi.
- `<ul>`, `<ol>`, `<li>`, `<dl>`, `<dt>`, `<dd>` teglaridan foydalanib turli xil ro'yxatlar tuza oladi.
- Ichma-ich (nested) ro'yxatlarni to'g'ri tuzilma bilan yoza oladi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 | Takrorlash | 1-hafta darslari (matn teglari, havolalar, block/inline) va uyga vazifa |
| 10–30 | Yangi mavzu 1 | `<img>` tegi, nisbiy/mutlaq yo'llar, `alt` ning ahamiyati, `<figure>` |
| 30–40 | Yangi mavzu 2 | Ro'yxat turlari: `<ul>`, `<ol>` (type, start, reversed) |
| 40–45 | Tanaffus | |
| 45–55 | Yangi mavzu 3 | Ta'rif ro'yxati (`<dl>`) va ichma-ich ro'yxatlar |
| 55–75 | Amaliyot | Retsept sahifasi va profil kartasi |
| 75–80 | Tezkor nazorat va xulosa | 5 ta savol, dars xulosasi |

---

## 2. Konspekt

### 2.1. Takrorlash (10 daqiqa)
O'tgan haftadagi bilimlarni qisqa eslang:
- Qaysi teglar inline, qaysilari block element? (`<a>`, `<span>`, `<strong>` inline; `<p>`, `<h1>`-`<h6>`, `<div>` block).
- `<a>` tegining `href` atributiga qanday qiymatlar beriladi?

### 2.2. Sahifaga rasm qo'yish: `<img>` tegi
`<img>` — **yopilmaydigan (void / self-closing)** va **inline** elementdir. Rasm matn kabi qatorda joylashadi, lekin kenglik va balandlikka ega bo'ladi (inline-block xususiyati).

```html
<img src="images/tabiat.jpg" alt="Tog'lar va ko'l manzarasi" width="600" height="400">
```

Asosiy atributlar:
1. `src` (source) — rasm faylining manzili. Bu atribut majburiy.
2. `alt` (alternative text) — rasm yuklanmay qolganda yoki ko'zi ojiz insonlar (screen reader) uchun matnli tavsif. SEO uchun juda muhim! `alt` ni hech qachon bo'sh qoldirmang.
3. `width` va `height` — rasmning piksellardagi o'lchami (birliksiz yoziladi). Ular sahifa yuklanayotganda sakrash (layout shift) bo'lmasligi uchun xizmat qiladi.
4. `title` — kursor rasm ustiga borganda chiquvchi kichik maslahat oynasi (tooltip).

### 2.3. Rasm yo'llari: nisbiy va mutlaq (Path)
O'quvchilar eng ko'p adashadigan joy — fayl manzillari:
- **Mutlaq yo'l (Absolute path):** to'liq internet manzili. Masalan: `https://example.com/logo.png`.
- **Nisbiy yo'l (Relative path):** joriy HTML fayl turgan joyga nisbatan yo'l:
  - `foto.jpg` — HTML fayl bilan bitta papkada.
  - `images/foto.jpg` — joriy papka ichidagi `images` papkasida.
  - `../foto.jpg` — bir pog'ona yuqoridagi papkada.
  - `../../images/foto.jpg` — ikki pog'ona yuqoriga chiqib, `images` papkasiga kirish.

### 2.4. Semantik rasm: `<figure>` va `<figcaption>`
Maqola yoki o'quv qo'llanmalarda rasm tagida izoh bo'ladi. HTML5 da buning uchun maxsus semantik teglar mavjud:
```html
<figure>
  <img src="images/samarqand.jpg" alt="Registon maydoni" width="600">
  <figcaption>1-rasm. Samarqand shahridagi Registon maydoni</figcaption>
</figure>
```
`<figure>` — block element bo'lib, rasmni va uning izohini bitta mustaqil blok sifatida birlashtiradi.

### 2.5. Ro'yxatlar (Lists)
HTMLda ro'yxatlar 3 turga bo'linadi:

#### A) Tartibsiz ro'yxat (`<ul>` — Unordered List)
Tartib ahamiyatsiz bo'lgan ro'yxatlar (do'kondan olinadigan narsalar, xususiyatlar, navigatsiya menyusi). Har bir band `<li>` (List Item) bilan beriladi:
```html
<ul>
  <li>Olma</li>
  <li>Banan</li>
  <li>Apelsin</li>
</ul>
```

#### B) Tartiblangan ro'yxat (`<ol>` — Ordered List)
Tartib qat'iy muhim bo'lgan ro'yxatlar (taom tayyorlash bosqichlari, g'oliblar ro'yxati, algoritm qadamlari).
```html
<ol>
  <li>Tuxumni chaqing</li>
  <li>Tuz solib aralashtiring</li>
  <li>Tovada 5 daqiqa qovuring</li>
</ol>
```
`<ol>` ning foydali atributlari:
- `start="5"` — raqamlash 5 dan boshlanadi.
- `reversed` — raqamlar teskari sanaladi (3, 2, 1).
- `type="A"` (yoki `a`, `I`, `i`, `1`) — raqamlar turini o'zgartiradi (katta harf, rim raqami va h.k.).

#### D) Ta'riflar ro'yxati (`<dl>` — Description List)
Atamalar va ularning izohi, lug'at yoki savol-javoblar uchun ishlatiladi:
- `<dl>` — ro'yxat konteyneri
- `<dt>` — atama (description term)
- `<dd>` — ta'rif / izoh (description details)
```html
<dl>
  <dt>HTML</dt>
  <dd>Veb-sahifaning asosiy skeletini yaratuvchi gipermatnli belgilash tili.</dd>
  <dt>CSS</dt>
  <dd>Sahifaning tashqi ko'rinishi va dizaynini bezovchi uslublar jadvali.</dd>
</dl>
```

### 2.6. Ichma-ich ro'yxatlar (Nested Lists)
Ro'yxat ichida yana boshqa ro'yxat bo'lishi mumkin. Qoida: ichki ro'yxat doimo ota ro'yxatning `<li>` tegi ICHIDA ochilishi va yopilishi shart!
```html
<ul>
  <li>Meva
    <ul>
      <li>Olma</li>
      <li>Uzum</li>
    </ul>
  </li>
  <li>Sabzavot
    <ul>
      <li>Sabzi</li>
      <li>Piyoz</li>
    </ul>
  </li>
</ul>
```

---

## 3. Amaliy topshiriqlar

### 1-topshiriq. Mening sevimli taomim retsepti
O'quvchi `retsept.html` faylini yaratadi. Sahifada:
1. Taom nomi (`<h1>`) va uning rasmi (`<img>`, `<figure>`, `<figcaption>`).
2. Masalliqlar ro'yxati (`<ul>`).
3. Tayyorlash bosqichlari (`<ol>`).

**Yechim:**
```html
<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <title>Osh retsepti</title>
</head>
<body>
  <h1>O'zbekcha Palov (Osh)</h1>
  
  <figure>
    <img src="osh.jpg" alt="Issiq tovoqda tortilgan palov" width="500">
    <figcaption>1-rasm. An'anaviy bayramona to'y oshi</figcaption>
  </figure>

  <h2>Zarur masalliqlar:</h2>
  <ul>
    <li>Guruch — 1 kg</li>
    <li>Qo'y go'shti — 1 kg</li>
    <li>Sariq sabzi — 1 kg</li>
    <li>Piyoz — 2-3 dona</li>
    <li>O'simlik yog'i — 300 ml</li>
    <li>Zira, tuz, murch — ta'bga ko'ra</li>
  </ul>

  <h2>Tayyorlash bosqichlari:</h2>
  <ol>
    <li>Qozonda yog'ni qizdirib, go'shtni qizarguncha qovuring.</li>
    <li>Piyozni solib tillarang bo'lguncha qovuring, keyin sabzini qo'shing.</li>
    <li>Suv quyib, zirvakni 40 daqiqa past olovda qaynating.</li>
    <li>Yuvilgan guruchni tekis solib, suvini tortguncha kuting.</li>
    <li>Guruchni gumbaz qilib, 20-25 daqiqaga damlang.</li>
  </ol>
</body>
</html>
```

### 2-topshiriq. Dasturlash tillari lug'ati (`<dl>`)
Kamida 4 ta atamadan iborat ta'riflar ro'yxatini yarating.

**Yechim:**
```html
<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <title>IT Atamalar</title>
</head>
<body>
  <h1>Veb-dasturlash lug'ati</h1>
  <dl>
    <dt>Frontend</dt>
    <dd>Foydalanuvchi brauzerda ko'radigan barcha tugma, matn va dizayn qismi.</dd>
    
    <dt>Backend</dt>
    <dd>Serverda ishlaydigan, ma'lumotlar bazasi va biznes-mantiqni boshqaradigan qism.</dd>
    
    <dt>URL</dt>
    <dd>Internetdagi har qanday sahifa yoki faylning aniq manzili.</dd>
    
    <dt>DNS</dt>
    <dd>Domen nomlarini raqamli IP manzillarga aylantirib beruvchi tizim.</dd>
  </dl>
</body>
</html>
```

### 3-topshiriq. Ichma-ich sayt mundarijasi
Kitob yoki kurs mundarijasini ichma-ich ro'yxat (`<ol>` ichida `<ol>`) ko'rinishida tuzing.

**Yechim:**
```html
<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <title>Kurs mundarijasi</title>
</head>
<body>
  <h1>Veb Full-stack kursi mundarijasi</h1>
  <ol>
    <li>HTML asoslari
      <ol type="a">
        <li>Teglar va atributlar</li>
        <li>Matn va havolalar</li>
        <li>Rasm va ro'yxatlar</li>
      </ol>
    </li>
    <li>CSS asoslari
      <ol type="a">
        <li>Selektorlar va ranglar</li>
        <li>Box model</li>
        <li>Flexbox va Grid</li>
      </ol>
    </li>
  </ol>
</body>
</html>
```

---

## 4. Tezkor nazorat (5 daqiqa)

1. `<img>` tegida nima uchun yopilish tegi (`</img>`) yo'q?
   - **Javob:** `<img>` void element bo'lib, uning ichiga matn yoki boshqa teg yozilmaydi, barcha parametrlar atributlarda beriladi.
2. `alt` atributi nima uchun majburiy hisoblanadi?
   - **Javob:** Rasm ochilmay qolsa o'rnida matn chiqishi, qidiruv tizimlari (SEO) tushunishi va screen reader foydalanuvchilariga eshittirilishi uchun.
3. `<ol>` va `<ul>` teglarining asosiy farqi nimada?
   - **Javob:** `<ol>` tartiblangan (raqamli), `<ul>` esa tartibsiz (markerli) ro'yxat.
4. Ichma-ich ro'yxat yozganda ichki `<ul>` qaysi teg ichiga qo'yilishi shart?
   - **Javob:** Ota ro'yxatning `<li>` tegi ichiga.
5. `<figure>` va `<figcaption>` nima vazifani bajaradi?
   - **Javob:** Rasmni va uning ostidagi izohni bitta semantik blok qilib birlashtiradi.

---

## 5. Xulosa va keyingi darsga ko'prik
Bugun biz veb-sahifaga jon bag'ishlaydigan rasmlar va ma'lumotlarni tartibga soluvchi ro'yxatlar bilan ishladik.
**Keyingi dars (5-dars):** HTMLda ma'lumotlarni qator va ustunlarga ajratib ko'rsatish — `<table>`, `<tr>`, `<td>`, `<th>` jadvallarini o'rganamiz!
