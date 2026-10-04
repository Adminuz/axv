# 3-hafta: Uyga vazifalar to'plami (Kiberxavfsizlik)

Ushbu haftada o'tilgan darslar bo'yicha mustaqil amaliy uyga vazifalar ro'yxati:

---

## 7-dars. Raqamli gigiyena va shaxsiy kiberxavfsizlik
1. O'zingiz muntazam foydalanadigan brauzeringizga (Chrome, Firefox yoki Edge) `uBlock Origin` va `ClearURLs` kengaytmalarini o'rnating. Har qanday 3 ta ommabop yangiliklar saytiga kirib, qancha kuzatuvchi (tracker) va reklama skriptlari bloklanganini qayd eting.
2. Shaxsiy kompyuteringiz yoki smartfoningizda shifrlangan xavfsiz DNS serverini (Cloudflare `1.1.1.1` yoki `1.1.1.2` zararli dasturlardan himoyalangan DNS) sozlang. Sozlash jarayonini skrinshotlar orqali hujjatlashtiring.
3. Telegram yoki Google hisobingizda 2-bosqichli tasdiqlash (2FA) yoqilganligini tekshiring, agar yoqilmagan bo'lsa yoqing va maxfiy tiklash kodi/parolini ishonchli offline joyda saqlang.

---

## 8-dars. STRIDE tahdid modeli, Red Team vs Blue Team va CTF musobaqalari
1. O'zingiz bilgan bitta onlayn servis (masalan, maktab oshxonasi to'lov ilovasi yoki onlayn kutubxona tizimi) uchun STRIDE modeli bo'yicha tahdidlar tahlili jadvalini to'ldiring:
   - **S (Spoofing):** Birov boshqa o'quvchi nomidan tizimga kirish xavfi;
   - **T (Tampering):** Hisobdagi balans yoki kitob ma'lumotlarini o'zgartirish xavfi;
   - **R (Repudiation):** O'tkazilgan to'lov yoki olingan kitobni rad etish xavfi;
   - **I (Information Disclosure):** O'quvchilar telefon raqamlari yoki parollarining oqib ketishi;
   - **D (Denial of Service):** Tizimni ko'p so'rovlar yuborib ishdan chiqarish;
   - **E (Elevation of Privilege):** Oddiy o'quvchining administrator huquqiga ega bo'lib olishi.
2. Red Team va Blue Team rollarini solishtiruvchi qisqa esse (1 sahifa) yozing: nega tashkilotlar uchun faqat himoyalanish (Blue Team) yetarli emas va doimiy mustaqil sinovlar (Red Team) talab etiladi?
3. CTF musobaqalarining asosiy yo'nalishlari (Web, Forensics, Reverse, Pwn, Crypto) bo'yicha konspekt tuzing.

---

## 9-dars. Tarmoq asoslari: topologiyalar, OSI modeli va TCP/IP steki
1. Yulduzsimon (Star) va To'rsimon (Mesh) topologiyalarining kamida 3 tadan afzallik va kamchiliklarini taqqoslovchi jadval tuzing. Nima sababdan hozirgi zamonaviy lokal tarmoqlarda yulduzsimon topologiya keng qo'llaniladi?
2. OSI modelining 7 ta qatlamini tartib bilan yozing va har bir qatlamda ishlaydigan kamida bittadan protokol yoki qurilmani ko'rsating.
3. TCP va UDP protokollari o'rtasidagi farqni tushuntiring:
   - Nima sababdan veb-saytlarni yuklashda (HTTP/HTTPS) va fayl uzatishda TCP ishlatiladi?
   - Nima sababdan onlayn o'yinlar, videoqo'ng'iroqlar va jonli efirlarda UDP afzal ko'riladi?
4. Kompyuteringiz terminalida `ping` va `traceroute` (yoki Windowsda `tracert`) buyruqlari orqali `google.com` yoki `edu.uz` manziliga tarmoq marshrutini tahlil qiling va natijalarni yozib oling.

---

## Mentor uchun

### Baholash mezonlari (100 ballik tizim)

1. **Raqamli gigiyena va shaxsiy himoya ko'nikmalari (30 ball):**
   - Brauzer kengaytmalari va xavfsiz DNS sozlamalarini mustaqil amalga oshira olishi (15 ball);
   - 2FA (ikki bosqichli autentifikatsiya) ahamiyatini tushunishi va amalda yoqa olishi (15 ball).

2. **Tahdidlarni modellashtirish va jamoalar falsafasi (35 ball):**
   - Tanlangan tizim uchun STRIDE ning barcha 6 ta toifasini to'g'ri va asosli tahlil qilgani (20 ball);
   - Red Team, Blue Team va Purple Team vazifalari o'rtasidagi muvozanatni tushunishi (10 ball);
   - CTF yo'nalishlarini to'g'ri ifodalashi (5 ball).

3. **Tarmoq arxitekturasi va OSI modeli tahlili (35 ball):**
   - Topologiyalar (Star, Mesh, Ring, Bus) xususiyatlarini to'g'ri ajratishi (10 ball);
   - OSI 7 qatlami va TCP/IP 4 qatlami o'rtasidagi o'zaro bog'liqlikni to'g'ri tushuntirishi (15 ball);
   - TCP va UDP farqlarini ishonchli misollar bilan asoslay olishi, ping/traceroute natijalarini to'g'ri o'qiy olishi (10 ball).

### Kutiladigan namunaviy natijalar
- STRIDE tahlilida o'quvchi shunchaki umumiy gaplar yozmasdan, aniq tahdid ssenariysini (masalan: "Tampering: foydalanuvchi HTTP so'rovdagi narx parametrini o'zgartirishi") keltirishi kerak;
- Tarmoq vazifasida TCP ning 3 tomonlama bog'lanishi (SYN, SYN-ACK, ACK) va UDP ning bog'lanish o'rnatmasligi (Connectionless) aniq tushuntirilishi shart.
