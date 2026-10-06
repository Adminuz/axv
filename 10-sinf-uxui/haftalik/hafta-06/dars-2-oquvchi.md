# 17-dars. Flexbox layout tizimi va bir o'lchamli joylashuv

> Elementlarni yonma-yon qo'yish va markazlashni CSS da qanday qilamiz? Bugun Flexbox ni o'rganamiz: navbar va kartalar qatori yasaymiz.

## Dars xulosasi

- `display: flex` konteyner bolalarini bir qatorga tizadi.
- Ikki o'q bor: bosh (`flex-direction`) va ko'ndalang.
- `justify-content` bosh o'q, `align-items` ko'ndalang o'q bo'ylab tekislaydi.
- `gap` oraliq beradi, `flex-wrap: wrap` qatorga o'tkazadi.
- `flex: 1` bo'sh joyni teng bo'lishadi.
- `margin-left: auto` navbar da havolalarni o'ngga suradi.

## Qo'shimcha ma'lumot

### flex-direction
`row`, `column`, `row-reverse`, `column-reverse`.

### align-self
Bitta elementni alohida tekislaydi.

### order
Elementlar tartibini o'zgartiradi.

### Flex va semantika
Tartibni o'zgartirish ekran o'quvchilar uchun HTML tartibini o'zgartirmaydi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Flexbox | Bir o'lchamli joylashuv tizimi |
| Flex konteyner | `display: flex` ota |
| Flex element | Konteynerning bevosita bolasi |
| Bosh o'q | Asosiy yo'nalish |
| Ko'ndalang o'q | Unga perpendikulyar |
| gap | Orasidagi masofa |
| wrap | Qatorga o'tkazish |
| flex: 1 | Teng o'sish |

## Bilasizmi?

- DevTools da flex konteynerning yonida `flex` belgisi chiqadi; bosganda o'qlar ko'rinadi.
- `gap` avval faqat Grid da edi, hozir Flexbox da ham ishlaydi.
- Flexbox 1 o'lchamli, Grid esa 2 o'lchamli joylashuv uchun.

## Topshiriqlar

### 1. Qatorga tizish · oson

3 ta blokni qatorga qo'ying.

**Kutiladigan natija:** `display: flex`.

### 2. Oraliq · oson

Orasiga 20px bo'sh joy bering.

**Kutiladigan natija:** `gap: 20px`.

### 3. Ustun · oson

Elementlarni ustunga tizing.

**Kutiladigan natija:** `flex-direction: column`.

### 4. O'qlar · oson

Bosh va ko'ndalang o'qni tushuntiring.

**Kutiladigan natija:** Tizilish yo'nalishi va unga perpendikulyar.

### 5. Markazlash · o'rta

Matnni to'liq markazlang.

**Kutiladigan natija:** `justify-content` va `align-items: center`.

### 6. Chetga surish · o'rta

Ikki element: biri chapda, biri o'ngda.

**Kutiladigan natija:** `space-between`.

### 7. Navbar · o'rta

Logo chapda, havolalar o'ngda navbar yozing.

**Kutiladigan natija:** `margin-left: auto`.

### 8. Teng kartalar · o'rta

Uch kartaga teng kenglik bering.

**Kutiladigan natija:** `flex: 1`.

### 9. Moslashuvchan qator · qiyin

Kartalar mobilda pastga tushsin.

**Kutiladigan natija:** `flex-wrap` va `flex-basis`.

### 10. Rol almashishi · qiyin

`column` da `justify` va `align` qaysi o'qqa tegishli?

**Kutiladigan natija:** `justify` vertikal, `align` gorizontal.

### 11. Footer · qiyin

Sahifa balandligi kam bo'lsa ham footer pastda tursin (`min-height: 100vh`).

**Kutiladigan natija:** `flex-direction: column` va `main { flex: 1 }`.

### 12. Maktab sayti · bonus

Saytga flex navbar va kartalar qatorini qo'shing.

**Kutiladigan natija:** Ishlaydigan navbar va kartalar.

## O'zingizni tekshiring

1. `display: flex` nimaga yoziladi?
2. Bosh o'q nima?
3. `justify-content` va `align-items`?
4. `flex-wrap` nima?
5. `flex: 1` nima?
6. Navbar da auto margin?

## Uyga vazifa

Maktab saytiga flex navbar va kartalar qatorini qo'shing (30–40 daqiqa). To'liq shart: `uyga-vazifa.md`.
