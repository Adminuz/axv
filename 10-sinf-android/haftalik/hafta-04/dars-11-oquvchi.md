# 11-dars. Branch, Merge va Pull Request jarayonlari

> Katta jamoalar bitta ilova ustida bir vaqtda ishlaydi va bir-birini buzmaydi. Buning kaliti: branch, merge va Pull Request.

## Dars xulosasi

- Branch: loyihaning mustaqil shoxchasi, asosiy kodga zarar bermaydi.
- `git checkout -b nom` branch yaratadi va unga o'tadi.
- Branch commitga ishora qiluvchi yengil ko'rsatkich (pointer).
- Merge ikki branchni bitta tarixga birlashtiradi.
- Bir xil satr ikki xil o'zgarsa, merge konflikti chiqadi va qo'lda hal qilinadi.
- Pull Request: o'zgarishni asosiy branchga qo'shish uchun rasmiy so'rov.
- Code Review: jamoa kodni satrma-satr tekshiradi, keyin merge qilinadi.
- Branch nomi maqsadni bildiradi: `feature/`, `bugfix/`, `hotfix/`, `refactor/`.

## Qo'shimcha ma'lumot

### Nega branch yengil?

Branch kopiya emas. U zanjirdagi bitta commitga qaratilgan "o'q". Yangi commit qilsangiz, o'q yangi commitga suriladi. Shuning uchun yuzlab branch ham diskni to'ldirmaydi.

### Konflikt belgilarini o'qish

```text
<<<<<<< HEAD
fun loadUser() { ... }
=======
fun loadUserData() { ... }
>>>>>>> login-feature
```

`=======` dan yuqori qism sizning joriy branchingiz, pastki qism qo'shilayotgan branch. Uchta ish: variantni tanlang (yoki birlashtiring), Git belgilarini o'chiring, `git add` va `git commit` qiling.

### Merge usullari

Dasturda fast-forward va squash nomlari bor. Fast-forward: pointer oldinga suriladi. Squash: bir nechta commit bittaga aylanadi. Rebase esa branchni asosiy branch ustiga qaytadan qo'yadi va tarixni silliq qiladi, lekin noto'g'ri ishlatilsa xatolarga olib keladi.

### PR nega kerak?

Do'stingizga uy vazifangizni topshirishdan oldin ko'rsatasiz: xatoni u ko'radi. PR ham shunday: kod asosiy loyihaga tushmasdan oldin boshqalar ko'zi bilan tekshiriladi.

### Odatiy xatolar

- To'g'ridan-to'g'ri `main` ga yozish.
- Konflikt belgilarini o'chirmay commit qilish.
- Juda katta PR ochish.
- Ma'nosiz commit xabari.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Branch | Loyihaning mustaqil shoxchasi |
| Pointer | Branch ishora qiladigan commit ko'rsatkichi |
| Merge | Ikki branchni bitta tarixga birlashtirish |
| Conflict | Bir xil satr ikki xil o'zgarganda yuzaga keladigan to'qnashuv |
| Feature Branch | Yangi funksiya uchun alohida branch |
| Pull Request | O'zgarishni qo'shish uchun rasmiy so'rov |
| Code Review | Jamoaning kodni tekshirishi |
| Rebase | Branchni asosiy branch ustiga qayta qo'yish |
| Git Flow | main, develop, feature, release, hotfix branchlariga asoslangan strategiya |
| Workflow | Jamoaning ishlash tartibi |

## Bilasizmi?

- Dasturchilar bir necha o'n yil avval bir xil fayl ustida navbat bilan ishlagan, bugun yuzlab dasturchi bitta kod ustida parallel ishlaydi.
- Androidning Retrofit, Coil, Ktor kabi mashhur kutubxonalari GitHub'da shu usul bilan boshqariladi.
- Katta kompaniyalarda PR orqali kodni tasdiqlash majburiy bosqich.
- Konflikt xato emas: har bir dasturchi uni muntazam hal qiladi.

