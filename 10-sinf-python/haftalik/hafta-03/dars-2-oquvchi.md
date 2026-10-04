# 8-dars. Statik fayllar bilan ishlash. Fayllarni yuklash va koʻchirib olish

> Har qanday zamonaviy yangiliklar portali jozibali muqova rasmlari, foydalanuvchilarning fotosuratlari va yuklab olinuvchi hujjatlarsiz to'liq bo'lmaydi. Ushbu darsda biz Django loyihasida statik va media fayllarni to'g'ri tashkil etishni, multipart fayllarni qabul qilish va xavfsiz yuklab olish endpointlarini quramiz.

## Dars xulosasi

- **Statik fayllar (Static)** &mdash; dasturchi tomonidan yaratilgan va sayt dizayni hamda mantiqini ta'minlovchi doimiy fayllardir (CSS uslublar, JavaScript skriptlar, logotiplar).
- **Media fayllar (Media)** &mdash; foydalanuvchilar tomonidan sayt ishlashi jarayonida yuklangan dinamik fayllardir (muqova rasmlari, foydalanuvchi avatari, PDF hujjatlar).
- Ma'lumotlar bazasida faylning o'zi saqlanmaydi, balki uning server diskidagi saqlash yo'li (URL manzili) saqlanadi.
- Katta hajmdagi fayllar Git tizimini behuda og'irlashtirmasligi uchun `media/` va `staticfiles/` papkalari majburiy ravishda `.gitignore` ga qo'shiladi.
- Fayllarni uzatish uchun standart JSON to'g'ri kelmaydi; mijoz **`multipart/form-data`** formatidan foydalanadi va DRF da **`MultiPartParser`** uni qabul qiladi.
- Rasm yuklashda xavfsizlik uchun albatta MIME formati (`image/jpeg`, `image/png`, `image/webp`) va maksimal hajm (masalan, 5 MB) serializer orqali tekshirilishi shart.
- Fayllarni xavfsiz yuklab olish uchun Django ning **`FileResponse`** klassi ishlatiladi va `as_attachment=True` orqali brauzerda yuklab olish oynasi ochiladi.

## Qo'shimcha ma'lumot

### 1. Nega rasmlar ma'lumotlar bazasida (BLOB) saqlanmaydi?

Ba'zi yangi dasturchilar: "Nega rasmni ham xuddi matn kabi to'g'ridan-to'g'ri ma'lumotlar bazasiga (BLOB &mdash; Binary Large Object) solib qo'ymaymiz?" deb o'ylashadi.
Sabablari:
1. **Baza hajmining haddan tashqari shishib ketishi:** 100 000 ta 3 Megabaytli rasm bazani 300 Gigabaytga aylantiradi. Bunday bazadan zaxira nusxa (backup) olish soatlab vaqt oladi.
2. **Sekinlik:** Baza matnli indekslarni qidirish uchun optimallashgan, katta hajmdagi ikkilik fayllarni o'qish esa xotirani band qiladi.
3. **To'g'ri yechim:** Fayl fayl tizimiga (diskka yoki AWS S3 / MinIO bulutli xotirasiga) saqlanadi, bazada esa bor-yo'g'i 50 baytlik matn saqlanadi: `covers/2026/10/ai_news.jpg`.

### 2. Nginx va Production da fayllarni boshqarish

Ishlab chiqish (Development) paytida `DEBUG=True` bo'lgani sababli, rasmlarni Django ning o'zi brauzerga ko'rsatib turadi (`urls.py` dagi `static(MEDIA_URL)` sabab).
Ammo real serverda (Production) Django faqat API mantiqini hisoblashi kerak, rasmlarni tarqatish bilan esa tezyurar veb-server &mdash; **Nginx** shug'ullanadi:
- Foydalanuvchi rasm so'raganda, so'rov Python ga yetib bormasdan, to'g'ridan-to'g'ri Nginx tomonidan diskdan olinib, 5 millisoniyada yuboriladi!
- Statik fayllarni bitta papkaga to'plash uchun esa `python manage.py collectstatic` buyrug'i ishga tushiriladi.

### 3. Rasm formatlari: Nima uchun WebP tavsiya etiladi?

Zamonaviy veb-ishlab chiqishda an'anaviy JPEG va PNG formatlari o'rniga Google tomonidan yaratilgan **WebP** formati keng qo'llanilmoqda:
- JPEG bilan bir xil sifatni ta'minlagan holda fayl hajmini 30-40% ga kichraytiradi;
- PNG kabi shaffoflikni (transparency) qo'llab-quvvatlaydi;
- Kichik hajm saytning 2 barobar tezroq yuklanishini ta'minlaydi.

### 4. Dasturchilar ko'p yo'l qo'yadigan xatolar

