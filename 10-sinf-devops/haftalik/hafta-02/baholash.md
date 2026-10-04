# 10-sinf (DevOps): 2-hafta baholash qaydnomasi

**Mavzular:**
1. Xizmatlar va jarayonlarni boshqarish (ps, top, htop, nice, kill signallari, systemd va systemctl)
2. Disk, fayl tizimlari (df, du, fdisk, mount) va paket menejerlari (APT, DNF, paketlarni o'rnatish va yangilash)
3. Git va versiya boshqaruvi tizimlariga kirish: VCS konsepsiyasi, git init, status, add, commit, log va .gitignore

---

## Baholash mezonlari

| Mezon | Tavsif | Maks. ball |
|---|---|---|
| **Jarayonlar va Xizmatlar** | PID, Foreground/Background boshqaruvi, signallar (SIGTERM/SIGKILL), systemctl amallari | 30 ball |
| **Disklar va Paketlar** | df -h, du -sh saralash, blokli qurilmalar, mount nuqtasi, apt update/install/purge | 30 ball |
| **Git Asoslari va Amaliyot** | 3 ta hudud (Working, Staging, Repo), git init, add, commit, log va .gitignore sozlash | 40 ball |
| **JAMI** | | **100 ball** |

---

## O'quvchilar natijalari jadvali

| № | O'quvchi F.I.Sh. | Jarayonlar (30) | Disk & Paket (30) | Git Asoslari (40) | Jami ball (100) | Izoh |
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

- **Darsdagi asosiy qiyinchiliklar:** O'quvchilar Git'da faylni o'zgartirgandan keyin to'g'ridan-to'g'ri `git commit` qilishga urinishlari va «no changes added to commit» xatoligiga uchrashlari mumkin. `git add` ning zarurati (Staging Area bosqichi) yana bir bor amalda ko'rsatilishi lozim.
- **Iqtidorli o'quvchilar uchun:** `systemd` xizmati sifatida oddiy Python veb-skriptini avtomat ishga tushuvchi daemon qilish yoki `ncdu` bilan butun tizim bo'yicha eng katta fayllarni xaritada tahlil qilish topshirig'i berilishi mumkin.
