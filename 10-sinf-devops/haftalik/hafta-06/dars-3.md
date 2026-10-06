# 18-dars. GitHub Flow va GitKraken/CLI orqali jamoaviy kollaboratsiya

**Darsning maqsadi:** `GitHub Flow` ning bosqichlarini (branch, commit, PR, review, merge, deploy), branch nomlash qoidalarini (`feature/`, `bugfix/`, `hotfix/`), `gh` CLI buyruqlarini va GitKraken (grafik Git mijozi) bilan bir xil ishni bajarishni o'rgatish.

**Manba (rasmiy hujjat):** O'quv qo'llanma va uslubiy ko'rsatma, Git bobi: branch turlari (feature, bugfix, hotfix, release), branching strategiyalari (Feature branching, Git Flow, GitHub Flow, Trunk-based), Pull Request va code review (uchta qaror), `git rebase origin/main`. `gh` buyruqlari va GitKraken imkoniyatlari standart hujjatlardan qo'shildi.

**Vaqt taqsimoti (80 daqiqa):**
- Takrorlash: 10 daqiqa (17-dars: tag, SemVer, release)
- 01. GitHub Flow: 15 daqiqa
- 02. PR va code review: 15 daqiqa
- Tanaffus: 5 daqiqa
- 03. CLI va GitKraken: 15 daqiqa
- Amaliyot: 15 daqiqa
- Xulosa va tezkor nazorat: 5 daqiqa

---

## 1. Konspekt (mentor uchun)

### 1.1. GitHub Flow: bosqichlar
**GitHub Flow** — kichik jamoalar va o'quv loyihalari uchun mos oddiy strategiya. Qoida: **`main` doim barqaror** (deploy qilsa bo'ladigan). Har bir vazifa uchun **alohida branch** ochiladi, o'zgarish **Pull Request (PR)** orqali ko'rib chiqiladi va tasdiqlangach `main` ga birlashtiriladi. Bosqichlar: 1) branch yaratish, 2) commit lar, 3) PR ochish, 4) code review, 5) merge, 6) deploy va branch ni o'chirish. Katta enterprise loyihalarda Git Flow (release va hotfix branch lari) ishlatiladi.
```bash
main                   # barqaror
feature/login-api      # yangi funksiya
bugfix/navbar          # kichik tuzatish
hotfix/payment-error   # productiondagi shoshilinch xato
release/v2.1           # versiya tayyorlash
```
Branch nomi nima qilinayotganini aytsin: `feature/login-api`, `fix1` emas. Bitta branch — bitta vazifa.

### 1.2. Pull Request va code review
Branch ni push qilgach, GitHub da **Pull Request** ochiladi: nima o'zgargani va nima uchun yozilgani tushuntiriladi. Hamkasblar kodni ko'radi: izohlar, `suggestion` lar, lint/test tekshiruvlari va tasdiq (**approval**). Review natijasi odatda uchtadan biri: **Approve** (tasdiq), **Request changes** (o'zgartirish talab) yoki **Comment** (izoh). Siz tuzatib, yana push qilsangiz, PR avtomatik yangilanadi. Asosiy branch yangilangan bo'lsa, `git rebase origin/main` yoki merge bilan moslashtiriladi. Tasdiqdan so'ng **Merge**, keyin branch o'chiriladi.
```bash
git switch -c feature/hello-button
git add .
git commit -m "feat: add hello button"
git push -u origin feature/hello-button
gh pr create --fill
gh pr checks
```
Commit xabarida qisqa prefiks (`feat:`, `fix:`, `docs:`) review ni osonlashtiradi. PR kichik bo'lsin: katta PR ni hech kim diqqat bilan o'qimaydi.

### 1.3. gh CLI va GitKraken
Bir xil ishni ikki usulda qilish mumkin. **CLI** (terminal) tez va avtomatlashtiriladi: `git` va `gh`. **GitKraken** — grafik Git mijozi: commit tarixi grafik ko'rinishda, branch lar chap panelda, konfliktni yechish va PR yaratish tugmalar orqali. Boshlovchilar uchun grafik tarix tushunishga yordam beradi, CLI esa serverda va avtomatlashtirishda zarur. Reviewer tomoni: `gh pr checkout 12` PR ni lokalga oladi, `gh pr review 12 --approve` tasdiqlaydi, `gh pr merge 12 --squash --delete-branch` birlashtiradi.
```bash
gh pr list
gh pr checkout 12
gh pr review 12 --approve
gh pr merge 12 --squash --delete-branch
git switch main && git pull
```
`--squash` PR dagi barcha commit larni bittaga aylantiradi. GitKraken da ham xuddi shu: PR ni oching, tekshiring va Merge ni bosing.

---

## 2. Amaliy topshiriqlar va yechimlari

### 1-topshiriq (oson). Branch yarating
`feature/login-api` branch ini yarating.

**Yechim:**
```bash
git switch -c feature/login-api
```

### 2-topshiriq (oson). Push qiling
Branch ni birinchi marta GitHub ga yuboring.

**Yechim:**
```bash
git push -u origin feature/login-api
```

### 3-topshiriq (o'rta). PR oching
`gh` bilan PR oching.

**Yechim:**
```bash
gh pr create --fill
```

### 4-topshiriq (o'rta). Nomni tuzating
`fix1` branch nomini yaxshilang.

**Yechim:** Masalan `bugfix/navbar-overlap`: vazifani aytsin.

### 5-topshiriq (qiyin). Review
Hamkasb PR ini lokalda sinab, tasdiqlang.

**Yechim:**
```bash
gh pr checkout 12
gh pr review 12 --approve
```

### 6-topshiriq (qo'shimcha). Strategiya
Nega katta jamoa Git Flow ni tanlaydi?

**Yechim:** Rejali release lar va hotfix lar uchun alohida branch lar kerak.

---

## 3. Tezkor nazorat
1. **GitHub Flow bosqichlari?** *Javob:* Branch, commit, PR, review, merge, deploy.
2. **`main` qanday bo'ladi?** *Javob:* Doim barqaror.
3. **Branch nomi misoli?** *Javob:* `feature/login-api`.
4. **Review natijalari?** *Javob:* Approve, request changes, comment.
5. **CLI va GitKraken farqi?** *Javob:* CLI — terminal; GitKraken — grafik, natija bir xil.

## Mentor uchun eslatma
Juft ishlashda B ning GitHub hisobini Settings → Collaborators ga qo'shishni oldindan tayyorlang. `gh` o'rnatilmagan bo'lsa, PR ni veb orqali oching; GitKraken ixtiyoriy va o'rnatishni talab qiladi. Hujjatda branch turlari, strategiyalar, PR va review qarorlari bor; konkret `gh` buyruqlari va GitKraken tavsifi standart manbalardan qo'shildi. Reviewer kodni sinamay tasdiqlamasligini ta'kidlang. Keyingi dars: GitHub Actions asoslari.