- **Xato 1: MultiPartParser ni unutish.** Dasturchi rasm yuklash endpointini yozadi, lekin ViewSet ga `parser_classes=[MultiPartParser, FormParser]` qo'shishni unutadi. Natijada `request.data` bo'sh keladi va rasm saqlanmaydi.
- **Xato 2: Fayl kengaytmasiga ishonish.** Foydalanuvchi `virus.exe` faylining nomini `virus.jpg` deb o'zgartirib yuklashi mumkin. Shuning uchun tekshiruv fayl nomidagi kengaytmaga qarab emas, uning haqiqiy MIME turiga (`file.content_type`) va `Pillow` kutubxonasiga tayanib bajarilishi shart.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Static files** | Dasturning vizual ko'rinishi va ishlashi uchun zarur bo'lgan doimiy dasturchi fayllari (CSS/JS/rasmlar). |
| **Media files** | Sayt foydalanuvchilari tomonidan tizimga yuklangan barcha dinamik fayllar (avarlar, muqovalar). |
| **collectstatic** | Barcha ilovalardagi statik fayllarni ishlab chiqarish uchun bitta umumiy papkaga yig'uvchi Django buyrug'i. |
| **multipart/form-data** | Ikkilik (binary) fayllarni va shakl ma'lumotlarini HTTP orqali birgalikda yuborish uchun maxsus MIME turi. |
| **MultiPartParser** | DRF da `multipart/form-data` orqali yuborilgan fayllarni o'qib, `request.FILES` ga yuklovchi parser. |
| **FileResponse** | Django da fayllarni oqimli (streaming) tarzda mijozga uzatish uchun mo'ljallangan maxsus HTTP javob klassi. |
| **as_attachment** | Brauzerga faylni ekranda ochmasdan, kompyuterga yuklab olishni majburlash parametri. |
| **Pillow** | Python tilida tasvirlar (rasmlar) bilan ishlash, o'lchamini o'zgartirish va tahlil qilish uchun asosiy kutubxona. |
| **MIME type** | Faylning asl tabiatini va formatini ifodalovchi xalqaro standart identifikator (masalan: `image/jpeg`). |
| **STATIC_ROOT** | `collectstatic` buyrug'i barcha statik fayllarni joylashtiradigan mutlaq katalog yo'li. |

## Bilasizmi?

- YouTube har daqiqada 500 soatdan ortiq videofayllarni qabul qiladi. Agar ular ushbu videolarni bitta server diskida saqlaganida, server disklari 1 kunda to'lib qolardi. Shuning uchun barcha yirik media fayllar taqsimlangan bulutli ob'yektli xotiralarda (Object Storage) saqlanadi.
- Django-ning `FileResponse` klassi hatto 10 Gigabaytlik ulkan faylni ham server operativ xotirasini (RAM) to'ldirmasdan, 8 Kilobaytlik kichik oqimlar (chunks) shaklida mijozga ravon yetkazib bera oladi.
- Python-da tasvirlar bilan ishlash uchun `Pillow` kutubxonasi o'rnatilishi shart (`pip install pillow`), aks holda Django `ImageField` maydonidan foydalanishga ruxsat bermaydi.

## Topshiriqlar

### 1. Fayl turlarini ajratish · oson
Quyidagi fayllarni `Static` yoki `Media` toifalariga ajrating:
a) Sayt logotipi `logo.png`
b) Foydalanuvchi profiliga yuklagan pasport fotosurati
c) Bootstrap uslublar fayli `bootstrap.min.css`
d) Yangiliklar maqolasining muqova rasmi
**Kutiladigan natija:** 4 ta fayl uchun to'g'ri toifa (Static yoki Media).

### 2. .gitignore qoidasi · oson
Nima uchun `media/` va `staticfiles/` papkalari loyiha Git omboriga (GitHub-ga) yuklanmasligi kerak? Buning 2 ta sababini yozing.
**Kutiladigan natija:** Git omborini toza va yengil saqlash bo'yicha 2 ta asosli sabab.

### 3. collectstatic buyrug'i · oson
`python manage.py collectstatic` buyrug'i nima vazifani bajaradi va u qaysi papkaga fayllarni yig'adi?
**Kutiladigan natija:** Buyruq vazifasi va `STATIC_ROOT` ga ishora.

### 4. FileResponse parametri · oson
Fayl havolasi ochilganda brauzerda rasm shunchaki ko'rinmasdan, foydalanuvchi kompyuteriga yuklab olinishi uchun `FileResponse` ga qaysi parametr berilishi kerak?
**Kutiladigan natija:** Aniq parametr nomi va uning qiymati (`as_attachment=True`).

### 5. Fayl hajmini tekshirish validatsiyasi · o'rta
Foydalanuvchi avatari (`avatar`) hajmi 2 MB dan oshmasligini tekshiruvchi `validate_avatar(self, file)` metodini yozing. Hajm me'yordan oshganda qanday xatolik xabari chiqishi kerak?
**Kutiladigan natija:** To'liq Python validatsiya metodi.

