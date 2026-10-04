# 6-dars. Code Review metodologiyasi, etikasi va Branch Protection

**Hafta:** 2 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliyot · **I-bob**, 6-dars (umumiy 6–51)

## 1. Dars rejasi

**Maqsad:** o'quvchi dasturiy ta'minot muhandisligida Code Review madaniyatini, professional diff tahlilini, reviewer va author o'rtasidagi muloqot etikasini, "Nitpick vs Blocker" farqini hamda GitHub Branch Protection qoidalarini amalda qo'llashni o'rganadi.

**Kutiladigan natija:**
- Code Review'ning 3 ta asosiy maqsadini (xatolarni erta tutish, bilim almashish, arxitektura barqarorligi) tushuntiradi.
- Konstruktiv sharh yozish etikasini ("odamni emas, kodni tahlil qilish", taklif va savol berish) biladi.
- Kritik xatolar (Blockers) bilan mayda maslahatlarni (Nitpicks) ajratadi.
- GitHub'dagi `Files changed` panelida inline sharhlar va bir bosishda qabul qilinuvchi **suggestion blocks** (````suggestion````) yozadi.
- PR'ga 3 xil yakuniy baho (Approve, Request Changes, Comment) berish mantig'ini tushunadi.
- GitHub repozitoriyasida `main` tarmog'i uchun Branch Protection Rules (kamida 1 ta approve, to'g'ridan-to'g'ri push taqiqlash) o'rnatadi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 | Takrorlash | 5-dars (Pull Request, What/Why/How, merge turlari, konfliktlar) |
| 10–30 | Yangi mavzu 1 | Code Review nima uchun kerak? Reviewer va Author etikasi |
| 30–40 | Yangi mavzu 2 | Diff tahlili, Nitpicking vs Blocker, GitHub taklif kodi (suggestion) |
| 40–45 | Tanaffus | |
| 45–55 | Yangi mavzu 3 | GitHub Branch Protection: main tarmog'ini qulflash |
| 55–75 | Amaliyot | Hamkasb kodi ustida review o'tkazish, suggestion yozish va Branch Protection sozlash |
| 75–80 | Tezkor nazorat va xulosa | 5 ta savol, 2-hafta yakuni |

---

## 2. Konspekt

### 2.1. Takrorlash (10 daqiqa)
- PR nima va nega unga dalil (skrinshot/log) qo'shish kerak?
- Squash and merge qanday ishlaydi?

### 2.2. Code Review nima va nega u dasturchining asosiy o'sish quroli?
**Code Review** — bu boshqa bir muhandis tomonidan yozilgan kodni asosiy tarmoqqa birlashtirishdan oldin sinchiklab o'qib chiqish, tahlil qilish va fikr bildirish jarayonidir.

Code Review nima uchun kerak?
1. **Xatolarni erta aniqlash:** Hatto eng kuchli dasturchi ham charchaganida oddiy xatolarga yo'l qo'yadi. Boshqa odamning yangi nigohi xatoni darhol ilg'aydi.
2. **Xavfsizlik (Security):** Kodda ochiq qolgan parollar, SQL inyeksiya xavfi yoki ruxsatsiz kirish teshiklarini to'sadi.
3. **Bilim almashish (Knowledge Sharing):** Jamoaning har bir a'zosi loyihaning boshqa qismlari qanday ishlayotganini bilib boradi. Yosh dasturchilar tajribali muhandislarning sharhlaridan eng tez o'rganadi.
4. **Kod tozaligi (Code Maintainability):** Loyihada yagona format va me'moriy uslub saqlanadi.

### 2.3. Code Review etikasi (Muloqot madaniyati)
Code Review — bu kim aqlliroq ekanini isbotlash musobaqasi EMAS! Yomon muloqot jamoani parokanda qilishi mumkin.

**Asosiy qoidalar:**
1. **Kodni tanqid qiling, shaxsni emas:**
   - ❌ Noto'g'ri: *"Sen bu yerda juda xunuk va sekin kod yozgansan."*
   - ✅ To'g'ri: *"Bu sikl katta ro'yxatlarda sekinlashishi mumkin. Keling, buni lug'at (hashmap) orqali O(1) tezlikka keltiramiz."*
