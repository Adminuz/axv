# 17-dars. SSH: kalitga asoslangan autentifikatsiya va xavfsiz ulanish

**Hafta:** 6 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + terminal amaliyoti · **II-bob**, 17-dars (umumiy 1–51)

**Manba:** O'quv qo'llanma, II bob, «SSH: kalitga asoslangan autentifikatsiya» bo'limi (kalit juftligi, `ssh-keygen -t ed25519`, `ssh-copy-id`, `authorized_keys`, `sshd_config`, `ssh-agent`, `~/.ssh/config`, kalit cheklovlari, diagnostika `ssh -vvv`); o'quv dasturi. Mashqlar mualliflik; `ssh-keygen` terminalda sinab ko'rilgan.

## 1. Dars rejasi

**Maqsad:** SSH ning ikki rejimini (parol va kalit), kalit juftligi mantig'ini (shaxsiy va ommaviy kalit), `ssh-keygen -t ed25519`, `ssh-copy-id`, `authorized_keys` va ruxsatlarni, `sshd_config` ni qattiqlashtirishni (`PasswordAuthentication no`), `ssh-agent`, `~/.ssh/config` va xatolarni `ssh -vvv` bilan topishni o'rgatish.

**Kutiladigan natija:**
- Parol va kalit autentifikatsiyasi farqini tushuntiradi.
- `ssh-keygen -t ed25519 -C ...` bilan kalit juftini yaratadi, shaxsiy kalitni himoyalaydi.
- `ssh-copy-id` va `authorized_keys` orqali ommaviy kalitni serverga qo'yadi (700/600).
- `sshd_config` da `PasswordAuthentication no` va `PermitRootLogin no` ni xavfsiz yoqadi.
- `~/.ssh/config` va `ssh -vvv` bilan ulanishni soddalashtiradi va xatoni topadi.

**Kerakli jihozlar:**
- Linux/macOS terminali yoki Windows OpenSSH (WSL)
- Mashq uchun server (virtual mashina) yoki `localhost` da `sshd`
- `library-api` papkasi

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va kirish | 16-dars: ruxsatlar (700/600), `systemctl` |
| 10–35 daq | Yangi mavzu | Parol va kalit; kalit juftligi mantig'i; `ssh-keygen`; `ssh-copy-id`, `authorized_keys`, birinchi ulanish va `known_hosts` |
| 35–40 daq | Tanaffus | Harakatli tanaffus |
| 40–65 daq | Amaliyot | `sshd_config`, `ssh-agent`, `~/.ssh/config` bilan mashq |
| 65–75 daq | Tezkor nazorat | 5 ta savol; Xavfsizlik, kalit aylantirish, `ssh -vvv` diagnostika |
| 75–80 daq | Xulosa va uyga vazifa | Keyingi darsga ko'prik |

---

## 2. Dars konspekti

### 2.1. Kalit juftligi va ssh-keygen

SSH (Secure Shell) — masofaviy serverga xavfsiz ulanish uchun protokol. Parol tez, lekin zaif (brute-force, tinglash). **Kalit juftligi** kuchliroq: mijozda **shaxsiy (private)** va **ommaviy (public)** kalit yaratiladi. Ommaviy kalit serverga qo'yiladi, shaxsiy kalit **faqat sizda** qoladi va hech qachon ulashilmaydi. Ulanishda server shaxsiy kalit egasi ekaningizni kriptografik tekshiradi, parol tarmoq orqali yuborilmaydi. Tavsiya etilgan algoritm — **`ed25519`**; moslik uchun `rsa -b 4096`. Kalitga **passphrase** qo'ying: o'g'irlansa ham himoya bo'ladi.

```bash
ssh-keygen -t ed25519 -C "ali@maktab"
ls ~/.ssh
# id_ed25519      shaxsiy (sir)
# id_ed25519.pub  ommaviy
cat ~/.ssh/id_ed25519.pub
```

Shaxsiy kalit (`id_ed25519`) ni hech kimga bermang va GitHub ga qo'ymang. Faqat `.pub` faylni ulashing.

### 2.2. ssh-copy-id va authorized_keys

