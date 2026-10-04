# 1-hafta: Uyga vazifalar (DevOps)

1-haftada Linux operatsion tizimi, terminal asoslari, FHS kataloglar ierarxiyasi, fayl ruxsatlari (chmod/chown), matn muharrirlari (Nano, Vim) hamda Shell muhiti va I/O yo'naltirish mavzulari o'rganildi. Quyidagi topshiriqlar o'tilgan bilimlarni mustahkamlashga qaratilgan.

---

## 1-dars vazifasi: Linux fayl tizimi va navigatsiya

1. O'z kompyuteringizdagi Linux terminalida (yoki WSL/VirtualBox Ubuntu muhitida) uy katalogingizda `devops_lab` nomli asosiy papka oching.
2. `mkdir -p` yordamida uning ichida `projects/backend`, `projects/frontend`, `configs` va `logs` papkalarini bir martada yarating.
3. Har bir papka ichida bittadan `.txt` fayl hosil qiling (`touch` orqali).
4. `projects/backend` ichidagi faylni `configs` papkasi ichiga boshqa nom bilan nusxalang (`cp`).
5. `logs` papkasidagi faylni `projects/frontend` ga ko'chiring (`mv`).
6. `history` buyrug'i orqali bajargan barcha amallaringiz ro'yxatini daftaringizga qayd eting.
*(Kutiladigan vaqt: 25 daqiqa)*

---

## 2-dars vazifasi: Ruxsatlar va Vim bilan ishlash

1. `devops_lab` papkasi ichida `start_server.sh` va `secret.env` nomli ikkita fayl yarating.
2. `nano` yoki `vim` yordamida `start_server.sh` ichiga quyidagi qatorni yozing:
   ```bash
   echo "Server 8080-portda muvaffaqiyatli ishga tushdi!"
   ```
3. `secret.env` ichiga esa `DB_PASSWORD="SuperSecret123"` qatorini kiriting.
4. `chmod` orqali quyidagi qat'iy ruxsatlarni o'rnating:
   - `start_server.sh` fayliga: `755` (egasi to'liq, guruh va boshqalar faqat o'qish va bajarish).
   - `secret.env` fayliga: `600` (faqat egasi o'qish va yozish, qolgan barcha toifalarga mutlaqo taqiqlash).
5. `./start_server.sh` buyrug'i bilan skriptingizni ishga tushiring va natijani ko'ring.
6. `ls -l` buyrug'i natijasini skrinshot qilib yoki daftaringizga ko'chirib yozing.
*(Kutiladigan vaqt: 25 daqiqa)*

---

## 3-dars vazifasi: Shell muhiti, Aliaslar va Quvurlar

1. `~/.bashrc` faylini `vim` yoki `nano` bilan oching.
2. Faylning eng oxiriga o'tib, quyidagi sozlamalarni qo'shing:
   - `export MY_ROLE="DevOps Engineer"`
   - `alias dlab='cd ~/devops_lab && pwd && ls -la'`
   - `alias update_sys='sudo apt update'`
3. Faylni saqlang va `source ~/.bashrc` buyrug'i orqali o'zgarishlarni qo'llang.
4. Terminalda `echo $MY_ROLE` deb yozib o'zgaruvchi ishlaganini, so'ngra `dlab` deb yozib yangi alias bir zumda sizni laboratoriya papkangizga olib borganini tekshiring.
5. `/etc` katalogidagi barcha fayllar ro'yxatini `ls /etc | wc -l` quvuri orqali sanang va chiqqan raqamni yozib qo'ying.
*(Kutiladigan vaqt: 25 daqiqa)*

---

## Mentor uchun

- **Tekshirish mezonlari:**
  1. O'quvchi FHS va nisbiy/mutlaq yo'llar farqini tushunganmi (`cd ..`, `cd ~`, `mkdir -p`).
  2. Ruxsatlar to'g'ri berilganmi: `deploy.sh` da bajarish (`x`) huquqi bormi, maxfiy fayllar `600` bilan himoyalanganmi.
  3. Vim muharririda Normal va Insert rejimlaridan to'g'ri foydalanilganmi.
  4. Alias va muhit o'zgaruvchilari `~/.bashrc` faylida xatosiz e'lon qilinganmi.
- **Tez-tez uchraydigan xatolar:**
  - O'zgaruvchi e'lon qilishda tenglik atrofida bo'sh joy qoldirish (`NAME = "Ali"` deb yozish xatolik beradi).
  - Vim'dan chiqishda `:wq` o'rniga oynani shunchaki yopib yuborish (natijada `.swp` fayllar hosil bo'ladi).
  - Skriptga `chmod +x` bermasdan `./script.sh` chaqirish va «Permission denied» xatosiga tushish.
