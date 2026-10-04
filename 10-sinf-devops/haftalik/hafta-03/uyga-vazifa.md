# 3-hafta: Uyga vazifalar (DevOps)

3-haftada Git versiya boshqaruvi tizimining ilg'or mexanizmlari (tarmoqlanish, birlashtirish, ziddiyatlarni hal qilish va masofaviy repozitoriyalar) hamda kompyuter tarmoqlarining fundamental asoslari (OSI modeli, TCP/IP steki, IP manzillash, Subnetting va tarmoq diagnostikasi) o'rganildi. Quyidagi amaliy topshiriqlar bilimlarni sinovdan o'tkazishga qaratilgan.

---

## 7-dars vazifasi: Git Branchlar va Birlashtirish

1. O'tgan haftadagi `my_git_lab` repozitoriyasida `feature-auth` nomli yangi branch oching (`git switch -c feature-auth`).
2. Yangi branch ichida `auth.py` faylini yaratib, ichiga oddiy login kodini yozing va `git commit -m "feat: login funksiyasi qo'shildi"` bilan commit qiling.
3. Asosiy `main` branchga qayting (`git switch main`).
4. `feature-auth` branchini `main` ga birlashtiring (`git merge feature-auth`).
5. Birlashtirilgan branchni xavfsiz o'chiring (`git branch -d feature-auth`).
6. `git log --oneline --graph` buyrug'i natijasini daftaringizga qayd eting.
*(Kutiladigan vaqt: 25 daqiqa)*

---

## 8-dars vazifasi: Tarmoq qatlamlari va Interfeyslar tahlili

1. Linux terminalida `ip a` buyrug'ini ishga tushiring. Tizimingizdagi jismoniy tarmoq kartasining nomi, uning MAC manzili va lokal IP manzilini aniqlab daftaringizga ko'chirib yozing.
2. `ip route` buyrug'i yordamida tashqi dunyoga chiquvchi Default Gateway (Router) IP manzilini toping.
3. OSI 7 qatlamli modelining har bir qatlami nomini (1 dan 7 gacha) va har bir qatlamda ishlovchi kamida bittadan protokolni jadval ko'rinishida daftaringizga chizing.
*(Kutiladigan vaqt: 25 daqiqa)*

---

## 9-dars vazifasi: Subnetting va Tarmoq diagnostikasi

1. `ping -c 4 8.8.8.8` buyrug'i orqali Google DNS serveriga so'rov yuboring. O'rtacha kechikish (rtt avg) va paketlar yo'qolish foizini daftaringizga qayd eting.
2. `curl ifconfig.me` buyrug'i yordamida uyingizning tashqi ommaviy (Public) IP manzilini aniqlang.
3. `curl -I https://yandex.uz` buyrug'ini berib, HTTP javob kodini aniqlang.
4. Quyidagi hisoblash masalasini yeching:
   - Berilgan: `192.168.100.0/25` tarmog'i.
   - Aniqlang:
     a) Tarmoq maskasi (Subnet Mask)
     b) Foydalanish mumkin bo'lgan maksimal xostlar soni
     c) Tarmoq manzili (Network ID)
     d) Efir manzili (Broadcast ID)
*(Kutiladigan vaqt: 25 daqiqa)*

---

## Mentor uchun

- **Tekshirish mezonlari:**
  1. O'quvchi branch ochish (`git switch -c`), kommit qilish va `merge` qilish ketma-ketligini to'g'ri bajarganmi.
  2. OSI 7 qatlamli modeli va TCP/IP steki o'rtasidagi mantiqiy bog'liqlikni tushunganmi.
  3. MAC va IP manzil farqini ajrata oladimi (2-qatlam vs 3-qatlam).
  4. Subnetting formulasidan ($2^H - 2$) to'g'ri foydalanib, xostlar soni va tarmoq parametrlarini to'g'ri hisoblaganmi.
  5. `ping` va `curl` buyruqlari natijalarini to'g'ri tahlil qila oladimi.
- **Tez-tez uchraydigan xatolar:**
  - Branch birlashtirishda `main` ga o'tishni unutib, yangi branch ichida turib merge qilish.
  - Subnet hisoblashda 2 ta zaxira manzilni (Network ID va Broadcast ID) ayirishni unutish ($2^H$ o'rniga $2^H - 2$).
  - Ommaviy va xususiy IP farqini tushunmaslik (`192.168.x.x` manzilini global Internetda izlash).
