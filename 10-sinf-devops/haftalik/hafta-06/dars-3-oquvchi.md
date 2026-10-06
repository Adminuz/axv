# 18-dars. GitHub Flow va GitKraken/CLI orqali jamoaviy kollaboratsiya

> Jamoada hamma bir vaqtda main ga yozsa, tartibsizlik bo'ladi. Bugun GitHub Flow, PR va code review ni amalda sinaymiz.

## Dars xulosasi

- GitHub Flow: main doim barqaror, har vazifa alohida branch da.
- Bosqichlar: branch, commit, PR, review, merge, deploy.
- Nomlash: `feature/`, `bugfix/`, `hotfix/`, `release/`.
- Review natijasi: approve, request changes, comment.
- `gh pr create`, `checkout`, `review`, `merge` — CLI orqali.
- GitKraken — grafik alternativ, natija bir xil.

## Qo'shimcha ma'lumot

### Branch protection
`main` ga to'g'ridan-to'g'ri push ni taqiqlaydi.

### Squash merge
PR commit larini bittaga birlashtiradi.

### Code owner
Muayyan fayllarni tekshiruvchi mas'ul.

### Draft PR
Hali tayyor bo'lmagan PR.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| GitHub Flow | Oddiy branch + PR jarayoni |
| PR | Pull Request |
| Review | Kod tekshiruvi |
| Approve | Tasdiqlash |
| Merge | Birlashtirish |
| feature branch | Vazifa branch i |
| gh | GitHub CLI |
| GitKraken | Grafik Git mijozi |

## Bilasizmi?

- GitHub Flow tashkilotlarda eng ko'p ishlatiladigan oddiy strategiyalardan biri.
- Branch protection qoidalari `main` ga to'g'ridan-to'g'ri push qilishni taqiqlashi mumkin.
- Ko'p jamoalar PR da avtomatik testlarni (CI) majburiy qiladi.

## Topshiriqlar

### 1. Bosqichlar · oson

GitHub Flow ning 6 bosqichini yozing.

**Kutiladigan natija:** Branch, commit, PR, review, merge, deploy.

### 2. Branch nomi · oson

Yangi funksiya uchun branch nomini yozing.

**Kutiladigan natija:** `feature/...`.

### 3. Branch yaratish · oson

Branch yaratib, GitHub ga yuboring.

**Kutiladigan natija:** `git switch -c`, `git push -u`.

### 4. main qoidasi · oson

`main` haqida asosiy qoida?

**Kutiladigan natija:** Doim barqaror.

### 5. PR ochish · o'rta

PR ni CLI orqali oching.

**Kutiladigan natija:** `gh pr create --fill`.

### 6. Review qarori · o'rta

3 ta review qarorini yozing.

**Kutiladigan natija:** Approve, request changes, comment.

### 7. Hotfix · o'rta

Productiondagi xato uchun branch nomi?

**Kutiladigan natija:** `hotfix/...`.

### 8. Sinxronlash · o'rta

PR branch ini yangi main bilan qanday moslashtirasiz?

**Kutiladigan natija:** `git rebase origin/main` yoki merge.

### 9. Reviewer · qiyin

Reviewer PR ni qanday sinaydi?

**Kutiladigan natija:** `gh pr checkout` va test.

### 10. Strategiya · qiyin

GitHub Flow va Git Flow ni qachon tanlaysiz?

**Kutiladigan natija:** Kichik jamoa va katta jamoa.

### 11. PR tavsifi · qiyin

Yaxshi PR tavsifi nimalarni o'z ichiga oladi?

**Kutiladigan natija:** Nima, nega, qanday sinaldi.

### 12. Juft loyiha · bonus

Juftlikda PR sikl ini bajaring va skrinshot qo'shing.

**Kutiladigan natija:** Ochilgan, review qilingan, merge PR.

## O'zingizni tekshiring

1. GitHub Flow bosqichlari?
2. `main` qanday bo'ladi?
3. Branch nomlash?
4. Review natijalari?
5. `gh pr create` nima qiladi?
6. CLI va GitKraken farqi?

## Uyga vazifa

Juft bilan PR siklini bajaring (30 daqiqa). To'liq shart: `uyga-vazifa.md`.
