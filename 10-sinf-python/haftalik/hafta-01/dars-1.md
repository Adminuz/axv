# 1-dars. Django REST Framework. Server side rendering va user side rendering tushunchalari

## Dars rejasi (80 daqiqa)

1. **Tashkiliy qism va kirish (10 daqiqa):** 10-sinf dasturi bilan tanishuv, Advanced Python Back-end va Prompt Engineering kursi maqsadi, veb-dasturlashda mijoz (client) va server munosabatlari.
2. **Yangi mavzu: SSR va CSR/USR tushunchalari (25 daqiqa):**
   - Server-Side Rendering (SSR) mohiyati: HTML serverda shakllantirilishi, afzalliklari (SEO, birinchi yuklanish) va kamchiliklari (server yuki, to'liq refresh).
   - User/Client-Side Rendering (CSR/USR) mohiyati: brauzerda JavaScript orqali sahifa qurilishi, SPA arxitekturasi, afzalliklari (yuqori interaktivlik, server yukining kamayishi) va kamchiliklari (SEO murakkabligi, dastlabki yuklanish).
   - SSR va USR ni taqqoslash jadvali, qaysi loyihaga qaysi biri mosligi.
3. **Yangi mavzu: REST arxitekturasi va Django REST Framework (20 daqiqa):**
   - RESTful API tamoyillari: Stateless, Client-Server, Uniform Interface, HTTP metodlari (GET, POST, PUT, PATCH, DELETE).
   - Django REST Framework (DRF) nima, an'anaviy Django MTV dan farqi, JSON almashinuvi, Browsable API, Serializerlar va ViewSetlar roli.
4. **Amaliy topshiriqlar va muhokama (15 daqiqa):** Veb-ilovalar arxitekturasini tahlil qilish, HTTP status kodlari va JSON ma'lumotlar bilan ishlash mashqlari.
5. **Dars xulosasi va tezkor nazorat (10 daqiqa):** Savol-javob, o'quvchilarni baholash, uyga vazifa berish.

---

## Mentor konspekti

### 1. Veb dasturlash tushunchasi: Frontend va Backend

Veb-ilova ikki asosiy qismdan tashkil topadi:
- **Frontend (foydalanuvchi tomoni):** Foydalanuvchi ko'radigan interfeys, dizayn, tugmalar, shakllar va animatsiyalar. HTML (tuzilma), CSS (uslub) va JavaScript (interaktivlik) orqali yaratiladi.
- **Backend (server tomoni):** Foydalanuvchi ko'rmaydigan "sahna orti". Serverlar, ma'lumotlar bazalari, autentifikatsiya, biznes mantiq va xavfsizlik. Python (Django, FastAPI), Java, Go, Node.js kabi texnologiyalarda quriladi.

### 2. Server-Side Rendering (SSR)

**Ta'rif:** Web sahifaning HTML tarkibi serverda to'liq shakllantirilib, tayyor holda brauzerga yuboriladigan arxitektura.

**Ishlash tartibi:**
1. Foydalanuvchi brauzerga manzilni kiritadi: `GET /news/1/`.
2. So'rov serverga keladi. Django View ma'lumotlar bazasidan yangilikni oladi.
3. Django shablon dvigateli (`DTL - Django Template Language`) HTML shablon ichidagi `{{ post.title }}` va `{{ post.body }}` o'zgaruvchilarini ma'lumotlar bilan to'ldiradi.
4. To'liq shakllangan HTML hujjat brauzerga qaytariladi.
5. Brauzer HTML-ni o'qib, ekranda ko'rsatadi.

**Afzalliklari:**
- **SEO (Search Engine Optimization):** Google, Yandex botlari to'liq HTML-ni hech qanday qiyinchiliksiz o'qiydi va indekslaydi.
- **Birinchi ko'rinish tezligi (First Contentful Paint):** Foydalanuvchi sahifani darhol ko'radi, kutib qolmaydi.

**Kamchiliklari:**
- Har bir sahifaga o'tganda yoki forma yuborilganda butun sahifa qayta yuklanadi (refresh).
- Serverga yuklama katta bo'ladi, chunki har bir foydalanuvchi uchun HTML qaytadan render qilinadi.

### 3. User-Side Rendering (USR / CSR)

**Ta'rif:** Server brauzerga bo'shroq HTML skeletini va JavaScript kodini yuboradi. Sahifaning to'liq ko'rinishi foydalanuvchi qurilmasida (brauzerda) JavaScript orqali dinamik yig'iladi.

**Ishlash tartibi:**
1. Foydalanuvchi saytga kiradi: `GET /`.
2. Server bitta bo'sh HTML (`<div id="root"></div>`) va JS fayllarni yuboradi.
3. Brauzer JS kodni ishga tushiradi va backend API serveriga ma'lumot so'rab asinxron so'rov (AJAX / Fetch) yuboradi: `GET /api/v1/posts/1/`.
4. Backend API faqat toza ma'lumotni (JSON formatida) qaytaradi.
5. Brauzerdagi JS (React, Vue, Flutter Web) ushbu JSON-ni qabul qilib, DOM elementlarini o'zi yaratadi.

**Afzalliklari:**
- **Yuqori interaktivlik va SPA (Single Page Application):** Sahifa qayta yuklanmaydi, o'zgarishlar bir zumda ekranda namoyon bo'ladi.
- **Server yukining keskin kamayishi:** Server HTML render qilmaydi, faqat JSON uzatadi.
- **Bitta backend — ko'p frontend:** Yaratilgan REST API-dan bir vaqtning o'zida Web, iOS, Android va Telegram bot foydalanishi mumkin!

**Kamchiliklari:**
- Dastlabki yuklanish og'ir bo'lishi mumkin (katta hajmdagi JS fayllarni yuklab olish talab etiladi).
- SEO uchun qo'shimcha choralarni (Next.js, Nuxt.js yoki Prerender) talab qiladi.

### 4. Taqqoslash jadvali

| Xususiyat | Server-Side Rendering (SSR) | User-Side Rendering (CSR/USR) |
|---|---|---|
| **Render joyi** | Serverda | Foydalanuvchi brauzerida |
| **SEO samaradorligi** | A'lo darajada | Murakkabroq |
| **Dastlabki yuklanish** | Juda tez | Sekinroq (JS yuklanguncha) |
| **Keyingi harakatlar** | Butun sahifa yangilanadi | Faqat kerakli komponent yangilanadi |
| **Server yuklamasi** | Yuqori | Minimal (faqat JSON API) |
| **Mos keladigan loyihalar** | Yangiliklar portallari, bloglar, e-tijorat | Admin panellar, ijtimoiy tarmoqlar, dashboardlar |

### 5. REST arxitekturasi va Django REST Framework

**REST (Representational State Transfer)** — bu tarmoqdagi tizimlar o'rtasida ma'lumot almashish uchun arxitektura tamoyillari to'plamidir.
- **Stateless (Holatsiz):** Har bir so'rov mustaqil, server oldingi so'rov holatini eslab qolmaydi. Barcha kerakli ma'lumot (token, parametrlar) so'rovning o'zida bo'ladi.
- **Client-Server ajratilganligi:** Foydalanuvchi interfeysi va backend mustaqil rivojlanadi.
- **Uniform Interface:** Resurslar aniq URL orqali murojaat qilinadi va standart HTTP metodlari orqali boshqariladi.

**Django REST Framework (DRF):**
Django asosida professional darajadagi RESTful API qurishga imkon beruvchi vositalar to'plamidir. U quyidagi tayyor yechimlarni beradi:
- **Web Browsable API:** Brauzer orqali API-ni to'g'ridan-to'g'ri testlash va ko'rish interfeysi.
- **Serializers:** Python/Django modellarini JSON-ga va aksincha, kelgan JSON-ni Python obyektlariga tekshirib (validatsiya qilib) o'tkazish.
- **ViewSets & Routers:** URL marshrutlarni va CRUD logikasini bir necha qator kodda yaratish.
- **Keng qamrovli xavfsizlik:** Token, JWT, OAuth va Session autentifikatsiyasi.

---

## Kod namunalari

### 1. Django an'anaviy SSR View (HTML qaytaradi)

```python
# Klassik Django (SSR): HTML render qiladi
from django.shortcuts import render
from .models import Post

def post_list_view(request):
    posts = Post.objects.filter(status='published')
    # Server shablonni to'ldirib, tayyor HTML qaytaradi
    return render(request, 'news/post_list.html', {'posts': posts})
```

### 2. Django REST Framework USR View (JSON qaytaradi)

```python
# Django REST Framework (CSR/USR uchun API): JSON qaytaradi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostListSerializer

class PostListAPIView(APIView):
    def get(self, request):
        posts = Post.objects.filter(status='published')
        # Serializer orqali Python queryset JSON formatiga o'giriladi
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
```

### 3. API qaytaradigan namunaviy JSON strukturasi

```json
[
  {
    "id": 1,
    "title": "Sun'iy intellekt sohasidagi yangi yutuqlar",
    "slug": "suniy-intellekt-yutuqlari",
    "excerpt": "O'zbekistonda yosh dasturchilar AI loyihalarini yaratmoqda.",
    "category": {
      "id": 2,
      "name": "Texnologiya",
      "slug": "texnologiya"
    },
    "created_at": "2026-10-04T10:30:00Z"
  }
]
```

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq (Oson): Veb-arxitektura modellarini ajratish
Quyidagi loyihalar uchun qaysi rendering usuli (SSR yoki USR) mos kelishini aniqlang va sababini tushuntiring:
a) Kun.uz yangiliklar portali.
b) Trello vazifalar boshqaruv doskasi (drag-and-drop).
c) Maktab o'quvchilarining shaxsiy baho va davomat kabineti (kundalik).

