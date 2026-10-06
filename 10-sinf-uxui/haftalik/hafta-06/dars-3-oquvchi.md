# 18-dars. CSS Grid layout tizimi va murakkab sahifa to'rlari

> Sahifaning yuqori, chap va pastki qismlarini bir vaqtda qanday joylashtiramiz? Bugun CSS Grid bilan sahifa maketi va responsiv kartalar yasaymiz.

## Dars xulosasi

- Grid — ikki o'lchamli joylashuv: ustun va qator.
- `grid-template-columns` ustunlarni, `gap` oraliqni beradi.
- `fr` — bo'sh joy ulushi, `repeat()` ustunlarni takrorlaydi.
- `grid-template-areas` va `grid-area` maketni xaritadek yozadi.
- `repeat(auto-fit, minmax(200px, 1fr))` responsiv to'r beradi.
- Grid — sahifa maketi uchun, Flexbox — bir yo'nalishli qatorlar uchun.

## Qo'shimcha ma'lumot

### grid-template-rows
Qatorlar balandligini belgilaydi.

### auto-fill
Bo'sh ustunlarni ham saqlab qoladi.

### Gutter
Ustunlar orasidagi masofa; CSS da `gap`.

### 12 ustunli grid
Dizaynda keng tarqalgan, 2, 3, 4, 6 ga bo'linadi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Grid | Ikki o'lchamli joylashuv |
| fr | Bo'sh joy ulushi |
| repeat() | Ustunlarni takrorlash |
| minmax() | Eng kam va ko'p o'lcham |
| gap | Oraliq |
| grid-area | Nomlangan soha |
| auto-fit | Sig'gancha joylash |
| span | Bir necha ustunga yoyish |

## Bilasizmi?

- DevTools da Grid belgisi bosilsa, setka chiziqlari va nomlari ko'rinadi.
- Qo'llanmadagi 6 turdagi gridlar: Baseline, Column, Modular, Manuscript, Pixel, Hierarchical.
- Qo'llanma tavsiyasi: oraliqlar uchun 8pt grid (8, 16, 24, 32 piksel).

## Topshiriqlar

### 1. 3 ustun · oson

3 ta teng ustun yarating.

**Kutiladigan natija:** `repeat(3, 1fr)`.

### 2. fr · oson

`1fr 2fr` ni tushuntiring.

**Kutiladigan natija:** 1/3 va 2/3.

### 3. Oraliq · oson

Katakchalar orasiga 20px bering.

**Kutiladigan natija:** `gap: 20px`.

### 4. Grid yoqish · oson

Grid ni qanday yoqasiz?

**Kutiladigan natija:** `display: grid`.

### 5. Sidebar maket · o'rta

240px chap ustun va qolgan joy.

**Kutiladigan natija:** `240px 1fr`.

### 6. Areas · o'rta

4 qismli maketni `areas` bilan yozing.

**Kutiladigan natija:** header, sidebar, main, footer.

### 7. Yoyish · o'rta

Bitta kartani 2 ustunga yoying.

**Kutiladigan natija:** `grid-column: span 2`.

### 8. minmax · o'rta

`minmax(150px, 1fr)` nimani bildiradi?

**Kutiladigan natija:** Kamida 150px, ko'pi bilan teng ulush.

### 9. Responsiv to'r · qiyin

Media-so'rovsiz responsiv kartalar yozing.

**Kutiladigan natija:** `auto-fit` va `minmax`.

### 10. Tanlov · qiyin

Navbar va sahifa maketi uchun qaysi tizim?

**Kutiladigan natija:** Navbar — Flexbox, sahifa — Grid.

### 11. Maktab sayti · qiyin

Saytga header, sidebar, main, footer maketini qo'shing.

**Kutiladigan natija:** Ishlaydigan maket.

### 12. Mobil maket · bonus

Tor ekranda maketni bitta ustunga o'zgartiring.

**Kutiladigan natija:** Media-so'rov bilan `areas` almashadi.

## O'zingizni tekshiring

1. Grid nechta o'lchamli?
2. `fr` nima?
3. `repeat(3, 1fr)`?
4. `grid-area` nima?
5. `auto-fit` nima qiladi?
6. Grid va Flexbox tanlovi?

## Uyga vazifa

Maktab saytiga Grid maketi va responsiv kartalar to'rini qo'shing (40 daqiqa). To'liq shart: `uyga-vazifa.md`.
