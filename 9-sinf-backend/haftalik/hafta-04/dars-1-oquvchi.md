# 10-dars. Ma’lumotlar tuzilmalari va string (satr) asoslari

> Bir nechta son yoki matnlarni qanday tartibda saqlashni bilmayapsizmi? Ushbu darsda Python'dagi ma'lumotlar tuzilmalari xaritasi va eng ko'p ishlatiladigan `string` (satr) turining xususiyatlarini o'rganamiz.

## Dars xulosasi

- **Ma’lumotlar tuzilmasi (Data Structure)** &mdash; ma’lumotlarni kompyuter xotirasida tartibli saqlash va ularni tez qayta ishlash usulidir.
- Python-da 5 ta asosiy o'rnatilgan ma'lumotlar tuzilmasi mavjud: `string`, `list`, `tuple`, `set`, `dict`.
- **`string` (`str`)** &mdash; belgilarning tartiblangan ketma-ketligi (matn).
- String yaratishning 3 ta usuli:
  1. Qo'shtirnoq: `"Toshkent"`
  2. Bittalik tirnoq: `'Backend'`
  3. Ko'p qatorli matnlar uchun uchlik tirnoq: `"""..."""` yoki `'''...'''`
- **O'zgarmaslik (Immutability):** String obyektlari yaratilgach, ularning ichki belgilarini to'g'ridan-to'g'ri o'zgartirib bo'lmaydi (`s[0] = 'J'` &rarr; `TypeError`).
- Belgini almashtirish uchun yangi satr yaratiladi: `"J" + s[1:]`.

## Qo'shimcha ma'lumot

### Nega tirnoqlarning 3 xil turi bor?
1. Matn ichida qo'shtirnoq yoki apostrof qatnashsa, tashqi tirnoq turini boshqacha tanlash qulay:
   - `shahar = "O'zbekiston"` &mdash; apostrof matn ichida xatolik chiqarmaydi.
   - `iqtibos = 'Ustoz dedi: "Python o\'rganing"'` &mdash; qo'shtirnoq matn ichida qulay.
2. Uchlik tirnoq (`"""`) nafaqat ko'p qatorli matn yozishda, balki funksiya va modullarga izoh (docstring) yozishda ham standart hisoblanadi.

### Xotirada Immutability nima beradi?
Satrlar o'zgarmas (immutable) bo'lgani sababli, Python ularni xotirada xavfsiz keshlaydi (String Interning). Bu esa backend tizimlarida katta matnlar bilan ishlaganda dastur xotirasini tejaydi va tezlikni oshiradi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Data Structure | Ma'lumotlar tuzilmasi |
| String (str) | Belgilar ketma-ketligidan iborat matn toifasi |
| Immutable | O'zgarmaslik (yaratilgach ichki qiymatini o'zgartirib bo'lmaydigan toifa) |
| TypeError | Noto'g'ri ma'lumot toifasi yoki ruxsat etilmagan amal bajarilgandagi xato |
| Docstring | Funksiya yoki modul vazifasini tushuntiruvchi ko'p qatorli hujjatlashtirish matni |

## Bilasizmi?

- Python dasturlash tilida bitta harf uchun alohida `char` (belgi) toifasi yo'q! Bitta harfli `"A"` ham 1 uzunlikdagi oddiy `string` hisoblanadi.
- Dunyodagi barcha yirik qidiruv tizimlari (masalan Google) har soniyada millionlab satrli so'rovlarni aynan ma'lumotlar tuzilmalarining to'g'ri tanlanishi evaziga bir zumda qayta ishlaydi.

## Topshiriqlar

### 1. Uch usul · oson
O‘z ismingizni `"..."` bilan, familiyangizni `'...'` bilan yarating va ikkalasini alohida qatorda chiqaring.
**Kutiladigan natija:** 2 qatorda ism va familiya.

### 2. Ko‘p qatorli matn · oson
`"""..."""` yordamida 3 qatorli maqolni bitta o‘zgaruvchida saqlang va bitta `print()` bilan chiqaring.
**Kutiladigan natija:** 3 qator matn.

### 3. Apostrofli matn · oson
`O'zbekiston - kelajagi buyuk davlat!` jumlasidan iborat string yarating (tashqi tirnoqni to‘g‘ri tanlang).
**Kutiladigan natija:** Jumla xatosiz chiqadi.

### 4. Tirnoq ichida tirnoq · oson
Ekranga `Alisher dedi: "Bugun dars juda qiziq bo'ldi!"` matnini chiqaruvchi bitta `print()` yozing.
**Kutiladigan natija:** Matn qo‘shtirnoqlari bilan chiqadi.

### 5. Turini aniqlang · o'rta
`a = "15"`, `b = 15`, `c = """15"""` ning turlarini `type()` bilan chiqaring. Qaysilari string?
**Kutiladigan natija:** `str`, `int`, `str`.

### 6. Bu kod nima chiqaradi? · o'rta
```python
s = "Python"
t = "J" + s[1:]
print(s, t)
```
Avval daftarga javob yozing, keyin tekshiring.
**Kutiladigan natija:** Bashoratingiz va haqiqiy natija bir xil.

### 7. Xatoni toping · o'rta
```python
shahar = 'O'zbekiston'
print(shahar)
```
Nega xato chiqadi? Tuzating.
**Kutiladigan natija:** `O'zbekiston` chiqadi.

### 8. Satr uzunligi · o'rta
`shahar = "Samarqand"` va `gap = "Men dasturchiman"` uchun `len()` natijasini chiqaring. Bo‘sh joy hisobga kirdimi?
**Kutiladigan natija:** `9` va `16`.

### 9. Bosh harfni almashtirish · qiyin
`word = "Salom"` dan `"Kalom"` hosil qiling. So‘ng `"Salom!"` yarating. Asl `word` o‘zgarmaganini chiqarib isbotlang.
**Kutiladigan natija:** `Kalom`, `Salom!`, `Salom`.

### 10. Jython va Cython · qiyin
`s = "Python"` dan bir-biridan mustaqil `"Jython"` va `"Cython"` stringlarini yarating. `s` ham, ikkala yangi string ham chiqsin.
**Kutiladigan natija:** `Python Jython Cython`

### 11. Tuzilmalarni moslashtirish · qiyin
Quyidagi ma’lumotlar uchun mos tuzilmani tanlang va izoh shaklida yozing: a) o‘quvchining ismi; b) o‘zgaradigan baholar ro‘yxati; c) GPS koordinatalari (o‘zgarmas); d) telefon daftarchasi (ism -> raqam).
**Kutiladigan natija:** 4 ta javob va qisqa izoh.

### 12. Men haqimda kartochka · bonus
Ism (`"`), maktab (`'`) va 3 qatorli «Men haqimda» (`"""`) stringlarini yarating. Ismning birinchi harfini (`ism[0]`) va har bir stringning `len()` ini chiqaring.
**Kutiladigan natija:** Kartochka va 3 ta uzunlik.

## O'zingizni tekshiring

1. Ma’lumotlar tuzilmasi nima va nega uni to‘g‘ri tanlash muhim?
2. Pythonning 5 ta asosiy tuzilmasini ayting.
3. String ichida qanday belgilar bo‘lishi mumkin?
4. Stringni qanday 3 usulda yaratish mumkin?
5. Nega `s[0] = "J"` xato beradi?
6. String o‘zgarmas bo‘lsa, «o‘zgartirilgan» variantni qanday olamiz?

## Uyga vazifa

1. `string_asos.py`: ism (`"`), familiya (`'`) va 3 qatorli «Men haqimda» (`"""`) matnini yarating va chiqaring.
2. `s = "Python"` dan `"Jython"` va `"Cython"` yasang, asl `s` o‘zgarmaganini isbotlang.
3. Ism, yosh, fanlar ro‘yxati, koordinata, telefon-ism juftligi uchun mos tuzilmani izoh shaklida yozing.
