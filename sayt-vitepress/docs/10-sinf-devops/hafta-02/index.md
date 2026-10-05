---
title: "2-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "10-sinf (DevOps)", "link": "/10-sinf-devops/"}, "n": 2, "bob": "I-bob · Operatsion tizimlar (Linux)", "lessons": [{"g": 4, "title": "Xizmatlar va jarayonlarni boshqarish (ps, top, kill, systemd)", "lead": "Linux operatsion tizimi tomir urishi: jarayonlar monitoringi (ps, top), boshqaruv signallari (kill, nice) hamda doimiy ishlovchi xizmatlar (systemd/systemctl).", "link": "/10-sinf-devops/hafta-02/dars-1", "slide": "/slaydlar/10-sinf-devops/hafta-02/dars-1.html", "test": "/slaydlar/10-sinf-devops/hafta-02/dars-1-test.html"}, {"g": 5, "title": "Disklar, fayl tizimlari va paket menejerlari (APT, DNF)", "lead": "Linuxda xotira boshqaruvi: disklar va bo'limlar arxitekturasi (df, du, mount), zamonaviy fayl tizimlari hamda xavfsiz dastur o'rnatish tizimi (APT/DNF).", "link": "/10-sinf-devops/hafta-02/dars-2", "slide": "/slaydlar/10-sinf-devops/hafta-02/dars-2.html", "test": "/slaydlar/10-sinf-devops/hafta-02/dars-2-test.html"}, {"g": 6, "title": "Git va versiya boshqaruvi tizimlariga kirish (Git asoslari)", "lead": "Dasturiy ta'minotning vaqt mashinasi: Git versiya boshqaruvi, 3 ta hudud (Working, Staging, Repository), commitlar anatomiyasi va .gitignore sirlari.", "link": "/10-sinf-devops/hafta-02/dars-3", "slide": "/slaydlar/10-sinf-devops/hafta-02/dars-3.html", "test": "/slaydlar/10-sinf-devops/hafta-02/dars-3-test.html"}], "test": "/slaydlar/10-sinf-devops/hafta-02/hafta-test.html"}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

2-haftada jarayonlar (processes) va systemd xizmatlarini boshqarish, disklar va fayl tizimlari tahlili (df/du), paket menejerlari (APT) hamda Git versiya boshqaruvi tizimining poydevori (init, add, commit, .gitignore) o'rganildi. Quyidagi vazifalar amaliy ko'nikmalarni mustahkamlash uchun berilgan.

---

### 4-dars vazifasi: Jarayonlar va Xizmatlar

1. Terminalda `top` yoki `htop` dasturini oching. Tizimingizda umumiy nechta jarayon mavjudligi, ulardan nechtasi faol («running») holatda ekanini daftaringizga qayd eting.
2. `sleep 400 &` buyrug'i yordamida yangi fon jarayonini ishga tushiring. `jobs` va `ps aux | grep sleep` buyruqlari yordamida uning PID raqamini aniqlang.
3. Aniqlangan PID raqami bo'yicha `kill [PID]` buyrug'i bilan ushbu jarayonni to'xtating.
4. `systemctl status cron` (yoki `crond`) buyrug'ini bajarib, rejalashtiruvchi xizmatning faol holatini tekshiring.
*(Kutiladigan vaqt: 25 daqiqa)*

---

### 5-dars vazifasi: Disk sarfi va Paketlar

1. `df -h` buyrug'ini bajaring va asosiy ildiz (`/`) bo'limida qancha umumiy hajm, ishlatilgan hajm va bo'sh joy qolganini aniqlang.
2. O'z uy katalogingizdagi barcha papkalar hajmini `du -sh ~/* | sort -h` orqali saralangan holda ko'ring va eng katta 3 ta papkani yozib oling.
3. `sudo apt update` buyrug'i orqali paketlar indeksini yangilang, so'ngra `sudo apt install -y curl wget ncdu` buyruqlari bilan ushbu utilitalarni o'rnating.
4. `ncdu ~` dasturini ishga tushirib, interaktiv terminal orqali xotira taqsimotini tahlil qiling.
*(Kutiladigan vaqt: 25 daqiqa)*

---

### 6-dars vazifasi: Git va Repozitoriya asoslari

1. Uy katalogingizda `my_git_lab` nomli yangi papka oching va uni `git init` orqali Git omboriga aylantiring.
2. Repozitoriya ichida `app.py`, `README.md` va `database.log` fayllarini yarating.
3. `.gitignore` faylini yaratib, uning ichiga `*.log` qoidasini yozing.
4. `git status` orqali `database.log` ning e'tiborsiz qoldirilganini tekshiring.
5. Qolgan fayllarni `git add .` qiling va `git commit -m "feat: dastlabki fayllar yaratildi"` izohi bilan birinchi commitni amalga oshiring.
6. `README.md` fayliga bitta yangi qator qo'shib, uni ikkinchi commit bilan tarixga saqlang (`git commit -m "docs: README yangilandi"`).
7. `git log --oneline` natijasini daftaringizga ko'chirib yozing.
*(Kutiladigan vaqt: 25 daqiqa)*

---

</div>
