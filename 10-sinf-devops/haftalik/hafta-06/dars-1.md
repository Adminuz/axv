# 16-dars. Git ilg'or texnikalari: git stash, rebase, cherry-pick va reflog imkoniyatlari

**Darsning maqsadi:** `git stash` bilan tugallanmagan ishni vaqtincha chetga qo'yishni, `git rebase` va `merge` farqini, `rebase -i` bilan commit larni tozalashni, `git cherry-pick` bilan bitta commit ni ko'chirishni va `git reflog` bilan «yo'qolgan» commit larni tiklashni o'rgatish.

**Manba (rasmiy hujjat):** O'quv qo'llanma va uslubiy ko'rsatma: Git bobi (branch, merge va rebase farqi, PR da `git rebase origin/main`). `git stash`, `cherry-pick` va `reflog` rejadagi mavzu bo'yicha standart Git hujjatlaridan qo'shildi.

**Vaqt taqsimoti (80 daqiqa):**
- Takrorlash: 10 daqiqa (14-dars: branch, merge va konfliktlar)
- 01. git stash: 15 daqiqa
- 02. rebase va cherry-pick: 15 daqiqa
- Tanaffus: 5 daqiqa
- 03. git reflog: 15 daqiqa
- Amaliyot: 15 daqiqa
- Xulosa va tezkor nazorat: 5 daqiqa

---

## 1. Konspekt (mentor uchun)

### 1.1. git stash: tugallanmagan ishni saqlash
Siz `feature` branch da ishlayapsiz, lekin tugallanmagan; shu payt `main` da shoshilinch xatoni tuzatish kerak. Commit qilish uchun kod hali tayyor emas. **`git stash`** o'zgarishlarni vaqtincha «javon»ga qo'yadi va ishchi papkani toza holatga qaytaradi. Keyin branch almashtirasiz, ishni qilasiz, qaytib kelib **`git stash pop`** bilan o'zgarishlarni qaytarasiz. Ro'yxat: `git stash list`. `apply` o'zgarishni qaytaradi, lekin stash ni saqlaydi; `pop` qaytarib, stash ni o'chiradi. Yangi (kuzatilmayotgan) fayllar uchun `-u` kerak.
```bash
git stash push -m "login formasi yarim"
git switch main
# ... shoshilinch tuzatish, commit ...
git switch feature/login
git stash list
git stash pop
```
`git stash push -u -m "..."` yangi fayllarni ham saqlaydi. Stash ga xabar (`-m`) yozing, aks holda keyin nimaligini topolmaysiz.

### 1.2. rebase, interaktiv rebase va cherry-pick
**Merge** ikkala tarixni saqlab, birlashtiruvchi commit yaratadi. **Rebase** branch ingiz commit larini `main` ning oxiriga «ko'chirib» qo'yadi: tarix to'g'ri chiziq bo'ladi. Uslubiy ko'rsatmada PR yangilanayotganda `git rebase origin/main` (yoki merge) ishlatiladi. Konflikt chiqsa: fayllarni tuzating, `git add`, `git rebase --continue`; qaytish uchun `--abort`. **`git rebase -i HEAD~3`** oxirgi 3 commit ni tahrirlaydi (`squash` — birlashtirish, `reword` — xabarni o'zgartirish). **`git cherry-pick <sha>`** boshqa branch dagi bitta commit ni ko'chirib oladi. **Oltin qoida:** boshqalar ishlatayotgan (push qilingan) umumiy tarixni rebase qilmang.
```bash
git switch feature/hello-button
git fetch origin
git rebase origin/main
# konflikt bo'lsa:
git add .
git rebase --continue
git rebase -i HEAD~3
git switch main
git cherry-pick a1b2c3d
```
Rebase commit larning SHA ini o'zgartiradi. Push qilingan branch dan keyin kerak bo'lsa `git push --force-with-lease` ishlatiladi, `--force` emas, va faqat o'z branch ingizda.

### 1.3. git reflog: yo'qolgan commit ni topish
Xato qildingiz: `git reset --hard` bilan commit larni «yo'qotdingiz» yoki branch ni o'chirdingiz. Git hamma narsani darrov o'chirmaydi. **`git reflog`** HEAD ning barcha harakatlarini (commit, checkout, reset, rebase) vaqt tartibida ko'rsatadi: `HEAD@{0}`, `HEAD@{1}`... Kerakli holatning SHA sini topib, `git reset --hard HEAD@{2}` yoki `git switch -c tiklangan a1b2c3d` bilan qaytasiz. Reflog faqat **lokal** va vaqtinchalik (odatda bir necha hafta saqlanadi), shuning uchun xatodan keyin kutmang.
```bash
git reset --hard HEAD~2
git reflog
git switch -c tiklangan a1b2c3d
git log --oneline
```
Tiklashda `reset --hard` o'rniga yangi branch ochish xavfsizroq: hech narsa ustiga yozilmaydi.

---

## 2. Amaliy topshiriqlar va yechimlari

### 1-topshiriq (oson). Stash qiling
Yarim ishni stash ga qo'ying va ro'yxatni ko'ring.

**Yechim:**
```bash
git stash push -m "yarim ish"
git stash list
```

### 2-topshiriq (oson). Stash qaytaring
Stash ni qaytarib, ro'yxatdan olib tashlang.

**Yechim:**
```bash
git stash pop
```

### 3-topshiriq (o'rta). Merge yoki rebase
Umumiy main ni yangilashda qaysi biri xavfsizroq?

**Yechim:** Umumiy tarixda merge xavfsizroq; rebase faqat o'z, push qilinmagan branch uchun.

### 4-topshiriq (o'rta). Cherry-pick
`a1b2c3d` commit ni `main` ga ko'chiring.

**Yechim:**
```bash
git switch main
git cherry-pick a1b2c3d
```

### 5-topshiriq (qiyin). Squash
Oxirgi 3 commit ni bittaga birlashtirish buyrug'ini yozing.

**Yechim:** `git rebase -i HEAD~3`, so'ng 2 va 3-qatorda `pick` o'rniga `squash`.

### 6-topshiriq (qo'shimcha). Tiklash
`reset --hard` dan keyin commit ni tiklang.

**Yechim:** `git reflog` → SHA → `git switch -c tiklangan <sha>`.

---

## 3. Tezkor nazorat
1. **`git stash` nima qiladi?** *Javob:* Tugallanmagan o'zgarishlarni vaqtincha saqlaydi.
2. **`pop` va `apply` farqi?** *Javob:* `pop` stash ni o'chiradi, `apply` saqlab qoladi.
3. **Merge va rebase farqi?** *Javob:* Merge tarixni saqlaydi, rebase uni to'g'ri chiziqqa ko'chiradi.
4. **`cherry-pick` nima?** *Javob:* Bitta commit ni boshqa branch ga ko'chiradi.
5. **`reflog` nima uchun?** *Javob:* Yo'qolgan commit ni topib tiklash.

## Mentor uchun eslatma
Mashqlarni test repozitoriyda bajaring; haqiqiy loyiha tarixida rebase qilishdan oldin nusxa branch oching. `force-with-lease` ni ko'rsating, lekin umumiy branch da ishlatilmasligini ta'kidlang. Hujjatda faqat `git rebase origin/main` va merge va rebase farqi bor; `stash`, `cherry-pick` va `reflog` standart Git hujjatlaridan qo'shildi. Konflikt chiqsa `git status` har bosqichda nima qilish kerakligini aytib turadi. Keyingi dars: taglar va SemVer.
