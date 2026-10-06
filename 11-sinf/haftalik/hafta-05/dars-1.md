# 13-dars. Muloqot va jamoada ishlash ko'nikmalari

**Hafta:** 5 · **Davomiyligi:** 80 daqiqa · **Turi:** ma'ruza + amaliyot · **I-bob**, 13-dars (umumiy 1–51)

**Manba:** O'quv qo'llanma, I bob, «Muloqot va jamoada ishlash ko'nikmalari» ma'ruzasi (1.18–1.22-jadvallar, ADR 1.21-jadval); o'quv dasturi, shu mavzu natijalari (faol tinglash, SBI, PR/issue yozish, meeting etikasi, RACI).

## 1. Dars rejasi

**Maqsad:** O'quvchi professional muloqotning asosiy ko'nikmalarini (faol tinglash, aniqlashtiruvchi savol, «I-xabar», SBI) qo'llaydi; yozma xabar va PR tavsifini kontekst, tuzilma, yakun bo'yicha yozadi; jamoada rol va mas'uliyat, psixologik xavfsizlik, mini-retro, nizoni boshqarish va masofaviy ish qoidalarini biladi.

**Kutiladigan natija:**
- Faol tinglash bosqichlarini aytadi va «qayta ifodalash + aniqlashtiruvchi savol» misolini yozadi.
- «I-xabar» (holat, ta'sir, so'rov) va SBI formulasi bilan fikr bildiradi.
- Xabar va PR tavsifini kontekst, tuzilma va yakun (keyingi qadamlar) bilan yozadi.
- Nizoni «muammo, ta'sir, variantlar, qaror» tuzilmasi bilan boshqaradi va 15 daqiqalik mini-retro o'tkazadi.

**Kerakli jihozlar:**
- Kompyuter va matn muharriri (yoki daftar)
- GitHub hisobi (PR tavsifi shablonini sinash uchun)
- Proyektor/monitor; zaxira: A4 qog'oz va qalam

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va kirish | 12-dars: JSON kontrakti, yagona xato formati |
| 10–35 daq | Yangi mavzu | Faol tinglash, aniqlashtiruvchi savol, «I-xabar»; Yozma muloqot: kontekst, tuzilma, yakun; PR tavsifi; Jamoa: rollar, psixologik xavfsizlik, mini-retro, nizo, masofaviy ish |
| 35–40 daq | Tanaffus | Harakatli tanaffus + mini-quiz |
| 40–65 daq | Amaliyot | Mini-retro va PR tavsifini yozish |
| 65–75 daq | Tezkor nazorat | 5 ta savol |
| 75–80 daq | Xulosa va uyga vazifa | Pr tavsifi va mini-retro yozuvi |

---

## 2. Dars konspekti

### 2.1. Faol tinglash, savol va «I-xabar»

Dasturchining qiymati faqat yozgan kodi bilan o'lchanmaydi: u Product Owner, dizayner, QA va mijozdan to'g'ri ma'lumot olishi, aniqlik kiritishi va kelishuv tuzishi kerak. **Faol tinglash** — suhbatdosh fikrini eshitib, qayta ifodalab tekshirish. **Aniqlashtiruvchi savol** ochiq bo'ladi: «Qaysi qurilma siz uchun eng muhim?». **«I-xabar»** tanqidni shaxsga emas, vaziyatga qaratadi: holat, ta'sir, so'rov. SBI modeli ham shunday: Situation, Behavior, Impact. Auditoriyaga mos gapiring: menejerga risk va natija, muhandisga diagramma, log va metrika bilan.

«Sen doim kechikasan» emas, «Kecha 3 PR kechikdi, bu relizni surdi» deb yozing: faktga qarating, shaxsga emas.

### 2.2. Yozma xabar va PR tavsifi

Yozma muloqot (chat, email, Jira, PR) uchta mezonga tayanadi. **Kontekst** — nima haqida va nima sababdan yozayotganingiz, 1–2 gapda. **Tuzilma** — ro'yxat va punktlar, havolalar (Figma, ticket, commit SHA). **Yakun** — keyingi qadam, owner va deadline. O'quv dasturi PR/issue/sprint yozuvlari uchun What/Why/How tuzilmasini beradi. Masofaviy ishda xabar kimga, nima haqida va qachongacha degan savollarga darrov javob bersin. «Ok?» o'rniga «Tasdiqlaysizmi?» deb aniq savol qo'ying.

Yomon xabar: «Endpointni o'zgartirdim, qarang.» Yaxshi xabarda kontekst, ro'yxat va yakun bor.

### 2.3. Rollar, mini-retro, nizo va masofaviy ish

