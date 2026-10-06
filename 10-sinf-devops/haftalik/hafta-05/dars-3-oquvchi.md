# 15-dars. Linux xavfsizligi va foydalanuvchilar: useradd, usermod, sudoers, SSH kalitlar bilan xavfsiz ulanish

> Serverga uchta dasturchi kirishi kerak. Hamma bitta parol bilan kirsa, kim nima qilganini bilib bo'lmaydi. Bugun hisoblar, huquqlar va SSH kalitlarni o'rganamiz.

---

## Dars xulosasi

- `useradd -m`, `passwd`, `id`, `groups` bilan hisob yaratiladi va tekshiriladi.
- `usermod -aG` guruhga qo'shadi; `-a` ni unutsangiz eski guruhlar o'chadi.
- `userdel -r` hisobni uy papkasi bilan o'chiradi; `usermod -L` bloklaydi.
- `sudo visudo` va `sudo` guruhi orqali huquq beriladi; `NOPASSWD` ehtiyot bilan.
- `ssh-keygen -t ed25519` kalit juftligini yaratadi, `ssh-copy-id` ochiq kalitni serverga qo'yadi.
- Ruxsatlar: `~/.ssh` 700, kalit va `authorized_keys` 600; serverda parol bilan kirishni o'chirish.

---

## Qo'shimcha ma'lumot

### 1. useradd va adduser
`useradd` — past darajali buyruq, `-m` siz uy papkasi yaratmaydi. Debian/Ubuntu da `adduser` interaktiv va qulayroq: parol va ma'lumotlarni so'raydi.

### 2. Eng kam huquq tamoyili
Har kimga faqat kerakli huquq beriladi. Sudo ni hamma foydalanuvchiga bermang, root bilan to'g'ridan-to'g'ri ishlamang.

### 3. Odatiy xatolar
`usermod -G` ni `-a` siz yozish; `sudoers` ni oddiy muharrirda tahrirlash; shaxsiy kalitni ulashish; `~/.ssh` ruxsatlarini 777 qilish.

---

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **useradd** | Yangi foydalanuvchi yaratadi |
| **usermod** | Mavjud foydalanuvchini o'zgartiradi |
| **sudo** | Administrator huquqida bajarish |
| **visudo** | sudoers ni xavfsiz tahrirlash |
| **SSH** | Xavfsiz masofaviy ulanish |
| **ssh-keygen** | Kalit juftligini yaratadi |
| **Ochiq kalit** | Serverga qo'yiladigan kalit (.pub) |
| **Shaxsiy kalit** | Faqat sizda saqlanadigan kalit |

---

## Bilasizmi?

- `/etc/shadow` ni oddiy foydalanuvchi o'qiy olmaydi: parol xeshlari shu yerda.
- GitHub ga ulanish uchun ham aynan SSH kalit ishlatiladi.
- Kalit bilan kirishni yoqib, parolni o'chirish brute-force hujumlarini foydasiz qiladi.

---

## Topshiriqlar

### 1. Hisob yaratish · oson
`useradd -m` bilan `test1` hisobini yarating va `id test1` ni ko'ring.

**Kutiladigan natija:** uid va gid chiqadi.

### 2. Parol berish · oson
`test1` ga parol bering.

**Kutiladigan natija:** Parol o'rnatilgan.

### 3. Guruhlar · oson
O'z guruhlaringizni `groups` bilan ko'ring.

**Kutiladigan natija:** Guruhlar ro'yxati.

### 4. Fayllar · oson
`/etc/passwd` dagi `test1` qatorini toping (`grep`).

**Kutiladigan natija:** Bitta qator.

### 5. Guruhga qo'shish · o'rta
`test1` ni `users` guruhiga `-aG` bilan qo'shing va tekshiring.

**Kutiladigan natija:** `id test1` da users bor.

### 6. Bloklash · o'rta
`usermod -L` bilan hisobni bloklang, so'ng `-U` bilan oching.

**Kutiladigan natija:** Blok va ochish bajarildi.

### 7. sudo -l · o'rta
`sudo -l` natijasini izohlang.

**Kutiladigan natija:** Ruxsat etilgan buyruqlar tavsifi.

### 8. Kalit yaratish · o'rta
`ssh-keygen -t ed25519` bilan kalit yarating; qaysi fayl ochiq, qaysi shaxsiy ekanini yozing.

**Kutiladigan natija:** `.pub` — ochiq.

### 9. Ruxsatlar · qiyin
`~/.ssh` va shaxsiy kalitga to'g'ri ruxsatlarni (`chmod`) bering va sababini tushuntiring.

**Kutiladigan natija:** 700 va 600.

### 10. sshd xavfsizligi · qiyin
`sshd_config` da qaysi 2 sozlama xavfsizlikni oshiradi? Nima uchun sessiyani yopmay sinash kerak?

**Kutiladigan natija:** `PasswordAuthentication no`, `PermitRootLogin no`; xato bo'lsa chiqib qolish mumkin.

### 11. Xatoni toping · qiyin
`sudo usermod -G docker ali` dan keyin ali sudo huquqini yo'qotdi. Sababi?

**Kutiladigan natija:** `-a` unutilgan: eski guruhlar o'chdi; tuzatish `usermod -aG sudo,docker ali`.

### 12. Yangi dasturchi · bonus
Yangi dasturchi uchun: hisob, sudo guruhi va SSH kirish kaliti bo'yicha 6 qadamli ko'rsatma yozing.

**Kutiladigan natija:** Tartibli 6 qadam.

---

## O'zingizni tekshiring

1. `useradd -m` nima qiladi?
2. `usermod -aG` dagi `-a` nima?
3. Nega `visudo` ishlatiladi?
4. Qaysi kalit serverga qo'yiladi?
5. `~/.ssh` ruxsati nechi?
6. `PasswordAuthentication no` nima qiladi?
7. `ed25519` nima?

---

## Uyga vazifa

Foydalanuvchi yaratish, sudo va SSH kalit mashqlarini bajaring (25 daqiqa). To'liq shart: `uyga-vazifa.md`.
