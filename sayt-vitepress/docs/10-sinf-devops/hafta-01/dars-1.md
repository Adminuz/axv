---
title: "1-dars. Linux terminal va asosiy buyruqlar: FHS va fayllar tizimi bilan ishlash"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (DevOps)", "link": "/10-sinf-devops/"}, "week": {"n": 1, "link": "/10-sinf-devops/hafta-01/"}, "g": 1, "title": "Linux terminal va asosiy buyruqlar: FHS va fayllar tizimi bilan ishlash", "lead": "Linux terminali — DevOps muhandisining eng asosiy quroli: serverlarni boshqarish, fayllar daraxti (FHS) bo'ylab chaqqon harakatlanish va tizimni avtomatlashtirishning poydevori.", "slide": "/slaydlar/10-sinf-devops/hafta-01/dars-1.html", "test": "/slaydlar/10-sinf-devops/hafta-01/dars-1-test.html", "tabs": [{"g": 1, "link": "/10-sinf-devops/hafta-01/dars-1", "current": true}, {"g": 2, "link": "/10-sinf-devops/hafta-01/dars-2", "current": false}, {"g": 3, "link": "/10-sinf-devops/hafta-01/dars-3", "current": false}], "prev": null, "next": {"g": 2, "title": "Fayl ruxsatlari tizimi va matn tahrirlash vositalari (Nano, Vim)", "link": "/10-sinf-devops/hafta-01/dars-2"}}
---

---

<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- Linux — zamonaviy bulut platformalari, serverlar va konteynerlashtirilgan ilovalarning 90% dan ortig'ini boshqaruvchi asosiy operatsion tizim hisoblanadi.
- Serverlarda resurslarni tejash va xavfsizlikni oshirish maqsadida grafik interfeys (GUI) o'rniga buyruqlar satri (CLI) ishlatiladi.
- Linux fayl tizimi yagona ildiz (`/`) ostida daraxtsimon ierarxiya (FHS) ko'rinishida tuzilgan bo'lib, unda disk drayvlari harflari (masalan, `C:`, `D:`) mavjud emas.
- «Hamma narsa — bu fayl» tamoyili asosida konfiguratsiyalar (`/etc`), loglar (`/var/log`), jarayonlar (`/proc`) va hatto apparat qurilmalari (`/dev`) fayl ko'rinishida taqdim etiladi.
- `pwd`, `cd`, `ls`, `mkdir`, `touch`, `cp`, `mv`, `rm` kabi asosiy utilitalar tizim boshqaruvining fundamental amallarini tashkil etadi.
- Linuxdagi buyruqlar odatda `buyruq [opsiyalar] [argumentlar]` shaklida chaqiriladi va ularni o'zaro zanjir qilib birlashtirish mumkin.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Terminal arxitekturasi: Ekranda nimalar sodir bo'ladi?
Ko'pchilik foydalanuvchilar qora oynani shunchaki «terminal» deb atashadi. Aslida u uchta mustaqil dasturning uzluksiz hamkorligidir:
1. **Terminal emulyatori** (masalan, GNOME Terminal, Alacritty, iTerm2): klaviaturadagi tugmalarni tutib oladi va ekranda matnli grafika hosil qiladi.
2. **Shell** (masalan, Bash, Zsh): foydalanuvchi yozgan satrni (prompt) o'qiydi, sintaktik bo'laklarga ajratadi, o'zgaruvchilarni almashtiradi va kerakli dasturni topib ishga tushiradi.
3. **Linux yadrosi (Kernel)**: dastur so'ragan tizim chaqiruvlarini (system calls) apparat vositalari (xotira, protsessor, disk) darajasida amalga oshiradi.

### 2. Mutlaq va nisbiy yo'llar (Absolute vs Relative Path)
Linuxda har qanday fayl yoki katalogga murojaat qilishning ikki usuli mavjud:
- **Mutlaq yo'l (Absolute path)**: Doimo eng yuqori ildiz — `/` katalogidan boshlanadi. Masalan: `/var/log/nginx/access.log`. Siz fayl tizimining qaysi burchagida turishingizdan qat'i nazar, mutlaq yo'l har doim bitta aniq manzilga olib boradi.
- **Nisbiy yo'l (Relative path)**: Siz hozir turgan joriy ishchi katalogga (`pwd`) nisbatan hisoblanadi. Unda quyidagi maxsus belgilar qo'llaniladi:
  - `.` (bitta nuqta) — joriy katalog.
  - `..` (ikkita nuqta) — bitta yuqoridagi ota katalog.
  - Masalan, agar siz `/home/devops` ichida bo'lsangiz, `cd ../ali` buyrug'i sizni `/home/ali` katalogiga olib boradi.

