# 4-hafta: Uyga vazifalar to'plami (Kiberxavfsizlik)

Ushbu haftada o'tilgan darslar bo'yicha mustaqil amaliy uyga vazifalar (har biri 20-30 daqiqa).

---

## 10-dars. Tarmoq qurilmalari va xavfsizlik muammolari (1-qism)
1. Maktab yoki uyingizdagi tarmoq sxemasini chizing: kompyuter, switch, router, gateway va internet. Har bir qurilma yoniga OSI sathini yozing.
2. Hab, switch va router uchun jadval tuzing: qaysi sathda, nimaga qaraydi, ma'lumotni qayerga beradi.
3. Quyidagi 5 holatni zaiflik, tahdid yoki hujum deb tasniflang va ichki yoki tashqi ekanini yozing: (a) yangilanmagan brauzer; (b) ishdan ketgan xodim diskka kira oladi; (c) tayyor skript bilan sinab ko'ruvchi notanish shaxs; (d) server DDoS ostida; (e) shifrlanmagan protokol ma'lumotni oshkor qiladi.

---

## 11-dars. Wireshark yordamida tarmoq trafigini tahlil qilish
1. Kompyuteringizga Wiresharkni o'rnating (Npcap bilan) va faol interfeysni tanlab, capture boshlang. Oynaning 3 panelini skrinshotda belgilang.
2. `http` va `tls` filtrlari bilan har birida GET so'rovi va TLS Client Hello paketini toping.
3. TCP, UDP, DNS va ICMP protokollari bo'yicha kamida 3 tadan paketni tahlil qilib (Source, Destination, Protocol, Info), natijalarni fayl ko'rinishida saqlang va hisobot tayyorlang.
4. Sayt ochilishini 4 bosqichda o'z so'zlaringiz bilan yozing.

---

## 12-dars. Ping va traceroute buyruqlari bilan marshrutlarni tahlil qilish
1. 4 ta turli saytga `ping` yuboring. Jadval: sayt, o'rtacha ms, yo'qotish %, TTL, taxminiy hop soni (128 yoki 64 dan ayirib).
2. Shu saytlarga `tracert` (Linux/Mac: `traceroute`) yuboring; kamida bittasida flaglardan foydalaning (`-d`, `-h`, `-w`).
3. Bitta marshrutni hop-hop izohlang: uy routeri, provayder, O'zbekiston uzeli, tashqi tranzit, manzil.
4. `* * *` chiqqan bo'lsa, buning mumkin bo'lgan sababini yozing.

---

## Mentor uchun

### Baholash mezonlari (100 ballik tizim)

1. **Tarmoq qurilmalari va xavf tasnifi (30 ball):**
   - Qurilmalarni OSI sathiga to'g'ri moslashi (15 ball);
   - Zaiflik, tahdid va hujumni to'g'ri ajratishi (15 ball).

2. **Wireshark tahlili (35 ball):**
   - O'rnatish, interfeys tanlash va capture bajarilishi (10 ball);
   - `http` va `tls` filtrlari natijalari (10 ball);
   - Protokol bo'yicha paket tahlili hisoboti (15 ball).

3. **Ping va traceroute tahlili (35 ball):**
   - Buyruqlarni to'g'ri bajarishi va jadval to'ldirishi (15 ball);
   - RTT, TTL, hop va `* * *` ni to'g'ri izohlashi (15 ball);
   - Flaglardan foydalanishi (5 ball).

### Kutiladigan namunaviy natijalar
- Sayt ochilishi «DNS, TCP handshake, TLS, HTTP GET» ko'rinishida aniq tushuntirilishi kerak.
- `* * *` hujum belgisi deb emas, ICMP bloklangani deb izohlanishi kerak.
- Hisobotda faqat o'z trafigi tahlil qilinganligi tekshiriladi.
