# 3-dars. Model, View va Serializer. Routerlar

> Django REST Framework ning yuragi — bu Model, Serializer, View va Router komponentlarining o'zaro mukammal uyg'unligidir. Ushbu darsda biz NewsPortal tizimining to'liq ishlaydigan dastlabki REST API endpointlarini quramiz va N+1 muammosini hal etishni o'rganamiz.

## Dars xulosasi

- **Django ORM** orqali Python sinflari ma'lumotlar bazasi jadvallariga aylanadi; `TimeStampedModel` abstrakt modeli barcha jadvallar uchun `created_at` va `updated_at` maydonlarini avtomatik ta'minlaydi.
- **Serializer** — Django model obyektlari (QuerySet) va JSON formati o'rtasidagi asosiy ko'prikdir: ma'lumotlarni o'qiydi (serialization) va kiruvchi so'rovlarni qat'iy tekshiradi (deserialization).
- O'qish (Read) va Yozish (Write) amallarining talabi turlicha: shuning uchun `PostListSerializer` (nested ma'lumotlar bilan) va `PostWriteSerializer` (oddiy ID lar bilan) ajratib yoziladi.
- **N+1 muammosi** — bir nechta bog'langan obyektlarni so'rashda serverning bazaga yuzlab keraksiz so'rovlar yuborib sekinlashishi.
- `select_related()` (ForeignKey uchun) va `prefetch_related()` (ManyToMany uchun) yordamida N+1 muammosi to'liq bartaraf etiladi.
- **ModelViewSet** — barcha CRUD (Create, Retrieve, Update, Destroy) amallarini bir joyda jamlaydi, `get_serializer_class()` metodi esa amalga qarab serializer tanlaydi.
- **DefaultRouter** — bir necha qator kod bilan xalqaro REST standartlariga mos barcha URL marshrutlarni avtomatik tarzda yaratadi.

## Qo'shimcha ma'lumot

### 1. Serializer qanday ishlaydi: Ma'lumot bojxonasi

Tasavvur qiling, Serializer bu — dasturingizning ma'lumotlar bojxona nazoratidir:
- **Eksport (Serialization):** Siz bazadan ma'lumotni tashqi dunyoga chiqarmoqchisiz. Serializer murakkab Python obyektini oladi, uning ichidagi maxfiy narsalarni (masalan, foydalanuvchi parolini) yashiradi va brauzer tushunadigan toza JSON formatiga qadoqlaydi.
- **Import (Deserialization & Validation):** Tashqi dunyodan kimdir sizning bazangizga yangi maqola yozmoqchi. Serializer kelgan ma'lumotni tekshiradi: sarlavha bormi? Uzunligi to'g'rimi? Rasm formati to'g'rimi? Agar hammasi to'g'ri bo'lsa (`serializer.is_valid()`), uni bazaga kiritadi. Agar xato bo'lsa, aniq tushuntirish bilan rad etadi (`400 Bad Request`).

### 2. N+1 muammosi: Real hayotiy misol

Tasavvur qiling, o'qituvchi sinfdagi 30 ta o'quvchining qaysi shahardan ekanligini bilmoqchi.
- **N+1 usuli (yomon):** O'qituvchi bitta-bitta har bir o'quvchining oldiga borib: "Sen qaysi shahardansan?" deb 30 marta so'raydi. Jami: 1 ta umumiy ro'yxat + 30 ta alohida savol = 31 ta harakat!
- **`select_related` usuli (aqlli):** O'qituvchi ro'yxatni ochgandayoq har bir o'quvchining ismi yonida uning shahri yozilgan bitta umumiy ro'yxatni oladi (SQL JOIN). Jami: bor-yo'g'i 1 ta harakat!
`select_related` server tezligini 10 barobargacha oshiradi.

### 3. `lookup_field = "slug"` afzalligi

Standart holatda DRF bitta maqolani ID bo'yicha qidiradi:
`GET /api/v1/posts/14/`
Ammo foydalanuvchi va qidiruv tizimlari uchun bu manzil hech narsani anglatmaydi.
Biz ViewSet ichiga `lookup_field = "slug"` yozganimiz sababli, manzil bunday go'zal shaklga keladi:
`GET /api/v1/posts/suniy-intellekt-yutuqlari/`

### 4. Dasturchilar ko'p yo'l qo'yadigan xatolar

