# 16-dars. Unix/Linux muhiti: fayl tizimi, ruxsatlar, xizmatlar va loglar

**Hafta:** 6 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + terminal amaliyoti · **II-bob**, 16-dars (umumiy 1–51)

**Manba:** O'quv qo'llanma, II bob, «Unix/Linux muhiti va tarmoq xizmati konfiguratsiyasi: SSH hamda Nginx reverse-proxyga kirish», «Unix/Linux asoslari» bo'limi (2.1–2.3-jadvallar); o'quv dasturi, II bob. `chmod`/`umask` hisob-kitoblari va mashqlar mualliflik; buyruqlar terminalda sinab ko'rilgan.

## 1. Dars rejasi

**Maqsad:** II bobni boshlash: Linux fayl tizimi iyerarxiyasini (`/etc`, `/var/log`, `/home`, `/usr/bin`...), ruxsatlar modelini (egasi, guruh, boshqalar; `rwx` va oktal), `chmod`, `chown`, `umask`, `systemctl` va `journalctl` bilan xizmat boshqaruvini, loglar va tarmoq diagnostikasi buyruqlarini (`ip a`, `ss -lntp`, `curl -I`, `dig`) o'rgatish.

**Kutiladigan natija:**
- Linux asosiy kataloglarining vazifasini aytadi (`/etc`, `/var/log`, `/home`, `/opt`).
- `rwx` va oktal ruxsatlarni (`750`, `644`) o'qiydi va `chmod`, `chown` bilan o'zgartiradi.
- `umask 022` bo'lganda yangi fayl va katalog ruxsatini hisoblaydi (644 va 755).
- `systemctl status/restart/enable` va `journalctl -u ... -f` bilan xizmatni boshqaradi va logni o'qiydi.
- `ip a`, `ss -lntp`, `curl -I`, `dig` bilan tarmoqni tekshiradi.

**Kerakli jihozlar:**
- Linux (Ubuntu/Debian) virtual mashina yoki WSL
- Terminal va `sudo` huquqi
- Mini-loyiha papkasi (`library-api`)

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va kirish | Oraliq nazorat tahlili (kuchsiz mavzular) |
| 10–35 daq | Yangi mavzu | Fayl tizimi iyerarxiyasi va ruxsatlar (`chmod`, `chown`, `umask`); `systemd` va loglar: `systemctl`, `journalctl` |
| 35–40 daq | Tanaffus | Harakatli tanaffus |
| 40–65 daq | Amaliyot | Terminalda 3 ta mashq: ruxsat, xizmat, tarmoq |
| 65–75 daq | Tezkor nazorat | 5 ta savol; Minimal ruxsat qoidasi va xulosa |
| 75–80 daq | Xulosa va uyga vazifa | Keyingi darsga ko'prik |

---

## 2. Dars konspekti

### 2.1. Fayl tizimi iyerarxiyasi va ruxsatlar

Linux da hamma narsa **fayl**, daraxt `/` (root) dan boshlanadi. Asosiy kataloglar (2.1-jadval): `/etc` — sozlamalar (`/etc/ssh/sshd_config`), `/var/log` — loglar, `/usr/bin` va `/usr/sbin` — dasturlar, `/home/<user>` — uy papkasi, `/opt` — uchinchi tomon ilovalari, `/tmp` — vaqtinchalik. Ruxsat 3 doirada beriladi: **egasi**, **guruh**, **boshqalar**; har birida `r` (4), `w` (2), `x` (1). `-rwxr-x---` = egaga 7, guruhga 5, boshqalarga 0 → **750**. `chmod 750 script.sh` ruxsatni, `chown odil:dev script.sh` egasi va guruhni o'zgartiradi. **umask** yangi fayl ruxsatini belgilaydi: `umask 022` da fayl 644, katalog 755.

```bash
pwd
ls -la
chmod 750 script.sh
chown odil:dev script.sh
umask 022
touch yangi.txt && mkdir yangi_katalog
ls -ld yangi.txt yangi_katalog
```

Oddiy ishlarni oddiy foydalanuvchi sifatida bajaring, `sudo` ni faqat zarur bo'lganda ishlating (minimal ruxsat qoidasi). Konfiguratsiyani `sudoedit`, sudoers ni `visudo` bilan tahrirlang.

### 2.2. systemctl, journalctl va loglar

Zamonaviy Linux da xizmatlarni **systemd** boshqaradi. Uch odat: `systemctl status nginx` — holatni ko'rish (`active (running)`, `inactive (dead)` yoki `failed`), `start/stop/restart/enable` — hayot sikli, `journalctl -u nginx -f` — xizmat logini jonli kuzatish. `failed` bo'lsa, darhol jurnalga qarab sababini toping. Xizmat unit fayllari `/etc/systemd/system/*.service` da turadi. Loglar `/var/log` (masalan `/var/log/syslog`) yoki `journalctl` da. Disk to'lishi — eng oddiy va og'riqli muammo: `df -h` bo'sh joyni, `du -sh /var/log/* | sort -h | tail` katta loglarni ko'rsatadi.

```bash
systemctl status nginx
sudo systemctl restart nginx
sudo systemctl enable nginx
journalctl -u nginx -f
df -h
du -sh /var/log/* | sort -h | tail
```

`enable` xizmatni server qayta yonganda ham avtomatik ishga tushiradi; `start` faqat hozir ishga tushiradi.

