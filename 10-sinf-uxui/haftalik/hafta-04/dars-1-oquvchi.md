# 10-dars. Prototip va ularning turlari (Low-fidelity vs High-fidelity)

> Katta uy qurishdan oldin karton maket yasaladi. Dizaynerlar ham shunday qiladi: xatoni qimmatga tushmasdan oldin prototipda topadi.

## Dars xulosasi

- Prototip: mahsulotning soddalashtirilgan namunasi, u g'oyani vaqt va pul sarflamasdan tekshirishga yordam beradi.
- Prototip arzon va tez tayyorlanadi, xatolarni erta ochadi, yaramaydigan g'oyani oldindan rad etishga imkon beradi.
- Prototipning 5 maqsadi: g'oyani ishlab chiqish, jamoada umumiy tushuncha, mijozni ishontirish, texnik imkoniyatni tekshirish, foydalanuvchi bilan sinash.
- Jarayon 4 bosqichdan iborat: Konseptual dizayn, O'zaro ta'sir dizayni, Ekran dizayni, Sinovdan o'tkazish.
- Statik prototiplar: qog'oz prototipi, wireframe, grafik muharrirdagi rasmlar. Dinamik prototip: tugmalar orqali ekranlar orasida o'tish bor.
- Qora-oq wireframe (low-fidelity) tez va oson o'zgaradi; rangli interaktiv prototip yakuniy natijaga o'xshaydi, lekin xatoni tuzatish qiyinroq.
- Sahifa bloklari: navigatsiya, axborot, xizmat, dizayner, reklama.
- Navigatsiya dizayni bir vaqtda 3 muammoni hal qiladi: yo'l, elementlar orasidagi munosabat, joriy sahifaga munosabat.

## Qo'shimcha ma'lumot

### Nega birinchi prototip «noto'g'ri» chiqadi, va bu yaxshi

Hujjatda aytilishicha, ko'pgina birinchi prototiplar noto'g'ri chiqadi, bu tabiiy hol. Yozuvchi birinchi qoralamani yozadi, so'ng tahrir qiladi. Prototip ham qoralama: uni mukammal qilishga urinmang, oddiy variantni tez chizing, sinang, so'ng yaxshilang. Bu takrorlash **iteratsiya** deb ataladi.

### Qog'oz prototipi: nega «eskirgan» emas

Qog'ozda chizilgan ekranni o'zgartirish uchun bitta o'chirg'ich yetadi. Bundan tashqari, rangsiz chizmada odamlar «rangi yoqmadi» demaydi, ular tuzilma va mantiq haqida gapiradi. Shuning uchun dizaynerlar g'oyani avval qog'ozda sinaydi.

### Statik va dinamik: «rasm» va «video» kabi

Statik prototip — rasm: ko'rasiz, lekin bosib bo'lmaydi. Dinamik prototip — kichik o'yin: tugmani bosasiz va keyingi ekran ochiladi. Hujjat dinamik prototipni «har bir ekran alohida slayd, tugma bosish natijasi esa slaydlar orasidagi o'tish» deb tushuntiradi.

```text
Ekran 1 (Bosh sahifa)  --[Kirish tugmasi]-->  Ekran 2 (Login)  --[Tasdiqlash]-->  Ekran 3 (Profil)
```

### Past va yuqori detallashgan prototip

- **Low-fidelity:** qora-oq, oddiy shakllar, faqat tuzilma. Maqsad: «qayerda nima turadi?»
- **High-fidelity:** ranglar, shriftlar, rasmlar, yakuniy natijaga yaqin ko'rinish. Maqsad: mijoz va ishlab chiquvchi bilan aniq muloqot.

Qaysi biri yaxshi? Savol noto'g'ri: ular ketma-ket bosqichlar. Avval low, so'ng high.

### Odatiy xatolar

- Birinchi bosqichdayoq rang va rasm tanlab, vaqt yo'qotish.
- Hamma sahifani bir-biriga bog'lashga urinish (hujjat: bu imkonsiz, faqat kerakli havolalar tanlanadi).
- Qidiruv maydonini «ko'rinmasin» deb yashirish.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Prototip | Mahsulotning soddalashtirilgan namunasi |
| Wireframe | Interfeysning eng soddalashtirilgan konturli skeleti |
| Qog'oz prototipi | Qo'lda qog'ozga chizilgan ekranlar |
| Statik prototip | O'zgarmaydigan, bosma yoki rasm ko'rinishidagi prototip |
| Dinamik (interaktiv) prototip | Tugmalar orqali ekranlar orasida o'tish bor prototip |
| Iteratsiya | Sinov asosida prototipni qayta yaxshilash sikli |
| Navigatsiya | Foydalanuvchining sayt/ilova ichida yurishini ta'minlovchi elementlar |
| Breadcrumbs (navigatsiya paneli) | Foydalanuvchining joriy sahifaga yo'lini ko'rsatuvchi havolalar ketma-ketligi |
| Footer («podval») | Sahifa pastidagi matnli havolalar bloki |
| Layout | Sahifa tartibi, elementlarning joylashuvi |

## Bilasizmi?

- «Prototip» so'zi yunoncha «protos» (birinchi) va «typos» (nusxa, shakl) so'zlaridan kelib chiqqan.
- Avtomobil kompaniyalari yangi modelni ishlab chiqarishdan oldin ko'pincha loy yoki kartondan to'liq o'lchamli maket yasaydi.
- Hujjatdagi misollar: arxitektor maket yasaydi, aviatsiya muhandisi aerodinamik quvurda model sinaydi. Siz esa interfeys prototipini yasaysiz.
- Rasmlar galereyasida bitta katta rasm o'rniga bir nechta kichik rasm qo'yish sahifani tezroq yuklaydi.

