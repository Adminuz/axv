# 5-dars. Disklar, fayl tizimlari va paket menejerlari (APT, DNF)

> Linuxda xotira boshqaruvi: disklar va bo'limlar arxitekturasi (df, du, mount), zamonaviy fayl tizimlari hamda xavfsiz dastur o'rnatish tizimi (APT/DNF).

---

## Dars xulosasi

- Linuxda barcha qattiq disklar va bo'limlar `/dev` katalogida blokli qurilma fayli sifatida taqdim etiladi (`/dev/sda`, `/dev/nvme0n1`).
- `df -h` buyrug'i butun fayl tizimi bo'yicha umumiy, ishlatilgan va bo'sh disk joyini qulay o'lchov birliklarida (GB, MB) ko'rsatadi.
- `du -sh *` buyrug'i joriy papkadagi har bir alohida katalog va fayl qancha joy egallab turganini hisoblab beradi.
- Windows'dagi disklarga harf berish (masalan, `D:\`) tizimidan farqli ravishda, Linuxda tashqi disklar fayl tizimi daraxtidagi papkaga ulanadi (Mount point).
- Linuxda dasturlar markazlashtirilgan repozitoriylardan paket menejerlari orqali (Debian/Ubuntu'da `apt`, RHEL/Fedora'da `dnf`, Alpine'da `apk`) xavfsiz o'rnatiladi.
- `apt update` paketlarning eng yangi versiyalar ro'yxatini yuklab olsa, `apt upgrade` tizimdagi dasturlarni yangilaydi, `apt install` esa yangi dastur o'rnatadi.
- `apt remove` faqat dastur binar fayllarini o'chirsa, `apt purge` uning barcha konfiguratsiya fayllari bilan birga butunlay yo'q qiladi.

---

## Qo'shimcha ma'lumot

### 1. Ext4, XFS va Btrfs: Qaysi fayl tizimi yaxshiroq?
Linuxda turli maqsadlar uchun turli fayl tizimlari yaratilgan:
- **ext4 (Fourth Extended Filesystem)**: Ubuntu va ko'plab distributivlarning standarti. O'n yillik tajribadan o'tgan, o'ta ishonchli va barqaror.
- **XFS**: Red Hat Enterprise Linux (RHEL) standarti. Katta hajmdagi ma'lumotlar bazalari va gigant fayllar bilan ishlashda eng yuqori unumdorlikni beradi.
- **Btrfs (B-tree FS)**: Snapshot (bir zumlik nusxalar) olish, xatolarni o'zi tuzatish (self-healing) va disk massivlarini birlashtirish imkonini beruvchi zamonaviy fayl tizimi.

### 2. Disk to'lib qolganda DevOps muhandisi nima qiladi?
Serverda disk 100% to'lib qolsa, ma'lumotlar bazasi to'xtaydi, veb-sayt ishlamay qoladi. Bunday holatda «birinchi yordam» qoidalari:
1. `df -h` bilan qaysi bo'lim (odatda `/` yoki `/var`) to'lganini aniqlang.
2. `sudo du -sh /var/* | sort -h` orqali aynan qaysi papka shishib ketganini toping.
3. Ko'pincha bu eskirgan loglar bo'ladi: `/var/log` ichidagi eski `.gz` arxiv loglarini tozalang yoki `sudo journalctl --vacuum-time=3d` qiling.
4. Paket menejeri keshini tozalang: `sudo apt clean` va `sudo apt autoremove`.

### 3. Repozitoriylar siri: `/etc/apt/sources.list`
`apt install` yozganingizda tizim fayllarni qayerdan oladi?
Linux barcha rasmiy serverlar manzillarini `/etc/apt/sources.list` faylida va `/etc/apt/sources.list.d/` katalogidagi `.list` fayllarda saqlaydi.
Har bir repozitoriya o'zining raqamli GPG kalitiga ega, shuning uchun yuklab olingan fayl soxtalashtirilmagani yoki virus yuqtirilmaganiga 100% kafolat beriladi.

### 4. Swap xotira nima uchun kerak?
Swap — bu operativ xotiraning (RAM) «xavfsizlik yostig'i»dir. Agar serverda 8 GB RAM bo'lsa va unga 9 GB lik og'ir ma'lumotlar bazasi so'rovi kelsa, kompyuter OOM (Out Of Memory) xatoligi bilan qulab tushmaydi, balki ortiqcha 1 GB ni vaqtincha Swap disk bo'limiga yozadi. Albatta, disk RAM dan ancha sekin ishlaydi, lekin u serverni qulashdan saqlab qoladi.

---

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Filesystem (Fayl tizimi)** | Ma'lumotlarni qattiq diskda saqlash, nomlash va ularga kirishni tartibga soluvchi mantiqiy tizim. |
| **Mount Point** | Tashqi disk yoki bo'lim fayl tizimi daraxtiga ulanadigan katalog nuqtasi. |
| **Block Device** | Ma'lumotlarni qat'iy bloklar (masalan, 512 bayt yoki 4 KB) ko'rinishida o'qiydigan va yozadigan saqlash qurilmasi (HDD, SSD). |
| **Swap** | RAM to'lganda ma'lumotlarni vaqtincha saqlab turish uchun ajratilgan maxsus disk bo'limi yoki fayli. |
| **Package Manager** | Dasturlarni repozitoriylardan avtomatik yuklab oluvchi, o'rnatuvchi, yangilovchi va bog'liqliklarini tekshiruvchi utilita. |
| **Repository (Repozitoriya)** | Dasturlar paketlari va ularning yangilanishlari saqlanadigan masofaviy rasmiy server. |
| **Dependency (Bog'liqlik)** | Biror dasturning to'liq ishlashi uchun talab etiladigan qo'shimcha kutubxonalar va modullar. |
| **APT (Advanced Package Tool)** | Debian va Ubuntu tizimlarining standart paket menejeri. |

---

## Bilasizmi?

- Linuxda birinchi qattiq disk nomining `sda` deb atalishi qadimgi «SCSI Disk A» atamasidan kelib chiqqan (ikkinchi disk `sdb`, uchinchi disk `sdc`).
- APT paket menejeri dastur o'rnatishdan oldin uning barcha bog'liqliklarini daraxtsimon grafik ko'rinishida yechadi (Dependency resolution).
- Red Hat kompaniyasi 1990-yillarda yaratgan `.rpm` paket formati dastur o'rnatish madaniyatida inqilob yasagan va keyinchalik DNF vositasiga asos bo'lgan.

---

## Topshiriqlar

### 1. Umumiy disk bo'sh joyini ko'rish · oson
`df -h` buyrug'ini ishga tushiring va ildiz (`/`) bo'limida qancha GB bo'sh joy borligini aniqlang.
**Kutiladigan natija:** Disk bo'limlari, ularning hajmi va foizi inson o'qiy oladigan formatda chiqadi.

### 2. Bitta papka hajmini tekshirish · oson
O'z uy katalogingiz qancha joy egallab turganini `du -sh ~` buyrug'i yordamida hisoblang.
**Kutiladigan natija:** Ekranda `120M /home/username` ko'rinishidagi aniq hajm ko'rinadi.

### 3. Blokli qurilmalar ro'yxatini ko'rish · oson
`lsblk` buyrug'ini bering va tizimingizdagi qattiq disklar nomlarini (masalan, `sda`, `vda` yoki `nvme0n1`) aniqlang.
**Kutiladigan natija:** Disklar va ularning bo'limlari daraxti aks etadi.

### 4. Yangi paket indekslarini yangilash · oson
`sudo apt update` buyrug'ini bajarib, tizim repozitoriyalari bilan aloqa o'rnating.
**Kutiladigan natija:** Repozitoriya serverlaridan eng yangi paketlar indeksi yuklab olinadi.

### 5. Foydali utilita o'rnatish · o'rta
`sudo apt install -y tree htop` buyrug'i orqali ikkita muhim boshqaruv utilitasini o'rnating va `tree --version` bilan tasdiqlang.
**Kutiladigan natija:** Dasturlar muvaffaqiyatli o'rnatiladi va foydalanishga tayyor bo'ladi.

### 6. Joriy papkadagi barcha elementlar hajmini saralash · o'rta
`du -sh * | sort -h` buyrug'i orqali joriy papkangizdagi har bir fayl va papkaning o'lchamini o'sish tartibida saralang.
**Kutiladigan natija:** Eng kichik fayldan eng katta papkagacha bo'lgan ro'yxat chiqadi.

### 7. Dasturni to'liq (sozlamalari bilan) o'chirish · o'rta
Eskirgan yoki keraksiz dasturni `sudo apt purge [paket_nomi]` buyrug'i orqali barcha sozlamalari bilan birga tozalang.
**Kutiladigan natija:** Dastur konfiguratsiyalari bilan birga o'chiriladi.

### 8. Keshni tozalash va diskni bo'shatish · o'rta
`sudo apt clean` va `sudo apt autoremove -y` buyruqlarini bajarib, tizimdan vaqtinchalik o'rnatish fayllari va keraksiz kutubxonalarni tozalang.
**Kutiladigan natija:** Tizimda bo'sh disk maydoni hosil bo'ladi.

### 9. Qaysi paket qaysi buyruqni berganini aniqlash · qiyin
`dpkg -S $(which ls)` yoki `dpkg -S /bin/ls` buyrug'ini bajaring va `ls` buyrug'i qaysi paket (`coreutils`) tarkibiga kirishini aniqlang.
**Kutiladigan natija:** Binar fayl tegishli bo'lgan asosiy paket nomi aniqlanadi.

### 10. O'rnatilgan paketlar ro'yxatini qidirish · qiyin
`dpkg -l | grep -i "ssh"` buyrug'i orqali tizimda SSH bilan bog'liq qanday paketlar o'rnatilganini tahlil qiling.
**Kutiladigan natija:** SSH paketlari va ularning versiyalari ro'yxati chiqadi.

### 11. Ncdu (Disk Usage) interaktiv tahlil · bonus
`sudo apt install -y ncdu` dasturini o'rnating va `ncdu ~` buyrug'i yordamida interaktiv rejimda disk xotirangizni eng ko'p band qilgan papkalarni grafik terminalda tahlil qiling.
**Kutiladigan natija:** Vizual chiroyli matnli interfeysda xotira taqsimoti tahlil qilinadi.

---

## O'zingizni tekshiring

1. `df` buyrug'idagi `-h` bayrog'i nima maqsadda qo'shiladi?
2. Linuxda disk qanday ulanadi va «Mount point» nima?
3. `sudo apt update` va `sudo apt upgrade` buyruqlarining vazifalari qanday farqlanadi?
4. `apt remove` bilan `apt purge` ning qanday farqi bor?
5. Swap xotira nima va u serverlarda nima uchun zarur?

---

## Uyga vazifa

1. O'z tizimingizda `df -h` buyrug'ini ishga tushirib, asosiy bo'limlarning umumiy va bo'sh hajm parametrlarini daftaringizga ko'chirib yozing.
2. `sudo apt update && sudo apt install -y curl wget tree` buyruqlari orqali uchta muhim tarmoq va fayl utilitasini o'rnating.
3. `/var/log` papkasi hajmini `sudo du -sh /var/log` orqali aniqlab, qanday natija chiqqanini qayd eting (taxminiy vaqt: 25 daqiqa).
