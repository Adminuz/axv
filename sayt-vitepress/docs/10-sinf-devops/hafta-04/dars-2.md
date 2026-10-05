---
title: "11-dars. Shart operatorlari va mantiqiy ifodalar (if/elif/else, test, [[ ]], arifmetik amallar)"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (DevOps)", "link": "/10-sinf-devops/"}, "week": {"n": 4, "link": "/10-sinf-devops/hafta-04/"}, "g": 11, "title": "Shart operatorlari va mantiqiy ifodalar (if/elif/else, test, [[ ]], arifmetik amallar)", "lead": "Skriptingiz endi o'zi qaror qiladi: fayl bormi, son juftmi, parol uzunmi? Bugun skriptga «aql» kiritamiz.", "slide": "/slaydlar/10-sinf-devops/hafta-04/dars-2.html", "test": "/slaydlar/10-sinf-devops/hafta-04/dars-2-test.html", "tabs": [{"g": 10, "link": "/10-sinf-devops/hafta-04/dars-1", "current": false}, {"g": 11, "link": "/10-sinf-devops/hafta-04/dars-2", "current": true}, {"g": 12, "link": "/10-sinf-devops/hafta-04/dars-3", "current": false}], "prev": {"g": 10, "title": "Bash skripting asoslari: o'zgaruvchilar, argumentlar va kiritish/chiqarish (read, echo, printf)", "link": "/10-sinf-devops/hafta-04/dars-1"}, "next": {"g": 12, "title": "Sikllar va takrorlanishlar (for, while, until) hamda matnli oqimlarni qayta ishlash", "link": "/10-sinf-devops/hafta-04/dars-3"}}
---

---

<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- Har buyruq chiqish kodi qaytaradi: `0` muvaffaqiyat, boshqasi xato. Oxirgisi `$?` da.
- `test`, `[ ]` va `[[ ]]` shartni tekshiradi; qavs ichida bo'sh joylar shart.
- Son uchun `-eq -ne -lt -le -gt -ge`, matn uchun `= != -z -n`, fayl uchun `-e -f -d -r -w -x`.
- `if ... then ... elif ... else ... fi` tarmoqlanish beradi.
- `&&` (va), `||` (yoki), `!` (inkor) shartlarni birlashtiradi; `A && B`, `A || B` qisqa zanjir.
- Arifmetika: `$(( ))` va `(( ))`, amallar `+ - * / % **`; bo'lish butun sonli.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Shell uchun «rost» nima?
Boshqa tillarda `true/false` bor, shellda esa buyruq muvaffaqiyatli tugasa (kod 0) shart «rost». `if` aslida buyruqni ishga tushiradi va uning kodiga qaraydi. `[ ]` ham aslida buyruq (`test` ning boshqacha yozilishi), shuning uchun `[` dan keyin va `]` dan oldin bo'sh joy kerak.

### 2. `[ ]` bilan `[[ ]]` ning farqi
`[[ ]]` Bash'ga xos kengaytirilgan versiya: o'zgaruvchi atrofida tirnoq majburiy emas, ichida `&&`, `||` ishlaydi va naqsh bilan solishtiradi: `[[ $FAYL == *.txt ]]`. `[ ]` hamma shellda ishlaydi, lekin `"$A"` kabi tirnoq kerak bo'ladi.

### 3. `&&` va `||`: qisqa zanjirlar
O'quv qo'llanmada `apt update && apt upgrade -y` uchraydi: yangilash faqat indeks yangilangach boshlanadi. `[ -f x ] || echo "yo'q"` esa «yo'q bo'lsa xabar ber» degani. Skriptni ikki marta ishlatganda xato bermasligi (idempotentlik) uchun: `[ -d backup ] || mkdir backup`.

### 4. Odatiy xatolar
- `[ $A -eq 5 ]` da `A` bo'sh bo'lsa xato: `"$A"` yozing.
- Son uchun `=` yoki matn uchun `-eq` ishlatish.
- `if` ni `fi` bilan yopishni unutish.
- `$((7/2))` kasr emas, `3` beradi.

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Exit code** | Buyruq tugagach qaytaradigan son; 0 = muvaffaqiyat. |
| **`$?`** | Oxirgi buyruqning chiqish kodi. |
| **test / `[ ]`** | Shartni tekshiruvchi buyruq. |
| **`[[ ]]`** | Bash'ning kengaytirilgan shart ifodasi. |
| **if / elif / else** | Tarmoqlanish operatorlari, `fi` bilan tugaydi. |
| **Mantiqiy operator** | `&&`, `||`, `!`. |
| **Arifmetik kengaytma** | `$(( ))`: ichidagi hisobni bajaradi. |
| **Idempotentlik** | Amalni takror bajarish natijani o'zgartirmasligi. |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Shellda `0` «rost» hisoblanadi, chunki xatoning ko'p turi bor, muvaffaqiyat esa bitta.
- `[` aslida `/usr/bin/[` nomli oddiy dastur. Buni `type [` bilan ko'rish mumkin.
- Hujjatga ko'ra, deklarativ vositalar idempotent bo'ladi, oddiy skriptda esa bunga `if` bilan o'zingiz erishasiz.
- `RANDOM` o'zgaruvchisi har o'qilganda 0..32767 orasida tasodifiy son beradi.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Chiqish kodi <Badge type="tip" text="oson" />
`ls /tmp`, so'ng `echo $?`; keyin `ls /yoq_papka`, so'ng `echo $?`. Natijalarni solishtiring.

