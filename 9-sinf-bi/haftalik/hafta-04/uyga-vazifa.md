# 4-hafta: Uyga vazifalar to'plami

Mazkur haftada o'tilgan darslar bo'yicha mustaqil bajarish uchun topshiriqlar. Har bir vazifa 20–30 daqiqaga mo'ljallangan.

---

## 10-dars: Normalizatsiya asoslari va BI'dagi o'rni

1. Quyidagi «yassi» kutubxona jadvalini oling: `KitobID, KitobNomi, Muallif, MuallifDavlati, OquvchiIsmi, OquvchiSinfi, OlinganSana, QaytarishSana`.
2. Undagi takrorlanuvchi ma'lumotlarni belgilang va har bir anomaliya (Update, Insert, Delete) uchun bittadan misol yozing.
3. Jadvalni bosqichma-bosqich 1NF → 2NF → 3NF ga keltiring. Natijada 3–4 ta jadval hosil bo'ladi (masalan: `Mualliflar`, `Kitoblar`, `Oquvchilar`, `Ijaralar`).
4. Sxemani daftarda chizing: har bir jadvalda PK, FK va munosabat turi (1:N, M:N) ko'rsatilsin.

**Kutiladigan natija:** anomaliyalar tahlili va 3NF dagi bog'langan jadvallar sxemasi.

---

## 11-dars: RDBMS muhitlari va ma'lumotlar yaxlitligi

1. 10-dars uyga vazifasidagi kutubxona modeli uchun SSMS da (yoki SQLite da) `Kutubxona` bazasini yarating.
2. Har bir jadval uchun `CREATE TABLE` skriptini yozing: PK, kerakli FK, kamida bittadan `NOT NULL`, `UNIQUE`, `CHECK` (masalan, `QaytarishSana >= OlinganSana`) va `DEFAULT`.
3. Har bir jadvalga 3 tadan to'g'ri yozuv qo'shing (`INSERT`).
4. Har bir cheklov turini buzadigan bittadan `INSERT` yozing, bajaring va chiqqan xato xabarini 1 jumlada izohlang.

**Kutiladigan natija:** ishlaydigan skript, to'ldirilgan jadvallar va 5 ta izohlangan xato.

---

## 12-dars: SQL asoslari — SELECT, ustunlar va sodda ifodalar

1. Darsdagi `Mahsulotlar` jadvalini 10 ta mahsulotgacha to'ldiring (yangi `INSERT` lar).
2. Quyidagi 6 ta so'rovni yozing va bajaring:
   - barcha ustunlar;
   - nomi va narxi `Mahsulot` va `Narx (so'm)` taxalluslari bilan;
   - har bir mahsulotning ombor qiymati (`Narx * Soni`);
   - QQS bilan narx (`Narx * 1.12`);
   - takrorsiz kategoriyalar (`DISTINCT`);
   - birinchi 3 ta mahsulot (`TOP 3`).
3. Har bir so'rov ostiga natijada nechta qator va ustun chiqqanini hamda 1 ta xulosani yozing.

**Kutiladigan natija:** `.sql` fayl (yoki daftar) — 6 ta to'g'ri so'rov va natijalar tavsifi.

---

## Mentor uchun

Keyingi dars boshida (13-dars, WHERE) 2–3 o'quvchining 11-darsdagi xato xabarlarini ekranda ko'rsatib muhokama qiling: qaysi cheklov qaysi yaxlitlik turini himoya qiladi. 12-darsdagi `Mahsulotlar` jadvali 13-darsda WHERE filtrlari uchun asos bo'lib xizmat qiladi — o'quvchilar uni saqlab qo'ysin.
