# 3-dars. Shell muhiti, tizim o'zgaruvchilari va I/O yo'naltirish (Redirection)

> Linux Shell qudrati: tizim o'zgaruvchilari (PATH, export), .bashrc sozlamalari hamda ma'lumot oqimlari (I/O Redirection va quvurlar) yordamida buyruqlarni zanjirga ulash.

---

## Dars xulosasi

- Shell — operatsion tizim yadrosi bilan aloqa o'rnatuvchi, buyruqlarni qabul qilib bajaruvchi kuchli interpretatordir (Bash, Zsh).
- Muhit o'zgaruvchilari (Environment Variables) tizim va dasturlarning ishlash parametrlarini (masalan, portlar, yo'llar, foydalanuvchi) saqlaydi.
- `$PATH` o'zgaruvchisi shell'ga buyruqlar qaysi papkalardan qidirilishi kerakligini aytadi; buyruq nomi to'liq yo'lsiz terilganda aynan `$PATH` tekshiriladi.
- Yangi o'zgaruvchi yaratilganda, uning barcha quyi jarayonlarda ishlashi uchun `export` buyrug'i bilan muhitga chiqariladi.
- Linuxda har bir jarayon 3 ta standart oqimga ega: STDIN (0, kirish), STDOUT (1, chiqish) va STDERR (2, xatolik).
- `>` operatori natijani faylga yangidan yozsa (overwrite), `>>` operatori mavjud fayl oxiriga qo'shadi (append).
- Quvurlar (`|` pipe) yordamida oraliq fayllarsiz bir buyruqning chiqishini ikkinchi buyruqning kirishiga to'g'ridan-to'g'ri uzatish mumkin.

---

## Qo'shimcha ma'lumot

### 1. `PATH` qanday ishlaydi va o'z skriptingizni qanday global qilish mumkin?
Agar siz `myscript.sh` faylini yaratgan bo'lsangiz, uni ishga tushirish uchun `./myscript.sh` deb yozishingiz shart, chunki joriy katalog odatda xavfsizlik sababli `$PATH` ichida bo'lmaydi.
Lekin agar siz uni doimiy ravishda istalgan joydan shunchaki `myscript` deb chaqirmoqchi bo'lsangiz:
1. Skriptingizni `/usr/local/bin` papkasiga nusxalang:
   `sudo cp myscript.sh /usr/local/bin/myscript`
2. Yoki o'z shaxsiy skriptlar papkangizni `~/.bashrc` faylida `$PATH` ga qo'shing:
   `export PATH="$PATH:$HOME/scripts"`
Shundan so'ng terminalni qayta ochsangiz yoki `source ~/.bashrc` qilsangiz, skriptingiz tizimning rasmiy buyrug'iga aylanadi!

### 2. Uchta oqim deskriptorlari (0, 1, 2)
Linuxda har bir oqimning o'z raqamli identifikatori (file descriptor) mavjud:
- `0` — STDIN: kiritish oqimi.
- `1` — STDOUT: standart chiqish oqimi. Masalan: `ls 1> files.txt` (odatda `1` yozilmaydi, shunchaki `> files.txt`).
- `2` — STDERR: standart xatolik oqimi. Masalan: `find /etc -name "*.conf" 2> errors.log`.
- Agar xatoliklar ekranni to'ldirib yuborishini xohlamasangiz, ularni «axlat qutisi»ga yo'naltirasiz:
  `command 2> /dev/null`

### 3. Piping (`|`) kuchi: Unix falsafasi amalda
Nega Linux utilitalari bunchalik kichik? Chunki ularni quvurlar orqali birlashtirganda har qanday murakkab masalani yechish mumkin:
Masalan: `ps aux | grep node | awk '{print $2}' | xargs kill -9`
Bu yagona satr:
1. Barcha ishlayotgan jarayonlarni oladi (`ps aux`).
2. Faqat `node` so'zi bor qatorlarni ajratadi (`grep node`).
3. Ularning PID raqamini ajratib oladi (`awk`).
4. Barcha olingan PID larni birdaniga to'xtatadi (`xargs kill -9`).
Buning uchun alohida dastur yozish shart emas!