## Topshiriqlar

### 1. Branch nima? · oson
Branchni o'z so'zingiz bilan bir jumlada izohlang.

**Kutiladigan natija:** "mustaqil shoxcha" ma'nosi bor jumla.

### 2. Buyruqni tanlang · oson
Yangi branch ochib, unga o'tadigan buyruqni yozing: `login-feature` nomi bilan.

**Kutiladigan natija:** `git checkout -b login-feature`.

### 3. Branch nomi · oson
"Pul o'tkazish xatosini zudlik bilan tuzatish" uchun branch nomini yozing.

**Kutiladigan natija:** `hotfix/payment-error` kabi nom.

### 4. PR so'zi · oson
PR qisqartmasi nimani anglatadi va GitLab'da u qanday ataladi?

**Kutiladigan natija:** Pull Request; GitLab'da Merge Request.

### 5. Branch ichida ishlash · o'rta
Bo'sh papkada repo yarating, `feature/login` branchida fayl yaratib commit qiling va `main` ga qaytib fayl yo'qligiga ishonch hosil qiling.

**Kutiladigan natija:** main'da fayl ko'rinmaydi.

### 6. Merge qiling · o'rta
5-topshiriqdagi branchni `main` ga merge qiling va `git log --oneline` natijasini tushuntiring.

**Kutiladigan natija:** fayl main'da paydo bo'ladi, tarixda commitlar ko'rinadi.

### 7. Bu nima? · o'rta
Quyidagi kod bo'lagi nima ekanini va qaysi qism qaysi branchniki ekanini tushuntiring:
```text
<<<<<<< HEAD
val title = "Salom"
=======
val title = "Xush kelibsiz"
>>>>>>> feature/home
```

**Kutiladigan natija:** bu merge konflikti; yuqorisi joriy branch (HEAD), pastki feature/home.

### 8. Review mezonlari · o'rta
Code Review'da tekshiriladigan 5 narsani sanang.

**Kutiladigan natija:** toza kod, takrorlanish yo'qligi, xavfsizlik, arxitektura, UI natijasi.

### 9. Konfliktni hal qiling · qiyin
`HomeScreen.kt` faylida ikki branchda bir xil satrni turlicha o'zgartiring, merge qiling va konfliktni qo'lda hal qiling.

**Kutiladigan natija:** belgilarsiz fayl, `git commit` bilan yakunlangan merge.

### 10. Xatoni toping · qiyin
Hamkasbingiz konflikt belgilarini o'chirmay fayl commit qildi. Nima bo'ladi va qanday tuzatasiz?

**Kutiladigan natija:** kodda belgilar qolib, kompilyatsiya xatosi chiqadi; faylni ochib belgilarni olib tashlash va yangi commit qilish.

### 11. PR tavsifi · qiyin
"Lessons screen" funksiyasi uchun PR sarlavhasi va 2-3 jumlalik tavsif yozing.

**Kutiladigan natija:** nima o'zgardi va nima uchun, aniq tilda.

### 12. Branch qoidalari · bonus
O'z jamoangiz uchun branch nomlash va PR qoidalarini 1 sahifada yozing.

**Kutiladigan natija:** nomlash namunalari, PR hajmi, review tartibi.

## O'zingizni tekshiring

1. Nega to'g'ridan-to'g'ri `main` ga yozmaymiz?
2. Branch pointer ekani nimani anglatadi?
3. Merge qanday ishlaydi va konflikt qachon chiqadi?
4. Konflikt belgilaridan qaysi biri qaysi branchga tegishli?
5. Pull Request qanday jarayon?
6. Code Review nimani tekshiradi?
7. Git Flow'da qaysi branch turlari bor?

## Uyga vazifa

1. `feature/` nomli branch oching, 2 ta commit qiling va `main` ga merge qiling.
2. Sun'iy konflikt hosil qilib, qo'lda hal qiling.
