---
title: "10-dars. Bash skripting asoslari: o'zgaruvchilar, argumentlar va kiritish/chiqarish (read, echo, printf)"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (DevOps)", "link": "/10-sinf-devops/"}, "week": {"n": 4, "link": "/10-sinf-devops/hafta-04/"}, "g": 10, "title": "Bash skripting asoslari: o'zgaruvchilar, argumentlar va kiritish/chiqarish (read, echo, printf)", "lead": "Bugun terminaldagi buyruqlarni faylga yig'ib, o'zingizning birinchi avtomatlashtirilgan skriptingizni yaratasiz: u ismingizni so'raydi, argument qabul qiladi va chiroyli hisobot chiqaradi.", "slide": "/slaydlar/10-sinf-devops/hafta-04/dars-1.html", "test": "/slaydlar/10-sinf-devops/hafta-04/dars-1-test.html", "tabs": [{"g": 10, "link": "/10-sinf-devops/hafta-04/dars-1", "current": true}, {"g": 11, "link": "/10-sinf-devops/hafta-04/dars-2", "current": false}, {"g": 12, "link": "/10-sinf-devops/hafta-04/dars-3", "current": false}], "prev": null, "next": {"g": 11, "title": "Shart operatorlari va mantiqiy ifodalar (if/elif/else, test, [[ ]], arifmetik amallar)", "link": "/10-sinf-devops/hafta-04/dars-2"}}
---

---

<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- Buyruqlar ketma-ketligini faylga yozib, shell orqali bajarish **shell scripting** deyiladi va jarayonlarni avtomatlashtiradi.
- Skriptning birinchi qatori `#!/bin/bash` (shebang) bo'ladi; `#` bilan boshlangan qator izoh.
- Ishga tushirish uchun `chmod +x skript.sh`, so'ng `./skript.sh`.
- O'zgaruvchi `NOM="qiymat"` ko'rinishida (tenglik atrofida bo'sh joy yo'q), ishlatish `$NOM`.
- `"..."` ichida `$` ishlaydi, `'...'` ichida matn o'zgarishsiz qoladi; `$(buyruq)` buyruq natijasini beradi.
- Argumentlar: `$0` skript nomi, `$1`, `$2` ... qiymatlar, `$#` soni, `$@` hammasi.
- `echo`, `printf` chiqaradi, `read` klaviaturadan o'qiydi.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Skript nima uchun kerak?
Tasavvur qiling, har kuni serverga 4 ta buyruq yozasiz: `apt update`, `apt install -y nginx`, konfiguratsiyani nusxalash, xizmatni qayta ishga tushirish. Biror qadamni unutsangiz, natija boshqacha bo'ladi. Skript bu qadamlarni bir marta yozib qo'yadi, keyin istalgancha bir xil natija bilan ishga tushiradi. O'quv qo'llanmada bu *imperativ yondashuv* deyiladi: qadamlar tartibi muhim.