### 6. Multipart so'rov sarlavhasi · o'rta
Postman dasturida rasm yuklash so'rovini yuborayotganda `Body` bo'limida qaysi parametr tanlanadi va so'rov sarlavhalarida (Headers) `Content-Type` qanday ko'rinishda bo'ladi?
**Kutiladigan natija:** Postman parametri va `multipart/form-data` sarlavhasi.

### 7. Foydalanuvchi avatari yuklash endpointi · o'rta
Foydalanuvchi o'z avatarini yuklashi uchun `apps/accounts/views.py` modulida `AvatarUploadView(APIView)` klassini yozing (undagi `parser_classes` MultiPart va FormParser bo'lsin).
**Kutiladigan natija:** To'liq ishlovchi APIView kodi.

### 8. Kod tahlili: Xatoni topish · o'rta
Boshlovchi dasturchi modelda quyidagi maydonni yaratdi:
```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to="covers/")
```
Lekin `makemigrations` qilganda terminalda quyidagi xato chiqdi:
`Cannot use ImageField because Pillow is not installed.`
Ushbu xatoni qanday hal qilish kerak?
**Kutiladigan natija:** Sababi va terminalda berilishi kerak bo'lgan `pip install pillow` buyrug'i.

### 9. Mini-loyiha: PDF fayllarni xavfsiz yuklab olish · qiyin
Elektron jurnal API loyihasida `Article` modeli mavjud bo'lib, uning `pdf_file = models.FileField(upload_to="articles/pdf/")` maydoni bor.
Faqat tizimga kirgan foydalanuvchilar ushbu PDF faylni yuklab olishi mumkin bo'lgan `@action(detail=True, methods=["get"])` metodini yozing (agar fayl bo'lmasa 404 chiqsin).
**Kutiladigan natija:** Ruxsatlar bilan himoyalangan to'liq yuklab olish action kodi.

### 10. Tasvirlarni avtomatik kichraytirish (Resize) · qiyin
Foydalanuvchilar ba'zan juda katta (masalan, 15 Megapikselli) rasmlarni yuklashadi.
`Pillow` kutubxonasi yordamida rasm modelga saqlanayotganda uning o'lchamini maksimal `1200x800` pikselliga avtomatik kichraytirib (resize qilib) saqlash mantiqini qanday yozish mumkin?
**Kutiladigan natija:** Modelning `save()` metodida `Pillow.Image` yordamida o'lchamni kichraytirish namunasi.

### 11. Bulutli saqlash: AWS S3 va MinIO integratsiyasi · qiyin
Production serverda media fayllarni mahalliy diskda saqlash o'rniga S3 ob'yektli xotiraga yuklash talab etiladi.
1. `django-storages` va `boto3` kutubxonalari nima uchun kerak?
2. `DEFAULT_FILE_STORAGE` sozlamasi orqali Django qanday qilib fayllarni avtomatik tarzda AWS S3 yoki MinIO ga yo'naltiradi?
**Kutiladigan natija:** Bulutli xotira integratsiyasi arxitekturasi va sozlamalar tahlili.

### 12. Bonus tadqiqot: Video oqimlari va HTTP Range Headers · bonus
Agar foydalanuvchi 2 Gigabaytlik videoni yuklab olmasdan, veb-saytda onlayn ko'rmoqchi (stream qilmoqchi) bo'lsa:
1. Nima uchun butun faylni bitta `FileResponse` bilan berish brauzerni sekinlashtiradi?
2. HTTP `Range: bytes=0-1048575` sarlavhasi video pleyerlarga videoni qismlarga bo'lib yuklashga qanday imkon beradi?
**Kutiladigan natija:** Video oqimli uzatish (streaming) bo'yicha mustaqil tadqiqot.

## O'zingizni tekshiring

1. Statik fayllar bilan Media fayllar orasidagi asosiy farqni bitta jumlada ayting.
2. `Pillow` kutubxonasi Django da nima maqsadda talab etiladi?
3. Fayl yuklashda qaysi HTTP kontent turi ishlatiladi va DRF da uni qaysi parser o'qiydi?
4. Nima uchun fayllar ma'lumotlar bazasida emas, alohida fayl tizimida saqlanadi?
5. `FileResponse` ning oddiy HTTP javoblardan ustunligi nimada?
6. Nega `.gitignore` ga `media/` papkasi kiritilishi shart?

## Uyga vazifa

1. Kompyuteringizda `pip install pillow` buyrug'ini bering va `Post` modelida `cover_image` maydoni borligiga ishonch hosil qiling.
2. `src/apps/news/serializers.py` faylida `PostCoverUploadSerializer` klassini yozing.
3. `PostViewSet` da `upload_cover` va `download_cover` actionlarini yozib, Postman orqali kompyuterdan rasm yuklash va uni yuklab olishni sinovdan o'tkazing.
