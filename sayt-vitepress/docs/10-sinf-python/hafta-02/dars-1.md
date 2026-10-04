---
title: "4-dars. Foydalanuvchilarni boshqarish: Identifikatsiya, autentifikatsiya va avtorizatsiya. Token, session va JWT"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (Python)", "link": "/10-sinf-python/"}, "week": {"n": 2, "link": "/10-sinf-python/hafta-02/"}, "g": 4, "title": "Foydalanuvchilarni boshqarish: Identifikatsiya, autentifikatsiya va avtorizatsiya. Token, session va JWT", "lead": "Foydalanuvchilarni tanish va himoya qilish — har qanday backend tizimning eng muhim ustunidir. Ushbu darsda biz login, parol, sessiya va zamonaviy JSON Web Token (JWT) mexanizmlari bilan tanishamiz hamda NewsPortal uchun Custom User modelini quramiz.", "slide": "/slaydlar/10-sinf-python/hafta-02/dars-1.html", "tabs": [{"g": 4, "link": "/10-sinf-python/hafta-02/dars-1", "current": true}, {"g": 5, "link": "/10-sinf-python/hafta-02/dars-2", "current": false}, {"g": 6, "link": "/10-sinf-python/hafta-02/dars-3", "current": false}], "prev": null, "next": {"g": 5, "title": "Ruxsatlar bilan ishlash", "link": "/10-sinf-python/hafta-02/dars-2"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- Tizim xavfsizligi uchta asosiy bosqichdan iborat: **Identifikatsiya** (shaxsni e'lon qilish), **Autentifikatsiya** (haqiqiylikni isbotlash) va **Avtorizatsiya** (huquqlarni belgilash).
- **Session-based** autentifikatsiya server xotirasida (RAM / DB) sessiya kalitini saqlaydi, bu esa yirik taqsimlangan tizimlarda va mobil ilovalarda serverga yuklama beradi.
- **Token-based** autentifikatsiyada har bir so'rov sarlavhasida (Headers) token yuboriladi, bu esa serverni holatsiz (stateless) qilishga yordam beradi.
- **JSON Web Token (JWT)** uch qismdan iborat: **Header** (algoritm), **Payload** (foydalanuvchi ma'lumotlari) va **Signature** (serverning maxfiy kaliti bilan tasdiqlangan raqamli imzo).
- JWT tizimida ikkita token juftligi ishlatiladi: qisqa muddatli **Access Token** (amallarni bajarish uchun) va uzoq muddatli **Refresh Token** (yangi access token olish uchun).
- Djangoning standart `username` ga asoslangan modeli o'rniga zamonaviy email orqali kiruvchi **Custom User** modelini yaratish xalqaro standart hisoblanadi.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Pasport va Viza analogiyasi: Autentifikatsiya va Avtorizatsiya

Farqni darhol eslab qolish uchun aeroportdagi chegarani tasavvur qiling:
- **Identifikatsiya:** Siz pasport nazoratchisiga: "Mening ismim Anvar, men O'zbekiston fuqarosiman", deb aytasiz.
- **Autentifikatsiya:** Nazoratchi sizning pasportingizdagi fotosuratni yuzingiz bilan solishtiradi va barmoq izingizni tekshiradi. Haqiqatan ham siz ekanligingiz tasdiqlandi!
- **Avtorizatsiya:** Endi nazoratchi pasportingizdagi vizaga qaraydi: "Siz bu mamlakatga kela olasiz, lekin faqat sayyoh sifatida 30 kun yashashingiz mumkin, ishlash huquqingiz yo'q!". Bu — avtorizatsiyadir.

### 2. Nega JWT buzilmas (tamper-proof) hisoblanadi?

Ba'zi o'quvchilar: "Agar JWT ochiq matn (Base64) bo'lsa, xaker uning ichidagi `user_id: 5` ni `user_id: 1` (admin) qilib o'zgartirib olsa nima bo'ladi?" deb so'rashadi.
Javob: **Signature (Raqamli imzo)!**
Imzo quyidagi formula bilan hisoblanadi:
`HMACSHA256(base64UrlEncode(header) + "." + base64UrlEncode(payload), SECRET_KEY)`

Faqat servergina o'zining maxfiy `SECRET_KEY` kalitini biladi. Agar xaker payload ichidagi biror harfni o'zgartirsa, imzo matematik jihatdan butunlay boshqacha bo'lib qoladi. Server kelgan tokenni tekshirganda, imzo mos kelmagani sababli so'rovni darhol rad etadi (`401 Unauthorized`).

### 3. Access va Refresh tokenlarning xavfsizlik siri

Nima uchun bitta uzoq muddatli token bilan cheklanmaymiz?
- Agar bitta token 1 yilga berilsa va xaker uni kompyuterdan o'g'irlab olsa, u 1 yil davomida sizning hisobingizdan erkin foydalana oladi.
- Shuning uchun **Access Token** atigi 15-30 daqiqa yashaydi. U o'g'irlangan taqdirda ham, 15 daqiqadan so'ng o'z-o'zidan "o'ladi".
- **Refresh Token** esa juda kamdan-kam, faqat yangi token olishda serverga yuboriladi va u maxfiy HTTP-only cookie yoki himoyalangan joyda saqlanadi.

### 4. Dasturchilar ko'p yo'l qo'yadigan xatolar

- **Xato 1: JWT Payload ichida maxfiy parollarni saqlash.** Esda tuting: JWT shifrlangan emas, faqat imzolangan! Har qanday odam uni `jwt.io` saytiga qo'yib, ichidagi ma'lumotni o'qiy oladi. Shuning uchun payload ichiga hech qachon parol yoki bank kartasi ma'lumotlari yozilmaydi.
- **Xato 2: Custom User yaratishni kechiktirish.** Loyihani standart Django User bilan boshlab, keyin 1 oydan so'ng Custom User ga o'tish juda katta migratsiya muammolarini keltirib chiqaradi. Custom User har doim loyihaning 1-kunida yozilishi shart!

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Identifikatsiya** | Foydalanuvchining o'z shaxsini tizimga e'lon qilishi (masalan: email yoki login kiritishi). |
| **Autentifikatsiya** | Foydalanuvchi taqdim etgan dalillar (parol, token) orqali uning haqiqiy shaxsini tasdiqlash. |
| **Avtorizatsiya** | Tizimga kirgan foydalanuvchining qaysi ma'lumotlar va amallarga huquqi borligini belgilash. |
| **Session** | Server tomonida saqlanuvchi, mijozning tashrif holatini eslab turuvchi ma'lumotlar to'plami. |
| **JWT (JSON Web Token)** | Tomonlar o'rtasida ma'lumotlarni xavfsiz JSON ko'rinishida uzatish uchun ochiq standart (RFC 7519). |
| **Access Token** | API so'rovlarini bajarish uchun ishlatiladigan qisqa muddatli ruxsatnoma tokeni. |
| **Refresh Token** | Eskirgan access token o'rniga yangisini olish uchun xizmat qiluvchi uzoq muddatli token. |
| **Payload** | JWT tokeni ichida saqlanadigan foydali ma'lumotlar (user_id, email, rollar). |
| **Signature** | Tokenning o'zgarmaganligini va server tomonidan berilganligini tasdiqlovchi raqamli imzo. |
| **AbstractBaseUser** | Djangoda noldan boshlab to'liq moslashtirilgan foydalanuvchi modelini yaratish uchun asosiy klass. |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Parollar ma'lumotlar bazasida hech qachon ochiq matn holda saqlanmaydi! Django ularni `PBKDF2` va `SHA-256` algoritmlari yordamida 260 000 marta qayta aylanuvchi bir tomonlama heshga aylantirib saqlaydi.
- Dunyodagi eng yirik servislar (Netflix, Uber, Spotify) har soniyada yuz minglab API so'rovlarini aynan JWT orqali autentifikatsiya qiladi, chunki bu usul ma'lumotlar bazasiga ortiqcha so'rov yubormasdan server resurslarini 70% gacha tejaydi.
- Agar xaker serverning `SECRET_KEY` kalitini bilib olsa, u xohlagan foydalanuvchi (hatto bosh admin) nomidan soxta JWT token yasab olishi mumkin. Shu sababli bu kalit `.env` faylida o'ta maxfiy saqlanadi.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Xavfsizlik bosqichlarini aniqlash <Badge type="tip" text="oson" />
Quyidagi vaziyatlarning qaysi biri Identifikatsiya, qaysi biri Autentifikatsiya va qaysi biri Avtorizatsiya ekanligini belgilang:
a) Foydalanuvchi barmoq izini skanerga qo'ydi va telefon qulfi ochildi.
b) Saytga kirishda o'z loginini yozdi.
c) Sayt admin panelga kirmoqchi bo'lgan oddiy foydalanuvchiga "403 Forbidden" xabarini ko'rsatdi.
**Kutiladigan natija:** Har bir vaziyatga mos tushuncha nomi.

