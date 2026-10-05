---
title: "10-dars. API havfsizligini ta'minlash"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (Python)", "link": "/10-sinf-python/"}, "week": {"n": 4, "link": "/10-sinf-python/hafta-04/"}, "g": 10, "title": "API havfsizligini ta'minlash", "lead": "Qalin devorli binoning ochiq eshigi: sizning API ingiz ham shunday bo'lmasin! Bu darsda JWT, ruxsatlar, throttling, CORS va production sozlamalari bilan API ni haker hujumlaridan himoyalashni o'rganasiz.", "slide": "/slaydlar/10-sinf-python/hafta-04/dars-1.html", "test": "/slaydlar/10-sinf-python/hafta-04/dars-1-test.html", "tabs": [{"g": 10, "link": "/10-sinf-python/hafta-04/dars-1", "current": true}, {"g": 11, "link": "/10-sinf-python/hafta-04/dars-2", "current": false}, {"g": 12, "link": "/10-sinf-python/hafta-04/dars-3", "current": false}], "prev": null, "next": {"g": 11, "title": "Tayyor loyihani hostingga joylash (deploy)", "link": "/10-sinf-python/hafta-04/dars-2"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- API xavfsizligi — ruxsatsiz kirish, ma'lumot o'g'irlash va tizimni ishdan chiqarishning oldini olish mexanizmlari yig'indisi.
- **Defense in Depth:** bitta qulfga ishonmaymiz, bir necha himoya qatlami quramiz.
- **Authentication** — «siz kimsiz?», **Authorization (Permissions)** — «nima qila olasiz?».
- DRF da Basic, Session va Token autentifikatsiyasi bor; zamonaviy yechim — **JWT** (Header.Payload.Signature).
- Access token qisqa (5-15 daqiqa), Refresh token uzoq yashaydi; rotate + blacklist xavfni kamaytiradi.
- **Throttling** brute-force va DDoS dan himoya qiladi, limit oshsa `429`.
- **CORS** — brauzerda domenlararo ruxsat, **CSRF** — cookie asosidagi soxta so'rov hujumi.
- Productionda `DEBUG=False`, `.env`, HTTPS, security headers va checklist majburiy.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. 401 va 403: qanday farqlash mumkin?
Kinoteatrni tasavvur qiling. Chipta so'ralganda siz hech narsa ko'rsata olmasangiz, sizni tanimaydilar: bu **401** (kimligingiz noma'lum). Chiptangiz bor, lekin u oddiy zalniki, siz VIP zalga kirmoqchisiz: bu **403** (kimligingiz ma'lum, lekin taqiqlangan).

### 2. Nega JWT bazaga murojaat qilmaydi?
Oddiy token «mehmonxona kaliti» kabi: administrator har safar kitobdan tekshiradi. JWT esa «muhrli chipta» kabi: muhrning o'zi haqiqiyligini ko'rsatadi. Server `SECRET_KEY` bilan imzoni qayta hisoblaydi, mos kelmasa token soxta.

```python
# Payload ni o'zgartirishga urinish: imzo mos kelmaydi
# user_id=5 -> user_id=1 qilsangiz, Signature endi yaroqsiz
```

### 3. Custom permission qanday ishlaydi
```python
class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated      # URL ga kira oladimi?

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user         # aynan shu postga haqlimi?
```
Birinchi funksiya «eshikdan o'tish», ikkinchisi «ma'lum bir xonaga kirish» desak bo'ladi.

### 4. Odatiy xatolar
- Payload ichiga parol yozish (u shifrlanmagan!).
- Productionda `DEBUG = True` qoldirish: xato sahifasida sirlar ko'rinishi mumkin.
- `SECRET_KEY` va DB parolini GitHub ga yuklash.
- Login endpoint uchun throttling qo'ymaslik.
- `CORS_ALLOW_ALL_ORIGINS = True` ni productionda qoldirish.

### 5. Nega faqat JWT bilan CSRF kerak emas?
CSRF hujumi brauzer cookie ni **avtomatik** yuborishiga tayanadi. JWT ni esa frontend kodi har safar `Authorization` headeriga o'zi qo'shadi; brauzer uni boshqa saytga o'zi yubormaydi.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Authentication | Foydalanuvchi kimligini aniqlash |
| Authorization | Foydalanuvchining nimaga haqi borligini tekshirish |
| JWT | JSON Web Token: o'z to'g'riligini o'zi tasdiqlovchi token |
| Payload | JWT ning ma'lumot qismi (shifrlanmagan) |
| Signature | Maxfiy kalit bilan hosil qilingan raqamli imzo |
| Access token | Har so'rovda yuboriladigan qisqa muddatli token |
| Refresh token | Yangi Access olish uchun uzoq muddatli token |
| Throttling | Vaqt birligida so'rovlar sonini cheklash |
| CORS | Domenlararo resurs almashinuvi |
| CSRF | Saytlararo so'rovni soxtalashtirish hujumi |
| SQL Injection | Kiritish maydoniga SQL buyrug'i yozib bazaga zarar yetkazish |
| XSS | Izohga JavaScript kodi joylash hujumi |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Base64 shifrlash emas, shunchaki kodlash formati: uni istalgan odam bir zumda o'qiy oladi.
- Brute-force hujumida bot sekundiga minglab parolni sinab ko'rishi mumkin. Shu sababli login uchun alohida qattiq limit qo'yiladi.
- `HSTS` brauzerga «bu saytga faqat HTTPS orqali kir» deb ko'rsatma beradi; qo'llanmada u 1 yilga (31536000 soniya) sozlanadi.
- «Never trust user input» (foydalanuvchi ma'lumotiga hech qachon ishonmang) — xavfsizlikning oltin qoidasi.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Atamalarni juftlang <Badge type="tip" text="oson" />
Quyidagilarni juftlang: Authentication, Authorization, Throttling, CORS va ularga mos savollar: «Nima qila olasiz?», «Siz kimsiz?», «Necha marta?», «Qaysi domen kira oladi?».

**Kutiladigan natija:** 4 ta to'g'ri juftlik.

### 2. Status kodlari <Badge type="tip" text="oson" />
Quyidagi holatlarga qaysi status kodi mos: (a) token yuborilmadi; (b) token bor, lekin boshqa odamning postini o'zgartirmoqchi; (c) bir daqiqada limitdan ko'p so'rov.

**Kutiladigan natija:** a) 401, b) 403, c) 429.

