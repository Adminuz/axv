# 6-hafta. Uyga vazifalar

Har bir vazifa 20–30 daqiqa. Parol, shaxsiy token, maxfiy kalit va shaxsiy ma'lumotlarni repozitoriyga yozmang: topshirishda faqat ochiq GitHub repo yoki Pull Request havolasi kerak.

## 16-dars uchun (Unix/Linux muhiti)
**1-topshiriq: «Linux cheat sheet va ruxsatlar»**
1. `docs/linux-cheatsheet.md` yozing: kataloglar (6 ta), ruxsat oktali va 8 ta asosiy buyruq izohi bilan.
2. `library-api` papkasida `deploy.sh` (750) va `app.log` (640) yarating; `ls -l` natijasini faylga saqlang.
3. Bitta xizmat (`nginx` yoki `ssh`) uchun `systemctl status` va `journalctl -u ... -n 20` natijalarini o'qib, 3 jumlada tushuntiring.

**Kutiladigan natija:** cheat sheet, ruxsat mashqi va xizmat holati izohi.  
**Topshirish:** GitHub commit yoki fayl havolasi.

---

## 17-dars uchun (SSH kalitlari)
**2-topshiriq: «SSH kalit va config»**
1. Mashina uchun yangi `ed25519` kalit yarating; `docs/ssh.md` ga buyruqlarni va fayl ruxsatlarini (private kalitni ko'rsatmasdan) yozing.
2. `~/.ssh/config` da 2 ta `Host` bloki yozing (sinov serveri va GitHub), faylni ochiq repoga qo'ymang, faqat namunani `docs/ssh-config.example` ga qo'ying.
3. `sshd_config` ni qattiqlashtirish tartibini 6 qadamda yozing (avval sinash, keyin parolni o'chirish).

**Kutiladigan natija:** SSH hujjati, config namunasi va qattiqlashtirish tartibi.  
**Topshirish:** GitHub commit yoki fayl havolasi.

---

## 18-dars uchun (Nginx reverse-proxy)
**3-topshiriq: «Nginx konfiguratsiyasi»**
1. `docs/nginx.md` yozing: reverse-proxy ning 5 afzalligi va arxitektura sxemasi.
2. `library.conf` konfiguratsiyasini (server, location, 4 ta sarlavha) yozing va `nginx -t` natijasini qo'shing.
3. Ikki ilova uchun `upstream` blokini yozing va `least_conn` nima qilishini bir jumlada tushuntiring.

**Kutiladigan natija:** `nginx.md`, `library.conf` va upstream bloki.  
**Topshirish:** GitHub commit yoki fayl havolasi.

---

## Mentor uchun
16-darsda oktal hisobini va minimal ruxsat qoidasini tekshiring. 17-darsda shaxsiy kalit hech qayerda ko'rinmasligiga ishonch hosil qiling. 18-darsda `nginx -t` natijasi va sarlavhalar to'liqligini ko'ring. Natijalarni `baholash.md` ga kiriting.
