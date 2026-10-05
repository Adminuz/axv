---
title: "2-dars. Fayl ruxsatlari tizimi va matn tahrirlash vositalari (Nano, Vim)"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (DevOps)", "link": "/10-sinf-devops/"}, "week": {"n": 1, "link": "/10-sinf-devops/hafta-01/"}, "g": 2, "title": "Fayl ruxsatlari tizimi va matn tahrirlash vositalari (Nano, Vim)", "lead": "Linux xavfsizligining tayanchi bo'lgan ruxsatlar tizimi (ugo/rwx) va server ma'murlari quroli bo'lgan matn muharrirlari (Nano va Vim) sirlari.", "slide": "/slaydlar/10-sinf-devops/hafta-01/dars-2.html", "test": "/slaydlar/10-sinf-devops/hafta-01/dars-2-test.html", "tabs": [{"g": 1, "link": "/10-sinf-devops/hafta-01/dars-1", "current": false}, {"g": 2, "link": "/10-sinf-devops/hafta-01/dars-2", "current": true}, {"g": 3, "link": "/10-sinf-devops/hafta-01/dars-3", "current": false}], "prev": {"g": 1, "title": "Linux terminal va asosiy buyruqlar: FHS va fayllar tizimi bilan ishlash", "link": "/10-sinf-devops/hafta-01/dars-1"}, "next": {"g": 3, "title": "Shell muhiti, tizim o'zgaruvchilari va I/O yo'naltirish (Redirection)", "link": "/10-sinf-devops/hafta-01/dars-3"}}
---

---

