# 1-hafta. Uyga vazifalar

Har bir vazifa 20–30 daqiqa. Parol, token, maxfiy kalit va shaxsiy ma'lumotlarni hech kimga yubormang va fayllarga yozmang: topshirishda faqat fayl yoki ochiq repo havolasi kerak.

## 1-dars uchun (IT ekotizimi va SDLC)
**1-topshiriq: «Portfolio-loyiha: talab»**
1. Darsda boshlagan `SRS-mini.md` faylini yakunlang. Unda bo'lishi kerak: bir jumlalik maqsad; 5 ta user story; har bir user story uchun kamida 2 ta qabul mezoni; «loyiha nimani qilmaydi» bo'limida 3 ta cheklov.
2. Qabul mezonlarini o'lchanadigan qilib yozing: «chiroyli», «tez» kabi mavhum so'zlar o'rniga son yoki tekshiriladigan shart yozing.
3. Sevimli ilovangizning 4 qatlamli xaritasini (klient, ilova, platforma, infratuzilma) toza chizing: har qatlamda kamida 2 ta komponent bo'lsin. Rasm yoki foto qiling.
4. Terminalda `git --version` buyrug'ini ishga tushiring va natijani tekshiring: keyingi darsda Git bilan ishlaymiz.

**Kutiladigan natija:** `SRS-mini.md` (5 user story, 10 dan ortiq o'lchanadigan qabul mezoni, 3 cheklov); ilova xaritasining rasmi; `git --version` versiya raqamini chiqaradi.
**Topshirish:** `SRS-mini.md` fayli, xarita rasmi va `git --version` natijasining skrinshoti yoki ko'chirilgan matni.

## 2-dars uchun (Git asoslari: commit, branch, merge)
**2-topshiriq: `dev-journal` ni boyiting**
1. `dev-journal` repozitoriyasida `.gitignore` faylini yarating. Unda kamida `.env` va `__pycache__/` qatorlari bo'lsin.
2. Uch kun uchun `notes/kun-1.md`, `notes/kun-2.md`, `notes/kun-3.md` yozuvlarini yozing. Har bir fayl alohida commit bo'lsin, xabarlar Conventional Commits uslubida (masalan, `docs: ...`).
3. `feature/skills` shoxini oching, unda bitta o'zgarish qiling va commit qiling, so'ng uni `main` ga merge qiling.
4. `git log --oneline --graph` natijasini `log.txt` fayliga saqlang va shu faylni ham commit qiling.

**Kutiladigan natija:** `git log` da 3 ta kunlik yozuv commiti, `.gitignore` commiti, merge va `log.txt` commiti ko'rinadi; grafikda `feature/skills` shoxi `main` ga qo'shilgani bilinadi; `git status` toza.
**Topshirish:** `log.txt` fayli va `git status` natijasi. Keyingi darsda bu repoz GitHub'ga yuklanadi.

## 3-dars uchun (GitHub)
**3-topshiriq: `dev-log` ni davom ettiring**
1. Darsda yaratgan `dev-log` repongizga yana 2 ta mazmunli commit qo'shing (masalan, `todo.py` ga yangi buyruq va `README.md` ni yaxshilash). Commit xabari nima o'zgarganini aniq aytsin.
2. GitHub'da bitta Issue oching va uni commit xabaridagi `Closes #N` (o'z Issue raqamingiz) orqali yoping.
3. O'zgarishlarni `git push` bilan GitHub'ga yuboring va repo ochiq (public) ekanini tekshiring.
4. Repo havolasini mentorga yuboring.

**Kutiladigan natija:** GitHub'dagi `dev-log` da yangi 2 ta commit; Issue `Closed` holatida va uni yopgan commitga havola bor; `README.md` va `.gitignore` joyida; repo havolasi brauzerda (kirmasdan) ochiladi.
**Topshirish:** faqat ochiq repo havolasi (`https://github.com/<nom>/dev-log`). Parol, token yoki kalit yubormang.

## Mentor uchun
- 1-dars: mavhum mezonlarni («tez», «qulay») qaytaring, son va tekshiriladigan shart so'rang. Xaritada komponent noto'g'ri qatlamga qo'yilgan bo'lsa (masalan, DB klientda), tuzatishni o'quvchining o'ziga topdiring.
- 2-dars: `log.txt` da grafik (`*`, `|`) haqiqatan bor-yo'qligini va commit xabarlari uslubini tekshiring. Hash'lar har kimda boshqacha bo'lishi tabiiy. Merge fast-forward bo'lsa, grafik tekis chiqadi: bu xato emas, lekin shox mavjudligini `git branch` yoki xabarlardan tekshiring.
- 3-dars: havolani brauzerda oching, Issue yopilgan-yopilmaganini va yopgan commitni ko'ring. `.env`, kalit yoki token repoga tushib qolmaganini tekshiring; tushgan bo'lsa, darhol kalitni almashtirishni va tarixdan tozalashni tushuntiring. Parol/tokenni so'ramang.
- Keyingi dars boshida (10 daqiqa) 1–2 ta ishni ekranda ko'rib chiqing, xatolarni o'quvchining o'zi topsin.
- Kechikkan yoki to'liq bo'lmagan vazifani rad etmang: nima yetishmasligini aytib, qayta topshirishga imkon bering va baholashda dinamikani yozib boring.
