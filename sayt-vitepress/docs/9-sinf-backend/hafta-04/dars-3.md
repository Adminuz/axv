---
title: "12-dars. List (ro‘yxat): yaratish, indeks va metodlar"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (Back-end)", "link": "/9-sinf-backend/"}, "week": {"n": 4, "link": "/9-sinf-backend/hafta-04/"}, "g": 12, "title": "List (ro‘yxat): yaratish, indeks va metodlar", "lead": "O'nlab o'zgaruvchilarni alohida e'lon qilishdan charchadingizmi? Ushbu darsda Python'ning eng ko'p qo'llaniladigan va moslashuvchan tuzilmasi &mdash; list (ro'yxat) hamda uning amallari bilan tanishamiz.", "slide": "/slaydlar/9-sinf-backend/hafta-04/dars-3.html", "test": null, "tabs": [{"g": 10, "link": "/9-sinf-backend/hafta-04/dars-1", "current": false}, {"g": 11, "link": "/9-sinf-backend/hafta-04/dars-2", "current": false}, {"g": 12, "link": "/9-sinf-backend/hafta-04/dars-3", "current": true}], "prev": {"g": 11, "title": "String: indeks, slicing va metodlar", "link": "/9-sinf-backend/hafta-04/dars-2"}, "next": null}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **`list` (ro'yxat)** &mdash; tartiblangan, o'zgaruvchan (mutable) va turli tipdagi qiymatlarni bitta konteynerda saqlovchi ma'lumotlar tuzilmasi.
- List kvadrat qavslar `[ ]` yordamida yaratiladi: `sonlar = [10, 20, 30]`.
- **Mutable (O'zgaruvchanlik):** Stringdan farqli o'laroq, list elementini indeks orqali to'g'ridan-to'g'ri o'zgartirish mumkin (`sonlar[0] = 99`).
- **Asosiy ro'yxat metodlari:**
  - `.append(qiymat)` &mdash; ro'yxat oxiriga bitta element qo'shadi;
  - `.insert(indeks, qiymat)` &mdash; belgilangan indeksga yangi element kiritadi;
  - `.remove(qiymat)` &mdash; ro'yxatdan birinchi uchragan ko'rsatilgan qiymatni o'chiradi;
  - `.pop()` &mdash; oxirgi elementni sug'urib oladi (qaytaradi va o'chiradi);
  - `.pop(indeks)` &mdash; ko'rsatilgan indeksdagi elementni sug'urib oladi;
  - `.clear()` &mdash; ro'yxatni butunlay tozalab, bo'sh `[]` qiladi.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### String vs List taqqoslovi
| Xususiyat | `string` | `list` |
|---|---|---|
| Qavs turi | `"..."`, `'...'` | `[...]` |
| Tartiblanganmi? | Ha (indeks bor) | Ha (indeks bor) |
| Slicing bormi? | Ha (`s[1:4]`) | Ha (`a[1:4]`) |
| O'zgaruvchanmi (Mutable)? | **Yo'q** (`TypeError`) | **Ha** (`a[0] = 50`) |
| Element turlari | Faqat belgilar | Har qanday tur (son, matn, hatto boshqa list) |

### `remove()` va `pop()` farqi
- `remove(qiymat)` &mdash; siz elementning o'zini (qiymatini) bilasiz, lekin qayerdaligini bilmaysiz. U o'chirilgan qiymatni qaytarmaydi.
- `pop(indeks)` &mdash; siz indeksni bilasiz va sug'urib olingan qiymatni o'zgaruvchida saqlab qolmoqchisiz: `chiqarildi = a.pop(0)`.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| List (Ro'yxat) | Tartiblangan va o'zgartirish mumkin bo'lgan elementlar to'plami |
| Mutable | O'zgaruvchanlik (yaratilgach ichki tarkibini o'zgartirib bo'ladigan toifa) |
| Append | Ro'yxat oxiriga element ulash |
| Insert | Belgilangan pozitsiyaga yangi element kiritish |
| Pop | Elementni ro'yxatdan sug'urib olib qaytarish |
| Clear | Ro'yxatni to'liq bo'shatish |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Pythonda bitta ro'yxat ichida bir vaqtning o'zida har xil turlarni saqlash mumkin: `aralash = ["Ali", 16, True, 4.5, ["Python", "Django"]]`.
- Telegram botlarda foydalanuvchilar savati (shopping cart) yoki to'lovlar tarixi xotirada aynan `list` ma'lumotlar tuzilmasida boshqariladi.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

1. **Meva ro'yxati · oson**  
   `mevalar = ["olma", "banan", "shaftoli"]` ro'yxatini e'lon qiling va uning 0-hamda -1-indeksdagi elementlarini chiqaring.

2. **Oxiriga qo'shish · oson**  
   Bo'sh `shaxarlar = []` ro'yxatini tuzing va unga `.append()` yordamida navbatma-navbat 3 ta shahar nomini qo'shing.

3. **Boshiga kiritish · oson**  
   `sonlar = [10, 20, 30]` ro'yxatining eng boshiga (`0`-indeksga) `.insert(0, 5)` orqali 5 sonini kiriting.

4. **Qiymatni o'zgartirish · oson**  
   `baholar = [4, 5, 3, 5]` ro'yxatidagi 3 bahosini (`baholar[2]`) 5 ga o'zgartiring.

5. **Qiymat bo'yicha o'chirish · oson**  
   `fanlar = ["Matematika", "Adabiyot", "Fizika"]` ro'yxatidan `.remove("Adabiyot")` yordamida "Adabiyot"ni o'chirib tashlang.

6. **Oxirgi elementni sug'urish · o'rta**  
   `navbat = ["Ali", "Vali", "Gani"]` ro'yxatidan eng oxirgi odamni `.pop()` orqali sug'urib oling va `print("Xizmat ko'rsatildi:", odam)` deb chiqaring.

7. **Boshidan sug'urish · o'rta**  
   Xuddi shu navbatdan birinchi turgan odamni `.pop(0)` orqali oling va qolgan navbatni chiqaring.

8. **Kodni bashorat qiling · o'rta**  
   Quyidagi kod natijasini taxmin qiling va tekshiring:  
   ```python
   a = [1, 2, 2, 3]
   a.remove(2)
   x = a.pop(0)
   print(x, a)
   ```

9. **Talabaning fanlari mini-loyihasi · qiyin**  
   Talaba ismi (`string`) va uning 3 ta fani (`list`) berilgan. Yangi fan qo'shing (`append`), 1-o'ringa boshqa fan kiriting (`insert`), bir fanni o'chiring (`remove`) va oxirgisini `pop()` qilib har bir holatdagi ro'yxatni chop eting.

10. **Ro'yxatni saralash va tozalash · bonus**  
    `raqamlar = [45, 12, 89, 3, 27]` ro'yxatini o'sish tartibida saralang (`.sort()`), so'ngra `.clear()` qilib bo'sh qolganini ko'rsating.

</div>

