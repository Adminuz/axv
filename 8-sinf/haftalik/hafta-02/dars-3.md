# 6-dars. Forma elementlari va validatsiyasi: `<form>`, `<input>`, `<label>`, `<select>`, `<textarea>`

**Hafta:** 2 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliyot · **I-bob**, 6-dars

## 1. Dars rejasi

**Maqsad:** o'quvchi veb-sahifada foydalanuvchidan ma'lumot qabul qiluvchi interaktiv formalar (`<form>`) tuzishni, turli xil `<input>` turlarini to'g'ri tanlashni, `<label>` orqali foydalanish qulayligini (accessibility) ta'minlashni hamda HTML5 validatsiya atributlarini qo'llashni o'rganadi.

**Kutiladigan natija:**
- `<form>` ning `action` va `method` (GET va POST) atributlari vazifasini tushuntira oladi.
- `<label>` va `<input>` o'rtasida `for` va `id` orqali to'g'ri bog'lanish o'rnatadi.
- Asosiy `input` turlarini (`text`, `password`, `email`, `number`, `date`, `checkbox`, `radio`, `file`, `submit`) amalda qo'llay oladi.
- Bir tanlovli `radio` guruhida `name` atributining ahamiyatini biladi.
- Ko'p qatorli matn uchun `<textarea>`, ochiluvchi ro'yxat uchun `<select>` va `<option>` lardan foydalanadi.
- `required`, `placeholder`, `min`, `max`, `disabled` atributlari bilan validatsiya o'rnatadi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 | Takrorlash | 5-dars (jadvallar, `th`, `td`, `colspan`, `rowspan`) |
| 10–30 | Yangi mavzu 1 | Forma nima? `<form>`, `action`, `method` (GET/POST), `<label>` va `<input>` |
| 30–40 | Yangi mavzu 2 | Input turlari (`text`, `password`, `email`, `number`, `checkbox`, `radio`) |
| 40–45 | Tanaffus | |
| 45–55 | Yangi mavzu 3 | `<select>`, `<textarea>`, `<button>`, HTML5 validatsiyasi (`required` va b.) |
| 55–75 | Amaliyot | Ro'yxatdan o'tish (Sign Up) va fikr-mulohaza formasi |
| 75–80 | Tezkor nazorat va xulosa | 5 ta savol, 2-hafta yakuni |

---

## 2. Konspekt

### 2.1. Takrorlash (10 daqiqa)
- Jadvalda ustunlarni birlashtirish uchun nima ishlatiladi? (`colspan`)
- `<thead>` va `<tfoot>` qanday vazifani bajaradi?

### 2.2. Veb-forma nima? `<form>` tegi
Shu kungacha biz faqat axborotni o'quvchiga ko'rsatishni o'rgandik. **Forma** — foydalanuvchiga sayt bilan muloqot qilish, ma'lumot kiritish (login, parol, qidiruv so'zi, sharh) va uni serverga yuborish imkonini beruvchi vositadir.

```html
<form action="server.php" method="POST">
  ... forma elementlari ...
</form>
```

Asosiy atributlar:
1. `action` — ma'lumotlar qaysi server manziliga yoki faylga yuborilishi kerakligini belgilaydi.
2. `method` — ma'lumotlarni yuborish usuli:
   - `GET` — ma'lumotlar brauzer manzil qatorida (URL) ochiq ko'rinadi (masalan: `google.com/search?q=futbol`). Qidiruvlar uchun ishlatiladi. Parol yoki maxfiy ma'lumotlar uchun ASLO ishlatilmaydi!
   - `POST` — ma'lumotlar yashirin tarzda (so'rov tanasida) yuboriladi. Ro'yxatdan o'tish, parollar, to'lovlar uchun doimo POST ishlatiladi.

### 2.3. `<label>` va `<input>` bog'liqligi
Har bir kiritish maydoni o'z nomiga (`<label>`) ega bo'lishi kerak.
Tugma yoki yozuv bosilganda kursorni avtomatik input ichiga o'tkazish uchun `label` dagi `for` atributi `input` dagi `id` bilan bir xil bo'lishi shart!

```html
<label for="ismingiz">Ismingiz:</label>
<input type="text" id="ismingiz" name="user_name" placeholder="Masalan: Ali">
```
`name` atributi — ma'lumot serverga borganda qaysi o'zgaruvchi nomi bilan saqlanishini belgilaydi.

