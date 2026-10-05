# 4-hafta: Uyga vazifalar (DevOps)

4-haftada Bash skriptingning asoslari o'rganildi: skript fayli, o'zgaruvchilar va argumentlar, kiritish/chiqarish (`read`, `echo`, `printf`), shart operatorlari (`if/elif/else`, `test`, `[[ ]]`, arifmetika) hamda sikllar (`for`, `while`, `until`) va matnli oqimlarni qayta ishlash. Quyidagi topshiriqlar shu ko'nikmalarni mustahkamlaydi.

---

## 10-dars vazifasi: Bash skripting asoslari

1. `profil.sh` nomli skript yarating (birinchi qatorda `#!/bin/bash`).
2. Ism va yoshni argument (`$1`, `$2`) yoki `read -p` orqali oling.
3. `$USER`, `$(date +%F)` va `$(ls | wc -l)` qiymatlarini oling.
4. Hammasini `printf` bilan tartibli hisobot qilib chiqaring.
5. `chmod +x profil.sh` qilib ishga tushiring va natijani daftaringizga yozing.
*(Kutiladigan vaqt: 25 daqiqa)*

---

## 11-dars vazifasi: Shart operatorlari

1. `tekshir.sh` skriptini yozing: argument sifatida nom oladi.
2. Nom fayl (`-f`), papka (`-d`) yoki mavjud emasligini aniqlab xabar bering.
3. Fayl bo'lsa, o'qish, yozish va bajarish ruxsatlari (`-r`, `-w`, `-x`) bormi, alohida qatorda ko'rsating.
4. Argument berilmasa «Ishlatish: ...» deb yozib, `exit 1` bilan chiqing.
5. Skriptni 3 xil kirish bilan sinab, natijalarni daftaringizga yozing.
*(Kutiladigan vaqt: 25 daqiqa)*

---

## 12-dars vazifasi: Sikllar va matnli oqimlar

1. `royxat.txt` fayliga 8-10 ta qator yozing (ba'zilari takrorlansin).
2. `hisobot.sh` skriptida `while read -r` bilan qatorlarni raqamlab chiqaring.
3. `sort | uniq | wc -l` bilan noyob qatorlar sonini toping.
4. Qo'shimcha: `uniq -c` bilan eng ko'p takrorlangan qatorni aniqlang.
5. Natijalarni daftaringizga yozing.
*(Kutiladigan vaqt: 25 daqiqa)*

---

## Mentor uchun

- **Tekshirish mezonlari:**
  1. Skriptda shebang, `chmod +x` va to'g'ri ishga tushirish bor.
  2. O'zgaruvchi va tirnoqlar to'g'ri ishlatilgan (tenglik atrofida bo'sh joy yo'q).
  3. `if/elif/else` va qavs ichidagi bo'sh joylar to'g'ri; son va matn operatorlari adashtirilmagan.
  4. Sikl to'g'ri tugaydi (cheksiz sikl yo'q), `done < fayl` ishlatilgan.
  5. `sort` dan keyin `uniq` quvuri to'g'ri.
- **Tez-tez uchraydigan xatolar:**
  - `NOM = "Ali"` yozish; `Permission denied` ni `chmod +x` bilan bog'lamaslik.
  - `[ $A -eq 5 ]` da bo'sh joy yoki tirnoq yetishmasligi.
  - Siklda hisoblagichni oshirishni unutish.
  - `sort` siz `uniq` ishlatish.
