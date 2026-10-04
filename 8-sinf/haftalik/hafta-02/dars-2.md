# 5-dars. Jadval teglari: `<table>`, `<tr>`, `<td>`, `<th>`, `colspan` va `rowspan`

**Hafta:** 2 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliyot · **I-bob**, 5-dars

## 1. Dars rejasi

**Maqsad:** o'quvchi HTMLda ma'lumotlarni qator va ustunlar ko'rinishida to'g'ri semantik jadvallarga joylashtirishni, `<thead>`, `<tbody>`, `<tfoot>` bo'limlarini qo'llashni hamda `colspan` va `rowspan` yordamida katakchalarni birlashtirishni o'rganadi.

**Kutiladigan natija:**
- `<table>`, `<tr>`, `<td>`, `<th>` vazifalarini biladi va dars jadvalini yarata oladi.
- `<th>` va `<td>` farqini tushunadi (`<th>` markazlashgan va qalin bo'ladi).
- Jadvalni semantik bo'limlarga (`<thead>`, `<tbody>`, `<tfoot>`, `<caption>`) ajratadi.
- `colspan` va `rowspan` atributlari orqali katakchalarni gorizontal va vertikal birlashtira oladi.
- Jadval tuzishda katakchalar soni hisobini to'g'ri olib boradi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 | Takrorlash | 4-dars mavzulari (rasmlar, `alt`, ro'yxat turlari, nested list) |
| 10–30 | Yangi mavzu 1 | Jadval nima? `<table>`, `<tr>`, `<td>`, `<th>`, `<caption>` |
| 30–40 | Yangi mavzu 2 | Semantik bloklar: `<thead>`, `<tbody>`, `<tfoot>` |
| 40–45 | Tanaffus | |
| 45–55 | Yangi mavzu 3 | Katakchalarni birlashtirish: `colspan` va `rowspan` |
| 55–75 | Amaliyot | Dars jadvali va do'kon hisob-kitobi |
| 75–80 | Tezkor nazorat va xulosa | 5 ta savol, dars xulosasi |

---

## 2. Konspekt

### 2.1. Takrorlash (10 daqiqa)
- Rasm yuklanmay qolsa nima yordamga keladi? (`alt`)
- Ichma-ich ro'yxat tuzganda asosiy qoida nima? (ichki ro'yxat `<li>` ichiga kiradi).

### 2.2. Jadval asoslari: `<table>`, `<tr>`, `<td>`, `<th>`
Veb-dasturlashda jadval — bu ma'lumotlarni satrlar (qatorlar) va ustunlar kesishmasida tartibli ko'rsatish vositasidir.
HTMLda jadval **qatorlar bo'yicha** yoziladi:

1. `<table>` — jadval konteyneri.
2. `<tr>` (table row) — jadvalning har bir gorizontal qatori.
3. `<td>` (table data) — qator ichidagi oddiy ma'lumot katakchasi.
4. `<th>` (table header) — jadval sarlavhasi katakchasi (avtomatik qalin va o'rtaga tekislangan bo'ladi).
5. `<caption>` — jadvalning sarlavhasi / nomi (`<table>` ning eng birinchi bolasi bo'lishi kerak).

```html
<table border="1">
  <caption>Haftalik ob-havo</caption>
  <tr>
    <th>Kun</th>
    <th>Harorat</th>
  </tr>
  <tr>
    <td>Dushanba</td>
    <td>+22°C</td>
  </tr>
  <tr>
    <td>Seshanba</td>
    <td>+25°C</td>
  </tr>
</table>
```

*(Eslatma: `border="1"` atributi katakchalarga ramka berish uchun vaqtincha ishlatiladi. Keyingi haftalarda ramkalarni to'liq CSS bilan bezaymiz).*

### 2.3. Semantik jadval qismlari: `<thead>`, `<tbody>`, `<tfoot>`
Katta va professional jadvallarni 3 ta asosiy bo'limga bo'lish qabul qilingan:
- `<thead>` (Table Head) — sarlavhalar qatori turadigan yuqori qism.
- `<tbody>` (Table Body) — jadvalning asosiy ma'lumotlar qatorlari.
- `<tfoot>` (Table Foot) — jadvalning yakuniy, xulosa yoki jami hisob qatori (masalan: "Jami: 150 000 so'm").

Bu bo'limlar jadvalni o'qishni osonlashtiradi, sahifa chop etilganda (print) har bir varaqda `<thead>` ni avtomatik takrorlaydi.

### 2.4. Katakchalarni birlashtirish: `colspan` va `rowspan`
Haqiqiy hayotda ba'zi katakchalar bir nechta ustun yoki qatorni egallashi kerak bo'ladi (masalan, tushlik tanaffusi yoki jami hisob).

#### A) `colspan` (Column Span — ustunlarni birlashtirish)
Katakchani gorizontaliga bir nechta ustunga cho'zadi:
```html
<tr>
  <td colspan="2">Bu katakcha 2 ta ustun o'rnini egallaydi</td>
</tr>
```

#### B) `rowspan` (Row Span — qatorlarni birlashtirish)
Katakchani vertikaliga bir nechta qatorga cho'zadi:
```html
<tr>
  <td rowspan="2">Dushanba</td>
  <td>Matematika</td>
</tr>
<tr>
  <!-- Bu yerda birinchi katakcha yozilmaydi, chunki yuqoridagi rowspan uni egallagan! -->
  <td>Fizika</td>
</tr>
```

**Muhim hisob-kitob qoidasi:**
Agar biror qatorda `colspan="2"` ishlatilsa, shu qatordagi jami `<td>` lar soni bittaga kamayadi. Agar `rowspan="2"` ishlatilsa, keyingi qatordagi `<td>` lar soni bittaga kam bo'lishi shart!

---

## 3. Amaliy topshiriqlar

### 1-topshiriq. Maktab dars jadvali
Dushanbadan jumagacha bo'lgan dars jadvalini tuzing. Sarlavhada: Kuni, 1-dars, 2-dars, 3-dars.

**Yechim:**
```html
<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <title>Dars jadvali</title>
</head>
<body>
  <h1>8-A sinf dars jadvali</h1>
  <table border="1">
    <caption>Haftalik dars taqvimi</caption>
    <thead>
      <tr>
        <th>Kun</th>
        <th>1-dars</th>
        <th>2-dars</th>
        <th>3-dars</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Dushanba</td>
        <td>Ona tili</td>
        <td>Matematika</td>
        <td>Informatika</td>
      </tr>
      <tr>
        <td>Seshanba</td>
        <td>Ingliz tili</td>
        <td>Tarix</td>
        <td>Adabiyot</td>
      </tr>
      <tr>
        <td>Chorshanba</td>
        <td>Fizika</td>
        <td>Geometriya</td>
        <td>Biologiya</td>
      </tr>
    </tbody>
  </table>
</body>
</html>
```

### 2-topshiriq. Xarid cheki (`tfoot` va `colspan`)
Xarid qilingan mahsulotlar ro'yxati, miqdori, narxi va eng pastki qatorda `colspan` bilan "Jami to'lov" qatorini tuzing.

**Yechim:**
```html
<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <title>Xarid cheki</title>
</head>
<body>
  <h1>Do'kon xarid cheki</h1>
  <table border="1">
    <thead>
      <tr>
        <th>Mahsulot</th>
        <th>Miqdori</th>
        <th>Narxi</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Non</td>
        <td>2 dona</td>
        <td>6 000 so'm</td>
      </tr>
      <tr>
        <td>Sut</td>
        <td>1 litr</td>
        <td>11 000 so'm</td>
      </tr>
      <tr>
        <td>Shakar</td>
        <td>1 kg</td>
        <td>14 000 so'm</td>
      </tr>
    </tbody>
    <tfoot>
      <tr>
        <th colspan="2">Jami to'lov:</th>
        <th>31 000 so'm</th>
      </tr>
    </tfoot>
  </table>
</body>
</html>
```

### 3-topshiriq. Tanaffusli dars jadvali (`rowspan` va `colspan`)
2 kunlik jadval tuzing. Unda 2-darsdan keyin "Katta tanaffus" katakchasi butun jadval bo'ylab (`colspan="3"`) cho'zilsin.

**Yechim:**
```html
<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <title>Katta tanaffusli jadval</title>
</head>
<body>
  <table border="1">
    <thead>
      <tr>
        <th>Kun</th>
        <th>Vaqt</th>
        <th>Fan</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td rowspan="4">Dushanba</td>
        <td>08:30 - 09:15</td>
        <td>Algebra</td>
      </tr>
      <tr>
        <td>09:25 - 10:10</td>
        <td>Fizika</td>
      </tr>
      <tr>
        <td colspan="2" align="center"><strong>Katta tanaffus (20 daqiqa)</strong></td>
      </tr>
      <tr>
        <td>10:30 - 11:15</td>
        <td>Informatika</td>
      </tr>
    </tbody>
  </table>
</body>
</html>
```

---

## 4. Tezkor nazorat (5 daqiqa)

1. `<tr>`, `<td>`, `<th>` qisqartmalari nimani anglatadi?
   - **Javob:** `<tr>` — table row, `<td>` — table data, `<th>` — table header.
2. `<th>` tegidagi matn brauzerda qanday ko'rinadi?
   - **Javob:** Qalin shriftda va katakcha o'rtasiga tekislangan holda.
3. Katakchani 3 ta ustunga birlashtirish uchun qaysi atribut yoziladi?
   - **Javob:** `colspan="3"`.
4. Katakchani 2 ta qatorga birlashtirish uchun-chi?
   - **Javob:** `rowspan="2"`.
5. `<thead>`, `<tbody>` va `<tfoot>` nima uchun kerak?
   - **Javob:** Jadvalning bosh, asosiy va xulosa qismlarini semantik ajratish uchun.

---

## 5. Xulosa va keyingi darsga ko'prik
Bugun biz ma'lumotlarni jadvallar ko'rinishida tuzishni o'rgandik.
**Keyingi dars (6-dars):** Foydalanuvchilar bilan muloqot qilish — ro'yxatdan o'tish formasi, login, parollar, checkbox va tugmalar (`<form>`, `<input>`, `<button>`) bilan ishlaymiz!
