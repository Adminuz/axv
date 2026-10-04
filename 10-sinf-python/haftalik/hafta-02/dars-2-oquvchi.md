# 5-dars. Ruxsatlar bilan ishlash

> Tizimga kirish yetarli emas — har bir foydalanuvchining o'z chegarasi va vakolati bo'lishi shart! Ushbu darsda biz Django REST Framework ning ruxsatlar (Permissions) mexanizmi bilan tanishamiz va o'z maqolasini faqat uning muallifigina tahrirlay oladigan xavfsiz tizim quramiz.

## Dars xulosasi

- **Autentifikatsiya** foydalanuvchining shaxsini aniqlaydi, **Permission (Ruxsat)** esa uning qanday amallarni bajarishga haqli ekanligini belgilaydi.
- Ruxsatsiz qoldirilgan tizimlarda foydalanuvchilar bir-birining shaxsiy ma'lumotlarini o'chirib yuborishi yoki boshqa birov nomidan maqola chop etishi mumkin (IDOR zaifligi).
- DRF tayyor ruxsat klasslariga ega: `AllowAny` (barcha uchun ochiq), `IsAuthenticated` (faqat ro'yxatdan o'tganlar), `IsAdminUser` (faqat adminlar), `IsAuthenticatedOrReadOnly` (o'qish barchaga, yozish faqat kirganlarga).
- **`BasePermission`** klassi yordamida o'zimizning maxsus qoidalarimizni yaratamiz: `has_permission` (umumiy so'rov) va `has_object_permission` (aniq bitta obyekt ustida amal).
- **`SAFE_METHODS`** (`GET`, `HEAD`, `OPTIONS`) ma'lumotlar bazasini o'zgartirmaydigan xavfsiz metodlar hisoblanadi.
- **`perform_create`** metodi orqali yangi maqola yoki izoh yaratilganda, uning muallifi sifatida joriy `request.user` server tomonida avtomatik biriktiriladi.

## Qo'shimcha ma'lumot

### 1. Mehmonxona analogiyasi: Kalit va Xona huquqlari

Ruxsatlar tizimini yaxshiroq tushunish uchun zamonaviy mehmonxonani tasavvur qiling:
- **Autentifikatsiya:** Siz qabulxonaga (reception) borib, pasportingizni ko'rsatasiz. Administrator sizga elektron plastik karta (Token) beradi.
- **Ruxsat (Permission):** Siz mehmonxonaning umumiy zali, restorani va liftidan foydalana olasiz (`AllowAny` yoki `IsAuthenticated`). Lekin 304-xonaning eshigiga kartangizni tekkizsangiz eshik ochiladi, qo'shni 305-xonaning eshigiga tekkizsangiz qizil chiroq yonadi (`IsOwnerOrStaff` &mdash; faqat o'z xonangizga kirish huquqingiz bor!).

### 2. IDOR (Insecure Direct Object Reference) nima?

