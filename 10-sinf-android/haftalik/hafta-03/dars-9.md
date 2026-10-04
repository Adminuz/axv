# 9-dars: GitHub’da loyihalar yaratish va boshqarish

**Fan:** Advanced Android dasturlash  
**Sinf:** 10-sinf  
**Hafta:** 3-hafta, 3-dars (umumiy 9-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga global tarqoq dasturlash platformasi hisoblangan **GitHub**ning vazifasi va imkoniyatlarini tushuntirish, masofaviy repozitoriy (**Remote Repository**) yaratish, lokal Git omborini GitHub bilan bog'lash (`git remote add origin`), kodlarni serverga yuklash (`git push -u origin main`) va o'zgarishlarni qabul qilish (`git pull`), loyiha yuzi hisoblangan professional `README.md` faylini Markdown formatida shakllantirish, vazifalarni boshqarish vositasi (**Issues**) bilan ishlash hamda Android Studio muhitidan to'g'ridan-to'g'ri GitHub bilan integratsiyalash ko'nikmalarini chuqur shakllantirish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- Git (lokal vosita) va GitHub (onlayn bulutli platforma) o'rtasidagi farqni aniq bilish;
- GitHub'da yangi repozitoriy ochishda Public vs Private turlarining strategik farqlarini tushunish;
- `git remote add origin <url>`, `git remote -v`, `git push -u origin main` va `git pull` buyruqlarini terminalda erkin qo'llay olish;
- Personal Access Token (PAT) yoki SSH kalitlari orqali GitHub xavfsiz avtorizatsiyasidan o'tishni tushunish;
- Professional darajadagi `README.md` faylini yozish (loyiha tavsifi, skrinshotlar, o'rnatish yo'riqnomasi, texnologiyalar ro'yxati);
- Loyihadagi vazifalar, takliflar va xatolarni qayd etish uchun GitHub Issues vositasidan foydalana olish;
- Android Studio ichidagi VCS vositalari orqali loyihani bir tugma bilan GitHub'da e'lon qilishni bilish.

---

## Kerakli jihozlar va vositalar

- Kompyuter yoki noutbuk;
- Internet tarmog'iga ulanish;
- O'quvchining shaxsiy GitHub akkaunti (github.com);
- Git va Android Studio dasturlari;
- Proyektor yoki monitor.

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va o'tgan dars takrori | Git branching, merge va to'qnashuvlarni hal qilish bo'yicha savol-javob |
| **10–30 min** | Yangi mavzu bayoni (Nazariya) | GitHub nima, Remote repo arxitekturasi, `push`/`pull` mexanizmi, README va Issues |
| **30–55 min** | Amaliy mashg'ulot (GitHub'ga yuklash) | GitHub'da repo ochish, lokal Android loyihasini remote ga ulash va `git push` qilish |
| **55–75 min** | Mustaqil amaliy ish (README & Issues) | Chiroyli `README.md` yozish, Issues doskasida vazifalar ochish va hamkor qo'shish |
| **75–80 min** | Xulosa va baholash | Tezkor savol-javob, 3-hafta yakuniy xulosalari va uyga vazifa |

---

## Nazariy qism (Batafsil tushuntirish)

### 1. Git va GitHub: Ular orasidagi farq nima?

Yangi boshlovchilar ko'pincha Git va GitHub bitta narsa deb o'ylashadi. Aslida:
- **Git** — bu sizning kompyuteringizda ishlaydigan dastur (lokal texnologiya). U o'zgarishlar tarixini kuzatadi.
- **GitHub** — bu internetda joylashgan bulutli platforma (onlayn servis). U Git repozitoriyalarini saqlaydi, dasturchilarga kodni butun dunyo bilan bo'lishish, jamoa bo'lib ishlash va portfoliolarini namoyish etish imkonini beradi.

Git — dvigatel bo'lsa, GitHub — butun dunyo avtomobillari harakatlanadigan xalqaro avtomagistraldir.

---

### 2. GitHub repozitoriyasi: Public vs Private

GitHub'da yangi repozitoriy ochishda quyidagi sozlamalar belgilanadi:
1. **Repository Name:** Qisqa, tushunarli va ma'noli nom (masalan, `weather-forecast-app`, `smart-finance-android`). Nomda bo'sh joy (probel) ishlatilmaydi, chiziqcha (`-`) qo'yiladi.
2. **Public (Ochiq):** Butun dunyo kodingizni ko'ra oladi, yuklab olishi va o'rganishi mumkin. Bu dasturchining professional rezumesi (CV) va portfoliosi uchun eng yaxshi vositadir.
3. **Private (Yopiq):** Kod faqat sizga va siz taklif qilgan jamoa a'zolariga ko'rinadi. Tijoriy loyihalar va maxfiy dasturlar uchun ishlatiladi.

---

### 3. Lokal kodni GitHub bilan bog'lash va Push qilish

Lokal kompyuteringizdagi mavjud Git repozitoriyasini GitHub bilan bog'lash uchun quyidagi buyruqlar bajariladi:

```bash
# 1. Masofaviy manzilni 'origin' nomi bilan ro'yxatga olish:
git remote add origin https://github.com/username/weather-forecast-app.git

# 2. Bog'langan manzillarni tekshirish:
git remote -v

# 3. Asosiy tarmoq nomini 'main' ga keltirish:
git branch -M main

# 4. Kodni birinchi marta serverga yuklash (-u flagi keyingi push larni osonlashtiradi):
git push -u origin main
```

Shundan so'ng, keyingi har bir commitdan keyin shunchaki:
```bash
git push
```
buyrug'ini berish kifoya.

Boshqalar kiritgan o'zgarishlarni kompyuteringizga yuklab olish uchun esa:
```bash
git pull origin main
```
ishlatiladi.

---

### 4. `README.md` faylining ahamiyati

`README.md` — bu repozitoriyning "yuzi" va tashrif qog'ozidir. Ish beruvchi yoki boshqa dasturchi loyihangizga kirganda birinchi bo'lib aynan shu faylni o'qiydi.

Fayl Markdown formatida yoziladi:
```markdown
# 🌤 Smart Weather App

Android operatsion tizimi uchun zamonaviy ob-havo ilovasi. 
OpenWeatherMap API orqali real vaqt rejimidagi ma'lumotlarni taqdim etadi.

## 📱 Ekran suratlari
![Bosh sahifa](screenshots/home.png)

## 🛠 Texnologiyalar to'plami
- Kotlin & Coroutines
- Jetpack Compose / XML
- Retrofit & Gson
- Room Database (Offline kesh)

## 🚀 O'rnatish va ishga tushirish
1. Repozitoriyani klonlang:
   git clone https://github.com/username/weather-app.git
2. Android Studio'da oching va 'Run' tugmasini bosing.
```

---

### 5. Issues (Muammolar va Vazifalar taxtasi)

GitHub **Issues** bo'limi loyihadagi xatolar (Bug report), yangi takliflar (Feature request) va jamoaviy vazifalarni qayd etish uchun ishlatiladi.
- Har bir issue o'zining unikal tartib raqamiga ega bo'ladi (masalan, `#1`, `#2`).
- Commit xabarida issue raqami ko'rsatilsa (masalan, `git commit -m "fix: login crash muammosi tuzatildi, fixes #1"`), GitHub ushbu issue'ni avtomatik tarzda yopadi (Close).

---

### 6. Android Studio integratsiyasi

Android Studio ichidan GitHub'ga chiqish uchun:
1. **Settings > Version Control > GitHub** bo'limidan akkaunt ulanadi.
2. Yuqori menyudan **Git > Share Project on GitHub** tugmasi bosiladi.
3. Android Studio avtomatik repozitoriy yaratadi, `.gitignore` ni tekshiradi va birinchi push'ni bajaradi.

---

## Amaliy topshiriqlar (Sinfda bajarish uchun)

### 1-topshiriq: GitHub'da repo ochish va lokal kodni push qilish

**Vazifa:** GitHub profilingizda `MyFirstAndroidRepo` nomli yangi Public repozitoriy oching. O'tgan darsda yaratilgan lokal loyihangizni unga ulang va barcha commitlarni `main` tarmog'iga push qiling.

**Yechim:**
```bash
# 1. Lokal loyiha papkasida ekanimizni tekshiramiz
pwd

# 2. Remote manzilni ulaymiz (username o'rniga o'z GitHub nomingiz)
git remote add origin https://github.com/alivaliyev/MyFirstAndroidRepo.git

# 3. Ulanganini tekshiramiz
git remote -v

# 4. Asosiy tarmoqni main deb belgilaymiz
git branch -M main

# 5. Serverga yuklaymiz
git push -u origin main
```
GitHub sahifasini yangilang (F5) — barcha fayllar va commitlar tarixi internetda paydo bo'ladi.

---

### 2-topshiriq: Professional `README.md` faylini yaratish

**Vazifa:** Loyiha ildizida `README.md` faylini yarating. Unda loyiha nomi, 2 jumlali tavsif, ishlatilgan texnologiyalar ro'yxati va dasturni ishga tushirish qadamlarini Markdown sintaksisida yozing. So'ngra uni commit qilib, GitHub'ga push qiling.

**Yechim:**
1. `README.md` faylini yaratamiz:
```markdown
# 📱 Android Notes App

«Muhammad al-Xorazmiy vorislari» kursi doirasida yaratilgan Android eslatmalar ilovasi.

## 🛠 Texnologiyalar
- Kotlin 1.9
- Android SDK (API 24 - 34)
- ProGuard va R8 optimallashtirish
- Git versiya nazorati

## 🚀 Ishga tushirish
```bash
git clone https://github.com/alivaliyev/MyFirstAndroidRepo.git
```
Loyihani Android Studio'da oching va emulyatorda ishga tushiring.
```

2. Terminalda yuklaymiz:
```bash
git add README.md
git commit -m "docs: to'liq README fayli yaratildi"
git push
```

---

### 3-topshiriq: GitHub Issues bilan ishlash va commit orqali yopish

**Vazifa:**
1. GitHub repozitoriyangizdagi "Issues" bo'limiga kiring va "New issue" tugmasini bosing.
2. "Bosh sahifada qidiruv tugmasini qo'shish kerak" nomli yangi issue oching (u `#1` raqamini oladi).
3. Kompyuteringizdagi loyihada `Search.kt` faylini oching va commit xabarida `fixes #1` kalit so'zini qo'llab push qiling.
4. GitHub'da issue avtomatik yopilganini kuzating.

**Yechim:**
```bash
# 1. Fayl yaratamiz
echo "// Qidiruv moduli" > Search.kt

# 2. Sahnaga olamiz
git add Search.kt

# 3. Maxsus 'fixes #1' xabari bilan commit qilamiz
git commit -m "feat: qidiruv funksiyasi qo'shildi, fixes #1"

# 4. Push qilamiz
git push origin main
```
GitHub'ga qaytib "Issues" bo'limini ko'rsangiz, `#1` issue'ning holati avtomatik tarzda "Closed" ga o'tgan bo'ladi!

---

## Tezkor savol-javob (Quick Check)

1. **Savol:** Git va GitHub o'rtasidagi asosiy farq nima?  
   **Javob:** Git — kompyuterda o'rnatiladigan versiya nazorati dasturi. GitHub — Git repozitoriyalarini internetda saqlovchi va jamoaviy ishlashni ta'minlovchi bulutli veb-platformadir.

2. **Savol:** `git remote add origin <url>` buyrug'idagi `origin` so'zi nimani bildiradi?  
   **Javob:** Bu masofaviy repozitoriy (Remote repository) serveriga berilgan standart qisqa nom (taxallus).

3. **Savol:** `git push` va `git pull` buyruqlarining vazifasi nima?  
   **Javob:** `git push` lokal kompyuterdagi commitlarni GitHub serveriga yuklaydi, `git pull` esa serverdagi yangi o'zgarishlarni kompyuterga yuklab oladi.

4. **Savol:** Nima sababdan `README.md` fayli har bir repozitoriy uchun muhim hisoblanadi?  
   **Javob:** U loyihaning bosh sahifasida avtomatik aks etadi va foydalanuvchilar hamda ish beruvchilarga loyiha nima haqidaligi, qanday ishlashi va qanday o'rnatilishini tushuntiradi.

5. **Savol:** Commit xabariga `fixes #1` deb yozish GitHub'da qanday natija beradi?  
   **Javob:** Ushbu commit push qilinganda, GitHub avtomatik ravishda 1-raqamli issue'ni muvaffaqiyatli yopilgan (Closed) deb belgilaydi.

---

## Uyga vazifa

1. O'z kompyuteringizdagi Android loyihalaridan birini tanlang va uni GitHub'da yangi Public repozitoriy ochib yuklang (`git push`).
2. Repozitoriyga skrinshotlar va chiroyli nishonlar (badge) bilan boyitilgan `README.md` faylini yozing.
3. Loyihangizda kamida 2 ta yangi "Issue" oching: biri rejadagi yangi ekran haqida, ikkinchisi tuzatilishi kerak bo'lgan xato haqida. Repozitoriy havolasini mentorga yuboring.
