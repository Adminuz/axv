# 11-dars. Branch, Merge va Pull Request jarayonlari

**Fan:** Advanced Android dasturlash
**Sinf:** 10-sinf
**Hafta:** 4-hafta, 2-dars (umumiy 11-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** `oquv-qollanma.txt` (Branch, Merge va Pull Request jarayonlari ma'ruzasi), `oquv-dasturi.txt` (kutilayotgan natijalar)

---

## Darsning maqsadi

Branch tushunchasi va uning rolini, feature branch modelini, merge jarayonini va uning usullarini (fast-forward, squash, rebase tushunchasi), merge konfliktlarini aniqlash va hal etishni, Pull Request yaratish va Code Review bosqichlarini o'rgatish.

## Kutilayotgan natijalar

- Branchning maqsadini ("asosiy loyihaga zarar bermaslik") va pointer modelini tushuntiradi;
- `git checkout -b`, `git merge` buyruqlarini qo'llaydi;
- Konflikt belgilarini (`<<<<<<< HEAD`, `=======`, `>>>>>>>`) o'qiydi va hal qiladi;
- Pull Request jarayonini va Code Review mezonlarini aytadi;
- Branch nomlash standartini va branch strategiyalarini (Git Flow, GitHub Flow, Trunk Based) biladi.

## Jihozlar

Kompyuter, Git, Android Studio yoki terminal, bo'sh test papka.

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| 00–08 | Takrorlash | 10-dars: platformalar, MR, rollar, pipeline |
| 08–22 | Branch | Daraxt analogiyasi, pointer modeli, `checkout -b`, nomlash |
| 22–38 | Merge | Merge jarayoni, usullar, konflikt belgilari, hal qilish |
| 38–43 | Tanaffus | |
| 43–55 | Pull Request | PR jarayoni, feature branch ssenariysi, Code Review, strategiyalar |
| 55–75 | Amaliyot | Branch, merge, sun'iy konflikt |
| 75–80 | Xulosa | Nazorat, uyga vazifa, anons |

---

## Konspekt

### 1. Branch

Branch: loyihaning mustaqil shoxchasi. Daraxt tanasi asosiy loyiha, shoxlar funksiyalar, xato tuzatish va tajriba ishlari. Har bir shox mustaqil rivojlanadi, o'zgarish asosiy loyihaga tegmaydi. To'g'ridan-to'g'ri `main` ga yozilsa, kichik xato butun loyihani ishdan chiqarishi mumkin.

```bash
git checkout -b login-feature
```

Yangi branch yaratadi va unga o'tadi. Asosiy ustunlik: xavfsizlik va mustaqillik.

Nomlash standarti: `feature/login`, `bugfix/profile-crash`, `hotfix/payment-error`, `refactor/home-screen`.

**Ichki mexanizm.** Branch aslida pointer (ko'rsatkich): qaysi commitga ishora qilayotganini bildiradi. Commitlar zanjir:

```
A → B → C → D   (main)
        \
         E → F  (feature/ui)
```

E va F main'ga tegmaydi. Yangi commit bo'lsa, branch pointeri o'sha commitga o'tadi. Shu yengil model tufayli branch tez ishlaydi va diskda ortiqcha joy egallamaydi.

### 2. Merge

Merge: ikki branchni bitta umumiy tarixga birlashtirish. Git ikki branchdagi commitlarni solishtiradi, farqlarni tahlil qiladi va yagona kodga birlashtiradi. Mustaqil o'zgarishlar avtomatik qo'shiladi.

```bash
git checkout main
git merge login-feature
```

**Usullar** (dastur: fast-forward, squash; hujjatda rebase ham bor):
- fast-forward: main shoxdan keyin o'zgarmagan bo'lsa pointer oldinga suriladi;
- squash: bir nechta commit bittaga birlashtiriladi;
- rebase: merge ikki branchni parallel saqlaydi, rebase esa branchni asosiy branch ustiga qaytadan "yopishtiradi", tarix silliq bo'ladi. Noto'g'ri ishlatilsa xato bo'ladi; jamoalarda odatda merge oldidan branchni yangilash uchun ishlatiladi.

> Aniqlik: hujjat fast-forward va squash'ni faqat nomi bilan keltiradi (tavsifi umumiy bilim). Rebase tavsifi hujjatda bor.

**Konflikt.** Bir faylning bir xil satri ikki branchda turlicha o'zgarsa, Git qaysi versiya to'g'riligini bilmaydi:

```
<<<<<<< HEAD
fun loadUser() { ... }
=======
fun loadUserData() { ... }
>>>>>>> login-feature
```

Yuqori qism main'dagi kod, pastki qism login-feature'dagi. Dasturchi variantni tanlaydi yoki ikkisini birlashtiradi, belgilarni o'chiradi, `git add` va `git commit` qiladi. Android'da XML, Kotlin klasslari (masalan `HomeScreen.kt`) va string resurslarda konflikt tabiiy.

Analogiya: ikki odam bir matnni bir vaqtda tahrirladi, ularni taqqoslab, yaxshisini tanlab birlashtirasiz.

### 3. Pull Request

PR: bir branchdagi o'zgarishlarni boshqasiga qo'shish uchun rasmiy so'rov (GitLab'da Merge Request). Mazmuni: "Men yangi funksiya yaratdim, asosiy loyihaga qo'shmoqchiman, jamoa ko'rib chiqib fikr bildirsin".

Ssenariy (hujjatdan): "Maktab Jadvali" ilovasi, "darslar ro'yxati ekrani".

```bash
git checkout -b feature/lessons-screen
# Compose bilan UI yoziladi
git add .
git commit -m "Lessons screen UI created"
git push origin feature/lessons-screen
```

```kotlin
@Composable
fun LessonsScreen() {
    Column {
        Text("Bugungi darslar")
        LessonItem("Matematika", "08:30")
        LessonItem("Ingliz tili", "09:20")
    }
}
```

Keyin PR ochiladi, jamoa sharh qoldiradi ("UI zo'r, lekin rang sxemasini Material3 ga moslashtiring"), muallif tuzatadi, PR yangilanadi, tasdiqlangach merge qilinadi.

**Code Review mezonlari:** kod toza yozilganmi; ortiqcha takrorlanish yo'qmi; xavfsizlik xatolari bormi; arxitektura qoidalariga amal qilinganmi; UI kutilgan natijani beradimi.

**PR madaniyati:** toza kod, ma'noli commitlar, PR hajmi katta bo'lmasligi, sharhlarga ochiqlik, konstruktiv fikr, hurmatli muloqot.

**Branch strategiyalari:** Git Flow, Trunk Based Development, GitHub Flow. Git Flow'da: main (barqaror), develop, feature, release, hotfix. Android jamoalari ko'pincha GitHub Flow yoki Trunk Based'ni qo'llaydi.

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Branch ochish

Bo'sh papkada `git init`, `README.md` yarating, commit qiling. `feature/login` branchini oching, `login.txt` yarating va commit qiling. `main` ga qaytib `login.txt` yo'qligini tekshiring.

**Yechim:**
```bash
git init
echo "Maktab Jadvali" > README.md
git add . && git commit -m "Boshlang'ich commit"
git checkout -b feature/login
echo "login kodi" > login.txt
git add . && git commit -m "Login fayli qo'shildi"
git checkout main
ls
```
`ls` natijasida `login.txt` ko'rinmaydi (o'zgarish shoxda qoldi).

### 2-topshiriq (o'rta). Merge

`feature/login` ni `main` ga merge qiling va `git log --oneline` ni ko'ring.

**Yechim:**
```bash
git checkout main
git merge feature/login
git log --oneline
```
Main shoxdan keyin o'zgarmagani uchun Git odatda fast-forward qiladi va `login.txt` main'da paydo bo'ladi.

### 3-topshiriq (qiyin). Sun'iy konflikt

`HomeScreen.kt` faylini yarating. Ikki branchda (`main` va `feature/home`) shu fayldagi bir xil satrni turlicha o'zgartiring va merge qilib, konfliktni hal qiling.

**Yechim:**
```bash
echo "fun loadUser() {}" > HomeScreen.kt
git add . && git commit -m "HomeScreen"
git checkout -b feature/home
echo "fun loadUserData() {}" > HomeScreen.kt
git commit -am "Nom o'zgardi"
git checkout main
echo "fun fetchUser() {}" > HomeScreen.kt
git commit -am "Boshqa nom"
git merge feature/home
```
Git `CONFLICT` deydi. Faylni oching, belgilarni o'chirib bitta variantni qoldiring (masalan `fun loadUserData() {}`):
```bash
git add HomeScreen.kt
git commit -m "Konflikt hal qilindi"
```

### 4-topshiriq (o'rta). Branch nomlari

Quyidagi uch ish uchun branch nomi yozing: "login ekrani", "profil sahifasi qulashi", "home ekranini tartiblash".

**Yechim:** `feature/login`, `bugfix/profile-crash`, `refactor/home-screen`.

### 5-topshiriq (qiyin). PR tavsifi va sharh

"Lessons screen" PR'i uchun qisqa tavsif yozing va hamkasbingiz kodiga 2 ta konstruktiv sharh bering.

**Yechim:** Tavsif: "Darslar ro'yxati ekrani Compose bilan qo'shildi, 2 ta LessonItem ko'rsatiladi." Sharhlar: "Rang sxemasini Material3 ga moslang." "LessonItem takrorlanayapti, ro'yxatdan chiqarish mumkinmi?" Mezon: aniq, hurmatli, taklifga yo'naltirilgan.

---

## Tezkor nazorat

1. Branch nima? **Javob:** Loyihaning mustaqil shoxchasi; aslida commitga ishora qiluvchi pointer.
2. `git checkout -b x` nima qiladi? **Javob:** x branchini yaratadi va unga o'tadi.
3. Konflikt qachon chiqadi? **Javob:** Bir faylning bir xil satri ikki branchda turlicha o'zgarsa.
4. `<<<<<<< HEAD` dan keyingi kod qaysi branchniki? **Javob:** Joriy (main) branchniki.
5. Code Review nimani tekshiradi? **Javob:** Toza kod, takrorlanish, xavfsizlik, arxitektura, UI natijasi.

## Uyga vazifa

`uyga-vazifa.md` ga qarang.