Kiberxavfsizlikda eng keng tarqalgan xatolardan biri bu — IDOR deb ataladi.
Tasavvur qiling, Anvar o'zining maqolasini tahrirlamoqchi va havola bunday:
`PUT /api/v1/posts/15/`
Agar server faqat "Foydalanuvchi tizimga kirganmi?" deb tekshirsa-yu (`IsAuthenticated`), "Bu 15-raqamli maqola haqiqatan Anvarga tegishlimi?" deb tekshirmasa (`has_object_permission` yo'qligi), u holda Anvar havoladagi raqamni `PUT /api/v1/posts/16/` deb o'zgartirib, Begzodning maqolasini osongina buzib qo'yishi mumkin!

Biz yaratgan `IsOwnerOrStaff` klassi aynan shu xavfli teshikni to'liq yopadi!

### 3. `perform_create` nima uchun xavfsizlik talabi?

Agar biz maqola yaratish serializerida `author` maydonini oddiy qoldirsak:
```json
{
  "title": "Kutilmagan yangilik",
  "body": "Matn...",
  "author": 1
}
```
Yomon niyatli foydalanuvchi `author: 1` (bosh adminning ID raqami) deb yozib yuborishi va admin nomidan yolg'on xabarlar tarqatishi mumkin.
Shu sababli, `author` maydoni serializerda `read_only=True` qilinadi va ViewSet ichida serverning o'zi uni mustaqil qo'yadi:
`serializer.save(author=self.request.user)`

### 4. Dasturchilar ko'p yo'l qo'yadigan xatolar

- **Xato 1: `has_object_permission` ni `GET /api/v1/posts/` ro'yxatida kutish.** `has_object_permission` ro'yxat (list) chaqirilganda ISHLAMAYDI! U faqat bitta aniq obyekt ochilganda (detail: retrieve, update, destroy) ishlaydi. Ro'yxatni cheklash uchun esa `get_queryset()` metodida filtrlash kerak bo'ladi.
- **Xato 2: Superuser (Admin) uchun istisno qoldirmaslik.** Agar kodda faqat `obj.author == request.user` deb yozilsa, tizim bosh admini ham boshqa foydalanuvchilarning xato yoki nomaqbul maqolalarini o'chira olmay qoladi. Shuning uchun har doim `if user.is_staff: return True` sharti qo'shiladi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Permission (Ruxsat)** | Foydalanuvchining muayyan resurs yoki amalga nisbatan huquqlarini tekshiruvchi himoya qatlami. |
| **BasePermission** | DRF da maxsus (custom) ruxsat qoidalarini yozish uchun asosiy sinf. |
| **has_permission** | So'rovning umumiy darajadagi ruxsatini (endpointga kirish) tekshiruvchi metod. |
| **has_object_permission** | Aniq bitta obyekt ustida amal bajarilayotganda ishga tushuvchi metod. |
| **SAFE_METHODS** | Ma'lumotlarni o'zgartirmaydigan xavfsiz HTTP metodlar to'plami (`GET`, `HEAD`, `OPTIONS`). |
| **403 Forbidden** | Foydalanuvchining shaxsi ma'lum, ammo unga ushbu amalni bajarishga huquq yetarli emasligini bildiruvchi status. |
| **IDOR** | Obyektlarga to'g'ridan-to'g'ri havolani ruxsatsiz o'zgartirish orqali boshqa birovning ma'lumotlariga kirish zaifligi. |
| **perform_create** | DRF ViewSet da ma'lumot bazaga saqlanishidan avval qo'shimcha maydonlarni (masalan: muallif) biriktiruvchi metod. |
| **is_staff** | Djangoda foydalanuvchining xodim yoki administrator ekanligini ko'rsatuvchi mantiqiy bayroqcha. |
| **Object-level permission** | Har bir alohida ma'lumot qatori (obyekt) darajasida tekshiriladigan ruxsat. |

## Bilasizmi?

- Kiberxavfsizlik bo'yicha dunyodagi eng nufuzli tashkilot — OWASP (Open Web Application Security Project) talqiniga ko'ra, "Buzuq kirish nazorati" (Broken Access Control) dunyodagi veb-zaifliklar reytingida 1-o'rinda turadi!
- Django REST Framework permission tizimi shu qadar tez ishlaydiki, u ma'lumotlar bazasiga keraksiz ortiqcha og'ir so'rovlarni yubormasdan, xotiradagi `request.user` orqali mikrosoniyalarda tekshiruvni amalga oshiradi.
- Yirik bank va to'lov tizimlarida har bir tranzaksiya ustida kamida 4-5 xil murakkab permission qatlamlari bir vaqtning o'zida parallel ravishda tekshiriladi.

## Topshiriqlar

### 1. Standart ruxsat klasslarini tanlash · oson
Quyidagi vaziyatlar uchun qaysi standart DRF ruxsat klassi mos kelishini aniqlang:
a) Yangiliklar saytidagi maqolalar ro'yxatini hamma (mehmonlar ham) ko'rishi mumkin.
b) Faqat sayt xodimlari va administratorlar kira oladigan ichki hisobotlar sahifasi.
c) Maqolalarni hamma o'qiy oladi, lekin faqat tizimga kirganlargina yangi maqola yoza oladi.
**Kutiladigan natija:** 3 ta vaziyatga mos standart DRF klasslari nomlari.