**Kutiladigan natija:** birinchisida `0`, ikkinchisida 0 emas.

### 2. Musbat yoki manfiy <Badge type="tip" text="oson" />
`read` bilan son oling; `if` bilan «musbat», «nol» yoki «manfiy» deb yozing.

**Kutiladigan natija:** uch xil kirishda uch xil javob.

### 3. Bashorat qiling <Badge type="tip" text="oson" />
Natijani oldindan ayting: `echo $((17/5)) $((17%5)) $((2**4))`.

**Kutiladigan natija:** uchta son; keyin terminalda tekshiring.

### 4. Xatoni toping <Badge type="tip" text="oson" />
`if [$A -eq 5]; then echo ok; fi` nega ishlamaydi?

**Kutiladigan natija:** bo'sh joylar yetishmasligi tushuntirilgan, to'g'ri variant yozilgan.

### 5. Fayl tekshiruvchi <Badge type="warning" text="o'rta" />
Argument bo'yicha berilgan nom fayl, papka yoki mavjud emasligini aytsin. Argument yo'q bo'lsa «Ishlatish: ...» deb chiqsin.

**Kutiladigan natija:** `./t.sh /etc` papka, `./t.sh /etc/hosts` fayl, boshqasi topilmadi.

### 6. Juft/toq <Badge type="warning" text="o'rta" />
`(( S % 2 == 0 ))` yordamida son juft yoki toqligini aniqlang.

**Kutiladigan natija:** 10 uchun juft, 7 uchun toq.

### 7. Parol uzunligi <Badge type="warning" text="o'rta" />
`read -s` bilan parol so'rang: 8 belgidan kam bo'lsa «qisqa», bo'lmasa «yaxshi» (`${#P}` uzunlikni beradi).

**Kutiladigan natija:** ikki xil javob.

### 8. Idempotent papka <Badge type="warning" text="o'rta" />
`loyiha` papkasi yo'q bo'lsa yarating, bor bo'lsa «bor» deb yozing. Skriptni 2 marta ishga tushiring.

**Kutiladigan natija:** ikkinchi ishga tushirishda xato chiqmaydi.

### 9. Baho hisoblagich <Badge type="danger" text="qiyin" />
Ball bo'yicha 5/4/3/2 baho bering (86+, 71-85, 56-70, qolgani); 0-100 dan tashqarisi uchun xato xabari.

**Kutiladigan natija:** chegara qiymatlar (55, 56, 70, 71, 85, 86) to'g'ri baholanadi.

### 10. Mini-loyiha: kalkulyator <Badge type="danger" text="qiyin" />
`./calc.sh 12 + 5` kabi 3 argumentni qabul qilsin (`+ - * /`), natijani chiqarsin; nolga bo'lishda xabar bersin.

**Kutiladigan natija:** to'rt amal ishlaydi, `./calc.sh 5 / 0` da «nolga bo'lib bo'lmaydi».

### 11. Tadqiqot: `[ ]` vs `[[ ]]` <Badge type="danger" text="qiyin" />
`F="a b"` bo'lganda `[ $F = "a b" ]` va `[[ $F = "a b" ]]` ni sinab, nega farq chiqishini yozing.

**Kutiladigan natija:** birinchisida xato, ikkinchisida ishlaydi; izoh.

### 12. Bonus: kun vaqti salomi <Badge type="info" text="bonus" />
`date +%H` bilan soatni olib, «Xayrli tong / kun / kech» deb salomlashadigan skript yozing (8 lik sanoq sistemasi xatosiga e'tibor bering: `$((10#$(date +%H)))`).

**Kutiladigan natija:** soatga mos salom.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Chiqish kodi 0 nimani anglatadi?
2. `[ ]` ichida nega bo'sh joylar shart?
3. `-eq` bilan `=` ning farqi nima?
4. `elif` nima uchun kerak?
5. `A && B` va `A || B` qachon B ni bajaradi?
6. `$((9/2))` nega 4?
7. `[ -z "$X" ]` nimani tekshiradi?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

`tekshir.sh` yozing: argument bo'yicha fayl turini aniqlasin, o'qish/yozish/bajarish ruxsatlarini (`-r -w -x`) ko'rsatsin va yo'q bo'lsa xato kodi 1 bilan chiqsin. Kutiladigan vaqt: 25 daqiqa.

</div>

