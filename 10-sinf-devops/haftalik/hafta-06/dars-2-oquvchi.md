# 17-dars. Git taglar va versiyalash: semantik versiyalash (SemVer), release yaratish

> Loyiha tayyor bo'lganda nima uchun «v1.0.0» deb yozamiz? Bugun taglar, SemVer va release larni o'rganamiz.

## Dars xulosasi

- Tag commit ga doimiy belgi qo'yadi.
- Annotated tag (`-a`) xabar va muallifni saqlaydi.
- Tag `git push origin <tag>` bilan yuboriladi.
- SemVer: MAJOR.MINOR.PATCH.
- Xato — PATCH, yangi imkoniyat — MINOR, buzuvchi o'zgarish — MAJOR.
- GitHub Release tag asosida nashr yaratadi.

## Qo'shimcha ma'lumot

### Pre-release
`1.0.0-rc.1` kabi sinov versiyalar.

### Rollback
Muammo chiqsa, oldingi tag ga qaytish.

### --tags
Barcha lokal tag larni yuboradi.

### 0.x
Birinchi barqaror versiyadan oldingi davr.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| tag | Commit belgisi |
| annotated | Xabar bilan tag |
| SemVer | Semantik versiyalash |
| MAJOR | Buzuvchi o'zgarish raqami |
| MINOR | Yangi imkoniyat raqami |
| PATCH | Xato tuzatish raqami |
| Release | Nashr sahifasi |
| Rollback | Oldingi versiyaga qaytish |

## Bilasizmi?

- SemVer rasmiy sayti: semver.org.
- Ko'p loyihalar release larni CI da avtomatik yaratadi (keyingi haftalarda GitHub Actions).
- Tag nomi `v` bilan yoki `v` siz bo'lishi mumkin, lekin jamoada bir xil bo'lishi kerak.

## Topshiriqlar

### 1. Tag yaratish · oson

`v1.0.0` annotated tag yarating.

**Kutiladigan natija:** `git tag -a v1.0.0 -m`.

### 2. Tagni ko'rish · oson

Barcha taglarni ro'yxatlang.

**Kutiladigan natija:** `git tag -l`.

### 3. SemVer qismlari · oson

MAJOR, MINOR, PATCH nimani bildiradi?

**Kutiladigan natija:** Buzuvchi, yangi, tuzatish.

### 4. Tagni yuborish · oson

Tagni GitHub ga yuboring.

**Kutiladigan natija:** `git push origin v1.0.0`.

### 5. Versiyani toping · o'rta

`1.4.2` + yangi imkoniyat = ?

**Kutiladigan natija:** 1.5.0.

### 6. Versiyani toping 2 · o'rta

`1.5.0` + API buzildi = ?

**Kutiladigan natija:** 2.0.0.

### 7. Tag turlari · o'rta

Lightweight va annotated farqi?

**Kutiladigan natija:** Annotated xabar va muallif saqlaydi.

### 8. Pre-release · o'rta

`2.0.0` ning sinov versiyasini yozing.

**Kutiladigan natija:** `2.0.0-rc.1`.

### 9. Release yaratish · qiyin

`gh` bilan release yarating.

**Kutiladigan natija:** `gh release create`.

### 10. Rollback · qiyin

Muammoli release dan oldingi versiyaga qanday qaytasiz?

**Kutiladigan natija:** Oldingi tag dan deploy qilish.

### 11. Release notes · qiyin

3 bo'limli release notes shablonini yozing.

**Kutiladigan natija:** Yangi, tuzatilgan, buzuvchi.

### 12. Avtomat · bonus

`bump` funksiyasiga `patch` ni qo'shing va 3 holat bilan sinang.

**Kutiladigan natija:** To'g'ri ishlaydigan funksiya.

## O'zingizni tekshiring

1. Tag nima?
2. SemVer formati?
3. Xato tuzatilsa qaysi raqam oshadi?
4. Tag qanday yuboriladi?
5. Annotated tag farqi?
6. Release nima?

## Uyga vazifa

Tag va release yarating (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
