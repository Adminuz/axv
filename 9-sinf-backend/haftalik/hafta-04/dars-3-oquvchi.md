# 12-dars. List (ro‘yxat): yaratish, indeks va metodlar

> O'nlab o'zgaruvchilarni alohida e'lon qilishdan charchadingizmi? Ushbu darsda Python'ning eng ko'p qo'llaniladigan va moslashuvchan tuzilmasi &mdash; `list` (ro'yxat) hamda uning amallari bilan tanishamiz.

## Dars xulosasi

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

## Qo'shimcha ma'lumot

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

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| List (Ro'yxat) | Tartiblangan va o'zgartirish mumkin bo'lgan elementlar to'plami |
| Mutable | O'zgaruvchanlik (yaratilgach ichki tarkibini o'zgartirib bo'ladigan toifa) |
| Append | Ro'yxat oxiriga element ulash |
| Insert | Belgilangan pozitsiyaga yangi element kiritish |
| Pop | Elementni ro'yxatdan sug'urib olib qaytarish |
| Clear | Ro'yxatni to'liq bo'shatish |

## Bilasizmi?

- Pythonda bitta ro'yxat ichida bir vaqtning o'zida har xil turlarni saqlash mumkin: `aralash = ["Ali", 16, True, 4.5, ["Python", "Django"]]`.
- Telegram botlarda foydalanuvchilar savati (shopping cart) yoki to'lovlar tarixi xotirada aynan `list` ma'lumotlar tuzilmasida boshqariladi.

## Topshiriqlar

### 1. Meva ro‘yxati · oson
`mevalar = ["olma", "banan", "shaftoli"]` ning 0- va -1-elementlarini chiqaring.
**Kutiladigan natija:** `olma` va `shaftoli`.

### 2. Oxiriga qo‘shish · oson
Bo‘sh `shaharlar = []` yarating va `append()` bilan 3 ta shahar qo‘shing.
**Kutiladigan natija:** 3 ta shahardan iborat list.

### 3. Boshiga kiritish · oson
`sonlar = [10, 20, 30]` boshiga `insert(0, 5)` bilan 5 ni kiriting.
**Kutiladigan natija:** `[5, 10, 20, 30]`

### 4. Qiymatni o‘zgartirish · oson
`baholar = [4, 5, 3, 5]` dagi 3 ni (`baholar[2]`) 5 ga o‘zgartiring.
**Kutiladigan natija:** `[4, 5, 5, 5]`

### 5. Qiymat bo‘yicha o‘chirish · o'rta
`fanlar = ["Matematika", "Adabiyot", "Fizika"]` dan `remove()` bilan `"Adabiyot"` ni o‘chiring.
**Kutiladigan natija:** `['Matematika', 'Fizika']`

### 6. Navbat · o'rta
`navbat = ["Ali", "Vali", "Gani"]`. Birinchi odamni `pop(0)` bilan oling va `Xizmat ko'rsatildi: Ali` deb chiqaring, so‘ng qolgan navbatni chiqaring.
**Kutiladigan natija:** `Xizmat ko'rsatildi: Ali` va `['Vali', 'Gani']`.

### 7. Bu kod nima chiqaradi? · o'rta
```python
a = [1, 2, 2, 3]
a.remove(2)
x = a.pop(0)
print(x, a)
```
Avval bashorat qiling, keyin tekshiring.
**Kutiladigan natija:** Bashoratingiz va haqiqiy natija.

### 8. Slicing · o'rta
`filmlar` ro‘yxatiga 5 ta film yozing. `[1:4]`, `[:2]` va `[::-1]` natijalarini chiqaring.
**Kutiladigan natija:** 3 ta kesilgan list.

### 9. Xatoni toping · qiyin
```python
a = [10, 20, 30]
a.insert(99)
a.remove(40)
print(a[3])
```
Har bir qatordagi xatoni tushuntiring va kodni ishlaydigan qiling.
**Kutiladigan natija:** Xatosiz ishlaydigan kod.

### 10. Metodlar zanjiri · qiyin
`a = [1, 2]` bilan ketma-ket: `append(3)`, `insert(0, 0)`, `remove(2)`, `pop()`, `clear()`. Har qadamdan keyin `a` ni chiqaring.
**Kutiladigan natija:** `[1, 2, 3]`, `[0, 1, 2, 3]`, `[0, 1, 3]`, `[0, 1]`, `[]`.

### 11. Talabaning fanlari · qiyin
Talaba ismi (`string`) va 3 ta fani (`list`) berilgan. Yangi fan qo‘shing (`append`), 1-o‘ringa boshqa fan kiriting (`insert`), bir fanni o‘chiring (`remove`), oxirgisini `pop()` qiling. Har holatdagi ro‘yxatni va `len()` ni chiqaring.
**Kutiladigan natija:** 4 bosqichdagi ro‘yxatlar.

### 12. Teskari navbat · bonus
`navbat = ["Ali", "Vali", "Gani", "Laylo"]`. `while` sikli va `pop()` yordamida ro‘yxat bo‘shaguncha har safar oxirgi odamni chiqaring (`while navbat:`).
**Kutiladigan natija:** `Laylo`, `Gani`, `Vali`, `Ali` va oxirida `[]`.

## O'zingizni tekshiring

1. List nima va uning 3 ta xususiyatini ayting.
2. List va string’ning umumiy jihati va asosiy farqi nimada?
3. `append()` va `insert()` farqi nima?
4. `remove()` va `pop()` qachon ishlatiladi?
5. `pop()` va `pop(0)` farqi nima?
6. `clear()` dan keyin list nimaga teng bo‘ladi?

## Uyga vazifa

1. `list_mashq.py`: 5 ta film ro‘yxatini yarating; birinchi, oxirgi elementni, `[1:4]` va `[::-1]` ni chiqaring.
2. `a = [1, 2]` ni `append`, `insert`, `remove`, `pop`, `clear` bilan o‘zgartirib, har qadamni chop eting.
3. «Talabalar ma’lumotlari» boshlang‘ich qismi: ism-familiya `string`, fanlar `list` (qo‘shish va o‘chirish bilan).
