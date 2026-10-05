---
title: "4-dars. Xizmatlar va jarayonlarni boshqarish (ps, top, kill, systemd)"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (DevOps)", "link": "/10-sinf-devops/"}, "week": {"n": 2, "link": "/10-sinf-devops/hafta-02/"}, "g": 4, "title": "Xizmatlar va jarayonlarni boshqarish (ps, top, kill, systemd)", "lead": "Linux operatsion tizimi tomir urishi: jarayonlar monitoringi (ps, top), boshqaruv signallari (kill, nice) hamda doimiy ishlovchi xizmatlar (systemd/systemctl).", "slide": "/slaydlar/10-sinf-devops/hafta-02/dars-1.html", "test": "/slaydlar/10-sinf-devops/hafta-02/dars-1-test.html", "tabs": [{"g": 4, "link": "/10-sinf-devops/hafta-02/dars-1", "current": true}, {"g": 5, "link": "/10-sinf-devops/hafta-02/dars-2", "current": false}, {"g": 6, "link": "/10-sinf-devops/hafta-02/dars-3", "current": false}], "prev": null, "next": {"g": 5, "title": "Disklar, fayl tizimlari va paket menejerlari (APT, DNF)", "link": "/10-sinf-devops/hafta-02/dars-2"}}
---

---

<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- Linuxda diskdagi dastur xotiraga yuklanib, protsessor tomonidan bajarila boshlaganda «jarayon» (process) deb ataladi va unga noyob PID raqami beriladi.
- Tizimdagi eng birinchi ota jarayon — `PID 1` bo'lib, zamonaviy Linuxda u `systemd` deb ataladi.
- Jarayonlar ikki rejimda ishlaydi: Oldingi (Foreground — terminalni band qiladi) va Fon (Background — `&` belgisi bilan erkin fonda ishlaydi).
- `Ctrl + Z` jarayonni to'xtatadi, `bg` fon rejimida davom ettiradi, `jobs` ularni ko'rsatadi, `fg` esa yana terminalga qaytaradi.
- Jarayonlar holatlari: R (Running), S (Sleeping), D (Disk kutish), T (Stopped), Z (Zombie).
- Jarayonga ta'sir o'tkazish signallar orqali bo'ladi: SIGTERM (15 — xavfsiz to'xtatish), SIGKILL (9 — majburiy yo'q qilish), SIGINT (2 — Ctrl+C).
- Serverdagi doimiy xizmatlar (daemons) `systemctl` utilitasi orqali boshqariladi (`start`, `stop`, `restart`, `status`, `enable`).

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. PID 1 va Ota-Bola (Parent-Child) munosabatlari
Linuxda jarayonlar daraxtsimon ierarxiyada rivojlanadi (`pstree` buyrug'i buni ajoyib ko'rsatadi). Har bir jarayon boshqa bir jarayonning «bolasi» (child) hisoblanadi. Agar siz terminalda `ls` deb yozsangiz:
1. Shell (`bash`) o'zining nusxasini klonlaydi (`fork`).
2. Yangi paydo bo'lgan bola jarayon `ls` kodini o'ziga yuklaydi (`exec`).
3. Ishini tugatgach, ota jarayonga chiqish kodini (exit code) topshiradi va xotirani bo'shatadi.

### 2. Zombie (Z) jarayon nima va undan qanday qutulish mumkin?
Ba'zan bola jarayon o'z vazifasini tugatadi, lekin ota jarayon boshqa ish bilan band bo'lib, bolaning chiqish hisobotini qabul qilmaydi.
Bu holatda bola jarayon xotiradan deyarli resurs olmaydi, lekin jarayonlar jadvalida (Process Table) «Zombie» (Z) bo'lib turadi. Zombi jarayonni `kill -9` bilan o'ldirib bo'lmaydi (chunki u allaqachon o'lgan!). Undan qutulishning yagona yo'li — uning ota jarayonini to'xtatish yoki qayta ishga tushirishdir.

