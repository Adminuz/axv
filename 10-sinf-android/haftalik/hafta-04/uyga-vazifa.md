# 4-hafta: Uyga vazifalar to'plami

Mazkur haftada o'tilgan darslar bo'yicha mustaqil bajarish uchun topshiriqlar. Har bir vazifa 20–30 daqiqaga mo'ljallangan.

---

## 10-dars: GitLab va Bitbucket'da jamoaviy ish jarayonlari

1. O'z jamoangiz uchun guruh (Group), 2 ta loyiha va 4 ta a'zo sxemasini tuzing, har bir a'zoga rol yozing.
2. Kanban doskasini (To Do, In Progress, Done) 5 ta vazifa bilan to'ldiring.
3. Android loyihangiz uchun pipeline bosqichlarini ketma-ketlikda yozing (masalan, Commit, Build, Test, Review, Deploy) va test yiqilsa nima bo'lishini tushuntiring.

---

## 11-dars: Branch, Merge va Pull Request jarayonlari

1. Yangi repo yarating. `feature/` bilan boshlanadigan branch oching, unda 2 ta ma'noli commit qiling va `main` ga merge qiling.
2. Bitta faylda sun'iy merge konflikti hosil qiling, uni qo'lda hal qilib, merge'ni yakunlang.
3. Hamkasbingiz kodi uchun 3 ta konstruktiv Code Review sharhi yozing.

---

## 12-dars: Continuous Integration (CI/CD) tushunchasi

1. CI, Continuous Delivery va Continuous Deployment atamalarini o'z so'zingiz bilan yozing.
2. O'z Android loyihangiz uchun "Android CI" nomli GitHub Actions workflow'ini (YAML) yozing: push va PR (main) da ishlasin, JDK 17 o'rnatsin, `./gradlew build` bajarsin.
3. Nega API kalit va tokenlar YAML faylga to'g'ridan-to'g'ri yozilmasligini 3-4 jumlada tushuntiring.

---

## Mentor uchun

### Baholash mezonlari (Jami 100 ball)
- **10-dars vazifasi (30 ball):** jamoa sxemasining mantiqiyligi (rollar vazifaga mos), Kanban doskasi, pipeline bosqichlari.
- **11-dars vazifasi (40 ball):** feature branch ochish, toza merge, konfliktni qo'lda xatosiz hal qilish (belgilar o'chirilgan), sharhlarning konstruktivligi.
- **12-dars vazifasi (30 ball):** CI/CD atamalarini to'g'ri izohlash, YAML tuzilishi (`name`, `on`, `jobs`, `steps`), Secrets haqida to'g'ri xulosa.

### Eslatma
- Konflikt belgilari (`<<<<<<<`, `=======`, `>>>>>>>`) faylda qolmaganini tekshiring.
- YAML'da bo'shliq (indent) xatolariga e'tibor bering.
- Agar o'quvchida GitLab/Bitbucket akkaunti bo'lmasa, 1-vazifa daftarda sxema ko'rinishida qabul qilinadi.
