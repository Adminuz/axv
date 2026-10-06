# 18-dars. Git va GitHub (1-qism): versiya nazorati, commit va GitHub'ga push

> Loyihangiz o'sib bormoqda: sahifa, CSS, rasmlar. Xato qilsangiz, eski holatga qaytish kerak bo'ladi. Bugun Git bilan loyiha tarixini saqlaymiz va GitHub'ga yuboramiz.

## Dars xulosasi

- Git — versiya nazorati; GitHub — onlayn saqlash.
- Uch hudud: ishchi papka → staging → repository.
- `init`, `status`, `add`, `commit`, `log` — asosiy buyruqlar.
- Commit xabari aniq va qisqa bo'lsin.
- `.gitignore` maxfiy va keraksiz fayllarni chiqaradi.
- `remote add origin` va `push -u origin main` — GitHub'ga yuborish.

## Qo'shimcha ma'lumot

### `git diff`
Hali commit qilinmagan o'zgarishlarni ko'rsatadi.

### `git restore`
Faylni oxirgi commit holatiga qaytaradi.

### README.md
Repo sahifasidagi tavsif fayli.

### Conventional commits
Commit xabarlari uchun yagona qoida.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| VCS | Versiya nazorati tizimi |
| Repository | Loyiha va uning tarixi |
| Commit | Saqlangan holat |
| Staging | Commitga tayyorlash hududi |
| Remote | Masofaviy repo |
| origin | Remote'ning odatiy nomi |
| Push | GitHub'ga yuborish |
| .gitignore | Kuzatilmaydigan fayllar ro'yxati |

## Bilasizmi?

- Commit ID — 40 belgili kod; `--oneline` da faqat boshidagi 7 belgi ko'rinadi.
- `git diff` commitdan oldin nima o'zgarganini ko'rsatadi.
- Git'ni 2005-yilda Linus Torvalds Linux yadrosi uchun yaratgan.

## Topshiriqlar

### 1. Git nima · oson

Git nima va nima uchun kerak?

**Kutiladigan natija:** Versiya nazorati tizimi.

### 2. Commit · oson

Commit nima? Nimalardan iborat?

**Kutiladigan natija:** Xabar, muallif, vaqt, ID.

### 3. Uch hudud · oson

Uch hududni tartib bilan yozing.

**Kutiladigan natija:** Ishchi papka, staging, repository.

### 4. Buyruq vazifasi · oson

`init` va `status` nima qiladi?

**Kutiladigan natija:** Repo yaratadi, holatni ko'rsatadi.

### 5. Add va commit · o'rta

`add` va `commit` farqini yozing.

**Kutiladigan natija:** Add — tayyorlash, commit — saqlash.

### 6. Xabar yozish · o'rta

3 ta yaxshi commit xabari yozing.

**Kutiladigan natija:** Aniq, qisqa xabarlar.

### 7. Git log · o'rta

Tarixni qisqa ko'rinishda chiqarish buyrug'i?

**Kutiladigan natija:** `git log --oneline`.

### 8. gitignore · o'rta

Qaysi fayllar `.gitignore` ga yoziladi?

**Kutiladigan natija:** `.env`, `node_modules/`.

### 9. Remote · qiyin

GitHub bilan ulash buyrug'ini yozing.

**Kutiladigan natija:** `git remote add origin URL`.

### 10. Push tartibi · qiyin

Yangi o'zgarishni GitHub'ga yuborish tartibini yozing.

**Kutiladigan natija:** add, commit, push.

### 11. Xavfsizlik · qiyin

Nega parollarni repo'ga yuklab bo'lmaydi?

**Kutiladigan natija:** Public repo hammaga ko'rinadi.

### 12. Loyiha tarixi · bonus

Loyihangiz uchun 5 ta commit xabarini rejalashtiring.

**Kutiladigan natija:** Mantiqiy 5 qadam.

## O'zingizni tekshiring

1. Git va GitHub farqi?
2. Uch hudud?
3. Asosiy buyruqlar?
4. `.gitignore` nima?
5. Push qanday bajariladi?
6. Commit xabari qanday bo'lishi kerak?

## Uyga vazifa

«Maktab sayti» ni Git bilan boshqaring va GitHub'ga yuboring (30 daqiqa). To'liq shart: `uyga-vazifa.md`.