### 4. Aliaslar: Barmoqlaringizni asrang!
Tez-tez ishlatiladigan uzun buyruqlarni qisqa laqablar bilan almashtirish qulay:
`alias cls='clear'`
`alias gs='git status'`
`alias ports='netstat -tulpn'`
Ushbu aliaslarni `~/.bashrc` oxiriga joylab qo'ysangiz, ular har doim saqlanib qoladi.

---

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Environment Variable** | Tizim, shell va ishga tushirilayotgan dasturlar foydalanadigan dinamik kalit-qiymat ma'lumoti. |
| **Export** | Mahalliy shell o'zgaruvchisini global muhit o'zgaruvchisiga aylantiruvchi buyruq. |
| **$PATH** | Shell buyruqlarni qidiradigan kataloglar ro'yxatini belgilovchi maxsus muhit o'zgaruvchisi. |
| **STDIN (Standard Input)** | Jarayonga ma'lumot kirituvchi standart kirish oqimi (deskriptor 0). |
| **STDOUT (Standard Output)** | Jarayonning muvaffaqiyatli natijasini chiqaruvchi standart chiqish oqimi (deskriptor 1). |
| **STDERR (Standard Error)** | Jarayon yuzaga keltirgan xatolik xabarlarini chiqaruvchi oqim (deskriptor 2). |
| **Pipe (`|`)** | Bir jarayonning chiqishini boshqa jarayonning kirishiga xotira orqali ulovchi vertikal belgi. |
| **Redirection (`>`, `>>`)** | Standart kirish/chiqish oqimlarini fayllar tomon yo'naltirish mexanizmi. |
| **Alias** | Uzun va murakkab terminal buyruqlariga beriladigan qisqa taxallus. |
| **/dev/null** | Unga yuborilgan har qanday ma'lumotni izsiz yo'qotuvchi maxsus virtual qurilma («qora tuynuk»). |

---

## Bilasizmi?

- Unix operatsion tizimiga quvurlar (pipes) g'oyasi 1973-yilda Duglas Makilroy (Douglas McIlroy) tomonidan kiritilgan va u butun dasturlash madaniyatini o'zgartirib yuborgan.
- `$PATH` da kataloglar chapdan o'ngga qarab tekshiriladi; birinchi topilgan dastur darhol ishga tushadi, qolganlari e'tiborsiz qoldiriladi.
- Linuxda `> file.txt` deb yozsangiz, hattoki buyruq ko'rsatilmagan bo'lsa ham faylning ichi 0 bayt qilib tozalanadi.
- Bash so'zi «Bourne Again Shell» ning qisqartmasi bo'lib, u Stiven Born (Stephen Bourne) tomonidan yozilgan original Sh interpretatorining ochiq kodli vorisidir.

---

## Topshiriqlar

### 1. Tizim o'zgaruvchilarini o'qish · oson
Terminalda `echo $USER`, `echo $HOME` va `echo $SHELL` buyruqlarini bajarib, o'z tizimingiz haqidagi ma'lumotlarni aniqlang.
**Kutiladigan natija:** Ekranda joriy foydalanuvchi nomi, uning boshlang'ich papkasi va ishlatilayotgan shell dasturi ko'rinadi.

### 2. Mahalliy o'zgaruvchi yaratish · oson
`COURSE="DevOps"` nomli o'zgaruvchi e'lon qiling va uni `echo $COURSE` orqali ekranga chiqaring.
**Kutiladigan natija:** Ekranga `DevOps` so'zi chiqadi.

### 3. Natijani yangi faylga yo'naltirish (`>`) · oson
`date > today.txt` buyrug'i orqali joriy sana va vaqtni `today.txt` fayliga yozing va `cat` orqali tekshiring.
**Kutiladigan natija:** Faylda tizim sanasi saqlanadi.

### 4. Faylga ma'lumot qo'shish (`>>`) · oson
`echo "1-hafta tugamoqda" >> today.txt` buyrug'ini bajaring va fayl mazmunini tekshiring.
**Kutiladigan natija:** Faylda ikki qator matn paydo bo'ladi (sana o'chib ketmaydi).

