<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { withBase } from 'vitepress'
import Icon from './Icon.vue'
import Crumbs from './Crumbs.vue'

// --- Active Tab State ---
// 'binary' | 'logic' | 'memory' | 'flowchart' | 'hardware'
const activeTab = ref<string>('binary')

// ==========================================
// 1. IKKILIK SANOQ TIZIMI VA BITLAR (BINARY)
// ==========================================
const bitValues = [128, 64, 32, 16, 8, 4, 2, 1]
const bits = ref<number[]>([0, 0, 0, 0, 0, 0, 0, 0])

const toggleBit = (index: number) => {
  bits.value[index] = bits.value[index] === 1 ? 0 : 1
}

const decimalValue = computed(() => {
  return bits.value.reduce((acc, bit, idx) => acc + bit * bitValues[idx], 0)
})

const binaryString = computed(() => bits.value.join(''))
const hexValue = computed(() => '0x' + decimalValue.value.toString(16).toUpperCase().padStart(2, '0'))
const octalValue = computed(() => '0o' + decimalValue.value.toString(8))
const asciiChar = computed(() => {
  const code = decimalValue.value
  if (code >= 32 && code <= 126) return String.fromCharCode(code)
  if (code === 0) return 'NULL'
  if (code === 32) return 'Bo\'sh joy (Space)'
  return 'Maxsus belgi'
})

const setDecimal = (num: number) => {
  const clamped = Math.max(0, Math.min(255, num))
  const binary = clamped.toString(2).padStart(8, '0')
  bits.value = binary.split('').map(Number)
}

const resetBits = () => {
  bits.value = [0, 0, 0, 0, 0, 0, 0, 0]
}

// Binary Game Mode
const gameTarget = ref<number>(42)
const gameScore = ref<number>(0)
const gameStreak = ref<number>(0)
const gameFeedback = ref<string>('')

const generateNewGameTarget = () => {
  gameTarget.value = Math.floor(Math.random() * 254) + 1
  resetBits()
  gameFeedback.value = ''
}

const checkGameAnswer = () => {
  if (decimalValue.value === gameTarget.value) {
    gameScore.value += 10
    gameStreak.value += 1
    gameFeedback.value = 'success'
    setTimeout(() => {
      generateNewGameTarget()
    }, 900)
  } else {
    gameStreak.value = 0
    gameFeedback.value = 'error'
  }
}

// ==========================================
// 2. MANTIQIY ELEMENTLAR (LOGIC GATES)
// ==========================================
const gateType = ref<'AND' | 'OR' | 'NOT' | 'XOR' | 'NAND' | 'NOR'>('AND')
const inputA = ref<number>(0)
const inputB = ref<number>(0)

const gateOutput = computed(() => {
  const a = inputA.value === 1
  const b = inputB.value === 1
  switch (gateType.value) {
    case 'AND': return (a && b) ? 1 : 0
    case 'OR': return (a || b) ? 1 : 0
    case 'NOT': return (!a) ? 1 : 0
    case 'XOR': return (a !== b) ? 1 : 0
    case 'NAND': return !(a && b) ? 1 : 0
    case 'NOR': return !(a || b) ? 1 : 0
    default: return 0
  }
})

const gateExplanations: Record<string, { desc: string; formula: string; code: string }> = {
  AND: {
    desc: 'VA (AND) — Ikkala kirish ham 1 (rost) bo\'lgandagina chiqish 1 bo\'ladi. Birontasi 0 bo\'lsa — natija 0.',
    formula: 'A · B (yoki A ∧ B)',
    code: 'if a and b: # ikkisi ham rost bo\'lishi shart'
  },
  OR: {
    desc: 'YOKI (OR) — Kirishlardan kamida bittasi 1 bo\'lsa, chiqish 1 bo\'ladi. Ikkisi ham 0 bo\'lsagina natija 0.',
    formula: 'A + B (yoki A ∨ B)',
    code: 'if a or b: # kamida bittasi rost bo\'lsa yetarli'
  },
  NOT: {
    desc: 'INKOR (NOT) — Kirish signalini teskarisiga aylantiradi: 0 bo\'lsa 1, 1 bo\'lsa 0 qiladi (Faqat bitta kirish).',
    formula: '¬A (yoki !A)',
    code: 'if not a: # teskari qiymat'
  },
  XOR: {
    desc: 'ISTISNO YOKI (XOR) — Kirishlar har xil bo\'lganda 1, bir xil bo\'lganda 0 chiqadi.',
    formula: 'A ⊕ B',
    code: 'if a != b: # biri 1, ikkinchisi 0 bo\'lganda'
  },
  NAND: {
    desc: 'AND ning teskarisi (NOT-AND) — Ikkisi ham 1 bo\'lgandagina 0 beradi, qolgan barcha holatda 1.',
    formula: '¬(A · B)',
    code: 'not (a and b)'
  },
  NOR: {
    desc: 'OR ning teskarisi (NOT-OR) — Ikkisi ham 0 bo\'lgandagina 1 beradi, qolgan holatlarda 0.',
    formula: '¬(A + B)',
    code: 'not (a or b)'
  }
}

const truthTableRows = computed(() => {
  if (gateType.value === 'NOT') {
    return [
      { a: 0, b: '-', out: 1 },
      { a: 1, b: '-', out: 0 }
    ]
  }
  const combinations = [
    { a: 0, b: 0 },
    { a: 0, b: 1 },
    { a: 1, b: 0 },
    { a: 1, b: 1 }
  ]
  return combinations.map(c => {
    let out = 0
    const a = c.a === 1, b = c.b === 1
    if (gateType.value === 'AND') out = (a && b) ? 1 : 0
    else if (gateType.value === 'OR') out = (a || b) ? 1 : 0
    else if (gateType.value === 'XOR') out = (a !== b) ? 1 : 0
    else if (gateType.value === 'NAND') out = !(a && b) ? 1 : 0
    else if (gateType.value === 'NOR') out = !(a || b) ? 1 : 0
    return { a: c.a, b: c.b, out }
  })
})

// ==========================================
// 3. AXBOROT HAJMI VA XOTIRA (MEMORY)
// ==========================================
const inputDataValue = ref<number>(1)
const inputDataUnit = ref<string>('GB')

const unitsPower: Record<string, number> = {
  Bit: 1 / 8,
  Bayt: 1,
  KB: 1024,
  MB: 1024 ** 2,
  GB: 1024 ** 3,
  TB: 1024 ** 4
}