2. **Buyruq bermang, savol bering va sabab keltiring:**
   - ❌ Noto'g'ri: *"Bu funksiyani 3 ga bo'l!"*
   - ✅ To'g'ri: *"Bu funksiya 80 qatordan oshib ketibdi. Uni testlash osonroq bo'lishi uchun 2 ta kichik yordamchi funksiyaga ajratsak qanday qaraysiz?"*
3. **Yaxshi yechimlarni ham maqtang:**
   - Review faqat xato topishdan iborat emas. Agar hamkasbingiz chiroyli va nafis algoritm yozgan bo'lsa: *"Ajoyib yechim, menga juda yoqdi!"* deb sharh qoldiring.

### 2.4. Nitpicking vs Blocker (Pashshadan fil yasamang!)
Reviewer har bir o'zgarishning darajasini to'g'ri ajrata bilishi kerak:

- **Blocker (Kritik xato — Qat'iy to'siq):**
  - Tizim qulashiga olib keluvchi xatolik;
  - Xavfsizlik zaifligi (masalan, token ochiq qolgan);
  - Biznes mantiq noto'g'ri ishlashi;
  - Testlar yo'qligi.
  - *Natija:* `Request changes` (tuzatmaguncha merge qilish taqiqlanadi!).

- **Nitpick (Mayda maslahat / Maydalashish):**
  - O'zgaruvchi nomini boshqacha atash;
  - Ortiqcha bitta bo'sh qator;
  - Shaxsiy ta'bga bog'liq mayda uslub.
  - *Qoida:* Sharh boshiga `nit:` yoki `ixtiyoriy:` deb yoziladi. Bu muallifning ixtiyorida qoladi va PR'ni to'xtatib turmasligi shart!

### 2.5. GitHub Review asboblari va Taklif kodi (Suggestion)
GitHub PR interfeysidagi `Files changed` bo'limida:
- Qator ustiga kursor olib borib, `+` tugmasini bosish orqali aynan o'sha qatorga sharh qoldiriladi.
- **Taklif kodi (Code Suggestion):** Sharh oynasidagi maxsus tugma orqali kod taklif qilish mumkin:
```markdown
```suggestion
def calculate_total(items):
    return sum(item.price for item in items)
```
```
Muallif ushbu taklifni ko'rganda, o'z kompyuterida kod yozib o'tirmasdan, GitHub'dagi **"Commit suggestion"** tugmasini bitta bosish orqali taklifni to'g'ridan-to'g'ri o'z branchiga commit qilib oladi!

**Review yakuni bo'yicha 3 ta qaror:**
1. `Comment` — shunchaki savollar berish (tasdiqlamaydi ham, bloklamaydi ham).
2. `Approve` — kod to'liq talabga javob beradi, mergaga ruxsat.
3. `Request changes` — jiddiy xatolar bor, qayta ishlab ko'rsatish talab qilinadi.

### 2.6. GitHub Branch Protection Rules
Jamoada hech kim (hatto jamoa sardori yoki loyiha egasi ham) xatolik bilan `main` tarmog'ini buzib qo'ymasligi uchun GitHub'da himoya qoidalari o'rnatiladi:
- `Settings → Branches → Add branch ruleset / protection rule`:
  1. **Branch name pattern:** `main`
  2. **Require a pull request before merging:** to'g'ridan-to'g'ri `git push origin main` qilish butunlay bloklanadi!
  3. **Require approvals:** kamida 1 nafar (yoki 2 nafar) boshqa muhandis `Approve` bosmaguncha "Merge" tugmasi nofaol bo'ladi.
  4. **Require status checks to pass:** avtomatlashtirilgan testlar (CI) muvaffaqiyatli o'tmaguncha merge qilish taqiqlanadi.

---

## 3. Amaliy topshiriqlar

### 1-topshiriq. Konstruktiv inline sharh yozish
Hamkasbingiz kodida quyidagi qatorni ko'rdingiz:
`sql = "SELECT * FROM users WHERE name = '" + user_input + "'"`
Unga xavfsizlik (SQL Injection) bo'yicha professional, konstruktiv va xushmuomala sharh matnini yozing.

