# 3-dars. GitHub: masofaviy repo, push/pull/clone, README, .gitignore, Issues va birinchi loyiha

**Hafta:** 1 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliyot · **I-bob**, 3-dars (hafta 1 ning yakuniy darsi)

> Dasturda «Axborot texnologiyalari ekotizimi, SDLC va versiyalarni boshqarish (Git/GitHub)» mavzusiga 3 dars ajratilgan (1–3). Bo'linish: 1-dars — IT ekotizimi va SDLC; 2-dars — Git asoslari lokal (init, add, commit, status, log, `.git`, working directory → staging → repository); **3-dars — GitHub: akkaunt, repo, remote, push/pull/clone, README.md, .gitignore, Issues, birinchi loyihani e'lon qilish.** Branching strategiyalari, Pull Request va code review keyingi haftada (4–6-darslar). Dasturdagi «Issues/Projects» dan bu darsda faqat Issues olinadi, Projects (board) 2-haftada.

> Eslatma: 2-dars materiali menga ko'rinmaydi. Bu dars o'quvchi lokal repoda `git init`, `git add`, `git commit`, `git status`, `git log` ni bilishiga tayanadi. Agar 2-darsda bular o'tilmagan bo'lsa, 1-bo'limdagi takrorlash 5 daqiqaga cho'zilsin.

## 1. Dars rejasi

**Maqsad:** o'quvchi lokal reponi GitHub'dagi masofaviy repoga ulaydi, xavfsiz autentifikatsiya sozlaydi, README.md va `.gitignore` bilan to'ldirilgan birinchi mini loyihasini e'lon qiladi va Issue orqali vazifa yuritadi.

**Kutiladigan natija:**
- Git va GitHub farqini, «local» va «remote» (`origin`) tushunchalarini tushuntiradi.
- GitHub akkaunti (2FA bilan) va bo'sh repo yaratadi.
- Autentifikatsiya usullarini (HTTPS + token, SSH kalit, `gh auth login`) farqlaydi; kamida bittasini sozlaydi.
- `git remote add`, `git push -u`, `git pull`, `git clone`, `git fetch` buyruqlarini ma'noli ishlatadi.
- `README.md` yozadi (loyiha nomi, nima qiladi, qanday ishga tushadi); `.gitignore` bilan sirlar va chiqindi fayllar tarixga kirmasligini ta'minlaydi.
- GitHub Issues'da vazifa ochadi va commit orqali yopadi (`Closes #1`).
- Maxfiy ma'lumot tarixga tushib qolsa nima qilishni biladi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–8 | Takrorlash | 1–2-dars: SDLC va Git zanjiri; lokal repo holati (`status`, `log`) |
| 8–30 | Yangi mavzu 1 | Git vs GitHub; akkaunt, 2FA; remote; autentifikatsiya; push/pull/clone/fetch |
| 30–35 | Tanaffus | |
| 35–50 | Yangi mavzu 2 | README.md, .gitignore, Issues, sirlar xavfsizligi |
| 50–75 | Amaliyot | `dev-log` mini loyihasini yaratish va GitHub'ga e'lon qilish |
| 75–80 | Tezkor nazorat va xulosa | Keyingi hafta ko'prigi |

## 2. Konspekt

### 2.1. Takrorlash (8 daqiqa)
Savollar: SDLC bosqichlari qaysi (talab, dizayn, kod, test, deploy, ekspluatatsiya)? Git qaysi bosqichda ishlatiladi? Working directory, staging va repository nima? `git commit` nimani saqlaydi (snapshot: muallif, vaqt, izoh, ota commit)? Tekshiruv: o'quvchi 2-darsdagi lokal repo ichida `git status` va `git log --oneline` ni ishlatadi. Ko'prik: «Hozir tarix faqat sizning noutbukingizda. Noutbuk buzilsa, hammasi yo'qoladi, jamoa esa uni ko'rmaydi. Bugun uni ulaymiz.»

### 2.2. Git va GitHub: farq
- **Git** — kompyuteringizdagi dastur (versiyalarni boshqarish tizimi, buyruq qatori). Internet shart emas.
- **GitHub** — Git repolarini saqlaydigan va ular atrofida hamkorlik (Issues, Pull Request, review, Actions) tashkil qiladigan veb-xizmat. Muqobillari: GitLab, Bitbucket. Qo'llanmada: «GitHub — masofaviy repo va hamkorlik: PR, review, Issues/Projects, Actions».
- O'xshatish: Git — Word'ning «versiyalar tarixi»; GitHub — Google Drive + izohlar + vazifalar doskasi.
- Sizning portfolio'ingiz ham shu yerda: ish beruvchi va mijozlar GitHub profilingizga qaraydi (IV bobda case study shu asosda quriladi).