### 2. JWT tarkibiy qismlarini sanash <Badge type="tip" text="oson" />
Quyidagi namunaviy token qismlarga bo'lingan:
`AAAAAA.BBBBBB.CCCCCC`
Nuqtalar bilan ajratilgan A, B va C qismlari qanday nomlanishini yozing.
**Kutiladigan natija:** 3 ta qismning aniq nomlari.

### 3. Standart User va Custom User farqi <Badge type="tip" text="oson" />
Standart Django User modeli login uchun qaysi maydondan foydalanadi? Custom User modelimizda bu vazifani qaysi maydon bajarishini belgiladik?
**Kutiladigan natija:** Standart va yangi maydon nomlari.

### 4. HTTP Bearer sarlavhasi <Badge type="tip" text="oson" />
Frontend dasturchi API ga so'rov yuborayotganda tokenni qaysi HTTP sarlavhasida (Header) va qanday formatda yozishi kerakligini ko'rsating.
**Kutiladigan natija:** Aniq sarlavha nomi va namunaviy qator.

### 5. Access va Refresh token taqqoslovi <Badge type="warning" text="o'rta" />
Access token va Refresh tokenning quyidagi 3 ta mezon bo'yicha farqlarini jadval ko'rinishida yozing:
1. Yashash muddati (qancha vaqt amal qiladi);
2. Asosiy vazifasi;
3. Qayerda va qay tarzda ishlatilishi.
**Kutiladigan natija:** Uchta parametr bo'yicha qiyosiy jadval.

