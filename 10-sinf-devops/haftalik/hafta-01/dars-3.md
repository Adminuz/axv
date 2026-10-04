# 3-dars. Shell muhiti, tizim o'zgaruvchilari va I/O yo'naltirish (Redirection)

**Darsning maqsadi:** O'quvchilarga Linux Shell muhiti, muhit o'zgaruvchilari (Environment Variables: `PATH`, `USER`, `HOME`, `SHELL`), o'zgaruvchilarni yaratish va eksport qilish (`export`), konfiguratsiya fayllari (`.bashrc`), aliaslar hamda Linux ma'lumot oqimlari (STDIN, STDOUT, STDERR), I/O redirection (`>`, `>>`, `<`) va buyruqlar quvurlari (`|` pipe) bilan ishlashni amaliy o'rgatish.

**Vaqt taqsimoti:**
- O'tgan darsni takrorlash (Ruxsatlar va Vim): 10 daqiqa
- Yangi mavzu: Shell turlari, Environment variables va `PATH` ishlash mexanizmi: 20 daqiqa
- Yangi mavzu: I/O oqimlari (0, 1, 2), qayta yo'naltirish va piping (`|`): 20 daqiqa
- Amaliy mashg'ulot (O'zgaruvchi yaratish, .bashrc sozlash va quvurlar orqali ma'lumot filtrlash): 25 daqiqa
- Dars xulosasi va tezkor nazorat: 5 daqiqa

---

## 1. Dars konspekti (Mentor uchun)