### 3. Nice va Renice: Nega -20 eng yuqori?
Unix mualliflari bu tizimni «odob-axloq» (niceness) konsepsiyasi asosida yaratishgan:
- Agar siz o'ta odobli («nice») bo'lsangiz (+19), o'z protsessor navbatingizni boshqalarga berib yuborasiz va eng oxirida ishlaysiz.
- Agar siz «odobli bo'lmasangiz» (-20), barcha navbatlarni yorib o'tib, protsessorni o'zingizga qaratib olasiz!
Shuning uchun manfiy qiymatlarni (ustuvorlikni oshirish) faqatgina `root` administratori qo'ya oladi.

### 4. `systemctl enable` va `systemctl start` farqi
DevOps amaliyotida eng ko'p uchraydigan adashish:
- `systemctl start app`: Hozir ishga tushiradi, lekin server o'chib yonsa, qayta ishlamaydi.
- `systemctl enable app`: Server har safar yoqilganda avtomatik ishga tushishini sozlaydi (`/etc/systemd/system` da havola yaratadi), lekin hozirning o'zida uni yoqmaydi.
- Ikkalasini birvarakayiga bajarish: `sudo systemctl enable --now app`.

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Process (Jarayon)** | Operativ xotiraga yuklangan va CPU tomonidan bajarilayotgan faol dastur. |
| **PID (Process ID)** | Operatsion tizim tomonidan har bir jarayonga beriladigan noyob raqamli identifikator. |
| **PPID (Parent PID)** | Joriy jarayonni ishga tushirgan ota jarayonning identifikatori. |
| **Daemon** | Foydalanuvchi aralashuvisiz fonda doimiy ishlaydigan tizim xizmati (masalan, `sshd`, `nginx`). |
| **Systemd** | Zamonaviy Linux distributivlarida barcha xizmatlar va tizim resurslarini boshqaruvchi asosiy init tizimi. |
| **SIGTERM (Signal 15)** | Dasturga ma'lumotlarni saqlab, xavfsiz va toza yopilishni so'rovchi standart signal. |
| **SIGKILL (Signal 9)** | Yadro darajasida jarayonni ogohlantirishsiz darhol yo'q qiluvchi majburiy signal. |
| **Nice value** | Jarayonning CPU navbatidagi ustuvorlik darajasini belgilovchi son (-20 dan +19 gacha). |
| **Load Average** | Ma'lum vaqt oralig'ida (1, 5, 15 daqiqa) CPU navbatida kutayotgan jarayonlar o'rtacha soni. |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Linuxda bir vaqtning o'zida yuzlab va minglab jarayonlar mavjud bo'lsa-da, ko'p yadroli zamonaviy protsessorlar vaqtni millisekundlarga bo'lib (time-sharing) ularni parallel bajargandek taassurot qoldiradi.
- `htop` utilitasida klaviaturadagi `F9` tugmasini bossangiz, istalgan jarayonga yuborish mumkin bo'lgan barcha 64 xil Unix signallari menyusi ochiladi.
- Eng mashhur «fork bomb» buyrug'i (`:(){ :|:& };:`) cheksiz ravishda o'z-o'zini klonlaydigan jarayonlarni yaratib, butun kompyuterni bir necha soniyada to'xtatib qo'yishi mumkin.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Tizimdagi o'z jarayonlaringizni ko'rish <Badge type="tip" text="oson" />
`ps` buyrug'ini bajaring va faqat joriy terminalingizda ishlab turgan jarayonlar va ularning PID raqamini aniqlang.
**Kutiladigan natija:** Ekranda `bash` va `ps` jarayonlari ro'yxati chiqadi.

### 2. Real vaqtli monitoringni ochish <Badge type="tip" text="oson" />
Terminalda `top` buyrug'ini ishga tushiring, umumiy RAM hajmi va CPU yuklamasini ko'ring, so'ngra `q` tugmasini bosib chiqing.
**Kutiladigan natija:** Real vaqt rejimida yangilanib turuvchi tizim paneli ko'rinadi.

### 3. Fon rejimida jarayon ishga tushirish <Badge type="tip" text="oson" />
Buyruq oxiriga `&` belgisini qo'yib, `sleep 120 &` jarayonini ishga tushiring va unga qanday job raqami hamda PID berilganini ko'ring.
**Kutiladigan natija:** Ekranda `[1] 12345` ko'rinishidagi yozuv paydo bo'ladi va terminal bo'sh qoladi.