### 2.3. Tarmoq buyruqlari va quvur (pipe)

Tarmoq bilan ishlashda bir nechta buyruq yetarli (2.3-jadval): `ip a` — interfeyslar va IP, `ip route` — marshrutlar, **`ss -lntp`** — qaysi portni qaysi jarayon tinglayapti, `curl -I https://...` — HTTP sarlavhalar (200, 301, 4xx), `dig A example.com` — DNS yozuvi, `ping -c 3 8.8.8.8` — aloqa. Shell ning kuchi — **quvur** (`|`): bitta buyruq chiqishi keyingisiga kirish bo'ladi. `grep -i error error.log | tail -n 50` oxirgi xatolarni ko'rsatadi; `awk '{print $1}' access.log | sort | uniq -c | sort -nr | head` eng ko'p kirgan IP larni chiqaradi. Bu reflekslar Nginx ni sozlaganda juda kerak: port ochiqmi, DNS to'g'rimi, javob qanday sarlavhalar bilan keladi.

```bash
ip a
ss -lntp
curl -I https://example.com
dig A example.com
grep -i error error.log | tail -n 50
awk '{print $1}' access.log | sort | uniq -c | sort -nr | head
```

`ss -lntp` ni ko'p holda `sudo` bilan yozing: jarayon nomlarini ko'rsatish uchun huquq kerak.

### Qo'shimcha kod: Ruxsat va umask ni sinash (skript):

```bash
#!/usr/bin/env bash
umask 022
touch fayl.txt
mkdir katalog
ls -ld fayl.txt katalog    # -rw-r--r--  va  drwxr-xr-x
chmod 750 fayl.txt
ls -l fayl.txt             # -rwxr-x---
```

---

## 3. Amaliy mashg'ulot (mini-loyiha: «Kutubxona boshqaruvi» serveri)

Linux terminalida `library-api` papkasini yarating, ichida `app.log` va `deploy.sh` fayllarini ochib ruxsatlarni sozlang (`deploy.sh` — 750, `app.log` — 640). Keyin `systemctl status` bilan biror xizmat holatini ko'ring, `journalctl -u <xizmat> -n 20` ni o'qing va `ss -lntp`, `curl -I`, `dig` bilan tarmoqni tekshiring.

### 1-mashq (oson). Oktal hisob
**Vazifa:** `rw-r-----` ruxsatni oktalda yozing va `chmod` buyrug'ini keltiring.

**Yechim:** 6 (rw-) + 4 (r--) + 0 = **640**; `chmod 640 fayl`.

### 2-mashq (oson). Katalog vazifasi
**Vazifa:** `/etc`, `/var/log`, `/home/odil` nimaga xizmat qiladi?

**Yechim:** `/etc` — sozlamalar; `/var/log` — loglar; `/home/odil` — foydalanuvchi uy papkasi.

### 3-mashq (o'rta). umask
**Vazifa:** `umask 022` da yangi fayl va katalog ruxsatini hisoblang.

**Yechim:** Fayl 666−022 = 644; katalog 777−022 = 755.

### 4-mashq (o'rta). Ruxsatni to'g'rilang
**Vazifa:** `deploy.sh` ni faqat egasi bajara oladigan, guruh o'qiydigan qiling.

**Yechim:**
```bash
chmod 740 deploy.sh
chown odil:dev deploy.sh
```

### 5-mashq (qiyin). Xizmatni tiklang
**Vazifa:** `nginx` `failed` bo'ldi. Sababini toping va qayta ishga tushiring.

**Yechim:**
```bash
systemctl status nginx
journalctl -u nginx -n 50
sudo nginx -t
sudo systemctl restart nginx
```

### 6-mashq (bonus). Eng ko'p IP
**Vazifa:** `access.log` dan eng ko'p kirgan 5 ta IP ni chiqaring.

**Yechim:**
```bash
awk '{print $1}' access.log | sort | uniq -c | sort -nr | head -5
```

---

## 4. Tezkor savollar

1. `rwxr-x---` oktalda nima?
   - **Javob:** 750.
2. `umask 022` da fayl va katalog ruxsati?
   - **Javob:** Fayl 644, katalog 755.
3. `systemctl status` nima uchun?
   - **Javob:** Xizmat holatini ko'rsatadi: active, inactive yoki failed.
4. Loglar qayerda?
   - **Javob:** `/var/log` va `journalctl`.
5. `ss -lntp` nimani ko'rsatadi?
   - **Javob:** Tinglayotgan portlar va ularning jarayonlarini.

## 5. Mentor uchun eslatmalar

- Mashqlarni virtual mashina yoki WSL da bajarish; ish kompyuterida `sudo` bilan tajriba qilmang.
- Oraliq nazoratdan aniqlangan kuchsiz mavzularni dars boshida 3–5 daqiqada takrorlang (5-hafta baholash tavsiyasi).
- Qo'llanmada `chmod`, `umask`, `systemd`, tarmoq buyruqlari tushuntirilgan; `chmod 750`, `umask` hisobi va skript namunasi mualliflik, terminalda sinab ko'rilgan.
- `systemctl` va `journalctl` WSL1 da ishlamasligi mumkin: WSL2 yoki virtual mashina kerak.
- Keyingi dars: SSH kalitlari. `~/.ssh` ruxsatlari (700/600) bugungi ruxsat mavzusiga tayanadi.
