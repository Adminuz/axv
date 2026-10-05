# 11-dars. Shart operatorlari va mantiqiy ifodalar (if/elif/else, test, [[ ]], arifmetik amallar)

**Darsning maqsadi:** O'quvchi skriptga qaror qabul qilishni o'rgatadi: chiqish kodi (`$?`), `test` / `[ ]` / `[[ ]]`, matn, son va fayl tekshiruvlari, `if / elif / else / fi`, mantiqiy `&&`, `||`, `!` va arifmetika (`$(( ))`, `(( ))`).

**Manba (rasmiy hujjat):** shell scripting ta'rifi (o'zgaruvchilar, buyruqlar ketma-ketligi), `&&` bilan buyruq zanjiri (`apt update && apt upgrade -y`, `git switch main && git pull --ff-only`), imperativ skript va idempotentlik haqidagi bo'lim (skriptni ikki marta ishlatish xato berishi mumkin: shart bilan tekshirish shu muammoni yechadi).

**Vaqt taqsimoti (80 daqiqa):**
- Takrorlash (10-dars: o'zgaruvchi, `read`, `$1`): 10 daqiqa
- 01. Chiqish kodi va `test` / `[ ]` / `[[ ]]`: 20 daqiqa
- 02. `if / elif / else` va `&&`, `||`: 15 daqiqa
- Tanaffus: 5 daqiqa
- 03. Arifmetik amallar: 10 daqiqa
- Amaliyot: 15 daqiqa
- Xulosa va tezkor nazorat: 5 daqiqa

---

## 1. Konspekt (mentor uchun)

### 1.1. Chiqish kodi
Har buyruq tugagach son qaytaradi, `$?` da ko'rinadi: `0` = muvaffaqiyat, boshqa son = xato.
```bash
ls /tmp;  echo $?     # 0
ls /yoq;  echo $?     # 0 emas (xato)
```
`if` aynan shu kodga qaraydi.

### 1.2. test, `[ ]`, `[[ ]]`
`test ifoda` va `[ ifoda ]` bir xil. `[[ ]]` Bash'ning kengaytirilgan varianti (naqsh `==`, `&&`, `||`, o'zgaruvchi atrofida tirnoq majburiy emas). Qavs ichida **bo'sh joylar shart**: `[ $A -eq 5 ]`.

| Turi | Operatorlar |
|---|---|
| Son | `-eq -ne -lt -le -gt -ge` |
| Matn | `= (==)`, `!=`, `-z` (bo'sh), `-n` (bo'sh emas) |
| Fayl | `-e` bor, `-f` oddiy fayl, `-d` papka, `-r -w -x` ruxsat |
| Mantiq | `!` (inkor), `&&`, `||` |

### 1.3. if / elif / else
```bash
#!/bin/bash
read -p "Son: " S
if [ "$S" -lt 0 ]; then
  echo "manfiy"
elif [ "$S" -eq 0 ]; then
  echo "nol"
else
  echo "musbat"
fi
```
`then` alohida qatorda yoki `;` dan keyin, `fi` bilan tugaydi.

### 1.4. && va ||
`A && B`: B faqat A muvaffaqiyatli bo'lsa. `A || B`: B faqat A xato bo'lsa. Hujjat: `apt update && apt upgrade -y`.
```bash
[ -f config.txt ] || echo "config.txt topilmadi"
mkdir -p log && cd log
```
Idempotentlik: `[ -d backup ] || mkdir backup` skriptni ikki marta ishlatsa ham xato bermaydi.

### 1.5. Arifmetika
Bash o'zgaruvchilari matn; hisob uchun `$(( ))`: `+ - * / % **`. Butun son bo'lish: `$((7/2))` = 3, `$((7%2))` = 1. `(( ))` shartda: `if (( S % 2 == 0 ))`. Kasr kerak bo'lsa `bc` (qo'shimcha).

---

## 2. Amaliy topshiriqlar va yechimlari

### 1-topshiriq (oson). Juft yoki toq
**Yechim:**
```bash
#!/bin/bash
read -p "Son: " S
if (( S % 2 == 0 )); then echo "juft"; else echo "toq"; fi
```

### 2-topshiriq (o'rta). Fayl tekshiruvi
Argument sifatida berilgan nom fayl, papka yoki yo'qligini aytsin; argument berilmasa yordam matni chiqsin.

**Yechim:**
```bash
#!/bin/bash
if [ -z "$1" ]; then
  echo "Ishlatish: $0 <nom>"
  exit 1
fi
if [ -f "$1" ]; then echo "fayl"
elif [ -d "$1" ]; then echo "papka"
else echo "topilmadi"
fi
```

### 3-topshiriq (qiyin). Baho
Ball (0-100) bo'yicha: 86+ `5`, 71-85 `4`, 56-70 `3`, qolgani `2`; 0-100 dan tashqari bo'lsa «noto'g'ri ball».

**Yechim:**
```bash
#!/bin/bash
read -p "Ball: " B
if [ "$B" -lt 0 ] || [ "$B" -gt 100 ]; then echo "noto'g'ri ball"
elif [ "$B" -ge 86 ]; then echo 5
elif [ "$B" -ge 71 ]; then echo 4
elif [ "$B" -ge 56 ]; then echo 3
else echo 2
fi
```

### 4-topshiriq (bonus). Idempotent zaxira
`backup` papkasi yo'q bo'lsa yaratsin, bor bo'lsa «allaqachon bor» desin; so'ng `info.txt` ni unga nusxalasin.

**Yechim:**
```bash
#!/bin/bash
if [ -d backup ]; then echo "allaqachon bor"; else mkdir backup; fi
[ -f info.txt ] && cp info.txt backup/
```

---

## 3. Tezkor nazorat
1. **`$?` nima?** *Javob:* oxirgi buyruqning chiqish kodi; 0 = muvaffaqiyat.
2. **`[ $A -eq 5 ]` va `[$A -eq 5]` farqi?** *Javob:* ikkinchisida bo'sh joy yo'q, xato (`[` alohida buyruq).
3. **`-z` nimani tekshiradi?** *Javob:* matn bo'shligini.
4. **`$((9/2))` nechaga teng?** *Javob:* 4 (butun bo'lish).
5. **`A || B` da B qachon bajariladi?** *Javob:* A xato qaytarganda.

## Mentor uchun eslatma
Rasmiy hujjatda `if/test/[[ ]]` bo'yicha alohida bo'lim yo'q: rejadagi mavzu bo'yicha tuzildi, `&&` va idempotentlik tushunchalari hujjatdan. Barcha kod Bash'da sinalgan.