### 2.3. Akkaunt va 2FA
GitHub akkaunt o'quvchining o'zi tomonidan o'z brauzerida yaratiladi (mentor yaratib bermaydi, parolni ko'rmaydi). Foydalanuvchi nomi professional bo'lsin: u profilingiz manzili (`github.com/<nom>`) va CV'dagi havola bo'ladi. Majburiy: **2FA** (ikki bosqichli tasdiqlash) yoqiladi, tiklash kodlari (recovery codes) xavfsiz joyda saqlanadi. Parol va kodlarni hech kimga, mentorga ham, chatga ham yubormang.

### 2.4. Masofaviy repo (remote)
Remote — boshqa joyda turgan repo nusxasiga nom berilgan havola. Odatiy nom: `origin`.

```bash
git remote add origin https://github.com/<nom>/dev-log.git   # havolani bog'lash
git remote -v                                               # ro'yxat
```

Yangi repo yaratganda GitHub bosh sahifada tayyor buyruqlarni ko'rsatadi. Repo yaratishda README/.gitignore/license'ni **belgilamang**, agar lokal repo allaqachon bor bo'lsa (aks holda ikkala tomonda tarix «ajralib» ketadi, `push` rad etiladi).

### 2.5. Autentifikatsiya: uch yo'l
| Yo'l | Qanday ishlaydi | Eslatma |
|---|---|---|
| HTTPS + PAT (Personal Access Token) | Parol o'rniga token; Git credential manager saqlaydi | GitHub oddiy parol bilan `push` ni qabul qilmaydi. Fine-grained token, faqat kerakli repo, qisqa muddat. |
| SSH kalit | Kompyuterda kalit juftligi; **ochiq** kalit GitHub'ga qo'yiladi | Eng qulay uzoq muddatli yo'l. |
| GitHub CLI: `gh auth login` | Brauzer orqali tasdiqlaydi, tokenni o'zi boshqaradi | Eng oson boshlash. |

**SSH kalit yaratish:**
```bash
ssh-keygen -t ed25519 -C "sizning@emailingiz"   # passphrase qo'yish tavsiya etiladi
cat ~/.ssh/id_ed25519.pub                        # FAQAT .pub (ochiq) kalit ko'rsatiladi
```
- `id_ed25519` — **maxfiy** kalit: hech qachon yubormang, repoga qo'shmang, skrinshot qilmang.
- `id_ed25519.pub` — ochiq kalit: GitHub → Settings → SSH and GPG keys → New SSH key ga qo'yiladi.
- Tekshirish: `ssh -T git@github.com` («Hi <nom>! You've successfully authenticated...»).
- SSH repo manzili: `git@github.com:<nom>/dev-log.git`.

**Token qoidalari (PAT ishlatilsa):** tokenni faqat ko'rsatilgan paytda bir marta nusxalang; kodga, README'ga, `.env` ni commit qilishga, chatga, skrinshotga yozmang; kam ruxsat (least privilege: qo'llanmadagi «minimal vakolat tamoyili»), muddat qo'ying; sizib chiqsa — darhol GitHub'da o'chiring (revoke).

> Mentor uchun: dars paytida o'quvchi parol yoki tokenni ekranda boshqalarga ko'rsatmasin; terminalda token so'ralsa uni o'zi kiritadi. Mentor token/parol so'ramaydi, ko'rmaydi.

### 2.6. push, pull, fetch, clone
```
Lokal repo  --push-->  GitHub (origin)
Lokal repo  <--pull--  GitHub (origin)
GitHub      --clone--> yangi lokal nusxa
```
- `git push -u origin main` — commitlarni yuboradi; `-u` (upstream) keyin shunchaki `git push` / `git pull` yetadi.
- `git fetch` — yangiliklarni **yuklab oladi**, lekin ishchi fayllarni o'zgartirmaydi (xavfsiz ko'rish).
- `git pull` — `fetch` + birlashtirish (merge): yuklaydi va qo'shadi.
- `git clone <manzil>` — reponing to'liq nusxasi (tarix bilan) + `origin` avtomatik sozlanadi.
- Boshlang'ich shox nomini `main` qilish: `git branch -M main` (eski nom `master` bo'lishi mumkin).
- Qo'llanmadagi ritm: fetch → pull → push. Push qilishdan oldin pull qilish odat bo'lsin.
- Push rad etilsa («rejected, non-fast-forward») — masofada sizda yo'q commit bor. Majburlama (`--force` ishlatmang), avval `git pull`.

