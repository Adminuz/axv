# 12-dars. Kotlin sintaksisi: if va when shart operatorlari

> Dasturda qarorlar qabul qilish va shartlar bo'yicha turli amallarni bajarish vaqti keldi! Ushbu darsda Kotlindagi `if-else` ifodalari hamda eng qudratli `when` operatorini o'rganamiz.

## Dars xulosasi

- **`if-else` ifoda sifatida (Expression):** Kotlinda `if` nafaqat shart tekshiradi, balki natija ham qaytara oladi (`val max = if (a > b) a else b`).
- **Ternar operatori yo'qligi:** Java'dagi `a ? b : c` o'rniga to'g'ridan-to'g'ri `if (a) b else c` yoziladi.
- **`when` operatori:** Java'dagi `switch` operatorining zamonaviy va kuchaytirilgan ko'rinishi.
- **`when` afzalliklari:**
  - `break` so'zini yozish umuman shart emas;
  - Bir nechta qiymatni vergul bilan tekshirish mumkin (`1, 2 -> ...`);
  - Oraliqlarni (`in 1..10 -> ...`) tekshirish mumkin;
  - Ifoda sifatida o'zgaruvchiga qiymat yuklay oladi (`val baho = when (ball) { ... }`).

## Qo'shimcha ma'lumot

### Nega `when` ifoda sifatida ishlatilganda `else` shart?
Agar `val natija = when (kun) { 1 -> "Du", 2 -> "Se" }` deb yozsak va `kun = 5` bo'lib qolsa, o'zgaruvchiga qanday qiymat yuklash noma'lum bo'ladi. Shu sababli Kotlin kompilyatori xatolik bermasligi uchun majburiy `else` talab qiladi.

### Range (Oraliq) &mdash; `..` operatori
Kotlinda `1..5` yozuvi 1, 2, 3, 4, 5 sonlarini o'z ichiga olgan oraliqni bildiradi. Shart tekshirishda `in 1..5` yoki `!in 1..5` (oraliqqa kirmaslik) ko'rinishida qo'llaniladi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Condition (Shart) | Mantiqiy ifoda (`true` yoki `false`) |
| if-else | Shartli tarmoqlanish operatori |
| when | Ko'p variantli tanlash operatori |
| Expression (Ifoda) | Bajarilgach, aniq bir natija (qiymat) qaytaruvchi kod bo'lagi |
| Range | Sonlar oralig'i (`1..100`) |
| else | Yuqoridagi barcha shartlar bajarilmaganda ishga tushuvchi zaxira blok |

## Bilasizmi?

- Kotlindagi `when` operatori nafaqat son va matnlarni, balki har qanday murakkab obyektlarni va ularning turlarini (`is String`, `is Int`) ham tekshira oladi.
- Android ilovalarida tugma bosilganda qaysi element tanlanganini aniqlashda `when (view.id) { ... }` eng ko'p ishlatiladigan andoza hisoblanadi.

## Topshiriqlar

1. **Musbat yoki manfiy · oson**  
   Son berilgan (`val son = -15`). `if-else` yordamida uning musbat yoki manfiy ekanligini konsolga chiqaring.

2. **Kattasini topish · oson**  
   Ikkita son `a = 45` va `b = 78` berilgan. `val katta = if (a > b) a else b` ifodasi orqali kattasini aniqlang va chiqaring.

3. **Fasllar aniqlagichi · oson**  
   1 dan 4 gacha bo'lgan fasl raqamiga qarab fasl nomini (`1 &rarr; Qish, 2 &rarr; Bahor...`) chiqaruvchi `when` dasturini yozing.

4. **Oraliq tekshiruvi · oson**  
   O'quvchining yoshi berilgan. `in 7..17` sharti orqali uning maktab o'quvchisi ekanligini aniqlang.

5. **Parol uzunligi · o'rta**  
   Parol satri berilgan. Agar uzunligi (`parol.length`) 8 dan kam bo'lsa &mdash; `"Zaif parol"`, 8 va undan ko'p bo'lsa &mdash; `"Xavfsiz parol"` deb chiqaring.

6. **Baholash tizimi · o'rta**  
   0 dan 100 gacha bo'lgan ball berilgan. `when` va `in` orqali an'anaviy bahoni (2, 3, 4, 5) aniqlab, `val baho` o'zgaruvchisiga saqlang.

7. **Svetofor qoidasi · o'rta**  
   Chiroq rangi (`"Qizil"`, `"Sariq"`, `"Yashil"`) bo'yicha haydovchiga nima qilish kerakligini ko'rsatuvchi `when` blokini yozing.

8. **Oy kunlari soni · o'rta**  
   Oy raqami (1..12) berilgan. `when` yordamida oydagi kunlar sonini (28, 30 yoki 31) aniqlang (bir nechta oyni vergul bilan yozing: `1, 3, 5, 7, 8, 10, 12 -> 31`).

9. **Mini-Kalkulyator · qiyin**  
   Ikkita haqiqiy son `val a = 12.0`, `val b = 4.0` va amal belgisi `val amal = "/"` berilgan. `when (amal)` orqali barcha 4 arifmetik amalni bajaring (0 ga bo'lish xavfini `if (b == 0.0)` bilan tekshiring).

10. **Valyuta kursi va konvertatsiya · bonus**  
    Foydalanuvchi summa (`100.0`) va valyuta kodi (`"USD"`, `"EUR"`, `"RUB"`) kiritadi. `when` orqali mos kursga ko'paytirib, o'zbek so'midagi yakuniy summani chiqaring.