### 4. Fon jarayonlari ro'yxatini ko'rish <Badge type="tip" text="oson" />
`jobs` buyrug'i yordamida fonda ishlab turgan vazifalar ro'yxatini va ularning holatini ekranga chiqaring.
**Kutiladigan natija:** `[1]+ Running sleep 120 &` holati aks etadi.

### 5. Jarayonni qidirish va to'xtatish <Badge type="warning" text="o'rta" />
`ps aux | grep sleep` orqali yuqoridagi jarayonning PID raqamini aniqlang va `kill [PID]` buyrug'i orqali uni xavfsiz to'xtating.
**Kutiladigan natija:** Jarayon muvaffaqiyatli to'xtatiladi va `jobs` da «Terminated» xabari chiqadi.

### 6. Jarayonni oldingi rejimga qaytarish <Badge type="warning" text="o'rta" />
`sleep 60 &` ni ishga tushiring, so'ngra `fg %1` buyrug'i yordamida uni terminalning oldingi (foreground) rejimiga olib chiqing va `Ctrl+C` bilan to'xtating.
**Kutiladigan natija:** Fon jarayoni yana faol terminal oynasiga qaytadi.

### 7. Tizim xizmati holatini tekshirish <Badge type="warning" text="o'rta" />
`systemctl status systemd-journald` buyrug'ini bajarib, tizim log xizmatining faol (active/running) ekanligini tekshiring.
**Kutiladigan natija:** Yashil rangda «active (running)» statusi ko'rinadi.

### 8. Past ustuvorlik bilan jarayon ochish <Badge type="warning" text="o'rta" />
`nice -n 19 sleep 100 &` buyrug'i orqali eng past ustuvorlikdagi fon jarayonini yarating va `ps -o pid,ni,cmd` orqali uning nice qiymati 19 ekanligini tekshiring.
**Kutiladigan natija:** Jarayon ro'yxatida `NI` ustuni `19` ekanligi tasdiqlanadi.

### 9. Barcha bir xil jarayonlarni birdaniga to'xtatish <Badge type="danger" text="qiyin" />
Bir vaqtda 3 ta `sleep 500 &` jarayonini ishga tushiring, so'ngra `killall sleep` yagona buyrug'i bilan ularning barchasini to'xtating.
**Kutiladigan natija:** Barcha 3 ta sleep jarayoni bir vaqtning o'zida yopiladi.

### 10. Eng ko'p RAM yeyayotgan jarayonlarni aniqlash <Badge type="danger" text="qiyin" />
`ps aux --sort=-%mem | head -n 6` buyrug'ini ishga tushirib, tizimda eng ko'p operativ xotira sarflayotgan TOP-5 ta jarayonni aniqlang.
**Kutiladigan natija:** Xotira iste'moli bo'yicha eng yuqori jarayonlar ro'yxati saralanib chiqadi.

### 11. O'z systemd xizmatini yozish (Tadqiqot) <Badge type="info" text="bonus" />
`/etc/systemd/system/` katalogida `myservice.service` faylining umumiy tuzilishini (`[Unit]`, `[Service]`, `[Install]`) o'rganing va oddiy skriptni tizim xizmati ko'rinishida qanday sozlash mumkinligini tahlil qiling.
**Kutiladigan natija:** Systemd unit fayllarining asosiy arxitekturasi va parametrlari tushuniladi.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Diskdagi dastur bilan operativ xotiradagi jarayonning farqi nimada?
2. Nima uchun `kill -9` signalidan doimiy foydalanish tavsiya etilmaydi?
3. `top` panelida «load average» nimani ifodalaydi?
4. `systemctl restart` bilan `systemctl reload` ning qanday farqi bor?
5. `jobs` va `ps` buyruqlarining asosiy farqi nimada?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. O'z tizimingizda `top` yoki `htop` dasturini oching va tizimda jami nechta jarayon ishlab turgani, ulardan nechtasi «running» holatida ekanini daftaringizga yozing.
2. Terminalda `cron` xizmatining holatini `systemctl status cron` (yoki `crond`) orqali tekshiring.
3. 2 ta `sleep 300 &` jarayonini ishga tushirib, ularni `killall` yordamida to'xtatish amaliyotini bajaring (taxminiy vaqt: 25 daqiqa).

</div>

