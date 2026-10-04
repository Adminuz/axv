# 10-sinf (Advanced Android): 2-hafta baholash qaydnomasi

**Mavzular:**
1. Dependency management va ziddiyatlarni hal qilish: Tranzitiv bog'liqliklar, dependency tree tahlili, `exclude` va `resolutionStrategy`
2. ProGuard va R8 yordamida kodni optimallashtirish (1-qism): Shrinking, Obfuscation, Optimization, Resource Shrinking, `minifyEnabled`
3. ProGuard va R8 qoidalari bilan ishlash (2-qism: Amaliyot): `proguard-rules.pro`, `-keep` direktivalari, Gson/Moshi refleksiya muammolari, `mapping.txt`, `@Keep`

---

## Baholash mezonlari

| Mezon | Tavsif | Maks. ball |
|---|---|---|
| **Tranzitiv bog'liqliklar va Ziddiyatlar** | Dependency daraxtini terminal orqali chiqarish, to'qnash kelayotgan kutubxona versiyalarini aniqlash va `exclude` sintaksisini to'g'ri qo'llash | 30 ball |
| **R8 va Minifikatsiya Asoslari** | `minifyEnabled` va `shrinkResources` parametrlarini to'g'ri kiritish, APK Analyzer orqali hajm o'zgarishini solishtirish va R8 ishlash tamoyilini tushunish | 35 ball |
| **ProGuard Qoidalari va Himoya** | `proguard-rules.pro` faylida `-keep` direktivalarini to'g'ri yozish, `@Keep` annotatsiyasini qo'llash va `mapping.txt` orqali deobfuskatsiyani tushunish | 35 ball |
| **JAMI** | | **100 ball** |

---

## O'quvchilar natijalari jadvali

| № | O'quvchi F.I.Sh. | Ziddiyatlar & Exclude (30) | R8 & Minify (35) | ProGuard & Rules (35) | Jami ball (100) | Izoh |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |
| 9 | | | | | | |
| 10 | | | | | | |
| 11 | | | | | | |
| 12 | | | | | | |

---

## Mentor qaydlari va tahlil

- **Darsdagi asosiy qiyinchiliklar:** O'quvchilar ko'pincha `shrinkResources` parametrini `minifyEnabled true` qilmasdan ishlatishga urinishadi va Gradle xatolik beradi (`Resource shrinker requires code shrinker`). Shuningdek, model klasslariga `-keep` qo'yishda paket nomini to'liq yozmaslik tufayli release da crashlar yuzaga kelishi mumkin.
- **Tavsiya:** Amaliyot davomida har bir o'quvchiga ataylab DTO modeliga ega ilovani `minifyEnabled = true` bilan obfuskatsiya qildirib, crash berishini ko'rsatish, so'ngra birgalikda `proguard-rules.pro` fayliga qoida kiritib tuzatish jarayonini bajarish eng samarali metod hisoblanadi.