- **Xato 1: `makemigrations` dan so'ng `migrate` qilishni unutish.** O'quvchi modelga yangi maydon qo'shadi va `makemigrations` qiladi, lekin `migrate` qilmaydi. Keyin server ishga tushganda `OperationalError: no such column` xatosi chiqadi.
- **Xato 2: ManyToMany maydonni `select_related` bilan ishlatish.** `select_related` faqat `ForeignKey` va `OneToOne` uchun ishlaydi. `ManyToMany` uchun esa albatta `prefetch_related` ishlatilishi shart!

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **QuerySet** | Django ORM da ma'lumotlar bazasidan olingan obyektlar to'plami. |
| **Serialization** | Python/Django ma'lumotlarini JSON formatiga o'girish jarayoni. |
| **Deserialization** | Kiruvchi JSON ma'lumotlarini Python formatiga va model obyektiga aylantirish jarayoni. |
| **ModelSerializer** | Django modeli asosida avtomatik serializer maydonlarini shakllantiruvchi qulay DRF klassi. |
| **ModelViewSet** | Model uchun barcha standart CRUD amallarini ta'minlovchi to'liq boshqaruv klassi. |
| **DefaultRouter** | ViewSetlar uchun standart RESTful URL larni avtomatik tarzda shakllantiruvchi vosita. |
| **N+1 muammosi** | Bog'langan jadvallarni noto'g'ri so'rash oqibatida yuzaga keladigan ortiqcha SQL so'rovlar muammosi. |
| **select_related** | `ForeignKey` bog'lanishlarini bitta SQL `JOIN` so'rovi bilan birlashtirib oluvchi optimizatsiya metodi. |
| **prefetch_related** | `ManyToMany` va teskari bog'lanishlarni alohida bitta qo'shimcha so'rov bilan birlashtiruvchi metod. |
| **Abstract Model** | O'zi uchun alohida jadval ochilmaydigan, faqat boshqa modellarga umumiy maydonlarni beruvchi model. |

## Bilasizmi?

- Django ORM da yozilgan bitta qator Python kodi (masalan, `Post.objects.select_related('category').all()`) orqa fonda murakkab va optimallashgan SQL `INNER JOIN` yoki `LEFT OUTER JOIN` so'roviga aylanadi.
- Instagram loyihasi har kuni yuz millionlab so'rovlarni qabul qiladi va uning backend qismida aynan Django va uning optimallashtirilgan QuerySet mexanizmlari ishlaydi!
- `DefaultRouter` faqat JSON emas, balki so'rov oxiriga `.json` qo'shilganda mos formatni beruvchi format-suffix (`/posts.json`) xususiyatini ham o'z ichiga oladi.

## Topshiriqlar

### 1. Serializer maydonlarini belgilash · oson
`Category` modeli uchun `CategorySerializer` klassida quyidagi qaysi maydonlar bo'lishi kerakligini aniqlang:
`id`, `name`, `slug`, `created_at`. Ushbu serializer kodini yozing.
**Kutiladigan natija:** To'g'ri sintaksis bilan yozilgan `CategorySerializer` kodi.

### 2. Router ro'yxatdan o'tkazish · oson
`TagViewSet` nomli ViewSet-ni `DefaultRouter` ga `tags` prefiksi bilan ro'yxatdan o'tkazish kodini yozing.
**Kutiladigan natija:** `router.register(...)` buyrug'i.

### 3. Migratsiya buyruqlari maqsadi · oson
`python manage.py makemigrations` va `python manage.py migrate` buyruqlarining har birining vazifasini 1 tadan gap bilan tushuntiring.
**Kutiladigan natija:** Ikkala buyruq vazifasining qisqa va aniq ta'rifi.

### 4. lookup_field vazifasi · oson
Standart DRF da maqola tafsilotini olish manzili: `/api/v1/posts/1/`.
Agar ViewSet ichida `lookup_field = "slug"` deb belgilansa, qidiruv qaysi parametr orqali amalga oshadi va URL qanday ko'rinishga keladi?
**Kutiladigan natija:** Yangi URL namunasi va tushuntirish.

### 5. N+1 muammosini aniqlash va tuzatish · o'rta
Quyidagi kodda N+1 muammosi mavjud. Muammoni tushuntiring va kodni optimallashtiring:
```python
class CommentViewSet(viewsets.ModelViewSet):
    # Har bir izoh uchun post va parent alohida SQL so'rovi bilan olinmoqda
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
```
**Kutiladigan natija:** Muammo izohi va `select_related` qo'shilgan to'g'rilangan kod.

### 6. Read va Write serializerlarini taqqoslash · o'rta
Nima uchun yangiliklar maqolasi uchun `PostListSerializer` da kategoriya obyekt sifatida (nested: `id`, `name`, `slug`), yangi maqola yaratishda esa `PostWriteSerializer` da shunchaki integer ID sifatida qabul qilinadi?
Bu qoidaning frontend dasturchilar uchun qanday 2 ta afzalligi bor?
**Kutiladigan natija:** Sababi va frontend uchun afzalliklari yozilgan tahlil.

