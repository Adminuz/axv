# 18-dars. Nginx reverse-proxy: ilova oldidagi eshik

> Ilova tayyor, endi uni dunyoga qanday xavfsiz chiqaramiz? Bugun Nginx reverse-proxy: ilova oldidagi eshikni o'rnatamiz.

## Dars xulosasi

- Reverse-proxy mijoz so'rovini ichki ilovaga uzatadi.
- Nginx 80/443 da, ilova `127.0.0.1` da: tashqariga ochilmaydi.
- Konfig: `server`, `listen`, `server_name`, `location`, `proxy_pass`.
- `Host`, `X-Real-IP`, `X-Forwarded-For/Proto` sarlavhalari ilovaga kontekst beradi.
- `sites-available` → `sites-enabled` (symlink) → `nginx -t` → `reload`.
- `upstream` bilan bir nechta ilovaga yuk taqsimlanadi.

## Qo'shimcha ma'lumot

### sites-enabled
Faol saytlarga symlinklar.

### round-robin
Standart yuk taqsimlash: navbat bilan.

### TLS terminatsiya
HTTPS ni Nginx hal qiladi, ilovaga oddiy HTTP boradi.

### Kesh
Statik fayllarga `expires` va `Cache-Control`.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Nginx | Veb-server va reverse-proxy |
| Reverse-proxy | Teskari vositachi |
| server | Virtual xost bloki |
| location | Yo'l bo'yicha qoida |
| proxy_pass | Orqa manzilga uzatish |
| upstream | Orqa serverlar guruhi |
| symlink | Fayl havolasi |
| reload | Sozlamani yangilash |

## Bilasizmi?

- Nginx event-driven arxitekturada ishlaydi: kam xotira bilan ko'p ulanishga xizmat qiladi.
- Ko'p tashkilotlarda ilova portlari faqat `127.0.0.1` da tinglaydi, tashqariga faqat Nginx chiqadi.
- `least_conn` yukni eng kam band serverga yo'naltiradi.

## Topshiriqlar

### 1. Reverse-proxy · oson

Reverse-proxy nima? 1 jumla.

**Kutiladigan natija:** Ichki ilovaga uzatuvchi vositachi.

### 2. Portlar · oson

80 va 443 qaysi protokollar?

**Kutiladigan natija:** HTTP va HTTPS.

### 3. O'rnatish · oson

Nginx ni o'rnating va yoqing.

**Kutiladigan natija:** `apt install`, `enable --now`.

### 4. Fayllar · oson

Konfig fayllari qayerda?

**Kutiladigan natija:** `/etc/nginx/...`.

### 5. server bloki · o'rta

`app.local` uchun 80-portda server bloki yozing.

**Kutiladigan natija:** `listen`, `server_name`.

### 6. proxy_pass · o'rta

3000-portdagi ilovaga uzating.

**Kutiladigan natija:** `proxy_pass http://127.0.0.1:3000;`.

### 7. Sarlavhalar · o'rta

Nega `X-Forwarded-Proto` kerak?

**Kutiladigan natija:** Ilova http yoki https ekanini biladi.

### 8. Symlink · o'rta

Konfigni yoqing.

**Kutiladigan natija:** `ln -s ... sites-enabled/`.

### 9. Tekshirish · qiyin

Konfigni qo'llash buyruqlari ketma-ketligi?

**Kutiladigan natija:** `nginx -t && reload`.

### 10. Xato topish · qiyin

`nginx -t` xatosini o'qing va tuzating.

**Kutiladigan natija:** Aniq qator topildi.

### 11. Upstream · qiyin

2 ta ilova uchun upstream yozing.

**Kutiladigan natija:** `upstream`, 2 ta `server`.

### 12. Mini-loyiha · bonus

`library-api` ni Nginx orqasiga qo'ying va hisobot yozing.

**Kutiladigan natija:** Ishlaydigan konfig va `curl -I`.

## O'zingizni tekshiring

1. Reverse-proxy nima?
2. `proxy_pass` nima?
3. Nega `X-Forwarded-For`?
4. `nginx -t` nima?
5. Upstream nima?
6. Konfigni qanday yoqasiz?

## Uyga vazifa

Nginx reverse-proxy konfiguratsiyasini yozing (30 daqiqa). To'liq shart: `uyga-vazifa.md`.
