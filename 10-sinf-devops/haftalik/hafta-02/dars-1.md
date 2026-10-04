# 4-dars. Xizmatlar va jarayonlarni boshqarish (ps, top, kill, systemd)

**Darsning maqsadi:** O'quvchilarga Linux operatsion tizimida jarayonlar (processes) tushunchasi, Foreground va Background rejimlari, jarayon holatlari (R, S, D, T, Z), jarayonlarni kuzatish (`ps`, `top`, `htop`), ustuvorlikni boshqarish (`nice`, `renice`), signallar va to'xtatish (`kill`, `killall`) hamda tizim xizmatlarini boshqarish (`systemd`, `systemctl`) asoslarini amaliy o'rgatish.

**Vaqt taqsimoti:**
- O'tgan haftani takrorlash (FHS, ruxsatlar, Shell): 10 daqiqa
- Yangi mavzu: Jarayonlar anatomiyasi, holatlar va monitoring (`ps aux`, `top`): 25 daqiqa
- Yangi mavzu: Signallar (SIGTERM, SIGKILL) va `systemctl` xizmatlar boshqaruvi: 15 daqiqa
- Amaliy mashg'ulot (Jarayonlarni fon rejimiga o'tkazish, ustuvorlik berish va xizmatlarni boshqarish): 25 daqiqa
- Dars xulosasi va tezkor nazorat: 5 daqiqa

---

## 1. Dars konspekti (Mentor uchun)

### 1.1. Jarayon (Process) nima?
Linuxda dastur — bu diskda saqlangan statik fayl (masalan, `/usr/bin/python3`). U xotiraga (RAM) yuklanib, protsessor (CPU) tomonidan bajarila boshlagach, **jarayon (process)**ga aylanadi.
Har bir jarayon operatsion tizim tomonidan berilgan noyob raqam — **PID (Process ID)** ga ega bo'ladi.
- **PPID (Parent Process ID)**: Har bir jarayon boshqa bir ota jarayon tomonidan yaratiladi (fork qilinadi).
- Eng birinchi va barcha jarayonlarning otasi — `PID 1` bo'lib, zamonaviy Linux tizimlarida bu **systemd** dasturidir.

### 1.2. Foreground va Background jarayonlar
1. **Foreground (Oldingi) rejim**: Foydalanuvchi bilan bevosita muloqot qiladi va terminalni band qilib turadi. Masalan, `ping google.com`.
2. **Background (Fon) rejim**: Terminalni band qilmay, fonda ishlaydi.
   - Ishga tushirishdayoq fonga yuborish: buyruq oxiriga `&` belgisi qo'yiladi:
     `python3 app.py &`
   - Ishlayotgan jarayonni fonga o'tkazish:
     - `Ctrl + Z` — jarayonni vaqtincha to'xtatadi (Pause/Suspend).
     - `bg` — uni fon rejimida davom ettiradi.
     - `jobs` — joriy terminaldagi fon vazifalarini ko'rish.
     - `fg %1` — fon vazifasini yana terminalning oldingi rejimiga qaytarish.