const totalBytes = computed(() => {
  const factor = unitsPower[inputDataUnit.value] || 1
  return inputDataValue.value * factor
})

const convertedValues = computed(() => {
  const bytes = totalBytes.value
  return {
    bits: (bytes * 8).toLocaleString('uz-UZ'),
    bytes: Math.round(bytes).toLocaleString('uz-UZ'),
    kb: (bytes / 1024).toFixed(2),
    mb: (bytes / (1024 ** 2)).toFixed(3),
    gb: (bytes / (1024 ** 3)).toFixed(4),
    tb: (bytes / (1024 ** 4)).toFixed(6)
  }
})

const realWorldAnalogy = computed(() => {
  const gb = totalBytes.value / (1024 ** 3)
  const mb = totalBytes.value / (1024 ** 2)
  const kb = totalBytes.value / 1024

  if (gb >= 1) {
    const movies = (gb / 1.5).toFixed(1)
    const photos = Math.round(gb * 300)
    const books = Math.round(gb * 1000)
    return `Bu hajmga taxminan ${movies} ta Full HD film, ${photos.toLocaleString()} ta sifatli fotosurat yoki ${books.toLocaleString()} ta elektron kitob sig'adi.`
  } else if (mb >= 1) {
    const songs = Math.round(mb / 4)
    const photos = Math.round(mb / 3)
    return `Bu hajmga taxminan ${songs} ta MP3 musiqa yoki ${photos} ta telefon fotosurati sig'adi.`
  } else {
    const pages = Math.round(kb / 2)
    return `Bu hajmga taxminan ${pages || 1} sahifalik to'liq matnli hujjat sig'adi.`
  }
})

// ==========================================
// 4. BLOK-SXEMA VA ALGORITMLAR (FLOWCHART)
// ==========================================
interface FlowStep {
  id: number
  type: 'start' | 'process' | 'decision' | 'output' | 'end'
  text: string
  detail: string
  code: string
}

const algorithmMode = ref<'linear' | 'branch' | 'loop'>('branch')
const currentStepIndex = ref<number>(0)
const algoVariables = ref<Record<string, any>>({ son: 7, natija: '' })

const ALGORITHMS: Record<string, { title: string; desc: string; steps: FlowStep[] }> = {
  linear: {
    title: '1. Chiziqli algoritm (Ketma-ketlik)',
    desc: 'Barcha qadamlar hech qanday shartsiz, ketma-ket bir martadan bajariladi.',
    steps: [
      { id: 1, type: 'start', text: 'Boshlanish', detail: 'Dastur ishga tushirildi.', code: '# Dastur start' },
      { id: 2, type: 'process', text: 'a = 15, b = 25', detail: 'O\'zgaruvchilarga qiymat yuklandi.', code: 'a = 15\nb = 25' },
      { id: 3, type: 'process', text: 'yigindi = a + b', detail: 'Amal bajarildi: 15 + 25 = 40', code: 'yigindi = a + b' },
      { id: 4, type: 'output', text: 'Chiqarish: yigindi', detail: 'Ekranga 40 soni chiqarildi.', code: 'print("Yig\'indi:", yigindi)' },
      { id: 5, type: 'end', text: 'Tamom', detail: 'Algoritm muvaffaqiyatli yakunlandi.', code: '# Dastur tugadi' }
    ]
  },
  branch: {
    title: '2. Tarmoqlanuvchi algoritm (Shart if/else)',
    desc: 'Shart tekshiriladi: to\'g\'ri bo\'lsa bir yo\'ldan, noto\'g\'ri bo\'lsa boshqa yo\'ldan ketadi.',
    steps: [
      { id: 1, type: 'start', text: 'Boshlanish', detail: 'Son tekshirish boshlandi.', code: 'son = 7' },
      { id: 2, type: 'decision', text: 'son % 2 == 0 ?', detail: '7 ni 2 ga bo\'lgandagi qoldiq 0 ga tengmi? (Yo\'q: 1 == 0 yolg\'on)', code: 'if son % 2 == 0:' },
      { id: 3, type: 'process', text: 'natija = "Toq son"', detail: 'Shart bajarilmadi, else bloki ishladi.', code: 'else:\n    natija = "Toq son"' },
      { id: 4, type: 'output', text: 'Chiqarish: "Toq son"', detail: 'Ekranga "Toq son" javobi chiqdi.', code: 'print(natija)' },
      { id: 5, type: 'end', text: 'Tamom', detail: 'Algoritm yakunlandi.', code: '# Finish' }
    ]
  },
  loop: {
    title: '3. Takrorlanuvchi algoritm (Sikl / While loop)',
    desc: 'Berilgan shart bajarilguncha ma\'lum bir amallar qayta-qayta takrorlanadi.',
    steps: [
      { id: 1, type: 'start', text: 'Boshlanish (i = 1, sum = 0)', detail: 'Boshlang\'ich hisoblagichlar o\'rnatildi.', code: 'i = 1\nsum = 0' },
      { id: 2, type: 'decision', text: 'i <= 3 ?', detail: 'Hozir i = 1 (1 <= 3 rost, sikl davom etadi)', code: 'while i <= 3:' },
      { id: 3, type: 'process', text: 'sum += i, i += 1', detail: 'sum = 1, i endi 2 bo\'ldi.', code: '    sum += i\n    i += 1' },
      { id: 4, type: 'output', text: 'Chiqarish: sum (6)', detail: 'Jami yig\'indi 1+2+3 = 6 chiqarildi.', code: 'print("Jami:", sum)' },
      { id: 5, type: 'end', text: 'Tamom', detail: 'Sikl to\'xtadi va yakunlandi.', code: '# Loop finish' }
    ]
  }
}

const currentAlgorithm = computed(() => ALGORITHMS[algorithmMode.value])
const currentFlowStep = computed(() => currentAlgorithm.value.steps[currentStepIndex.value] || currentAlgorithm.value.steps[0])

const nextAlgoStep = () => {
  if (currentStepIndex.value < currentAlgorithm.value.steps.length - 1) {
    currentStepIndex.value++
  } else {
    currentStepIndex.value = 0
  }
}

const resetAlgo = () => {
  currentStepIndex.value = 0
}

// ==========================================
// 5. KOMPYUTER ANATOMIYASI (HARDWARE)
// ==========================================
const selectedPart = ref<string>('cpu')