## Topshiriqlar

### 1. Prototip ta'rifi · oson
Prototip nima ekanini o'z so'zlaringiz bilan 1–2 jumlada yozing va hayotdan bitta misol keltiring (hujjatdagilardan boshqa).

**Kutiladigan natija:** ta'rifda «soddalashtirilgan namuna» va «g'oyani oldindan tekshirish» g'oyalari bor, misol mantiqli.

### 2. Maqsadlarni toping · oson
Quyidagilardan prototipning maqsadi bo'lmaganini toping: (a) jamoada umumiy tushuncha yaratish; (b) mijozni ishontirish; (c) tayyor saytni xostingga yuklash; (d) texnik imkoniyatni tekshirish.

**Kutiladigan natija:** to'g'ri harf va 1 jumlalik sabab.

### 3. Bosqichlar tartibi · oson
Aralash berilgan bosqichlarni tartiblang: Sinovdan o'tkazish, Ekran dizayni, Konseptual dizayn, O'zaro ta'sir dizayni.

**Kutiladigan natija:** 4 bosqich to'g'ri tartibda.

### 4. Statik yoki dinamik · oson
Turkumlang: (a) daftarga chizilgan ilova ekranlari; (b) tugmalar bosilganda ochiladigan Figma namoyishi; (c) bitta qora-oq maket rasmi.

**Kutiladigan natija:** har biriga «statik» yoki «dinamik» va sabab.

### 5. Blok turini aniqlang · o'rta
Har bir blok qaysi turga kiradi (navigatsiya, axborot, xizmat, dizayner, reklama)? Logotip havolasi; til tanlash; «Bo'lim» (yangiliklar); sarlavha va shior; breadcrumbs; bosma versiya.

**Kutiladigan natija:** 6 ta blok turkumlangan jadval.

### 6. Taqqoslash jadvali · o'rta
Qog'oz prototipi va rangli interaktiv prototipni 4 mezon bo'yicha taqqoslang: tezlik, narx/mehnat, o'zgartirish osonligi, qachon qo'llanadi.

**Kutiladigan natija:** 2 ustunli, 4 qatorli jadval, hujjat fikriga mos.

### 7. Bu qaysi muammo? · o'rta
Sayt menyusida 40 ta havola bor, ular tartibsiz ro'yxat. Navigatsiya dizaynining uch muammosidan qaysi biri buzilgan? Qanday tuzatasiz?

**Kutiladigan natija:** buzilgan muammo nomi (elementlar orasidagi munosabat) va 2 ta tuzatish g'oyasi.

### 8. Bashorat qiling · o'rta
Foydalanuvchi uzoq yo'lni o'tib, 5-sahifaga yetdi. Qaysi navigatsiya bloki unga «qayerdaman» va «bir qadam orqaga» imkonini beradi? U uzun bo'lsa, qanday qisqartiriladi?

**Kutiladigan natija:** navigatsiya paneli (breadcrumbs); oraliq havolalar ellips bilan almashtiriladi.

### 9. Xatoni toping · qiyin
Dizayner wireframega qizil-yashil gradient fon, 6 xil shrift va rasmlar qo'ydi, so'ng «g'oyani sinab ko'raman» dedi. Nima noto'g'ri? Nega? Qanday tuzatasiz?

**Kutiladigan natija:** past detallashgan bosqichda rang va grafika e'tiborni chalg'itadi; tuzatish: qora-oq soddalashtirish.

### 10. Maktab sayti qog'oz prototipi · qiyin
Maktab sayti bosh sahifasini A4 da chizing: logotip, gorizontal menyu, qidiruv, yangiliklar, galereya, til tanlash, podval. Har blokka turini yozing. Do'stingiz «Qabul qoidalarini toping» vazifasini bajarsin va qayerga bosishini ko'rsatsin.

**Kutiladigan natija:** 7 blok, to'g'ri joylashuv, sinov natijasi va 1 ta tuzatish yozilgan.

### 11. Oqim rejasi · qiyin
Telegram-bot yoki o'zingiz yaratmoqchi bo'lgan ilova uchun 4 bosqichning har birida aynan nima qilishingizni 1–2 jumladan yozing.

**Kutiladigan natija:** 4 bosqich, har biri konkret mahsulotga bog'langan.

### 12. Bonus: ikki xil fidelity · bonus
Bir ekranni (masalan, login) avval 3 daqiqada qora-oq chizing, so'ng rangli, 3 daqiqada ikkinchi variant chizing. Qaysi birida o'zgartirish oson bo'ldi va nega?

**Kutiladigan natija:** ikki chizma va 3 jumlalik xulosa.

## O'zingizni tekshiring

1. Prototip nima va nega kerak?
2. Prototipning kamida 4 maqsadini sanang.
3. Prototiplash jarayoni qaysi 4 bosqichdan iborat?
4. Qog'oz prototipining afzalliklari nimalar?
5. Dinamik prototip statikdan nimasi bilan farq qiladi?
6. Qora-oq wireframe va rangli prototip qachon qo'llanadi?
7. Navigatsiya dizayni qaysi 3 muammoni hal qilishi kerak?
8. Axborot, xizmat va reklama bloklariga bittadan misol keltiring.

## Uyga vazifa

Oilangizdagi biror kishining kundalik ishlatadigan ilovasini (masalan, bank yoki Telegram) tanlang, uning bitta ekranini qog'ozga qora-oq prototip sifatida chizing, ekrandagi kamida 5 blokning turini belgilang va 3 jumlada «bu ekran qaysi muammoni yaxshi hal qiladi?» deb yozing (20–30 daqiqa).
