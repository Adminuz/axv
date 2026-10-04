# 1-dars. Linux terminal va asosiy buyruqlar: FHS va fayllar tizimi bilan ishlash

**Darsning maqsadi:** O'quvchilarga Linux operatsion tizimining DevOps sohasidagi o'rni, Linux buyruqlar satri (CLI) arxitekturasi, Filesystem Hierarchy Standard (FHS) tuzilishi hamda fayl va kataloglar ustida navigatsiya va boshqaruv amallarini (`pwd`, `ls`, `cd`, `mkdir`, `cp`, `mv`, `rm`, `touch`, `find`) amaliy o'rgatish.

**Vaqt taqsimoti:**
- O'tgan mavzuni takrorlash va kirish: 10 daqiqa
- Yangi mavzu bayoni (CLI, FHS ierarxiyasi, buyruqlar zanjiri): 25 daqiqa
- Amaliy mashg'ulot (Terminalda kataloglar daraxti yaratish va manipulyatsiya): 35 daqiqa
- Dars xulosasi va tezkor savol-javob: 10 daqiqa

---

## 1. Dars konspekti (Mentor uchun)

### 1.1. DevOps dunyosida nima uchun Linux va Terminal?
Zamonaviy bulut infratuzilmalari (AWS, GCP, Azure), serverlar, konteynerlar (Docker, Kubernetes) va CI/CD muhitlarining 90% dan ortig'i aynan Linux operatsion tizimida ishlaydi. Linux — server va bulut olamining standartidir.
- **CLI (Command Line Interface)**: Grafik interfeys (GUI) serverlarda ortiqcha RAM va CPU sarflaydi. Terminal orqali tizimni boshqarish minimal resurs talab qiladi, to'liq masofadan (SSH orqali) boshqariladi va buyruqlar yordamida har qanday jarayonni 100% avtomatlashtirish (scripting) imkonini beradi.
- **Unix falsafasi**: «Har bir utilita bitta ishni bajarsin, lekin uni a'lo darajada bajarsin» hamda «Hamma narsa — bu fayl». Linuxda disklar, tarmoq soketlari, jarayonlar hatto apparat qurilmalari ham fayllar tizimi daraxti ichida ifodalanadi.

### 1.2. Terminal ishlash zanjiri
Terminal oddiy qora oyna emas, u aniq arxitekturaga ega:
1. **Terminal Emulator** (`gnome-terminal`, `xterm`, `Windows Terminal`): Klaviaturadan belgilar kiritilishini qabul qiladi va ekranga chiqaradi.
2. **Shell** (`Bash`, `Zsh`): Buyruqlarni o'qiydi (parsing), sintaktik tahlil qiladi, o'zgaruvchilarni almashtiradi va kerakli dasturni ishga tushiradi.
3. **System Calls & Kernel**: Utilita yadroga tizim chaqiruvlari orqali murojaat qiladi, yadro apparat resurslaridan (CPU, disk) natijani olib, shell orqali foydalanuvchiga qaytaradi.