const HARDWARE_PARTS: Record<string, {
  name: string
  badge: string
  icon: string
  analogy: string
  role: string
  unit: string
  example: string
}> = {
  cpu: {
    name: 'CPU (Markaziy Protsessor)',
    badge: 'Kompyuterning "Miyasi"',
    icon: 'cpu',
    analogy: 'Oshpaz (Barcha hisob-kitoblar va buyruqlarni birma-bir tezda bajaradi)',
    role: 'Dasturlar yozilgan buyruqlarni milliardlab marta soniyasiga hisoblaydi, mantiqiy va arifmetik amallarni boshqaradi.',
    unit: 'Gigagerts (GHz) — soniyasiga milliardlab taktlar, hamda Yadrolar soni (Masalan: 8 yadro 3.8 GHz).',
    example: 'Intel Core i7, AMD Ryzen 7, Apple M3.'
  },
  ram: {
    name: 'RAM (Tezkor Xotira)',
    badge: 'Vaqtinchalik ish maydoni',
    icon: 'memory-stick',
    analogy: 'Oshpazning ish stoli (Hozir ishlayotgan mahsulotlar stol ustida turadi, tok o\'chsa stol tozalanadi)',
    role: 'Hozirda ochiq turgan dasturlar, o\'yinlar va brauzer yorliqlari ma\'lumotlarini o\'ta tezkor o\'qish va yozish uchun saqlaydi.',
    unit: 'Gigabayt (GB) va Megagerts (MHz) — Masalan: 16 GB DDR5 5600 MHz.',
    example: '8 GB, 16 GB, 32 GB DDR4/DDR5.'
  },
  storage: {
    name: 'SSD / HDD (Doimiy Xotira)',
    badge: 'Uzoq muddatli omborxona',
    icon: 'hard-drive',
    analogy: 'Muzlatgich yoki javon (Barcha fayllar, rasmlar va dasturlar saqlanadi, tok o\'chsa ham o\'chmaydi)',
    role: 'Operatsion tizim (Windows/Linux/macOS), fayllar, o\'yinlar va kodlarni kompyuter o\'chganda ham o\'chmasdan doimiy saqlash.',
    unit: 'Gigabayt (GB) va Terabayt (TB) — Masalan: 512 GB yoki 1 TB NVMe SSD.',
    example: 'Kingston NVMe SSD, Samsung 990 Pro.'
  },
  gpu: {
    name: 'GPU (Videokarta)',
    badge: 'Grafika va Vizual hisob-kitoblar',
    icon: 'circuit-board',
    analogy: 'Rassomlar jamoasi (Millionlab piksellarni bir vaqtda parallel chizib beradi)',
    role: 'Ekrandagi 3D grafika, o\'yinlar, video montaj va sun\'iy intellekt (AI) modellarining parallel hisob-kitoblarini tezlashtiradi.',
    unit: 'VRAM (GB) va CUDA/Stream yadrolar soni — Masalan: 8 GB GDDR6.',
    example: 'NVIDIA RTX 4060, AMD Radeon RX 7600.'
  },
  motherboard: {
    name: 'Ona plata (Motherboard)',
    badge: 'Magistral yo\'l va asab tizimi',
    icon: 'circuit-board',
    analogy: 'Shahar yo\'llari tarmog\'i (Barcha qismlarni bir-biri bilan bog\'laydi)',
    role: 'Protsessor, xotira, videokarta va boshqa barcha qurilmalarni elektr quvvati va yuqori tezlikdagi ma\'lumot shinalari bilan tutashtiradi.',
    unit: 'Chipset va Soket turi — Masalan: B650 chipset, AM5 soket.',
    example: 'ASUS ROG, MSI Tomahawk, Gigabyte AORUS.'
  }
}

const currentHardware = computed(() => HARDWARE_PARTS[selectedPart.value] || HARDWARE_PARTS.cpu)

onMounted(() => {
  generateNewGameTarget()
})
</script>

