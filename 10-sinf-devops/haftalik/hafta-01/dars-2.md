# 2-dars. Fayl ruxsatlari tizimi va matn tahrirlash vositalari (Nano, Vim)

**Darsning maqsadi:** O'quvchilarga Linux operatsion tizimida xavfsizlikning negizi bo'lgan fayl va katalog ruxsatlari tizimini (User, Group, Others; r, w, x; simvolik va oktal raqamli usul), ruxsatlarni o'zgartirish (`chmod`, `chown`, `chgrp`) hamda server muhitida matnli konfiguratsiya fayllarini tahrirlash vositalari (`nano` va `vim`) bilan ishlashni amaliy o'rgatish.

**Vaqt taqsimoti:**
- O'tgan darsni takrorlash (FHS va navigatsiya): 10 daqiqa
- Yangi mavzu: Fayl ruxsatlari tuzilishi, oktal hisoblash va Least Privilege prinsipi: 25 daqiqa
- Yangi mavzu: Server muharrirlari (Nano va Vim rejimlari: Normal, Insert, Command): 15 daqiqa
- Amaliy mashg'ulot (Ruxsatlarni sozlash va Vim'da konfiguratsiya yozish): 25 daqiqa
- Dars xulosasi va nazorat: 5 daqiqa

---

## 1. Dars konspekti (Mentor uchun)

### 1.1. Linux xavfsizlik modeli va ruxsatlar tizimi
Linux ko'p foydalanuvchili (multi-user) operatsion tizim bo'lib, unda har bir fayl va katalog o'z egasiga va muayyan guruhga tegishli bo'ladi.
`ls -l` buyrug'i berilganda birinchi ustunda 10 ta belgidan iborat qator ko'rinadi:
Masalan: `-rwxr-xr-- 1 devops developers 4096 Oct 10 12:00 deploy.sh`

1. **1-belgi — Obyekt turi:**
   - `-` — oddiy fayl (regular file).
   - `d` — katalog (directory).
   - `l` — ramziy havola (symbolic link).
2. **Keyingi 9 ta belgi 3 ta guruhga (triadaga) bo'linadi:**
   - `rwx` (1–3) — **User (u)**: Fayl egasining ruxsatlari.
   - `r-x` (4–6) — **Group (g)**: Fayl tegishli bo'lgan guruh a'zolarining ruxsatlari.
   - `r--` (7–9) — **Others (o)**: Tizimdagi qolgan barcha foydalanuvchilarning ruxsatlari.

### 1.2. Ruxsat turlari va ularning ma'nosi
| Harf | Belgisi | Fayl uchun ma'nosi | Katalog uchun ma'nosi | Bit qiymati |
|---|---|---|---|---|
| **r** | Read | Fayl mazmunini o'qish | Katalog ichidagi fayllar ro'yxatini ko'rish (`ls`) | 4 |
| **w** | Write | Faylga o'zgartirish kiritish yoki o'chirish | Katalog ichida yangi fayl yaratish yoki o'chirish | 2 |
| **x** | Execute | Skript/dastur sifatida ishga tushirish | Katalog ichiga kirish (`cd`) | 1 |
| **-** | None | Ruxsat berilmagan | Ruxsat berilmagan | 0 |