### 6. Session va JWT taqqoslash hisobi <Badge type="warning" text="o'rta" />
Tasavvur qiling, internet-do'konga bir vaqtning o'zida 100 000 ta faol foydalanuvchi kirdi.
- Agar Session ishlatilsa, server xotirasida har biri 2 KB dan bo'lgan 100 000 ta sessiya fayli saqlanadi. Jami qancha RAM xotira kerak bo'ladi?
- Agar JWT ishlatilsa, server xotirasida qancha ma'lumot saqlanadi?
**Kutiladigan natija:** Ikkala holat uchun xotira sarfi hisob-kitobi va xulosa.

### 7. Custom User modelida UserManager vazifasi <Badge type="warning" text="o'rta" />
Nima sababdan `User` modeli bilan birga alohida `UserManager(BaseUserManager)` klassi ham yoziladi? Undagi `create_user` va `create_superuser` metodlari nima vazifani bajaradi?
**Kutiladigan natija:** UserManager roli va ikkala metodning vazifalari tushuntirilishi.

### 8. Kod tahlili: Xatolikni topish <Badge type="warning" text="o'rta" />
Boshlovchi dasturchi foydalanuvchi yaratish uchun quyidagi kodni yozdi:
```python
user = User(email="test@mail.uz", password="mypassword123")
user.save()
```
Ushbu kod nima uchun xavfsizlik jihatidan o'ta xato va nega tizimga kirishda bu parol ishlamaydi? To'g'ri kod qanday bo'lishi kerak?
**Kutiladigan natija:** Xatolik sababi (heshitilmagan parol) va `user.set_password()` kodi.

