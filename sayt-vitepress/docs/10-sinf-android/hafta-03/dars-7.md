---
title: "13-dars. 7-dars: Git bilan versiya nazorati asoslari"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (Android)", "link": "/10-sinf-android/"}, "week": {"n": 3, "link": "/10-sinf-android/hafta-03/"}, "g": 13, "title": "7-dars: Git bilan versiya nazorati asoslari", "lead": "build.gradle faylining asosiy tuzilmasi va modullararo bog‘lanishi", "slide": "/slaydlar/10-sinf-android/hafta-03/dars-7.html", "test": "/slaydlar/10-sinf-android/hafta-03/dars-7-test.html", "tabs": [{"g": 13, "link": "/10-sinf-android/hafta-03/dars-7", "current": true}, {"g": 14, "link": "/10-sinf-android/hafta-03/dars-8", "current": false}, {"g": 15, "link": "/10-sinf-android/hafta-03/dars-9", "current": false}], "prev": null, "next": {"g": 14, "title": "8-dars: Git bilan ishlash amaliyoti (Tarmoqlar va Konfliktlar)", "link": "/10-sinf-android/hafta-03/dars-8"}}
---

**Fan:** Advanced Android dasturlash  
**Sinf:** 10-sinf  
**Mavzu:** Git bilan versiya nazorati asoslari (Git vazifasi, sozlash, git init, 3 holat, commit, Android uchun .gitignore)

---

<div class="blk">

## <Icon name="file-text" /> Nazariy konspekt

### 1. Git nima va u nega dasturchining vaqt mashinasi?
Git — bu loyihadagi har bir fayl va satr darajasidagi o'zgarishlarni vaqt bo'yicha qayd etib boruvchi **Tarqoq Versiya Nazorati Tizimi (DVCS)**dir.
- **Xatolardan qo'rqmaslik:** Yangi kod yozib ilovani buzib qo'ysangiz ham, istalgan paytda avvalgi ishchi holatga qaytish mumkin.
- **Tarix va mualliflik:** Har bir kod qatori kim tomonidan, qachon va nima maqsadda yozilgani saqlanadi.
- **Offline ishlash:** Internet bo'lmaganda ham kompyuteringizda butun loyiha tarixi mavjud bo'ladi.

---

### 2. Gitni birlamchi sozlash
Git o'rnatilgandan so'ng, tizimga o'zingizni tanitishingiz kerak:
```bash
git config --global user.name "Ismingiz Familiyangiz"
git config --global user.email "sizning_pochtangiz@example.com"
```
Sozlamalarni tekshirish:
```bash
git config --list
```

---

### 3. Gitning 3 holati (Three States)
Gitda fayllar 3 bosqichdan o'tadi:
1. **Working Directory (Ishchi maydon):** Kompyuteringizdagi real papka. Siz kod yozayotgan joy.
2. **Staging Area (Tayyorlash sahnasi):** Keyingi commit uchun belgilangan o'zgarishlar.
3. **Repository (Ombor):** Barcha commitlar va loyiha tarixi saqlanadigan `.git` ma'lumotlar bazasi.

```text
[Working Directory] -- git add --> [Staging Area] -- git commit --> [Repository (.git)]
```

---

### 4. Asosiy terminal buyruqlari

