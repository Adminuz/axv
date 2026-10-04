---
title: "14-dars. 8-dars: Git bilan ishlash amaliyoti (Tarmoqlar va Konfliktlar)"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (Android)", "link": "/10-sinf-android/"}, "week": {"n": 3, "link": "/10-sinf-android/hafta-03/"}, "g": 14, "title": "8-dars: Git bilan ishlash amaliyoti (Tarmoqlar va Konfliktlar)", "lead": ">>>>>> feature-api", "slide": "/slaydlar/10-sinf-android/hafta-03/dars-8.html", "tabs": [{"g": 13, "link": "/10-sinf-android/hafta-03/dars-7", "current": false}, {"g": 14, "link": "/10-sinf-android/hafta-03/dars-8", "current": true}, {"g": 15, "link": "/10-sinf-android/hafta-03/dars-9", "current": false}], "prev": {"g": 13, "title": "7-dars: Git bilan versiya nazorati asoslari", "link": "/10-sinf-android/hafta-03/dars-7"}, "next": {"g": 15, "title": "9-dars: GitHub’da loyihalar yaratish va boshqarish", "link": "/10-sinf-android/hafta-03/dars-9"}}
---

**Fan:** Advanced Android dasturlash  
**Sinf:** 10-sinf  
**Mavzu:** Git bilan ishlash amaliyoti (diff, branch, checkout/switch, merge, to'qnashuvlarni hal qilish, reset, stash)

---

<div class="blk">

## <Icon name="file-text" /> Nazariy konspekt

### 1. Tarmoqlar (Branches) falsafasi
Tarmoq — bu asosiy loyihadan (`main`) ajralib chiquvchi parallel ish maydoni.
- Yangi funksiya (`feature-login`, `feature-payment`) yoki xato tuzatish (`fix-crash`) har doim alohida branch'da yoziladi.
- Asosiy `main` tarmog'i doimo barqaror va ishchi holatda qoladi.
- Tajriba muvaffaqiyatli o'tgach, branch `main` ga birlashtiriladi (**Merge**).

---

### 2. Asosiy buyruqlar

| Buyruq | Tavsif |
|---|---|
| `git branch` | Barcha mavjud branchlar ro'yxatini ko'rsatadi |
| `git switch -c <nom>` | Yangi branch yaratadi va unga darhol o'tadi (`git checkout -b` analogi) |
| `git switch <nom>` | Ko'rsatilgan branchga o'tadi |
| `git branch -d <nom>` | Ishlatib bo'lingan branchni o'chiradi |
| `git diff` | Saqlanmagan o'zgarishlarni satrma-satr solishtiradi |
| `git merge <branch>` | Berilgan branchni joriy branchga birlashtiradi |
| `git stash` | Chala o'zgarishlarni vaqtinchalik yashirib turadi |
| `git stash pop` | Yashirilgan o'zgarishlarni qaytaradi |
| `git revert <hash>` | Xato commitni yangi teskari commit bilan bekor qiladi |

---

### 3. Merge Conflict (To'qnashuv) nima va uni qanday yechish kerak?
Agar ikki kishi yoki ikkita branch bitta faylning ayni bir satrini tahrirlagan bo'lsa, Git to'xtaydi va faylga belgi qo'yadi:

```text
<<<<<<< HEAD
val API_URL = "https://server1.uz/api"
=======
val API_URL = "https://server2.uz/api"
```

**Hal qilish algoritmi:**
1. Faylni ochib, kerakli to'g'ri satrni qoldiring.
2. `<<<<<<< HEAD`, `=======`, `>>>>>>>` belgilarini butunlay o'chirib tashlang.
3. Faylni saqlang, `git add <fayl>` va `git commit -m "merge: konflikt hal qilindi"` buyruqlarini bering.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy topshiriqlar

### 1-topshiriq: Yangi branch yaratish <Badge type="tip" text="oson" />
Terminalda `git switch -c feature-cart` buyrug'i orqali yangi tarmoq oching va `git branch` orqali faol tarmoq nomini tekshiring.

### 2-topshiriq: Tarmoqda fayl yaratish <Badge type="tip" text="oson" />
`feature-cart` tarmog'ida `CartItem.kt` faylini yarating va uni ma'noli commit bilan omborga yozing.

### 3-topshiriq: Asosiy tarmoqqa qaytish <Badge type="tip" text="oson" />
`git switch main` buyrug'i orqali asosiy tarmoqqa o'ting va `ls` orqali `CartItem.kt` fayli ko'rinmayotganiga ishonch hosil qiling.

### 4-topshiriq: O'zgarishlarni taqqoslash (diff) <Badge type="warning" text="o'rta" />
Mavjud faylga yangi satr yozing (commit qilmasdan) va `git diff` buyrug'i orqali qo'shilgan qator qanday rangda va qaysi belgi bilan chiqqanini tahlil qiling.

### 5-topshiriq: Muvaffaqiyatli Merge bajarish <Badge type="warning" text="o'rta" />
`main` tarmog'ida turib, `git merge feature-cart` buyrug'ini ishga tushiring va `CartItem.kt` endi `main` ga ham qo'shilganini tasdiqlang.

### 6-topshiriq: Eski branchni tozalash <Badge type="warning" text="o'rta" />
Birlashtirib bo'lingan `feature-cart` tarmog'ini `git branch -d feature-cart` buyrug'i orqali o'chirib tashlang.

### 7-topshiriq: Sun'iy to'qnashuv (Conflict) hosil qilish <Badge type="danger" text="qiyin" />
`main` va `feature-theme` tarmoqlarida bitta faylning ayni bir satrini turlicha o'zgartiring va ularni birlashtirishga urinib ko'ring.

### 8-topshiriq: To'qnashuv belgilarini tozalash va commit <Badge type="danger" text="qiyin" />
Chiqgan konfliktli faylni oching, `<<<<<<<` va `>>>>>>>` belgilarini o'chirib, to'g'ri variantni qoldiring va merge jarayonini muvaffaqiyatli yakunlang.

### 9-topshiriq: git stash mexanizmini sinash <Badge type="danger" text="qiyin" />
Faylga chala kod yozing, `git stash` qilib yashiring. `git status` toza ekanini ko'ring, so'ng `git stash pop` qilib kodingizni qaytarib oling.

### 10-topshiriq: git revert orqali xato commitni bekor qilish <Badge type="info" text="bonus" />
Oxirgi qilgan testingizdagi xato commit xeshini `git log --oneline` orqali toping va `git revert <hash>` orqali yangi bekor qiluvchi commit hosil qiling.

---

</div>

<div class="blk">

## <Icon name="file-text" /> O'zini tekshirish uchun savollar

1. Nima uchun barcha yangi funksiyalarni `main` da emas, alohida branch'da qilish tavsiya etiladi?
2. `git switch -c` va `git switch` buyruqlarining farqi nimada?
3. Merge Conflict yuz berganda Git qanday belgilarni kod ichiga kiritadi?
4. `git diff` buyrug'ida yashil `+` va qizil `-` nimani ifodalaydi?
5. `git stash` nima maqsadda ishlatiladi va `git stash pop` nima qiladi?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. Loyihangizda `feature-login` nomli yangi branch oching va `LoginScreen.kt` faylini yaratib commit qiling.
2. `main` ga qaytib, `feature-login` tarmog'ini birlashtiring.
3. Uyda mustaqil tarzda bitta fayl bo'yicha sun'iy merge conflict hosil qiling va uni qo'lda bartaraf etib, `git log` dagi birlashtiruvchi commitni ko'ring.

</div>