### 2. Uch xil o'zgaruvchi
Qo'llanmaga ko'ra: **Local** (faqat joriy shellda), **Environment** (quyi jarayonlarga ham beriladi: `export PORT=8080`) va **Shell/System** (shellning o'zi yaratadi: `USER`, `HOME`, `PWD`, `SHELL`, `PATH`). Ularni `printenv` yoki `env` bilan ko'rasiz.
```bash
ISM="Ali"            # local
export PORT=8080     # environment
echo "$USER $HOME"   # system
```

### 3. Tirnoq nega muhim?
```bash
ISM="Ali Valiyev"
echo "Salom, $ISM"    # Salom, Ali Valiyev
echo 'Salom, $ISM'    # Salom, $ISM
```
Qo'sh tirnoq o'zgaruvchini ochadi, bitta tirnoq esa «qotirib qo'yadi». Qiymatda bo'sh joy bo'lsa, o'zgaruvchini ishlatganda ham `"$ISM"` deb yozing, aks holda shell uni bo'laklarga ajratadi.

### 4. Odatiy xatolar
- `NOM = "Ali"`: shell `NOM` ni buyruq deb o'ylaydi (`command not found`).
- `chmod +x` ni unutish: `Permission denied`.
- Shebang yo'q yoki imloviy xato: `#! /bin/bsh`.
- `echo "$SONta"` o'rniga `echo "${SON}ta"` kerak: nom qayerda tugashi aniq bo'lsin.

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Shell** | Foydalanuvchi va kernel o'rtasidagi buyruq interpretatori (masalan, bash). |
| **Shell scripting** | Buyruqlar ketma-ketligini faylga yozib, shell orqali bajarish. |
| **Shebang** | Skriptning birinchi qatori `#!/bin/bash`: qaysi dastur bilan ishga tushishini bildiradi. |
| **Variable** | Nomi bor qiymat: `NOM="qiymat"`. |
| **Environment variable** | Quyi jarayonlarga ham uzatiladigan o'zgaruvchi (`export`). |
| **Argument** | Skript chaqirilganda berilgan qiymat (`$1`, `$2`). |
| **stdin / stdout** | Kiritish oqimi (klaviatura) va chiqish oqimi (ekran). |
| **Command substitution** | `$(buyruq)`: buyruq natijasini matn sifatida qo'yish. |
| **chmod +x** | Faylga bajarish (execute) ruxsatini berish. |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Shebang so'zi ikki belgidan olingan: `#` (sharp) va `!` (bang).
- Bash nomi «Bourne Again Shell» degani: eski Bourne shell nomiga qilingan so'z o'yini.
- Linux serverlarining ko'pchiligi kunlik ishlarni (zaxira nusxa, log tozalash) aynan shunday kichik skriptlar bilan avtomatlashtiradi.
- `printf` nomi C tilidagi funksiyadan kelgan, shuning uchun `%s` va `%d` belgilari ikkala joyda ham bir xil.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Birinchi skript <Badge type="tip" text="oson" />
`salom.sh` yarating: shebang, bitta izoh va `echo` bilan o'z ismingizni chiqaring. `chmod +x` qilib ishga tushiring.

**Kutiladigan natija:** terminalda ismingiz chiqadi.

### 2. Bashorat qiling <Badge type="tip" text="oson" />
Bu kod nima chiqaradi?
```bash
A="Linux"
echo "Men $A ni yaxshi ko'raman"
echo 'Men $A ni yaxshi ko'raman'
```
**Kutiladigan natija:** ikki qatorning farqini oldindan yozing, keyin sinab tekshiring.

### 3. Xatoni toping <Badge type="tip" text="oson" />
`ISM = "Ali"` qatori nega ishlamaydi? Tuzating va xabarni o'qing.

**Kutiladigan natija:** xato xabari (`command not found`) va to'g'ri variant.

### 4. Tizim o'zgaruvchilari <Badge type="tip" text="oson" />
`$USER`, `$HOME`, `$PWD`, `$SHELL` qiymatlarini bitta skript bilan chiqaring.

**Kutiladigan natija:** 4 qator, har birida nom va qiymat.

### 5. Tanishuv skripti <Badge type="warning" text="o'rta" />
`read -p` bilan ism va yoshni so'rang, `printf` bilan `Ali, siz 16 yoshdasiz` ko'rinishida chiqaring.

**Kutiladigan natija:** formatli bitta qator.

### 6. Argumentlar <Badge type="warning" text="o'rta" />
`arg.sh` yozing: `$0`, `$1`, `$2`, `$#`, `$@` ni chiqarsin. `./arg.sh Ali 16` va `./arg.sh bir ikki uch to'rt` bilan sinang.

**Kutiladigan natija:** ikki xil chaqiruvda `$#` 2 va 4 bo'ladi.

### 7. Buyruq natijasi <Badge type="warning" text="o'rta" />
`$(date +%F)` va `$(ls | wc -l)` yordamida «Bugun 2026-... , papkada N ta fayl bor» deb yozadigan skript tuzing.

**Kutiladigan natija:** sana va fayllar soni bir jumlada.

### 8. Parolsiz emas <Badge type="warning" text="o'rta" />
`read -s` bilan «parol» so'rang va uni ekranga **chiqarmasdan** faqat uzunligini yozing (`${#PAROL}`).

**Kutiladigan natija:** terminalda parol ko'rinmaydi, `Uzunlik: 8` kabi chiqadi.

### 9. Mini-loyiha: profil.sh <Badge type="danger" text="qiyin" />
Ism, shahar, yoshni `read` bilan oling; `$USER`, sana, hostname (`$(hostname)`) bilan birga chiroyli «vizitka» chiqaring (`printf`).

**Kutiladigan natija:** 5-6 qatorli tartibli vizitka.

### 10. Argument yoki so'rash <Badge type="danger" text="qiyin" />
Agar ism argument sifatida berilsa shuni ishlating, berilmasa `read` bilan so'rang. (Maslahat: `${1}` bo'shmi? Keyingi darsda `if` ni o'rganasiz, hozircha `ISM="${1:-Mehmon}"` ni sinab ko'ring.)

**Kutiladigan natija:** `./s.sh Ali` da `Salom, Ali`, argumentsiz `Salom, Mehmon`.

### 11. Tadqiqot: printf formatlari <Badge type="danger" text="qiyin" />
`printf "%5s|%-5s|%05d\n" ab cd 42` ni sinab, har bir formatning nima qilishini o'z so'zingiz bilan tushuntiring.

**Kutiladigan natija:** 3 formatning izohi (o'ngga tekis, chapga tekis, nollar bilan to'ldirish).

### 12. Bonus: o'zgaruvchi chegarasi <Badge type="info" text="bonus" />
`SON=5` bo'lganda `echo "$SONta"`, `echo "${SON}ta"` ni solishtiring va nega farq borligini yozing.

**Kutiladigan natija:** birinchisi bo'sh, ikkinchisi `5ta`.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Shebang nima va nega birinchi qatorda turishi kerak?
2. `NOM="Ali"` va `NOM = "Ali"` ning farqi nimada?
3. Qo'sh va bitta tirnoq qanday farq qiladi?
4. `$#` va `$@` nimani bildiradi?
5. `echo` bilan `printf` ning asosiy farqi nima?
6. `read -p` va `read -s` nima uchun ishlatiladi?
7. `Permission denied` chiqsa nima qilasiz?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

`profil.sh` skriptini yozing: ism va yoshni argument yoki `read` orqali oling, `$USER`, sana va fayllar soni bilan birga `printf` yordamida tartibli hisobot chiqaring. Kutiladigan vaqt: 25 daqiqa.

</div>

