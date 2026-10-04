# 5-dars. Disklar, fayl tizimlari va paket menejerlari (APT, DNF)

**Darsning maqsadi:** O'quvchilarga Linux operatsion tizimida disklar va fayl tizimlari tuzilishi (ext4, xfs, swap), xotira monitoringi (`df -h`, `du -sh`), blokli qurilmalar (`lsblk`, `fdisk`), diskni ulash (`mount`, `umount`) hamda dasturiy ta'minotni paket menejerlari (APT va DNF/YUM) orqali o'rnatish, yangilash va xavfsiz boshqarish asoslarini amaliy o'rgatish.

**Vaqt taqsimoti:**
- O'tgan darsni takrorlash (Jarayonlar va systemctl): 10 daqiqa
- Yangi mavzu: Disklar va fayl tizimlari monitoringi (`df`, `du`, `lsblk`, `mount`): 25 daqiqa
- Yangi mavzu: Paket menejerlari arxitekturasi (APT vs DNF, repozitoriylar): 15 daqiqa
- Amaliy mashg'ulot (Disk sarfini tahlil qilish, yangi paket o'rnatish va boshqarish): 25 daqiqa
- Dars xulosasi va tezkor nazorat: 5 daqiqa

---

## 1. Dars konspekti (Mentor uchun)

### 1.1. Disklar va fayl tizimlari arxitekturasi
Linuxda fizik disklar va ularning bo'limlari (partitions) `/dev` katalogida maxsus qurilma fayli sifatida aks etadi:
- `/dev/sda` — birinchi SATA/SCSI qattiq disk (SSD/HDD).
- `/dev/sda1`, `/dev/sda2` — shu diskdagi 1-va 2-bo'limlar.
- `/dev/nvme0n1` — zamonaviy NVMe M.2 yuqori tezlikdagi SSD drayv.
- **Fayl tizimi (Filesystem)**: Ma'lumotlarni disk bloklarida saqlash va indekslash qoidasi (Linuxda eng keng tarqalganlari: **ext4**, **xfs**, **btrfs**).
- **Swap**: Operativ xotira (RAM) to'lib qolganda, kam ishlatilayotgan xotira sahifalarini vaqtincha saqlab turuvchi disk bo'limi yoki fayli.

### 1.2. Disk monitoringi buyruqlari
1. `df` (disk free) — fayl tizimlaridagi bo'sh joyni ko'rsatadi:
   - `df -h` — inson tushunadigan o'lchov birliklarida (GB, MB) chiqarish (DevOps'ning eng birinchi tekshiruv buyrug'i!).
2. `du` (disk usage) — ma'lum bir papka yoki fayl qancha joy egallayotganini hisoblaydi:
   - `du -sh *` — joriy katalogdagi har bir elementning umumiy hajmini qisqa xulosa qilib chiqaradi (`-s` summary, `-h` human-readable).
   - `du -sh /var/log` — loglar papkasi hajmini tekshirish.
3. `lsblk` (list block devices) — barcha disklar va ularning bo'limlari daraxtini ko'rsatadi.
4. `sudo fdisk -l` — disklar hajmi, bo'limlar jadvali (GPT, MBR) va sektorlar haqida to'liq texnik ma'lumot beradi.

### 1.3. Ulanish nuqtasi (Mount Point) tushunchasi
Windows'da yangi fleshka yoki disk ulanganda unga yangi harf (masalan, `E:\`) beriladi. Linuxda esa disk yagona fayl tizimi daraxtidagi biror bo'sh papkaga biriktiriladi (ulanish nuqtasi — mount point deb ataladi):
- Diskni ulash: `sudo mount /dev/sdb1 /mnt/backup`
- Diskni uzish: `sudo umount /mnt/backup`
- Doimiy avtomatik ulanish sozlamalari `/etc/fstab` faylida saqlanadi.

### 1.4. Linux paket menejerlari (Package Managers)
Windows'da dastur o'rnatish uchun `.exe` yuklab olib «Next-Next» bosilsa, Linuxda xavfsiz va markazlashtirilgan paket menejerlari ishlaydi:
- Dasturlar rasmiy, imzolangan va tekshirilgan **repozitoriy (repository)** larda saqlanadi.
- Paket menejeri dasturning barcha bog'liqliklarini (dependencies) avtomatik ravishda yuklab olib o'rnatadi.
- Asosiy oilalar:
  - **Debian / Ubuntu**: Paket formati `.deb`, vosita: **APT** (`apt`).
  - **RHEL / CentOS / Fedora**: Paket formati `.rpm`, vosita: **DNF / YUM** (`dnf`).
  - **Alpine Linux**: Paket formati `.apk`, vosita: **APK** (Docker konteynerlarida juda mashhur).

