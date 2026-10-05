# 11-dars. UX flow diagrammalari va axborot arxitekturasi

> Metro sxemasiga qarab, qayerda tushish va qayerda ko'chishni oldindan bilasiz. User flow ham ilovaning «metro sxemasi»: foydalanuvchi qaysi yo'llardan o'tishini kod yozilmasdan oldin ko'rsatadi.

## Dars xulosasi

- User flow: foydalanuvchi mahsulot ichida bosib o'tishi mumkin bo'lgan yo'llarning vizual tasviri.
- Flowchart kirish nuqtasidan (onboarding yoki bosh sahifa) boshlanib, yakuniy harakatga (xarid, ro'yxatdan o'tish) boradi.
- Romb: qaror qabul qilish nuqtasi («Ha» / «Yo'q»). To'rtburchak: bajariladigan amal.
- Uch tur: task flow (bitta vazifa), wireflow (wireframe + flowchart), user flow (turli personalar va kirish nuqtalari).
- User flow dastlabki rejalashtirishda, user research tugagach tuziladi va nechta ekran, qanday ketma-ketlik, qaysi elementlar kerakligini aniqlaydi.
- U jamoani bir fikrga keltiradi va mijozga dizayn qarorlarini tushuntiradi.
- Axborot arxitekturasi: karta tartiblash (ochiq, gibrid, yopiq) va daraxt testi yordamida foydalanuvchi mantiqiga mos qilib shakllantiriladi.

## Qo'shimcha ma'lumot

### Oqim diagrammasini qanday o'qiladi

Diagramma har doim kirish nuqtasidan boshlanadi: masalan, Login ekrani yoki bosh sahifa. Keyin siz o'qlar bo'ylab yurasiz. To'rtburchakda «nima qilinadi?» deb o'qiysiz (Kirish, Sotib olish). Rombga yetganingizda to'xtab savolga javob berasiz: «Ha» bo'lsa bir tomonga, «Yo'q» bo'lsa boshqasiga. Oxirgi nuqta maqsad: foydalanuvchi nimaga erishdi.

```text
[Login ekrani] -> [Parolni unutdim] -> <Hisob topildimi?> -Ha-> [Kod yuboriladi]
                                                    \-Yo'q-> [Xato xabari]
```

(Bu yerda `[ ]` to'rtburchak, `< >` romb. Bu o'quv misoli.)

### Task flow, wireflow va user flow: qaysi birini qachon?

- **Task flow:** «Parolni tiklash» kabi bitta vazifa uchun. Odatda bitta asosiy yo'l ko'rsatiladi.
- **Wireflow:** har bir bosqich yoniga ekranning qora-oq maketi qo'yiladi. Mobil ilovalar uchun qulay: ekranlar kichik, diagrammaga osongina sig'adi.
- **User flow:** hamma foydalanuvchi bir xil yo'ldan bormaydi. Kimdir bosh sahifadan, kimdir reklama bannerdan, kimdir qidiruv natijasidan keladi. User flow shularni birga ko'rsatadi.

### Nega user flowdan keyin ekranlar sonini bilamiz?

User flow ekranlar, ularning ketma-ketligi va kerakli elementlarni aniqlaydi. Shuning uchun u dizaynning boshida chiziladi, ammo avval foydalanuvchini o'rganish kerak: empatiya xaritasi, persona, asosiy ssenariylar. Bu siz 2-haftada o'rgangan narsalar.

### Axborot arxitekturasi: ma'lumotni kim qanday guruhlaydi

Sayt bo'limlarini o'zimizga qulay qilib emas, foydalanuvchiga qulay qilib guruhlash kerak. Buning uchun **karta tartiblash** o'tkaziladi: har bir kartaga mavzu yoziladi, foydalanuvchi ularni guruhlaydi.
- Ochiq: toifalarni foydalanuvchining o'zi nomlaydi.
- Gibrid: tayyor toifalar bor, yangisini qo'shish mumkin.
- Yopiq: faqat berilgan toifalar.

Keyin **daraxt testi**: soddalashtirilgan tuzilmada foydalanuvchi kerakli axborotni topa oladimi?

### Odatiy xatolar

- Hamma sahifani bitta diagrammaga qo'yish. Bitta vazifa uchun bitta diagramma.
- Rombdan «Ha» va «Yo'q» yo'llarini chiqarmaslik.
- Kirish nuqtasi va maqsadni belgilamaslik.
- Karta tartiblash natijasiga ko'r-ko'rona ishonish: u real hayotdagi qarorlarni har doim to'liq aks ettirmasligi mumkin.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| User flow | Foydalanuvchi mahsulot ichida bosib o'tishi mumkin bo'lgan yo'llarning vizual tasviri |
| Flowchart | Oqim diagrammasi: kirish nuqtasidan yakuniy harakatgacha bosqichlar |
| Task flow | Bitta aniq vazifani bajarish oqimi |
| Wireflow | Wireframe va flowchartning aralashmasi |
| Kirish nuqtasi | Foydalanuvchi mahsulotga kiradigan joy (onboarding, bosh sahifa, reklama, qidiruv) |
| Maqsad (goal) | Foydalanuvchi erishmoqchi bo'lgan yakuniy harakat |
| Qaror nuqtasi | Romb shakli: «Ha» yoki «Yo'q» yo'nalishlari chiqadigan joy |
| Persona | Maqsadli foydalanuvchining namunaviy obrazi |
| Karta tartiblash | Foydalanuvchilar mavzu kartalarini mantiqiy guruhlarga ajratadigan usul |
| Daraxt testi | Soddalashtirilgan tuzilmada axborotni topa olishni baholash |
| Axborot arxitekturasi (IA) | Mahsulotdagi axborotni guruhlash va tartiblash tuzilmasi |

## Bilasizmi?

- Oqim diagrammalaridagi romb va to'rtburchak shakllari dasturlashda algoritm blok-sxemalarida ham ishlatiladi.
- Metro sxemalari geografik aniq emas, faqat bekatlar orasidagi bog'lanishni ko'rsatadi. User flow ham xuddi shunday.
- Hujjatga ko'ra, user flow loyiha oxirida mijozga beriladigan asosiy hujjatlardan biri.
- Karta tartiblashni oddiy qog'oz kartalarda ham, raqamli vositalarda ham o'tkazish mumkin.

## Topshiriqlar

### 1. Shaklni tanlang · oson
Quyidagi uchun romb yoki to'rtburchak tanlang: (a) «Kirish» tugmasi bosiladi; (b) «Parol to'g'rimi?»; (c) «Arizani yuborish»; (d) «Foydalanuvchi ro'yxatdan o'tganmi?»

**Kutiladigan natija:** 4 ta javob va qisqa sabab.

### 2. Ta'rif · oson
User flow nima ekanini o'z so'zlaringiz bilan 1–2 jumlada yozing va hayotdagi o'xshatish toping (metrodan boshqa).

**Kutiladigan natija:** ta'rifda «yo'llar» va «foydalanuvchi» so'zlari, mantiqli o'xshatish.

### 3. Kirish va maqsad · oson
Telegram'da «yangi guruh yaratish» vazifasi uchun kirish nuqtasi va maqsadni yozing.

**Kutiladigan natija:** kirish nuqtasi (masalan, chatlar ro'yxati) va maqsad (guruh yaratildi).

### 4. Uchta tur · oson
Task flow, wireflow va user flow ni bittadan jumla bilan farqlang.

**Kutiladigan natija:** 3 jumla, har birida asosiy xususiyat.

### 5. Qaysi tur? · o'rta
Vaziyatlar: (a) «Parolni tiklash» uchun bitta yo'l; (b) mobil ilovaning har ekrani maketi va ular orasidagi o'qlar; (c) bir vazifaga ikki persona va uch kirish nuqtasidan boriladi. Har biriga turini yozing.

**Kutiladigan natija:** task flow, wireflow, user flow va sabablar.

### 6. Diagramma o'qing · o'rta
Quyidagini o'qing va savolga javob bering:
```text
[Do'konga kirish] -> [Mahsulot tanlandi] -> <Savatda bormi?> -Ha-> [To'lov]
                                                       \-Yo'q-> [Savatga qo'shish] -> [To'lov]
```
«Savatda bormi?» qaysi shakl va undan nechta yo'l chiqadi? Maqsad nima?

**Kutiladigan natija:** romb, 2 yo'l (Ha, Yo'q), maqsad: to'lov.

### 7. Bashorat qiling · o'rta
Foydalanuvchi ro'yxatdan o'tish formasida kod keldi, lekin uni kiritdi va «Kod noto'g'ri» xabarini ko'rdi. Diagrammada bu holat qaysi element bilan ko'rsatiladi va keyin nima bo'lishi kerak?

**Kutiladigan natija:** romb («Kod to'g'rimi?»), «Yo'q» yo'li qayta urinishga qaytadi.

### 8. Tartib · o'rta
Quyidagilarni to'g'ri tartibda joylashtiring: user flow chizish, foydalanuvchi tadqiqoti, persona yaratish, ekranlar sonini aniqlash.

**Kutiladigan natija:** tadqiqot, persona, user flow, ekranlar soni.

### 9. Xatoni toping · qiyin
Dizayner «Parolni tiklash» diagrammasiga barcha 30 sahifani, 3 xil personani va 4 xil kirish nuqtasini qo'ydi. Nima noto'g'ri va qaysi ikki turga ajratish kerak?

**Kutiladigan natija:** task flow bitta vazifaga qaratiladi; bitta murakkab diagramma o'rniga task flow va alohida user flow.

### 10. Maktab saytida ro'yxatdan o'tish · qiyin
Kirish nuqtasidan maqsadgacha kamida 5 to'rtburchak va 2 romb bilan task flow chizing. Sherigingizdan qayerda to'xtab qolish mumkinligini toptiring.

**Kutiladigan natija:** chizma, 2 qaror nuqtasi (Ha/Yo'q yo'llari bilan), sherik topgan 1 ta to'siq va uning tuzatishi.

### 11. Karta tartiblash · qiyin
12 ta kartaga o'z maktabingiz saytining mavzularini yozing (Qabul, Dars jadvali, Yangiliklar, To'garaklar, Galereya, Aloqa va h.k.). Ikki sinfdoshingizga ochiq tartiblash o'tkazing, so'ng 4 ta berilgan toifa bilan yopiq tartiblashni sinang. Natijalar qanday farq qildi?