### 3. FHS tizimining muhim kataloglari va ularning DevOps'dagi o'rni
- `/etc` — butun tizim sozlamalari markazi. Masalan, Docker daemon konfiguratsiyasi `/etc/docker/daemon.json`, tarmoq sozlamalari yoki Nginx veb-server sozlamalari aynan shu yerda joylashadi.
- `/var/log` — barcha xizmatlarning faoliyat jurnallari. DevOps muhandisi nosozliklarni qidirganda (troubleshooting) birinchi bo'lib shu katalogni ochadi.
- `/tmp` — vaqtinchalik ma'lumotlar saqlanadigan joy. Server qayta yuklanganda uning ichi avtomatik tozalanadi.
- `/opt` — uchinchi tomon yirik dasturiy ta'minotlari o'rnatiladigan katalog.

### 4. `rm` buyrug'i bilan ishlashda xavfsizlik madaniyati
Linuxda o'chirilgan fayllar Windows'dagi kabi «Savatcha»ga (Recycle Bin) tushmaydi — ular darhol disk bloklaridan uziladi va qayta tiklash juda qiyinlashadi. Ayniqsa `rm -rf` buyrug'idan foydalanganda yo'lning to'g'riligini doimo ikki marta tekshirish qat'iy talab etiladi.

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **CLI (Command Line Interface)** | Foydalanuvchi buyruqlarni klaviatura orqali matn shaklida kiritadigan boshqaruv interfeysi. |
| **Shell** | Foydalanuvchi kiritgan matnli buyruqlarni operatsion tizim yadrosiga yetkazuvchi dastur (interpretator). |
| **FHS (Filesystem Hierarchy Standard)** | Linux va Unix operatsion tizimlarida fayl va kataloglarning yagona joylashuv tartibini belgilovchi standart. |
| **Root (`/`)** | Linux fayllar tizimining eng yuqori boshlang'ich nuqtasi bo'lgan ildiz katalog. |
| **Superuser (root)** | Linux operatsion tizimida cheklanmagan mutlaq boshqaruv huquqiga ega bo'lgan bosh administrator foydalanuvchi. |
| **PWD (Print Working Directory)** | Foydalanuvchi hozirda turgan joriy ishchi katalogni to'liq mutlaq yo'l bilan ko'rsatuvchi buyruq. |
| **Timestamp** | Faylning yaratilgan, oxirgi marta o'zgartirilgan yoki ochilgan vaqtini belgilovchi metadata tamg'asi. |
| **Recursive (`-r`)** | Buyruqni katalogning o'ziga hamda uning ichidagi barcha quyi papkalar va fayllarga ketma-ket tatbiq etish usuli. |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Dunyodagi eng kuchli TOP-500 superkompyuterlarning 100 foizi aynan Linux operatsion tizimida ishlaydi.
- Linux yadrosi 1991-yilda 21 yoshli talaba Linus Torvalds tomonidan shaxsiy qiziqish sifatida yaratilgan bo'lib, bugungi kunda uning kod bazasi 30 million qatordan oshib ketgan.
- Mars planetasida harakatlanuvchi NASA roverlari (masalan, Perseverance va Ingenuity vertolyoti) ham Linux boshqaruvida parvoz qilmoqda.
- `cat` buyrug'ining nomi mushukka hech qanday aloqador emas — u inglizcha «concatenate» (birlashtirish) so'zining qisqartmasidir.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Joriy manzilni aniqlash <Badge type="tip" text="oson" />
Terminalni oching va `pwd` buyrug'i yordamida joriy ishchi katalogingizning mutlaq yo'lini aniqlang.
**Kutiladigan natija:** Ekranda `/home/username` ko'rinishidagi mutlaq yo'l chiqadi.

### 2. Yashirin fayllarni ko'rish <Badge type="tip" text="oson" />
O'z uy katalogingiz tarkibini barcha yashirin (nuqta bilan boshlanuvchi) fayllari bilan birga ekranga chiqaring.
**Kutiladigan natija:** `.bashrc`, `.profile` kabi fayllarni o'z ichiga olgan to'liq ro'yxat aks etadi.

### 3. Yangi bo'sh fayl yaratish <Badge type="tip" text="oson" />
`touch` buyrug'i yordamida joriy katalogda `devops_notes.txt` nomli yangi fayl hosil qiling va `ls -l` orqali uning o'lchami 0 bayt ekanligini ko'ring.
**Kutiladigan natija:** Fayllar ro'yxatida `devops_notes.txt` paydo bo'ladi.

