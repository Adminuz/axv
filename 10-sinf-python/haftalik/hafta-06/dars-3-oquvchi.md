# 18-dars. Docker orqali deploy qilish

> Loyiha tayyor, endi uni boshqa kompyuter va serverga qanday olib chiqamiz? Bugun Docker bilan «bir marta yasa, hamma joyda ishlat» tamoyilini o'rganamiz.

## Dars xulosasi

- Docker «mening kompyuterimda ishlagan» muammosini hal qiladi.
- Image — shablon, konteyner — uning ishlayotgan nusxasi.
- `Dockerfile` image retsepti; `.dockerignore` maxfiy narsalarni chiqarib tashlaydi.
- `docker run -p` port ulaydi, `--env-file` sozlama beradi.
- Compose da API va PostgreSQL bitta fayldan ko'tariladi; host `db`.
- Ma'lumot volume da saqlanadi; parol `.env` da.

## Qo'shimcha ma'lumot

### Layer cache
`requirements.txt` ni kodan oldin nusxalash tezlatadi.

### healthcheck
Baza tayyorligini tekshiradi.

### PaaS
Render, Railway: Dockerfile ni o'zi yig'adi.

### VPS
Docker o'rnatilgan oddiy Linux server.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Docker | Konteynerlash platformasi |
| Image | Konteyner shabloni |
| Konteyner | Ishlayotgan nusxa |
| Dockerfile | Image retsepti |
| compose | Ko'p xizmatli boshqaruv |
| Volume | Doimiy ma'lumot joyi |
| Port | Tarmoq kirish nuqtasi |
| Deploy | Ilovani serverga joylash |

## Bilasizmi?

- Docker image qatlamlardan iborat; o'zgarmagan qatlamlar keshdan olinadi.
- Qo'llanmaga ko'ra Docker ilovani istalgan serverda 100% bir xil muhitda ishga tushiradi.
- Render va Railway kabi PaaS xizmatlari Dockerfile asosida ilovani o'zi yig'ib, ishga tushiradi.

## Topshiriqlar

### 1. Image · oson

Image nima? Konteynerdan farqini yozing.

**Kutiladigan natija:** Shablon va ishlayotgan nusxa.

### 2. Dockerfile · oson

Dockerfile nima uchun kerak?

**Kutiladigan natija:** Image retsepti.

### 3. Port · oson

`-p 8000:8000` ni tushuntiring.

**Kutiladigan natija:** Tashqi:ichki port.

### 4. Buyruqlar · oson

Image yasash va konteyner ishga tushirish buyruqlarini yozing.

**Kutiladigan natija:** `docker build`, `docker run`.

### 5. Dockerfile yozish · o'rta

FastAPI uchun 7 qatorli Dockerfile yozing.

**Kutiladigan natija:** FROM, WORKDIR, COPY, RUN, COPY, CMD.

### 6. `.dockerignore` · o'rta

Nima uchun `.env` ni ignore qilamiz?

**Kutiladigan natija:** Maxfiy qiymatlar image da qolmasligi uchun.

### 7. Kesh · o'rta

`requirements.txt` ni nima uchun oldinroq nusxalaymiz?

**Kutiladigan natija:** Qatlam keshi.

### 8. Loglar · o'rta

Konteyner xatosini qanday ko'rasiz?

**Kutiladigan natija:** `docker logs`.

### 9. Compose · qiyin

API + PostgreSQL uchun compose yozing.

**Kutiladigan natija:** 2 xizmat, env, volume.

### 10. DB hosti · qiyin

Compose da baza hosti nega `db`?

**Kutiladigan natija:** Xizmat nomi orqali murojaat.

### 11. Volume · qiyin

Volume nima va `down -v` nimaga olib keladi?

**Kutiladigan natija:** Ma'lumotni saqlaydi; `-v` bazani o'chiradi.

### 12. Deploy · bonus

Loyihani VPS yoki Render ga joylash rejasini yozing.

**Kutiladigan natija:** Qadamlar ro'yxati.

## O'zingizni tekshiring

1. Image va konteyner farqi?
2. Dockerfile nima?
3. `-p` nima?
4. Compose da baza hosti?
5. Volume nima uchun?
6. `.env` image ga tushadimi?

## Uyga vazifa

Loyihani Docker ga joylang (40 daqiqa). To'liq shart: `uyga-vazifa.md`.
