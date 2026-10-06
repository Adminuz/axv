# 18-dars. Fayllar bilan ishlash: open, with, o'qish va yozish

> Dastur o'chsa, o'zgaruvchilardagi ma'lumot yo'qoladi. Bugun ma'lumotni faylga saqlashni va qayta o'qishni o'rganamiz, 16–17-darslardagi funksiyalar va try/except bilan «Kundalik» dasturini yozamiz.

## Dars xulosasi

- `with open(...) as f` faylni avtomatik yopadi.
- Rejimlar: `r` o'qish, `w` yozish (o'chiradi), `a` qo'shish, `x` yaratish.
- `write` yozadi; `\n` yangi qator.
- O'qish: `read`, `readline`, `readlines`, `for`.
- `encoding="utf-8"` ni yozing.
- Fayl yo'q bo'lsa — `FileNotFoundError` ni ushlang.

## Qo'shimcha ma'lumot

### `writelines`
Qatorlar ro'yxatini yozadi.

### `os.path.exists`
Fayl bormi — tekshiradi.

### `json`
Lug'atni faylda saqlash.

### `seek(0)`
Fayl kursorini boshiga qaytaradi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Fayl | Xotirada saqlanadigan ma'lumot |
| open() | Faylni ochish |
| with | Avtomatik yopuvchi blok |
| Rejim | Ochish maqsadi: r, w, a, x |
| write | Faylga yozish |
| read | Fayldan o'qish |
| encoding | Matn kodlanishi |
| FileNotFoundError | Fayl topilmadi |

## Bilasizmi?

- `pathlib.Path` yordamida fayl yo'llari bilan qulay ishlash mumkin (keyingi bosqichlarda).
- `json` moduli lug'at va ro'yxatlarni faylga yozish uchun qulay.
- Backend'da yozuvlar fayl o'rniga ma'lumotlar bazasiga (PostgreSQL) yoziladi.

## Topshiriqlar

### 1. Fayl nima · oson

Fayl nima uchun kerak?

**Kutiladigan natija:** Ma'lumotni saqlash.

### 2. with · oson

`with open` ning afzalligi?

**Kutiladigan natija:** Fayl avtomatik yopiladi.

### 3. Rejimlar · oson

4 ta fayl rejimini yozing.

**Kutiladigan natija:** r, w, a, x.

### 4. Yangi qator · oson

Yangi qator belgisi qaysi?

**Kutiladigan natija:** `\n`.

### 5. w va a · o'rta

`w` va `a` farqini yozing.

**Kutiladigan natija:** w o'chiradi, a qo'shadi.

### 6. Yozish · o'rta

Faylga ism yozing.

**Kutiladigan natija:** `write("Ali\n")`.

### 7. O'qish · o'rta

Faylni qator-qator o'qing.

**Kutiladigan natija:** `for qator in f`.

### 8. strip · o'rta

`strip()` nima qiladi?

**Kutiladigan natija:** Chetdagi bo'shliq va `\n` ni olib tashlaydi.

### 9. Xatoni ushlash · qiyin

Fayl yo'q bo'lsa xabar bering.

**Kutiladigan natija:** `except FileNotFoundError`.

### 10. Funksiya · qiyin

Yozuv qo'shadigan funksiya yozing.

**Kutiladigan natija:** `yozuv_qosh(matn)`.

### 11. Raqamlash · qiyin

Qatorlarni raqamlab chiqaring.

**Kutiladigan natija:** `enumerate`.

### 12. Kundalik · bonus

Sana bilan yozadigan kundalik yozing.

**Kutiladigan natija:** Yozuvlar sana bilan saqlanadi.

## O'zingizni tekshiring

1. Fayl rejimlari?
2. with nima uchun?
3. w va a farqi?
4. Fayl qanday o'qiladi?
5. FileNotFoundError nima?
6. utf-8 nima uchun?

## Uyga vazifa

«Kundalik» dasturini yozing (30–40 daqiqa). To'liq shart: `uyga-vazifa.md`.
