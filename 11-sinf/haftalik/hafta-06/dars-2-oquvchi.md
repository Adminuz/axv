# 17-dars. SSH: kalitga asoslangan autentifikatsiya va xavfsiz ulanish

> Parol bilan serverga kirish — eshikni oddiy qulf bilan yopish. Bugun SSH kalit juftligi bilan xavfsizroq kirishni o'rganamiz.

## Dars xulosasi

- SSH da parol zaif, kalit kuchli.
- Kalit jufti: private (sirda) va public (serverga).
- `ssh-keygen -t ed25519` kalit yaratadi, `ssh-copy-id` joylaydi.
- `~/.ssh` 700, `authorized_keys` 600.
- `PasswordAuthentication no` dan oldin kalitni sinab oling.
- `~/.ssh/config` va `ssh -vvv` ishni va diagnostikani soddalashtiradi.

## Qo'shimcha ma'lumot

### MITM
O'rtadagi odam hujumi; `known_hosts` himoyalaydi.

### Passphrase
Shaxsiy kalitni qo'shimcha himoyalovchi parol ibora.

### Kalit aylantirish
Kalitlarni vaqti-vaqti bilan yangilash va eskisini o'chirish.

### rsync/sftp
Fayl yuborish, kalit bilan parolsiz.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| SSH | Xavfsiz masofaviy ulanish protokoli |
| Private key | Shaxsiy kalit |
| Public key | Ommaviy kalit |
| ed25519 | Zamonaviy kalit algoritmi |
| authorized_keys | Ruxsat berilgan kalitlar |
| known_hosts | Tanilgan serverlar |
| ssh-agent | Kalitni xotirada saqlovchi |
| Passphrase | Kalit paroli |

## Bilasizmi?

- `ssh-agent` kalitni seans davomida xotirada ushlab, passphrase ni qayta-qayta so'ramaydi.
- Windows 10/11 da OpenSSH Client odatda o'rnatilgan.
- `fail2ban` va `ufw` kabi vositalar SSH ni qo'shimcha himoyalaydi.

## Topshiriqlar

### 1. Kalit nima · oson

Private va public kalit farqini yozing.

**Kutiladigan natija:** Private sirda, public serverga.

### 2. Yaratish · oson

`ed25519` kalitni yarating.

**Kutiladigan natija:** `ssh-keygen -t ed25519`.

### 3. Fayllar · oson

Qaysi fayl ommaviy?

**Kutiladigan natija:** `.pub` fayl.

### 4. Joylash · oson

Ommaviy kalitni serverga qo'ying.

**Kutiladigan natija:** `ssh-copy-id`.

### 5. Ruxsatlar · o'rta

`~/.ssh` va `authorized_keys` ruxsatlari?

**Kutiladigan natija:** 700 va 600.

### 6. Birinchi ulanish · o'rta

`known_hosts` nima uchun kerak?

**Kutiladigan natija:** MITM dan himoya.

### 7. Config · o'rta

`ssh prod` uchun config yozing.

**Kutiladigan natija:** `Host prod` bloki.

### 8. sshd_config · o'rta

Parol va root kirishni o'chirish sozlamalari?

**Kutiladigan natija:** `PasswordAuthentication no`, `PermitRootLogin no`.

### 9. Tartib · qiyin

Parolni o'chirishda xavfsiz tartibni yozing.

**Kutiladigan natija:** Avval kalitni sinash, keyin o'chirish.

### 10. Diagnostika · qiyin

`Permission denied (publickey)` sababini qidiring.

**Kutiladigan natija:** Ruxsat, format, `-vvv`, log.

### 11. Kalit yo'qolsa · qiyin

Shaxsiy kalit sizsa nima qilasiz?

**Kutiladigan natija:** Ommaviy kalitni serverlardan o'chirish.

### 12. Cheklash · bonus

`authorized_keys` da bitta IP diapazoni uchun cheklov yozing.

**Kutiladigan natija:** `from="..."` prefiksi.

## O'zingizni tekshiring

1. Qaysi kalit serverga qo'yiladi?
2. `ed25519` nima?
3. `~/.ssh` va `authorized_keys` ruxsati?
4. Parolni o'chirishdan oldin nima?
5. `ssh -vvv` nima?
6. `~/.ssh/config` nima uchun?

## Uyga vazifa

SSH kalit va config bo'yicha topshiriq (30 daqiqa). To'liq shart: `uyga-vazifa.md`.