### 2.7. README.md
Reponing «old eshigi». GitHub uni repo sahifasida avtomatik ko'rsatadi. Format — Markdown. Minimal tuzilma: nom, 1 jumlalik tavsif, nima qila oladi, o'rnatish/ishga tushirish, misol, muallif/litsenziya. (Portfolio uchun keyinchalik: skrinshot/GIF, badge — qo'llanma IV bobi.) Yaxshi README savoli: «notanish odam 2 daqiqada ishga tushira oladimi?»

### 2.8. .gitignore
Git'ga «bu fayllarni kuzatma» deydigan fayl. Nega: (1) sirlar (`.env`, kalitlar, tokenlar) tarixga kirmasligi uchun; (2) chiqindilar (`__pycache__/`, `node_modules/`, build, loglar); (3) OS/IDE fayllari (`.DS_Store`, `.vscode/`, `.idea/`); (4) katta binar fayllar (qo'llanma: binar fayllar repoga ortiqcha yuk, `.gitignore` build chiqindilaridan himoya qiladi).

```gitignore
# sirlar
.env
*.pem
id_ed25519
# Python
__pycache__/
*.pyc
.venv/
# mahalliy ma'lumot
tasks.json
# OS / IDE
.DS_Store
.vscode/
```
Muhim: `.gitignore` faqat **hali kuzatilmayotgan** fayllarga ta'sir qiladi. Fayl allaqachon commit qilingan bo'lsa: `git rm --cached <fayl>` va commit. Eng muhim: **tarixga tushgan sir — «yo'qolmaydi»**. Faylni o'chirib commit qilish yetmaydi, eski commit'da turaveradi. To'g'ri yo'l: (1) sirni darhol bekor qiling (token revoke, parolni almashtiring); (2) keyin tarixni tozalash (maxsus vositalar) haqida o'ylang. Birinchi qadam har doim — sirni almashtirish.

### 2.9. Issues
Issue — repodagi vazifa/xato/g'oya kartochkasi (raqami `#1`, `#2`...). Qismlari: sarlavha, tavsif, label (bug, enhancement, documentation), assignee, milestone. SDLC bilan bog'liq: talab/xato → Issue → kod → commit → yopiladi. Commit xabarida `Closes #1` / `Fixes #1` yozilsa, GitHub'ga yetib borgach (asosiy shoxda) issue avtomatik yopiladi. Kichik commit va aniq issue — keyingi haftadagi branching → PR oqimiga poydevor: issue → feature branch → PR → review → merge.

### 2.10. Keyingi haftaga ko'prik (3 daqiqa)
Bugun hamma ishni to'g'ridan-to'g'ri `main` ga qildik: yakka o'zimiz uchun mumkin, jamoada esa bunday qilinmaydi. Keyingi hafta: **branching strategiyalari** (feature, release, hotfix), **Pull Request** (What/Why/How) va **code review** — bugungi repo ustida davom etamiz.

## 3. Kod namunalari

**Namuna 1 — mini loyiha `todo.py`** (tekshirilgan, Python 3):
```python
"""dev-log: kichik vazifalar ro'yxati (CLI). Ishlatish: python3 todo.py add "matn" | list | done 1"""
import json
import sys
from pathlib import Path

FAYL = Path("tasks.json")  # mahalliy ma'lumot: .gitignore ga qo'shiladi


def yukla():
    return json.loads(FAYL.read_text(encoding="utf-8")) if FAYL.exists() else []


def saqla(vazifalar):
    FAYL.write_text(json.dumps(vazifalar, ensure_ascii=False, indent=2), encoding="utf-8")


def main(args):
    if not args:
        print("Buyruqlar: add <matn> | list | done <raqam>")
        return
    vazifalar = yukla()
    buyruq = args[0]
    if buyruq == "add" and len(args) > 1:
        vazifalar.append({"matn": " ".join(args[1:]), "bajarildi": False})
        saqla(vazifalar)
        print(f"Qo'shildi: {vazifalar[-1]['matn']}")
    elif buyruq == "list":
        for i, v in enumerate(vazifalar, 1):
            belgi = "x" if v["bajarildi"] else " "
            print(f"{i}. [{belgi}] {v['matn']}")
    elif buyruq == "done" and len(args) > 1 and args[1].isdigit():
        i = int(args[1]) - 1
        if 0 <= i < len(vazifalar):
            vazifalar[i]["bajarildi"] = True
            saqla(vazifalar)
            print("Bajarildi!")
        else:
            print("Bunday raqam yo'q")
    else:
        print("Noma'lum buyruq")


if __name__ == "__main__":
    main(sys.argv[1:])
```
(Mentor: dastur mazmuni darsning asosiy mavzusi emas, u Git ishlashi uchun «tirik» loyiha. O'quvchi o'z loyihasini tanlashi mumkin, masalan HTML vizitka.)

