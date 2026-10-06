# 14-dars. Linux jarayonlari va rejalashtirish: cron, crontab, at va tizim monitoringi (htop, iotop)

> Server har kecha o'zi zaxira oladi, uxlayotganingizda ham. Buni `cron` qiladi. Bugun vazifalarni vaqtga bog'lashni va tizim yuklamasini kuzatishni o'rganamiz.

---

## Dars xulosasi

- `ps aux` jarayonlarni ko'rsatadi, `top` va `htop` CPU va xotirani, `iotop` diskni kuzatadi.
- `kill PID` jarayonni to'xtatadi, `kill -9` oxirgi chora.
- `crontab -e/-l/-r`: vazifalarni tahrirlash, ko'rish va o'chirish.
- Cron qatori: daqiqa soat kun oy hafta_kuni buyruq.
- `*/5`, `1-5`, `1,15`, `@reboot` kabi yozuvlar.
- `at` bir martalik vazifa; `atq` ko'radi, `atrm` bekor qiladi.

---

## Qo'shimcha ma'lumot

### 1. htop tugmalari
`F6` saralash, `F4` filtr, `F9` jarayonni to'xtatish, `F10` chiqish. Sichqoncha ham ishlaydi.

### 2. Cron muammolari
Skript bajariladigan emas (`chmod +x`), yo'l nisbiy, PATH qisqa, natija log ga yo'naltirilmagan: shu sabablar eng ko'p uchraydi.

### 3. Odatiy xatolar
Daqiqa va soatni adashtirish; `crontab -r` bilan hamma vazifani o'chirish; `kill -9` ni darrov ishlatish.

---

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Jarayon** | Ishlayotgan dastur |
| **PID** | Jarayon raqami |
| **top / htop** | CPU va xotira monitoringi |
| **iotop** | Disk yuklamasi monitoringi |
| **cron** | Vazifalarni vaqt bo'yicha ishga tushiruvchi xizmat |
| **crontab** | Cron vazifalari jadvali |
| **at** | Bir martalik vazifa |
| **SIGKILL** | `kill -9`, majburiy to'xtatish |

---

## Bilasizmi?

- Cron nomi yunoncha «chronos» (vaqt) so'zidan olingan.
- `htop` ni `top` ning rangli va qulay vorisi deb atashadi.
- Haftaning yakshanba kuni cron da 0 va 7 bilan yoziladi.

---

## Topshiriqlar

### 1. Jarayon toping · oson
`ps aux | grep ssh` bilan ssh jarayonlarini toping.

**Kutiladigan natija:** Ro'yxatda PID ko'rinadi.

### 2. htop · oson
`htop` ni oching va eng ko'p CPU yeyuvchi jarayonni aniqlang.

**Kutiladigan natija:** Jarayon nomi.

### 3. crontab -l · oson
Joriy cron vazifalarini ko'ring.

**Kutiladigan natija:** Ro'yxat yoki «no crontab».

### 4. Maydonlar · oson
Cron qatorining 5 maydonini tartib bilan sanang.

**Kutiladigan natija:** Daqiqa, soat, kun, oy, hafta kuni.

### 5. Har 5 daqiqa · o'rta
Har 5 daqiqada `date >> ~/vaqt.txt` bajaruvchi qatorni yozing.

**Kutiladigan natija:** `*/5 * * * * date >> ~/vaqt.txt`.

### 6. Ish kunlari · o'rta
Ish kunlari 09:00 da bajariladigan qatorni yozing.

**Kutiladigan natija:** `0 9 * * 1-5 ...`.

### 7. Oyning 1-kuni · o'rta
Har oyning 1-kuni yarim tunda ishlovchi qatorni yozing.

**Kutiladigan natija:** `0 0 1 * * ...`.

### 8. at · o'rta
`at now + 2 minutes` bilan fayl yarating va `atq` bilan ko'ring.

**Kutiladigan natija:** Navbatda vazifa bor.

### 9. Qatorni o'qing · qiyin
`15 14 1 * *` qachon ishlaydi?

**Kutiladigan natija:** Har oyning 1-kuni 14:15.

### 10. Sekin tizim · qiyin
Tizim sekinlashdi. Qaysi vositalar bilan sababni (CPU, xotira, disk) topasiz?

**Kutiladigan natija:** `top/htop` va `iotop`.

### 11. Xatoni toping · qiyin
Cron vazifa ishlamayapti: `* * * * * zaxira.sh`. Sabablarni yozing.

**Kutiladigan natija:** To'liq yo'l, `chmod +x`, log yo'q.

### 12. Mini-monitor · bonus
Har daqiqada diskdagi bo'sh joyni (`df -h`) log ga yozuvchi cron vazifasi yarating, 3 daqiqadan so'ng log ni tekshirib, qatorni o'chiring.

**Kutiladigan natija:** Log da 3 ta yozuv.

---

## O'zingizni tekshiring

1. `top` va `htop` farqi?
2. `iotop` nimani ko'rsatadi?
3. Cron qatori maydonlari?
4. `*/5` nima?
5. `at` va `cron` farqi?
6. `crontab -r` nima qiladi?
7. `kill` va `kill -9` farqi?

---

## Uyga vazifa

cron vazifasi va at mashqini bajaring, monitoring hisobotini yozing (25 daqiqa). To'liq shart: `uyga-vazifa.md`.
