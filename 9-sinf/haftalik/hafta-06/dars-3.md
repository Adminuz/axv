# 18-dars. Jamoaviy ishlash va Dev Mode: sharh, versiya tarixi va dizaynni dasturchiga topshirish

**Fan:** UX/UI dizayn va Advanced Front-end
**Sinf:** 9-sinf
**Hafta:** 6-hafta, 3-dars (umumiy 18-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** Uslubiy ko'rsatma, II bob, 2.1 «Figma'da interfeys dizayni»: «Jamoaviy ishlash va Dev Mode funksiyalari»; «Figma ishlab chiquvchilar uchun Developer Handoff rejimini taqdim etadi: obyektlarning masofalari va o'lchamlarini aniqlash, elementlarning CSS uslublari va kodlarini Android va iOS uchun nusxalash»; hamkorlik sabablari: kross-platforma, bulut xizmati, fikr-mulohaza. Dev Mode ning to'liq imkoniyatlari tarifga bog'liq.

---

## Darsning maqsadi

O'quvchilarga Figma'da fayl ulashishni (view/edit ruxsatlari), sharh qoldirish va javob berishni, versiya tarixidan foydalanishni, Dev Mode (Developer Handoff) orqali o'lcham, masofa, rang va CSS qiymatlarini olishni hamda dizaynni dasturchiga topshirish ro'yxatini (nomlash, komponent, eksport) o'rgatish.

## Kutiladigan natija

- Faylni view yoki edit ruxsati bilan ulashadi va nega ruxsat cheklanishini tushuntiradi;
- Dizayn bo'yicha sharh qoldiradi, javob beradi va hal qilingan deb belgilaydi;
- Versiya tarixidan oldingi holatni topadi;
- Dev Mode'da o'lcham, masofa, rang va CSS qiymatlarini oladi;
- Dizaynni dasturchiga topshirish ro'yxatini (handoff checklist) bajaradi.

## Kerakli jihozlar

- Kompyuter va Figma
- 17-darsdagi komponentli «E-kutubxona» fayli
- Juft bo'lib ishlash: sinfdosh bilan fayl almashinuvi

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 00–08 | Takrorlash | 17-dars: komponentlar va variantlar |
| 08–22 | Yangi mavzu 1 | Ulashish va ruxsatlar |
| 22–32 | Yangi mavzu 2 | Sharhlar va versiya tarixi |
| 32–38 | Tanaffus + mini-quiz | Slayddagi `.quiz` |
| 38–50 | Yangi mavzu 3 | Dev Mode: qiymatlarni olish va CSS |
| 50–75 | Amaliyot | Handoff ro'yxati, xulosa |
| 75–80 | Xulosa | Tezkor nazorat, uyga vazifa |

---

## Konspekt (mentor aytadigan matn)

### 1. Ulashish, ruxsatlar va hamkorlik

Figma — butun jamoa uchun yagona muhit: dasturchi doim oxirgi o'zgarishlarni ko'radi, menejer jarayonni kuzatadi, mijoz to'g'ridan-to'g'ri Figma'da sharh qoldiradi. Faylni ulashish: o'ng yuqoridagi **Share** tugmasi. Ruxsatlar: **Can view** (faqat ko'rish) va **Can edit** (tahrirlash). Havola orqali ulashishda ham ruxsat tanlanadi. Qoida — **eng kam ruxsat**: mentor va dasturchiga odatda ko'rish yetarli, tahrirlashni faqat jamoadoshlarga bering. Tahrirlayotganlarning kursorlari real vaqtda ko'rinadi. Ish tugaganda keraksiz ruxsatlarni olib tashlang. Shaxsiy ma'lumot (haqiqiy ism, telefon, rasm) dizayn faylida ommaviy havola bilan ulashilmasin.

Havolasi bor har kim tahrirlay oladigan (Can edit) ommaviy havola — xavfli: dizayn tasodifan buzilishi yoki o'chirilishi mumkin.

### 2. Sharhlar va versiya tarixi

**Sharh** (`C`) — dizaynning aniq joyiga qo'yiladigan izoh: bosib yozasiz, `@ism` bilan odamni belgilaysiz, javob yozish mumkin, hal bo'lgach **Resolve** qilinadi. Shu bilan muhokamalar tarixi pochtada yo'qolmaydi, tasdiqlash tezlashadi. Sharh yozish qoidasi: aniq (nima va qayerda), muloyim va taklif bilan: «Tugma matni ko'rinmayapti: fonni to'qroq qilsak-chi?». **Versiya tarixi** (File → Show version history) fayl o'zgarishlarini vaqt bo'yicha saqlaydi: muhim bosqichda **nom bilan** versiya saqlang («Handoff v1»), xato bo'lsa oldingi holatga qaytasiz. Bu Git'dagi commit g'oyasiga o'xshaydi.

Muhim bosqichdan oldin versiyani nom bilan saqlang: «Komponentlar tayyor», «Handoff v1». Keyin qaytish oson.

### 3. Dev Mode: dasturchiga topshirish

**Dev Mode** (Developer Handoff, `Shift+D`) — dasturchi uchun mo'ljallangan ko'rinish, brauzer inspektoriga o'xshaydi. Elementni tanlasangiz, ko'rasiz: **o'lcham** (W, H), elementlar orasidagi **masofa** (Alt bosib turib boshqa elementga olib boring), **rang**, **shrift**, **radius**, shuningdek elementning **CSS uslublari** va Android/iOS uchun kod parchalari. Ularni nusxalash mumkin. Eslatma: Figma bergan kod — boshlang'ich nuqta, uni loyihaning o'z qoidalariga (class nomlari, `rem`, o'zgaruvchilar) moslab yozish kerak. Dev Mode'ning to'liq imkoniyatlari tarifga bog'liq; bepul akkauntda asosiy qiymatlarni Design panelidan olish mumkin. Rasmlar uchun: **Export** (SVG, PNG, JPEG, 1x/2x).

Qotirilgan `width: 280px` ni to'g'ridan-to'g'ri ko'chirmang: responsiv maket uchun `max-width` va `rem` ishlating (8-sinf, 15–16-darslar).

---

## Kod namunasi

Dev Mode qiymatlaridan loyiha CSS i (kitob kartasi):

```css
/* Dev Mode: Karta/Kitob 280 x auto, padding 16, gap 12, radius 12 */
.karta {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  max-width: 17.5rem;
  padding: 1rem;
  border-radius: 0.75rem;
  background: #fff;
}
/* Dev Mode: matn 18/24, qalin; muallif 14/20, kulrang */
.karta h3 { font-size: 1.125rem; line-height: 1.5rem; margin: 0; }
.karta .muallif { font-size: 0.875rem; line-height: 1.25rem; color: #666; }

/* Assets: ikonka/kitob.svg, muqova@2x.jpg Figma Export dan olindi */
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Ruxsat tanlash
Mentor va jamoadosh uchun qaysi ruxsatlarni berasiz?

**Kutiladigan natija:** To'g'ri ruxsatlar.

**Yechim:** Mentor — Can view; jamoadosh dizayner — Can edit.

### 2-topshiriq (oson). Sharh yozish
«Yoqmadi» sharhini aniq va muloyim qilib qayta yozing.

**Kutiladigan natija:** Yaxshi sharh.

**Yechim:** «Kategoriya paneli: matn kichik ko'rinadi. Shriftni 16 px qilsak-chi?»

### 3-topshiriq (o'rta). Versiya saqlash
Muhim bosqichda versiyani qanday saqlaysiz? Nom taklif qiling.

**Kutiladigan natija:** Nomli versiya.

**Yechim:** File → Show version history → Save → «Handoff v1».

### 4-topshiriq (o'rta). CSS ga o'tkazish
Dev Mode: width 280, padding 16, radius 12. Loyihaga moslab CSS yozing.

**Kutiladigan natija:** Moslashgan CSS.

**Yechim:** 
```css
.karta {
  max-width: 17.5rem;
  padding: 1rem;
  border-radius: 0.75rem;
}
```

### 5-topshiriq (qiyin). Handoff ro'yxati
Dasturchiga topshirishdan oldin 5 ta tekshiruvni yozing.

**Kutiladigan natija:** 5 tekshiruv.

**Yechim:** Qatlam nomlari; komponentlar; rang va shriftlar tizimi; assets eksport; barcha holatlar.

### 6-topshiriq (qo'shimcha). Ommaviy havola xavfi
Can edit ommaviy havolaning 2 ta xavfini yozing.

**Kutiladigan natija:** 2 xavf.

**Yechim:** Tasodifan buzilishi yoki o'chirilishi; begonalar tahrir qilishi.

---

## Tezkor nazorat (dars oxirida)

1. Share nima uchun? — Faylni ulashish uchun.
2. Eng kam ruxsat qoidasi? — Faqat kerakli odamga kerakli ruxsat.
3. Sharh tugmasi? — `C`.
4. Dev Mode nima beradi? — O'lcham, masofa, rang, CSS.
5. Figma kodiga munosabat? — Boshlang'ich nuqta: moslab yoziladi.

## Keng tarqalgan xatolar

- Hammaga Can edit berish.
- «Yoqmadi» kabi aniq bo'lmagan sharh yozish.
- Versiyani nom bermasdan saqlash.
- Figma kodini o'ylamasdan ko'chirish.
- Assets ni eksport qilmasdan topshirish.

## Bilasizmi? (qo'shimcha)

- Alt tugmasini bosib turib, elementlar orasidagi masofani piksellarda ko'rish mumkin.
- Dev Mode'da komponent hujjatlari va kod havolalarini biriktirish mumkin.
- Katta jamoalarda dizayn va kod izchil bo'lishi uchun dizayn tokenlari ishlatiladi.
