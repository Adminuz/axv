# 10-dars. Bash skripting asoslari: o'zgaruvchilar, argumentlar va kiritish/chiqarish (read, echo, printf)

**Darsning maqsadi:** O'quvchi buyruqlarni faylga yozib birinchi Bash skriptini yaratadi (`#!/bin/bash`, `chmod +x`), o'zgaruvchi e'lon qiladi, qo'sh va bitta tirnoq farqini biladi, `$(buyruq)` bilan natijani o'zgaruvchiga oladi, skriptga argument (`$1`, `$#`, `$@`) beradi va `read`, `echo`, `printf` bilan ma'lumot kiritadi/chiqaradi.

**Manba (rasmiy hujjat):** o'quv qo'llanma va uslubiy ko'rsatmadagi «Shell muhiti va tizim o'zgaruvchilari» bo'limi (shell scripting ta'rifi, uch tur o'zgaruvchi: Local, Environment, Shell/System; `USER`, `HOME`, `PWD`, `SHELL`, `printenv`, `env`), stdin/stdout oqimlari va IaC bobidagi imperativ bash skript misoli (`apt update`, `apt install -y nginx`, ...).

**Vaqt taqsimoti (80 daqiqa):**
- Takrorlash (3-hafta: tarmoq diagnostikasi; 1-hafta: shell o'zgaruvchilari, PATH, chmod): 10 daqiqa
- 01. Skript nima? Shebang, `chmod +x`, ishga tushirish: 15 daqiqa
- 02. O'zgaruvchilar, tirnoqlar, `$(...)`: 15 daqiqa
- Tanaffus: 5 daqiqa
- 03. Argumentlar va `read`/`echo`/`printf`: 15 daqiqa
- Amaliyot: 25 daqiqa
- Xulosa va tezkor nazorat: 5 daqiqa

---

## 1. Konspekt (mentor uchun)

### 1.1. Shell scripting nima?
Qo'llanmaga ko'ra: buyruqlar ketma-ketligini fayl ko'rinishida yozib, shell orqali bajarish **shell scripting** deyiladi. U Linuxda jarayonlarni avtomatlashtirishga yordam beradi. Shell (bash, Bourne Again Shell) foydalanuvchi va kernel o'rtasidagi interfeys.
Imperativ yondashuv misoli (qo'llanmadan): qadamlar tartibi muhim.
```bash
apt update
apt install -y nginx
cp nginx.conf /etc/nginx/nginx.conf
systemctl restart nginx
```

### 1.2. Skript fayli
```bash
#!/bin/bash
# salom.sh - birinchi skript
ISM="Ali"
echo "Salom, $ISM!"
echo "Papka: $PWD"
echo "Foydalanuvchi: $USER"
```
- `#!/bin/bash` (shebang): skriptni qaysi dastur bajarishini aytadi, birinchi qatorda turishi shart.
- `#` bilan boshlangan qator izoh.
- Ishga tushirish: `chmod +x salom.sh` (yoki `chmod 755`), keyin `./salom.sh`. Ruxsatsiz: `bash salom.sh`.
- Xato: `Permission denied` = `x` ruxsati yo'q (1-haftadagi `chmod`).

### 1.3. O'zgaruvchilar
- Yozuv: `NOM="qiymat"`, **tenglik atrofida bo'sh joy yo'q**. Ishlatish: `$NOM` yoki `${NOM}`.
- Qo'llanmadagi uch tur: Local (joriy shellda), Global/Environment (`export PORT=8080`, ko'rish: `printenv`, `env`), Shell/System (`USER`, `HOME`, `PWD`, `SHELL`, `PATH`, katta harf bilan).
- `"..."` ichida `$` ishlaydi, `'...'` ichida matn o'zgarmaydi.
- `$(buyruq)`: buyruq natijasi o'zgaruvchiga: `YIL=$(date +%Y)`.
- `${SON}ta` nom chegarasini aniq ko'rsatadi.

### 1.4. Argumentlar va kiritish/chiqarish
| Belgi | Ma'nosi |
|---|---|
| `$0` | skript nomi |
| `$1`, `$2` | 1-, 2-argument |
| `$#` | argumentlar soni |
| `$@` | barcha argumentlar |

- `echo` matn chiqaradi (`-n` qator o'tkazmaydi). `printf` formatli: `%s` matn, `%d` butun son, `\n` yangi qator.
- `read -p "Savol: " NOM` klaviaturadan (stdin) o'qiydi; `-s` yashirin kiritish (parol).
- `$((YOSH + 1))` arifmetika (batafsil 11-darsda).

---

## 2. Amaliy topshiriqlar va yechimlari

### 1-topshiriq (oson). `tanishuv.sh`
Ismni `read` bilan so'rab salomlashing.

**Yechim:**
```bash
#!/bin/bash
read -p "Ismingiz: " ISM
echo "Salom, $ISM!"
```
Kutiladigan natija: `Ismingiz: Ali` kiritilsa `Salom, Ali!`.

### 2-topshiriq (o'rta). Ikki argument va `printf`
`./juft.sh Ali Vali` chaqirilganda `Ali va Vali do'st` chiqsin; argument soni ham ko'rsatilsin.

**Yechim:**
```bash
#!/bin/bash
printf "%s va %s do'st\n" "$1" "$2"
printf "Argumentlar soni: %d\n" "$#"
```

### 3-topshiriq (qiyin). `info.sh`
`$USER`, `$HOME`, bugungi sana (`date +%F`) va joriy papkadagi fayllar sonini bitta hisobotga yig'ing.

**Yechim:**
```bash
#!/bin/bash
SANA=$(date +%F)
SON=$(ls | wc -l)
printf "Foydalanuvchi: %s\nUy papkasi: %s\nSana: %s\nFayllar: %d\n" "$USER" "$HOME" "$SANA" "$SON"
```

### 4-topshiriq (bonus). Yosh kalkulyatori
`read` bilan tug'ilgan yilni so'rab, yoshni hisoblang.

**Yechim:**
```bash
#!/bin/bash
read -p "Tug'ilgan yil: " Y
printf "Yoshingiz: %d\n" $(( $(date +%Y) - Y ))
```

---

## 3. Tezkor nazorat (dars yakuni)
1. **Shebang nima?** *Javob:* skriptning birinchi qatori `#!/bin/bash`, qaysi interpretator bilan ishlashni aytadi.
2. **`NOM = "Ali"` nega xato?** *Javob:* tenglik atrofida bo'sh joy bo'lmasligi kerak, aks holda `NOM` buyruq deb o'qiladi.
3. **`echo '$USER'` nima chiqaradi?** *Javob:* aynan `$USER` matnini (bitta tirnoq).
4. **`./a.sh 5 9 2` da `$#` nechaga teng?** *Javob:* 3.
5. **`Permission denied` nimani anglatadi?** *Javob:* `x` ruxsati yo'q, `chmod +x` kerak.

## Mentor uchun eslatma
Hujjatda skript sintaksisi alohida bobda yo'q: dars rejadagi mavzuga ko'ra tuzildi, tayanch ta'riflar qo'llanmadagi shell scripting bo'limidan olindi. Barcha kod namunalari Bash'da sinab ko'rilgan.