**Namuna 2 — to'liq ish oqimi (noldan GitHub'gacha):**
```bash
mkdir dev-log && cd dev-log
git init
git branch -M main
# todo.py, README.md, .gitignore yozilgan
git status
git add .gitignore README.md todo.py
git commit -m "feat: dastlabki vazifalar ro'yxati (CLI)"
# GitHub'da bo'sh repo yaratilgan (README/.gitignore tanlanMAGAN)
git remote add origin git@github.com:<nom>/dev-log.git
git push -u origin main
```

**Namuna 3 — clone va pull (ikkinchi nusxa bilan sinash):**
```bash
cd ..
git clone git@github.com:<nom>/dev-log.git dev-log-nusxa
cd dev-log-nusxa
git log --oneline
# GitHub veb-interfeysida README ni tahrirlab commit qiling, so'ng asl papkada:
cd ../dev-log
git pull
```

**Namuna 4 — issue yopuvchi commit:**
```bash
git commit -am "docs: README'ga ishga tushirish bo'limi qo'shildi. Closes #1"
git push
```

**Namuna 5 — tasodifan commit qilingan faylni kuzatuvdan chiqarish:**
```bash
echo "tasks.json" >> .gitignore
git rm --cached tasks.json     # faylni diskda qoldiradi, Git'dan olib tashlaydi
git commit -m "chore: tasks.json kuzatuvdan chiqarildi"
```

**Namuna 6 — README.md (minimal):**
```markdown
# dev-log
Terminalda ishlaydigan kichik vazifalar ro'yxati (Python).

## Imkoniyatlar
- vazifa qo'shish, ro'yxatni ko'rish, bajarilganini belgilash

## Ishga tushirish
    python3 todo.py add "README yozish"
    python3 todo.py list
    python3 todo.py done 1

## Muallif
<ismingiz> · 11-sinf, Professional IT development
```

## 4. Amaliy topshiriqlar