<template>
  <div class="axv foundation-container">
    <Crumbs :items="[{ t: 'Bosh sahifa', l: '/' }, { t: 'CS Laboratoriya (Foundation)' }]" />

    <!-- HERO SECTION -->
    <header class="foundation-hero">
      <div class="fh-left">
        <span class="fh-badge"><Icon name="binary" /> Computer Science Foundation</span>
        <h1>CS Laboratoriya</h1>
        <p class="fh-sub">
          Dasturlash va kompyuter fanlarining fundamental tushunchalarini interaktiv, vizual va sodda tarzda o'rganing.
        </p>
      </div>

      <!-- TAB NAVIGATION -->
      <nav class="foundation-tabs" aria-label="Laboratoriya bo'limlari">
        <button
          class="f-tab"
          :class="{ active: activeTab === 'binary' }"
          @click="activeTab = 'binary'"
        >
          <Icon name="binary" /> Ikkilik sanoq
        </button>
        <button
          class="f-tab"
          :class="{ active: activeTab === 'logic' }"
          @click="activeTab = 'logic'"
        >
          <Icon name="zap" /> Mantiqiy elementlar
        </button>
        <button
          class="f-tab"
          :class="{ active: activeTab === 'memory' }"
          @click="activeTab = 'memory'"
        >
          <Icon name="hard-drive" /> Axborot hajmi
        </button>
        <button
          class="f-tab"
          :class="{ active: activeTab === 'flowchart' }"
          @click="activeTab = 'flowchart'"
        >
          <Icon name="git-branch" /> Blok-sxemalar
        </button>
        <button
          class="f-tab"
          :class="{ active: activeTab === 'hardware' }"
          @click="activeTab = 'hardware'"
        >
          <Icon name="cpu" /> Qurilmalar (Hardware)
        </button>
      </nav>
    </header>

    <!-- ========================================== -->
    <!-- TAB 1: IKKILIK SANOQ TIZIMI VA BITLAR     -->
    <!-- ========================================== -->
    <section v-if="activeTab === 'binary'" class="lab-card">
      <div class="card-head">
        <div>
          <h2><Icon name="binary" /> 8-bitli Ikkilik sanoq tizimi trenajyori</h2>
          <p>Har bir bit (0 yoki 1) ning qiymatini ko'rish uchun kalitlarni yoqing yoki o'chiring.</p>
        </div>
        <button class="btn btn-ghost btn-sm" @click="resetBits">
          <Icon name="rotate-ccw" /> Tozalash (0)
        </button>
      </div>

      <!-- 8-Bit Interactive Board -->
      <div class="bit-board">
        <div
          v-for="(val, idx) in bitValues"
          :key="val"
          class="bit-col"
          :class="{ 'bit-active': bits[idx] === 1 }"
          @click="toggleBit(idx)"
        >
          <div class="bit-weight">2<sup>{{ 7 - idx }}</sup></div>
          <div class="bit-val-label">{{ val }}</div>
          <div class="bit-switch">
            <span class="bit-state">{{ bits[idx] }}</span>
          </div>
          <div class="bit-led" :class="{ on: bits[idx] === 1 }"></div>
        </div>
      </div>

      <!-- Conversion Live Displays -->
      <div class="conv-grid">
        <div class="conv-box highlight">
          <span class="cb-lbl">O'nlik (10-lik) son</span>
          <span class="cb-val">{{ decimalValue }}</span>
          <span class="cb-sub">{{ bits.map((b, i) => b ? bitValues[i] : null).filter(Boolean).join(' + ') || '0' }}</span>
        </div>
        <div class="conv-box">
          <span class="cb-lbl">Ikkilik (2-lik) kod</span>
          <span class="cb-val font-mono">{{ binaryString }}</span>
          <span class="cb-sub">8 ta bit (1 bayt)</span>
        </div>
        <div class="conv-box">
          <span class="cb-lbl">O'n oltilik (16-lik Hex)</span>
          <span class="cb-val font-mono">{{ hexValue }}</span>
          <span class="cb-sub">0x00 dan 0xFF gacha</span>
        </div>
        <div class="conv-box">
          <span class="cb-lbl">ASCII belgisi</span>
          <span class="cb-val font-mono">{{ asciiChar }}</span>
          <span class="cb-sub">Kod: {{ decimalValue }}</span>
        </div>
      </div>

      <!-- Mini-Game: Binary Challenge -->
      <div class="game-panel">
        <div class="gp-header">
          <div>
            <h3><Icon name="sparkles" /> Ikkilik chaqiriq: Sonni yig'ing!</h3>
            <p>Quyidagi sonni bitlar yordamida hosil qiling:</p>
          </div>
          <div class="gp-stats">
            <span class="gp-score">Ball: <b>{{ gameScore }}</b></span>
            <span class="gp-streak" v-if="gameStreak > 1">🔥 {{ gameStreak }}x</span>
          </div>
        </div>

        <div class="gp-target-row">
          <div class="gp-target-num">{{ gameTarget }}</div>
          <button class="btn btn-primary btn-lg" @click="checkGameAnswer">
            <Icon name="check" /> Tekshirish
          </button>
          <button class="btn btn-ghost btn-sm" @click="generateNewGameTarget">
            Boshqa son
          </button>
        </div>

        <div v-if="gameFeedback === 'success'" class="feedback-msg success">
          🎉 Ajoyib! To'g'ri topdingiz! Yangi son yuklanmoqda...
        </div>
        <div v-else-if="gameFeedback === 'error'" class="feedback-msg error">
          ❌ Hozirgi yig'indi: {{ decimalValue }}. Yana urinib ko'ring! (Kerakli: {{ gameTarget }})
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- TAB 2: MANTIQIY ELEMENTLAR (LOGIC GATES)  -->
    <!-- ========================================== -->
    <section v-else-if="activeTab === 'logic'" class="lab-card">
      <div class="card-head">
        <div>
          <h2><Icon name="zap" /> Mantiqiy elementlar (Logic Gates) simulyatori</h2>
          <p>Mantiqiy amallar kompyuter chipining asosi hisoblanadi. Elementni tanlang va signallarni tekshiring.</p>
        </div>
      </div>

      <!-- Gate Selector Tabs -->
      <div class="gate-selector">
        <button
          v-for="g in ['AND', 'OR', 'NOT', 'XOR', 'NAND', 'NOR'] as const"
          :key="g"
          class="gate-tab"
          :class="{ active: gateType === g }"
          @click="gateType = g"
        >
          {{ g }}
        </button>
      </div>

      <!-- Interactive Circuit View -->
      <div class="circuit-view">
        <!-- Input Switches -->
        <div class="circuit-inputs">
          <div class="circ-switch-group">
            <span class="cs-label">Kirish A:</span>
            <button
              class="switch-btn"
              :class="{ on: inputA === 1 }"
              @click="inputA = inputA === 1 ? 0 : 1"
            >
              {{ inputA }}
            </button>
          </div>

          <div v-if="gateType !== 'NOT'" class="circ-switch-group">
            <span class="cs-label">Kirish B:</span>
            <button
              class="switch-btn"
              :class="{ on: inputB === 1 }"
              @click="inputB = inputB === 1 ? 0 : 1"
            >
              {{ inputB }}
            </button>
          </div>
        </div>

        <!-- Gate Chip Representation -->
        <div class="circuit-gate-box">
          <div class="gate-name-badge">{{ gateType }}</div>
          <div class="gate-symbol">{{ gateExplanations[gateType].formula }}</div>
        </div>

        <!-- Output Bulb -->
        <div class="circuit-output">
          <span class="cs-label">Chiqish:</span>
          <div class="output-lamp" :class="{ 'lamp-on': gateOutput === 1 }">
            <Icon name="lightbulb" />
            <span class="lamp-val">{{ gateOutput }}</span>
          </div>
        </div>
      </div>

      <!-- Explanation & Truth Table Row -->
      <div class="gate-details-row">
        <!-- Left: Rule explanation -->
        <div class="g-info-card">
          <h3>Qoida va Tavsif</h3>
          <p>{{ gateExplanations[gateType].desc }}</p>
          <div class="code-preview">
            <code>{{ gateExplanations[gateType].code }}</code>
          </div>
        </div>

        <!-- Right: Truth Table -->
        <div class="g-table-card">
          <h3>Haqiqiylik jadvali (Truth Table)</h3>
          <table class="truth-table">
            <thead>
              <tr>
                <th>A</th>
                <th v-if="gateType !== 'NOT'">B</th>
                <th>Chiqish</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="r in truthTableRows"
                :key="`${r.a}-${r.b}`"
                :class="{ 'row-active': r.a === inputA && (gateType === 'NOT' || r.b === inputB) }"
              >
                <td>{{ r.a }}</td>
                <td v-if="gateType !== 'NOT'">{{ r.b }}</td>
                <td :class="{ 'out-one': r.out === 1 }">{{ r.out }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- TAB 3: AXBOROT HAJMI VA XOTIRA (MEMORY)   -->
    <!-- ========================================== -->
    <section v-else-if="activeTab === 'memory'" class="lab-card">
      <div class="card-head">
        <div>
          <h2><Icon name="hard-drive" /> Axborot o'lchov birliklari kalkulyatori</h2>
          <p>Bitdan Terabaytgacha: axborot qanday o'lchanishini va o'zaro nisbatlarini hisoblang.</p>
        </div>
      </div>

      <!-- Interactive Calculator Inputs -->
      <div class="mem-calc-bar">
        <div class="mcb-input-group">
          <label>Miqdor:</label>
          <input
            type="number"
            v-model.number="inputDataValue"
            min="1"
            class="mem-num-input"
          />
        </div>
        <div class="mcb-input-group">
          <label>Birlik:</label>
          <select v-model="inputDataUnit" class="mem-select">
            <option value="Bit">Bit</option>
            <option value="Bayt">Bayt (B)</option>
            <option value="KB">Kilobayt (KB)</option>
            <option value="MB">Megabayt (MB)</option>
            <option value="GB">Gigabayt (GB)</option>
            <option value="TB">Terabayt (TB)</option>
          </select>
        </div>
      </div>

      <!-- Converted Matrix -->
      <div class="mem-matrix">
        <div class="mem-card">
          <span class="mc-lbl">Bit (b)</span>
          <span class="mc-val">{{ convertedValues.bits }}</span>
          <span class="mc-hint">0 yoki 1</span>
        </div>
        <div class="mem-card">
          <span class="mc-lbl">Bayt (B)</span>
          <span class="mc-val">{{ convertedValues.bytes }}</span>
          <span class="mc-hint">8 bit</span>
        </div>
        <div class="mem-card">
          <span class="mc-lbl">Kilobayt (KB)</span>
          <span class="mc-val">{{ convertedValues.kb }}</span>
          <span class="mc-hint">1024 bayt</span>
        </div>
        <div class="mem-card">
          <span class="mc-lbl">Megabayt (MB)</span>
          <span class="mc-val">{{ convertedValues.mb }}</span>
          <span class="mc-hint">1024 KB</span>
        </div>
        <div class="mem-card">
          <span class="mc-lbl">Gigabayt (GB)</span>
          <span class="mc-val">{{ convertedValues.gb }}</span>
          <span class="mc-hint">1024 MB</span>
        </div>
        <div class="mem-card">
          <span class="mc-lbl">Terabayt (TB)</span>
          <span class="mc-val">{{ convertedValues.tb }}</span>
          <span class="mc-hint">1024 GB</span>
        </div>
      </div>

      <!-- Real world Analogy Card -->
      <div class="analogy-box">
        <span class="ab-icon"><Icon name="sparkles" /></span>
        <div class="ab-content">
          <h4>Amaliy hayotdagi hajmi:</h4>
          <p>{{ realWorldAnalogy }}</p>
        </div>
      </div>

      <!-- Memory Ladder Hierarchy -->
      <div class="ladder-section">
        <h3>Axborot zinapoyasi (Ierarxiya)</h3>
        <div class="ladder-grid">
          <div class="ladder-step">
            <span class="ls-badge">1 Bit</span>
            <p>1 ta tranzistor holati (0 yoki 1)</p>
          </div>
          <div class="ladder-arrow">➔</div>
          <div class="ladder-step">
            <span class="ls-badge">1 Bayt</span>
            <p>8 bit (1 ta harf yoki belgi, masalan 'A')</p>
          </div>
          <div class="ladder-arrow">➔</div>
          <div class="ladder-step">
            <span class="ls-badge">1 KB</span>
            <p>1024 bayt (1 bet matnli hujjat)</p>
          </div>
          <div class="ladder-arrow">➔</div>
          <div class="ladder-step">
            <span class="ls-badge">1 MB</span>
            <p>1024 KB (1 ta sifatli rasm yoki qo'shiq)</p>
          </div>
          <div class="ladder-arrow">➔</div>
          <div class="ladder-step">
            <span class="ls-badge">1 GB</span>
            <p>1024 MB (1 ta to'liq film yoki 1000 kitob)</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- TAB 4: BLOK-SXEMA VA ALGORITMLAR          -->
    <!-- ========================================== -->
    <section v-else-if="activeTab === 'flowchart'" class="lab-card">
      <div class="card-head">
        <div>
          <h2><Icon name="git-branch" /> Algoritmlar va Blok-sxemalar vizualizatori</h2>
          <p>Algoritm turini tanlang va "Keyingi qadam" orqali qanday ishlashini bosqichma-bosqich kuzating.</p>
        </div>
        <div class="flow-controls">
          <button class="btn btn-primary" @click="nextAlgoStep">
            <Icon name="play" /> Keyingi qadam ({{ currentStepIndex + 1 }}/{{ currentAlgorithm.steps.length }})
          </button>
          <button class="btn btn-ghost btn-sm" @click="resetAlgo">
            <Icon name="rotate-ccw" /> Boshiga
          </button>
        </div>
      </div>

      <!-- Algorithm Type Tabs -->
      <div class="gate-selector">
        <button
          class="gate-tab"
          :class="{ active: algorithmMode === 'linear' }"
          @click="algorithmMode = 'linear'; resetAlgo()"
        >
          Chiziqli algoritm
        </button>
        <button
          class="gate-tab"
          :class="{ active: algorithmMode === 'branch' }"
          @click="algorithmMode = 'branch'; resetAlgo()"
        >
          Tarmoqlanuvchi (if/else)
        </button>
        <button
          class="gate-tab"
          :class="{ active: algorithmMode === 'loop' }"
          @click="algorithmMode = 'loop'; resetAlgo()"
        >
          Takrorlanuvchi (Sikl / Loop)
        </button>
      </div>

      <!-- Interactive Flowchart Diagram -->
      <div class="flowchart-visual">
        <div
          v-for="(st, idx) in currentAlgorithm.steps"
          :key="st.id"
          class="flow-node"
          :class="[
            `node-${st.type}`,
            { 'node-active': idx === currentStepIndex },
            { 'node-passed': idx < currentStepIndex }
          ]"
        >
          <div class="fn-type-badge">{{ st.type.toUpperCase() }}</div>
          <div class="fn-text">{{ st.text }}</div>
          <div v-if="idx < currentAlgorithm.steps.length - 1" class="fn-connector">
            <span class="fn-arrow-down">↓</span>
          </div>
        </div>
      </div>

      <!-- Current Step Live Explanation -->
      <div class="step-live-card">
        <div class="slc-info">
          <h4>Qadam {{ currentStepIndex + 1 }}: {{ currentFlowStep.text }}</h4>
          <p>{{ currentFlowStep.detail }}</p>
        </div>
        <div class="slc-code">
          <span class="code-label">Python kodi:</span>
          <code>{{ currentFlowStep.code }}</code>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- TAB 5: KOMPYUTER ANATOMIYASI (HARDWARE)   -->
    <!-- ========================================== -->
    <section v-else-if="activeTab === 'hardware'" class="lab-card">
      <div class="card-head">
        <div>
          <h2><Icon name="cpu" /> Kompyuter Anatomiyasi (Hardware)</h2>
          <p>Kompyuterning asosiy qismlari qanday ishlashini va bir-biri bilan qanday bog'langanini ko'ring.</p>
        </div>
      </div>

      <!-- Interactive Component Selector -->
      <div class="hw-selector-grid">
        <button
          v-for="(part, key) in HARDWARE_PARTS"
          :key="key"
          class="hw-nav-card"
          :class="{ active: selectedPart === key }"
          @click="selectedPart = key as string"
        >
          <span class="hwn-icon"><Icon :name="part.icon" /></span>
          <span class="hwn-title">{{ part.name.split(' ')[0] }}</span>
          <span class="hwn-sub">{{ part.badge }}</span>
        </button>
      </div>

      <!-- Detailed Hardware View -->
      <div class="hw-detail-card">
        <div class="hwd-header">
          <div class="hwd-title-box">
            <span class="hwd-badge">{{ currentHardware.badge }}</span>
            <h3>{{ currentHardware.name }}</h3>
          </div>
          <div class="hwd-unit">
            <span class="hu-lbl">O'lchov birligi:</span>
            <b>{{ currentHardware.unit }}</b>
          </div>
        </div>

        <div class="hwd-body">
          <div class="hwd-block">
            <h4><Icon name="sparkles" /> Hayotiy o'xshatish:</h4>
            <p class="analogy-text">{{ currentHardware.analogy }}</p>
          </div>

          <div class="hwd-block">
            <h4><Icon name="info" /> Asosiy vazifasi:</h4>
            <p>{{ currentHardware.role }}</p>
          </div>

          <div class="hwd-block">
            <h4><Icon name="check" /> Haqiqiy misollar:</h4>
            <p class="font-mono text-brand">{{ currentHardware.example }}</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.foundation-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 8px 16px 32px;
}

/* HERO */
.foundation-hero {
  margin-bottom: 24px;
}

.fh-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.8rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 4px 12px;
  border-radius: 999px;
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
  margin-bottom: 8px;
}