<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- Linux — ko'p foydalanuvchili tizim bo'lib, har bir fayl va katalog qat'iy uchta toifaga bo'linadi: User (egasi), Group (guruh) va Others (begonalar).
- Ruxsat turlari uch xil bo'ladi: `r` (read — o'qish, 4), `w` (write — yozish/o'chirish, 2), `x` (execute — bajarish/katalogga kirish, 1).
- Ruxsatlarni belgilashda oktal (raqamli) usul keng qo'llaniladi: 755 (skriptlar uchun), 644 (oddiy fayllar uchun), 600 (maxfiy kalitlar uchun).
- DevOps amaliyotida «Least Privilege» (eng kam imtiyoz) tamoyili qo'llaniladi — hech qachon ishlab chiqarish fayllariga keraksiz `chmod 777` berilmaydi.
- `chmod` buyrug'i ruxsatlarni, `chown` buyrug'i fayl egasi va guruhini, `chgrp` esa faqat guruhni o'zgartiradi.
- Serverlarda GUI bo'lmagani sababli konfiguratsiyalarni tahrirlash uchun terminal muharrirlari — `nano` (sodda) va `vim` (modal, professional) ishlatiladi.
- Vim uchta asosiy rejimda ishlaydi: Normal (harakat va buyruqlar), Insert (matn yozish) va Command-line (saqlash va chiqish).

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Ruxsatlarni hisoblashning ikkilik (Binary) mantig'i
Nega aynan 4, 2, 1 raqamlari tanlangan? Chunki bu kompyuter arxitekturasidagi ikkilik (binary) sanoq tizimidir:
- Read (`r`) — 1-bit (`100` ikkilikda = 4 o'nlikda)
- Write (`w`) — 2-bit (`010` ikkilikda = 2 o'nlikda)
- Execute (`x`) — 3-bit (`001` ikkilikda = 1 o'nlikda)
Bularning kombinatsiyasi har doim yagona va takrorlanmas raqamni beradi:
- `r + w = 4 + 2 = 6` (`110`)
- `r + x = 4 + 1 = 5` (`101`)
- `r + w + x = 4 + 2 + 1 = 7` (`111`)

### 2. Kataloglar uchun `x` (bajarish) ruxsatining nozikligi
Ko'pchilik yangi o'rganuvchilar kataloglarni «dastur emas-ku, nega ularga execute beriladi?» deb o'ylashadi.
- Agar katalogda `r` (o'qish) bo'lsa, siz uning ichidagi fayllar ro'yxatini (`ls`) ko'ra olasiz.
- Lekin agar katalogda `x` (execute) bo'lmasa, siz `cd` buyrug'i bilan uning ichiga kira olmaysiz va ichidagi biror faylni o'qiy olmaysiz! Shuning uchun kataloglar uchun minimal standart ruxsat doimo `755` yoki `750` bo'ladi.

### 3. Ramziy (Symbolic) usul: qachon qulay?
Raqamlar butun triadaga birvarakayiga ta'sir qilsa, ramziy usul faqat bitta huquqni aniq qo'shish yoki olib tashlashda qulay:
- `chmod +x deploy.sh` — barcha toifalarga (u, g, o) tezda bajarish huquqini qo'shadi.
- `chmod g-w config.yml` — guruh a'zolaridan faqat yozish huquqini olib tashlaydi, qolgan huquqlarga tegmaydi.
- `chmod u=rwx,go=rx test.sh` — egasiga to'liq, qolganlarga faqat o'qish va bajarish huquqini belgilaydi.

### 4. Vim dunyosida omon qolish qoidalari
Vim dastlab chalkash tuyulishi mumkin, lekin uning falsafasini tushunsangiz, klaviaturadan qo'lni uzmay sekundiga tahrir qilasiz:
- `vim fayl.txt` bilan ochganingizda, siz **Normal** rejimdasiz. Shoshilib klaviaturani bosmang!
- `i` tugmasini bosing — ekranning chap pastida `-- INSERT --` paydo bo'ladi. Endi matn yoza olasiz.
- Yozib bo'lgach, har doim `Esc` ni bosing (yana Normal rejimga qaytasiz).
- Normal rejimda `:` tugmasini bosing va `wq` (write and quit) deb yozib Enter bosing.
- Agar biror narsani buzib qo'ysangiz va saqlamay chiqmoqchi bo'lsangiz: `Esc` → `:q!` → Enter.

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Chmod (Change Mode)** | Fayl yoki katalogning kirish ruxsatlari rejimini o'zgartiruvchi buyruq. |
| **Chown (Change Owner)** | Fayl yoki katalog egasi va unga biriktirilgan guruhni o'zgartiruvchi buyruq. |
| **User (u)** | Faylni yaratgan yoki uning mulkdori hisoblangan foydalanuvchi hisob qaydnomasi. |
| **Group (g)** | Bir xil loyiha yoki resurs ustida ishlaydigan foydalanuvchilar to'plami. |
| **Others (o)** | Tizimda mavjud bo'lgan, lekin fayl egasi ham, belgilangan guruh a'zosi ham bo'lmagan foydalanuvchilar. |
| **Least Privilege** | Axborot xavfsizligida subyektga faqat o'z vazifasini bajarishi uchun zarur bo'lgan minimal huquqlarni berish qoidasi. |
| **Normal Mode** | Vim muharririda ochilish rejim bo'lib, unda matn terilmaydi, harakat va matn bloklari ustida amallar bajariladi. |
| **Insert Mode** | Vim muharririda bevosita yangi matn kiritish va tahrirlash imkonini beruvchi rejim. |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Stack Overflow so'rovnomalariga ko'ra, har yili millionlab dasturchilar «How to exit Vim?» (Vim'dan qanday chiqiladi?) savolini qidiradi.
- Linuxda `root` foydalanuvchisi har qanday faylning ruxsati `000` qilib qulflangan bo'lsa ham uni bemalol o'qiy oladi va o'zgartira oladi.
- Vim dasturi 1991-yilda Bram Moolenaar tomonidan Commodore Amiga kompyuterlari uchun yaratilgan va u to'liq xayriya loyihasi sifatida rivojlantirilgan.
- `chmod 777` buyrug'i DevOps olamida eng katta xavfsizlik antipatterni hisoblanadi va «devops gunohlari» ro'yxatida birinchi o'rinda turadi.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Fayl ruxsatlarini tahlil qilish <Badge type="tip" text="oson" />
Terminalda `touch test_perm.txt` buyrug'i bilan fayl yarating va `ls -l test_perm.txt` orqali uning egasi, guruhi va dastlabki ruxsatlarini aniqlang.
**Kutiladigan natija:** `-rw-r--r--` ko'rinishidagi 9 ta ruxsat biti va foydalanuvchi nomi ko'rinadi.

### 2. Ramziy usulda bajarish huquqini berish <Badge type="tip" text="oson" />
`chmod +x test_perm.txt` buyrug'i orqali faylga bajarish huquqini qo'shing va `ls -l` bilan ruxsatning o'zgarganini tasdiqlang.
**Kutiladigan natija:** Ruxsatlar qatorida `x` harflari paydo bo'ladi (`-rwxr-xr-x`).

### 3. Nano muharririda oddiy fayl yozish <Badge type="tip" text="oson" />
`nano welcome.txt` orqali yangi fayl oching, ichiga «DevOps kursiga xush kelibsiz!» deb yozing, `Ctrl+O` bilan saqlab, `Ctrl+X` bilan chiqing.
**Kutiladigan natija:** `cat welcome.txt` bajarilganda yozilgan matn ekranga chiqadi.

### 4. Boshqalardan o'qish huquqini olib tashlash <Badge type="tip" text="oson" />
`chmod o-r test_perm.txt` buyrug'ini bajarib, «Others» (begonalar) toifasidan o'qish ruxsatini bekor qiling.
**Kutiladigan natija:** Oxirgi uchta belgi `---` ga aylanadi.

### 5. Oktal usulda 755 ruxsatini berish <Badge type="warning" text="o'rta" />
`deploy_app.sh` nomli yangi skript fayli yarating va unga raqamli oktal notation orqali aynan `755` ruxsatini biriktiring.
**Kutiladigan natija:** Fayl ruxsatlari aniq `-rwxr-xr-x` ko'rinishiga keladi.

### 6. Maxfiy fayl uchun 600 ruxsatini sozlash <Badge type="warning" text="o'rta" />
`private_key.pem` nomli fayl yarating va unga faqat fayl egasi o'qiy oladigan va yoza oladigan (`600`) qilib cheklov o'rnating.
**Kutiladigan natija:** `ls -l` ko'rsatganda `-rw-------` ruxsati aks etadi.

### 7. Vim'da birinchi konfiguratsiya fayli <Badge type="warning" text="o'rta" />
`vim server.conf` orqali fayl oching. `i` ni bosib Insert rejimga o'ting va `PORT=8080` qatorini yozing. So'ng `Esc` bosib, `:wq` orqali saqlab chiqing.
**Kutiladigan natija:** Fayl muvaffaqiyatli saqlanadi va `cat server.conf` orqali o'qiladi.

### 8. Rekursiv ruxsatlarni o'zgartirish <Badge type="warning" text="o'rta" />
`app_data` papkasini yarating va ichiga bir nechta fayl joylang. `chmod -R 750 app_data` buyrug'i bilan butun papka va uning ichidagilariga birvarakayiga ruxsat bering.
**Kutiladigan natija:** `ls -la app_data` papkaning barcha elementlari `rwxr-x---` bo'lganini ko'rsatadi.

### 9. Vim'da qatorlarni boshqarish amaliyoti <Badge type="danger" text="qiyin" />
`vim practice.txt` faylini oching, unga 5 ta ixtiyoriy qator yozing. So'ng Normal rejimda `dd` orqali 3-qatorni o'chiring, `yy` bilan 1-qator nusxasini oling va `p` orqali pastga qo'ying.
**Kutiladigan natija:** Normal rejimning tahrirlash buyruqlari amalda sinab ko'riladi.

### 10. Foydalanuvchi va guruhni o'zgartirish <Badge type="danger" text="qiyin" />
`sudo chown` buyrug'idan foydalanib, `test_perm.txt` faylining guruhini mavjud boshqa guruhga o'zgartiring (masalan, `nogroup` yoki `adm`).
**Kutiladigan natija:** `ls -l` ro'yxatida guruh ustuni yangilanganini ko'rasiz.

### 11. Murakkab ruxsatlar kombinatsiyasi testi <Badge type="info" text="bonus" />
Bitta katalog yarating, unga `chmod 644` (ya'ni `x` ruxsatisiz) bering va uning ichiga `cd` bilan kirishga urinib ko'ring. Terminal nima xatolik berishini tahlil qiling va uni bartaraf eting.
**Kutiladigan natija:** «Permission denied» xatosi yuzaga keladi, so'ngra `chmod +x` orqali katalogga kirish imkoniyati tiklanadi.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. `chmod 755` bilan `chmod 644` ning qanday amaliy farqlari bor va qaysi biri qachon ishlatiladi?
2. Nima uchun kataloglar uchun `x` (execute) huquqi berilmasa, uning ichiga `cd` qilib kirib bo'lmaydi?
3. Ramziy usulda `u`, `g`, `o`, `a` harflari kimlarni anglatadi?
4. Vim muharririda Normal, Insert va Command-line rejimlariga qanday o'tiladi?
5. `sudo chown user:group filename` buyrug'i tizimda aynan qanday o'zgarish yasaydi?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Linux terminalingizda `scripts` nomli katalog yarating. Uning ichida `backup.sh` va `clean.sh` nomli ikkita fayl oching. `nano` yoki `vim` yordamida har bir fayl ichiga `echo "Ishga tushdi"` satrini yozing. Skriptlarga faqat egasi va guruhiga bajarish ruxsatini bering (`750`). So'ngra `./backup.sh` buyrug'i orqali skriptni ishga tushirib ko'ring. Barcha qadamlarni daftaringizga qayd eting (taxminiy vaqt: 25 daqiqa).

</div>

