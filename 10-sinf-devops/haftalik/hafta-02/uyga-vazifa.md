# 2-hafta: Uyga vazifalar (DevOps)

2-haftada jarayonlar (processes) va systemd xizmatlarini boshqarish, disklar va fayl tizimlari tahlili (df/du), paket menejerlari (APT) hamda Git versiya boshqaruvi tizimining poydevori (init, add, commit, .gitignore) o'rganildi. Quyidagi vazifalar amaliy ko'nikmalarni mustahkamlash uchun berilgan.

---

## 4-dars vazifasi: Jarayonlar va Xizmatlar

1. Terminalda `top` yoki `htop` dasturini oching. Tizimingizda umumiy nechta jarayon mavjudligi, ulardan nechtasi faol («running») holatda ekanini daftaringizga qayd eting.
2. `sleep 400 &` buyrug'i yordamida yangi fon jarayonini ishga tushiring. `jobs` va `ps aux | grep sleep` buyruqlari yordamida uning PID raqamini aniqlang.
3. Aniqlangan PID raqami bo'yicha `kill [PID]` buyrug'i bilan ushbu jarayonni to'xtating.
4. `systemctl status cron` (yoki `crond`) buyrug'ini bajarib, rejalashtiruvchi xizmatning faol holatini tekshiring.
*(Kutiladigan vaqt: 25 daqiqa)*

---

## 5-dars vazifasi: Disk sarfi va Paketlar

1. `df -h` buyrug'ini bajaring va asosiy ildiz (`/`) bo'limida qancha umumiy hajm, ishlatilgan hajm va bo'sh joy qolganini aniqlang.
2. O'z uy katalogingizdagi barcha papkalar hajmini `du -sh ~/* | sort -h` orqali saralangan holda ko'ring va eng katta 3 ta papkani yozib oling.
3. `sudo apt update` buyrug'i orqali paketlar indeksini yangilang, so'ngra `sudo apt install -y curl wget ncdu` buyruqlari bilan ushbu utilitalarni o'rnating.
4. `ncdu ~` dasturini ishga tushirib, interaktiv terminal orqali xotira taqsimotini tahlil qiling.
*(Kutiladigan vaqt: 25 daqiqa)*

---

## 6-dars vazifasi: Git va Repozitoriya asoslari

1. Uy katalogingizda `my_git_lab` nomli yangi papka oching va uni `git init` orqali Git omboriga aylantiring.
2. Repozitoriya ichida `app.py`, `README.md` va `database.log` fayllarini yarating.
3. `.gitignore` faylini yaratib, uning ichiga `*.log` qoidasini yozing.
4. `git status` orqali `database.log` ning e'tiborsiz qoldirilganini tekshiring.
5. Qolgan fayllarni `git add .` qiling va `git commit -m "feat: dastlabki fayllar yaratildi"` izohi bilan birinchi commitni amalga oshiring.
6. `README.md` fayliga bitta yangi qator qo'shib, uni ikkinchi commit bilan tarixga saqlang (`git commit -m "docs: README yangilandi"`).
7. `git log --oneline` natijasini daftaringizga ko'chirib yozing.
*(Kutiladigan vaqt: 25 daqiqa)*

---

## Mentor uchun

- **Tekshirish mezonlari:**
  1. O'quvchi jarayonlarni fonga o'tkazish (`&`, `Ctrl+Z`, `bg`, `fg`) va to'xtatish (`kill`, `killall`) mexanizmini to'liq o'zlashtirganmi.
  2. `df` va `du` buyruqlarining amaliy farqi tushunilganmi (umumiy bo'lim vs aniq katalog).
  3. `apt update` va `apt install` mantiqan to'g'ri ketma-ketlikda bajarilganmi.
  4. Git'ning 3 ta hududi (Working, Staging, Repo) to'g'ri qo'llanganmi, commit izohlari standart qolipda yozilganmi.
  5. `.gitignore` fayli orqali loglar to'g'ri filtrlanganmi.
- **Tez-tez uchraydigan xatolar:**
  - `kill` buyrug'iga job raqami (`%1`) o'rniga oddiy raqam berish yoki PID raqami bilan adashtirish.
  - `git commit` qilishdan oldin `git add` qilishni unutish (Changes not staged for commit).
  - `.gitignore` ga fayl qo'shishdan oldin uni allaqachon commit qilib qo'yish (kuzatuvga kirib qolgan faylni keshdan tozalash kerak bo'ladi).
