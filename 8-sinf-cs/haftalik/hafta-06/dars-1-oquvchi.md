# 16-dars. Git va GitHub bilan tanishuv (3-qism): GitHub akkaunti va loyihani repositoryga joylash

> Kompyuterdagi «Kundalik» loyihasi buzilsa, hammasi yo'qoladi. Bugun uni GitHub'ga joylaymiz: loyiha internetda saqlanadi va uni boshqalarga ko'rsatish mumkin bo'ladi.

## Dars xulosasi

- GitHub — loyihalarni internetda saqlaydigan sayt.
- Akkaunt: 13+ yosh, ota-ona bilan, kuchli parol, 2FA.
- Yangi repo bo'sh yaratiladi, nomi aniq bo'ladi.
- `git remote add origin URL` — GitHub'ga ulanish.
- `git push -u origin main` — birinchi yuklash.
- Keyin: add → commit → push.

## Qo'shimcha ma'lumot

### Private repo
Faqat siz va taklif qilinganlar ko'radi.

### README
Repo sahifasida birinchi ko'rinadi.

### Token
Parol o'rniga ishlatiladigan maxsus kalit.

### Profil README
Username nomli repo profilda ko'rinadi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| GitHub | Loyihalarni internetda saqlaydigan sayt |
| Remote | Masofaviy repository manzili |
| origin | Remote'ning odatiy nomi |
| Push | Commitlarni GitHub'ga yuborish |
| Public | Hamma ko'radigan repo |
| Private | Yopiq repo |
| 2FA | 2 bosqichli tekshiruv |
| URL | Repository manzili |

## Bilasizmi?

- GitHub 2018-yildan Microsoft'ga tegishli, Git esa ochiq dastur.
- Terminalda parol o'rniga ko'pincha brauzer orqali kirish yoki maxsus token ishlatiladi.
- Shaxsiy kalit yoki parolni hech qachon GitHub'ga yuklamang.

## Topshiriqlar

### 1. Git va GitHub · oson

Git va GitHub farqini bir jumlada yozing.

**Kutiladigan natija:** Git — dastur, GitHub — sayt.

### 2. Yosh chegarasi · oson

GitHub akkaunti uchun eng kichik yosh qancha?

**Kutiladigan natija:** 13 yosh.

### 3. Repo manzili · oson

`github.com/vali/sayt.git` dan egani va repo nomini toping.

**Kutiladigan natija:** Ega `vali`, repo `sayt`.

### 4. Public/Private · oson

Ikki ko'rinish farqini yozing.

**Kutiladigan natija:** Public — hamma, Private — taklif qilinganlar.

### 5. Username tanlash · o'rta

3 ta xavfsiz username taklif qiling.

**Kutiladigan natija:** Shaxsiy ma'lumotsiz nomlar.

### 6. Remote buyrug'i · o'rta

GitHub manzilini ulaydigan buyruqni yozing.

**Kutiladigan natija:** `git remote add origin URL`.

### 7. Tekshirish · o'rta

Ulanishni qaysi buyruq ko'rsatadi?

**Kutiladigan natija:** `git remote -v`.

### 8. Bo'sh repo · o'rta

Nega mavjud loyiha uchun README qo'shilmaydi?

**Kutiladigan natija:** Tarixlar farq qilmasligi uchun.

### 9. Birinchi push · qiyin

Birinchi yuklash buyruqlarini tartib bilan yozing.

**Kutiladigan natija:** `branch -M main`, `push -u origin main`.

### 10. Keyingi push · qiyin

Fayl o'zgarganda 3 ta buyruq ketma-ketligi?

**Kutiladigan natija:** add, commit, push.

### 11. Xatoni toping · qiyin

Push'dan keyin GitHub'da yangi fayl yo'q. Sabab?

**Kutiladigan natija:** Commit qilinmagan.

### 12. Portfolio g'oyasi · bonus

GitHub'da qanday 3 ta loyiha ko'rsatgan bo'lardingiz?

**Kutiladigan natija:** Asoslangan g'oyalar.

## O'zingizni tekshiring

1. GitHub nima?
2. Akkaunt xavfsizligi qoidalari?
3. Repo qanday yaratiladi?
4. remote nima?
5. push nima qiladi?
6. Keyingi o'zgarishlar qanday yuklanadi?

## Uyga vazifa

«Kundalik» loyihangizni GitHub'ga yuklang (ota-ona yordami bilan), 25–30 daqiqa. To'liq shart: `uyga-vazifa.md`.