**Kutiladigan natija:** ikki natija jadvali va 2–3 jumlalik xulosa (kelishmovchilik bo'lgan kartalar ro'yxati).

### 12. Bonus: o'z ilovangiz uchun user flow · bonus
O'zingiz o'ylagan ilova uchun bitta vazifa (masalan, «buyurtma berish») ni ikki xil kirish nuqtasidan (bosh sahifa va qidiruv) ko'rsating. Ikkala yo'l qayerda birlashadi?

**Kutiladigan natija:** ikki kirish nuqtali diagramma va birlashish nuqtasi.

## O'zingizni tekshiring

1. User flow nima va nega kerak?
2. Flowchartdagi romb va to'rtburchak nimani bildiradi?
3. Task flow, wireflow va user flow qanday farqlanadi?
4. User flow dizayn jarayonining qaysi bosqichida tuziladi va undan oldin nimalar bajarilgan bo'ladi?
5. User flow jamoa va mijoz uchun qanday foyda beradi?
6. Karta tartiblashning 3 turi qaysilar?
7. Daraxt testi nimani tekshiradi?
8. Qanday hollarda mavjud user flowni qayta ko'rib chiqish kerak?

## Uyga vazifa

Kundalik ishlatadigan ilovangizdan bitta vazifani tanlang (masalan, «yangi hisob yaratish»), uning task flow sini kamida 5 amal va 2 qaror nuqtasi bilan qog'ozga chizing, kirish nuqtasi va maqsadni belgilang. Oxirida 2–3 jumlada qayerda foydalanuvchi adashishi mumkinligini yozing (20–30 daqiqa).
