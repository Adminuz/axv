# 10-sinf (DevOps): 5-hafta baholash qaydnomasi

**Mavzular:**
1. Matn filtralari va muntazam ifodalar: `grep`, regex, `sed`, `awk`, `xargs`
2. Linux jarayonlari va rejalashtirish: `ps`, `top`, `htop`, `iotop`, `cron`, `crontab`, `at`
3. Linux xavfsizligi va foydalanuvchilar: `useradd`, `usermod`, `sudoers`, SSH kalitlar

---

## Baholash mezonlari

| Mezon | Tavsif | Maks. ball |
|---|---|---|
| **Matn filtralari** | `grep` flaglari, regex naqshlari, `sed` almashtirish, `awk` ustunlari, `xargs` zanjirlari | 35 ball |
| **Jarayonlar va rejalashtirish** | `ps`/`top`/`htop`/`iotop`, `kill`, crontab 5 maydon, `at` | 35 ball |
| **Foydalanuvchilar va SSH** | `useradd`/`usermod -aG`, `visudo`, sudo huquqi, SSH kalit va ruxsatlar | 30 ball |
| **JAMI** | | **100 ball** |

---

## O'quvchilar natijalari jadvali

| № | O'quvchi F.I.Sh. | Matn filtralari (35) | Jarayonlar/cron (35) | Foydalanuvchilar/SSH (30) | Jami ball (100) | Izoh |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |
| 9 | | | | | | |
| 10 | | | | | | |
| 11 | | | | | | |
| 12 | | | | | | |

---

## Mentor qaydlari va tahlil

- **Darsdagi asosiy qiyinchiliklar:** naqshni tirnoqsiz yozish, `awk` ustun raqamini adashtirish, cron da daqiqa va soat o'rnini almashtirish, nisbiy yo'l ishlatish, `usermod -aG` da `-a` ni unutish, `~/.ssh` ruxsatlari.
- **Iqtidorli o'quvchilar uchun:** loglarni tahlil qiluvchi `loganaliz.sh` (grep, awk, sort, uniq birga) yoki cron bilan avtomatik disk monitoringi.
- **Xavfsizlik:** `userdel`, `kill -9`, `sshd_config` mashqlari faqat laboratoriya muhitida bajarilganini tekshiring.