.fh-left h1 {
  font-size: 2.1rem;
  font-weight: 800;
  margin: 0 0 8px;
  background: var(--ax-grad);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.fh-sub {
  color: var(--vp-c-text-2);
  margin: 0 0 20px;
  max-width: 700px;
  font-size: 1rem;
  line-height: 1.5;
}

/* TABS */
.foundation-tabs {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding-bottom: 6px;
}

.f-tab {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 18px;
  border-radius: 12px;
  font-size: 0.92rem;
  font-weight: 700;
  color: var(--vp-c-text-2);
  background: var(--ax-card);
  border: 1px solid var(--ax-line);
  cursor: pointer;
  transition: all 0.15s ease;
  white-space: nowrap;
}

.f-tab:hover {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-text-1);
}

.f-tab.active {
  background: var(--vp-c-brand-1);
  color: #fff;
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 4px 14px rgba(14, 112, 192, 0.35);
}

/* MAIN CARD */
.lab-card {
  background: var(--ax-card);
  border: 1px solid var(--ax-line);
  border-radius: 20px;
  padding: 24px;
  box-shadow: var(--ax-shadow);
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.card-head {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  flex-wrap: wrap;
  gap: 12px;
}

.card-head h2 {
  font-size: 1.4rem;
  font-weight: 800;
  margin: 0 0 4px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.card-head p {
  color: var(--vp-c-text-2);
  margin: 0;
  font-size: 0.95rem;
}

/* TAB 1: BIT BOARD */
.bit-board {
  display: grid;
  grid-template-columns: repeat(8, 1fr);
  gap: 10px;
  background: var(--vp-c-bg);
  border: 1px solid var(--ax-line);
  border-radius: 16px;
  padding: 18px 12px;
}

.bit-col {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  background: var(--ax-card);
  border: 1px solid var(--ax-line);
  border-radius: 12px;
  padding: 12px 6px;
  cursor: pointer;
  user-select: none;
  transition: all 0.15s ease;
}

.bit-col:hover {
  border-color: var(--vp-c-brand-1);
  transform: translateY(-2px);
}

.bit-col.bit-active {
  background: var(--vp-c-brand-soft);
  border-color: var(--vp-c-brand-1);
}

.bit-weight {
  font-size: 0.75rem;
  color: var(--vp-c-text-2);
}

.bit-val-label {
  font-size: 1.1rem;
  font-weight: 800;
  color: var(--vp-c-text-1);
}

.bit-switch {
  width: 44px;
  height: 44px;
  border-radius: 10px;
  background: var(--vp-c-bg-alt);
  border: 2px solid var(--ax-line);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.4rem;
  font-weight: 800;
  color: var(--vp-c-text-2);
  transition: all 0.15s ease;
}

.bit-active .bit-switch {
  background: var(--vp-c-brand-1);
  color: #fff;
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 0 12px rgba(14, 112, 192, 0.5);
}

.bit-led {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #454545;
  transition: all 0.15s ease;
}

.bit-led.on {
  background: var(--ax-good);
  box-shadow: 0 0 8px var(--ax-good);
}

/* CONVERSION GRID */
.conv-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
}

.conv-box {
  background: var(--vp-c-bg);
  border: 1px solid var(--ax-line);
  border-radius: 14px;
  padding: 16px;
  display: flex;
  flex-direction: column;
}

.conv-box.highlight {
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
}

.cb-lbl {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--vp-c-text-2);
  margin-bottom: 4px;
}

