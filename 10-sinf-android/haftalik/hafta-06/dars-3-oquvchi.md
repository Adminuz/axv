# 18-dars. implementation, api, compileOnly kabi dependency turlari

> Bir kutubxonani ulashning bir necha usuli bor va ular build tezligiga ta'sir qiladi. Bugun dependency turlarini ajratamiz.

## Dars xulosasi

- `implementation` — default: kutubxona faqat joriy modulda ko'rinadi.
- `api` — kutubxona boshqa modullarga ham ochiladi.
- `compileOnly` — faqat kompilyatsiya; `runtimeOnly` — faqat ish vaqti.
- `testImplementation` — unit testlar; `androidTestImplementation` — qurilma testlari.
- Shubhada `implementation` yozing: build tezroq, bog'liqlik toza.
- Tur kutubxonaning kimga va qachon kerakligini ifodalaydi.

## Qo'shimcha ma'lumot

### Nega implementation tezroq?
Kutubxona o'zgarganda faqat uni ishlatayotgan modullar qayta yig'iladi, `api` esa zanjir bo'ylab qayta yig'ishni keltiradi.

### Eski compile
`compile` turi ko'p yillar oldin `implementation` va `api` ga bo'lingan; eski kodda uchrasa, almashtiring.

### Test turlari
Test kutubxonalari release APK ga tushmaydi, shuning uchun hajm kattalashmaydi.

### Ko'p modul
`app` odatda `core`, `data`, `feature` modullariga `implementation(project(...))` bilan bog'lanadi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| implementation | Modul ichida ko'rinuvchi bog'liqlik |
| api | Boshqa modullarga ochiq bog'liqlik |
| compileOnly | Faqat kompilyatsiya uchun |
| runtimeOnly | Faqat ish vaqti uchun |
| testImplementation | Unit test kutubxonasi |
| androidTestImplementation | Qurilma test kutubxonasi |
| Modul | Loyihaning alohida qismi |
| Transitive | Ichki bog'liqlik |

## Bilasizmi?

- `implementation` o'zgarganda kamroq modul qayta yig'iladi: bu katta loyihada build vaqtini kamaytiradi.
- Eski Gradle da `compile` turi bor edi; u `implementation` va `api` ga bo'lingan.
- Qo'llanma `implementation`, `api`, `compileOnly` farqini asosiy savollar qatorida beradi.

## Topshiriqlar

### 1. Turlarni sanang · oson

6 ta dependency turini va qisqa vazifasini yozing.

**Kutiladigan natija:** 6 ta tur.

### 2. Default · oson

Qaysi tur default va nega?

**Kutiladigan natija:** `implementation`.

### 3. api qachon · oson

`api` ni qachon ishlatasiz?

**Kutiladigan natija:** Boshqa modul ham kutubxonani ko'rishi kerak bo'lsa.

### 4. Test turlari · oson

JUnit va Espresso qaysi turlarda?

**Kutiladigan natija:** testImplementation, androidTestImplementation.

### 5. Tanlang · o'rta

Coil, JUnit, annotatsiya uchun tur tanlang.

**Kutiladigan natija:** implementation, testImplementation, compileOnly.

### 6. Xatoni toping · o'rta

`core` da Gson `implementation`, `app` da Gson ishlatilgan. Nima xato?

**Kutiladigan natija:** Gson `app` ga ochiq emas.

### 7. compileOnly · o'rta

`compileOnly` kutubxona APK ga tushadimi?

**Kutiladigan natija:** Yo'q.

### 8. runtimeOnly · o'rta

`runtimeOnly` ga misol keltiring.

**Kutiladigan natija:** Ish vaqtidagi drayver.

### 9. Ikki modul · qiyin

`core` va `app` uchun dependencies yozing.

**Kutiladigan natija:** api va implementation(project).

### 10. Build tezligi · qiyin

Hammasi `api` bo'lsa, build nima uchun sekinlashadi?

**Kutiladigan natija:** Qayta yig'ish zanjiri uzayadi.

### 11. Refaktoring · qiyin

3 ta keraksiz `api` ni `implementation` ga o'zgartirish rejasini yozing.

**Kutiladigan natija:** Qadamlar ro'yxati.

### 12. Eski compile · bonus

Eski `compile` ni qanday almashtirasiz?

**Kutiladigan natija:** implementation yoki api.

## O'zingizni tekshiring

1. `implementation` va `api` farqi?
2. `compileOnly` nima?
3. `runtimeOnly` nima?
4. Test turlari?
5. Qaysi tur default?
6. Hammasi `api` bo'lsa nima bo'ladi?

## Uyga vazifa

Ikki modulda dependency turlarini sinab ko'ring (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