### 1.3. Linux fayl tizimi ierarxiyasi (FHS — Filesystem Hierarchy Standard)
Windows'dagi kabi `C:\`, `D:\` harflari Linuxda yo'q. Barcha fayllar yagona ildiz — `/` (root) katalogidan boshlanuvchi daraxtsimon ierarxiyada joylashadi:
- `/` — ildiz katalog (Root directory).
- `/bin` va `/usr/bin` — barcha foydalanuvchilar uchun standart bajariluvchi buyruqlar (`ls`, `cp`, `bash`).
- `/sbin` va `/usr/sbin` — tizim administratori (root) uchun maxsus buyruqlar (`iptables`, `fdisk`).
- `/etc` — tizim va xizmatlarning barcha konfiguratsiya fayllari (DevOps'ning eng muhim joyi: masalan, `/etc/nginx/nginx.conf`).
- `/home` — oddiy foydalanuvchilarning shaxsiy ishchi kataloglari (masalan, `/home/devops/`).
- `/root` — superuser (tizim egasi) ning shaxsiy uy katalogi.
- `/var` — tez-tez o'zgaruvchi ma'lumotlar: tizim loglari (`/var/log`), ma'lumotlar bazalari, keshlar.
- `/tmp` — vaqtinchalik fayllar (tizim o'chirilganda tozalanadi).
- `/dev` — qurilma fayllari (`/dev/sda` — qattiq disk, `/dev/null` — axborotni yo'qotuvchi qora tuynuk).
- `/proc` va `/sys` — virtual fayl tizimlari: ishlayotgan jarayonlar va Linux yadrosi holati haqidagi ma'lumotlar.

---

## 2. Asosiy buyruqlar va sintaksis

Har bir buyruq quyidagi umumiy qolipga ega:
`buyruq [opsiyalar/bayroqlar] [argumentlar]`
Masalan: `ls -la /var/log`

### 2.1. Navigatsiya va ko'rish
- `pwd` (print working directory) — joriy ishchi katalogni ekranga to'liq yo'l bilan chiqaradi.
- `cd [manzil]` (change directory) — ko'rsatilgan katalogga o'tadi:
  - `cd ~` yoki shunchaki `cd` — o'z uy katalogiga (`$HOME`) o'tish.
  - `cd ..` — bir pog'ona yuqoriga (ota katalogga) chiqish.
  - `cd -` — oldingi turgan katalogga qaytish.
  - `cd /` — eng yuqori ildiz katalogga o'tish.
- `ls` (list) — katalog tarkibini ko'rish:
  - `ls -l` — batafsil ma'lumot (ruxsatlar, hajm, sana, egasi).
  - `ls -a` — barcha fayllar, shu jumladan nuqta bilan boshlanuvchi yashirin fayllar (`.bashrc`).
  - `ls -lh` — fayl hajmlarini inson tushunadigan formatda ko'rsatish (`KB`, `MB`, `GB`).

### 2.2. Fayl va kataloglar ustida amallar
- `mkdir [nom]` (make directory) — yangi papka yaratish:
  - `mkdir -p devops/project1/src` — ichma-ich butun kataloglar zanjirini birvarakayiga yaratish.
- `touch [nom]` — yangi bo'sh fayl yaratish yoki mavjud faylning vaqt tamg'asini (timestamp) yangilash.
- `cp [manba] [manzil]` (copy) — nusxalash:
  - `cp app.py backup/` — bitta faylni nusxalash.
  - `cp -r src/ backup_src/` — butun katalogni rekursiv nusxalash.
- `mv [manba] [manzil]` (move) — faylni ko'chirish yoki uning nomini o'zgartirish:
  - `mv old.txt new.txt` — qayta nomlash.
  - `mv config.json /etc/app/` — ko'chirish.
- `rm [fayl]` (remove) — o'chirish:
  - `rm file.txt` — bitta faylni o'chirish.
  - `rm -r myfolder` — katalogni ichidagilari bilan birga rekursiv o'chirish.
  - `rm -rf dir` — ogohlantirishlarsiz majburiy o'chirish (ehtiyotkorlik talab etiladi!).
- `cat [fayl]` — fayl mazmunini to'liq terminalga chiqarish.
- `find [yo'l] -name "[namuna]"` — fayllarni qidirish (masalan: `find . -name "*.log"`).

---

## 3. Amaliy topshiriqlar va yechimlari (Mentor uchun)

### 1-topshiriq. FHS bo'ylab sayohat va navigatsiya
O'quvchi o'z uy katalogidan `/var/log` katalogiga mutlaq yo'l bilan o'tsin, uning ichidagi fayllarni inson o'qiy oladigan formatda batafsil ko'rsin, so'ngra bir buyruq bilan yana o'z uy katalogiga qaytsin.

**Yechim:**
```bash
# 1. Joriy joyni tekshirish
pwd

# 2. Mutlaq (absolute) yo'l orqali /var/log ga o'tish
cd /var/log

# 3. Fayllar ro'yxatini batafsil ko'rish
ls -lh

# 4. To'g'ridan-to'g'ri o'z uy katalogiga qaytish
cd ~
# yoki:
cd
pwd
```

### 2-topshiriq. Loyiha strukturasini yaratish
Yagona buyruq yordamida quyidagi ichma-ich tuzilmani yarating: `company/project/backend/api` va `company/project/frontend/public`. Har bir quyi papkada `index.txt` faylini yarating.

**Yechim:**
```bash
# -p parametri orqali ichma-ich kataloglarni yaratish
mkdir -p company/project/backend/api company/project/frontend/public

# Fayllarni yaratish
touch company/project/backend/api/index.txt
touch company/project/frontend/public/index.txt

# Yaratilgan daraxtni tekshirish
ls -R company/
```

### 3-topshiriq. Fayllarni nusxalash va zaxiralash
`company/project/backend/api/index.txt` faylini `company/project/backend/api/index_backup.txt` ga nusxalang, so'ngra asl faylni `server.py` deb qayta nomlang.

**Yechim:**
```bash
# 1. Nusxa olish
cp company/project/backend/api/index.txt company/project/backend/api/index_backup.txt

# 2. Qayta nomlash (mv)
mv company/project/backend/api/index.txt company/project/backend/api/server.py

# 3. Tekshirish
ls company/project/backend/api/
```

### 4-topshiriq. Rekursiv qidiruv va tozalash
`company` papkasi ichidagi barcha `.txt` kengaytmali fayllarni `find` buyrug'i bilan toping, so'ngra butun `company` papkasini xavfsiz tarzda o'chirib tashlang.

**Yechim:**
```bash
# 1. Qidirish
find company -name "*.txt"

# 2. Butun katalogni rekursiv o'chirish
rm -rf company

# 3. O'chirilganini tekshirish
ls company
# Natija: ls: cannot access 'company': No such file or directory
```

---

## 4. Tezkor nazorat savollari (Dars yakuni)

1. **Linuxda nisbiy (relative) va mutlaq (absolute) yo'lning qanday farqi bor?**
   *Javob:* Mutlaq yo'l doimo ildiz (`/`) dan boshlanadi (masalan: `/var/log/syslog`). Nisbiy yo'l esa hozir turgan joriy ishchi katalogga nisbatan yoziladi (masalan: `cd ../backup`).
2. **Nima uchun ishlab chiqarish (production) serverlarida grafik interfeys (GUI) deyarli o'rnatilmaydi?**
   *Javob:* GUI ortiqcha operativ xotira (RAM) va protsessor resursini sarflaydi, serverda qo'shimcha xavfsizlik zaifliklarini keltirib chiqaradi va skriptlar orqali avtomatlashtirish uchun yaroqsiz.
3. **`mkdir -p` buyrug'idagi `-p` bayrog'i nima vazifani bajaradi?**
   *Javob:* Ota kataloglar mavjud bo'lmasa, ularning barchasini avtomatik ravishda birvarakayiga yaratadi (parent directories).
4. **`rm -rf` buyrug'i qanday xavf tug'dirishi mumkin?**
   *Javob:* U katalog va uning barcha ichki elementlarini so'rovsiz va qayta tiklab bo'lmaydigan qilib darhol o'chiradi. Agar noto'g'ri yo'l (masalan, `rm -rf /`) kiritilsa, butun operatsion tizim yo'q qilinadi.