### 1.1. Shell muhiti va o'zgaruvchilar turlari
Shell — foydalanuvchi bilan operatsion tizim yadrosi (Kernel) o'rtasidagi buyruqlar interpretatoridir (eng mashhurlari: Bash, Zsh, Sh).
Shell ish jarayonida uch xil o'zgaruvchilar bilan ishlaydi:
1. **Local variables (Mahalliy o'zgaruvchilar)**: Faqat joriy shell sessiyasida mavjud bo'ladi. Shell yopilsa yoki yangi quyi jarayon (child process) ochilsa, yo'qoladi.
   - Sintaksis: `NAME="Ali"` (tenglik atrofida bo'sh joy bo'lmasligi shart!).
   - Qiymatni ko'rish: `echo $NAME`.
2. **Environment variables (Muhit / Global o'zgaruvchilari)**: Joriy shell va undan tug'ilgan barcha quyi dasturlar va jarayonlar uchun ochiq bo'ladi.
   - Yaratish/Eksport: `export APP_PORT=8080`.
   - Barcha muhit o'zgaruvchilarini ko'rish: `printenv` yoki `env`.
3. **Shell / System variables**: Shell'ning o'zi tomonidan avtomat boshqariladigan tizim o'zgaruvchilari:
   - `$USER` — joriy tizim foydalanuvchisi.
   - `$HOME` — foydalanuvchining uy katalogi.
   - `$SHELL` — ishlatilayotgan shell dasturi yo'li.
   - `$PWD` — joriy katalog.
   - `$PATH` — buyruqlar qidiriladigan kataloglar ro'yxati.

### 1.2. `$PATH` o'zgaruvchisining ahamiyati
Nima uchun biz `ls` deb yozganimizda u ishlaydi, lekin o'zimiz yozgan `script.sh` ni ishga tushirish uchun `./script.sh` deb yozishimiz kerak?
- Terminalda biror buyruq kiritilganda, shell butun diskni qidirmaydi! U faqat `$PATH` o'zgaruvchisida ko'rsatilgan kataloglar ichidan (ikki nuqta `:` bilan ajratilgan) shu nomli faylni qidiradi.
- `$PATH` tarkibi odatda: `/usr/local/bin:/usr/bin:/bin:/usr/games`.
- O'z dasturingizni istalgan joydan turib nomi bilan chaqirish uchun uning papkasini `$PATH` ga qo'shish kerak:
  `export PATH="$PATH:/home/user/my_scripts"`
- O'zgaruvchilarni doimiy saqlab qolish uchun uni `~/.bashrc` (yoki `~/.zshrc`) fayliga yozib qo'yiladi:
  `source ~/.bashrc` — o'zgarishlarni terminalni yopmasdan darhol yuklash.

### 1.3. Aliaslar (Buyruq taxalluslari)
Uzun va murakkab buyruqlarni qisqartma shaklida saqlash:
`alias ll='ls -la'`
`alias update='sudo apt update && sudo apt upgrade -y'`
Doimiy saqlash uchun `~/.bashrc` fayliga kiritiladi.

### 1.4. Linux ma'lumot oqimlari (I/O Streams)
Har bir Linux jarayoni ishga tushganda avtomatik ravishda 3 ta standart oqim bilan bog'lanadi:
1. **STDIN (Standard Input — 0)**: Dasturga kiruvchi ma'lumot (standart: klaviatura).
2. **STDOUT (Standard Output — 1)**: Dasturning muvaffaqiyatli natijasi (standart: terminal ekrani).
3. **STDERR (Standard Error — 2)**: Dastur yuzaga keltirgan xatolik xabarlari (standart: terminal ekrani).

### 1.5. Qayta yo'naltirish (Redirection)
Natijani ekranga chiqarmay, faylga yozish yoki fayldan o'qish:
- `>` — STDOUT'ni faylga yo'naltiradi (fayl mavjud bo'lsa, ichidagini o'chirib yangidan yozadi — overwrite).
  Masalan: `ls -la > files_list.txt`
- `>>` — STDOUT'ni fayl oxiriga qo'shadi (append).
  Masalan: `echo "Server started at $(date)" >> app.log`
- `<` — Faylni dasturga STDIN sifatida uzatadi.
  Masalan: `mysql db_name < backup.sql`
- `2>` — Faqat xatoliklarni (STDERR) faylga yo'naltiradi.
  Masalan: `find / -name "*.conf" 2> /dev/null` (`/dev/null` — keraksiz xatolarni yo'qotuvchi qora tuynuk).
- `&>` yoki `> file.log 2>&1` — Ham natija (STDOUT), ham xatolikni (STDERR) bitta faylga yozadi.

### 1.6. Quvurlar (Pipes `|`)
Unix falsafasining eng buyuk kashfiyoti. Pipe (`|`) — bir buyruqning chiqish oqimini (STDOUT) hech qanday oraliq fayllarsiz to'g'ridan-to'g'ri keyingi buyruqning kirish oqimiga (STDIN) ulaydi!
- `ls ~ | wc -l` — Uy katalogidagi fayllar sonini hisoblash.
- `cat /var/log/syslog | grep "error" | wc -l` — Log ichidagi xatolar sonini sanash.
- `ps aux | grep "nginx"` — Ishlayotgan Nginx jarayonlarini topish.

---

## 2. Amaliy topshiriqlar va yechimlari (Mentor uchun)

### 1-topshiriq. Tizim muhit o'zgaruvchilarini tekshirish
Terminalda joriy foydalanuvchi nomi, uning uy katalogi va `$PATH` tarkibini `echo` orqali ekranga chiqaring.

**Yechim:**
```bash
echo "Foydalanuvchi: $USER"
echo "Uy katalogi: $HOME"
echo "Qidiruv yo'llari: $PATH"
```

### 2-topshiriq. Yangi o'zgaruvchi yaratish va eksport qilish
`DB_HOST="localhost"` va `DB_PORT="5432"` o'zgaruvchilarini yarating, ularni global muhitga `export` qiling va `env` buyrug'i orqali mavjudligini tasdiqlang.

**Yechim:**
```bash
# 1. O'zgaruvchilarni yaratish va eksport qilish
export DB_HOST="localhost"
export DB_PORT="5432"

# 2. Grep bilan tekshirish
env | grep DB_
# Natija:
# DB_HOST=localhost
# DB_PORT=5432
```

### 3-topshiriq. Natijalarni faylga yo'naltirish (`>` va `>>`)
Tizim sanasi va vaqtini `deployment.log` fayliga yangidan yozing. So'ngra fayl mazmunini o'chirmasdan uning oxiriga «Deploy muvaffaqiyatli yakunlandi» matnini qo'shing.

**Yechim:**
```bash
# 1. Sanani faylga yangidan yozish (>)
date > deployment.log

# 2. Fayl oxiriga qo'shish (>>)
echo "Deploy muvaffaqiyatli yakunlandi" >> deployment.log

# 3. Faylni tekshirish
cat deployment.log
```

### 4-topshiriq. Quvurlar (`|`) orqali loglarni filtrlash
`ls /etc | grep "cron" | wc -l` zanjirini tuzing va uning har bir bosqichida nima sodir bo'layotganini tahlil qiling.

**Yechim:**
```bash
ls /etc | grep "cron" | wc -l

# Bosqichlar tahlili:
# 1. 'ls /etc' — /etc papkasidagi barcha fayllarni chiqaradi.
# 2. '| grep "cron"' — faqat nomida 'cron' so'zi bor qatorlarni ajratib oladi.
# 3. '| wc -l' — ajratilgan qatorlar sonini hisoblaydi.
```

---

## 3. Tezkor nazorat savollari (Dars yakuni)

1. **`>` bilan `>>` operatorlarining qanday farqi bor?**
   *Javob:* `>` operatori fayl mavjud bo'lsa uning ichidagi barcha ma'lumotlarni o'chirib yangidan yozadi (overwrite), `>>` esa faylning mavjud mazmuniga teginmasdan uning eng oxiriga yangi qator qo'shadi (append).
2. **`$PATH` o'zgaruvchisi nima uchun kerak?**
   *Javob:* Shell buyruq kiritilganda uning executable faylini qidirishi kerak bo'lgan kataloglar ro'yxatini belgilaydi.
3. **Pipe (`|`) belgisi nima vazifani bajaradi?**
   *Javob:* Birinchi buyruqning STDOUT natijasini to'g'ridan-to'g'ri ikkinchi buyruqning STDIN kirish oqimiga xotira orqali uzatadi.
4. **Linuxda STDERR (xatolik) oqimi qaysi deskriptor raqamiga ega va uni qanday yo'naltirish mumkin?**
   *Javob:* Raqami `2`. Masalan: `2> error.log` yoki xatolarni ko'rsatmaslik uchun `2> /dev/null`.
