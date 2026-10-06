# 5-hafta: Uyga vazifalar (DevOps)

5-haftada matn bilan ishlash vositalari (`grep`, `sed`, `awk`, `xargs`), jarayonlar va rejalashtirish (`cron`, `at`, `htop`, `iotop`) hamda foydalanuvchilar va SSH kalitlar o'rganildi. Quyidagi topshiriqlar shu ko'nikmalarni mustahkamlaydi.

---

## 13-dars vazifasi: grep, sed, awk va xargs

1. `app.log` ga kamida 10 qator yozing (INFO, WARN, ERROR aralash).
2. `grep -c` bilan har daraja sonini toping.
3. `awk` bilan faqat ERROR qatorlaridagi foydalanuvchi nomlarini ajrating.
4. `sed` bilan ERROR ni XATO ga almashtiring (natijani yangi faylga yo'naltiring).
5. `tahlil.sh` skriptiga hammasini yig'ib, natijani daftaringizga yozing.
*(Kutiladigan vaqt: 25 daqiqa)*

---

## 14-dars vazifasi: cron, at va monitoring

1. `tekshir.sh` yozing: sana va bo'sh disk joyini (`df -h /`) `~/tekshir.log` ga qo'shib yozsin.
2. Skriptni `chmod +x` qiling va to'liq yo'l bilan har 5 daqiqada ishlaydigan crontab qatorini qo'shing.
3. `crontab -l` natijasini va `tekshir.log` ning bir nechta qatorini daftaringizga yozing, so'ng vazifani o'chiring.
4. `at now + 3 minutes` bilan `salom.txt` yarating; `atq` ni tekshiring.
5. `htop` va `iotop` ekranini tavsiflang: eng ko'p CPU va disk ishlatgan 3 jarayon nomini yozing.
*(Kutiladigan vaqt: 25 daqiqa)*

---

## 15-dars vazifasi: Foydalanuvchilar, sudoers va SSH

1. Virtual mashinada `dasturchi1` hisobini yarating (`useradd -m -s /bin/bash`) va parol bering.
2. `dasturchi1` ni `sudo` va `docker` guruhlariga `-aG` bilan qo'shing; `id` natijasini yozing.
3. `ssh-keygen -t ed25519` bilan kalit yarating; ochiq va shaxsiy kalit fayllarini tavsiflang.
4. `~/.ssh` va kalit fayllariga to'g'ri ruxsatlarni bering (`chmod 700`, `chmod 600`).
5. `sshd_config` da xavfsizlik sozlamalari (parolni o'chirish, root kirishini taqiqlash) ni sinfdagi namunaviy serverda ko'rsating yoki daftarga yozing.
*(Kutiladigan vaqt: 25 daqiqa)*

---

## Mentor uchun

- **Tekshirish mezonlari:**
  1. `grep`, `sed`, `awk` buyruqlari to'g'ri flaglar bilan ishlatilgan, natija `app.log` bo'yicha to'g'ri.
  2. Cron qatori 5 maydon bilan to'g'ri yozilgan, skript to'liq yo'l bilan chaqirilgan va bajariladigan (`chmod +x`).
  3. `at` vazifasi navbatda ko'rinadi (`atq`), jarayonni to'xtatish `kill` bilan bajarilgan.
  4. Foydalanuvchi `useradd -m` bilan yaratilgan, guruhga `-aG` bilan qo'shilgan.
  5. SSH kalit `ed25519`, ruxsatlar 700/600, shaxsiy kalit hech kimga uzatilmagan.
- **Tez-tez uchraydigan xatolar:**
  - Naqshni tirnoqqa olmaslik; `grep` ning o'zini jarayon sifatida topishi.
  - Cron da `* * * * *` ni sinovdan keyin o'chirmaslik.
  - `usermod -G` ni `-a` siz yozish.
  - Shaxsiy kalitni (`id_ed25519`) ulashish yoki `.pub` bilan adashtirish.
