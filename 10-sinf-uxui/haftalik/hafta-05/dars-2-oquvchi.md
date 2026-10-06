# 14-dars. Formalar, validatsiya va interfeys elementlari semantikasi

> Formani to'ldirib bo'lmasa, odam saytni tark etadi. Bugun forma yozamiz: tushunarli, tekshiriladigan va hamma uchun qulay.

## Dars xulosasi

- `form` ichida har maydonga `label`; `for` qiymati `input` ning `id` siga teng.
- `fieldset` va `legend` bog'liq maydonlarni guruhlaydi.
- To'g'ri `type` (email, tel, number, date) mobil klaviatura va tekshiruvni yaxshilaydi.
- Validatsiya: `required`, `minlength`, `maxlength`, `min`, `max`, `pattern`.
- Xato xabari aniq bo'lsin va `aria-describedby` bilan bog'lansin; faqat rangga tayanmang.
- `a` — sahifaga o'tish, `button` — amal; serverda ham tekshirish kerak.

## Qo'shimcha ma'lumot

### placeholder va label
`placeholder` yozishni boshlaganda yo'qoladi, shuning uchun maydon nomi sifatida `label` kerak.

### Mobil klaviatura
`type="tel"` raqamli, `type="email"` esa `@` li klaviatura ochadi.

### Rangga tayanmaslik
Xatoni faqat qizil rang bilan ko'rsatish rang ajratmaydigan foydalanuvchilar uchun yetarli emas: matn qo'shing.

### Odatiy xatolar
`label` yo'q; `for` va `id` mos emas; `button` ga `type` yozilmagan.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| form | Ma'lumot yuborish bloki |
| label | Maydon nomi |
| input | Kiritish maydoni |
| fieldset | Maydonlar guruhi |
| legend | Guruh nomi |
| Validatsiya | Kiritilgan ma'lumotni tekshirish |
| pattern | Muntazam ifoda atributi |
| required | Majburiy maydon atributi |
| aria-describedby | Maydonga izoh bog'lash |

## Bilasizmi?

- `label` bosilganda maydon faollashadi: mobil telefonda bu bosish maydonini kattalashtiradi.
- `type="email"` mobil klaviaturada `@` belgisini ko'rsatadi.
- Brauzer yuborishdan oldin o'zi tekshiradi, lekin uni DevTools orqali chetlab o'tish mumkin.

## Topshiriqlar

### 1. label ni ulang · oson

`<input id="fam">` ga `Familiya` label ini ulang.

**Kutiladigan natija:** `<label for="fam">Familiya</label>`.

### 2. Type tanlash · oson

Email, telefon, sana va son uchun `type` yozing.

**Kutiladigan natija:** email, tel, date, number.

### 3. Majburiy maydon · oson

Ism maydonini majburiy va kamida 2 belgili qiling.

**Kutiladigan natija:** `required minlength="2"`.

### 4. a yoki button · oson

«Qoidalarni ko'rish» (sahifaga o'tish) va «Yuborish» uchun qaysi teg?

**Kutiladigan natija:** `a` va `button`.

### 5. Sinf maydoni · o'rta

Sinf (1–11) uchun maydon yozing.

**Kutiladigan natija:** `type="number" min="1" max="11"`.

### 6. Telefon pattern · o'rta

+998 va 9 raqamga `pattern` yozing.

**Kutiladigan natija:** `pattern="\+998[0-9]{9}"`.

### 7. Fieldset · o'rta

Radio tugmalarni `fieldset` va `legend` bilan guruhlang.

**Kutiladigan natija:** Guruhlangan radio.

### 8. Xato xabari · o'rta

«Noto'g'ri» xabarini tushunarli qilib qayta yozing.

**Kutiladigan natija:** Nima xato va qanday tuzatish yozilgan.

### 9. Qabul formasi · qiyin

5 maydonli qabul formasini to'liq yozing.

**Kutiladigan natija:** `label`, validatsiya, `submit`.

### 10. aria-describedby · qiyin

Xato xabarini maydonga bog'lang.

**Kutiladigan natija:** `aria-describedby` = xabar `id`.

### 11. Klaviatura testi · qiyin

Formani faqat Tab va Enter bilan to'ldirib ko'ring, muammolarni yozing.

**Kutiladigan natija:** Tartib va fokus tekshirilgan.

### 12. Server tekshiruvi · bonus

Telefon uchun server tekshiruvi qoidasini (so'z bilan) yozing.

**Kutiladigan natija:** +998 bilan boshlanadi, 13 belgi.

## O'zingizni tekshiring

1. `label` va `for` nima qiladi?
2. Qaysi `type` lar bor?
3. `required` va `pattern`?
4. Xato xabari qanday bo'lishi kerak?
5. `button` va `a` farqi?
6. Nima uchun serverda ham tekshiramiz?

## Uyga vazifa

Maktab qabul formasini yozing va klaviatura bilan sinang (25 daqiqa). To'liq shart: `uyga-vazifa.md`.