.cb-val {
  font-size: 1.8rem;
  font-weight: 800;
  color: var(--vp-c-text-1);
}

.cb-sub {
  font-size: 0.8rem;
  color: var(--vp-c-text-2);
  margin-top: 4px;
}

/* MINI-GAME */
.game-panel {
  background: var(--vp-c-bg-alt);
  border: 1px solid var(--ax-line);
  border-radius: 16px;
  padding: 20px;
}

.gp-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 14px;
}

.gp-header h3 {
  font-size: 1.15rem;
  font-weight: 700;
  margin: 0 0 4px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.gp-header p {
  color: var(--vp-c-text-2);
  margin: 0;
  font-size: 0.9rem;
}

.gp-stats {
  display: flex;
  align-items: center;
  gap: 10px;
}

.gp-score {
  background: var(--ax-card);
  padding: 4px 12px;
  border-radius: 8px;
  border: 1px solid var(--ax-line);
  font-size: 0.9rem;
}

.gp-streak {
  font-size: 1.1rem;
}

.gp-target-row {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 12px;
}

.gp-target-num {
  font-size: 2.8rem;
  font-weight: 900;
  color: var(--vp-c-brand-1);
  min-width: 100px;
}

.feedback-msg {
  padding: 10px 16px;
  border-radius: 10px;
  font-size: 0.95rem;
  font-weight: 600;
}

.feedback-msg.success {
  background: rgba(46, 125, 50, 0.15);
  color: var(--ax-good);
  border: 1px solid var(--ax-good);
}

.feedback-msg.error {
  background: rgba(224, 108, 117, 0.15);
  color: #e06c75;
  border: 1px solid #e06c75;
}

/* TAB 2: LOGIC GATES */
.gate-selector {
  display: flex;
  gap: 8px;
  overflow-x: auto;
}

.gate-tab {
  padding: 8px 20px;
  border-radius: 10px;
  font-size: 0.95rem;
  font-weight: 700;
  background: var(--vp-c-bg);
  border: 1px solid var(--ax-line);
  color: var(--vp-c-text-2);
  cursor: pointer;
  transition: all 0.15s ease;
}

.gate-tab.active {
  background: var(--vp-c-brand-1);
  color: #fff;
  border-color: var(--vp-c-brand-1);
}

.circuit-view {
  display: flex;
  align-items: center;
  justify-content: space-around;
  background: var(--vp-c-bg);
  border: 1px solid var(--ax-line);
  border-radius: 18px;
  padding: 32px 20px;
  flex-wrap: wrap;
  gap: 20px;
}

.circuit-inputs {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.circ-switch-group {
  display: flex;
  align-items: center;
  gap: 12px;
}

.cs-label {
  font-weight: 700;
  font-size: 0.95rem;
  min-width: 70px;
}

.switch-btn {
  width: 54px;
  height: 54px;
  border-radius: 12px;
  background: var(--ax-card);
  border: 2px solid var(--ax-line);
  font-size: 1.6rem;
  font-weight: 900;
  color: var(--vp-c-text-2);
  cursor: pointer;
  transition: all 0.15s ease;
}

.switch-btn.on {
  background: var(--ax-good);
  color: #fff;
  border-color: var(--ax-good);
  box-shadow: 0 0 14px rgba(46, 125, 50, 0.5);
}

.circuit-gate-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 140px;
  height: 100px;
  background: linear-gradient(135deg, #0e70c0, #2392dc);
  border-radius: 16px;
  color: #fff;
  box-shadow: 0 8px 20px rgba(14, 112, 192, 0.35);
}

.gate-name-badge {
  font-size: 1.4rem;
  font-weight: 900;
  letter-spacing: 0.05em;
}

.gate-symbol {
  font-size: 0.9rem;
  opacity: 0.85;
}

.circuit-output {
  display: flex;
  align-items: center;
  gap: 14px;
}

.output-lamp {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  width: 90px;
  height: 54px;
  border-radius: 14px;
  background: var(--ax-card);
  border: 2px solid var(--ax-line);
  font-size: 1.3rem;
  color: var(--vp-c-text-3);
  transition: all 0.2s ease;
}

.output-lamp.lamp-on {
  background: rgba(229, 192, 123, 0.2);
  color: #e5c07b;
  border-color: #e5c07b;
  box-shadow: 0 0 20px rgba(229, 192, 123, 0.6);
}

.lamp-val {
  font-weight: 900;
  font-size: 1.4rem;
}

.gate-details-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.g-info-card, .g-table-card {
  background: var(--vp-c-bg);
  border: 1px solid var(--ax-line);
  border-radius: 16px;
  padding: 20px;
}

.g-info-card h3, .g-table-card h3 {
  font-size: 1.1rem;
  font-weight: 700;
  margin: 0 0 10px;
}

.code-preview {
  margin-top: 12px;
  background: var(--vp-c-bg-alt);
  padding: 10px 14px;
  border-radius: 8px;
  border: 1px solid var(--ax-line);
  font-family: monospace;
}

.truth-table {
  width: 100%;
  border-collapse: collapse;
  text-align: center;
  font-size: 0.95rem;
}

.truth-table th {
  background: var(--ax-card);
  padding: 8px;
  border-bottom: 2px solid var(--ax-line);
}

.truth-table td {
  padding: 8px;
  border-bottom: 1px solid var(--ax-line);
  font-weight: 600;
}

.truth-table tr.row-active {
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
}

.out-one {
  color: var(--ax-good);
  font-weight: 800;
}

/* TAB 3: MEMORY */
.mem-calc-bar {
  display: flex;
  gap: 16px;
  background: var(--vp-c-bg);
  border: 1px solid var(--ax-line);
  border-radius: 14px;
  padding: 16px 20px;
  align-items: center;
}

.mcb-input-group {
  display: flex;
  align-items: center;
  gap: 10px;
}

.mem-num-input {
  padding: 8px 14px;
  border-radius: 8px;
  border: 1px solid var(--ax-line);
  background: var(--ax-card);
  color: var(--vp-c-text-1);
  font-size: 1.1rem;
  font-weight: 700;
  width: 140px;
}

.mem-select {
  padding: 8px 14px;
  border-radius: 8px;
  border: 1px solid var(--ax-line);
  background: var(--ax-card);
  color: var(--vp-c-text-1);
  font-size: 1rem;
  font-weight: 600;
}

.mem-matrix {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
}

.mem-card {
  background: var(--vp-c-bg);
  border: 1px solid var(--ax-line);
  border-radius: 14px;
  padding: 16px;
  display: flex;
  flex-direction: column;
}

.mc-lbl {
  font-size: 0.75rem;
  text-transform: uppercase;
  color: var(--vp-c-text-2);
  margin-bottom: 4px;
}

.mc-val {
  font-size: 1.4rem;
  font-weight: 800;
  color: var(--vp-c-text-1);
  word-break: break-all;
}

.mc-hint {
  font-size: 0.8rem;
  color: var(--vp-c-brand-1);
  margin-top: 4px;
}

.analogy-box {
  display: flex;
  align-items: center;
  gap: 16px;
  background: var(--vp-c-brand-soft);
  border: 1px solid var(--vp-c-brand-1);
  border-radius: 14px;
  padding: 16px 20px;
}

.ab-icon {
  font-size: 1.8rem;
  color: var(--vp-c-brand-1);
}

.ab-content h4 {
  margin: 0 0 4px;
  font-weight: 800;
}

.ab-content p {
  margin: 0;
  font-size: 0.95rem;
  color: var(--vp-c-text-1);
}

.ladder-section h3 {
  font-size: 1.15rem;
  font-weight: 700;
  margin: 0 0 12px;
}

.ladder-grid {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--vp-c-bg);
  border: 1px solid var(--ax-line);
  border-radius: 16px;
  padding: 18px;
  overflow-x: auto;
  gap: 10px;
}

.ladder-step {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  min-width: 140px;
}

.ls-badge {
  background: var(--ax-card-hi);
  border: 1px solid var(--ax-line);
  padding: 4px 12px;
  border-radius: 8px;
  font-weight: 800;
  color: var(--vp-c-brand-1);
  margin-bottom: 6px;
}

.ladder-step p {
  font-size: 0.78rem;
  color: var(--vp-c-text-2);
  margin: 0;
}

.ladder-arrow {
  color: var(--vp-c-text-3);
  font-size: 1.2rem;
}

/* TAB 4: FLOWCHART */
.flowchart-visual {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  background: var(--vp-c-bg);
  border: 1px solid var(--ax-line);
  border-radius: 18px;
  padding: 28px;
}

.flow-node {
  position: relative;
  min-width: 260px;
  padding: 12px 20px;
  text-align: center;
  border: 2px solid var(--ax-line);
  background: var(--ax-card);
  transition: all 0.2s ease;
}

.node-start, .node-end {
  border-radius: 999px;
}

.node-process {
  border-radius: 8px;
}

.node-decision {
  border-radius: 6px;
  transform: rotate(0deg);
  border-color: #d19a66;
}

.node-output {
  border-radius: 12px;
  transform: skewX(-10deg);
}

.node-active {
  background: var(--vp-c-brand-soft) !important;
  border-color: var(--vp-c-brand-1) !important;
  box-shadow: 0 0 16px rgba(14, 112, 192, 0.5);
  transform: scale(1.05);
}

.node-passed {
  opacity: 0.6;
}

.fn-type-badge {
  font-size: 0.65rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  color: var(--vp-c-text-3);
  margin-bottom: 2px;
}

.fn-text {
  font-size: 0.95rem;
  font-weight: 700;
}

.fn-connector {
  position: absolute;
  bottom: -20px;
  left: 50%;
  transform: translateX(-50%);
  color: var(--vp-c-text-3);
  font-size: 1rem;
}

.step-live-card {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: var(--vp-c-bg-alt);
  border: 1px solid var(--ax-line);
  border-radius: 14px;
  padding: 16px 20px;
  gap: 16px;
  flex-wrap: wrap;
}

.slc-info h4 {
  margin: 0 0 4px;
  font-size: 1.05rem;
  font-weight: 800;
}

.slc-info p {
  margin: 0;
  font-size: 0.92rem;
  color: var(--vp-c-text-2);
}

.slc-code {
  display: flex;
  flex-direction: column;
  background: var(--vp-c-bg);
  padding: 8px 14px;
  border-radius: 8px;
  border: 1px solid var(--ax-line);
  font-family: monospace;
}

.code-label {
  font-size: 0.7rem;
  color: var(--vp-c-text-3);
  text-transform: uppercase;
}

/* TAB 5: HARDWARE */
.hw-selector-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 10px;
}

