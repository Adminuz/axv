# 5-hafta: Uyga vazifalar to'plami (Kiberxavfsizlik)

Ushbu haftada o'tilgan darslar bo'yicha mustaqil amaliy uyga vazifalar (har biri 20-30 daqiqa).

---

## 13-dars. IP-manzillash va qism tarmoqlar (subnets) (1-qism): IPv4 va IPv6 arxitekturasi, sinflar
1. `ipconfig` (yoki `ip a`) natijasidan IPv4, subnet mask va shlyuzni yozing; manzil sinfi va shaxsiy yoki umumiyligini aniqlang.
2. IPv4 va IPv6 farqini jadval qilib yozing (bit, format, manzil soni, sarlavha, manzil turlari).
3. 5 ta IP manzilning sinfini aniqlang: 3.4.5.6, 130.1.1.1, 200.2.2.2, 230.0.0.5, 250.1.1.1.

---

## 14-dars. IP-manzillash va qism tarmoqlar (subnets) (2-qism): CIDR, subnet maska hisoblash va tarmoq segmentatsiyasi
1. 192.168.20.0/24 ni 4 ta teng subnetga bo'ling: har biri uchun tarmoq manzili, host diapazoni va broadcast ni yozing.
2. /25, /27 va /29 prefikslarining maskasi va hostlar sonini hisoblab jadvalga yozing.
3. Maktabingiz uchun 4 segmentli tarmoq rejasini chizing va har segmentga subnet bering; segmentatsiya foydasini 3 jumlada yozing.

---

## 15-dars. Tarmoqlararo ekran va filtrlash (1-qism): Firewall turlari va ishlash prinsiplari
1. Firewall nima va qaysi tarmoqlar orasida turishini 5 jumlada tushuntiring; trusted va untrusted misollar keltiring.
2. Firewall turlarini jadvalga yozing: sath, nima bo'yicha filtrlaydi, afzallik, kamchilik.
3. Quyidagi vaziyat uchun ACL yozing: web-server (80, 443) ochiq; ichkariga tashqi SSH, Telnet va ping taqiqlansin; ichki tarmoq NAT orqali internetga chiqsin.

---

## Mentor uchun

### Baholash mezonlari (100 ballik tizim)

1. **IPv4/IPv6 va sinflar (30 ball):**
   - IPv4 va IPv6 farqini to'g'ri jadvalga yozishi (10 ball);
   - IP sinflari va shaxsiy diapazonlarni to'g'ri aniqlashi (10 ball);
   - `ipconfig` natijasini to'g'ri izohlashi (10 ball).

2. **Subnetlash va segmentatsiya (40 ball):**
   - 4 subnetga bo'lish: tarmoq, hostlar, broadcast (15 ball);
   - Prefikslar jadvali va hostlar soni (10 ball);
   - Maktab segmentatsiya rejasi va asoslash (15 ball).

3. **Firewall va ACL (30 ball):**
   - Firewall ta'rifi va trusted/untrusted misollari (10 ball);
   - Turlar jadvali (10 ball);
   - ACL qoidalari to'g'ri yozilgan, default-deny qo'llangan (10 ball).

### Kutiladigan namunaviy natijalar
- 192.168.20.0/24 ni bo'lish: .0/26, .64/26, .128/26, .192/26; broadcast .63, .127, .191, .255.
- 3.4.5.6 (A), 130.1.1.1 (B), 200.2.2.2 (C), 230.0.0.5 (D), 250.1.1.1 (E).
- ACL: `ALLOW IN ANY -> WebServer:80`, `ALLOW IN ANY -> WebServer:443`, `DENY IN ANY -> InternalNet:22`, `DENY IN ANY -> InternalNet:23`, `DENY IN ANY -> ANY (ICMP Echo Request)`, `NAT OUT InternalNet -> Internet`.
