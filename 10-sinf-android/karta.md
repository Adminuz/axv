# 10-sinf: o'quv xaritasi (Advanced Android dasturlash)

Manba: `4.3. Srtandart`, `4.3. Uslubiy ko'rsatma`, `4.3. O'quv qo'llanma`. Agentlar avval shu faylni o'qiydi, katta .docx'ni qayta o'qimaydi. Matnlari `_matn/` papkasida (chiqarilgan .txt).

**Tuzilma:** 102 dars, haftasiga 3 dars (har biri 80 daqiqa). Hafta = ceil(dars № / 3), jami 34 hafta.

**Holat belgilari:** ⬜ rejada · 📝 materiallar tayyorlangan · ✅ o'tilgan

## Joriy holat

- Oxirgi o'tilgan dars: **0**
- Keyingi dars: **10** (4-hafta)
- Oxirgi yangilanish: **2026-10-04 (3-hafta tayyorlandi: 7-9 darslar)**

## Eslatmalar

- Dastur: «Muhammad al-Xorazmiy vorislari» tizimi bo'yicha maxsus guruhlar (Advanced Android dasturlash).
- O'quv yili 34 hafta, haftasiga 3 darsdan jami 102 dars rejalashtirilgan.


## I bob. Android loyihalarini boshqarish va versiya nazorati tizimlari (12 dars)