**Yechim:**
```markdown
Ushbu so'rovda stringlarni to'g'ridan-to'g'ri qo'shish (concatenation) SQL Injection zaifligiga olib kelishi mumkin. Foydalanuvchi ma'lumotlari orqali bazani buzib kirmasliklari uchun parametrlangan so'rovlardan (prepared statements) foydalanishni taklif qilaman:

```suggestion
cursor.execute("SELECT * FROM users WHERE name = %s", (user_input,))
```
```

### 2-topshiriq. Branch Protection qoidalarini sozlash
GitHub repozitoriyangizda `main` tarmog'ini himoyalash qoidasini o'rnating: to'g'ridan-to'g'ri push qilishni taqiqlang va PR orqali kamida 1 ta approve talab qiling.

**Yechim:**
1. GitHub repoga kirish → `Settings` → chap menyudan `Branches`;
2. `Add classic branch protection rule` tugmasini bosish;
3. `Branch name pattern`: `main`;
4. `Require a pull request before merging` katakchasini yoqish;
5. `Require approvals`: 1 ta qilib belgilash;
6. `Save changes` tugmasini bosish.
*Natija:* Endi terminaldan `git push origin main` qilinsa, GitHub rad etadi: `remote: error: GH006: Protected branch update failed for refs/heads/main`.

### 3-topshiriq. Nitpick va Blocker tasnifi
Quyidagi 4 ta muammoni "Blocker" yoki "Nitpick" toifalariga ajrating:
1. API tokeni kod ichida ochiq yozilgan;
2. Funksiya argumenti nomi `x` deb atalgan, `user_count` deyilsa yaxshiroq bo'lardi;
3. Login funksiyasida bo'sh parol kiritilganda server 500 Internal Error berib qulaydi;
4. Qator oxirida ortiqcha 2 ta probel qolib ketgan.

**Yechim:**
- 1 va 3 — **Blocker** (xavfsizlik va server xatosi — tuzatish shart!).
- 2 va 4 — **Nitpick** (mayda uslubiy maslahat — ixtiyoriy, mergeni to'xtatmaydi).

---

## 4. Tezkor nazorat (5 daqiqa)

1. Code Review jarayonining jamoa uchun asosiy 3 ta foydasi nima?
   - **Javob:** Xatolarni erta tutish, xavfsizlikni ta'minlash va jamoada bilim/tajriba almashish.
2. Code Review etikasidagi "odamni emas, kodni baholash" qoidasini qanday tushunasiz?
   - **Javob:** Shaxsiy ayblash va haqoratlardan qochib, faqat texnik sabab va takliflar asosida xolis fikr bildirish.
3. "Nitpick" so'zi nimani bildiradi va u "Blocker"dan nimasi bilan farq qiladi?
   - **Javob:** Nitpick — kichik uslubiy maslahat bo'lib, u PR birlashishini to'xtatmaydi; Blocker esa xavfli xato bo'lib, tuzatilishi majburiy.
4. GitHub da code suggestion bloki qanday afzallik beradi?
   - **Javob:** Muallifga tayyor to'g'rilangan kodni taklif qiladi va uni bitta tugma bilan repoga commit qilib olish imkonini beradi.
5. Branch Protection Rules nima uchun kerak?
   - **Javob:** Asosiy tarmoqqa tasodifan yoki tekshirilmasdan xom kod push qilinishining oldini olish uchun.

---

## 5. Xulosa va keyingi darsga ko'prik
2-hafta davomida biz tarmoqlanish arxitekturasi, Conventional Commits, Pull Request madaniyati, konfliktlarni yechish, Code Review etikasi va Branch Protection qoidalarini to'liq o'zlashtirdik. Siz endi yirik IT-kompaniyalarda talab qilinadigan professional jamoaviy madaniyatga egasiz!
**Keyingi hafta (3-hafta, 7–8 darslar):** Kod sifati va arxitekturasining cho'qqisi — **Clean Code va SOLID tamoyillari** (SRP, OCP, LSP, ISP, DIP) bilan tanishamiz!