### 1.3. Jarayon holatlari (Process States)
`ps aux` buyrug'ining `STAT` ustunida quyidagi belgilar uchraydi:
- **R (Running / Runnable)**: Jarayon faol ishlayapti yoki CPU navbatida turibdi.
- **S (Interruptible Sleep)**: Hodisa yoki kiritish-chiqarishni kutmoqda (eng ko'p uchraydigan holat).
- **D (Uninterruptible Sleep)**: O'chirish signallariga javob bermay disk I/O ni kutmoqda.
- **T (Stopped)**: `Ctrl+Z` yoki signal bilan vaqtincha to'xtatilgan.
- **Z (Zombie)**: O'z vazifasini tugatgan, lekin ota jarayon uning xotira hisobotini hali qabul qilmagan «o'lik» jarayon.

### 1.4. Jarayonlarni monitoring qilish: ps, top, htop
- `ps aux` — tizimdagi barcha foydalanuvchilarning barcha jarayonlarini to'liq ro'yxat qiladi:
  - `USER`: egasi
  - `PID`: jarayon identifikatori
  - `%CPU`, `%MEM`: protsessor va operativ xotiradan foydalanish foizi
  - `STAT`: holati
  - `COMMAND`: jarayonni ishga tushirgan to'liq buyruq
- `top` — real vaqt rejimida yangilanib turuvchi monitoring (CPU, RAM, load average).
- `htop` — `top` ning rangli va qulay interaktiv analogi (F9 bilan jarayonni to'xtatish mumkin).

### 1.5. Ustuvorlik: nice va renice
Linuxda jarayon ustuvorligi `-20` dan `19` gacha bo'lgan son bilan o'lchanadi:
- **-20**: Eng yuqori ustuvorlik (protsessor birinchi bo'lib xizmat qiladi, faqat root qo'ya oladi).
- **19**: Eng past ustuvorlik («xushmuomala» jarayon, bo'sh vaqtda ishlaydi).
- Ishga tushirish: `nice -n 10 ./backup.sh`
- Ishlayotgan jarayonni o'zgartirish: `renice -n 5 -p 1234`

### 1.6. Signallar va to'xtatish: kill va killall
Jarayonga buyruq signallar orqali beriladi:
- **SIGTERM (15)**: Odobli to'xtash so'rovi (jarayon ma'lumotlarni saqlab, xavfsiz yopiladi). Standart: `kill 1234`.
- **SIGKILL (9)**: Majburiy darhol yo'q qilish (yadro tomonidan to'g'ridan-to'g'ri o'chiriladi, jarayon qarshilik qila olmaydi). Buyruq: `kill -9 1234`.
- **SIGHUP (1)**: Qayta yuklash (reload configuration).
- **SIGINT (2)**: `Ctrl + C` bosilganda yuboriladigan to'xtatish signali.
- `killall [nom]` — barcha bir xil nomli jarayonlarni birdaniga to'xtatadi: `killall nginx`.

### 1.7. Tizim xizmatlari va systemctl
Serverlarda dasturlar (Nginx, Docker, PostgreSQL) fonda xizmat (daemon) sifatida ishlaydi. Ularni **systemd** boshqaradi:
- `sudo systemctl start nginx` — xizmatni ishga tushirish.
- `sudo systemctl stop nginx` — xizmatni to'xtatish.
- `sudo systemctl restart nginx` — qayta ishga tushirish.
- `sudo systemctl status nginx` — holatini ko'rish (active, inactive, failed).
- `sudo systemctl enable nginx` — server qayta yuklanganda (reboot) avtomatik yoqilishini sozlash (autostart).
- `sudo systemctl disable nginx` — avtomatik yoqilishni bekor qilish.

---

## 2. Amaliy topshiriqlar va yechimlari (Mentor uchun)

### 1-topshiriq. Jarayonni fonga o'tkazish va qaytarish
`sleep 300` buyrug'ini ishga tushiring, so'ngra `Ctrl+Z` orqali uni to'xtatib, `bg` bilan fonda davom ettiring va `jobs` ro'yxatida ko'ring.

**Yechim:**
```bash
# 1. Jarayonni ishga tushirish
sleep 300

# 2. Klaviaturada 'Ctrl + Z' bosiladi:
# [1]+  Stopped                 sleep 300

# 3. Fondan davom ettirish
bg
# [1]+ sleep 300 &

# 4. Ro'yxatni tekshirish
jobs
# [1]+  Running                 sleep 300 &
```

### 2-topshiriq. Jarayonni qidirish va to'xtatish
Fondagi `sleep` jarayonining PID raqamini `ps aux | grep sleep` orqali aniqlang va uni `kill` buyrug'i yordamida to'xtating.

**Yechim:**
```bash
# 1. Qidirish
ps aux | grep sleep
# Masalan natija: devops 24512 0.0 0.0 5420 812 pts/0 S 14:00 0:00 sleep 300

# 2. To'xtatish (SIGTERM)
kill 24512

# 3. Tekshirish
jobs
# [1]+  Terminated              sleep 300
```

### 3-topshiriq. Past ustuvorlik bilan jarayon ishga tushirish
`nice` yordamida `15` ustuvorlik bilan yangi `sleep 200 &` jarayonini ishga tushiring va `ps -o pid,ni,cmd` orqali uning `NI` (nice) ustuni 15 ekanligini tasdiqlang.

**Yechim:**
```bash
# 1. Nice bilan ishga tushirish
nice -n 15 sleep 200 &

# 2. Nice ustunini tekshirish
ps -o pid,ni,cmd | grep sleep

# 3. Tozalash
killall sleep
```

### 4-topshiriq. Systemctl bilan xizmat holatini tekshirish
Tizimdagi `cron` yoki `ssh` xizmatining holatini `systemctl status` orqali tekshiring.

**Yechim:**
```bash
systemctl status cron
# Yoki:
systemctl status sshd
```

---

## 3. Tezkor nazorat savollari (Dars yakuni)

1. **`PID 1` nima va u Linuxda qanday vazifani bajaradi?**
   *Javob:* Bu tizimdagi eng birinchi ota jarayon bo'lib, zamonaviy Linuxda `systemd` deb ataladi va barcha boshqa xizmat va jarayonlarni boshqaradi.
2. **`kill -9` bilan oddiy `kill` (SIGTERM 15) ning qanday farqi bor?**
   *Javob:* Oddiy `kill` (SIGTERM) dasturga o'zini tartibli saqlab yopish imkonini beradi. `kill -9` (SIGKILL) esa zudlik bilan, ogohlantirishsiz xotiradan kuch bilan o'chiradi.
3. **`systemctl enable` va `systemctl start` buyruqlarining farqi nimada?**
   *Javob:* `start` xizmatni hozirning o'zida ishga tushiradi. `enable` esa operatsion tizim qayta yuklanganda xizmatning avtomatik yoqilishini ta'minlaydi.
4. **Jarayon holatlaridagi «Zombie» (Z) holati nimani anglatadi?**
   *Javob:* Jarayon bajarilib tugagan, ammo uning ota jarayoni chiqish kodini o'qib olmaguncha xotira jadvalida saqlanib turgan holat.
