# 18-dars. Nginx reverse-proxy: ilova oldidagi eshik

**Hafta:** 6 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + terminal amaliyoti · **II-bob**, 18-dars (umumiy 1–51)

**Manba:** O'quv qo'llanma, II bob, «Nginx reverse-proxy» bo'limi (reverse-proxy nima va nega kerak, o'rnatish, `sites-available`/`sites-enabled`, minimal konfiguratsiya, `X-Forwarded-*`, upstream va yuk muvozanati); o'quv dasturi. Konfiguratsiyalar qo'llanmadan olingan; `nginx -t` bu yerda ishga tushirilmagan (Nginx sandboxda yo'q), mentor muhitida sinab ko'ring.

## 1. Dars rejasi

**Maqsad:** Reverse-proxy ning vazifasini (ajratish, ishlash, masshtablash, xavfsizlik), Nginx ni o'rnatish va boshqarishni, `server`/`location` bloklari va `proxy_pass` bilan minimal konfiguratsiyani, `X-Forwarded-*` sarlavhalarini, `sites-available` va `sites-enabled` tartibini, `nginx -t` bilan tekshirishni va `upstream` bilan yukni muvozanatlashni o'rgatish.

**Kutiladigan natija:**
- Reverse-proxy nima va nega ilova portlari tashqariga ochilmasligini tushuntiradi.
- Nginx ni o'rnatadi (`apt`, `systemctl enable --now`) va `ss -lntp` bilan port 80 ni tekshiradi.
- `server`, `listen`, `server_name`, `location /`, `proxy_pass` bilan minimal konfiguratsiya yozadi.
- `Host`, `X-Real-IP`, `X-Forwarded-For`, `X-Forwarded-Proto` sarlavhalarini nima uchun berishni tushuntiradi.
- Konfiguratsiyani `nginx -t` bilan tekshirib, `reload` qiladi; `upstream` bilan 2 ta ilovaga yukni taqsimlaydi.

**Kerakli jihozlar:**
- Ubuntu/Debian virtual mashina yoki server
- `sudo`; tinglovchi ilova (masalan `python3 -m http.server 3000`)
- `library-api` loyihasi (REST API, 11-dars)

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va kirish | 17-dars: SSH kalit, `~/.ssh/config` |
| 10–35 daq | Yangi mavzu | Reverse-proxy g'oyasi va arxitektura; o'rnatish; Minimal konfiguratsiya: `server`, `location`, `proxy_pass`, sarlavhalar |
| 35–40 daq | Tanaffus | Harakatli tanaffus |
| 40–65 daq | Amaliyot | Mashq: oddiy ilovani Nginx orqali ochish; `nginx -t`, `reload` |
| 65–75 daq | Tezkor nazorat | 5 ta savol; Upstream (yuk muvozanati) va xatolar |
| 75–80 daq | Xulosa va uyga vazifa | Keyingi darsga ko'prik |

---

## 2. Dars konspekti

### 2.1. Reverse-proxy nima va nega kerak

**Nginx** — yuqori unumli veb-server va **reverse-proxy**. Reverse-proxy foydalanuvchi so'rovini qabul qilib, ichki tarmoqdagi ilovaga (Node.js, Python/Flask, FastAPI...) uzatadi. Nega kerak (qo'llanma): 1) **Ajratish** — TLS, kesh, sarlavhalar Nginx da, biznes mantiq ilovada; 2) **Ishlash** — statik fayllar (rasm, CSS, JS) Nginx dan tez beriladi; 3) **Masshtablash** — bir nechta ilovaga yukni tarqatish (round-robin, `ip_hash`, `least_conn`); 4) **Xavfsizlik** — ilova portlari tashqariga ochilmaydi; 5) **Soddalik** — bitta domen va sertifikat, ko'p orqa xizmat.

```bash
sudo apt update && sudo apt install -y nginx
sudo systemctl enable --now nginx
sudo systemctl status nginx
ss -lntp | grep ':80 '
```

`enable --now` Nginx ni hozir ishga tushiradi va server qayta yonganda ham avtomatik yoqadi.

### 2.2. server, location va proxy_pass

Asosiy fayl `/etc/nginx/nginx.conf`. Virtual xostlar `/etc/nginx/sites-available/*` da yoziladi va `sites-enabled/*` ga **symlink** bilan ulanadi (`ln -s`). Minimal reverse-proxy: `server` blokida `listen 80;`, `server_name example.com;`, `location /` ichida **`proxy_pass http://127.0.0.1:3000;`**. Sarlavhalar: `Host $host` (asl domen), `X-Real-IP $remote_addr` (mijoz IP), `X-Forwarded-For $proxy_add_x_forwarded_for` (proksi zanjiri), `X-Forwarded-Proto $scheme` (http yoki https). Ilova haqiqiy mijoz IP sini aynan shu sarlavhalardan oladi; auth, rate-limit va audit ham ularga tayanadi.

```nginx
server {
    listen 80;
    server_name example.com;

    location / {
        proxy_pass         http://127.0.0.1:3000;
        proxy_http_version 1.1;
        proxy_set_header   Host              $host;
        proxy_set_header   X-Real-IP         $remote_addr;
        proxy_set_header   X-Forwarded-For   $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Proto $scheme;
    }
}
```

Qo'llanmadagi to'liq namunada `proxy_read_timeout 60s;` va `Connection ""` ham bor. `example.com` o'rniga o'z domeningizni yozing.

### 2.3. Konfiguratsiyani yoqish va yuk muvozanati