Ommaviy kalitni serverga qo'yishning eng oson yo'li — **`ssh-copy-id user@server`**: u masofadagi `~/.ssh/authorized_keys` fayliga satr qo'shadi va ruxsatlarni to'g'rilaydi. Qo'lda: `cat ~/.ssh/id_ed25519.pub` ni ko'chirib, serverda `authorized_keys` ga yangi qator qilib qo'shing. Ruxsatlar muhim: **`chmod 700 ~/.ssh`** va **`chmod 600 ~/.ssh/authorized_keys`**. Birinchi ulanishda SSH server barmoq izini `~/.ssh/known_hosts` ga qo'shishni so'raydi: bu **MITM** (o'rtadagi odam) hujumidan himoya, server kaliti o'zgarsa SSH ogohlantiradi.

```bash
ssh-copy-id user@203.0.113.10
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
ssh user@203.0.113.10
```

`203.0.113.10` — hujjatlarda ishlatiladigan namunaviy IP. Server kaliti o'zgarganida ogohlantirishni «o'chirib tashlash»ga shoshilmang: avval sababni tekshiring.

### 2.3. sshd_config, ssh-agent va ~/.ssh/config

Kalit ishlab turgach, parolni o'chiramiz: `/etc/ssh/sshd_config` da **`PubkeyAuthentication yes`**, **`PasswordAuthentication no`**, **`PermitRootLogin no`**, so'ng `sudo systemctl restart sshd` (ba'zi tizimlarda `ssh`). **Muhim:** parolni o'chirishdan oldin kalit bilan kira olayotganingizni boshqa terminalda tekshiring, aks holda serverdan tashqarida qolasiz. **`ssh-agent`** kalitni seans davomida xotirada ushlaydi (`ssh-add ~/.ssh/id_ed25519`). **`~/.ssh/config`** da `Host prod` nomi bilan `HostName`, `User`, `IdentityFile` yoziladi, keyin faqat `ssh prod` yetadi. Muammo bo'lsa, `ssh -vvv user@server` va serverda `journalctl -u sshd -f`.

```ini
# /etc/ssh/sshd_config
PubkeyAuthentication yes
PasswordAuthentication no
PermitRootLogin no

# ~/.ssh/config
Host prod
  HostName 203.0.113.10
  User deploy
  IdentityFile ~/.ssh/id_ed25519
```

Sozlamadan keyin `ssh prod` bilan ulaning. Ulana olmasangiz: `ssh -vvv prod` va serverdagi log, odatda sabab ruxsat yoki `authorized_keys` formatida.

### Qo'shimcha kod: authorized_keys da kalitni cheklash (qo'llanmadan)

```ini
from="203.0.113.0/24",no-agent-forwarding,no-port-forwarding,no-pty ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAA... ci-runner
```

---

## 3. Amaliy mashg'ulot (mini-loyiha: «Kutubxona boshqaruvi» serveri)

Virtual mashinada (yoki `localhost` da `sshd` bilan) `ed25519` kalit juftini yarating, ommaviy kalitni `ssh-copy-id` bilan qo'ying va parolsiz kiring. Keyin `~/.ssh/config` da `Host dev` yozing. Parolni o'chirishdan oldin ikkinchi terminalda kalit bilan kirishni sinab, `sshd_config` ni qattiqlashtiring. Xatoni ataylab yarating (`chmod 777 ~/.ssh`) va `ssh -vvv` bilan sababini toping.

### 1-mashq (oson). Kalit yarating
**Vazifa:** `ed25519` kalit juftini `ali@maktab` izohi bilan yarating.

**Yechim:**
```bash
ssh-keygen -t ed25519 -C "ali@maktab"
```

### 2-mashq (oson). Qaysi kalit?
**Vazifa:** Serverga qaysi faylni joylaymiz va qaysini yashiramiz?

**Yechim:** Serverga `id_ed25519.pub` (ommaviy); `id_ed25519` (shaxsiy) sirda qoladi.

### 3-mashq (o'rta). Ruxsatlar
**Vazifa:** SSH kalitlari ishlashi uchun ruxsatlarni to'g'rilang.

**Yechim:**
```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

### 4-mashq (o'rta). Config yozing
**Vazifa:** `prod` nomi bilan serverga `deploy` foydalanuvchisi bilan ulanishni yozing.

**Yechim:**
```bash
Host prod
  HostName 203.0.113.10
  User deploy
  IdentityFile ~/.ssh/id_ed25519
```

### 5-mashq (qiyin). Qattiqlashtirish
**Vazifa:** `sshd_config` da parol va root kirishni o'chiring, xavfsiz tartibni yozing.

**Yechim:** Avval kalit bilan kirishni sinang; keyin `PasswordAuthentication no`, `PermitRootLogin no`, `sudo systemctl restart sshd`.

### 6-mashq (bonus). Diagnostika
**Vazifa:** `Permission denied (publickey)` chiqdi. 4 ta tekshiruv yozing.

**Yechim:** 1) `~/.ssh` 700; 2) `authorized_keys` 600; 3) `ssh -vvv user@server`; 4) serverda `journalctl -u sshd -f`.

---

## 4. Tezkor savollar

1. Qaysi kalit serverga qo'yiladi?
   - **Javob:** Ommaviy (`.pub`).
2. Kalit uchun tavsiya etilgan algoritm?
   - **Javob:** `ed25519`.
3. `~/.ssh` va `authorized_keys` ruxsati?
   - **Javob:** 700 va 600.
4. `PasswordAuthentication no` dan oldin nima?
   - **Javob:** Kalit bilan kirishni sinab ko'rish.
5. Ulanish xatosida nima qilinadi?
   - **Javob:** `ssh -vvv` va serverdagi log.

## 5. Mentor uchun eslatmalar

- SSH mashqlarini virtual mashinada bajaring. Haqiqiy serverda `sshd_config` ni o'zgartirishdan oldin ikkinchi terminal ochiq tursin.
- Shaxsiy kalit yoki parolni chatga, GitHub ga yubormang. Mashq natijasini skrinshotda `id_ed25519` ni ko'rsatmasdan oling.
- Qo'llanmada kalit cheklovlari (`from=`, `no-port-forwarding`), kalit aylantirish va Windows/macOS/WSL eslatmalari bor; port forwarding va bastion (jump host) 19-darsga qoldirildi.
- `ssh-keygen` terminalda sinab ko'rilgan; `sshd` sozlamalari qo'llanmadan olingan va sinov uchun sizning serveringiz kerak.
- Keyingi dars: Nginx reverse-proxy.
