---
title: "4-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "10-sinf (DevOps)", "link": "/10-sinf-devops/"}, "n": 4, "bob": "III-bob · Kompyuter tarmoqlari", "lessons": [{"g": 10, "title": "Bash skripting asoslari: o'zgaruvchilar, argumentlar va kiritish/chiqarish (read, echo, printf)", "lead": "Bugun terminaldagi buyruqlarni faylga yig'ib, o'zingizning birinchi avtomatlashtirilgan skriptingizni yaratasiz: u ismingizni so'raydi, argument qabul qiladi va chiroyli hisobot chiqaradi.", "link": "/10-sinf-devops/hafta-04/dars-1", "slide": "/slaydlar/10-sinf-devops/hafta-04/dars-1.html", "test": "/slaydlar/10-sinf-devops/hafta-04/dars-1-test.html"}, {"g": 11, "title": "Shart operatorlari va mantiqiy ifodalar (if/elif/else, test, [[ ]], arifmetik amallar)", "lead": "Skriptingiz endi o'zi qaror qiladi: fayl bormi, son juftmi, parol uzunmi? Bugun skriptga «aql» kiritamiz.", "link": "/10-sinf-devops/hafta-04/dars-2", "slide": "/slaydlar/10-sinf-devops/hafta-04/dars-2.html", "test": "/slaydlar/10-sinf-devops/hafta-04/dars-2-test.html"}, {"g": 12, "title": "Sikllar va takrorlanishlar (for, while, until) hamda matnli oqimlarni qayta ishlash", "lead": "Kompyuter charchamaydi: 1000 marta takrorlash unga bir qator. Bugun sikllar va quvurlar bilan matnli ma'lumotni «tegirmon» kabi ishlaymiz.", "link": "/10-sinf-devops/hafta-04/dars-3", "slide": "/slaydlar/10-sinf-devops/hafta-04/dars-3.html", "test": "/slaydlar/10-sinf-devops/hafta-04/dars-3-test.html"}], "test": "/slaydlar/10-sinf-devops/hafta-04/hafta-test.html"}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

4-haftada Bash skriptingning asoslari o'rganildi: skript fayli, o'zgaruvchilar va argumentlar, kiritish/chiqarish (`read`, `echo`, `printf`), shart operatorlari (`if/elif/else`, `test`, `[[ ]]`, arifmetika) hamda sikllar (`for`, `while`, `until`) va matnli oqimlarni qayta ishlash. Quyidagi topshiriqlar shu ko'nikmalarni mustahkamlaydi.

---

### 10-dars vazifasi: Bash skripting asoslari

1. `profil.sh` nomli skript yarating (birinchi qatorda `#!/bin/bash`).
2. Ism va yoshni argument (`$1`, `$2`) yoki `read -p` orqali oling.
3. `$USER`, `$(date +%F)` va `$(ls | wc -l)` qiymatlarini oling.
4. Hammasini `printf` bilan tartibli hisobot qilib chiqaring.
5. `chmod +x profil.sh` qilib ishga tushiring va natijani daftaringizga yozing.
*(Kutiladigan vaqt: 25 daqiqa)*

---

### 11-dars vazifasi: Shart operatorlari

1. `tekshir.sh` skriptini yozing: argument sifatida nom oladi.
2. Nom fayl (`-f`), papka (`-d`) yoki mavjud emasligini aniqlab xabar bering.
3. Fayl bo'lsa, o'qish, yozish va bajarish ruxsatlari (`-r`, `-w`, `-x`) bormi, alohida qatorda ko'rsating.
4. Argument berilmasa «Ishlatish: ...» deb yozib, `exit 1` bilan chiqing.
5. Skriptni 3 xil kirish bilan sinab, natijalarni daftaringizga yozing.
*(Kutiladigan vaqt: 25 daqiqa)*

---

### 12-dars vazifasi: Sikllar va matnli oqimlar

1. `royxat.txt` fayliga 8-10 ta qator yozing (ba'zilari takrorlansin).
2. `hisobot.sh` skriptida `while read -r` bilan qatorlarni raqamlab chiqaring.
3. `sort | uniq | wc -l` bilan noyob qatorlar sonini toping.
4. Qo'shimcha: `uniq -c` bilan eng ko'p takrorlangan qatorni aniqlang.
5. Natijalarni daftaringizga yozing.
*(Kutiladigan vaqt: 25 daqiqa)*

---

</div>
