# 2-hafta. Uyga vazifalar

Har bir vazifa 20–30 daqiqa. Parol, shaxsiy token, maxfiy kalit va shaxsiy ma'lumotlarni repozitoriyga yozmang: topshirishda faqat ochiq GitHub repo yoki Pull Request havolasi kerak.

## 4-dars uchun (Branching va Conventional Commits)
**1-topshiriq: «GitHub Flow va Semantik commitlar»**
1. O'z portfolio repozitoriyangizda `feature/user-profile` nomli yangi tarmoq oching.
2. Kamida 3 ta mustaqil commit qiling. Commit xabarlari qat'iy **Conventional Commits** spetsifikatsiyasi asosida bo'lsin:
   - `feat(profile): add avatar upload and bio field`
   - `fix(profile): validate image file format and max size`
   - `docs(readme): document profile setup and requirements`
3. Terminalda `git log --oneline --graph` buyrug'ini ishga tushiring va xabarlar aniq, semantik tartibda chiqqanini tekshiring.
4. Ushbu branch'ni GitHub'ga push qiling (`git push -u origin feature/user-profile`).

**Kutiladigan natija:** GitHub'da yangi `feature/user-profile` tarmog'i mavjud; commit xabarlari standart talablariga to'liq javob beradi.  
**Topshirish:** GitHub tarmog'i havolasi yoki commitlar tarixi skrinshoti.

---

## 5-dars uchun (Pull Request va Merge Konfliktlari)
**2-topshiriq: «Mukammal PR va sun'iy konfliktni yechish»**
1. `feature/user-profile` tarmog'idan `main` tarmog'iga qarab rasmiy Pull Request oching.
2. PR tavsifini **What / Why / How** professional shabloni bo'yicha to'ldiring:
   - **What:** Qanday o'zgarishlar kiritildi?
   - **Why:** Bu o'zgarish nima uchun kerak (muammo yoki vazifa)?
   - **How:** Texnik yechim qanday amalga oshirildi?
   - Skrinshot yoki test natijasi ilova qiling.
3. Ataylab merge konflikti hosil qiling: `main` da ham, `feature/user-profile` da ham bitta faylning ayni bir qatorini o'zgartirib commit qiling.
4. Konflikt belgilarini (`<<<<<<<`, `=======`, `>>>>>>>`) o'chirib, toza yechimni saqlang va commit qilib PR ni yangilang.

**Kutiladigan natija:** Tavsifi to'liq, skrinshotli, nizosiz (Able to merge) yashil holatdagi Pull Request.  
**Topshirish:** GitHub Pull Request havolasi.

---

## 6-dars uchun (Code Review va Branch Protection)
**3-topshiriq: «Branch Protection va Taklif kodi»**
1. Repozitoriyangiz sozlamalariga kiring (`Settings → Branches`) va `main` tarmog'i uchun himoya qoidasini yoqing:
   - `Require a pull request before merging` (to'g'ridan-to'g'ri push taqiqlansin);
   - `Require approvals: 1` (kamida 1 ta tasdiq talab qilinsin).
2. Terminalda `main` tarmog'ida turib to'g'ridan-to'g'ri push qilib ko'ring va `GH006: Protected branch` xatoligini oling.
3. Do'stingiz (yoki mentor) ochgan PR ga kiring:
   - Kod diff'idan bitta qatorni tanlab inline sharh qoldiring;
   - Kamida 1 ta ````suggestion```` bloki orqali to'g'rilangan kod taklifini taqdim eting;
   - Agar xatolik bo'lmasa `Approve`, aks holda `Request changes` tugmasini bosing.

**Kutiladigan natija:** `main` tarmog'i himoyalangan, to'g'ridan-to'g'ri push bloklanadi; PR sahifasida konstruktiv inline sharh va bir bosishda qabul qilinuvchi code suggestion mavjud.  
**Topshirish:** Sozlangan Branch Protection sahifasi skrinshoti va yozilgan review/suggestion havolasi (yoki skrinshoti).

---

## Mentor uchun
- **4-dars bo'yicha tekshiruv:** Commit xabarlari `type(scope): description` formatida ekanini, fe'l hozirgi zamonda (masalan, `add` o'rniga `added` emas) va kichik harflar bilan yozilganini tekshiring.
- **5-dars bo'yicha tekshiruv:** O'quvchi PR tavsifini bo'sh qoldirmaganligini tekshiring. Konflikt yechilgandan so'ng kodda Git qoldiqlari (`<<<<<<< HEAD`, `=======`) qolib ketmaganiga ishonch hosil qiling.
- **6-dars bo'yicha tekshiruv:** Branch Protection haqiqatan ishlashini o'zingiz tekshiring (o'quvchi repoga to'g'ridan-to'g'ri push qila olmasligi kerak). O'quvchi yozgan sharh konstruktiv, hurmatli va shaxsiyatga tegmaydigan shaklda ekanini baholang.
- Hafta yakunida o'quvchining jamoaviy madaniyati va Git ko'nikmalari o'sish dinamikasini `baholash.md` jadvaliga kiriting.
