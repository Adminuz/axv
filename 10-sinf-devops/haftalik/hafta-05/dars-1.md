# 13-dars. Matn filtralari va muntazam ifodalar: grep, sed, awk va xargs amaliyoti

**Darsning maqsadi:** O'quvchi `grep` bilan qidiradi (`-i`, `-n`, `-v`, `-c`, `-r`, `-E`), oddiy muntazam ifodalarni (`^`, `$`, `.`, `*`, `[0-9]`) yozadi, `sed` bilan almashtiradi va qator tanlaydi, `awk` bilan ustunlarni ajratadi va sanaydi, `xargs` bilan buyruq natijasini argument sifatida uzatadi.

**Manba (rasmiy hujjat):** O'quv qo'llanma: `grep "port" app.log`, `ps aux | grep ssh`, `df -Th | grep /dev`, `ps aux | grep nginx | awk '{print $2}' | xargs kill -9` misollari va pipe/redirect bo'limi. `sed`, `awk`, `xargs` va regex sintaksisi hujjatda qisqa (faqat bitta zanjir), shu sababli rejadagi mavzu bo'yicha qo'shildi.

**Vaqt taqsimoti (80 daqiqa):**
- Takrorlash: 10 daqiqa (Sikllar, `while read`, `sort | uniq`)
- 01. grep va regex: 15 daqiqa
- 02. sed va awk: 15 daqiqa
- Tanaffus: 5 daqiqa
- 03. xargs va zanjir: 15 daqiqa
- Amaliyot: 15 daqiqa
- Xulosa va tezkor nazorat: 5 daqiqa

---

## 1. Konspekt (mentor uchun)

### 1.1. grep va muntazam ifodalar
`grep` fayl yoki quvur oqimidan naqshga mos qatorlarni topadi. Foydali flaglar: `-i` (registrni e'tiborsiz), `-n` (qator raqami), `-v` (mos kelmaganlar), `-c` (sanoq), `-r` (papkada rekursiv), `-E` (kengaytirilgan regex). Regex belgilari: `^` qator boshi, `$` qator oxiri, `.` istalgan bitta belgi, `*` oldingi belgining 0 va undan ko'p marta takrori, `[0-9]` raqam, `-E` bilan `+`, `?`, `|`.
```bash
cat > app.log <<'EOF'
2025-03-01 10:00:01 INFO server started port=8080
2025-03-01 10:00:05 WARN disk 85%
2025-03-01 10:01:12 ERROR db timeout user=ali
2025-03-01 10:02:30 INFO login user=vali
2025-03-01 10:03:44 ERROR db timeout user=soli
EOF
grep ERROR app.log
grep -c ERROR app.log
grep -n -i "login" app.log
grep -v INFO app.log
grep -E "ERROR|WARN" app.log
grep "user=a.i" app.log
grep "^2025" app.log
```
`grep -c ERROR app.log` ikkita ERROR qatori bo'lgani uchun `2` chiqaradi. Naqshni tirnoqqa oling: shell `*` va `$` belgilarini o'zgartirmasin.

### 1.2. sed va awk
`sed` oqim muharriri: `s/eski/yangi/g` almashtiradi, `-n '3,5p'` faqat 3-5 qatorni chiqaradi, `/naqsh/d` mos qatorlarni o'chiradi. Fayl o'zgarmaydi, natija ekranga chiqadi; faylning o'zini o'zgartirish uchun `-i` (xavfsizlik uchun `-i.bak`). `awk` ustunlar bilan ishlaydi: `$1` birinchi ustun, `$NF` oxirgi, `NR` qator raqami, `-F:` ajratgich. Shartli ishlov: `awk '$3=="ERROR" {print $NF}'`.
```bash
sed 's/ERROR/XATO/' app.log
sed -n '3,5p' app.log
sed '/INFO/d' app.log

awk '{print $3}' app.log
awk '$3=="ERROR" {print $NF}' app.log
awk '{print $3}' app.log | sort | uniq -c
awk -F: '{print $1}' /etc/passwd
```
`sed -i` faylni o'zgartiradi. Avval `-i.bak` bilan nusxa oling yoki natijani ekranda tekshiring.

### 1.3. xargs va quvur zanjirlari
Ko'p buyruqlar stdin dan emas, argumentdan ishlaydi (`kill`, `rm`). `xargs` oldingi buyruq chiqishini argument qilib beradi. O'quv qo'llanmadagi zanjir: `ps aux | grep nginx | awk '{print $2}' | xargs kill -9` — nginx jarayonlarini topadi, PID ustunini oladi va to'xtatadi. Foydali flaglar: `-n 1` (har safar bitta argument), `-I {}` (o'rniga qo'yish). Diqqat: `grep nginx` o'zini ham topadi; `kill -9` oxirgi chora.
```bash
ps aux | grep nginx | awk '{print $2}' | xargs kill -9

ps aux | grep [n]ginx | awk '{print $2}'
find . -name "*.log" | xargs grep -l ERROR
echo "a b c" | xargs -n 1 echo
ls *.txt | xargs -I {} cp {} yedek/
```
`[n]ginx` naqshi `grep` ning o'zini topmaydi. Avval `kill` siz natijani ko'ring, so'ng `xargs kill` qo'shing; imkon bo'lsa `kill -9` o'rniga oddiy `kill` ishlating.

---

## 2. Amaliy topshiriqlar va yechimlari

### 1-topshiriq (oson). ERROR sanash
`app.log` da ERROR qatorlari sonini toping.

**Yechim:**
```bash
grep -c ERROR app.log
# 2
```

### 2-topshiriq (o'rta). Foydalanuvchilar
ERROR qatorlaridagi foydalanuvchi nomlarini (user=...) chiqaring.

**Yechim:**
```bash
grep ERROR app.log | awk '{print $NF}'
# user=ali
# user=soli
```

### 3-topshiriq (o'rta). Almashtirish
`sed` bilan ERROR so'zini XATO ga almashtirib, faqat shu qatorlarni chiqaring.

**Yechim:**
```bash
sed 's/ERROR/XATO/' app.log | grep XATO
```

### 4-topshiriq (qiyin). Daraja hisoboti
Har bir daraja (INFO, WARN, ERROR) necha marta uchraganini eng ko'pidan boshlab chiqaring.

**Yechim:**
```bash
awk '{print $3}' app.log | sort | uniq -c | sort -rn
```

---

## 3. Tezkor nazorat
1. **`grep -v` nima qiladi?** *Javob:* Naqshga mos kelmagan qatorlarni chiqaradi.
2. **`^` va `$` nima?** *Javob:* Qator boshi va oxiri.
3. **`sed 's/a/b/g'` nima qiladi?** *Javob:* Hamma `a` ni `b` ga almashtiradi (ekranda).
4. **`$NF` nima?** *Javob:* `awk` da oxirgi ustun.
5. **`xargs` nega kerak?** *Javob:* Chiqishni buyruqqa argument qilib berish uchun (masalan, `kill`).

## Mentor uchun eslatma
Hujjatda `sed` va `awk` bo'yicha alohida bo'lim yo'q (faqat bitta quvur zanjiri va `grep` misollari), shu sababli sintaksis rejadagi mavzu bo'yicha qo'shildi. `app.log` namunaviy fayl, o'quvchilar uni heredoc bilan yaratadi. `kill -9` mashqini faqat o'zi ishga tushirgan jarayonda (masalan, `sleep 300 &`) o'tkazing, tizim jarayonlarida emas. macOS da `sed -i` sintaksisi farq qiladi (`-i ''`), shu sababli Linux da bajarish tavsiya etiladi.
