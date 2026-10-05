# 12-dars. Sikllar va takrorlanishlar (for, while, until) hamda matnli oqimlarni qayta ishlash

**Darsning maqsadi:** O'quvchi `for`, `while`, `until` sikllarini yozadi, `break` va `continue` ni ishlatadi, faylni qatorma-qator o'qiydi (`while read`) va 1-haftadagi quvur (`|`) bilan matnli oqimlarni qayta ishlaydi (`wc`, `sort`, `uniq`, `grep`, `cut`, `head`).

**Manba (rasmiy hujjat):** `for pkg in docker.io docker-doc ...; do sudo apt-get remove $pkg; done` va `while true; do wget -q -O- http://php-apache; done` misollari; stdin/stdout/stderr oqimlari; quvur zanjirlari (`cat | uniq | wc -l`, `ls ~ | wc -l`, `ps aux | grep ssh`, `df -Th | grep /dev`); `wc -l` va `uniq` tavsifi.

**Vaqt taqsimoti (80 daqiqa):**
- Takrorlash (`if`, `test`, `$(( ))`): 10 daqiqa
- 01. `for` sikli: 15 daqiqa
- 02. `while`, `until`, `break`, `continue`: 15 daqiqa
- Tanaffus: 5 daqiqa
- 03. Matnli oqimlar: `while read`, quvurlar: 15 daqiqa
- Amaliyot: 15 daqiqa
- Xulosa va tezkor nazorat: 5 daqiqa

---

## 1. Konspekt (mentor uchun)

### 1.1. for
```bash
for ISM in Ali Vali Soli; do echo "Salom, $ISM"; done
for i in {1..5}; do echo $i; done           # 1 2 3 4 5
for ((i=0; i<3; i++)); do echo $i; done     # C uslubi
for F in *.txt; do echo "Fayl: $F"; done    # wildcard
```
Hujjatdagi misol: ro'yxat bo'yicha paketlarni o'chirish `for pkg in ...; do sudo apt-get remove $pkg; done`.

### 1.2. while va until
- `while` shart rost ekan davomida takrorlaydi: `while [ $n -gt 0 ]; do ...; n=$((n-1)); done`.
- `until` shart yolg'on bo'lguncha takrorlaydi (shart rost bo'lganda to'xtaydi): `until [ $k -ge 3 ]; do ...; done`.
- Cheksiz: `while true; do ...; done` (hujjatda yuklama berishda; to'xtatish `Ctrl+C`).
- `break` siklni to'xtatadi, `continue` keyingi aylanishga o'tadi.

### 1.3. Matnli oqimlar
Foreground jarayon stdin dan oladi, stdout ga chiqaradi (hujjat). Fayl qatorlarini o'qish:
```bash
while read -r QATOR; do echo "> $QATOR"; done < royxat.txt
```
Quvur: `sort royxat.txt | uniq -c`, `cut -d: -f1 /etc/passwd | head -5`, `ls ~ | wc -l`, `ps aux | grep ssh`. Hujjat: `uniq` faqat ketma-ket takrorlarni olib tashlaydi, shuning uchun avval `sort`.

---

## 2. Amaliy topshiriqlar va yechimlari

### 1-topshiriq (oson). 1 dan 10 gacha
**Yechim:**
```bash
for i in {1..10}; do echo $i; done
```

### 2-topshiriq (o'rta). Jadval va yig'indi
Argumentdagi sonning ko'paytirish jadvalini va 1..N yig'indisini chiqaring.

**Yechim:**
```bash
#!/bin/bash
N=$1; SUM=0
for ((i=1; i<=10; i++)); do echo "$N x $i = $((N*i))"; done
for ((i=1; i<=N; i++)); do SUM=$((SUM+i)); done
echo "1..$N yig'indisi: $SUM"
```

### 3-topshiriq (qiyin). Foydalanuvchilar hisoboti
`/etc/passwd` dan foydalanuvchi nomlarini (`cut`) qatorma-qator o'qib, raqam bilan chiqaring va umumiy sonni ko'rsating.

**Yechim:**
```bash
#!/bin/bash
N=0
while read -r NOM; do
  N=$((N+1))
  echo "$N. $NOM"
done < <(cut -d: -f1 /etc/passwd)
echo "Jami: $N"
```
(`< <(...)` process substitution Bash'da ishlaydi; muqobil: `cut ... | while read` va `wc -l`.)

### 4-topshiriq (bonus). Taxmin o'yini
1..20 orasida kompyuter son o'ylaydi (`$((RANDOM % 20 + 1))`), foydalanuvchi topguncha `until` bilan so'raydi, «katta/kichik» deydi.

**Yechim:**
```bash
#!/bin/bash
X=$((RANDOM % 20 + 1)); T=0
until [ "$T" -eq "$X" ]; do
  read -p "Taxmin: " T
  if [ "$T" -lt "$X" ]; then echo "kattaroq"
  elif [ "$T" -gt "$X" ]; then echo "kichikroq"; fi
done
echo "To'g'ri: $X"
```

---

## 3. Tezkor nazorat
1. **`for i in {1..3}` nechta aylanish?** *Javob:* 3 ta (1, 2, 3).
2. **`while` va `until` farqi?** *Javob:* `while` shart rost bo'lsa, `until` shart yolg'on bo'lsa davom etadi.
3. **`continue` nima qiladi?** *Javob:* joriy aylanishni tashlab, keyingisiga o'tadi.
4. **`uniq` dan oldin nega `sort`?** *Javob:* `uniq` faqat ketma-ket takrorlarni ko'radi.
5. **`while read -r Q; do ...; done < fayl` nima qiladi?** *Javob:* faylni qatorma-qator o'qiydi.

## Mentor uchun eslatma
Hujjatda sikllar bo'yicha alohida bo'lim yo'q (faqat `for` va `while true` misollari); sintaksis rejadagi mavzu bo'yicha qo'shildi. Kod Bash'da sinalgan (macOS bash 3.2 da ham `{1..5}` va `(( ))` ishlaydi).
