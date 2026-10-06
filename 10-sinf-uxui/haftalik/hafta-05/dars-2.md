# 14-dars. Formalar, validatsiya va interfeys elementlari semantikasi

**Fan:** Advanced UX/UI dizayn va Advanced Front-end
**Sinf:** 10-sinf
**Hafta:** 5-hafta, 2-dars (umumiy 14-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** `_matn/oquv-qollanma.txt`, V bob, 5.1 (`button`, `a`, `nav` semantikasi va anti-patternlar). `form`, `label`, `input` turlari va validatsiya atributlari rejadagi mavzu bo'yicha standart HTML5 bilimidan qo'shildi.

---

## Darsning maqsadi

O'quvchi `form`, `label`, `input` turlari va `fieldset` bilan qabul formasini yozadi, `required`, `minlength`, `pattern` bilan validatsiya qo'shadi, xato xabarini `aria-describedby` orqali bog'laydi va `a` bilan `button` farqini biladi.

## Kutiladigan natija

- `label` va `for`/`id` orqali maydonlarni bog'laydi;
- To'g'ri `type` (email, tel, date, number) tanlaydi;
- `required`, `minlength`, `pattern` bilan validatsiya yozadi;
- Tushunarli xato xabari beradi va `button type` ni to'g'ri qo'yadi.

## Kerakli jihozlar

- Har bir o'quvchi uchun kompyuter, brauzer va matn muharriri
- Brauzer DevTools (formani tekshirish uchun)
- Proyektor/monitor; zaxira: A4 qog'oz (forma eskizi uchun)

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 00–08 | Takrorlash | 13-dars: semantik teglar, landmark, ARIA |
| 08–22 | Yangi mavzu 1 | Forma tuzilmasi: `form`, `label`, `input`, `fieldset` |
| 22–32 | Yangi mavzu 2 | Input turlari va validatsiya atributlari |
| 32–38 | Tanaffus + mini-quiz | Slayddagi `.quiz` |
| 38–50 | Yangi mavzu 3 | Xato xabarlari va `button`/`a` semantikasi |
| 50–75 | Amaliyot | Maktab qabul formasini yozish |
| 75–80 | Xulosa | Tezkor nazorat, uyga vazifa |

---

## Konspekt (mentor aytadigan matn)

### 1. `form`, `label` va `fieldset`

Forma — foydalanuvchidan ma'lumot olish vositasi. `form` butun blokni o'raydi, har bir maydon uchun `label` yoziladi va `for` qiymati `input` ning `id` siga teng bo'ladi: shunda matn bosilsa, maydon faollashadi va ekran o'qiydigan qurilma maydon nomini aytadi. Bog'liq maydonlar `fieldset` ichida guruhlanadi, `legend` esa guruh nomi. Faqat `placeholder` ga tayanmang: u yozishni boshlaganda yo'qoladi va `label` o'rnini bosmaydi.

`for` va `id` bir xil bo'lishi shart. `name` esa serverga yuboriladigan maydon nomi.

### 2. Input turlari va validatsiya atributlari

To'g'ri `type` brauzerga yordam beradi: `email`, `tel`, `number`, `date`, `password` uchun mobil klaviatura va tekshiruv mos keladi. Validatsiya atributlari: `required` (majburiy), `minlength` va `maxlength` (uzunlik), `min` va `max` (son), `pattern` (muntazam ifoda). Brauzer formani yuborishdan oldin o'zi tekshiradi. `autocomplete` (masalan `email`, `tel`) to'ldirishni tezlashtiradi. Muhim: brauzer tekshiruvi qulaylik uchun, serverda ham tekshirish shart.

`pattern="\+998[0-9]{9}"` +998 va 9 raqamni talab qiladi. Foydalanuvchiga `title` yoki matn bilan formatni ko'rsating.

### 3. Xato xabarlari, `button` va `a`

Yaxshi xato xabari nima noto'g'ri va qanday tuzatishni aytadi: «Noto'g'ri» emas, «Telefon +998 bilan boshlanib, 9 raqam bo'lsin». Xabarni maydonga `aria-describedby` bilan bog'lang, shunda ekran o'qiydigan qurilma uni o'qiydi. Rangning o'zi yetarli emas: matn yoki belgi ham qo'shing. Tugmada `type` ni yozing: `submit` yuboradi, `button` hech narsa yubormaydi. `a` — boshqa sahifaga o'tish uchun, `button` — amal bajarish uchun.

`aria-describedby` qiymati xabar elementining `id` si. `button` ichidagi `type="button"` formani yubormaydi.

---

## Kod namunasi

Qabul formasi:

```html
<form action="/qabul" method="post">
  <fieldset>
    <legend>Qabul arizasi</legend>
    <label for="ism">Ism</label>
    <input type="text" id="ism" name="ism" required minlength="2">

    <label for="email">Email</label>
    <input type="email" id="email" name="email" required autocomplete="email">

    <label for="tel">Telefon</label>
    <input type="tel" id="tel" name="tel" pattern="\+998[0-9]{9}"
           aria-describedby="tel-xato" required>
    <p id="tel-xato">Telefon +998 bilan boshlanib, 9 raqam bo'lsin.</p>

    <label for="sinf">Sinf</label>
    <input type="number" id="sinf" name="sinf" min="1" max="11" required>

    <label><input type="checkbox" name="rozilik" required> Shartlarga roziman</label>
  </fieldset>
  <button type="submit">Yuborish</button>
</form>
```

Tanlov (radio):

```html
<fieldset>
  <legend>Til</legend>
  <label><input type="radio" name="til" value="uz" checked> O'zbekcha</label>
  <label><input type="radio" name="til" value="ru"> Ruscha</label>
</fieldset>
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Label bog'lang
`<input type="text" id="ism">` ga `label` qo'shing, matn bosilganda maydon faollashsin.

**Kutiladigan natija:** `label` bosilganda maydon faollashadi.

**Yechim:** `<label for="ism">Ism</label>` va `id="ism"`.

### 2-topshiriq (o'rta). To'g'ri type
Email, telefon, sinf (1–11) va tug'ilgan sana maydonlarini mos `type` va atributlar bilan yozing.

**Kutiladigan natija:** To'rt maydon, har birida `label`.

**Yechim:** `type="email"`, `tel`, `number min="1" max="11"`, `date`.

### 3-topshiriq (qiyin). Qabul formasi
Maktab qabul formasini yozing: fieldset ichida ism, email, telefon (pattern), sinf, rozilik (checkbox), `submit` tugmasi, xato xabarlari.

**Kutiladigan natija:** Bo'sh yuborilsa brauzer to'xtatadi; noto'g'ri telefonda xabar chiqadi.

**Yechim:** Namunaviy kodga qarang: `label`, `required`, `pattern`, `aria-describedby`, `button type="submit"`.

### 4-topshiriq (qo'shimcha). Server tekshiruvi
Nima uchun faqat brauzer validatsiyasi yetarli emas? 2 jumlada yozing.

**Kutiladigan natija:** Brauzer tekshiruvini chetlab o'tish mumkin.

**Yechim:** DevTools yoki so'rovni qo'lda yuborib, tekshiruvni chetlab o'tish mumkin; shuning uchun server ham tekshiradi.

---

## Tezkor nazorat (dars oxirida)

1. `label` nima uchun kerak? — Maydon nomini beradi va `for`/`id` orqali bog'lanadi.
2. `required` nima qiladi? — Maydonni majburiy qiladi.
3. `fieldset` va `legend`? — Bog'liq maydonlarni guruhlaydi va guruhga nom beradi.
4. Qaysi teg boshqa sahifaga o'tkazadi? — `a`.
5. Server tekshiruvi nega kerak? — Brauzer tekshiruvini chetlab o'tish mumkin.

## Keng tarqalgan xatolar

- `label` yozmasdan faqat `placeholder` ishlatish.
- `for` va `id` ni har xil yozish.
- Hamma maydonga `type="text"` yozish.
- Xato xabarini faqat qizil rang bilan berish.
- `button` ga `type` yozmaslik (forma kutilmaganda yuboriladi).
- Havola uchun `button`, amal uchun `a` ishlatish.

## Bilasizmi? (Internetdan, qo'shimcha)

- `label` bosilganda maydon faollashadi: mobil telefonda bu bosish maydonini kattalashtiradi.
- `type="email"` mobil klaviaturada `@` belgisini ko'rsatadi.
- Brauzer yuborishdan oldin o'zi tekshiradi, lekin uni DevTools orqali chetlab o'tish mumkin.
