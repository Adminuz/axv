# 10-dars. GitLab va Bitbucket'da jamoaviy ish jarayonlari

> Git bitta, lekin uni joylashtiradigan "uy"lar bir nechta. Bugun jamoa qanday ishlashini: guruhlar, rollar, vazifa doskasi, Merge Request va pipeline'ni ko'rasiz.

## Dars xulosasi

- GitHub, GitLab va Bitbucket: Git'ni bulutga chiqaradigan onlayn platformalar.
- Umumiy tomonlari: repository, guruhlar, Issue tracker, Code Review, CI/CD.
- `git clone` serverdagi loyihaning to'liq nusxasini kompyuterga tushiradi.
- Group va Team: loyihalar va odamlarni boshqarish; Role: kim nima qila olishini belgilaydi.
- Issue tracker va Kanban: vazifalar To Do, In Progress, Done ustunlari bo'ylab ko'chadi.
- GitLab'da Pull Request "Merge Request" deb ataladi.
- Code Review: jamoa kodni satrma-satr tekshiradi, tasdiqlagach merge qilinadi.
- Pipeline: build va test kabi bosqichlar avtomatik ketma-ket bajariladi.

## Qo'shimcha ma'lumot

### Nega bitta emas, uchta platforma?

Git bu "dvigatel". GitHub, GitLab va Bitbucket esa shu dvigatel o'rnatilgan turli "garaj"lar. Kodni push qilasiz, jamoa ko'radi. Buyruqlar bir xil, farq faqat sayt imkoniyatlari va atamalarida: masalan GitHub'da PR, GitLab'da MR.

### Nega rollar kerak?

Tasavvur qiling, maktab jurnalini hamma tahrirlay oladi. Bitta noto'g'ri bosish hammaning bahosini o'chiradi. Shuning uchun har kimga faqat o'z ishi uchun yetarli huquq beriladi, asosiy kodga o'zgarish esa tekshiruvdan keyin kiradi.

### Kanban doskasi

Devordagi stikerlar kabi: har vazifa bitta kartochka. Qaysi ustunda turgani ishning holatini ko'rsatadi: kim nima bilan bandligi bir qarashda ko'rinadi.

### Odatiy xatolar

- Hamma to'g'ridan-to'g'ri `main` ga yozadi.
- Branch nomi "test2" kabi tushunarsiz.
- Rol juda keng beriladi.
- Review'siz merge qilinadi.

### O'quv namunasi: `.gitlab-ci.yml`

Quyidagi fayl o'quv uchun to'qilgan oddiy misol (rasmiy hujjatda GitLab CI fayli ko'rsatilmagan):

```yaml
stages:
  - build
  - test
build_job:
  stage: build
  script:
    - ./gradlew assembleDebug
```

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| GitLab | DevOps imkoniyatlari kuchli Git platformasi |
| Bitbucket | Jamoalar uchun repository va pipeline platformasi |
| Repository | Loyiha kodi, tarixi va branchlar ombori |
| Group | Loyihalar va odamlarni birlashtiruvchi guruh |
| Team | Loyiha ustida ishlaydigan a'zolar |
| Role | A'zoning huquq darajasi |
| Issue | Xato, vazifa yoki taklif yozuvi |
| Merge Request | GitLab'da Pull Request nomi |
| Code Review | Jamoaning bir-birining kodini tekshirishi |
| Pipeline | Avtomatik bajariladigan jarayonlar ketma-ketligi |

## Bilasizmi?

- Katta kompaniyalarda kodni PR orqali tasdiqlash majburiy bosqich hisoblanadi.
- GitHub'ni dasturchilarning "ijtimoiy tarmog'i" deb ham atashadi: profil, Star va Fork bor.
- Test muvaffaqiyatsiz bo'lsa, GitLab CI Merge Request'ni avtomatik rad etadi.
- Kanban so'zi yapon tilidan olingan va "kartochka" ma'nosini anglatadi (qo'shimcha ma'lumot).

## Topshiriqlar

### 1. Uch platforma · oson
GitHub, GitLab va Bitbucket nomlarini yozing va ularning umumiy 3 ta funksiyasini ayting.

**Kutiladigan natija:** repository, Issue tracker, CI/CD kabi ro'yxat.

### 2. PR yoki MR? · oson
GitLab'da qaysi atama ishlatiladi: Pull Request yoki Merge Request?

**Kutiladigan natija:** Merge Request.

### 3. Kanban ustunlari · oson
Kanban doskasining 3 ustunini sanang.

**Kutiladigan natija:** To Do, In Progress, Done.

### 4. Branch nomi · oson
"Profil sahifasidagi xatoni tuzatish" uchun to'g'ri branch nomini yozing.

**Kutiladigan natija:** `bugfix/profile-crash` kabi nom.

### 5. Klonlash · o'rta
Quyidagi havoladagi loyihani klonlang, papkaga kiring va `feature/lessons-screen` branchini oching: `https://gitlab.com/guruh/maktab-jadvali.git`

**Kutiladigan natija:** 3 ta buyruq ketma-ketligi.

### 6. Guruh sxemasi · o'rta
Daftarda "maktab-it-jamoasi" guruhini chizing: 2 loyiha va 4 a'zo, har kimga rol.

**Kutiladigan natija:** tushunarli sxema, rollar vazifaga mos.

### 7. Xatoni toping · o'rta
Jamoada hamma `main` ga to'g'ridan-to'g'ri yozmoqda. Nima xavf bor va qanday tuzatasiz?

**Kutiladigan natija:** xavfni va "feature branch + MR + review" yechimini yozing.

### 8. Kanban doskasi · o'rta
Loyihangiz uchun 5 ta vazifa o'ylab toping va ustunlarga joylang.

**Kutiladigan natija:** har ustunda kamida bitta vazifa.

### 9. MR sharhi · qiyin
Hamkasbingizning "darslar ro'yxati ekrani" kodiga 3 ta konstruktiv sharh yozing.

**Kutiladigan natija:** aniq, hurmatli, taklifga yo'naltirilgan sharhlar.

### 10. Pipeline rejasi · qiyin
Android loyihangiz uchun pipeline bosqichlarini yozing va test yiqilsa nima bo'lishini tushuntiring.

**Kutiladigan natija:** Commit, Build, Test, Review, Deploy ketma-ketligi va MR rad etilishi.

### 11. Platformalar tadqiqoti · qiyin
GitLab va Bitbucket'ning rasmiy saytida ularning pipeline nomini toping va GitHub Actions bilan solishtiring.

**Kutiladigan natija:** 3-4 jumlalik taqqoslash.

### 12. Mini-loyiha: jamoa qoidalari · bonus
O'z jamoangiz uchun 1 sahifalik qoidalar yozing: branch nomlash, rollar, review tartibi.

**Kutiladigan natija:** aniq va qisqa hujjat.

## O'zingizni tekshiring

1. GitHub, GitLab va Bitbucket orasidagi umumiy tomonlar qaysilar?
2. Merge Request va Pull Request o'rtasida qanday munosabat bor?
3. Nega a'zolarga minimal huquq beriladi?
4. Kanban doskasi vazifa holatini qanday ko'rsatadi?
5. Code Review nimani tekshiradi?
6. Pipeline nima va nima uchun avtomatik?

## Uyga vazifa

1. O'z jamoangiz uchun guruh, rollar va Kanban ustunlari sxemasini tuzing.
2. Android loyihangiz uchun pipeline bosqichlarini yozing.