### 1.5. APT bilan ishlash asosiy buyruqlari
1. `sudo apt update`: Dasturlarni yangilamaydi! U faqat repozitoriy serverlariga ulanib, eng so'nggi versiyalar ro'yxatini (indeksini) yuklab oladi.
2. `sudo apt upgrade -y`: Tizimdagi barcha o'rnatilgan dasturlarni yangi versiyaga yangilaydi.
3. `sudo apt install [paket_nomi]`: Dasturni barcha bog'liqliklari bilan o'rnatadi (masalan: `sudo apt install htop nginx tree`).
4. `sudo apt remove [paket_nomi]`: Dasturni o'chiradi, lekin uning sozlama fayllari saqlanib qoladi.
5. `sudo apt purge [paket_nomi]`: Dasturni uning barcha konfiguratsiya fayllari bilan birga butunlay yo'q qiladi.
6. `sudo apt autoremove`: Keraksiz bo'lib qolgan qoldiq kutubxonalarni tozalaydi.

---

## 2. Amaliy topshiriqlar va yechimlari (Mentor uchun)

### 1-topshiriq. Tizimdagi bo'sh disk joyini tahlil qilish
`df -h` buyrug'ini ishga tushiring. Eng asosiy ildiz (`/`) bo'limi qaysi disk qurilmasiga biriktirilganini, uning umumiy hajmini va qancha foiz bo'sh joy qolganini aniqlang.

**Yechim:**
```bash
df -h
# Natija tahlili:
# Filesystem      Size  Used Avail Use% Mounted on
# /dev/sda1        50G   12G   36G  25% /
# Ildiz (/) bo'limi /dev/sda1 qurilmasida, jami 50G, 25% ishlatilgan.
```

### 2-topshiriq. Qaysi papka ko'p joy olayotganini aniqlash
`/var` katalogi ichidagi barcha papkalar hajmini `du -sh` yordamida ko'ring va ularni hajm bo'yicha kamayish tartibida saralang.

**Yechim:**
```bash
sudo du -sh /var/* | sort -h
```

### 3-topshiriq. APT repozitoriyalarini yangilash va yangi utilita o'rnatish
Paketlar indeksini yangilang (`apt update`) va tizimga `ncdu` (disk tahlilchisi) yoki `tree` dasturini o'rnating.

**Yechim:**
```bash
# 1. Repozitoriy indeksini yangilash
sudo apt update

# 2. Yangi dasturni o'rnatish
sudo apt install -y tree

# 3. Dastur ishlashini tekshirish
tree --version
```

### 4-topshiriq. Blokli qurilmalar daraxtini ko'rish
`lsblk` buyrug'i yordamida kompyuteringizga ulangan barcha disklar va ularning bo'limlari ierarxiyasini ekranga chiqaring.

**Yechim:**
```bash
lsblk
# Disklar (sda), ularning bo'limlari (sda1, sda2) va ulanish nuqtalari (MOUNTPOINT) aks etadi.
```

---

## 3. Tezkor nazorat savollari (Dars yakuni)

1. **`df` bilan `du` buyruqlarining farqi nimada?**
   *Javob:* `df` (disk free) butun fayl tizimi bo'limlari darajasida umumiy bo'sh va band joyni ko'rsatadi. `du` (disk usage) esa ma'lum bir katalog yoki faylning diskda qancha hajm egallashini hisoblaydi.
2. **`sudo apt update` buyrug'i dasturlarni yangilaydimi?**
   *Javob:* Yo'q, u faqat mavjud paketlarning eng so'nggi versiyalar ro'yxatini (indeksini) serverdan yuklab oladi. Dasturlarni yangilash uchun `sudo apt upgrade` bajariladi.
3. **`apt remove` bilan `apt purge` ning qanday farqi bor?**
   *Javob:* `remove` faqat dasturning o'zini o'chiradi, sozlamalarini saqlab qoladi. `purge` esa barcha konfiguratsiya fayllari bilan birga ildizi bilan o'chirib tashlaydi.
4. **Linuxda «Mount point» (ulanish nuqtasi) nima?**
   *Javob:* Tashqi disk yoki bo'limdagi fayllarga kirish imkonini beruvchi fayl tizimi daraxtidagi bo'sh katalog.