.hw-nav-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  background: var(--vp-c-bg);
  border: 1px solid var(--ax-line);
  border-radius: 14px;
  padding: 14px 10px;
  cursor: pointer;
  transition: all 0.15s ease;
}

.hw-nav-card:hover {
  border-color: var(--vp-c-brand-1);
}

.hw-nav-card.active {
  background: var(--vp-c-brand-soft);
  border-color: var(--vp-c-brand-1);
}

.hwn-icon {
  font-size: 1.6rem;
  color: var(--vp-c-brand-1);
  margin-bottom: 6px;
}

.hwn-title {
  font-weight: 800;
  font-size: 0.95rem;
  color: var(--vp-c-text-1);
}

.hwn-sub {
  font-size: 0.75rem;
  color: var(--vp-c-text-2);
  margin-top: 2px;
}

.hw-detail-card {
  background: var(--vp-c-bg);
  border: 1px solid var(--ax-line);
  border-radius: 18px;
  padding: 24px;
}

.hwd-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  border-bottom: 1px solid var(--ax-line);
  padding-bottom: 16px;
  margin-bottom: 20px;
  flex-wrap: wrap;
  gap: 10px;
}

.hwd-badge {
  display: inline-block;
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
  padding: 2px 10px;
  border-radius: 6px;
  margin-bottom: 6px;
}

.hwd-title-box h3 {
  font-size: 1.4rem;
  font-weight: 800;
  margin: 0;
}

.hwd-unit {
  font-size: 0.9rem;
}

.hu-lbl {
  color: var(--vp-c-text-2);
  margin-right: 6px;
}

.hwd-body {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.hwd-block h4 {
  font-size: 0.95rem;
  font-weight: 700;
  margin: 0 0 4px;
  display: flex;
  align-items: center;
  gap: 6px;
}

.hwd-block p {
  margin: 0;
  font-size: 0.95rem;
  color: var(--vp-c-text-2);
  line-height: 1.5;
}

.analogy-text {
  color: var(--vp-c-text-1) !important;
  font-weight: 600;
}

@media (max-width: 768px) {
  .bit-board {
    grid-template-columns: repeat(4, 1fr);
  }
  .conv-grid, .mem-matrix, .gate-details-row {
    grid-template-columns: 1fr;
  }
  .hw-selector-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>