### Oson — Hisob va xavfsizlik
GitHub'da o'z akkauntingizni yarating (agar bo'lmasa), 2FA ni yoqing, profilga ism va qisqa bio yozing. SSH kalit yarating va ochiq kalitni GitHub'ga qo'shing (yoki `gh auth login`). `ssh -T git@github.com` natijasini tekshiring.
**Kutiladigan natija:** «Hi <nom>! You've successfully authenticated» xabari; maxfiy kalit hech qayerga yuborilmagan.
**Yechim:** `ssh-keygen -t ed25519 -C "email"` → `cat ~/.ssh/id_ed25519.pub` natijasini GitHub → Settings → SSH and GPG keys → New SSH key ga qo'yish → `ssh -T git@github.com`. Xato bo'lsa: `ssh-add ~/.ssh/id_ed25519` (agent), yoki HTTPS + `gh auth login`. Maxfiy `id_ed25519` fayliga tegilmaydi.

### O'rta — `dev-log` ni e'lon qilish
Mini loyihani yarating: `todo.py` (namuna 1 yoki o'zingizning kichik dasturingiz), `README.md`, `.gitignore`. Kamida 3 ta mazmunli commit qiling (masalan: dastur; README; .gitignore). GitHub'da bo'sh `dev-log` repo oching, remote ulang, `git push -u origin main`.
**Kutiladigan natija:** repo sahifasida 3 ta commit, README chiroyli ko'rinadi, `tasks.json` va `__pycache__/` repoda yo'q.
**Yechim:** 2-bo'limdagi «Namuna 2» ketma-ketligi; commit xabarlari: `feat: ...`, `docs: ...`, `chore: ...`. Tekshirish: `git log --oneline` (3 qator), GitHub'da faylar ro'yxati. Agar `tasks.json` ko'rinsa: Namuna 5.

### O'rta — Issue → commit → yopish
Repoda 2 ta Issue oching: «README'ga ishga tushirish bo'limini qo'shish» (label: documentation) va «vazifani o'chirish buyrug'i (`delete`) qo'shish» (label: enhancement). Birinchisini commit orqali yoping.
**Kutiladigan natija:** birinchi Issue `Closed`, uning ichida yopgan commit havolasi; ikkinchisi `Open`.
**Yechim:** README'ni tahrirlab: `git commit -am "docs: ishga tushirish bo'limi. Closes #1"` → `git push`. Issue raqamlari 1 va 2 bo'lmasa, mos raqamni yozing.

### Qiyin — Ikkinchi nusxa va pull
`git clone` bilan loyihani boshqa papkaga yuklang. Nusxada (`dev-log-nusxa`) `todo.py` ga `delete` buyrug'ini qo'shing, commit va push qiling. Asl papkaga qaytib, `git fetch`, `git log origin/main --oneline`, so'ng `git pull`. Fetch va pull farqini o'z so'zlaringiz bilan yozing.
**Kutiladigan natija:** fetch'dan keyin `git status` «behind 1 commit» deydi, ishchi fayllar o'zgarmagan; pull'dan keyin `delete` kodi paydo bo'ladi.
**Yechim:** `fetch` faqat `origin/main` ni yangilaydi (ishchi fayllar teginilmaydi), `pull` esa uni joriy shoxga qo'shadi (`fetch` + `merge`). Delete namunasi: `elif buyruq == "delete" and len(args) > 1 and args[1].isdigit(): i = int(args[1]) - 1; if 0 <= i < len(vazifalar): vazifalar.pop(i); saqla(vazifalar)`.

### Qiyin (bonus, kuchli o'quvchi uchun) — Sir sizib chiqdi
Test rejimi: `.env` fayliga **soxta** qiymat (`API_KEY=soxta-qiymat-12345`) yozing va uni tasodifan commit qilib push qiling (faqat shu mashq repo'sida, haqiqiy kalit EMAS). So'ng to'g'ri tuzatish ketma-ketligini bajaring va yozma tushuntiring: nega shunchaki faylni o'chirish yetmaydi?
**Kutiladigan natija:** `.env` `.gitignore` da, kuzatuvdan chiqarilgan; yozma xulosada «haqiqiy kalit bo'lsa avval bekor qilinadi (revoke), tarix eski commit'da saqlanadi» fikri bor.
**Yechim:** `echo ".env" >> .gitignore; git rm --cached .env; git commit -m "chore: .env kuzatuvdan chiqarildi"; git push`. Faylni o'chirgan commit oxirgi holatni o'zgartiradi, ammo eski commit'da qiymat qoladi (`git log -p -- .env` ko'rsatadi). Haqiqiy sirda: avval sirni almashtirish/bekor qilish, so'ng tarixni tozalash vositasi (masalan `git filter-repo`) — bu keyingi bosqichda.

## 5. Tezkor nazorat
1. Git va GitHub farqi nima? *(Git — lokal dastur; GitHub — repolarni saqlaydigan va hamkorlik beradigan xizmat.)*
2. `git push -u origin main` dagi `origin` va `-u` nima? *(origin — masofaviy repo nomi; `-u` — upstream, keyin `git push/pull` argumentsiz ishlaydi.)*
3. `fetch` va `pull` farqi? *(fetch yuklaydi, pull yuklab + birlashtiradi.)*
4. `.gitignore` ga nimalar kiritiladi va nega `.env` shu yerda bo'lishi shart? *(Sirlar, chiqindilar, OS/IDE fayllari; sir tarixga tushsa yo'qolmaydi.)*
5. Token tasodifan GitHub'ga chiqib ketdi. Birinchi qadam? *(Tokenni darhol bekor qilish/revoke; faylni o'chirish yetarli emas.)*

## 6. Uyga vazifa
`uyga-vazifa.md` dagi 3-dars vazifasi (20–30 daqiqa): `dev-log` repoga yana 2 ta mazmunli commit (masalan `delete` buyrug'i va README'ni yaxshilash), 1 ta Issue yoping va repo havolasini mentorga yuboring (havola ochiq, maxfiy narsa yo'q). Parol/token yubormang.

## 7. Mentor uchun eslatmalar
- Birinchi navbatda xavfsizlik: o'quvchi paroli/tokenini ko'rmang, ekran ulashishda terminalda `cat id_ed25519` (maxfiy) qilinmasin.
- Muammolar: `Permission denied (publickey)` (kalit qo'shilmagan/agent), `remote origin already exists` (`git remote set-url origin ...`), `rejected (non-fast-forward)` (avval `git pull`), `master` vs `main` (`git branch -M main`).
- Brauzer va GitHub interfeysi o'zgarishi mumkin (menyu nomlari). Asosiy yo'l: Settings → SSH and GPG keys; Settings → Developer settings → Personal access tokens.
- Agar GitHub'ga kirishda muammo (13+ yosh, telefon tasdiqlash) bo'lsa — mentor bilan hal qilinadi; akkaunt o'quvchining o'ziniki.
- Dars hajmi katta: 2.7–2.9 qisqartirilsa, README va `.gitignore` amaliyot davomida tushuntirilsin.
