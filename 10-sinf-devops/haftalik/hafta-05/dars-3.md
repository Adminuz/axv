# 15-dars. Linux xavfsizligi va foydalanuvchilar: useradd, usermod, sudoers, SSH kalitlar bilan xavfsiz ulanish

**Darsning maqsadi:** O'quvchi foydalanuvchi va guruh yaratadi va boshqaradi (`useradd`, `passwd`, `usermod`, `userdel`), `sudo` huquqini `visudo` bilan xavfsiz beradi va SSH kalit juftligini yaratib, parolsiz xavfsiz ulanishni sozlaydi.

**Manba (rasmiy hujjat):** O'quv qo'llanma va uslubiy ko'rsatma: ruxsatlar tizimi (`chmod`, `chown`, `sudo`), `sudo usermod -aG docker $USER`, Git bobida SSH kalit yaratish (`ed25519`) va GitHub ga qo'shish. `useradd`, `sudoers` va serverda SSH kalit bilan kirish rejadagi mavzu bo'yicha qo'shildi.

**Vaqt taqsimoti (80 daqiqa):**
- Takrorlash: 10 daqiqa (cron, at va monitoring)
- 01. Foydalanuvchilar: 15 daqiqa
- 02. sudo va sudoers: 15 daqiqa
- Tanaffus: 5 daqiqa
- 03. SSH kalitlar: 15 daqiqa
- Amaliyot: 15 daqiqa
- Xulosa va tezkor nazorat: 5 daqiqa

---

## 1. Konspekt (mentor uchun)