| Buyruq | Vazifasi |
|---|---|
| `git init` | Joriy papkada yangi bo'sh Git repozitoriyasini ochadi (`.git` papkasi) |
| `git status` | Qaysi fayllar o'zgargani, sahnaga chiqqani yoki kuzatilmayotganini ko'rsatadi |
| `git add <fayl>` | Faylni sahnaga (Staging Area) chiqaradi (`git add .` barchasini qo'shadi) |
| `git commit -m "izoh"` | Sahnadagi o'zgarishlarni ma'noli izoh bilan tarixga muhrlaydi |
| `git log` | Commitlar tarixini to'liq ko'rsatadi |
| `git log --oneline` | Tarixni ixcham bir qatorda ko'rsatadi |

---

### 5. Android loyihalari uchun `.gitignore`
Android Studio loyihalarida avtomatik hosil bo'ladigan og'ir va shaxsiy fayllarni Gitga yuklash mumkin emas:
- `build/` va `app/build/` — vaqtinchalik kompilyatsiya fayllari;
- `.gradle/` — Gradle kesh fayllari;
- `local.properties` — dasturchining shaxsiy SDK yo'li;
- `*.apk`, `*.aab` — yig'ilgan og'ir ilova fayllari.

Bularning barchasi loyihaning boshidagi `.gitignore` fayliga kiritiladi.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy topshiriqlar

### 1-topshiriq: Git versiyasini aniqlash <Badge type="tip" text="oson" />
Terminalda `git --version` buyrug'ini ishga tushiring va kompyuteringizda o'rnatilgan Git versiyasini aniqlang.

### 2-topshiriq: Global sozlamalarni kiritish <Badge type="tip" text="oson" />
`git config --global` orqali ismingiz va elektron pochtangizni kiriting hamda `git config --list` orqali ularni tekshiring.

### 3-topshiriq: Birinchi repozitoriy yaratish <Badge type="tip" text="oson" />
Terminalda yangi `git-amaliyot` papkasini oching, unga kiring va `git init` buyrug'i orqali repozitoriy hosil qiling.

### 4-topshiriq: Fayl yaratish va statusni tahlil qilish <Badge type="tip" text="oson" />
Papkada `test.txt` faylini yarating. `git status` buyrug'ini bering va nima sababdan fayl qizil rangda chiqayotganini tushuntiring.

### 5-topshiriq: Faylni sahnaga qo'shish va birinchi commit <Badge type="warning" text="o'rta" />
`git add test.txt` orqali faylni sahnaga olib chiqing va `git commit -m "docs: birinchi sinov fayli yaratildi"` orqali tarixga yozing.

### 6-topshiriq: Ikkinchi commit va tarixni o'qish <Badge type="warning" text="o'rta" />
`test.txt` fayliga yangi qator yozing, o'zgarishlarni commit qiling va `git log --oneline` buyrug'i orqali ikkala commit xeshini daftaringizga qayd eting.

### 7-topshiriq: Android Studio loyihasi .gitignore faylini o'rganish <Badge type="warning" text="o'rta" />
Mavjud Android Studio loyihangizni oching va uning `.gitignore` faylini tahlil qiling. Unda `local.properties` va `build` papkalari yozilganiga ishonch hosil qiling.

### 8-topshiriq: .gitignore yaratish va sinash <Badge type="danger" text="qiyin" />
`git-amaliyot` papkangizda `.gitignore` faylini oching va unga `*.log` qatorini yozing. So'ng `server.log` faylini yarating va `git status` uni ko'rsatmasligiga ishonch hosil qiling.

### 9-topshiriq: Sahnaga tanlab qo'shish <Badge type="danger" text="qiyin" />
Papkada bir vaqtda 3 ta turli fayl yarating. `git add` yordamida faqat ikkitasini sahnaga olib chiqing, birinchisini esa Working Directory'da qoldirib, qisman commit qiling.

### 10-topshiriq: .git papkasi tuzilmasini o'rganish <Badge type="info" text="bonus" />
Terminalda `ls -la` (yoki Windowsda `dir /ah`) buyrug'ini bering. `.git` yashirin papkasi ichiga kiring va uning ichidagi `HEAD`, `config`, `objects` elementlarini ko'zdan kechiring.

---

</div>

<div class="blk">

## <Icon name="file-text" /> O'zini tekshirish uchun savollar

1. Nima uchun loyihalarni `proyekt_1`, `proyekt_final` qilib nusxalash yomon amaliyot hisoblanadi?
2. Gitning markazlashgan tizimlardan (masalan, SVN) asosiy farqi nimada?
3. Working Directory, Staging Area va Repository maydonlarining farqini ayting.
4. Nima sababdan Android Studio loyihasidagi `local.properties` fayli Gitga qo'shilmaydi?
5. `git log` buyrug'ida ko'rinadigan 40 xonali xesh (SHA-1) nima uchun kerak?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. O'z kompyuteringizda Git global sozlamalarini to'liq tekshiring.
2. Yangi papka ochib, unda kamida 3 ta ketma-ket ma'noli commit qiling (masalan, "feat: asosiy funksiya", "fix: xato tuzatildi", "docs: qo'llanma").
3. `git log --oneline --graph` buyrug'ini ishga tushirib, terminaldagi natijani tahlil qiling.

</div>

