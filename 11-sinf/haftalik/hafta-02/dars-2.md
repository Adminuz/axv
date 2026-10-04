# 5-dars. Pull Request (PR) madaniyati, PR shabloni va Merge konfliktlar

**Hafta:** 2 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + chuqur amaliyot · **I-bob**, 5-dars (umumiy 5–51)

## 1. Dars rejasi

**Maqsad:** o'quvchi GitHub platformasida professional Pull Request (PR) ochishni, PR shabloni (`pull_request_template.md`) va checklistdan foydalanishni, What/Why/How strukturasi bilan dalillashni, turli xil merge strategiyalarini (Merge commit, Squash, Rebase) hamda muqarrar merge konfliktlarni mustaqil yechishni o'rganadi.

**Kutiladigan natija:**
- Pull Request tushunchasini va uning jamoaviy sifat nazoratidagi o'rnini tushuntiradi.
- `.github/pull_request_template.md` shablonini yaratadi va undan foydalanadi.
- PR tavsifida What, Why, How bloklarini hamda Issues bog'lanishini (`Closes #issue`) to'g'ri yozadi.
- 3 ta merge strategiyasining (Create a merge commit, Squash and merge, Rebase and merge) farqi va afzalliklarini biladi.
- Sun'iy yaratilgan merge konfliktni terminal va VS Code da tahlil qilib, to'g'ri hal etadi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 | Takrorlash | 4-dars (Branching, GitHub Flow, Conventional Commits) |
| 10–30 | Yangi mavzu 1 | Pull Request nima? PR anatomiyasi: What, Why, How, dalillar |
| 30–40 | Yangi mavzu 2 | PR shabloni (`.github/pull_request_template.md`) va Checklist |
| 40–45 | Tanaffus | |
| 45–55 | Yangi mavzu 3 | Merge strategiyalari va Merge Conflict mexanikasi |
| 55–75 | Amaliyot | GitHubda PR ochish, konflikt yuzaga keltirish va uni VS Code da yechish |
| 75–80 | Tezkor nazorat va xulosa | 5 ta savol, 6-darsga ko'prik |

---

## 2. Konspekt

### 2.1. Takrorlash (10 daqiqa)
- Nima uchun yangi kod har doim alohida tarmoqda yoziladi?
- `git switch -c feat/my-feature` qanday vazifani bajaradi?
- Conventional commitning asosiy qismlari nimalardan iborat?

### 2.2. Pull Request (PR) nima?
**Pull Request (PR)** — dasturchi o'z tarmog'ida yozgan o'zgarishlarni asosiy (`main`) tarmoqqa birlashtirishni so'rab jamoaga yuboradigan rasmiy taklifidir.

PR shunchaki kod birlashtirish tugmasi emas. Bu:
1. **Muhokama maydoni:** Jamoa a'zolari kodni ko'rib chiqadi, savollar beradi, optimallashtirish taklif qiladi.
2. **Sifat eshigi:** Avtomatlashtirilgan testlar (CI), linterlar va xavfsizlik skanerlari ishga tushadi.
3. **Loyiha tarixi:** Nega aynan shu o'zgarish kiritilganligi kelajakdagi muhandislar uchun abadiy hujjat bo'lib saqlanadi.

### 2.3. Professional PR anatomiyasi (What / Why / How)
Yaxshi muhandis hech qachon bo'sh yoki "kod yozdim" degan tavsif bilan PR ochmaydi. Professional PR quyidagi 3 ta savolga aniq javob beradi:

1. **Why? (Nima uchun bu o'zgarish kerak?):**
   - Muammo nima edi? Qaysi talab yoki Issue yopilmoqda?
   - `Closes #14` yoki `Fixes #25` (bu yozuv PR merge bo'lganda GitHub'dagi Issue'ni avtomatik yopadi).
2. **What? (Aynan nimalar o'zgartirildi?):**
   - Asosiy o'zgarishlarning qisqa punktlari (bullet points).
3. **How? (Qanday yechildi?):**
   - Arxitektura qarori, tanlangan algoritm yoki ma'lumotlar bazasidagi o'zgarishlar.
4. **Screenshots / Evidence (Dalillar):**
   - Agar UI o'zgargan bo'lsa — "Oldin / Keyin" skrinshoti yoki GIF;
   - Agar backend/API bo'lsa — terminal logi yoki muvaffaqiyatli test skrinshoti.

### 2.4. PR shabloni (`pull_request_template.md`)
Har bir dasturchi bir xil standartda ma'lumot qoldirishi uchun repository ildizida `.github/pull_request_template.md` fayli yaratiladi:

```markdown
## Tavsif (Description)
<!-- Ushbu PR nima qiladi? -->

## Nima uchun kerak? (Why)
<!-- Qaysi Issue hal qilinmoqda? Masalan: Closes #12 -->

## Asosiy o'zgarishlar (Key Changes)
- 
- 

## Tekshiruv ro'yxati (Checklist)
- [ ] Kod uslubi (linter) tekshirildi
- [ ] Yangi funksiya uchun testlar yozildi
- [ ] Lokal muhitda barcha testlar muvaffaqiyatli o'tdi
- [ ] Kerakli hujjatlar (README) yangilandi
- [ ] Maxfiy ma'lumotlar (.env, tokenlar) yo'qligi tekshirildi
```

### 2.5. Merge strategiyalari (Uch xil yo'l)
GitHub'da "Merge pull request" tugmasi ostida 3 ta variant mavjud:

1. **Create a merge commit (Oddiy merge):**
   - Barcha alohida commitlar o'zgarishsiz saqlanadi va tepadan bitta maxsus `Merge branch ...` commiti hosil bo'ladi.
   - *Afzalligi:* Tarix 100% to'liq saqlanadi.
   - *Kamchiligi:* Katta jamoalarda tarix juda chalkash va chigal bo'lib ketadi.
2. **Squash and merge (Siqish va birlashtirish — eng mashhuri!):**
   - Feature branchdagi barcha (masalan, 10 ta kichik) commitlar bitta yagona toza commitga birlashtiriladi va `main` ga yoziladi.
   - *Afzalligi:* Asosiy tarmoq tarixi nihoyatda toza va chiziqli bo'ladi.
3. **Rebase and merge:**
   - Commitlar birma-bir `main` ning eng oxiriga ko'chirib ulanadi. Merge commiti hosil bo'lmaydi.

### 2.6. Merge Conflict (Konflikt) mexanikasi
Konflikt — bu fojea emas, balki Git ning ikkita ziddiyatli o'zgarishni ko'rgandagi **yordam so'rashidir**.
Qachon sodir bo'ladi?
Agar ikkita tarmoqda bitta faylning aynan bir xil qatori ikki xil qilib o'zgartirilsa, Git qaysi biri to'g'riligini o'zi hal qilolmaydi va konflikt e'lon qiladi:

```text
<<<<<<< HEAD (Joriy tarmoq - main)
def get_user_name(user_id):
    return db.users.find_one({"id": user_id})["full_name"]
=======
def get_user_name(user_id):
    return cache.get(user_id) or "Mehmon"
>>>>>>> feat/cache-users (Kelingan tarmoq)
```

**Konfliktni hal qilish:**
1. Dasturchi VS Code yoki muharrirda qaraydi;
2. `<<<<<<<`, `=======`, `>>>>>>>` belgilarini va keraksiz kodni qo'lda o'chiradi;
3. Ikkala mantiqni to'g'ri birlashtiradi;
4. `git add <fayl>` va `git commit` qilib konfliktni yakunlaydi.

---

## 3. Amaliy topshiriqlar

### 1-topshiriq. PR shablonini yaratish
Loyihangizda `.github` papkasi ochib, uning ichida `pull_request_template.md` shablonini yarating va GitHub'ga push qiling.

**Yechim:**
```bash
mkdir -p .github
cat << 'EOF' > .github/pull_request_template.md
## Tavsif
<!-- Nima o'zgardi? -->

## Sababi
<!-- Closes #... -->

## Checklist
- [ ] Kod tekshirildi
- [ ] Testlar o'tdi
EOF

git add .github/pull_request_template.md
git commit -m "chore(github): add pull request template"
git push origin main
```

### 2-topshiriq. Merge konflikt laboratoriyasi
Lokalda ataylab konflikt hosil qiling va uni hal qiling:

**Yechim:**
```bash
# 1. main da fayl yaratish
echo "Versiya 1.0 - Asosiy qator" > app.txt
git add app.txt && git commit -m "chore: initial app.txt"

# 2. Yangi branch ochib, birinchi qatorni o'zgartirish
git switch -c feat/update-text
echo "Versiya 2.0 - Feature tarmog'i varianti" > app.txt
git commit -am "feat: update line from feature branch"

# 3. main ga qaytib, o'sha qatorni boshqacha o'zgartirish
git switch main
echo "Versiya 1.5 - Main tarmog'i yangilanishi" > app.txt
git commit -am "fix: hotfix on main branch"

# 4. Mergeni sinab ko'rish -> KONFLIKT!
git merge feat/update-text
# Chiqish: CONFLICT (content): Merge conflict in app.txt
# Automatic merge failed; fix conflicts and then commit the result.

# 5. Faylni ochib konfliktni tuzatish
echo "Versiya 2.0 - Main va Feature kelishuvi" > app.txt

# 6. Mergeni yakunlash
git add app.txt
git commit -m "merge: resolve conflict between main and feat/update-text"
```

---

## 4. Tezkor nazorat (5 daqiqa)

1. Pull Request nima va u to'g'ridan-to'g'ri push qilishdan qanday afzalliklarga ega?
   - **Javob:** PR kodni asosiy tarmoqqa qo'shishdan oldin jamoaviy ko'rib chiqish (review) va avtomatlashtirilgan testlar orqali sifatni ta'minlovchi taklifdir.
2. PR tavsifida `Closes #15` yozish nimaga olib keladi?
   - **Javob:** PR asosiy tarmoqqa merge qilinganda 15-raqamli Issue avtomatik tarzda yopiladi.
3. Squash and merge strategiyasining asosiy ustunligi nimada?
   - **Javob:** Feature branchdagi ko'plab oraliq commitlarni bitta toza commitga birlashtirib, asosiy tarmoq tarixini tartibli saqlaydi.
4. Git merge conflict qanday holatda yuzaga keladi?
   - **Javob:** Bitta faylning bir xil qatoriga ikkita turli tarmoqda bir vaqtda ziddiyatli o'zgartirishlar kiritilganda.
5. `.github/pull_request_template.md` fayli nima uchun xizmat qiladi?
   - **Javob:** GitHub'da yangi PR ochilganda tavsif oynasiga avtomatik ravishda yagona standartdagi checklist va savollarni chiqarib berish uchun.

---

## 5. Xulosa va keyingi darsga ko'prik
Bugun biz Pull Request madaniyati, shablonlar va merge konfliktlarni mustaqil yechishni o'rgandik.
**Keyingi dars (6-dars):** Ochilgan PR larni professional tahlil qilish — **Code Review metodologiyasi va etikasi**, inline sharhlar, taklif kodi va GitHub Branch Protection qoidalarini o'rganamiz!