### 1.3. Raqamli (Oktal) ifodalash
Har bir toifa (User, Group, Others) uchun ruxsatlar yig'indisi hisoblanadi:
- `rwx` = 4 + 2 + 1 = **7** (to'liq ruxsat)
- `rw-` = 4 + 2 + 0 = **6** (o'qish va yozish)
- `r-x` = 4 + 0 + 1 = **5** (o'qish va bajarish)
- `r--` = 4 + 0 + 0 = **4** (faqat o'qish)
- `---` = 0 + 0 + 0 = **0** (hech qanday ruxsat yo'q)

**DevOps'dagi standart kombinatsiyalar:**
- `chmod 755 script.sh` — Egasi o'qiydi, yozadi, ishga tushiradi; guruh va boshqalar faqat o'qiydi va ishga tushiradi (skriptlar va dasturlar uchun).
- `chmod 644 config.conf` — Egasi o'qiydi va yozadi; qolganlar faqat o'qiydi (konfiguratsiya fayllari uchun).
- `chmod 600 id_rsa` — Faqat egasi o'qiydi va yozadi; qolgan hech kim ko'ra olmaydi (SSH maxfiy kalitlari uchun).
- **Least Privilege (Eng kam imtiyoz) prinsipi**: Hech qachon ishlab chiqarish muhitida `chmod 777` ishlatilmaydi!

### 1.4. Ruxsatlarni o'zgartirish buyruqlari
- `chmod [rejim] [fayl]` (change mode) — ruxsatlarni o'zgartirish:
  - Raqamli usul: `chmod 755 run.sh`
  - Ramziy usul: `chmod u+x run.sh` (egasiga bajarish huquqini qo'shish), `chmod g-w file.txt` (guruhdan yozishni olib tashlash).
- `chown [yangi_ega]:[yangi_guruh] [fayl]` (change owner) — fayl egasi va guruhini o'zgartirish:
  - `sudo chown www-data:www-data /var/www/html -R` (veb-server uchun egalikni berish).
- `chgrp [yangi_guruh] [fayl]` — faqat guruhni o'zgartirish.

### 1.5. Server matn muharrirlari: Nano va Vim
DevOps muhandislari ko'pincha masofaviy serverlarda (SSH orqali) grafik interfeyssiz ishlaydi. Shuning uchun terminal matn muharrirlarini puxta bilish shart.
- **Nano**: Boshlang'ich daraja uchun juda sodda, ekranning quyi qismida doimiy yordamchi buyruqlar ko'rsatiladi:
  - `Ctrl + O` — faylni saqlash.
  - `Ctrl + X` — muharrirdan chiqish.
- **Vim (Vi IMproved)**: Butun dunyo muhandislari foydalanadigan kuchli, tezkor va modal muharrir.
  - **Normal mode**: Vim ochilgandagi boshlang'ich rejim. Matn yozilmaydi, buyruqlar beriladi (`dd` — qatorni o'chirish, `yy` — nusxa olish, `p` — qo'yish, `/qidiruv` — izlash).
  - **Insert mode**: Matn yozish rejimi. Normal rejimda `i` (insert) yoki `a` (append) bosilganda o'tiladi. Rejimdan chiqish: `Esc`.
  - **Command-line mode**: Faylni saqlash va chiqish. Normal rejimda `:` bosiladi:
    - `:w` — saqlash (write).
    - `:q` — chiqish (quit).
    - `:wq` yoki `:x` — saqlab chiqish.
    - `:q!` — o'zgarishlarni bekor qilib majburiy chiqish.

---

## 2. Amaliy topshiriqlar va yechimlari (Mentor uchun)

### 1-topshiriq. Skriptga bajarish huquqini berish
O'z uy katalogingizda `deploy.sh` faylini yarating. Dastlab uning ruxsatlarini tekshiring, so'ngra unga ham raqamli (`755`), ham ramziy (`u+x`) usul yordamida bajarish (execute) huquqini bering.

**Yechim:**
```bash
# 1. Fayl yaratish
touch deploy.sh

# 2. Dastlabki ruxsatni ko'rish
ls -l deploy.sh
# Natija odatda: -rw-r--r-- (644)

# 3. Raqamli usulda 755 qilish
chmod 755 deploy.sh
ls -l deploy.sh
# Natija: -rwxr-xr-x

# 4. Ramziy usulda barcha uchun execute huquqini tekshirish
chmod +x deploy.sh
```

### 2-topshiriq. Maxfiy konfiguratsiya faylini himoyalash
`database.env` nomli fayl yarating. Unga faqatgina fayl egasi (User) o'qiy oladigan va yozadigan (`rw-`), qolgan hech bir guruh yoki boshqa foydalanuvchilar kira olmaydigan (`---`) ruxsatni belgilang.

**Yechim:**
```bash
# 1. Fayl yaratish
touch database.env

# 2. Faqat egasiga rwx/rw ruxsati berish (600)
chmod 600 database.env

# 3. Natijani tekshirish
ls -l database.env
# Natija: -rw------- 1 devops devops 0 Oct 10 12:00 database.env
```

### 3-topshiriq. Vim yordamida Nginx sozlama faylini yozish
`nano` yoki `vim` yordamida `nginx_test.conf` faylini oching, quyidagi matnni kiriting va saqlab chiqing:
```nginx
server {
    listen 80;
    server_name example.com;
    root /var/www/html;
}
```

**Yechim:**
```bash
# Vim'da ochish
vim nginx_test.conf

# Amal ketma-ketligi:
# 1. 'i' tugmasini bosib Insert mode ga o'tiladi.
# 2. Konfiguratsiya matni yoziladi.
# 3. 'Esc' tugmasi bosilib Normal mode ga qaytiladi.
# 4. ':wq' yozilib Enter bosiladi.

# Fayl mazmunini tekshirish
cat nginx_test.conf
```

### 4-topshiriq. Rekursiv egalik va ruxsatlarni o'zgartirish
`web_project` nomli papka yaratib, uning ichida bir nechta fayllar hosil qiling. Barcha ichki fayllar va papkalarga birvarakayiga `chmod 750` ruxsatini rekursiv tatbiq eting.

**Yechim:**
```bash
# 1. Papka va fayllarni hosil qilish
mkdir -p web_project/logs
touch web_project/app.js web_project/logs/error.log

# 2. Rekursiv -R bilan 750 (rwxr-x---) qilish
chmod -R 750 web_project

# 3. Natijani tekshirish
ls -la web_project
```

---

## 3. Tezkor nazorat savollari (Dars yakuni)

1. **`chmod 777` buyrug'i nima uchun xavfsizlik nuqtai nazaridan taqiqlangan yondashuv hisoblanadi?**
   *Javob:* U tizimdagi har qanday begona foydalanuvchi yoki buzg'unchi jarayonga faylni o'qish, o'zgartirish va uning o'rniga zararli kod joylab ishga tushirish imkonini beradi.
2. **`chmod 644` oktal kodi qanday ruxsatlarni bildiradi?**
   *Javob:* Fayl egasi uchun `rw-` (o'qish va yozish, 4+2=6), guruh uchun `r--` (faqat o'qish, 4), boshqalar uchun `r--` (faqat o'qish, 4).
3. **Katalog (directory) uchun `x` (execute) ruxsati nimani anglatadi?**
   *Javob:* Katalog ichiga `cd` buyrug'i orqali kirish va uning ichidagi fayllarga murojaat qilish imkoniyatini bildiradi.
4. **Vim muharririda kiritilgan o'zgarishlarni saqlamasdan majburiy chiqish qanday bajariladi?**
   *Javob:* `Esc` bosilib Normal rejimga o'tiladi va `:q!` buyrug'i teriladi.
