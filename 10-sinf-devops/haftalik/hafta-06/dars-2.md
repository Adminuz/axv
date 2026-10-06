# 17-dars. Git taglar va versiyalash: semantik versiyalash (SemVer), release yaratish

**Darsning maqsadi:** `git tag` ning ikki turini (lightweight va annotated), tagni GitHub ga yuborishni, `SemVer` (MAJOR.MINOR.PATCH) qoidalarini, pre-release (`-rc.1`) belgilarini va GitHub da release yaratishni (veb va `gh` orqali) o'rgatish.

**Manba (rasmiy hujjat):** O'quv qo'llanma, Git bobi: `release/v2.1` branch nomi, «Releases / Tags: versiyalarni belgilash; deploy va rollback strategiyalari». SemVer qoidalari, `git tag` va `gh release` buyruqlari standart hujjatlardan qo'shildi.

**Vaqt taqsimoti (80 daqiqa):**
- Takrorlash: 10 daqiqa (16-dars: stash, rebase, cherry-pick, reflog)
- 01. Git taglar: 15 daqiqa
- 02. SemVer: 15 daqiqa
- Tanaffus: 5 daqiqa
- 03. GitHub Release: 15 daqiqa
- Amaliyot: 15 daqiqa
- Xulosa va tezkor nazorat: 5 daqiqa

---

## 1. Konspekt (mentor uchun)

### 1.1. git tag: commit ga doimiy nom
Branch doim harakatlanadi, **tag** esa aniq bir commit ga qo'yiladigan doimiy belgi, masalan `v1.0.0`. U «aynan shu holat — 1.0 versiya» deganini bildiradi. Ikki tur: **lightweight** (oddiy ko'rsatkich) va **annotated** (`-a`: muallif, sana va xabar saqlanadi; release uchun tavsiya etiladi). Taglar `git push` bilan o'z-o'zidan yuborilmaydi: `git push origin v1.0.0` yoki barchasi uchun `git push --tags`. Ro'yxat: `git tag -l`, tafsilot: `git show v1.0.0`. Oldingi versiyaga qaytish: `git switch --detach v1.0.0`.
```bash
git tag v0.9.0
git tag -a v1.0.0 -m "Birinchi barqaror versiya"
git tag -l
git show v1.0.0
git push origin v1.0.0
git tag -d v0.9.0
```
Tag ni push qilingan keyin o'zgartirmang yoki o'chirmang: boshqalar ham uni ishlatadi. Yangi tag yarating.

### 1.2. Semantik versiyalash (SemVer)
**SemVer** versiyani uch raqam bilan yozadi: **MAJOR.MINOR.PATCH**, masalan `2.4.1`. **PATCH** — eski ishlashni buzmaydigan xato tuzatish (`2.4.1` → `2.4.2`). **MINOR** — orqaga mos yangi imkoniyat (`2.4.1` → `2.5.0`, PATCH 0 ga tushadi). **MAJOR** — orqaga mos bo'lmagan o'zgarish (`2.4.1` → `3.0.0`). Pre-release: `1.0.0-rc.1` (release candidate), `1.0.0-beta.2`. Tag odatda `v` bilan boshlanadi: `v2.4.1`. Raqamlar boshqarish uchun emas, o'zgarish xarakterini jamoaga bildirish uchun.
```python
def bump(v, qism):
    major, minor, patch = map(int, v.split("."))
    if qism == "major":
        return f"{major + 1}.0.0"
    if qism == "minor":
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"

print(bump("2.4.1", "minor"))
```
MINOR oshganda PATCH 0 bo'ladi, MAJOR oshganda MINOR va PATCH 0 bo'ladi.

### 1.3. GitHub da release yaratish
**Release** — tag asosida GitHub da rasmiy nashr sahifasi: versiya nomi, o'zgarishlar tavsifi (release notes) va yuklab olinadigan fayllar. Veb: repozitoriy → **Releases** → **Draft a new release** → tag tanlash → Publish. Buyruq qatorida: **`gh release create v1.0.0 --title "1.0.0" --notes "..."`**. Release notes da yangi imkoniyatlar, tuzatilgan xatolar va buzuvchi o'zgarishlar yoziladi. Tag lar deploy va **rollback** (oldingi versiyaga qaytish) uchun tayanch nuqta: muammo chiqsa, oldingi tag ga qaytiladi. Pre-release uchun `--prerelease` bayrog'i.
```bash
git tag -a v1.0.0 -m "1.0.0"
git push origin v1.0.0
gh release create v1.0.0 --title "1.0.0" --notes "Birinchi barqaror versiya"
gh release list
```
`gh` ni birinchi marta `gh auth login` bilan ulash kerak. Release notes ni tag nomi emas, o'zgarishlar mazmuni bilan yozing.

---

## 2. Amaliy topshiriqlar va yechimlari

### 1-topshiriq (oson). Tag yarating
`v1.0.0` annotated tag ni xabar bilan yarating.

**Yechim:**
```bash
git tag -a v1.0.0 -m "Birinchi versiya"
```

### 2-topshiriq (oson). Tagni yuboring
Tag ni GitHub ga yuboring.

**Yechim:**
```bash
git push origin v1.0.0
```

### 3-topshiriq (o'rta). Versiya oshirish
`2.4.1` dan yangi imkoniyat qo'shilsa, qaysi versiya?

**Yechim:** 2.5.0 (MINOR oshadi, PATCH 0).

### 4-topshiriq (o'rta). Buzuvchi o'zgarish
`2.5.0` da API buzildi. Yangi versiya?

**Yechim:** 3.0.0 (MAJOR oshadi).

### 5-topshiriq (qiyin). Release
`gh` bilan `v1.0.0` release yarating.

**Yechim:**
```bash
gh release create v1.0.0 --title "1.0.0" --notes "Birinchi versiya"
```

### 6-topshiriq (qo'shimcha). Rollback
Oldingi `v0.9.0` ga qaytish yo'lini yozing.

**Yechim:** `git switch --detach v0.9.0` yoki shu tag dan deploy.

---

## 3. Tezkor nazorat
1. **Tag nima?** *Javob:* Commit ga doimiy belgi, masalan versiya.
2. **SemVer formati?** *Javob:* MAJOR.MINOR.PATCH.
3. **Xato tuzatilsa qaysi raqam oshadi?** *Javob:* PATCH.
4. **Tag qanday yuboriladi?** *Javob:* `git push origin <tag>` yoki `--tags`.
5. **Release nima?** *Javob:* Tag asosidagi GitHub nashr sahifasi.

## Mentor uchun eslatma
Mashqni faqat test repozitoriyda bajaring; haqiqiy loyihada tag larni o'chirmang. `gh` o'rnatilmagan bo'lsa, release ni veb orqali yarating. Hujjatda faqat `release` branch va «Releases / Tags» sarlavhasi bor; `git tag`, SemVer va `gh release` qoidalari standart manbalardan qo'shildi. SemVer 0.x versiyalar uchun qoidalar yumshoq: 1.0.0 dan oldin hammasi o'zgarishi mumkin. Keyingi dars: GitHub Flow va jamoaviy ishlash.