### 1.1. Foydalanuvchi va guruhlarni boshqarish
Har bir foydalanuvchi alohida hisob bilan ishlaydi: kim nima qilganini kuzatish va huquqni cheklash mumkin. `sudo useradd -m -s /bin/bash ali` uy papkasi bilan hisob yaratadi, `sudo passwd ali` parol beradi, `id ali` va `groups ali` tekshiradi. `usermod` mavjud hisobni o'zgartiradi: `sudo usermod -aG docker ali` guruhga **qo'shadi** (`-a` siz eski guruhlar o'chib ketadi!). `sudo usermod -L ali` hisobni bloklaydi, `sudo userdel -r ali` uy papkasi bilan o'chiradi. Ma'lumotlar `/etc/passwd`, `/etc/group` da, parol xeshlari `/etc/shadow` da saqlanadi.
```bash
sudo useradd -m -s /bin/bash ali
sudo passwd ali
id ali
sudo usermod -aG docker ali
groups ali
sudo usermod -L ali
sudo userdel -r ali
```
`usermod -G docker ali` (`-a` siz) ali ning boshqa guruhlarini o'chirib yuboradi. Doim `-aG` yozing.

### 1.2. sudo huquqi va sudoers fayli
Ish uchun root hisobiga o'tmaslik, kerak bo'lganda `sudo` bilan bitta buyruqni administrator huquqida bajarish xavfsizroq. Kim sudo ishlata olishi `/etc/sudoers` da belgilanadi. Uni faqat `sudo visudo` bilan tahrirlang: u saqlashdan oldin sintaksisni tekshiradi. Eng oddiy yo'l: foydalanuvchini `sudo` guruhiga qo'shish (`usermod -aG sudo ali`). Alohida qoidalar `/etc/sudoers.d/` papkasida bo'lishi mumkin. `sudo -l` o'zingizga ruxsat etilgan buyruqlarni ko'rsatadi.
```bash
sudo usermod -aG sudo ali
sudo visudo
# ali bitta foydalanuvchi uchun:
ali ALL=(ALL:ALL) ALL
# guruh uchun:
%sudo ALL=(ALL:ALL) ALL
sudo -l
```
`NOPASSWD` parolsiz sudo beradi: faqat juda zarur va cheklangan buyruqlar uchun. `sudoers` ni oddiy muharrirda tahrirlash xatosi sudo ni butunlay buzishi mumkin.

### 1.3. SSH kalit juftligi va xavfsiz ulanish
SSH kalit juftligi: **shaxsiy** kalit (sizda qoladi) va **ochiq** kalit (`.pub`, serverga qo'yiladi). Zamonaviy va tez algoritm — `ed25519` (O'quv qo'llanmada Git uchun ham shu tavsiya etilgan). Yaratish: `ssh-keygen -t ed25519 -C "ali@maktab"`. Serverga o'tkazish: `ssh-copy-id ali@server`. Keyin `ssh ali@server` parolsiz ulaydi. Ruxsatlar qat'iy: `~/.ssh` — 700, `authorized_keys` va shaxsiy kalit — 600. Serverda `/etc/ssh/sshd_config` da `PasswordAuthentication no` va `PermitRootLogin no` qo'yilsa, xavfsizlik oshadi.
```bash
ssh-keygen -t ed25519 -C "ali@maktab"
ssh-copy-id ali@192.168.1.10
ssh ali@192.168.1.10
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
# sshd_config (serverda):
PasswordAuthentication no
PermitRootLogin no
sudo systemctl restart ssh
```
`sshd_config` ni o'zgartirishdan oldin joriy SSH sessiyani yopmang va boshqa terminalda kalit bilan kirishni sinab ko'ring: aks holda serverdan chiqib qolishingiz mumkin. Shaxsiy kalitni (`id_ed25519`) hech kimga bermang.

---

## 2. Amaliy topshiriqlar va yechimlari

### 1-topshiriq (oson). Hisob yaratish
`ali` foydalanuvchisini uy papkasi va bash bilan yarating va parol bering.

**Yechim:**
```bash
sudo useradd -m -s /bin/bash ali
sudo passwd ali
```

### 2-topshiriq (o'rta). Guruhga qo'shish
`ali` ni `docker` guruhiga mavjud guruhlarini saqlagan holda qo'shing va tekshiring.

**Yechim:**
```bash
sudo usermod -aG docker ali
id ali
```

### 3-topshiriq (o'rta). Sudo huquqi
`ali` ga sudo huquqini xavfsiz usulda bering.

**Yechim:**
```bash
sudo usermod -aG sudo ali
sudo -l -U ali
```

### 4-topshiriq (qiyin). SSH kirish
Kalit juftligini yarating, ochiq kalitni serverga o'tkazing va ulaning; ruxsatlarni to'g'rilang.

**Yechim:**
```bash
ssh-keygen -t ed25519 -C "ali@maktab"
ssh-copy-id ali@192.168.1.10
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
ssh ali@192.168.1.10
```

---

## 3. Tezkor nazorat
1. **`usermod -aG` dagi `-a` nima qiladi?** *Javob:* Mavjud guruhlarni saqlab, yangisiga qo'shadi.
2. **`/etc/sudoers` ni nima bilan tahrirlaymiz?** *Javob:* `sudo visudo` bilan: u sintaksisni tekshiradi.
3. **Qaysi kalit serverga qo'yiladi?** *Javob:* Ochiq (`.pub`).
4. **`~/.ssh` ruxsati nechi bo'lishi kerak?** *Javob:* 700 (authorized_keys va shaxsiy kalit 600).
5. **`PasswordAuthentication no` nima qiladi?** *Javob:* Parol bilan SSH kirishni o'chiradi, faqat kalit qoladi.

## Mentor uchun eslatma
Hujjatda `sudo usermod -aG docker $USER` va SSH kalit (`ed25519`) Git bo'limida bor; `useradd`, `sudoers` va serverga kalitli kirish rejadagi mavzu bo'yicha qo'shildi. Mashqlarni faqat sinf serveri yoki virtual mashinada bajaring; o'quvchi shaxsiy kompyuterida `userdel` ni sinab ko'rmasin. `sshd_config` o'zgartirilgach, joriy sessiyani yopmay, yangi terminalda sinash shartini alohida ta'kidlang. Shaxsiy kalitni (`id_ed25519`) messenjerda yoki GitHub ga yuklash xatosiga e'tibor bering. Keyingi hafta Git ilg'or texnikalari (stash, rebase, cherry-pick, reflog) bilan boshlanadi.