### 2.4. `<input>` turlari (Types)
1. `type="text"` — bir qatorli oddiy matn.
2. `type="password"` — parol maydoni (kiritilgan belgilar yashirin yulduzcha `••••` bo'lib ko'rinadi).
3. `type="email"` — elektron pochta formati (`@` belgisi borligini tekshiradi).
4. `type="number"` — faqat raqamlar (qo'shimcha `min="1" max="100"` berish mumkin).
5. `type="date"` — kalendar orqali sana tanlash.
6. `type="checkbox"` — kvadrat katakcha, bir vaqtning o'zida bir nechta bandni tanlash mumkin.
7. `type="radio"` — dumaloq tugma, berilgan variantlardan **faqat bittasini** tanlash mumkin.
   - *Qoida:* Radio tugmalar bitta guruhga mansub bo'lishi uchun ularning `name` atributi bir xil bo'lishi shart!

```html
<p>Jinsingizni tanlang:</p>
<input type="radio" id="erkak" name="jins" value="erkak">
<label for="erkak">Erkak</label>

<input type="radio" id="ayol" name="jins" value="ayol">
<label for="ayol">Ayol</label>
```

8. `type="file"` — kompyuterdan rasm yoki hujjat yuklash.
9. `type="submit"` — formani serverga yuboruvchi tugma.
10. `type="reset"` — formadagi barcha kiritilgan yozuvlarni tozalab tashlovchi tugma.

### 2.5. Boshqa forma elementlari: `<textarea>`, `<select>` va `<button>`
- `<textarea>` — ko'p qatorli matn kiritish maydoni (fikr-mulohaza, xat, xabar uchun). `rows="4" cols="50"` orqali o'lchami beriladi.
- `<select>` va `<option>` — ochiluvchi ro'yxat (dropdown menu):
```html
<label for="shahar">Shahringiz:</label>
<select id="shahar" name="shahar">
  <option value="toshkent">Toshkent</option>
  <option value="samarqand">Samarqand</option>
  <option value="buxoro">Buxoro</option>
</select>
```
- `<button type="submit">` — yuborish tugmasi. `<input type="submit">` dan farqli ravishda ichiga rasm, ikonka yoki alohida matn qo'yish mumkin.

### 2.6. HTML5 validatsiya atributlari
Brauzer foydalanuvchi ma'lumotni to'g'ri kiritganligini o'zi tekshirishi uchun atributlar:
- `required` — maydonni to'ldirish majburiy (bo'sh qoldirib yuborib bo'lmaydi).
- `placeholder` — kiritish maydonidagi shaffof yo'riqnoma matni.
- `value` — maydonning boshlang'ich qiymati.
- `readonly` — faqat o'qish uchun (o'zgartirib bo'lmaydi).
- `disabled` — butunlay nofaol (och kulrang bo'lib, serverga yuborilmaydi).
- `min`, `max` — raqam yoki sana uchun eng kichik va eng katta chegara.

---

## 3. Amaliy topshiriqlar

### 1-topshiriq. Tizimga kirish (Login) formasi
Oddiy login formasi tuzing: Login (email yoki text), Parol (`password`) va "Kirish" tugmasi. Har ikkala maydon ham to'ldirilishi shart (`required`) bo'lsin.

**Yechim:**
```html
<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <title>Tizimga kirish</title>
</head>
<body>
  <h1>Tizimga kirish</h1>
  <form action="/login" method="POST">
    <div>
      <label for="login">Login yoki Email:</label><br>
      <input type="text" id="login" name="username" placeholder="Loginni kiriting" required>
    </div>
    <br>
    <div>
      <label for="parol">Parol:</label><br>
      <input type="password" id="parol" name="userpass" placeholder="Kamida 8 belgi" required>
    </div>
    <br>
    <button type="submit">Kirish</button>
  </form>
</body>
</html>
```

### 2-topshiriq. To'liq ro'yxatdan o'tish (Sign Up) formasi
F.I.SH (`text`), Parol (`password`), Tug'ilgan sana (`date`), Telefon raqam (`tel`), Viloyat (`select`), Jins (`radio`) va "Qoidalarga roziman" (`checkbox`) maydonlaridan iborat forma tuzing.

**Yechim:**
```html
<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <title>Ro'yxatdan o'tish</title>
</head>
<body>
  <h1>O'quvchi ro'yxatdan o'tishi</h1>
  <form action="/register" method="POST">
    <p>
      <label for="ism">To'liq ismingiz:</label><br>
      <input type="text" id="ism" name="fullname" placeholder="Ali Valiyev" required>
    </p>

    <p>
      <label for="parol">Yangi parol:</label><br>
      <input type="password" id="parol" name="password" required>
    </p>

    <p>
      <label for="sana">Tug'ilgan sanangiz:</label><br>
      <input type="date" id="sana" name="birthdate">
    </p>

    <p>
      Jinsingiz:<br>
      <input type="radio" id="erkak" name="gender" value="erkak" checked>
      <label for="erkak">Erkak</label>
      <input type="radio" id="ayol" name="gender" value="ayol">
      <label for="ayol">Ayol</label>
    </p>

    <p>
      <label for="viloyat">Yashash hududingiz:</label><br>
      <select id="viloyat" name="region">
        <option value="toshkent">Toshkent shahri</option>
        <option value="samarqand">Samarqand viloyati</option>
        <option value="fargona">Farg'ona viloyati</option>
        <option value="buxoro">Buxoro viloyati</option>
      </select>
    </p>

    <p>
      <input type="checkbox" id="shartlar" name="terms" required>
      <label for="shartlar">Saytdan foydalanish qoidalariga roziman</label>
    </p>

    <button type="submit">Ro'yxatdan o'tish</button>
    <button type="reset">Tozalash</button>
  </form>
</body>
</html>
```

### 3-topshiriq. Fikr-mulohaza va xabar yuborish formasi (`<textarea>`)
Mavzu (`text`), Baholash (1 dan 5 gacha `number`) va Fikr matni (`<textarea>`) maydonlaridan iborat xabar shaklini tuzing.

**Yechim:**
```html
<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <title>Fikr bildirish</title>
</head>
<body>
  <h1>Bizga fikringizni yozib qoldiring</h1>
  <form action="/feedback" method="POST">
    <p>
      <label for="mavzu">Xabar mavzusi:</label><br>
      <input type="text" id="mavzu" name="subject" placeholder="Sayt haqida..." required>
    </p>

    <p>
      <label for="baho">Darsni baholang (1-5):</label><br>
      <input type="number" id="baho" name="rating" min="1" max="5" value="5">
    </p>

    <p>
      <label for="xabar">Xabaringiz:</label><br>
      <textarea id="xabar" name="message" rows="5" cols="40" placeholder="Fikringiz biz uchun muhim..."></textarea>
    </p>

    <button type="submit">Yuborish</button>
  </form>
</body>
</html>
```

---

## 4. Tezkor nazorat (5 daqiqa)

1. Formaning `method` atributidagi `GET` va `POST` ning asosiy farqi nima?
   - **Javob:** `GET` ma'lumotlarni URL manzilida ochiq ko'rsatadi, `POST` esa xavfsiz holda so'rov tanasida yashirin yuboradi.
2. `<label>` tegidagi `for` atributi qaysi atribut bilan bir xil bo'lishi kerak?
   - **Javob:** Tegishli `<input>` ning `id` atributi bilan.
3. Foydalanuvchiga faqat bitta variantni tanlash imkonini beruvchi tugma turi qaysi va uning qoidasi nima?
   - **Javob:** `type="radio"`; variantlar bitta guruh bo'lishi uchun ularning `name` atributi bir xil bo'lishi shart.
4. Ko'p qatorli matn kiritish uchun qaysi teg ishlatiladi?
   - **Javob:** `<textarea>`.
5. Maydonni to'ldirishni majburiy qilish uchun qaysi HTML5 atributi yoziladi?
   - **Javob:** `required`.

---

## 5. Xulosa va keyingi darsga ko'prik
2-hafta davomida biz rasmlar, ro'yxatlar, jadvallar va formalarni to'liq o'rganib chiqdik. Endi siz haqiqiy interaktiv veb-sahifa yarata olasiz!
**Keyingi hafta (3-hafta):** Zamonaviy HTML5 standartlari — `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<footer>` semantik teglari, audio va video qo'yish bilan tanishamiz!