Samarali jamoa uch narsaga tayanadi: **rol va mas'uliyat** (har kim «mening vazifam nima?» ga javob beradi: PO — biznes qiymat, Tech Lead — arxitektura, QA — sifat, Dev — implementatsiya), **psixologik xavfsizlik** (savol berish va xatoni tan olish jazolanmaydi) va **feedback ritmi** (haftalik mini-retro). Nizo — tabiiy holat: uni muammo, ta'sir, variantlar, qaror tuzilmasi bilan hal qiling, qarorni esa ADR da yozing. Masofaviy ishda: kontekstli yozma xabar, aniq kun tartibli uchrashuv, yagona hujjat makoni.

Har retro 1–2 action chiqarsin, har biriga owner va deadline qo'ying: SMART bo'lmasa, bajarilmaydi.

### 2.4. Namunalar

Kontekstli yozma xabar (masofaviy ish):

```text
Kimga: @Design
Muammo: «Pay» tugmasi iOS da 1px pastga tushib qolmoqda
Kontekst: iPhone 13, Checkout sahifasi
Artefakt: Figma link, screenshot
Deadline: bugun 17:00
Savol: Tasdiqlaysizmi?
```

Mini-retro yozuvi:

```text
Nima ishladi: kichik PR lar tez review bo'ldi
To'sqinlik: build vaqti 6 daqiqaga uzaydi
Action 1: keshni sozlash (owner: Ali, deadline: juma)
Action 2: PR hajmi <= 300 qator (owner: jamoa, boshlanishi: dushanba)
```

## 3. Amaliy mashg'ulot

### 1-mashq (oson). Qayta ifodalash
**Vazifa:** Hamkasbingiz: «Login sahifasi sekin». Faol tinglash bilan qayta ifodalang va 1 ta aniqlashtiruvchi savol bering.

**Kutiladigan natija:** Qayta ifodalash va ochiq savol.

**Yechim:** «To'g'ri tushundimmi, login sahifasi yuklanishi sekin? Qaysi qurilma va tarmoqda?»

### 2-mashq (o'rta). I-xabar
**Vazifa:** Hamkasbingiz PR ni 3 kun review qilmadi. «I-xabar» formulasi bilan xabar yozing.

**Kutiladigan natija:** Holat, ta'sir, so'rov bor; ayblov yo'q.

**Yechim:** «Bu PR 3 kundan beri kutyapti (holat), shu sabab keyingi vazifa boshlanmadi (ta'sir). Bugun 16:00 gacha ko'rib chiqa olasizmi? (so'rov)»

### 3-mashq (qiyin). PR tavsifi
**Vazifa:** Kutubxona API uchun `error envelope` qo'shilganini What/Why/How va keyingi qadam bilan yozing.

**Kutiladigan natija:** To'liq tavsif.

**Yechim:** What: yagona xato formati. Why: mijoz xatoni bir xil qayta ishlaydi. How: `make_error()` va testlar. Keyingi qadam: mentor review, deadline: ertaga.

### 4-mashq (bonus). Nizo ssenariysi
**Vazifa:** «Monolit yoki mikroxizmat?» bahsini muammo, ta'sir, variantlar, qaror tuzilmasida yozing.

**Kutiladigan natija:** 4 qadamli yozuv, metrika bilan.

**Yechim:** Qaror metrikaga tayanadi: PR review sikl vaqti, P95 kechikish, xatolar ulushi.

## 4. Tezkor savollar

1. Faol tinglash nima?
   - **Javob:** Suhbatdosh fikrini eshitib, qayta ifodalab tekshirish.
2. «I-xabar» tuzilishi?
   - **Javob:** Holat, ta'sir, so'rov.
3. Yozma xabarning uch mezoni?
   - **Javob:** Kontekst, tuzilma, yakun.
4. PR tavsifi bo'limlari?
   - **Javob:** What, Why, How va keyingi qadam.
5. Psixologik xavfsizlik nima?
   - **Javob:** Savol berish va xatoni tan olish jazolanmaydigan muhit.

## 5. Mentor uchun eslatmalar

- Qo'llanmada 1.18–1.22-jadvallar bor; kod yo'q, shuning uchun amaliyot matn yozish mashqlari bilan o'tadi.
- Bitta o'quvchi bilan «mini-retro» rolli o'yin: o'quvchi va mentor ikki rolni almashadi.
- PR tavsifi shablonini o'quvchining portfolio repozitoriysida `.github/pull_request_template.md` sifatida saqlash mumkin.
- O'quvchining real GitHub PR i bo'lsa, shuni tahlil qiling.
- Keng tarqalgan xatolar: Kontekstsiz xabar: «qarang», «ok?»; Tanqidni shaxsga qaratish («sen doim...»); Uzun matnni bitta paragraf qilib yozish; Yakun, owner va deadline qo'ymaslik.