| Dars | Hafta | Mavzu | Holat |
|---|---|---|---|
| 1 | 1 | Gradle konfiguratsiyasi va build tizimi asoslari: settings.gradle, build.gradle, SDK versiyalari | 📝 |
| 2 | 1 | Build variantlari va Product Flavors: Debug vs Release, R8 optimallashtirish, BuildConfig | 📝 |
| 3 | 1 | Dependency management va versiyalar bilan ishlash: kutubxonalar, repozitoriylar, Version Catalog (TOML) | 📝 |
| 4 | 2 | Dependency management va ziddiyatlarni hal qilish: tranzitiv bog'liqliklar, exclude, resolutionStrategy | 📝 |
| 5 | 2 | ProGuard va R8 yordamida kodni optimallashtirish (1-qism): Shrinking, Obfuscation, Optimization | 📝 |
| 6 | 2 | ProGuard va R8 qoidalari bilan ishlash (2-qism): -keep qoidalari, Reflection, mapping.txt | 📝 |
| 7 | 3 | Git bilan versiya nazorati asoslari: Git repository, commit, log, .gitignore | 📝 |
| 8 | 3 | Git bilan ishlash amaliyoti: fayllar holati, diff, checkout, reset, revert | 📝 |
| 9 | 3 | GitHub’da loyihalar yaratish va boshqarish: remote repozitoriy, push, pull, issues, README | 📝 |
| 10 | 4 | GitLab va Bitbucket’da jamoaviy ish jarayonlari: loyihani klonlash, access va rollar, pipeline | ⬜ |
| 11 | 4 | Branch, Merge va Pull Request jarayonlari: feature branching, merge konfliktlari, PR va Code Review | ⬜ |
| 12 | 4 | Continuous Integration (CI/CD) tushunchasi: build va test avtomatlashtirish, GitHub Actions | ⬜ |
| 13 | 5 | build.gradle faylining asosiy tuzilmasi va modullararo bog‘lanishi | ⬜ |
| 14 | 5 | Build variantlar (debug, release) va ularning farqi | ⬜ |
| 15 | 5 | Gradle yordamida kutubxonalarni ulash va versiyalarni boshqarish ko‘nikmasiga ega bo‘ladi; | ⬜ |
| 16 | 6 | Gradle so‘rovlarini (tasks) bajarish va xatoliklarni aniqlashni biladi; | ⬜ |
| 17 | 6 | build.gradle faylida kutubxonalarni ulash va boshqarishni biladi; | ⬜ |
| 18 | 6 | implementation, api, compileOnly kabi dependency turlarining farqini tushunadi; | ⬜ |
| 19 | 7 | Kutubxona versiyalarini yangilash va moslik muammolarini hal qilish ko‘nikmasiga ega bo‘ladi; | ⬜ |
| 20 | 7 | Versiyalarni avtomatik boshqarish va yangilanishni tekshirish usullarini qo‘llay oladi; | ⬜ |
| 21 | 7 | R8 ning Android’da standart bo‘lishi, ProGuard’dan farqi va ularning ishlash tamoyillarini biladi; | ⬜ |
| 22 | 8 | proguard-rules.pro faylida - keep, - dontwarn, sinf/a’zo patternlari bilan ishlashni amaliy qo‘llay oladi; | ⬜ |
| 23 | 8 | Obfuskatsiya sababli yuzaga keladigan xatolarni aniqlash, mapping.txt orqali stacktrace’ni deobfuskatsiya qilishni biladi; | ⬜ |
| 24 | 8 | Loyiha o‘zgarishlarini saqlash, kuzatish va boshqarish jarayonlarini biladi; | ⬜ |
| 25 | 9 | .gitignore faylini Android loyihasi uchun to‘g‘ri sozlashni o‘rganadi; | ⬜ |
| 26 | 9 | Tarmoqlar (branch) yaratish, birlashtirish va versiyalarni boshqarish ko‘nikmasiga ega bo‘ladi; | ⬜ |
| 27 | 9 | GitHub, GitLab kabi platformalar bilan sinxron ishlashni biladi; | ⬜ |
| 28 | 10 | GitHub platformasining maqsadi va imkoniyatlarini tushunadi; | ⬜ |
| 29 | 10 | Yangi repozitoriya (repository) yaratish va uni lokal loyiha bilan bog‘lashni biladi; | ⬜ |
| 30 | 10 | Collaborator qo‘shish, kod sharhlash (pull request) va muhokama (issue) jarayonlarini amaliy bajaradi; | ⬜ |
| 31 | 11 | GitHub Actions orqali avtomatik build va testlarni sozlash haqida tushuncha hosil qiladi; | ⬜ |
| 32 | 11 | Jamoaviy loyihalarda kodni saqlash, baham ko‘rish va boshqarish bo‘yicha mustaqil ishlay oladi | ⬜ |
| 33 | 11 | GitLab va Bitbucket platformalarining vazifasi va GitHub’dan farqini tushunadi; | ⬜ |
| 34 | 12 | Branch va merge jarayonlarini jamoaviy muhitda to‘g‘ri tashkil etish ko‘nikmasiga ega bo‘ladi; | ⬜ |
| 35 | 12 | Merge Request, Issue Tracker va Pipeline funksiyalarining ishlash tamoyillarini o‘rganadi; | ⬜ |
| 36 | 12 | Continuous Integration (CI) va Continuous Deployment (CD) jarayonlarini sozlash haqida tushuncha hosil qiladi; | ⬜ |
| 37 | 13 | Branch (tarmoq) tushunchasini va uning loyihalarda rolini tushunadi; | ⬜ |
| 38 | 13 | Yangi branch yaratish, unga o‘tish va o‘zgarishlarni mustaqil tarzda sinovdan o‘tkazishni biladi; | ⬜ |
| 39 | 13 | Asosiy tarmoqqa (main/master) o‘zgartirishlarni birlashtirish (merge) jarayonini bajaradi; | ⬜ |
| 40 | 14 | Merge vaqtida kelib chiqadigan konfliktlarni aniqlash va hal etish ko‘nikmasiga ega bo‘ladi; | ⬜ |
| 41 | 14 | Kod sharhlari (code review) va tasdiqlash (approve) mexanizmlaridan foydalanishni o‘rganadi; | ⬜ |
| 42 | 14 | CI/CD ning dastur ishlab chiqish jarayonini avtomatlashtirishdagi ahamiyatini biladi; | ⬜ |
| 43 | 15 | .yaml konfiguratsiya fayllarining tuzilishi va bosqichlarini (build, test, deploy) tushunadi; | ⬜ |
| 44 | 15 | CD bosqichida ilovani avtomatik tarzda Play Market yoki serverga joylashtirish jarayonini tushunadi; | ⬜ |
| 45 | 15 | CI jarayonida xatoliklarni aniqlash, test natijalarini tahlil qilish va avtomatik tuzatish mexanizmlarini biladi; | ⬜ |
| 46 | 16 | MVVM arxitekturasining maqsadi va uning afzalliklarini tushunadi; | ⬜ |
| 47 | 16 | Model, View va ViewModel qatlamlarining vazifalari va o‘zaro aloqasini biladi; | ⬜ |
| 48 | 16 | Data Binding va LiveData yordamida UI va ma’lumotlar o‘rtasidagi sinxronlashuvni o‘rganadi; | ⬜ |
| 49 | 17 | Jetpack komponentlari (ViewModel, LiveData, Repository) bilan ishlashni amaliyotda qo‘llay oladi; | ⬜ |
| 50 | 17 | MVVM yordamida kodni modulli, testlanadigan va oson kengaytiriladigan shaklda yozishni biladi; | ⬜ |
| 51 | 17 | MVI arxitektura naqshining mohiyatini va uni MVVM dan farqlovchi jihatlarni tushunadi; | ⬜ |
| 52 | 18 | Model, View va Intent qatlamlarining vazifalari va o‘zaro ishlash tamoyillarini biladi; | ⬜ |
| 53 | 18 | UI holatini (state) yagona oqim sifatida boshqarish tamoyillarini o‘rganadi; | ⬜ |
| 54 | 18 | Intents orqali foydalanuvchi harakatlarini kuzatish va ularni ViewModel yoki Reducer orqali qayta ishlashni biladi; | ⬜ |
| 55 | 19 | MVI yordamida barqaror va testlanadigan foydalanuvchi interfeysini qurishni o‘rganadi; | ⬜ |
| 56 | 19 | MVP arxitektura naqshining mohiyatini va uni MVVM hamda MVI dan farqini tushunadi; | ⬜ |
| 57 | 19 | Model, View va Presenter qismlarining vazifalari hamda o‘zaro aloqasini biladi; | ⬜ |
| 58 | 20 | Presenter orqali foydalanuvchi harakatlarini boshqarish va View bilan ma’lumot almashishni o‘rganadi; | ⬜ |
| 59 | 20 | Ma’lumotlarni Model qatlamida saqlash va yangilash jarayonlarini amalda qo‘llay oladi; | ⬜ |
| 60 | 20 | Kichik Android loyihalarida MVP arxitekturasini to‘g‘ri qo‘llay oladi | ⬜ |
| 61 | 21 | ViewModel va LiveData komponentlarining maqsadi va afzalliklarini tushunadi; | ⬜ |
| 62 | 21 | LiveData yordamida ma’lumotlar o‘zgarishini real vaqt rejimida kuzatish ko‘nikmasiga ega bo‘ladi; | ⬜ |
| 63 | 21 | ViewModel va LiveData ni birgalikda qo‘llab, UI va ma’lumotlar sinxronlashuvini ta’minlay oladi; | ⬜ |
| 64 | 22 | MVVM arxitekturasida ViewModel va LiveData’ni to‘g‘ri joylashtirish hamda amaliy loyihalarda tatbiq etish ko‘nikmasiga ega bo‘ladi | ⬜ |
| 65 | 22 | StateFlow va SharedFlow oqimlarining farqi va ularning ishlash tamoyillarini biladi; | ⬜ |
| 66 | 22 | CoroutineScope doirasida Flow oqimlarini boshqarish va bekor qilish (cancel) ko‘nikmasiga ega bo‘ladi; | ⬜ |
| 67 | 23 | SharedFlow orqali bir nechta kuzatuvchilarga (collectors) ma’lumot uzatish jarayonini tushunadi; | ⬜ |
| 68 | 23 | emit, collect, replay, subscription kabi asosiy funksiyalarni amalda qo‘llay oladi; | ⬜ |
| 69 | 23 | Repository pattern’ning maqsadi va uni MVVM arxitekturadagi o‘rni haqida tushuncha hosil qiladi; | ⬜ |
| 70 | 24 | DataSource tushunchasini va ma’lumot oqimining (data flow) yo‘nalishini o‘rganadi; | ⬜ |
| 71 | 24 | Remote (masofaviy) va Local (mahalliy) manbalar o‘rtasida sinxronlash jarayonini tushunadi; | ⬜ |
| 72 | 24 | Repository qatlamida xatoliklarni (Exception Handling) to‘g‘ri boshqarish ko‘nikmasiga ega bo‘ladi; | ⬜ |
| 73 | 25 | Barqaror, kengaytiriladigan va testlanadigan ma’lumot oqimini loyihalashni o‘rganadi | ⬜ |
| 74 | 25 | Dastur komponentlari orasidagi bog‘liqlikni kamaytirish va modullilikni oshirishning ahamiyatini biladi; | ⬜ |
| 75 | 25 | Dagger va Hilt kutubxonalarining ishlash tamoyillari va ularning farqlarini o‘rganadi; | ⬜ |
| 76 | 26 | @Inject, @Module, @Provides, @Singleton annotatsiyalarining vazifasini biladi; | ⬜ |
| 77 | 26 | Arxitekturaning asosiy qatlamlari - Presentation, Domain va Data qismlarining vazifalarini biladi; | ⬜ |
| 78 | 26 | Har bir qatlamning o‘zaro mustaqilligi va bog‘lanish chegaralarini (boundaries) o‘rganadi; | ⬜ |
| 79 | 27 | Use Case (Interactor) orqali biznes mantiqni alohida boshqarish usulini biladi; | ⬜ |
| 80 | 27 | Repository va Entity’lar orqali ma’lumot oqimini qatlamlar orasida to‘g‘ri tashkil eta oladi; | ⬜ |
| 81 | 27 | MVVM arxitekturasi asosida ilova modullarini tuzish jarayonini amalda bajaradi; | ⬜ |
| 82 | 28 | ViewModel va LiveData orqali foydalanuvchi ma’lumotlarini boshqarish va saqlashni biladi; | ⬜ |
| 83 | 28 | RecyclerView yordamida moliyaviy ma’lumotlarni ro‘yxat ko‘rinishida chiqarish ko‘nikmasiga ega bo‘ladi; | ⬜ |
| 84 | 28 | Room ma’lumotlar bazasidan foydalanib, kiritilgan xarajat va daromadlarni saqlashni o‘rganadi; | ⬜ |
| 85 | 29 | Data Binding orqali interfeys va ma’lumotlar o‘rtasida avtomatik bog‘lanish yaratadi; | ⬜ |
| 86 | 29 | SQLite ma’lumotlar bazasining tuzilmasi va ishlash prinsipi haqida tushunchaga ega bo‘ladi; | ⬜ |
| 87 | 29 | Jadval (table) yaratish va maydonlarga ma’lumot kiritish (INSERT) amallarini bajaradi; | ⬜ |
| 88 | 30 | SQL buyruqlari yordamida ma’lumotlarni yangilash (UPDATE) va o‘chirish (DELETE)ni bajaradi; | ⬜ |
| 89 | 30 | SELECT operatori orqali kerakli yozuvlarni saralab olishni o‘rganadi; | ⬜ |
| 90 | 30 | Smart Finance ilovasida xarajatlar ro‘yxatini saqlash uchun SQLite bazasini qo‘llaydi | ⬜ |
| 91 | 31 | Room kutubxonasining asosiy komponentlari (Entity, DAO, Database) bilan ishlashni biladi; | ⬜ |
| 92 | 31 | ORM texnologiyasining SQL kodlarini soddalashtirishdagi afzalliklarini tushunadi; | ⬜ |
| 93 | 31 | Room orqali CRUD (Create, Read, Update, Delete) amallarini bajarishni o‘rganadi; | ⬜ |
| 94 | 32 | LiveData va ViewModel orqali ma’lumotlarning real vaqt yangilanishini kuzatadi; | ⬜ |
| 95 | 32 | Smart Finance ilovasida foydalanuvchi ma’lumotlarini Room orqali saqlaydi va o‘qiydi | ⬜ |
| 96 | 32 | Realm ma’lumotlar bazasining tuzilishi va afzalliklarini biladi; | ⬜ |
| 97 | 33 | Realm orqali offline va online sinxronizatsiyani tashkil etish usullarini o‘rganadi; | ⬜ |
| 98 | 33 | Model sinflarini yaratish va ulardan ma’lumot olish jarayonini tushunadi; | ⬜ |
| 99 | 33 | Ma’lumot o‘zgarishlarini real vaqt rejimida kuzatish uchun Listener mexanizmini qo‘llaydi; | ⬜ |
| 100 | 34 | Smart Finance ilovasida foydalanuvchi tranzaksiyalarini real vaqt rejimida sinxronlashtiradi | ⬜ |
| 101 | 34 | Firestore bazasining “collection” va “document” tuzilmasini tushunadi; | ⬜ |
| 102 | 34 | CRUD amallarini (create, read, update, delete) Firestore orqali bajaradi; | ⬜ |

## III-BOB. Ma’lumotlar bazalari va sinxronlash tizimlari

| Dars | Hafta | Mavzu | Holat |
|---|---|---|---|

## IV-BOB. Tarmoq va API integratsiyasi

| Dars | Hafta | Mavzu | Holat |
|---|---|---|---|

## VI-BOB. Firebase xizmatlari va ilova integratsiyasi

| Dars | Hafta | Mavzu | Holat |
|---|---|---|---|

## VII-BOB. Testlash, tarqatish va yakuniy loyiha

| Dars | Hafta | Mavzu | Holat |
|---|---|---|---|
