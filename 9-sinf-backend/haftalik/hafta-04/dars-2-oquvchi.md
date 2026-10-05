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

1. **Birinchi va oxirgi belgi · oson**  
   `word = "Python"` satrining birinchi va oxirgi harfini indekslar yordamida ekranga chiqaring.

2. **So'zning o'rtasi · oson**  
   `matn = "Dasturlash"` satridan `[3:7]` oraliqdagi qismni ajratib olib ekranga chiqaring.

3. **Teskari o'girish · oson**  
   `shahar = "Toshkent"` so'zini `[::-1]` yordamida teskari tartibda chiqaring.

4. **Katta harflar · oson**  
   `fayl = "readme.txt"` satrini `.upper()` metodi bilan to'liq bosh harflarga aylantiring.

5. **Harflarni kichraytirish · oson**  
   `login = "ADMINISTRATOR"` satrini `.lower()` yordamida kichik harflarga o'tkazing.

6. **Har bir so'z bosh harfda · o'rta**  
   `kitob = "alisher navoiy xamsa"` satrini `.title()` metodi orqali `Alisher Navoiy Xamsa` ko'rinishiga keltiring.

7. **Ismni tozalash · o'rta**  
   Foydalanuvchi ismini noto'g'ri kiritgan: `ism = "dAvRoN"`. Uni chiroyli `Davron` ko'rinishiga keltiruvchi kod yozing.

8. **Qadam bilan sakrash · o'rta**  
   `alfabit = "abcdefghijklmnop"` satridan har ikkinchi harfni (`[::2]`) ajratib oling.

9. **Palindrom tekshiruvi · qiyin**  
   Foydalanuvchi kiritgan so'z palindrom (masalan `"alla"`, `"radar"`, `"kiyik"`) ekanligini `if/else` va `[::-1]` yordamida tekshiring.

10. **Matn shifrlash (Mirror string) · bonus**  
    Berilgan matnning birinchi yarmini o'z holicha, ikkinchi yarmini esa teskari tartibda birlashtirib chiqaruvchi dastur tuzing (Masalan: `"Dasturchi"` &rarr; birinchi yarmi + ikkinchi yarmi teskari).
