# 1-hafta: Uyga vazifalar to'plami (Kiberxavfsizlik)

Ushbu haftada o'tilgan darslar bo'yicha mustaqil amaliy uyga vazifalar ro'yxati:

---

## 1-dars. Kiberxavfsizlik asoslari: axborot xavfsizligi, kiberjinoyat, inson omili va aktivlar
1. O'zingiz muntazam foydalanadigan bitta raqamli tizimni tanlang (masalan, maktab elektron jurnali, Telegram kanalingiz yoki shaxsiy Google hisobingiz).
2. Ushbu tizim uchun 3 ta asosiy aktivni aniqlang va jadvalga yozing:
   - Aktiv nomi va turi (Ma'lumot / Dastur / Uskuna);
   - Unga tahdid soluvchi potensial omil;
   - Qanday zaiflik tufayli zarar yetishi mumkinligi;
   - Ushbu aktivni himoyalash uchun qanday aniq chora ko'rish kerakligi.
3. Inson omili tufayli yuzaga kelishi mumkin bo'lgan 3 ta real xatoni daftaringizga yozing.

---

## 2-dars. Kibertahdidlarning turlari: zararli dasturlar va DoS/DDoS hujumlari
1. Konspektdagi zararli dasturlarning 9 ta turini o'rganing va ulardan istalgan 3 tasini (masalan, Worm, Trojan, Ransomware) taqqoslovchi jadval tuzing.
2. Nima sababdan Slowloris hujumi past tezlikli DoS deb ataladi va an'anaviy gigabitli UDP-flood hujumlaridan qanday farq qiladi? Qisqa tahliliy javob yozing.
3. Ransomware hujumiga uchragan foydalanuvchiga tovon pulini to'lash nega tavsiya etilmasligini va 3-2-1 zaxiralash qoidasini yozma tushuntiring.

---

## 3-dars. Ijtimoiy muhandislik, fishing va email tahlili
1. O'z pochtangizdagi (Gmail, Mail.ru yoki boshqa) «Spam» jildini oching va kelgan shubhali xatlardan birini tanlang (yoki konspektdagi UzSanoat Bank xabari namunasidan foydalaning).
2. Xatning sarlavhalarini (Headers) oching:
   - Jo'natuvchi manzili va domenini tekshiring;
   - Xatdagi havolalarni shaxsiy brauzerda **ochmasdan**, `urlscan.io` orqali tekshirib ko'ring;
   - Sarlavhalarni `mxtoolbox.com/EmailHeaders.aspx` ga kiritib, SPF va DMARC holatini aniqlang.
3. Tahlil natijalari bo'yicha qisqa xulosa (xat fishing ekanligi yoki emasligi isboti bilan) tayyorlang.

---

## Mentor uchun

### Baholash mezonlari (100 ballik tizim)

1. **Nazariy tushunchalar va aktivlar tahlili (30 ball):**
   - Axborot xavfsizligi, kiberxavfsizlik, aktiv, zaiflik va tahdid o'rtasidagi farqlarni to'g'ri tushuntirishi (10 ball);
   - Inson omilining xavfsizlikka ta'sirini to'g'ri baholashi (10 ball);
   - Aktivlar va xavflar tahlili jadvalining asosli to'ldirilganligi (10 ball).

2. **Zararli dasturlar va DoS tushunchalari (30 ball):**
   - Virus, qurt, troyan va ransomware farqlarini aniq ajrata olishi (10 ball);
   - DoS va DDoS arxitekturasi hamda Slowloris ishlash mexanizmini to'g'ri tushunishi (10 ball);
   - 3-2-1 zaxiralash tamoyilini to'g'ri ifodalashi (10 ball).

3. **Pochta tahlili va amaliy ko'nikmalar (40 ball):**
   - Xat sarlavhalarini to'g'ri ajratib olish va tahlil qila olishi (15 ball);
   - MX Toolbox, urlscan.io va VirusTotal platformalari natijalarini to'g'ri talqin qilishi (15 ball);
   - SPF, DKIM va DMARC tekshiruvlarining ma'nosini to'g'ri asoslay olishi (10 ball).

### Kutiladigan namunaviy natijalar
- O'quvchi shubhali xat matnini ko'rib, asosiy domen va subdomen farqini ko'rsata olishi shart;
- urlscan.io yoki MX Toolbox orqali SPF/DMARC statusini tekshirib, xat soxta ekanligini ilmiy asoslab berishi kerak.