### 7. Daraxtsimon (Threaded) izohlar serializeri · o'rta
`Comment` modelida bitta izohga javob sifatida yozilgan izohlarni ifodalash uchun serializerda `parent` maydoni qanday ishlaydi? Agar izoh to'g'ridan-to'g'ri maqolaning o'ziga yozilgan bo'lsa, `parent` qiymati qanday bo'ladi?
**Kutiladigan natija:** Daraxtsimon izohlar tuzilishi va `parent=null` holati tushuntirilishi.

### 8. Kod tahlili: get_serializer_class · o'rta
Quyidagi metodni tahlil qiling:
```python
def get_serializer_class(self):
    if self.action in ("create", "update", "partial_update"):
        return PostWriteSerializer
    if self.action == "retrieve":
        return PostDetailSerializer
    return PostListSerializer
```
Foydalanuvchi `GET /api/v1/posts/` so'rovini yuborganda qaysi serializer ishlaydi? `POST /api/v1/posts/` so'rovida-chi?
**Kutiladigan natija:** Har ikki holat uchun ishga tushadigan aniq serializer nomi va sababi.

### 9. Mini-loyiha: Kitoblar portali ViewSet va Routeri · qiyin
Elektron kitoblar do'koni uchun:
1. `Book` modeli uchun `BookViewSet` yozing (undagi `author` va `genre` maydonlari uchun `select_related` qo'llansin).
2. `DefaultRouter` orqali uni `books` nomli endpointga ulang.
3. Hosil bo'ladigan barcha 5 ta standart REST yo'nalishlarini (HTTP metod + URL) yozib chiqing.
**Kutiladigan natija:** To'liq ViewSet, Router kodi va 5 ta endpoint ro'yxati.

### 10. Serializer Custom Validation (Validatsiya) · qiyin
`PostWriteSerializer` ichida maqola sarlavhasi (`title`) kamida 5 ta belgidan iborat bo'lishini va unda nomaqbul so'zlar bo'lmasligini tekshiruvchi maxsus validatsiya metodini (`validate_title`) qanday yozish mumkin?
Kod strukturasini yozing va qoida buzilganda qanday istisno (`serializers.ValidationError`) qaytarilishini ko'rsating.
**Kutiladigan natija:** `validate_title` metodi kodi va xatolik matni.

### 11. ReadOnlyField va SerializerMethodField tadqiqoti · qiyin
Ba'zi maydonlar ma'lumotlar bazasida saqlanmaydi, lekin hisoblab chiqariladi (masalan, maqola o'qilish vaqti: `reading_time_minutes` yoki izohlar soni: `comments_count`).
1. DRF dagi `SerializerMethodField` qanday ishlaydi?
2. Maqolaning so'zlar sonidan kelib chiqib o'qish daqiqasini hisoblab beruvchi `get_reading_time_minutes(self, obj)` funksiyasini qanday yozish mumkin?
**Kutiladigan natija:** `SerializerMethodField` mexanizmi va namunaviy kod.

### 12. Bonus tadqiqot: Django Signals va avtomatik slug · bonus
Biz modelning `save()` metodi ichida `slugify` ishlatdik.
Biroq Django-da bu vazifani `pre_save` signallari (signals) orqali ham qilish mumkin.
1. Django Signals nima va u qanday ishlaydi?
2. `save()` metodini qayta yozish bilan `pre_save` signaldan foydalanishning qanday farqlari bor?
3. Qaysi usul kattaroq loyihalarda afzal ko'riladi?
**Kutiladigan natija:** Django signallari va model `save()` usulini qiyoslovchi mustaqil tahlil.

## O'zingizni tekshiring

1. `TimeStampedModel` kabi abstrakt modellarning maqsadi nima?
2. Serializatsiya va Deserializatsiya jarayonlarining tub farqini ayting.
3. N+1 muammosi qanday oqibatlarga olib keladi va uni Django ORM da qanday vositalar hal qiladi?
4. `select_related` qaysi relyatsiyalarda, `prefetch_related` qaysi relyatsiyalarda qo'llaniladi?
5. `ModelViewSet` qanday standart harakatlarni (actions) o'z ichiga oladi?
6. `DefaultRouter` dasturchining qancha vaqtini tejaydi va u qanday marshrutlarni ochadi?

## Uyga vazifa

1. Konspektdagi `CategorySerializer`, `TagSerializer` va `PostListSerializer` kodlarini o'z loyihangizda yozing.
2. `apps/news/views.py` da `CategoryViewSet` va `PostViewSet` ni yarating, ularni `DefaultRouter` orqali `config/urls.py` ga ulang.
3. Serverni ishga tushirib, brauzer orqali `http://127.0.0.1:8000/api/v1/posts/` manzilini oching va Browsable API yordamida kamida 2 ta kategoriya va 3 ta yangilik yarating.