### 5. O'zgaruvchini eksport qilish (`export`) · o'rta
`APP_ENV="production"` o'zgaruvchisini yarating, uni `export` qiling va `printenv | grep APP_ENV` yordamida uning global muhitda paydo bo'lganini tasdiqlang.
**Kutiladigan natija:** `printenv` ro'yxatida `APP_ENV=production` aks etadi.

### 6. Quvur yordamida qatorlarni sanash · o'rta
`/etc` katalogida nechta element borligini `ls /etc | wc -l` quvuri orqali hisoblang.
**Kutiladigan natija:** Ekranda katalogdagi fayllar sonini ifodalovchi yagona butun son chiqadi.

### 7. Xatoliklarni alohida faylga yo'naltirish · o'rta
Mavjud bo'lmagan fayl ustida buyruq bering (masalan: `ls /not_existing_folder 2> error.log`) va `error.log` faylini ko'ring.
**Kutiladigan natija:** Xatolik xabari ekranga chiqmaydi, balki `error.log` ichiga yoziladi.

### 8. Alias yaratish va sinash · o'rta
Joriy terminalda `alias mydir='pwd && ls -lh'` aliasini e'lon qiling va `mydir` deb yozib natijasini sinab ko'ring.
**Kutiladigan natija:** Bitta so'z orqali ham joriy joy, ham batafsil fayllar ro'yxati chiqadi.

### 9. Ko'p bosqichli filtrlash zanjiri · qiyin
`cat /etc/passwd | cut -d: -f1 | sort | head -n 5` buyruqlar zanjirini bajaring va uning qanday ishlaganini tahlil qiling.
**Kutiladigan natija:** Tizimdagi foydalanuvchilar nomlari alifbo bo'yicha tartiblanib, dastlabki 5 tasi ko'rsatiladi.

### 10. Xatoliklarni /dev/null ga yuborish · qiyin
`find / -name "*.conf" 2> /dev/null | grep "nginx"` buyrug'ini bajaring. Tizimdagi «Permission denied» xatolari qayerga ketganini tushuntiring.
**Kutiladigan natija:** Hech qanday xatoliksiz faqatgina `nginx` ga tegishli konfiguratsiya yo'llari ekranga chiqadi.

### 11. O'z buyrug'ingizni $PATH ga qo'shish · bonus
O'z uy katalogingizda `my_bin` nomli papka oching, uning ichida `salom.sh` faylini yaratib (`chmod 755`), ichiga `echo "Salom, DevOps!"` yozing. So'ngra `export PATH="$PATH:$HOME/my_bin"` buyrug'i orqali uni `$PATH` ga qo'shing va istalgan papkadan turib `salom.sh` deb chaqiring!
**Kutiladigan natija:** Skript `./` qo'shmasdan oddiy tizim buyrug'i kabi to'g'ridan-to'g'ri ishga tushadi.

---

## O'zingizni tekshiring

1. Mahalliy (local) va global (environment) o'zgaruvchilarning farqi nimada?
2. Nima uchun `export` qilinmagan o'zgaruvchi yangi ishga tushgan skript ichida ko'rinmaydi?
3. `>` bilan `>>` operatorlari qachon qaysi biri ishlatiladi?
4. Linuxda 0, 1, 2 raqamlari qaysi standart oqimlarga tegishli?
5. `2> /dev/null` ifodasi nima maqsadda qo'llaniladi?

---

## Uyga vazifa

O'z uyingizdagi Linux tizimida `~/.bashrc` faylini oching (ehtiyotkorlik bilan!). Faylning eng oxiriga o'ting va o'zingiz uchun 3 ta qulay alias (masalan: `alias ll='ls -la'`, `alias cls='clear'`) hamda `DEV_NAME="sizning_ismingiz"` eksportini qo'shing. Faylni saqlang va `source ~/.bashrc` buyrug'i orqali o'zgarishlarni qo'llang. Terminalni qayta ochib, yaratgan aliaslaringiz va o'zgaruvchingiz ishlayotganini tekshiring (taxminiy vaqt: 25 daqiqa).
