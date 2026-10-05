# 11-dars. String: indeks, slicing va metodlar

> Matndan ma'lum bir harfni ajratib olish yoki so'zlarni bosh harfga aylantirish kerakmi? Ushbu darsda indekslash, qirqib olish (slicing) va eng muhim satr metodlari bilan tanishamiz.

## Dars xulosasi

- **Indekslash (Indexing)** &mdash; satrdagi har bir belgining o'z tartib raqami bor.
  - Musbat indekslar chapdan boshlanadi: `0, 1, 2, ...`
  - Manfiy indekslar o'ngdan (oxiridan) boshlanadi: `-1, -2, -3, ...` (`s[-1]` &mdash; doim oxirgi belgi).
- **Qirqib olish (Slicing)** &mdash; `satr[start : stop : step]`
  - `start` &mdash; boshlang'ich indeks (kiradi);
  - `stop` &mdash; tugash indeksi (**kirmaydi!**);
  - `step` &mdash; qadam miqdori (`[::-1]` &mdash; satrni teskari o'giradi).
- **Asosiy satr metodlari:**
  - `.upper()` &mdash; barcha harflarni KATTA qiladi;
  - `.lower()` &mdash; barcha harflarni kichik qiladi;
  - `.capitalize()` &mdash; faqat eng birinchi harfni katta qiladi;
  - `.title()` &mdash; har bir so'zning birinchi harfini katta qiladi.

## Qo'shimcha ma'lumot

### Slicing formulalari
| Kod | Ma'nosi | Natija (`"Backend"`) |
|---|---|---|
| `s[0]` | Eng birinchi belgi | `'B'` |
| `s[-1]` | Eng oxirgi belgi | `'d'` |
| `s[:4]` | Boshidan 4-indeksgacha | `'Back'` |
| `s[4:]` | 4-indeksdan oxirigacha | `'end'` |
| `s[::2]` | 2 qadam bilan (juft o'rinlar) | `'Bcen'` |
| `s[::-1]` | Butunlay teskari tartib | `'dnekcaB'` |

### Metodlar asl satrni o'zgartiradimi?
Yo'q! String immutable bo'lgani sababli, `s.upper()` chaqirilganda `s` o'zgarib qolmaydi, balki natija sifatida yangi o'zgartirilgan satr qaytadi. Uni saqlash uchun yangi o'zgaruvchiga tenglash lozim: `yangi = s.upper()`.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Index (Indeks) | Belgining satrdagi 0 dan boshlanuvchi tartib o'rni |
| Slicing (Kesish) | Satrdan oraliq qismni `[start:stop:step]` orqali ajratib olish |
| Step (Qadam) | Harflarni nechtadan tashlab o'tish miqdori |
| Method (Metod) | Muayyan obyektga biriktirilgan va uning ustida amal bajaruvchi funksiya |
| Palindrome | To'g'ri va teskari o'qilganda bir xil bo'ladigan so'z (masalan: `radar`, `non`) |

## Bilasizmi?

- Pythonda manfiy indekslash (`-1`) juda qulay imkoniyatdir. Ko'pgina boshqa dasturlash tillarida (C++, Java) oxirgi harfni olish uchun `s[s.length() - 1]` deb yozish shart.
- Slicing amali satr chegarasidan chiqib ketganda (masalan `"Salom"[0:100]`) xatolik bermaydi, boricha qirqib oladi!

## Topshiriqlar

### 1. Birinchi va oxirgi belgi · oson
`word = "Python"` ning birinchi va oxirgi harfini indeks bilan chiqaring.
**Kutiladigan natija:** `P` va `n`.

### 2. So‘zning o‘rtasi · oson
`matn = "Dasturlash"` dan `[3:7]` qismini chiqaring.
**Kutiladigan natija:** `turl`

### 3. Teskari o‘girish · oson
`shahar = "Toshkent"` ni `[::-1]` bilan teskari chiqaring.
**Kutiladigan natija:** `tnekhsoT`

### 4. Katta va kichik · oson
`fayl = "readme.txt"` ni `upper()` bilan, `login = "ADMINISTRATOR"` ni `lower()` bilan chiqaring.
**Kutiladigan natija:** `README.TXT` va `administrator`.

### 5. Har bir so‘z bosh harfda · o'rta
`kitob = "alisher navoiy xamsa"` ni `title()` bilan chiqaring. `capitalize()` natijasi bilan solishtiring.
**Kutiladigan natija:** `Alisher Navoiy Xamsa` va `Alisher navoiy xamsa`.

### 6. Ismni tozalash · o'rta
`ism = "dAvRoN"`. Uni `Davron` ko‘rinishiga keltiring.
**Kutiladigan natija:** `Davron`

### 7. Bu kod nima chiqaradi? · o'rta
```python
w = "Backend"
print(w[:4], w[4:], w[-1], w[::3])
```
Avval bashorat qiling, keyin tekshiring.
**Kutiladigan natija:** Bashoratingiz va haqiqiy natija.

### 8. Har ikkinchi harf · o'rta
`alfabit = "abcdefghijklmnop"` dan `[::2]` bilan har ikkinchi harfni oling.
**Kutiladigan natija:** `acegikmo`

### 9. Fayl kengaytmasi · qiyin
`fayl = "rasm.png"`. Manfiy indeksli slicing bilan oxirgi 3 belgini (kengaytmani) va nuqtagacha bo‘lgan nomni chiqaring.
**Kutiladigan natija:** `png` va `rasm`.

### 10. Palindrom tekshiruvi · qiyin
Foydalanuvchi so‘z kiritadi. `[::-1]` va `if/else` bilan palindrom ekanini tekshiring (`radar`, `kiyik`, `non`). Katta-kichik harf farq qilmasin (`lower()`).
**Kutiladigan natija:** `Radar` -> `Palindrom`, `Python` -> `Palindrom emas`.

### 11. Xatoni toping · qiyin
```python
s = "Python"
print(s[6])
s.upper()
print(s)
```
Bu kodda 2 ta muammo bor: biri xato beradi, ikkinchisi kutilgan `PYTHON` ni chiqarmaydi. Tuzating.
**Kutiladigan natija:** `n` va `PYTHON`.

### 12. Mirror string · bonus
Matnning birinchi yarmini o‘z holicha, ikkinchi yarmini teskari tartibda ulab chiqaring (`len()` va `//` dan foydalaning). Masalan: `"Dasturchi"`.
**Kutiladigan natija:** `Dastihcru`

## O'zingizni tekshiring

1. Pythonda indeks nechadan boshlanadi? Oxirgi belgining manfiy indeksi qanday?
2. Slicing shaklidagi 3 qismni ayting.
3. `[1:4]` da 4-indeksdagi belgi nega kirmaydi?
4. `[::-1]` nima qiladi?
5. `title()` va `capitalize()` farqi nimada?
6. Nega `s.upper()` dan keyin `s` o‘zgarmaydi?

## Uyga vazifa

1. `slicing_mashq.py`: `word = "Backend"` uchun `[1:4]`, `[:3]`, `[3:]`, `[::2]`, `[::-1]` natijalarini chiqaring.
2. `"ozbekiston respublikasi"` ni 4 ta metod bilan alohida qatorlarda chiqaring.
3. Kiritilgan so‘zning palindrom ekanini `[::-1]` bilan tekshiring.