### 4. Ota katalogga o'tish va qaytish <Badge type="tip" text="oson" />
Nisbiy yo'l yordamida bitta yuqori katalogga chiqing (`cd ..`), manzilni `pwd` bilan tekshiring va oldingi katalogga tezkor qaytish buyrug'ini bajaring.
**Kutiladigan natija:** Oldingi katalogga muvaffaqiyatli qaytiladi.

### 5. Ko'p qatlamli kataloglar daraxtini yaratish <Badge type="warning" text="o'rta" />
Yagona buyruq yordamida `cloud/infrastructure/terraform` va `cloud/infrastructure/ansible` papkalar zanjirini yarating.
**Kutiladigan natija:** `mkdir -p` orqali barcha ota va bola kataloglar bir martada hosil qilinadi.

### 6. Faylni boshqa nom bilan nusxalash <Badge type="warning" text="o'rta" />
`devops_notes.txt` faylini `cloud/infrastructure/` papkasi ichiga `backup_notes.txt` nomi bilan nusxalang.
**Kutiladigan natija:** Ko'rsatilgan manzil ichida yangi nomli fayl nusxasi paydo bo'ladi.

### 7. Faylni ko'chirish va qayta nomlash <Badge type="warning" text="o'rta" />
`backup_notes.txt` faylini `ansible` papkasining ichiga ko'chiring va uning nomini `hosts.ini` deb o'zgartiring.
**Kutiladigan natija:** `mv` buyrug'i natijasida fayl yangi joyda va yangi nom bilan saqlanadi.

### 8. Fayllarni o'lchami bo'yicha saralash <Badge type="warning" text="o'rta" />
`/etc` katalogi ichidagi barcha fayllarni ularning hajmiga qarab inson tushunadigan formatda kamayish tartibida ekranga chiqaring.
**Kutiladigan natija:** Eng katta konfiguratsiya fayllari ro'yxatning yuqori qismida ko'rinadi (`ls -lhS`).

### 9. Log fayllarini avtomat qidirish <Badge type="danger" text="qiyin" />
`find` buyrug'idan foydalanib, butun tizim bo'ylab (yoki uy katalogingizda) oxirgi 24 soat ichida o'zgartirilgan barcha `.log` fayllarini toping.
**Kutiladigan natija:** Qidiruv mezonlariga mos keluvchi log fayllarining mutlaq yo'llari ro'yxati chiqadi.

### 10. Tozalash va xavfsiz o'chirish <Badge type="danger" text="qiyin" />
Avval yaratilgan `cloud` katalogini va uning ichidagi barcha fayllarni birgina rekursiv buyruq bilan to'liq o'chirib tashlang, so'ngra uning yo'qligini tekshiring.
**Kutiladigan natija:** Papka butunlay o'chiriladi va unga murojaat qilinganda «No such file or directory» xabari chiqadi.

### 11. Bo'sh kataloglarni qidirib topish <Badge type="info" text="bonus" />
Linuxda `find` buyrug'ining maxsus parametrlaridan foydalanib, faqatgina bo'sh (ichida hech qanday fayl bo'lmagan) kataloglarni qidirib topuvchi buyruqni tuzing.
**Kutiladigan natija:** `-type d -empty` flaglari yordamida tizimdagi bo'sh papkalar ro'yxati aniqlanadi.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Linux fayl tizimida `/` belgisi bilan Windows'dagi `\` belgisining farqi nimada?
2. `ls` buyrug'iga beriladigan `-l`, `-a` va `-h` flaglarining har biri qanday vazifani bajaradi?
3. Fayl tizimida `.` va `..` belgilari nimani anglatadi va ular amalda qayerda kerak bo'ladi?
4. `/var` katalogi nima uchun serverlarda alohida disk bo'limiga ajratiladi?
5. `cp` va `mv` buyruqlarining asosiy farqi nimada?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

O'z kompyuteringizdagi Linux terminalida (yoki WSL/VirtualBox muhitida) o'z ismingiz bilan nomlangan asosiy papka oching. Uning ichida `projects`, `docs` va `backups` papkalarini yarating. Har bir papkada bittadan matnli fayl yaratib, ularni bir-biriga nusxalash va ko'chirish amallarini bajaring. Bajargan barcha buyruqlaringiz tarixini (`history` buyrug'i orqali) konspekt daftaringizga qayd eting (taxminiy vaqt: 25 daqiqa).

</div>