Yoqish tartibi: konfiguratsiyani `sites-available/app.conf` ga yozing, `sudo ln -s /etc/nginx/sites-available/app.conf /etc/nginx/sites-enabled/app.conf` bilan ulang, **`sudo nginx -t`** bilan sintaksisni tekshiring va faqat `ok` bo'lsa **`sudo systemctl reload nginx`** qiling. Xato bo'lsa, `reload` qilmang: `nginx -t` aniq qator va faylni ko'rsatadi. **Upstream** — ilovaning bir necha nusxasi: `upstream app_upstream { server 127.0.0.1:3001; server 127.0.0.1:3002; }` va `proxy_pass http://app_upstream;`. Standart algoritm — round-robin; `least_conn` va `ip_hash` ham bor. Tekshirish: `curl -I http://example.com`.

```bash
sudo ln -s /etc/nginx/sites-available/app.conf /etc/nginx/sites-enabled/app.conf
sudo nginx -t && sudo systemctl reload nginx
curl -I http://example.com

# upstream bloki:
# upstream app_upstream {
#     server 127.0.0.1:3001;
#     server 127.0.0.1:3002;
# }
```

`nginx -t && systemctl reload nginx` — xavfsiz juftlik: xato bo'lsa reload bajarilmaydi. HTTPS (Certbot) va yo'naltirish 19-darsda.

### Qo'shimcha kod: To'liq minimal konfiguratsiya (qo'llanmadan)

```nginx
server {
    listen 80;
    server_name example.com www.example.com;
    location / {
        proxy_pass         http://127.0.0.1:3000;
        proxy_http_version 1.1;
        proxy_set_header   Host               $host;
        proxy_set_header   X-Real-IP          $remote_addr;
        proxy_set_header   X-Forwarded-For    $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Proto  $scheme;
        proxy_set_header   Connection         "";
        proxy_read_timeout 60s;
    }
}
```

---

## 3. Amaliy mashg'ulot (mini-loyiha: «Kutubxona boshqaruvi» serveri)

Virtual mashinada `library-api` (yoki `python3 -m http.server 3000`) ni `127.0.0.1:3000` da ishga tushiring. Nginx o'rnating, `sites-available/library.conf` yarating, `sites-enabled` ga ulang, `nginx -t` va `reload` qiling. `curl -I http://localhost` bilan tekshiring va `ss -lntp` da 80 hamda 3000 portlarini ko'ring. Ataylab xato yozib (`proxy_pas`), `nginx -t` xabarini o'qing.

### 1-mashq (oson). Nginx o'rnating
**Vazifa:** Nginx ni o'rnating, xizmatni yoqing va holatini tekshiring.

**Yechim:**
```nginx
sudo apt update && sudo apt install -y nginx
sudo systemctl enable --now nginx
sudo systemctl status nginx
```

### 2-mashq (oson). Port tekshiring
**Vazifa:** Nginx 80-portni tinglayotganini qanday tekshirasiz?

**Yechim:**
```nginx
ss -lntp | grep ':80 '
```

### 3-mashq (o'rta). Proxy yozing
**Vazifa:** `example.com` so'rovlarini `127.0.0.1:3000` ga uzating.

**Yechim:**
```nginx
server {
    listen 80;
    server_name example.com;
    location / {
        proxy_pass http://127.0.0.1:3000;
    }
}
```

### 4-mashq (o'rta). Sarlavhalar
**Vazifa:** Ilova mijoz IP va sxemani (http/https) bilishi uchun sarlavhalar qo'shing.

**Yechim:**
```nginx
proxy_set_header X-Real-IP         $remote_addr;
proxy_set_header X-Forwarded-For   $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
```

### 5-mashq (qiyin). Yoqish
**Vazifa:** Konfiguratsiyani ulang, tekshiring va xavfsiz qo'llang.

**Yechim:**
```nginx
sudo ln -s /etc/nginx/sites-available/app.conf /etc/nginx/sites-enabled/app.conf
sudo nginx -t && sudo systemctl reload nginx
```

### 6-mashq (bonus). Upstream
**Vazifa:** Ikki ilovaga (3001, 3002) yukni taqsimlang.

**Yechim:**
```nginx
upstream app_upstream {
    server 127.0.0.1:3001;
    server 127.0.0.1:3002;
}
# location / ichida: proxy_pass http://app_upstream;
```

---

## 4. Tezkor savollar

1. Reverse-proxy nima?
   - **Javob:** Mijoz so'rovini ichki ilovaga uzatuvchi vositachi.
2. `proxy_pass` nima qiladi?
   - **Javob:** So'rovni orqa manzilga uzatadi.
3. Nega `X-Forwarded-For` kerak?
   - **Javob:** Ilova asl mijoz IP sini bilishi uchun.
4. `nginx -t` nima uchun?
   - **Javob:** Sintaksisni reload dan oldin tekshiradi.
5. Upstream nima?
   - **Javob:** Orqa ilovalar guruhi, yuk muvozanati uchun.

## 5. Mentor uchun eslatmalar

- Nginx ni virtual mashinada o'rnating; `nginx -t` natijasini o'quvchi bilan birga o'qing.
- Konfiguratsiyalar qo'llanmadan olingan; sandboxda Nginx yo'q, shuning uchun `nginx -t` darsdan oldin mentor tomonidan sinab ko'rilishi kerak.
- `set_real_ip_from` va `real_ip_header` qo'llanmadagi to'liq namunada bor, lekin ishlab chiqarishda ishonchli proksi manzillari bilan cheklanishi kerak, bu dars minimal variantni oladi.
- HTTPS (Certbot), HTTP→HTTPS yo'naltirish, kesh, WebSocket va port forwarding 19-darsga qoldirildi.
- Mini-loyiha: `library-api` ni Nginx orqasiga qo'yish keyingi darsda HTTPS bilan davom etadi.