### 3. JWT qismlari <Badge type="tip" text="oson" />
JWT uchta qismini tartib bilan yozing va har biri nimani saqlashini bir jumlada ayting.

**Kutiladigan natija:** Header (tur va algoritm), Payload (ID, iat, exp), Signature (maxfiy kalit bilan imzo).

### 4. Xavfli yoki xavfsiz? <Badge type="tip" text="oson" />
Qaysi biri production uchun xavfli: `DEBUG = True`, `ALLOWED_HOSTS = ["api.loyiha.uz"]`, `CORS_ALLOW_ALL_ORIGINS = True`, `SECRET_KEY` ni `.env` da saqlash.

**Kutiladigan natija:** Xavfli: birinchi va uchinchisi.

### 5. SimpleJWT sozlash <Badge type="warning" text="o'rta" />
`settings/base.py` ga Access 10 daqiqa, Refresh 7 kun, rotate va blacklist yoqilgan `SIMPLE_JWT` ni yozing va `INSTALLED_APPS` ga blacklist ilovasini qo'shing.

**Kutiladigan natija:** `python manage.py migrate` xatosiz o'tadi, login javobida `access` va `refresh` tokenlar keladi.

### 6. Bu kod nima qaytaradi? <Badge type="warning" text="o'rta" />
```python
class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
```
Ali yozgan postni Vali PATCH qilmoqchi. Qaysi status qaytadi va nega?

**Kutiladigan natija:** `403 Forbidden`, chunki `obj.author != request.user`.

### 7. Throttling hisoblash <Badge type="warning" text="o'rta" />
`anon: 60/min`, `login_anon: 5/min`. Mehmon 1 daqiqada login sahifasiga 8 marta urindi. Nechanchi urinishdan boshlab `429` olinadi?

**Kutiladigan natija:** 6-urinishdan boshlab (5 tasi o'tadi).

### 8. Xatoni toping <Badge type="warning" text="o'rta" />
```python
payload = {"user_id": 5, "password": "secret123", "exp": 1700000000}
```
Bu JWT payload ida qanday jiddiy xato bor va uni qanday tuzatasiz?

**Kutiladigan natija:** Parol payload da (u shifrlanmagan); parol olib tashlanadi, faqat `user_id`, `iat`, `exp` qoladi.

### 9. Upload validatsiyasi <Badge type="danger" text="qiyin" />
`PostCoverUploadSerializer` uchun `validate_cover_image` metodini yozing: faqat JPEG/PNG/WEBP va 5 MB gacha.

**Kutiladigan natija:** PDF fayl yuklansa va 6 MB rasm yuklansa `ValidationError` qaytadi.

### 10. Custom permission yozish <Badge type="danger" text="qiyin" />
`IsAuthorOrReadOnly` permission yozing: GET so'rovlari hammaga ochiq, o'zgartirish faqat muallifga.

**Kutiladigan natija:** Mehmon GET qila oladi, boshqa user PATCH qilsa 403.

### 11. Himoya zanjiri sxemasi <Badge type="danger" text="qiyin" />
Bitta so'rov API ga kelganda o'tadigan 4 himoya qatlamini (tartib bilan) chizing va har qatlam qaysi hujumdan saqlashini yozing.

**Kutiladigan natija:** Authentication, Permissions, Throttling, Validatsiya zanjiri va har biriga hujum turi.

### 12. Audit (mini-loyiha) <Badge type="info" text="bonus" />
O'z NewsPortal loyihangizni qo'llanmadagi 9 bandli security checklist bo'yicha tekshiring va natijani jadvalga yozing (bor / yo'q / tuzatildi).

**Kutiladigan natija:** Kamida 3 ta tuzatilgan band, jadval va qisqa izoh.

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Authentication va Authorization farqini o'z so'zingiz bilan tushuntiring.
2. Nima uchun Basic Authentication productionda ishlatilmaydi?
3. JWT ning Signature qismi nima uchun kerak?
4. Access va Refresh tokenlar nega ikkiga bo'lingan?
5. `has_permission` va `has_object_permission` qachon ishlatiladi?
6. CORS qanday muammoni hal qiladi?
7. Qaysi autentifikatsiya turida CSRF token zarur va nega?
8. SQL Injection ga qarshi DRF da qanday to'siqlar bor?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

(20-30 daqiqa) `settings/base.py` ga `SIMPLE_JWT` ni sozlang, `IsAuthor` permissionini yozib PostViewSet ga ulang va security checklist bo'yicha loyihangizdagi kamida 3 ta kamchilikni topib tuzating. To'liq ro'yxat: `uyga-vazifa.md`.

</div>