### 2. SAFE_METHODS tahlili · oson
Quyidagi HTTP metodlaridan qaysilari `SAFE_METHODS` ro'yxatiga kiradi:
`GET`, `POST`, `PUT`, `DELETE`, `PATCH`, `HEAD`, `OPTIONS`.
Nima uchun `POST` ushbu ro'yxatga kiritilmagan?
**Kutiladigan natija:** Xavfsiz metodlar ro'yxati va `POST` kiritilmasligining sababi.

### 3. Status kodlari: 401 va 403 farqi · oson
Tizimga kirmagan (token yubormagan) foydalanuvchi yangi post yaratmoqchi bo'lsa, qanday status oladi?
Tizimga kirgan oddiy foydalanuvchi boshqa birovning postini o'chirmoqchi bo'lsa, qanday status oladi?
**Kutiladigan natija:** Har ikki holat uchun aniq HTTP status kodi (401 yoki 403).

### 4. has_permission va has_object_permission · oson
Ushbu ikkala metodning qaysi biri:
1. `GET /api/v1/posts/` so'rovida ishlaydi?
2. `DELETE /api/v1/posts/suniy-intellekt/` so'rovida ishlaydi?
**Kutiladigan natija:** Har bir endpointga mos metod nomi.

### 5. IsStaffOrReadOnly mantiqini yozish · o'rta
`apps/common/permissions.py` modulida `IsStaffOrReadOnly` klassini yozing.
Qoidalar:
- Agar so'rov `SAFE_METHODS` bo'lsa &mdash; `True` qaytsin;
- Aks holda &mdash; foydalanuvchi tizimga kirgan va `is_staff == True` bo'lsa `True`, boshqa barcha hollarda `False` qaytsin.
**Kutiladigan natija:** Sintaktik jihatdan to'liq va to'g'ri Python klassi.

### 6. perform_create orqali izoh muallifini saqlash · o'rta
`CommentViewSet` da foydalanuvchi maqolaga yangi izoh qoldirayotganda, uning `user` maydonini joriy tizimga kirgan foydalanuvchi (`self.request.user`) bilan avtomatik bog'lash kodini yozing.
**Kutiladigan natija:** `perform_create` metodining to'g'ri kodi.

### 7. IsOwnerOrStaff da xatolikni tuzatish · o'rta
Quyidagi ruxsat kodida jiddiy xavfsizlik xatosi mavjud:
```python
class IsOwnerOrStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Adminlar ham, muallif ham tekshirilgan, lekin nima xato?
        if request.user.is_staff or obj.author == request.user:
            return True
        return False
```
Agar tizimga kirmagan anonim mehmon maqolani o'qimoqchi bo'lib `GET /api/v1/posts/1/` so'rovini yuborsa nima yuz beradi? Xatoni qanday to'g'rilash kerak?
**Kutiladigan natija:** Xatolik sababi (`AttributeError: AnonymousUser`) va `SAFE_METHODS` qo'shilgan to'g'ri kod.

### 8. Muallif maydonini himoyalash · o'rta
Nima uchun `PostWriteSerializer` da `author` maydonini frontenddan qabul qilish xavfli va uni qanday qilib `read_only_fields` ga qo'shish yoki serializerdan chiqarib tashlash kerak?
**Kutiladigan natija:** Xavfsizlik tahlili va to'g'ri serializer konfiguratsiyasi.

