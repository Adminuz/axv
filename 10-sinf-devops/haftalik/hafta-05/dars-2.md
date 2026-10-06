# 14-dars. Linux jarayonlari va rejalashtirish: cron, crontab, at va tizim monitoringi (htop, iotop)

**Darsning maqsadi:** O'quvchi jarayonlarni ko'radi va boshqaradi (`ps`, `top`, `htop`, `kill`), disk yuklamasini `iotop` bilan kuzatadi, `crontab` da takrorlanuvchi vazifa yozadi (5 maydon), `at` bilan bir martalik vazifa rejalashtiradi.

**Manba (rasmiy hujjat):** O'quv qo'llanma va uslubiy ko'rsatma: `ps aux`, `ps aux | grep ssh`, `kill`, `top` (resurs monitoringi) jadvali. `cron`, `crontab`, `at`, `htop`, `iotop` hujjatda alohida yoritilmagan, rejadagi mavzu bo'yicha qo'shildi.

**Vaqt taqsimoti (80 daqiqa):**
- Takrorlash: 10 daqiqa (grep, sed, awk, xargs)
- 01. Jarayonlar: 15 daqiqa
- 02. cron va crontab: 15 daqiqa
- Tanaffus: 5 daqiqa
- 03. at buyrug'i: 15 daqiqa
- Amaliyot: 15 daqiqa
- Xulosa va tezkor nazorat: 5 daqiqa

---

## 1. Konspekt (mentor uchun)

### 1.1. Jarayonlar va tizim monitoringi
Har bir ishlayotgan dastur — jarayon, uning PID raqami bor. `ps aux` barcha jarayonlarni ko'rsatadi, `ps aux | grep ssh` esa kerakli birini topadi. `top` real vaqtda CPU va xotira yuklamasini ko'rsatadi. `htop` — rangli, interaktiv variant (`F6` saralash, `F4` filtr, `F9` to'xtatish). `iotop` disk o'qish/yozish yuklamasini jarayonlar bo'yicha ko'rsatadi, administrator huquqi kerak. O'rnatish: `sudo apt install htop iotop`.
```bash
ps aux | grep ssh
top
sudo apt install htop iotop
htop
sudo iotop -o
sleep 300 &
kill 12345
kill -9 12345
```
Avval `kill PID` (SIGTERM) ni ishlating, `kill -9` (SIGKILL) faqat jarayon javob bermasa. Tizim jarayonlarini to'xtatmang.

### 1.2. cron va crontab
`cron` — vazifalarni vaqt bo'yicha avtomatik bajaruvchi xizmat. Vazifalar `crontab` faylida yoziladi: `crontab -e` (tahrirlash), `crontab -l` (ko'rish), `crontab -r` (hammasini o'chirish). Har qator 5 vaqt maydoni va buyruqdan iborat: **daqiqa soat kun oy hafta_kuni**. `*` — har qanday, `*/5` — har 5 birlikda, `1-5` — oraliq, `1,15` — ro'yxat. Haftaning kuni: 0 yoki 7 — yakshanba, 1 — dushanba.
```bash
# daq soat kun oy hafta  buyruq
*/5 * * * *     /home/ali/tekshir.sh
30 2 * * *      /home/ali/zaxira.sh
0 9 * * 1-5     /home/ali/hisobot.sh
0 0 1 * *       /home/ali/oylik.sh
@reboot         /home/ali/start.sh
```
Cron da PATH qisqa bo'ladi: skriptni to'liq yo'l bilan yozing. Natijani saqlash: `>> /home/ali/log.txt 2>&1`.

### 1.3. at: bir martalik rejalashtirish
`cron` takrorlanuvchi vazifalar uchun, `at` esa bir marta bajariladigan vazifa uchun. Vaqt ko'rsatiladi (`at 18:30`, `at now + 5 minutes`), keyin buyruq yoziladi va `Ctrl+D` bosiladi. Navbat: `atq`, bekor qilish: `atrm RAQAM`. Ishlashi uchun `atd` xizmati yoqilgan bo'lishi kerak: `sudo systemctl status atd`. Cron yozuvlarining bajarilishini `grep CRON /var/log/syslog` bilan kuzatish mumkin.
```bash
echo "echo salom > ~/salom.txt" | at now + 2 minutes
at 18:30
atq
atrm 3
sudo systemctl status atd
grep CRON /var/log/syslog
```
`at` va `cron` farqi: `at` bir marta, `cron` doimiy takror. Navbatda bo'lmagan vazifa raqamini `atrm` ga bermang.

---

## 2. Amaliy topshiriqlar va yechimlari

### 1-topshiriq (oson). Har 10 daqiqa
Har 10 daqiqada `tekshir.sh` ni ishga tushiruvchi crontab qatorini yozing.

**Yechim:**
```bash
*/10 * * * * /home/ali/tekshir.sh
```

### 2-topshiriq (o'rta). Ish kunlari
Dushanbadan jumagacha 08:30 da `hisobot.sh` ni ishga tushiring.

**Yechim:**
```bash
30 8 * * 1-5 /home/ali/hisobot.sh
```

### 3-topshiriq (o'rta). Log bilan
Har kuni 03:00 da `zaxira.sh` ishlasin, natija `zaxira.log` ga qo'shilib yozilsin.

**Yechim:**
```bash
0 3 * * * /home/ali/zaxira.sh >> /home/ali/zaxira.log 2>&1
```

### 4-topshiriq (qiyin). at va jarayon
2 daqiqadan keyin `salom.txt` yarating, navbatni ko'ring; `sleep 300 &` jarayonini toping va to'xtating.

**Yechim:**
```bash
echo "echo salom > ~/salom.txt" | at now + 2 minutes
atq
sleep 300 &
ps aux | grep [s]leep
kill PID
```

---

## 3. Tezkor nazorat
1. **cron va at farqi nima?** *Javob:* cron takrorlanuvchi, at bir martalik vazifa.
2. **`*/15 * * * *` nima?** *Javob:* Har 15 daqiqada.
3. **`crontab -l` nima qiladi?** *Javob:* Joriy foydalanuvchining cron vazifalarini ko'rsatadi.
4. **`iotop` nima ko'rsatadi?** *Javob:* Jarayonlarning disk o'qish/yozish yuklamasini.
5. **Nega skriptni to'liq yo'l bilan yozamiz?** *Javob:* Cron da PATH qisqa bo'ladi, nisbiy yo'l topilmasligi mumkin.

## Mentor uchun eslatma
Hujjatda faqat `ps aux`, `ps aux | grep ssh`, `kill` va `top` bor; `cron`, `at`, `htop`, `iotop` rejadagi mavzu bo'yicha qo'shildi. `iotop` va `at` sinfdagi kompyuterlarda o'rnatilmagan bo'lishi mumkin: `sudo apt install iotop at`. O'quvchi cron ga `* * * * *` qo'ysa, sinovdan keyin o'chirishini nazorat qiling. Cron ni sinash uchun saytlarga ko'p so'rov yuboruvchi vazifalarni yozdirmang.
