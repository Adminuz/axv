# 17-dars. Istisnoli holatlar: try, except, else, finally

> Foydalanuvchi har doim ham to'g'ri qiymat kiritmaydi, fayl esa yo'q bo'lishi mumkin. Bugun xatolarga qo'rqmasdan, ularni boshqarishni o'rganamiz: dastur yiqilmaydi, foydalanuvchi esa tushunarli xabar oladi.

## Dars xulosasi

- Istisno — signal; ushlanmasa, dastur to'xtaydi.
- Traceback: oxirgi qator — xato turi, yuqorida — joyi.
- `try/except` — xatoni ushlash; aniq istisnoni yozing.
- `else` — xatosiz bo'lsa; `finally` — doim ishlaydi.
- `while True` + `try` — to'g'ri bo'lguncha so'rash.
- `raise` — o'zimiz istisno chiqarish.

## Qo'shimcha ma'lumot

### `except Exception as e`
Xato obyektini olish.

### `assert`
Shartni tekshirish.

### Custom exception
O'zimiz yaratgan istisno turi.

### Logging
Xatolarni faylga yozish.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Istisno | Kutilmagan holat |
| Traceback | Xato haqidagi xabar |
| try | Xavfli kod bloki |
| except | Xatoni ushlash |
| else | Xatosiz bo'lsa |
| finally | Doim ishlaydi |
| raise | Istisno chiqarish |
| ValueError | Qiymat xatosi |

## Bilasizmi?

- `except Exception as e:` bilan xato obyektini olib, `print(e)` bilan xabarni ko'rsatish mumkin.
- Python'da `try/except` mantiqiy «oldin sinab ko'r» (EAFP) uslubiga mos.
- Backend'da xatolar fayl yoki log tizimiga yoziladi: bu keyingi bosqichlarda.

## Topshiriqlar

### 1. Istisno turi · oson

`10 / 0` qaysi istisnoni beradi?

**Kutiladigan natija:** `ZeroDivisionError`.

### 2. Traceback · oson

Traceback da xato turi qayerda yoziladi?

**Kutiladigan natija:** Oxirgi qatorda.

### 3. try tuzilishi · oson

try/except tuzilishini yozing.

**Kutiladigan natija:** `try:` va `except:` bloklari.

### 4. Istisno nomlari · oson

3 ta istisno turini yozing.

**Kutiladigan natija:** ValueError, KeyError, IndexError.

### 5. ValueError · o'rta

Songa aylantirishni xavfsiz qiling.

**Kutiladigan natija:** `try: int() except ValueError`.

### 6. else · o'rta

`else` qachon ishlaydi?

**Kutiladigan natija:** Xato bo'lmasa.

### 7. finally · o'rta

`finally` nimaga kerak?

**Kutiladigan natija:** Tozalash ishlari uchun.

### 8. Ikki xato · o'rta

Ikki istisnoni birga ushlang.

**Kutiladigan natija:** `except (A, B):`.

### 9. Kiritish sikli · qiyin

To'g'ri son kiritilguncha so'rang.

**Kutiladigan natija:** `while True` + `try`.

### 10. raise · qiyin

Manfiy yoshda xato chiqaring.

**Kutiladigan natija:** `raise ValueError`.

### 11. Kalkulyator · qiyin

Xatolarga chidamli kalkulyator yozing.

**Kutiladigan natija:** Xatolar ushlanadi.

### 12. Test rejasi · bonus

Kalkulyator uchun 5 ta xato holatini yozing.

**Kutiladigan natija:** Xato holatlar jadvali.

## O'zingizni tekshiring

1. Istisno nima?
2. try/except qanday yoziladi?
3. else va finally farqi?
4. Nega aniq istisno ushlanadi?
5. raise nima?
6. Kiritishni qanday tekshiramiz?

## Uyga vazifa

Xavfsiz kalkulyatorni yozing (30–40 daqiqa). To'liq shart: `uyga-vazifa.md`.