**Yechim:**
- a) Kun.uz — **SSR**. Sababi: Qidiruv tizimlari (Google, Yandex) orqali yangiliklar tez indekslanishi shart, SEO juda muhim va kontent asosan o'qish uchun mo'ljallangan.
- b) Trello — **USR (CSR)**. Sababi: Karta ko'chirish, vazifa yaratish yuqori darajada interaktivlikni talab qiladi, sahifa qayta yuklanmasligi kerak (SPA).
- c) Shaxsiy baho va davomat kabineti — **USR (yoki gibrid)**. Sababi: Tizim parolli shaxsiy hudud bo'lgani sababli SEO umuman kerak emas, interaktiv filtrlar va tezkor yangilanish qulay tajriba beradi.

### 2-topshiriq (O'rta): HTTP metodlari va CRUD mosligi
RESTful API-da quyidagi amallarni bajarish uchun qaysi HTTP metodi va qanday URL endpoint ishlatilishi kerakligini yozing:
1. Yangi maqola yaratish
2. Barcha maqolalar ro'yxatini olish
3. 5-raqamli maqolaning to'liq ma'lumotini ko'rish
4. 5-raqamli maqola sarlavhasini qisman o'zgartirish
5. 5-raqamli maqolani o'chirib tashlash

**Yechim:**
1. `POST /api/v1/posts/`
2. `GET /api/v1/posts/`
3. `GET /api/v1/posts/5/`
4. `PATCH /api/v1/posts/5/` (to'liq almashtirish uchun `PUT /api/v1/posts/5/`)
5. `DELETE /api/v1/posts/5/`

### 3-topshiriq (Qiyin): JSON strukturasi va Serializer model loyihasi
O'quvchilar onlayn kutubxona uchun API yaratmoqda. "Kitob" (Book) resursi uchun minimal JSON modelini loyihalashtiring: kitob id, nomi, muallifi (ismi va emaili bilan nested obyekt), narxi, mavjudligi (boolean) va yaratilgan sanasi bo'lsin.

**Yechim:**
```json
{
  "id": 101,
  "title": "Toza Kod (Clean Code)",
  "author": {
    "id": 12,
    "full_name": "Robert Martin",
    "email": "unclebob@example.com"
  },
  "price": 85000.00,
  "is_available": true,
  "published_at": "2026-05-15T09:00:00Z"
}
```

---

## Tezkor nazorat savollari

1. Server-Side Rendering (SSR) modelida HTML sahifa qayerda tayyorlanadi?
   - **Javob:** Serverda tayyorlanadi va to'liq shaklda brauzerga yuboriladi.
2. User-Side Rendering (USR/CSR) yondashuvida brauzer serverdan qanday formatda ma'lumot oladi?
   - **Javob:** Asosan toza ma'lumot sifatida JSON (yoki XML) formatida oladi.
3. Nima uchun qidiruv tizimlari (Google bot) SSR sahifalarni CSR ga qaraganda osonroq tahlil qiladi?
   - **Javob:** Chunki SSR da serverdan tayyor matnli HTML keladi, CSR da esa bot JavaScriptni ishga tushirishi va ma'lumot kelishini kutishi kerak bo'ladi.
4. RESTful API arxitekturasida "Stateless" tamoyili nimani anglatadi?
   - **Javob:** Har bir so'rov mustaqil ekanligini, server oldingi so'rov holatini sessiyada eslab qolmasligini anglatadi.
5. Django REST Framework-da Serializer qanday asosiy vazifani bajaradi?
   - **Javob:** Python/Django modellarini JSON formatiga va aksincha, kelgan JSON ma'lumotlarini tekshirib Python ma'lumotlariga o'tkazadi.

---

## Uyga vazifa

1. Mavzuni konspekt asosida takrorlash: SSR va USR ning kamida 3 tadan kuchli va zaif tomonlarini jadval qilib yozish.
2. Internetda o'zingiz foydalanadigan 5 ta mashhur veb-saytni (masalan: YouTube, Wikipedia, OLX, Telegram Web, Daryo.uz) ko'rib chiqing va ularning qaysi rendering modelidan foydalanishini tahlil qiling.
3. Kompyuteringizda Python 3.10+ o'rnatilganligini tekshirib, yangi `axv_backend` papkasi tayyorlab qo'ying.
