# 1-hafta: Uyga vazifalar to'plami (Android dasturlash)

Ushbu haftada o'tilgan darslar bo'yicha mustaqil amaliy uyga vazifalar ro'yxati:

---

## 1-dars. Android nima va uning rivojlanish tarixi
1. Shaxsiy smartfoningiz (yoki oila a'zolaringizdan birining telefoni) sozlamalariga kirib, uning Android versiyasini, modelini va texnik parametrlarini (RAM, protsessor) aniqlang va daftaringizga yozing.
2. «Android versiyasi» ustiga bir necha bor bosib, yashirin Easter Egg o'yinini oching va uning qisqa tasvirini yozing.
3. O'zbekistonda yaratilgan va o'zingiz faol foydalanadigan 3 ta mobil ilovani tanlang. Ularning qaysi funksiyalari aholiga eng ko'p qulaylik keltirayotganini tahlil qiling.

---

## 2-dars. Android tizimi va uning arxitekturasi
1. Android arxitekturasining 5 ta qatlamini (Linux Kernel, HAL, ART/Libraries, Java API Framework, Applications) chizib, daftaringizda ko'p qavatli bino shaklida tasvirlang.
2. Nima sababdan Android 5.0 dan boshlab eski Dalvik (JIT) virtual mashinasidan zamonaviy ART (AOT) tizimiga o'tildi? Asosiy texnik sabablarni yozing.
3. «Application Sandbox» nima va u telefoningizdagi bank ilovalari (Click, Payme) xavfsizligini qanday ta'minlashini tushuntiring.

---

## 3-dars. Androidning imkoniyatlari va qo‘llanilish sohalari
1. Smartfoningizda ekranni ikkiga bo'lish (Split-screen) rejimini yoqing va uning afzalliklari bo'yicha qisqa xulosa yozing.
2. Aqlli soat (Wear OS) va televizor (Android TV) interfeyslarini taqqoslovchi jadval tuzing: ekran o'lchami, boshqaruv turi va dasturchiga qo'yiladigan talablar.
3. Tasavvur qiling, siz maktabingiz uchun Android asosida ishlaydigan aqlli kiosk yaratmoqchisiz. Ushbu kiosk qanday apparat qismlaridan (ekran, kamera, NFC) foydalanishi va unda qanday ilova bo'lishi kerakligini yozma bayon qiling.

---

## Mentor uchun

### Baholash mezonlari (100 ballik tizim)

1. **Android tarixi va ekotizimi tahlili (30 ball):**
   - Android Inc., Andy Rubin va Google xaridi tarixini to'g'ri tushunishi (10 ball);
   - Versiyalar rivojlanishi va shirinlik nomlaridan raqamlarga o'tish sababini bilishi (10 ball);
   - Mahalliy mobil ilovalar va bozor tahlilini asosli ifodalashi (10 ball).

2. **Arxitektura va xavfsizlik modeli (40 ball):**
   - 5 ta vertikal qatlamni to'g'ri joylashtirishi va vazifalarini bayon qilishi (15 ball);
   - Dalvik (JIT) va ART (AOT) o'rtasidagi farqni unumdorlik va batareya tejamkorligi nuqtai nazaridan asoslay olishi (15 ball);
   - Linux yadrosi va Application Sandbox xavfsizlik modelini to'g'ri tushunishi (10 ball).

3. **Qo'llanilish sohalari va adaptiv dizayn (30 ball):**
   - Wear OS, Android Auto va Android TV farqlarini to'g'ri ajratishi (15 ball);
   - Kiosk yoki IoT loyihasi g'oyasini texnik jihatdan to'g'ri ifodalashi (15 ball).

### Kutiladigan namunaviy natijalar
- O'quvchi Android shunchaki telefon emas, balki Linux yadrosiga qurilgan global platforma ekanini chuqur tushunishi shart;
- Arxitektura tahlilida ilovalarning alohida UID ostida izolyatsiyalanishi va ART ning ilovani oldindan (AOT) mashina kodiga kompilyatsiya qilishi aniq ko'rsatilishi kerak.