### 9. Mini-loyiha: Postman orqali JWT olish va ishlatish <Badge type="danger" text="qiyin" />
`rest_framework_simplejwt` kutubxonasi yordamida:
1. Foydalanuvchi emaili va parolini yuborib token oluvchi `POST /api/v1/auth/jwt/create/` so'rovining JSON tanasini (Body) yozing.
2. Server qaytaradigan namunaviy javobni (JSON: `access` va `refresh`) ko'rsating.
3. Ushbu `access` token bilan `GET /api/v1/posts/` manziliga so'rov yuborish sarlavhasini yozing.
**Kutiladigan natija:** To'liq so'rov va javob namunalari.

### 10. Token muddati tugaganda frontend harakati <Badge type="danger" text="qiyin" />
Frontend ilova har safar API ga so'rov yuborganda `401 Unauthorized` xatosini oldi.
Ushbu holatda frontend ilova qanday avtomatlashtirilgan algoritm (Axios Interceptors) bo'yicha ish tutishi kerak?
- Qaysi endpointga qanday token yuboriladi?
- Agar yangi access token olinsa nima bo'ladi?
- Agar refresh token ham eskirgan bo'lsa, foydalanuvchi qayerga yo'naltiriladi?
**Kutiladigan natija:** Tokenni yangilash algoritmining bosqichma-bosqich tahlili.

### 11. Xavfsizlik tahlili: Token o'g'irlanishi (XSS va CSRF) <Badge type="danger" text="qiyin" />
Tokenlarni brauzerda qayerda saqlash xavfsizroq: `LocalStorage`dami yoki `HttpOnly Cookie`dami?
1. `LocalStorage` da saqlangan tokenni XSS (Cross-Site Scripting) hujumi orqali xaker qanday o'g'irlashi mumkin?
2. `HttpOnly Cookie` nima uchun JavaScript orqali o'qishdan himoyalangan?
**Kutiladigan natija:** Xavfsizlik tahlili va eng yaxshi amaliyotlar bo'yicha tavsiyalar.

### 12. Bonus tadqiqot: OAuth2 va ijtimoiy tarmoqlar orqali kirish <Badge type="info" text="bonus" />
Ko'plab saytlarda "Google orqali kirish" yoki "Telegram orqali kirish" tugmalari bor.
1. Bu tizim ortida qanday protokol (OAuth 2.0 / OpenID Connect) ishlaydi?
2. Google sizning parolingizni ushbu saytga bermasdan, qanday qilib sizning shaxsingizni tasdiqlab beradi?
3. DRF loyihasiga Google autentifikatsiyasini ulash qanday amalga oshiriladi?
**Kutiladigan natija:** OAuth 2.0 mexanizmini sodda tilda ochib beruvchi qiziqarli mustaqil tadqiqot.

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Identifikatsiya va Autentifikatsiya orasidagi asosiy farqni bitta hayotiy misol bilan ayting.
2. Nima uchun Session-based autentifikatsiyani "stateful", JWT-ni esa "stateless" deb atashadi?
3. JWT ning uchala qismi qanday nomlanadi va Signature nima vazifani bajaradi?
4. Nega Access token muddati qisqa, Refresh token muddati esa uzoq qilib belgilanadi?
5. Standart Django foydalanuvchi modeli o'rniga Custom User yaratish nima uchun muhim?
6. HTTP so'rovida token qaysi sarlavhada uzatiladi?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. Konspektdagi `User` va `UserManager` modellarini `src/apps/accounts/models.py` da yozing.
2. `settings/base.py` fayliga `AUTH_USER_MODEL = "accounts.User"` sozlamasini kiriting.
3. `rest_framework_simplejwt` paketini o'rnatib, `SIMPLE_JWT` sozlamalarini qo'shing.
4. Terminalda `makemigrations` va `migrate` qilib, `createsuperuser` orqali yangi admin hisobini oching.

</div>