### 9. Mini-loyiha: Faqat do'stlar o'qiy oladigan postlar · qiyin
Ijtimoiy tarmoq funksiyasini loyihalashtiring:
Har bir maqolada `is_private = models.BooleanField(default=False)` maydoni bor.
Agar `is_private == True` bo'lsa, uni faqat uning muallifi yoki admin o'qiy olsin, boshqalarga esa hatto `GET` so'rovida ham `403 Forbidden` xabari chiqsin.
`IsPostAuthorIfPrivate` nomli Custom Permission klassini yozing.
**Kutiladigan natija:** `has_object_permission` orqali to'liq ishlovchi maxsus ruxsat klassi.

### 10. IP manzil bo'yicha kirishni cheklovchi Permission · qiyin
Ba'zi maxfiy korporativ API larga faqat ma'lum bir IP manzillar doirasidan (masalan, faqat ofis tarmog'idan) kirishga ruxsat beriladi.
Mijozning IP manzilini `request.META.get('REMOTE_ADDR')` orqali olib, uni ruxsat berilgan IP manzillar ro'yxati (`ALLOWED_IPS = ['127.0.0.1', '192.168.1.100']`) bilan solishtiruvchi `IsWhitelistedIP` klassini yozing.
**Kutiladigan natija:** IP manzil tekshiruvchi to'liq permission klassi.

### 11. Role-Based Access Control (RBAC) tahlili · qiyin
Yirik tizimlarda oddiy `is_staff` yetarli bo'lmaydi, chunki turli xil rollar mavjud:
`Moderator`, `Muharrir`, `Bosh Muharrir`, `Menejer`, `Moliya bo'limi`.
1. Django-da bunday rollarni `models.TextChoices` yordamida User modelida qanday loyihalashtirish mumkin?
2. Muayyan bir endpointni faqat "Muharrir" va undan yuqori rollarga ochuvchi permission klassi qanday yoziladi?
**Kutiladigan natija:** Rollarga asoslangan ruxsatlar tizimi (RBAC) modeli va kodi.

### 12. Bonus tadqiqot: Django Guardian va Object-level Permissions · bonus
DRF dagi `has_object_permission` obyekt xotiraga yuklangandan keyin tekshiradi. Ammo bazada 1 millionta obyekt bo'lsa va foydalanuvchiga faqat o'zi ruxsati bor 10 ta obyektni ko'rsatish kerak bo'lsa-chi?
1. Django Guardian kutubxonasi ma'lumotlar bazasi darajasidagi ruxsatlarni (row-level permissions) qanday ta'minlaydi?
2. Standart Django guruhlari (`auth.Group`) va huquqlari (`auth.Permission`) dan DRF da qanday foydalanish mumkin?
**Kutiladigan natija:** Baza darajasidagi ruxsatlar bo'yicha qiziqarli mustaqil tadqiqot.

## O'zingizni tekshiring

1. Autentifikatsiya va Avtorizatsiya tushunchalarining asosiy farqi nimada?
2. `IsAuthenticatedOrReadOnly` klassi ro'yxatdan o'tmagan mehmonlarga qaysi HTTP metodlarni bajarishga ruxsat beradi?
3. `has_permission` bilan `has_object_permission` qaysi paytda ishga tushadi?
4. Kiberxavfsizlikda IDOR zaifligi nima va undan qanday himoyalanamiz?
5. `perform_create` metodining vazifasi nima va nega u xavfsizlik uchun muhim?
6. Bosh admin (`is_staff=True`) boshqa birovning maqolasini o'chira olishi uchun permission klassda qanday shart bo'lishi shart?

## Uyga vazifa

1. `src/apps/common/permissions.py` faylida `IsStaffOrReadOnly` va `IsOwnerOrStaff` klasslarini to'liq yozing.
2. `CategoryViewSet` va `TagViewSet` ga `permission_classes = (IsStaffOrReadOnly,)` sozlamasini ulang.
3. `PostViewSet` ga `permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrStaff)` ni qo'ying va `perform_create` metodini yozing.
4. Tizimda 2 ta foydalanuvchi ochib, 1-foydalanuvchining maqolasini 2-foydalanuvchi tahrirlay olmasligini (`403 Forbidden`) amalda sinab ko'ring.
