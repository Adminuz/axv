# 13-dars. Foydalanuvchilarni boshqarish: Identifikatsiya, autentifikatsiya va avtorizatsiya. Token, session va JWT

> Kutubxonaga hamma kirib ketaversa, kitoblarni kim yozganini bilmaymiz. Bugun E-Library ga ro'yxatdan o'tish va kirish tizimini qo'shamiz.

## Dars xulosasi

- **Identifikatsiya** — kim ekanligingiz; **autentifikatsiya** — isbot; **avtorizatsiya** — ruxsat darajasi.
- **Session** serverda holat saqlaydi, **token** (JWT) mijozda turadi va imzolangan.
- **JWT** = header.payload.signature; payload shifrlanmagan, imzo o'zgarishdan himoya qiladi.
- Parol **bcrypt** bilan xeshlanadi; bazada faqat `hashed_password`.
- `/auth/login` JWT beradi, `OAuth2PasswordBearer` tokenni oladi, `get_current_user` tekshiradi.
- Xatolar: 401 (autentifikatsiya), 403 (avtorizatsiya), 409 (email band), 422 (validatsiya).

## Qo'shimcha ma'lumot

### 1. Pochta timsoli
Identifikatsiya — pochta manzili, autentifikatsiya — pasport ko'rsatish, avtorizatsiya — qaysi xonaga kirish mumkinligi. Uchovi alohida bosqich.

### 2. Nega passlib va bcrypt?
bcrypt parolni sekin xeshlaydi: tajovuzkor ko'p variantni tez sinay olmaydi. `passlib` esa xeshlash va tekshirishni bitta interfeysga jamlaydi.

### 3. Odatiy xatolar
Parolni ochiq saqlash; `jwt_secret_key` ni kodga yozish; tokenga parol qo'shish; `401` o'rniga `403` qaytarish; `algorithms=[...]` ni ko'rsatmaslik.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Identifikatsiya** | Foydalanuvchi kimligini aytishi |
| **Autentifikatsiya** | Kimligini isbotlash |
| **Avtorizatsiya** | Ruxsat darajasini tekshirish |
| **Session** | Serverda saqlanadigan kirish holati |
| **JWT** | Imzolangan JSON token |
| **bcrypt** | Parolni sekin xeshlash algoritmi |
| **Bearer** | Tokenni sarlavhada yuborish usuli |
| **OAuth2PasswordBearer** | FastAPI da tokenni oluvchi sxema |

## Bilasizmi?

- JWT ni jwt.io saytida joylashtirib, payload ni o'qish mumkin: shuning uchun u maxfiy emas.
- bcrypt parolning birinchi 72 baytidan foydalanadi.
- FastAPI Swagger dagi Authorize tugmasi `OAuth2PasswordBearer` tufayli paydo bo'ladi.

## Topshiriqlar

### 1. Uch tushunchani ajrating · oson
Identifikatsiya, autentifikatsiya va avtorizatsiyaga bittadan misol keltiring.

**Kutiladigan natija:** 3 ta to'g'ri misol.

### 2. JWT qismlari · oson
JWT ning 3 qismini va har birining vazifasini yozing.

**Kutiladigan natija:** header, payload, signature.

### 3. Xesh yoki ochiq · oson
Nega bazada parol ochiq saqlanmaydi? 2 ta sabab yozing.

**Kutiladigan natija:** Sizib chiqish xavfi va xeshdan tiklab bo'lmasligi.

### 4. Status kodlar · oson
401, 403, 409 kodlarini holatlar bilan juftlang.

**Kutiladigan natija:** 3 ta juftlik.

### 5. User modeli · o'rta
`users` jadvali uchun `User` modelini yozing (id UUID, email unique, hashed_password).

**Kutiladigan natija:** `users` jadvali migratsiyada paydo bo'ladi.

### 6. Schema · o'rta
`UserCreate` va `UserRead` sxemalarini yozing; javobda parol bo'lmasin.

**Kutiladigan natija:** `UserRead` da `password` yo'q.

### 7. Register · o'rta
`/auth/register` ni yozing va bir xil email bilan ikkinchi marta yuborib 409 oling.

**Kutiladigan natija:** 201 va keyin 409.

### 8. Bu kod nima qiladi? · o'rta
`pwd.verify("12345678", hashed)` natijasi nima va nega xeshni `==` bilan solishtirib bo'lmaydi?

**Kutiladigan natija:** True/False; salt tufayli xesh har safar boshqacha.

### 9. Login · qiyin
`/auth/login` ni yozing: noto'g'ri parolda 401, to'g'ri bo'lsa `access_token` qaytsin.

**Kutiladigan natija:** Swagger da Authorize ishlaydi.

### 10. get_current_user · qiyin
Tokenni tekshirib `User` qaytaruvchi dependency yozing.

**Kutiladigan natija:** `/auth/me` o'z ma'lumotingizni qaytaradi.

### 11. Admin himoyasi · qiyin
`get_current_admin` yozing va oddiy foydalanuvchi uchun 403 olishni isbotlang.

**Kutiladigan natija:** 403 Forbidden.

### 12. Token muddati · bonus
`access_token_expire_minutes=1` qilib, 1 daqiqadan keyin `/auth/me` 401 berishini tekshiring va refresh token g'oyasini tushuntiring.

**Kutiladigan natija:** 1 daqiqadan keyin 401.

## O'zingizni tekshiring

1. Identifikatsiya va autentifikatsiya farqi?
2. Session va JWT farqi?
3. JWT qismlari?
4. Nega parol xeshlanadi?
5. `OAuth2PasswordBearer` nima qiladi?
6. 401 va 403 farqi?
7. `get_current_user` nima qiladi?

## Uyga vazifa

register, login, `/auth/me` va admin dependency vazifalarini bajaring (25 daqiqa). To'liq shart: `uyga-vazifa.md`.
