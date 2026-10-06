# 16-dars. Unix/Linux muhiti: fayl tizimi, ruxsatlar, xizmatlar va loglar

> Server — qora oyna va bir qancha buyruq. Bugun II bobni boshlaymiz: Linux muhitida yo'limizni topishni, ruxsatlar va xizmatlarni o'rganamiz.

## Dars xulosasi

- Linux fayl tizimi `/` dan boshlanadi: `/etc`, `/var/log`, `/home`.
- Ruxsat: egasi, guruh, boshqalar; `r`=4, `w`=2, `x`=1.
- `chmod`, `chown` ruxsat va egasini, `umask` standartni belgilaydi.
- `systemctl` xizmatni, `journalctl` logni boshqaradi.
- `ip a`, `ss -lntp`, `curl -I`, `dig` — tarmoq birinchi yordami.
- Minimal ruxsat qoidasi: kerak bo'lgancha, ortig'i yo'q.

## Qo'shimcha ma'lumot

### sudoedit va visudo
Konfiguratsiyani va sudoers ni xavfsiz tahrirlash.

### Hard va soft link
Hard link inodega, symlink yo'lga ishora qiladi.

### tar
`tar -czf backup.tgz /etc/nginx` zaxira arxivi.

### PATH
Bajariladigan fayl qidiriladigan kataloglar ro'yxati.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Root | Fayl tizimi ildizi `/` |
| chmod | Ruxsatni o'zgartirish |
| chown | Egasini o'zgartirish |
| umask | Standart ruxsat niqobi |
| systemd | Xizmatlar menejeri |
| journalctl | Log ko'rish buyrug'i |
| Quvur | `|` belgisi |
| PID | Jarayon raqami |

## Bilasizmi?

- Linux da qurilmalar ham fayl sifatida ko'rinadi: `/dev/sda`, `/dev/null`.
- `/proc` va `/sys` — yadro va jarayonlar haqida virtual fayl tizimlari.
- `PATH` o'zgaruvchisi bajariladigan fayllar qaysi kataloglarda qidirilishini belgilaydi.

## Topshiriqlar

### 1. Kataloglar · oson

`/etc`, `/var/log`, `/home` vazifasini yozing.

**Kutiladigan natija:** Sozlamalar, loglar, uy papkalari.

### 2. Oktal · oson

`rwx` va `r-x` oktalda?

**Kutiladigan natija:** 7 va 5.

### 3. Ruxsat berish · oson

Skriptga 750 ruxsat bering.

**Kutiladigan natija:** `chmod 750`.

### 4. Navigatsiya · oson

Joriy joyni va katalog tarkibini ko'rsating.

**Kutiladigan natija:** `pwd`, `ls -la`.

### 5. umask · o'rta

`umask 077` da fayl ruxsati?

**Kutiladigan natija:** 600.

### 6. Egasini o'zgartirish · o'rta

`app.log` egasini `odil:dev` qiling.

**Kutiladigan natija:** `chown odil:dev app.log`.

### 7. Xizmat holati · o'rta

`nginx` ni ishga tushiring va avtomatik yoqilishga qo'ying.

**Kutiladigan natija:** `start` va `enable`.

### 8. Log · o'rta

`nginx` loglarini jonli kuzating.

**Kutiladigan natija:** `journalctl -u nginx -f`.

### 9. Tashxis · qiyin

Port 80 ni kim tinglayapti? Qanday toping?

**Kutiladigan natija:** `ss -lntp | grep :80`.

### 10. Disk · qiyin

Qaysi log katta joy egallayapti?

**Kutiladigan natija:** `du -sh /var/log/* | sort -h | tail`.

### 11. Quvur · qiyin

`access.log` dan eng ko'p kirgan IP ni toping.

**Kutiladigan natija:** `awk | sort | uniq -c | sort -nr | head`.

### 12. Minimal ruxsat · bonus

Bir kutubxona skripti uchun ruxsat rejasi yozing.

**Kutiladigan natija:** Aniq egasi va 750/640.

## O'zingizni tekshiring

1. `rwxr-x---` oktalda?
2. `umask 022` natijasi?
3. `systemctl status` nima?
4. Loglar qayerda?
5. `ss -lntp` nima?
6. Minimal ruxsat nima?

## Uyga vazifa

Linux buyruqlari va ruxsatlar bo'yicha mashqlar (30 daqiqa). To'liq shart: `uyga-vazifa.md`.
