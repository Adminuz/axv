---
title: "10-dars. Ma’lumotlar tuzilmalari va string (satr) asoslari"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (Back-end)", "link": "/9-sinf-backend/"}, "week": {"n": 4, "link": "/9-sinf-backend/hafta-04/"}, "g": 10, "title": "Ma’lumotlar tuzilmalari va string (satr) asoslari", "lead": "Bir nechta son yoki matnlarni qanday tartibda saqlashni bilmayapsizmi? Ushbu darsda Python'dagi ma'lumotlar tuzilmalari xaritasi va eng ko'p ishlatiladigan string (satr) turining xususiyatlarini o'rganamiz.", "slide": "/slaydlar/9-sinf-backend/hafta-04/dars-1.html", "test": null, "tabs": [{"g": 10, "link": "/9-sinf-backend/hafta-04/dars-1", "current": true}, {"g": 11, "link": "/9-sinf-backend/hafta-04/dars-2", "current": false}, {"g": 12, "link": "/9-sinf-backend/hafta-04/dars-3", "current": false}], "prev": null, "next": {"g": 11, "title": "String: indeks, slicing va metodlar", "link": "/9-sinf-backend/hafta-04/dars-2"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Ma’lumotlar tuzilmasi (Data Structure)** &mdash; ma’lumotlarni kompyuter xotirasida tartibli saqlash va ularni tez qayta ishlash usulidir.
- Python-da 5 ta asosiy o'rnatilgan ma'lumotlar tuzilmasi mavjud: `string`, `list`, `tuple`, `set`, `dict`.
- **`string` (`str`)** &mdash; belgilarning tartiblangan ketma-ketligi (matn).
- String yaratishning 3 ta usuli:
  1. Qo'shtirnoq: `"Toshkent"`
  2. Bittalik tirnoq: `'Backend'`
  3. Ko'p qatorli matnlar uchun uchlik tirnoq: `"""..."""` yoki `'''...'''`
- **O'zgarmaslik (Immutability):** String obyektlari yaratilgach, ularning ichki belgilarini to'g'ridan-to'g'ri o'zgartirib bo'lmaydi (`s[0] = 'J'` &rarr; `TypeError`).
- Belgini almashtirish uchun yangi satr yaratiladi: `"J" + s[1:]`.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### Nega tirnoqlarning 3 xil turi bor?
1. Matn ichida qo'shtirnoq yoki apostrof qatnashsa, tashqi tirnoq turini boshqacha tanlash qulay:
   - `shahar = "O'zbekiston"` &mdash; apostrof matn ichida xatolik chiqarmaydi.
   - `iqtibos = 'Ustoz dedi: "Python o\'rganing"'` &mdash; qo'shtirnoq matn ichida qulay.
2. Uchlik tirnoq (`"""`) nafaqat ko'p qatorli matn yozishda, balki funksiya va modullarga izoh (docstring) yozishda ham standart hisoblanadi.

### Xotirada Immutability nima beradi?
Satrlar o'zgarmas (immutable) bo'lgani sababli, Python ularni xotirada xavfsiz keshlaydi (String Interning). Bu esa backend tizimlarida katta matnlar bilan ishlaganda dastur xotirasini tejaydi va tezlikni oshiradi.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Data Structure | Ma'lumotlar tuzilmasi |
| String (str) | Belgilar ketma-ketligidan iborat matn toifasi |
| Immutable | O'zgarmaslik (yaratilgach ichki qiymatini o'zgartirib bo'lmaydigan toifa) |
| TypeError | Noto'g'ri ma'lumot toifasi yoki ruxsat etilmagan amal bajarilgandagi xato |
| Docstring | Funksiya yoki modul vazifasini tushuntiruvchi ko'p qatorli hujjatlashtirish matni |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Python dasturlash tilida bitta harf uchun alohida `char` (belgi) toifasi yo'q! Bitta harfli `"A"` ham 1 uzunlikdagi oddiy `string` hisoblanadi.
- Dunyodagi barcha yirik qidiruv tizimlari (masalan Google) har soniyada millionlab satrli so'rovlarni aynan ma'lumotlar tuzilmalarining to'g'ri tanlanishi evaziga bir zumda qayta ishlaydi.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

1. **Uch usul · oson**  
   O‘z ismingizni `"..."` bilan, familiyangizni `'...'` bilan e'lon qiling va ikkalasini alohida qatorda ekranga chiqaring.

2. **Ko'p qatorli matn · oson**  
   `"""..."""` yordamida sevimli kitobingizdan 3 qatorli parcha yoki maqolni bitta o'zgaruvchida saqlab, ekranga chiqaring.

3. **Apostrofli matn · oson**  
   Matn ichida `"O'zbekiston - kelajagi buyuk davlat!"` jumlasi bo'lgan satr yarating (tashqi tirnoqlardan to'g'ri foydalaning).

4. **Tirnoq ichida tirnoq · oson**  
   Ekranga `Alisher dedi: "Bugun dars juda qiziq bo'ldi!"` matnini chiqaruvchi bitta `print()` yozing.

5. **Satr uzunligi · oson**  
   `shahar = "Samarqand"` satri berilgan. `len()` funksiyasidan foydalanib unda nechta belgi borligini aniqlang.

6. **Satrlarni ulash (Konkatenatsiya) · o'rta**  
   `a = "Backend"` va `b = "Dasturchi"` o'zgaruvchilarini oralariga bo'sh joy (`" "`) qo'shib birlashtiring.

7. **Kodni bashorat qiling · o'rta**  
   Quyidagi kod nima chiqaradi va nega?  
   ```python
   s = "Python"
   t = "J" + s[1:]
   print(s, t)
   ```

8. **Bosh harfni o'zgartirish · o'rta**  
   `word = "Salom"` satrining birinchi harfini `"K"` ga almashtirib yangi `Kalom` satrini hosil qiling. Asl `word` o'zgaruvchisi o'zgarmaganini isbotlang.

9. **Tuzilmalarni moslashtirish · qiyin**  
   Quyidagi 4 ta ma'lumot uchun Python'ning qaysi ma'lumotlar tuzilmasi eng mos kelishini tanlang va izohlang:  
   a) O'quvchining ismi;  
   b) Baholar ro'yxati (o'zgarishi mumkin);  
   c) GPS koordinatalari (kenglik, uzunlik &mdash; o'zgarmas);  
   d) Telefon daftarchasi (ism &rarr; raqam).

10. **Taqiqlangan amal va TypeError · bonus**  
    `matn = "Salom"` satrida `matn[0] = "X"` deb yozganda yuzaga keladigan xatolikni `try/except` yordamida ushlang va ekranga `"Satrlarni to'g'ridan-to'g'ri o'zgartirib bo'lmaydi!"` xabarini chiqaring.

</div>

