# 16-dars. Git ilg'or texnikalari: git stash, rebase, cherry-pick va reflog imkoniyatlari

> Haqiqiy ishda Git faqat add va commit emas. Bugun ishni chetga qo'yish, tarixni tartiblash va xatodan qaytishni o'rganamiz.

## Dars xulosasi

- `git stash` tugallanmagan ishni vaqtincha saqlaydi, `pop` qaytaradi.
- Merge tarixni saqlaydi, rebase uni to'g'ri chiziqqa o'tkazadi.
- Konfliktda `rebase --continue` yoki `--abort` ishlatiladi.
- `rebase -i` commit larni birlashtiradi va xabarini o'zgartiradi.
- `cherry-pick <sha>` bitta commit ni ko'chiradi.
- `reflog` yo'qolgan commit ni topishga yordam beradi.

## Qo'shimcha ma'lumot

### stash -u
Kuzatilmayotgan yangi fayllarni ham saqlaydi.

### --abort
Rebase ni to'xtatib, avvalgi holatga qaytaradi.

### force-with-lease
Boshqa birov push qilgan bo'lsa, ustiga yozishdan saqlaydi.

### HEAD~3
HEAD dan 3 ta commit orqaga.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| stash | Vaqtincha saqlash |
| rebase | Commit larni ko'chirish |
| cherry-pick | Bitta commit ko'chirish |
| reflog | HEAD jurnali |
| HEAD | Joriy commit |
| SHA | Commit identifikatori |
| squash | Commit larni birlashtirish |
| konflikt | Ziddiyatli o'zgarish |

## Bilasizmi?

- `git stash` bir nechta bo'lishi mumkin: `stash@{0}`, `stash@{1}`.
- `git reflog` faqat sizning lokal repozitoriyingizda saqlanadi, GitHub ga ketmaydi.
- Interaktiv rebase da commit tartibini o'zgartirish mumkin.

## Topshiriqlar

### 1. Stash qilish · oson

Faylni o'zgartirib, stash ga qo'ying va ro'yxatni ko'ring.

**Kutiladigan natija:** `git stash push -m`, `git stash list`.

### 2. Stash qaytarish · oson

Stash ni qaytaring. `pop` va `apply` farqi?

**Kutiladigan natija:** `pop` o'chiradi, `apply` saqlaydi.

### 3. Atamalar · oson

rebase, cherry-pick va reflog ni 1 jumlada ta'riflang.

**Kutiladigan natija:** 3 ta to'g'ri ta'rif.

### 4. SHA topish · oson

Commit SHA ni qaysi buyruq ko'rsatadi?

**Kutiladigan natija:** `git log --oneline`.

### 5. Rebase qilish · o'rta

`feature` ni `main` ustiga rebase qiling.

**Kutiladigan natija:** `git rebase main`.

### 6. Konflikt · o'rta

Rebase da konflikt bo'lsa, qadamlarni yozing.

**Kutiladigan natija:** Tuzatish, `git add`, `--continue`.

### 7. Merge yoki rebase · o'rta

3 kishi ishlaydigan branch uchun qaysi biri? Nega?

**Kutiladigan natija:** Merge: umumiy tarixni buzmaydi.

### 8. Cherry-pick · o'rta

Boshqa branch dagi bitta commit ni ko'chiring.

**Kutiladigan natija:** `git cherry-pick <sha>`.

### 9. Squash · qiyin

Oxirgi 4 commit ni bittaga birlashtiring.

**Kutiladigan natija:** `git rebase -i HEAD~4`, `squash`.

### 10. Tiklash · qiyin

`reset --hard HEAD~2` dan keyin commit larni qaytaring.

**Kutiladigan natija:** `git reflog` va `switch -c`.

### 11. Xavfsizlik · qiyin

`--force-with-lease` nega `--force` dan yaxshi?

**Kutiladigan natija:** Boshqa birovning ishini ustiga yozmaydi.

### 12. Skript · bonus

Stash, rebase va reflog dan 1 sahifalik qo'llanma yozing.

**Kutiladigan natija:** To'g'ri buyruqlar va ogohlantirish.

## O'zingizni tekshiring

1. `git stash` nima qiladi?
2. `pop` va `apply` farqi?
3. Merge va rebase farqi?
4. `cherry-pick` nima?
5. `reflog` nima uchun?
6. Rebase ning oltin qoidasi?

## Uyga vazifa

stash, rebase, cherry-pick va reflog ni test repozitoriyda sinang (30 daqiqa). To'liq shart: `uyga-vazifa.md`.
