<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'
import { withBase } from 'vitepress'
import Icon from './Icon.vue'
import Crumbs from './Crumbs.vue'

// --- Active Tab State ---
// 'binary' | 'logic' | 'memory' | 'flowchart' | 'hardware' | 'sorting' | 'crypto'
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
    desc: 'INKOR (NOT) — Kirish signalini teskarisiga o\'zgartiradi. 1 kirsa 0, 0 kirsa 1 chiqadi.',
    formula: '¬A (yoki NOT A)',
    code: 'not a # qiymatni teskarisiga o\'giradi'
  },
  XOR: {
    desc: 'ISTISNOLI YOKI (XOR) — Kirish signallari har xil bo\'lsagina 1 bo\'ladi. Ikkisi bir xil (0-0 yoki 1-1) bo\'lsa 0.',
    formula: 'A ⊕ B',
    code: 'if a != b: # faqat bittasi rost bo\'lishi kerak'
  },
  NAND: {
    desc: 'AND-NOT — AND natijasining teskarisi. Ikkala kirish 1 bo\'lgandagina 0 bo\'ladi, qolgan barcha holatda 1.',
    formula: '¬(A · B)',
    code: 'not (a and b)'
  },
  NOR: {
    desc: 'OR-NOT — OR natijasining teskarisi. Faqat ikkala kirish 0 bo\'lgandagina 1 bo\'ladi.',
    formula: '¬(A + B)',
    code: 'not (a or b)'
  }
}

const truthTableRows = computed(() => {
  if (gateType.value === 'NOT') {
    return [
      { a: 0, b: null, out: 1, active: inputA.value === 0 },
      { a: 1, b: null, out: 0, active: inputA.value === 1 }
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
    const a = c.a === 1
    const b = c.b === 1
    if (gateType.value === 'AND') out = (a && b) ? 1 : 0
    else if (gateType.value === 'OR') out = (a || b) ? 1 : 0
    else if (gateType.value === 'XOR') out = (a !== b) ? 1 : 0
    else if (gateType.value === 'NAND') out = !(a && b) ? 1 : 0
    else if (gateType.value === 'NOR') out = !(a || b) ? 1 : 0
    return {
      a: c.a,
      b: c.b,
      out,
      active: inputA.value === c.a && inputB.value === c.b
    }
  })
})

// ==========================================
// 3. AXBOROT HAJMI VA XOTIRA (MEMORY)
// ==========================================
const memoryUnits = [
  { id: 'b', name: 'Bit (b)', factor: 1 / 8, baseName: '1 yoki 0 (eng kichik birlik)' },
  { id: 'B', name: 'Bayt (Byte)', factor: 1, baseName: '8 ta bit (bitta harf/simvol)' },
  { id: 'KB', name: 'Kilobayt (KB)', factor: 1024, baseName: '1,024 Bayt (kichik matn)' },
  { id: 'MB', name: 'Megabayt (MB)', factor: 1024 * 1024, baseName: '1,024 KB (qo\'shiq, rasm)' },
  { id: 'GB', name: 'Gigabayt (GB)', factor: 1024 * 1024 * 1024, baseName: '1,024 MB (kino, o\'yin)' },
  { id: 'TB', name: 'Terabayt (TB)', factor: 1024 * 1024 * 1024 * 1024, baseName: '1,024 GB (katta disk)' }
]

const inputMemoryValue = ref<number>(1)
const selectedMemoryUnit = ref<string>('MB')

const bytesTotal = computed(() => {
  const unit = memoryUnits.find(u => u.id === selectedMemoryUnit.value) || memoryUnits[3]
  return (inputMemoryValue.value || 0) * unit.factor
})

const formattedMemoryUnits = computed(() => {
  const b = bytesTotal.value
  return [
    { id: 'bit', name: 'Bit (b)', val: (b * 8).toLocaleString('uz-UZ') + ' bit' },
    { id: 'byte', name: 'Bayt (B)', val: b.toLocaleString('uz-UZ', { maximumFractionDigits: 2 }) + ' B' },
    { id: 'kb', name: 'Kilobayt (KB)', val: (b / 1024).toLocaleString('uz-UZ', { maximumFractionDigits: 4 }) + ' KB' },
    { id: 'mb', name: 'Megabayt (MB)', val: (b / (1024 * 1024)).toLocaleString('uz-UZ', { maximumFractionDigits: 4 }) + ' MB' },
    { id: 'gb', name: 'Gigabayt (GB)', val: (b / (1024 * 1024 * 1024)).toLocaleString('uz-UZ', { maximumFractionDigits: 6 }) + ' GB' },
    { id: 'tb', name: 'Terabayt (TB)', val: (b / (1024 * 1024 * 1024 * 1024)).toLocaleString('uz-UZ', { maximumFractionDigits: 8 }) + ' TB' }
  ]
})

const realWorldEquivalents = computed(() => {
  const mb = bytesTotal.value / (1024 * 1024)
  return [
    { name: 'Kitob sahifasi (~2 KB)', count: Math.round(mb * 512).toLocaleString('uz-UZ') + ' bet matn' },
    { name: 'Yuqori sifatli rasm (~3 MB)', count: (mb / 3).toFixed(1) + ' ta fotosurat' },
    { name: 'MP3 Qo\'shiq (~4 MB)', count: (mb / 4).toFixed(1) + ' ta audio trek' },
    { name: 'Full HD Film (~2.5 GB)', count: (mb / 2560).toFixed(2) + ' ta kinofilm' }
  ]
})

// ==========================================
// 4. BLOK-SXEMALAR VA ALGORITM VIZUALIZATORI
// ==========================================
interface FlowStep {
  id: string
  label: string
  shape: 'oval' | 'rect' | 'rhomb' | 'io'
  codeLine: number
  detail: string
}

interface AlgorithmDef {
  id: string
  title: string
  desc: string
  pythonCode: string[]
  steps: FlowStep[]
  variables: Record<string, any>
  runLogic: (stepIdx: number, vars: any) => { nextIdx: number; log: string }
}

const ALGORITHMS: AlgorithmDef[] = [
  {
    id: 'linear',
    title: '1. Chiziqli algoritm (Kofe tayyorlash)',
    desc: 'Har bir qadam ketma-ket, birin-ketin bajariladi.',
    pythonCode: [
      'def make_coffee():',
      '    print("1. Suvni qaynatish")',
      '    print("2. Qahva va shakarni solish")',
      '    print("3. Qaynagan suvni quyish")',
      '    print("4. Qahva tayyor!")'
    ],
    steps: [
      { id: 's1', label: 'Boshlash', shape: 'oval', codeLine: 0, detail: 'Algoritm boshlandi' },
      { id: 's2', label: 'Suvni qaynatish', shape: 'rect', codeLine: 1, detail: 'Choynakda suv qaynadi' },
      { id: 's3', label: 'Qahva va shakar solish', shape: 'rect', codeLine: 2, detail: 'Finjonga masalliqlar solindi' },
      { id: 's4', label: 'Suvni quyish va aralashtirish', shape: 'rect', codeLine: 3, detail: 'Issiq suv quyilib aralashtirildi' },
      { id: 's5', label: 'Tamom (Tayyor)', shape: 'oval', codeLine: 4, detail: 'Qahva ichishga tayyor!' }
    ],
    variables: { holat: 'Boshlanmoqda' },
    runLogic: (idx, v) => {
      const msgs = ['Boshlandi', 'Suv qaynatildi', 'Qahva solindi', 'Aralashtirildi', 'Tayyor bo\'ldi!']
      v.holat = msgs[idx] || 'Tamom'
      return { nextIdx: idx + 1, log: msgs[idx] }
    }
  },
  {
    id: 'branching',
    title: '2. Tarmoqlanuvchi algoritm (Imtihon bahosi)',
    desc: 'Shart (if/else) tekshiriladi: ball >= 60 bo\'lsa "O\'tdi", aks holda "Qayta topshirish".',
    pythonCode: [
      'ball = 75',
      'if ball >= 60:',
      '    natija = "Imtihondan o\'tdi (Ajoyib!)"',
      'else:',
      '    natija = "Qayta topshirish kerak"',
      'print(natija)'
    ],
    steps: [
      { id: 's1', label: 'Boshlash (Ball = 75)', shape: 'oval', codeLine: 0, detail: 'O\'quvchi balli kiritildi: 75' },
      { id: 's2', label: 'Ball >= 60 ?', shape: 'rhomb', codeLine: 1, detail: 'Shart tekshirilmoqda: 75 >= 60 rostmi?' },
      { id: 's3', label: 'Natija: "O\'tdi"', shape: 'rect', codeLine: 2, detail: 'Shart rost bo\'lgani uchun ijobiy tarmoq ishga tushdi' },
      { id: 's4', label: 'Natijani chop etish', shape: 'io', codeLine: 5, detail: 'Ekranga xabar chiqarildi' },
      { id: 's5', label: 'Tamom', shape: 'oval', codeLine: 5, detail: 'Jarayon yakunlandi' }
    ],
    variables: { ball: 75, natija: 'Noma\'lum' },
    runLogic: (idx, v) => {
      if (idx === 1) {
        v.natija = v.ball >= 60 ? 'Imtihondan o\'tdi' : 'Qayta topshirish'
      }
      return { nextIdx: idx + 1, log: `Qadam: ${idx + 1}` }
    }
  },
  {
    id: 'loop',
    title: '3. Takrorlanuvchi algoritm (1 dan 5 gacha sanash)',
    desc: 'Sikl (while / for) toki shart bajarilguncha takrorlanadi.',
    pythonCode: [
      'son = 1',
      'while son <= 5:',
      '    print("Hozirgi son:", son)',
      '    son += 1',
      'print("Sikl tugadi!")'
    ],
    steps: [
      { id: 's1', label: 'Boshlash: son = 1', shape: 'oval', codeLine: 0, detail: 'Boshlang\'ich qiymat o\'rnatildi' },
      { id: 's2', label: 'son <= 5 ?', shape: 'rhomb', codeLine: 1, detail: 'Sikl sharti tekshirilmoqda' },
      { id: 's3', label: 'Ekranga: son ni chiqarish', shape: 'io', codeLine: 2, detail: 'Chop etildi' },
      { id: 's4', label: 'son = son + 1', shape: 'rect', codeLine: 3, detail: 'Son 1 taga oshirildi' },
      { id: 's5', label: 'Tamom (Sikl tugadi)', shape: 'oval', codeLine: 4, detail: 'Shart yolg\'on bo\'ldi va sikl yakunlandi' }
    ],
    variables: { son: 1, ekranda: [] },
    runLogic: (idx, v) => {
      if (idx === 3) {
        v.son++
      }
      return { nextIdx: idx + 1, log: `Son: ${v.son}` }
    }
  }
]

const selectedAlgorithmId = ref<string>('linear')
const currentStepIndex = ref<number>(0)
const algoVars = ref<any>({})
const algoLogs = ref<string[]>([])

const currentAlgorithm = computed(() => ALGORITHMS.find(a => a.id === selectedAlgorithmId.value) || ALGORITHMS[0])

const resetAlgorithm = () => {
  currentStepIndex.value = 0
  algoVars.value = JSON.parse(JSON.stringify(currentAlgorithm.value.variables))
  algoLogs.value = ['Algoritm ishga tushirishga tayyor.']
}

watch(selectedAlgorithmId, () => {
  resetAlgorithm()
})

const nextAlgoStep = () => {
  if (currentStepIndex.value < currentAlgorithm.value.steps.length - 1) {
    currentStepIndex.value++
    currentAlgorithm.value.runLogic(currentStepIndex.value, algoVars.value)
    algoLogs.value.push(currentAlgorithm.value.steps[currentStepIndex.value].detail)
  }
}

// ==========================================
// 5. KOMPYUTER ANATOMIYASI (HARDWARE)
// ==========================================
interface HardwarePart {
  id: string
  name: string
  role: string
  analogy: string
  unit: string
  details: string
  examples: string
  icon: string
}

const HARDWARE_PARTS: HardwarePart[] = [
  {
    id: 'cpu',
    name: 'CPU (Markaziy Protsessor)',
    role: 'Kompyuterning miyasi. Barcha hisob-kitoblar, dastur buyruqlari va mantiqiy amallarni bajaradi.',
    analogy: '🧠 Oshxonadagi bosh oshpaz: barcha buyurtmalarni o\'zi tahlil qiladi va tezlikda pishiradi.',
    unit: 'Gigagerts (GHz) — soniyasiga necha milliard amal bajarishi, Yadrolar (Cores).',
    details: 'Intel Core i5/i7/i9, AMD Ryzen, Apple M1/M2/M3/M4 chiplari.',
    examples: 'Dastur kodini kompilyatsiya qilish, matematik hisoblar, o\'yin fizikasini hisoblash.',
    icon: 'cpu'
  },
  {
    id: 'ram',
    name: 'RAM (Tezkor Xotira)',
    role: 'Vaqtinchalik tezkor xotira. Kompyuter o\'chsa ma\'lumot o\'chib ketadi (uchuvchan xotira).',
    analogy: '🪑 Oshpazning ish stoli: kerakli masalliqlar shu yerda turadi, tezda qo\'l yetadi. Ish tugagach stol tozalanadi.',
    unit: 'Gigabayt (GB) — 8 GB, 16 GB, 32 GB, 64 GB.',
    details: 'DDR4, DDR5 xotira modullari. Ochiq dasturlar va brauzer varaqlari aynan RAM\'da saqlanadi.',
    examples: 'O\'yin o\'ynayotganda yoki brauzerda 20 ta tab ochganda kerak bo\'ladigan joy.',
    icon: 'memory-stick'
  },
  {
    id: 'storage',
    name: 'SSD / HDD (Doimiy Xotira)',
    role: 'Ma\'lumotlarni uzoq muddat xavfsiz saqlash. Kompyuter o\'chganda ham saqlanib qoladi.',
    analogy: '📦 Oshxona ombori (muzlatgich): barcha mahsulotlar javonlarda yillar davomida saqlanadi.',
    unit: 'Gigabayt (GB) va Terabayt (TB) — 512 GB SSD, 1 TB NVMe SSD.',
    details: 'SSD (Solid State Drive) mikrosxemalarda ishlaydi va HDD dan 10-20 barobar tezroq ishlaydi.',
    examples: 'Windows/macOS operatsion tizimi, o\'rnatilgan dasturlar, foto va videolar.',
    icon: 'hard-drive'
  },
  {
    id: 'gpu',
    name: 'GPU (Videokarta)',
    role: 'Grafika va 3D tasvirlarni, piksellarni hamda sun\'iy intellekt (AI/ML) matritsalarini qayta ishlash.',
    analogy: '🎨 Rassomlar guruhi: bitta bosh oshpaz emas, minglab yordamchilar bir vaqtda millionlab nuqtalarni chizadi.',
    unit: 'VRAM (GB) — masalan, NVIDIA RTX 4090 24GB VRAM.',
    details: 'Minglab kichik parallel yadrolardan (CUDA cores) iborat bo\'lib, parallel hisoblashda CPU dan ancha tez.',
    examples: '3D o\'yinlar, video montaj (4K rendering), Neyron tarmoqlarni o\'qitish.',
    icon: 'circuit-board'
  },
  {
    id: 'motherboard',
    name: 'Ona Plata (Motherboard)',
    role: 'Barcha qismlarni (CPU, RAM, SSD, GPU, quvvat bloki) bir-biriga bog\'lovchi markaziy magistral.',
    analogy: '🏙️ Shahar yo\'llari va ko\'priklari: har bir bino va transportni bog\'lab turuvchi infratuzilma.',
    unit: 'Form-faktor: ATX, Micro-ATX, Mini-ITX, Chipset (masalan, B650, Z790).',
    details: 'Shinalar (Buses), portlar (USB, PCIe, SATA) va BIOS chipini o\'zida saqlaydi.',
    examples: 'Barcha signallarning o\'z vaqtida bir qismdan ikkinchisiga xatosiz yetib borishini ta\'minlaydi.',
    icon: 'circuit-board'
  }
]

const selectedHardwareId = ref<string>('cpu')
const currentHardware = computed(() => HARDWARE_PARTS.find(p => p.id === selectedHardwareId.value) || HARDWARE_PARTS[0])

// ==========================================
// 6. SARALASH VA QIDIRUV (SORTING & SEARCH)
// ==========================================
type SortAlgoType = 'bubble' | 'selection' | 'insertion' | 'binary_search'
const sortAlgorithm = ref<SortAlgoType>('bubble')
const sortArraySize = ref<number>(10)
const sortArray = ref<{ val: number; state: 'default' | 'comparing' | 'swapping' | 'sorted' | 'target' }[]>([])
const sortComparisons = ref<number>(0)
const sortSwaps = ref<number>(0)
const sortIsRunning = ref<boolean>(false)
const sortSpeedMs = ref<number>(200) // 400 = slow, 200 = normal, 60 = fast
const sortExplanation = ref<string>('')
const searchTargetVal = ref<number>(45)
let sortTimer: any = null

const generateSortArray = (type: 'random' | 'reversed' | 'sorted' = 'random') => {
  stopSorting()
  const arr: number[] = []
  for (let i = 0; i < sortArraySize.value; i++) {
    arr.push(Math.floor(Math.random() * 85) + 10)
  }
  if (type === 'reversed') arr.sort((a, b) => b - a)
  if (type === 'sorted') arr.sort((a, b) => a - b)
  sortArray.value = arr.map(v => ({ val: v, state: 'default' }))
  sortComparisons.value = 0
  sortSwaps.value = 0
  sortExplanation.value = 'Yangi massiv yaratildi. Saralashni boshlash uchun "Boshlash" tugmasini bosing.'
  if (sortAlgorithm.value === 'binary_search') {
    sortArray.value.sort((a, b) => a.val - b.val)
    searchTargetVal.value = sortArray.value[Math.floor(Math.random() * sortArray.value.length)].val
    sortExplanation.value = `Ikkilik qidiruv uchun massiv saralandi. Qidirilayotgan son: ${searchTargetVal.value}`
  }
}

const sleep = (ms: number) => new Promise(resolve => setTimeout(resolve, ms))

const startSorting = async () => {
  if (sortIsRunning.value) return
  sortIsRunning.value = true
  sortComparisons.value = 0
  sortSwaps.value = 0

  if (sortAlgorithm.value === 'bubble') {
    const n = sortArray.value.length
    for (let i = 0; i < n - 1; i++) {
      for (let j = 0; j < n - i - 1; j++) {
        if (!sortIsRunning.value) return
        sortArray.value[j].state = 'comparing'
        sortArray.value[j + 1].state = 'comparing'
        sortComparisons.value++
        sortExplanation.value = `Taqqoslanmoqda: ${sortArray.value[j].val} va ${sortArray.value[j + 1].val}`
        await sleep(sortSpeedMs.value)

        if (sortArray.value[j].val > sortArray.value[j + 1].val) {
          sortArray.value[j].state = 'swapping'
          sortArray.value[j + 1].state = 'swapping'
          sortSwaps.value++
          sortExplanation.value = `O'rin almashmoqda: ${sortArray.value[j].val} > ${sortArray.value[j + 1].val}`
          const tmp = sortArray.value[j].val
          sortArray.value[j].val = sortArray.value[j + 1].val
          sortArray.value[j + 1].val = tmp
          await sleep(sortSpeedMs.value)
        }
        sortArray.value[j].state = 'default'
        sortArray.value[j + 1].state = 'default'
      }
      sortArray.value[n - i - 1].state = 'sorted'
    }
    sortArray.value[0].state = 'sorted'
    sortExplanation.value = 'Bubble Sort muvaffaqiyatli yakunlandi! Barcha elementlar tartiblandi.'
  } else if (sortAlgorithm.value === 'selection') {
    const n = sortArray.value.length
    for (let i = 0; i < n; i++) {
      let minIdx = i
      sortArray.value[i].state = 'comparing'
      for (let j = i + 1; j < n; j++) {
        if (!sortIsRunning.value) return
        sortArray.value[j].state = 'comparing'
        sortComparisons.value++
        sortExplanation.value = `Eng kichigini qidirish: joriy min=${sortArray.value[minIdx].val}, tekshirilmoqda=${sortArray.value[j].val}`
        await sleep(sortSpeedMs.value)

        if (sortArray.value[j].val < sortArray.value[minIdx].val) {
          if (minIdx !== i) sortArray.value[minIdx].state = 'default'
          minIdx = j
          sortArray.value[minIdx].state = 'swapping'
        } else {
          sortArray.value[j].state = 'default'
        }
      }
      if (minIdx !== i) {
        sortSwaps.value++
        sortExplanation.value = `Eng kichik element topildi (${sortArray.value[minIdx].val}) va ${i}-o'ringa qo'yildi.`
        const tmp = sortArray.value[i].val
        sortArray.value[i].val = sortArray.value[minIdx].val
        sortArray.value[minIdx].val = tmp
        await sleep(sortSpeedMs.value)
      }
      if (minIdx !== i) sortArray.value[minIdx].state = 'default'
      sortArray.value[i].state = 'sorted'
    }
    sortExplanation.value = 'Selection Sort yakunlandi! Har bir qadamda minimum element topildi.'
  } else if (sortAlgorithm.value === 'insertion') {
    const n = sortArray.value.length
    sortArray.value[0].state = 'sorted'
    for (let i = 1; i < n; i++) {
      const key = sortArray.value[i].val
      let j = i - 1
      sortArray.value[i].state = 'swapping'
      sortExplanation.value = `Qo'yish uchun element tanlandi: ${key}`
      await sleep(sortSpeedMs.value)

      while (j >= 0 && sortArray.value[j].val > key) {
        if (!sortIsRunning.value) return
        sortComparisons.value++
        sortSwaps.value++
        sortArray.value[j + 1].val = sortArray.value[j].val
        sortArray.value[j].state = 'comparing'
        sortExplanation.value = `${sortArray.value[j].val} > ${key} bo'lgani uchun o'ngga surildi.`
        await sleep(sortSpeedMs.value)
        sortArray.value[j].state = 'sorted'
        j--
      }
      sortArray.value[j + 1].val = key
      sortArray.value[j + 1].state = 'sorted'
      for (let k = 0; k <= i; k++) sortArray.value[k].state = 'sorted'
      await sleep(sortSpeedMs.value)
    }
    sortExplanation.value = 'Insertion Sort yakunlandi! Elementlar o\'z o\'rniga joylashtirildi.'
  } else if (sortAlgorithm.value === 'binary_search') {
    let low = 0
    let high = sortArray.value.length - 1
    let found = false
    while (low <= high) {
      if (!sortIsRunning.value) return
      const mid = Math.floor((low + high) / 2)
      sortArray.value[mid].state = 'comparing'
      sortComparisons.value++
      sortExplanation.value = `O'rtadagi element (${sortArray.value[mid].val}) nishon (${searchTargetVal.value}) bilan solishtirilmoqda. [Diapazon: ${low} dan ${high} gacha]`
      await sleep(sortSpeedMs.value * 1.5)

      if (sortArray.value[mid].val === searchTargetVal.value) {
        sortArray.value[mid].state = 'target'
        sortExplanation.value = `🎉 Nishon topildi! Indeks: ${mid}, Qiymat: ${searchTargetVal.value}`
        found = true
        break
      } else if (sortArray.value[mid].val < searchTargetVal.value) {
        for (let k = low; k <= mid; k++) sortArray.value[k].state = 'default'
        low = mid + 1
        sortExplanation.value = `${sortArray.value[mid].val} < ${searchTargetVal.value} bo'lgani uchun chap yarmi tashlab yuborildi.`
      } else {
        for (let k = mid; k <= high; k++) sortArray.value[k].state = 'default'
        high = mid - 1
        sortExplanation.value = `${sortArray.value[mid].val} > ${searchTargetVal.value} bo'lgani uchun o'ng yarmi tashlab yuborildi.`
      }
      await sleep(sortSpeedMs.value)
    }
    if (!found) sortExplanation.value = `Nishon (${searchTargetVal.value}) massivda topilmadi.`
  }

  sortIsRunning.value = false
}

const stopSorting = () => {
  sortIsRunning.value = false
  if (sortTimer) clearTimeout(sortTimer)
  sortArray.value.forEach(item => { item.state = 'default' })
}

watch(sortAlgorithm, () => {
  generateSortArray()
})

// ==========================================
// 7. KIBERXAVFSIZLIK & KRIPTOGRAFIYA (CYBER)
// ==========================================
// Caesar Cipher
const caesarText = ref<string>('AXV MENTOR 2026')
const caesarShift = ref<number>(3)

const caesarEncrypted = computed(() => {
  const text = caesarText.value
  const s = ((caesarShift.value % 26) + 26) % 26
  let res = ''
  for (let i = 0; i < text.length; i++) {
    const code = text.charCodeAt(i)
    if (code >= 65 && code <= 90) {
      res += String.fromCharCode(((code - 65 + s) % 26) + 65)
    } else if (code >= 97 && code <= 122) {
      res += String.fromCharCode(((code - 97 + s) % 26) + 97)
    } else {
      res += text[i]
    }
  }
  return res
})

// Base64 Converter
const base64Input = ref<string>('Salom')
const base64Output = computed(() => {
  try {
    return btoa(unescape(encodeURIComponent(base64Input.value)))
  } catch (e) {
    return 'Xatolik'
  }
})

const base64BinaryBreakdown = computed(() => {
  const str = base64Input.value.slice(0, 4) // show first 4 chars
  return str.split('').map(ch => {
    const code = ch.charCodeAt(0)
    return {
      char: ch,
      dec: code,
      bin: code.toString(2).padStart(8, '0')
    }
  })
})

// Password Strength Analyzer
const testPassword = ref<string>('P@ssw0rd2026!')
const passwordStats = computed(() => {
  const p = testPassword.value
  const hasLower = /[a-z]/.test(p)
  const hasUpper = /[A-Z]/.test(p)
  const hasNumber = /[0-9]/.test(p)
  const hasSymbol = /[^a-zA-Z0-9]/.test(p)
  const len = p.length

  let poolSize = 0
  if (hasLower) poolSize += 26
  if (hasUpper) poolSize += 26
  if (hasNumber) poolSize += 10
  if (hasSymbol) poolSize += 32

  const entropy = len > 0 && poolSize > 0 ? Math.round(len * Math.log2(poolSize)) : 0

  let crackTime = 'Bir lahzada'
  let rank = 'Juda kuchsiz'
  let color = '#e06c75'
  let scorePct = Math.min(100, Math.round((entropy / 80) * 100))

  if (entropy < 28) {
    crackTime = '1 soniyadan kam'
    rank = 'Xavfli darajada ojiz'
    color = '#e06c75'
  } else if (entropy < 45) {
    crackTime = 'Bir necha daqiqa'
    rank = 'Kuchsiz'
    color = '#d19a66'
  } else if (entropy < 60) {
    crackTime = 'Bir necha oy'
    rank = 'O\'rtacha'
    color = '#e5c07b'
  } else if (entropy < 80) {
    crackTime = '100+ yil'
    rank = 'Kuchli'
    color = '#98c379'
  } else {
    crackTime = 'Millionlab yillar'
    rank = 'Super mustahkam 🛡️'
    color = '#56b6c2'
  }

  return {
    len,
    hasLower,
    hasUpper,
    hasNumber,
    hasSymbol,
    entropy,
    crackTime,
    rank,
    color,
    scorePct
  }
})

onMounted(() => {
  generateNewGameTarget()
  resetAlgorithm()
  generateSortArray()
})

onUnmounted(() => {
  stopSorting()
})
</script>

<template>
  <div class="foundation-page">
    <Crumbs :items="[{ t: 'Bosh sahifa', l: '/' }, { t: 'CS Laboratoriya' }]" />

    <!-- HERO SECTION -->
    <header class="foundation-hero">
      <div class="fh-left">
        <span class="fh-badge"><Icon name="binary" /> Computer Science Foundation</span>
        <h1>CS Laboratoriya</h1>
        <p class="fh-sub">
          Dasturlash va kompyuter fanlarining fundamental tushunchalarini interaktiv, vizual va sodda tarzda o'rganing.
        </p>
      </div>

      <!-- TAB NAVIGATION (7 CORE MODULES) -->
      <nav class="foundation-tabs" aria-label="Laboratoriya bo'limlari">
        <button class="f-tab" :class="{ active: activeTab === 'binary' }" @click="activeTab = 'binary'">
          <Icon name="binary" /> Ikkilik sanoq
        </button>
        <button class="f-tab" :class="{ active: activeTab === 'logic' }" @click="activeTab = 'logic'">
          <Icon name="zap" /> Mantiqiy elementlar
        </button>
        <button class="f-tab" :class="{ active: activeTab === 'memory' }" @click="activeTab = 'memory'">
          <Icon name="hard-drive" /> Axborot hajmi
        </button>
        <button class="f-tab" :class="{ active: activeTab === 'flowchart' }" @click="activeTab = 'flowchart'">
          <Icon name="git-branch" /> Blok-sxemalar
        </button>
        <button class="f-tab" :class="{ active: activeTab === 'hardware' }" @click="activeTab = 'hardware'">
          <Icon name="cpu" /> Qurilmalar
        </button>
        <button class="f-tab" :class="{ active: activeTab === 'sorting' }" @click="activeTab = 'sorting'">
          <Icon name="layers" /> Saralash & Qidiruv
        </button>
        <button class="f-tab" :class="{ active: activeTab === 'crypto' }" @click="activeTab = 'crypto'">
          <Icon name="shield" /> Kripto & Xavfsizlik
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
          <p>Har bir bit (kalit) 0 yoki 1 holatida bo'ladi. Har bir bitning o'z o'nlik qiymati (vazni) bor.</p>
        </div>
        <button class="btn btn-ghost btn-sm" @click="resetBits">
          <Icon name="rotate-ccw" /> Tozalash (0)
        </button>
      </div>

      <!-- 8-Bit Interactive Switchboard -->
      <div class="bit-board">
        <div
          v-for="(bit, idx) in bits"
          :key="idx"
          class="bit-col"
          :class="{ active: bit === 1 }"
          @click="toggleBit(idx)"
        >
          <div class="bit-weight">{{ bitValues[idx] }}</div>
          <div class="bit-power">2<sup>{{ 7 - idx }}</sup></div>
          <div class="bit-switch">
            <span class="bit-digit">{{ bit }}</span>
          </div>
          <div class="bit-state">{{ bit === 1 ? 'YONIQ' : 'O\'CHIQ' }}</div>
        </div>
      </div>

      <!-- Live Calculation & Encodings -->
      <div class="calc-grid">
        <div class="calc-box highlight">
          <span class="cb-label">O'nlik sanoq (Decimal, 10-lik)</span>
          <div class="cb-val">{{ decimalValue }}</div>
          <span class="cb-sub">
            <span v-for="(b, idx) in bits" :key="idx" v-show="b === 1">
              {{ bitValues[idx] }}<span v-if="idx < bits.lastIndexOf(1)"> + </span>
            </span>
            <span v-if="decimalValue === 0">0</span>
          </span>
        </div>

        <div class="calc-box">
          <span class="cb-label">Ikkilik kod (Binary, 2-lik)</span>
          <div class="cb-val mono">{{ binaryString }}</div>
          <span class="cb-sub">8 bit = 1 Bayt</span>
        </div>

        <div class="calc-box">
          <span class="cb-label">O'n oltilik (Hexadecimal, 16-lik)</span>
          <div class="cb-val mono">{{ hexValue }}</div>
          <span class="cb-sub">Rang kodlari va xotira manzillari</span>
        </div>

        <div class="calc-box">
          <span class="cb-label">ASCII Belgisi</span>
          <div class="cb-val ascii">{{ asciiChar }}</div>
          <span class="cb-sub">Kompyuter matnni qanday ko'radi</span>
        </div>
      </div>

      <!-- Quick Preset Buttons -->
      <div class="presets-row">
        <span class="pr-label">Tezkor namunalar:</span>
        <button class="pr-btn" @click="setDecimal(1)">1 (Faqat oxirgi bit)</button>
        <button class="pr-btn" @click="setDecimal(42)">42 (00101010)</button>
        <button class="pr-btn" @click="setDecimal(65)">65 ('A' harfi)</button>
        <button class="pr-btn" @click="setDecimal(127)">127 (01111111)</button>
        <button class="pr-btn" @click="setDecimal(255)">255 (Barchasi 1)</button>
      </div>

      <!-- Binary Challenge Game -->
      <div class="game-section">
        <div class="game-head">
          <div>
            <h3><Icon name="sparkles" /> Ikkilik chaqiriq: Sonni yig'ing!</h3>
            <p>Berilgan sonni hosil qilish uchun kerakli bitlarni yoqing.</p>
          </div>
          <div class="game-stats">
            <div class="gs-pill">Ball: <b>{{ gameScore }}</b></div>
            <div class="gs-pill">Streak: <b>{{ gameStreak }} 🔥</b></div>
          </div>
        </div>

        <div class="game-body">
          <div class="game-target-box">
            <span>Maqsad son:</span>
            <div class="gt-number">{{ gameTarget }}</div>
          </div>
          <div class="game-action">
            <button class="btn btn-primary btn-lg" @click="checkGameAnswer">
              <Icon name="check" /> Tekshirish
            </button>
            <button class="btn btn-ghost btn-lg" @click="generateNewGameTarget">
              O'tkazib yuborish
            </button>
          </div>
        </div>

        <div v-if="gameFeedback === 'success'" class="feedback-toast success">
          🎉 Barakalla! To'g'ri yig'ildi (+10 ball).
        </div>
        <div v-else-if="gameFeedback === 'error'" class="feedback-toast error">
          ❌ Hozircha {{ decimalValue }} bo'ldi, kutilgan: {{ gameTarget }}. Yana urinib ko'ring!
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- TAB 2: MANTIQIY ELEMENTLAR (LOGIC GATES)  -->
    <!-- ========================================== -->
    <section v-if="activeTab === 'logic'" class="lab-card">
      <div class="card-head">
        <div>
          <h2><Icon name="zap" /> Mantiqiy elementlar (Logic Gates) simulyatori</h2>
          <p>Dasturlashdagi <code>if / else</code> shartlari va kompyuter mikrosxemalari aynan shu mantiqiy darvozalar ustiga qurilgan.</p>
        </div>
      </div>

      <!-- Gate Selector -->
      <div class="gate-selector">
        <button
          v-for="g in ['AND', 'OR', 'NOT', 'XOR', 'NAND', 'NOR']"
          :key="g"
          class="gate-btn"
          :class="{ active: gateType === g }"
          @click="gateType = g as any"
        >
          {{ g }}
        </button>
      </div>

      <!-- Interactive Circuit Simulation -->
      <div class="circuit-area">
        <div class="circuit-inputs">
          <div class="sw-wrapper">
            <span class="sw-label">Kirish A</span>
            <button
              class="switch-btn"
              :class="{ on: inputA === 1 }"
              @click="inputA = inputA === 1 ? 0 : 1"
            >
              {{ inputA }}
            </button>
            <span class="sw-status">{{ inputA === 1 ? 'ROST (True)' : 'YOLG\'ON (False)' }}</span>
          </div>

          <div v-if="gateType !== 'NOT'" class="sw-wrapper">
            <span class="sw-label">Kirish B</span>
            <button
              class="switch-btn"
              :class="{ on: inputB === 1 }"
              @click="inputB = inputB === 1 ? 0 : 1"
            >
              {{ inputB }}
            </button>
            <span class="sw-status">{{ inputB === 1 ? 'ROST (True)' : 'YOLG\'ON (False)' }}</span>
          </div>
        </div>

        <!-- Visual Gate Diagram -->
        <div class="gate-visual">
          <div class="gv-box">
            <span class="gv-title">{{ gateType }}</span>
            <span class="gv-sub">GATE</span>
          </div>
          <div class="gv-wire" :class="{ live: gateOutput === 1 }"></div>
        </div>

        <!-- Output Indicator (Bulb) -->
        <div class="circuit-output">
          <span class="out-label">Natija (Chiqish)</span>
          <div class="bulb-box" :class="{ on: gateOutput === 1 }">
            <Icon name="lightbulb" />
            <div class="bulb-glow" v-if="gateOutput === 1"></div>
          </div>
          <div class="out-val mono">{{ gateOutput }}</div>
          <span class="out-text">{{ gateOutput === 1 ? '💡 Signal bor (1)' : '⭕ Signal yo\'q (0)' }}</span>
        </div>
      </div>

      <!-- Logic Explanation & Python code -->
      <div class="gate-info-grid">
        <div class="gi-box">
          <h4>Qoida va formula:</h4>
          <p>{{ gateExplanations[gateType].desc }}</p>
          <div class="formula-badge">Formula: <code>{{ gateExplanations[gateType].formula }}</code></div>
        </div>

        <div class="gi-box">
          <h4>Python tilidagi ifodasi:</h4>
          <pre class="code-preview"><code>{{ gateExplanations[gateType].code }}</code></pre>
        </div>
      </div>

      <!-- Truth Table -->
      <div class="truth-table-card">
        <h3>Rostlik jadvali (Truth Table)</h3>
        <table class="truth-table">
          <thead>
            <tr>
              <th>Kirish A</th>
              <th v-if="gateType !== 'NOT'">Kirish B</th>
              <th>Chiqish (Natija)</th>
              <th>Holat</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(row, idx) in truthTableRows"
              :key="idx"
              :class="{ 'row-active': row.active }"
            >
              <td><span class="badge-bit" :class="{ one: row.a === 1 }">{{ row.a }}</span></td>
              <td v-if="gateType !== 'NOT'"><span class="badge-bit" :class="{ one: row.b === 1 }">{{ row.b }}</span></td>
              <td><span class="badge-bit out" :class="{ one: row.out === 1 }">{{ row.out }}</span></td>
              <td>
                <span v-if="row.active" class="active-tag">Hozirgi holat ◀</span>
                <span v-else class="idle-tag">—</span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- TAB 3: AXBOROT HAJMI VA XOTIRA (MEMORY)   -->
    <!-- ========================================== -->
    <section v-if="activeTab === 'memory'" class="lab-card">
      <div class="card-head">
        <div>
          <h2><Icon name="hard-drive" /> Axborot o'lchov birliklari kalkulyatori</h2>
          <p>Kompyuterda har bir pog'ona 1024 (2<sup>10</sup>) ga karrali ravishda ortadi.</p>
        </div>
      </div>

      <!-- Input Converter -->
      <div class="memory-input-row">
        <div class="mi-field">
          <label>Qiymatni kiriting:</label>
          <input
            type="number"
            min="0"
            step="1"
            v-model.number="inputMemoryValue"
            class="mem-input"
          />
        </div>
        <div class="mi-field">
          <label>Birlikni tanlang:</label>
          <div class="unit-selector">
            <button
              v-for="u in memoryUnits"
              :key="u.id"
              class="u-btn"
              :class="{ active: selectedMemoryUnit === u.id }"
              @click="selectedMemoryUnit = u.id"
            >
              {{ u.name }}
            </button>
          </div>
        </div>
      </div>

      <!-- Converted Values Grid -->
      <div class="units-grid">
        <div v-for="unit in formattedMemoryUnits" :key="unit.id" class="unit-card">
          <span class="uc-name">{{ unit.name }}</span>
          <div class="uc-val">{{ unit.val }}</div>
        </div>
      </div>

      <!-- Memory Ladder Hierarchy -->
      <div class="ladder-card">
        <h3>Xotira narvoni (1024 qoidasi)</h3>
        <div class="ladder-steps">
          <div class="l-step"><span class="ls-u">8 Bit</span> = 1 Bayt</div>
          <div class="l-step"><span class="ls-u">1024 Bayt</span> = 1 KB (Kilobayt)</div>
          <div class="l-step"><span class="ls-u">1024 KB</span> = 1 MB (Megabayt)</div>
          <div class="l-step"><span class="ls-u">1024 MB</span> = 1 GB (Gigabayt)</div>
          <div class="l-step"><span class="ls-u">1024 GB</span> = 1 TB (Terabayt)</div>
        </div>
      </div>

      <!-- Real World Analogies -->
      <div class="analogies-card">
        <h3>Hayotiy misollarda bu qancha?</h3>
        <p class="an-sub">Kiritilgan <b>{{ inputMemoryValue }} {{ selectedMemoryUnit }}</b> hajmga taxminan quyidagilar sig'adi:</p>
        <div class="an-grid">
          <div v-for="item in realWorldEquivalents" :key="item.name" class="an-box">
            <span class="ab-icon"><Icon name="sparkles" /></span>
            <div>
              <div class="ab-title">{{ item.name }}</div>
              <div class="ab-val">{{ item.count }}</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- TAB 4: ALGORITM VA BLOK-SXEMALAR          -->
    <!-- ========================================== -->
    <section v-if="activeTab === 'flowchart'" class="lab-card">
      <div class="card-head">
        <div>
          <h2><Icon name="git-branch" /> Algoritmlar va Blok-sxemalar vizualizatori</h2>
          <p>Algoritm — maqsadga erishish uchun bajariladigan aniq buyruqlar ketma-ketligi.</p>
        </div>
        <div class="head-actions">
          <button class="btn btn-primary btn-sm" @click="nextAlgoStep">
            <Icon name="play" /> Keyingi qadam ({{ currentStepIndex + 1 }}/{{ currentAlgorithm.steps.length }})
          </button>
          <button class="btn btn-ghost btn-sm" @click="resetAlgorithm">
            <Icon name="rotate-ccw" /> Boshiga
          </button>
        </div>
      </div>

      <!-- Algorithm Type Selector -->
      <div class="algo-type-tabs">
        <button
          v-for="a in ALGORITHMS"
          :key="a.id"
          class="at-tab"
          :class="{ active: selectedAlgorithmId === a.id }"
          @click="selectedAlgorithmId = a.id"
        >
          {{ a.title }}
        </button>
      </div>

      <div class="algo-main-grid">
        <!-- Visual Flowchart Box -->
        <div class="flowchart-box">
          <div class="fc-header">
            <h4>Blok-sxema ko'rinishi</h4>
            <span>Qadam: {{ currentStepIndex + 1 }}</span>
          </div>

          <div class="fc-chain">
            <div
              v-for="(step, idx) in currentAlgorithm.steps"
              :key="step.id"
              class="fc-node-wrapper"
            >
              <div
                class="fc-node"
                :class="[step.shape, { active: currentStepIndex === idx, done: currentStepIndex > idx }]"
              >
                <span class="fcn-idx">{{ idx + 1 }}</span>
                <span class="fcn-label">{{ step.label }}</span>
              </div>
              <div v-if="idx < currentAlgorithm.steps.length - 1" class="fc-arrow">
                ↓
              </div>
            </div>
          </div>
        </div>

        <!-- Python Code & Variables Inspector -->
        <div class="algo-details-col">
          <div class="adc-card">
            <h4>Mos keluvchi Python kodi:</h4>
            <div class="code-flow-wrapper">
              <div
                v-for="(line, lIdx) in currentAlgorithm.pythonCode"
                :key="lIdx"
                class="code-line"
                :class="{ highlight: currentAlgorithm.steps[currentStepIndex]?.codeLine === lIdx }"
              >
                <span class="ln">{{ lIdx + 1 }}</span>
                <span class="code-txt">{{ line }}</span>
              </div>
            </div>
          </div>

          <div class="adc-card">
            <h4>O'zgaruvchilar xotirasi:</h4>
            <pre class="vars-json"><code>{{ JSON.stringify(algoVars, null, 2) }}</code></pre>
          </div>

          <div class="adc-card">
            <h4>Ijro jurnali:</h4>
            <ul class="logs-list">
              <li v-for="(log, logIdx) in algoLogs" :key="logIdx">
                ✓ {{ log }}
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- TAB 5: KOMPYUTER ANATOMIYASI (HARDWARE)    -->
    <!-- ========================================== -->
    <section v-if="activeTab === 'hardware'" class="lab-card">
      <div class="card-head">
        <div>
          <h2><Icon name="cpu" /> Kompyuter Anatomiyasi (Hardware)</h2>
          <p>Kompyuterning asosiy apparat qismlari, ularning o'zaro bog'liqligi va amaliy vazifalari.</p>
        </div>
      </div>

      <!-- Parts Navigation -->
      <div class="hardware-nav">
        <button
          v-for="part in HARDWARE_PARTS"
          :key="part.id"
          class="hwn-btn"
          :class="{ active: selectedHardwareId === part.id }"
          @click="selectedHardwareId = part.id"
        >
          <span class="hwn-icon"><Icon :name="part.icon" /></span>
          <span class="hwn-name">{{ part.name.split(' (')[0] }}</span>
        </button>
      </div>

      <!-- Selected Part Interactive Showcase -->
      <div class="part-showcase">
        <div class="ps-header">
          <div class="ps-badge"><Icon :name="currentHardware.icon" /> {{ currentHardware.name }}</div>
          <div class="ps-unit"><b>Birligi:</b> {{ currentHardware.unit }}</div>
        </div>

        <div class="ps-body">
          <div class="ps-info-block">
            <h4><Icon name="sparkles" /> Hayotiy o'xshatish:</h4>
            <p class="ps-analogy">{{ currentHardware.analogy }}</p>
          </div>

          <div class="ps-info-block">
            <h4><Icon name="info" /> Asosiy vazifasi:</h4>
            <p>{{ currentHardware.role }}</p>
          </div>

          <div class="ps-info-block">
            <h4><Icon name="check" /> Haqiqiy misollar:</h4>
            <p>{{ currentHardware.details }}</p>
            <div class="ps-examples"><b>Qayerda kerak:</b> {{ currentHardware.examples }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- TAB 6: SARALASH VA QIDIRUV (SORTING)      -->
    <!-- ========================================== -->
    <section v-if="activeTab === 'sorting'" class="lab-card">
      <div class="card-head">
        <div>
          <h2><Icon name="layers" /> Saralash va Qidiruv algoritmlari vizualizatori</h2>
          <p>Elementlarni tartiblash va qidirish algoritmlarining qadam-baqadam animatsion ko'rinishi.</p>
        </div>
        <div class="head-actions">
          <button v-if="!sortIsRunning" class="btn btn-primary btn-sm" @click="startSorting">
            <Icon name="play" /> Boshlash
          </button>
          <button v-else class="btn btn-warning btn-sm" @click="stopSorting">
            To'xtatish
          </button>
          <button class="btn btn-ghost btn-sm" @click="generateSortArray('random')">
            <Icon name="rotate-ccw" /> Yangi massiv
          </button>
        </div>
      </div>

      <!-- Controls Row -->
      <div class="sort-controls">
        <div class="sc-group">
          <label>Algoritm:</label>
          <div class="btn-group-sm">
            <button class="sc-btn" :class="{ active: sortAlgorithm === 'bubble' }" @click="sortAlgorithm = 'bubble'">Bubble Sort</button>
            <button class="sc-btn" :class="{ active: sortAlgorithm === 'selection' }" @click="sortAlgorithm = 'selection'">Selection Sort</button>
            <button class="sc-btn" :class="{ active: sortAlgorithm === 'insertion' }" @click="sortAlgorithm = 'insertion'">Insertion Sort</button>
            <button class="sc-btn" :class="{ active: sortAlgorithm === 'binary_search' }" @click="sortAlgorithm = 'binary_search'">Binary Search</button>
          </div>
        </div>

        <div class="sc-group">
          <label>Tezlik:</label>
          <div class="btn-group-sm">
            <button class="sc-btn" :class="{ active: sortSpeedMs === 400 }" @click="sortSpeedMs = 400">Sekin</button>
            <button class="sc-btn" :class="{ active: sortSpeedMs === 200 }" @click="sortSpeedMs = 200">Normal</button>
            <button class="sc-btn" :class="{ active: sortSpeedMs === 60 }" @click="sortSpeedMs = 60">Tez</button>
          </div>
        </div>
      </div>

      <!-- Live Bar Visualizer -->
      <div class="bars-container">
        <div
          v-for="(item, idx) in sortArray"
          :key="idx"
          class="sort-bar"
          :class="item.state"
          :style="{ height: `${Math.max(18, (item.val / 100) * 220)}px` }"
        >
          <span class="bar-val">{{ item.val }}</span>
          <span class="bar-idx">{{ idx }}</span>
        </div>
      </div>

      <!-- Explanation & Metrics -->
      <div class="sort-status-bar">
        <div class="ss-stats">
          <span class="ss-pill">Taqqoslashlar: <b>{{ sortComparisons }}</b></span>
          <span class="ss-pill" v-if="sortAlgorithm !== 'binary_search'">Almashishlar (Swaps): <b>{{ sortSwaps }}</b></span>
          <span class="ss-pill" v-else>Nishon: <b>{{ searchTargetVal }}</b></span>
        </div>
        <div class="ss-exp">{{ sortExplanation }}</div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- TAB 7: KIBERXAVFSIZLIK & KRIPTO (CRYPTO)   -->
    <!-- ========================================== -->
    <section v-if="activeTab === 'crypto'" class="lab-card">
      <div class="card-head">
        <div>
          <h2><Icon name="shield" /> Kiberxavfsizlik va Kriptografiya laboratoriyasi</h2>
          <p>Shifrlash (Encryption), Base64 va parollarning xavfsizlik darajasi tahlili.</p>
        </div>
      </div>

      <div class="crypto-grid">
        <!-- 1. Caesar Cipher -->
        <div class="crypto-card">
          <div class="cc-head">
            <h3><Icon name="key" /> Sezar shifri (Caesar Cipher)</h3>
            <span class="cc-badge">Siljitish: +{{ caesarShift }}</span>
          </div>
          <div class="cc-body">
            <div class="cc-field">
              <label>Asl matn:</label>
              <input type="text" v-model="caesarText" class="mem-input" />
            </div>
            <div class="cc-field">
              <label>Siljitish qadami (Shift 0..25): {{ caesarShift }}</label>
              <input type="range" min="0" max="25" v-model.number="caesarShift" class="range-slider" />
            </div>
            <div class="cc-result">
              <span class="cc-res-label">Shifrlangan natija:</span>
              <div class="cc-res-val mono">{{ caesarEncrypted }}</div>
            </div>
          </div>
        </div>

        <!-- 2. Base64 Converter -->
        <div class="crypto-card">
          <div class="cc-head">
            <h3><Icon name="binary" /> Base64 Kodlash</h3>
            <span class="cc-badge">8-bit → 6-bit</span>
          </div>
          <div class="cc-body">
            <div class="cc-field">
              <label>Matn kiriting:</label>
              <input type="text" v-model="base64Input" class="mem-input" />
            </div>
            <div class="cc-result">
              <span class="cc-res-label">Base64 qatori:</span>
              <div class="cc-res-val mono">{{ base64Output }}</div>
            </div>
            <div class="base64-bits-box">
              <span class="bbb-title">Belgilarning 8-bitli ikkilik ko'rinishi:</span>
              <div class="bbb-grid">
                <div v-for="b in base64BinaryBreakdown" :key="b.char" class="bbb-item">
                  <b>'{{ b.char }}'</b> → <code>{{ b.bin }}</code>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 3. Password Strength Analyzer -->
        <div class="crypto-card full-width">
          <div class="cc-head">
            <h3><Icon name="shield" /> Parol Mustahkamligi Tahlilchisi</h3>
            <span class="cc-badge" :style="{ background: passwordStats.color + '22', color: passwordStats.color }">
              {{ passwordStats.rank }}
            </span>
          </div>
          <div class="cc-body">
            <div class="pass-input-row">
              <input type="text" v-model="testPassword" placeholder="Parolni kiriting..." class="mem-input mono" />
            </div>

            <!-- Strength Bar -->
            <div class="pass-bar-wrapper">
              <div class="pass-bar" :style="{ width: `${passwordStats.scorePct}%`, background: passwordStats.color }"></div>
            </div>

            <div class="pass-metrics-grid">
              <div class="pm-box">
                <span class="pm-label">Entropiya (Bitlar):</span>
                <div class="pm-val">{{ passwordStats.entropy }} bit</div>
              </div>
              <div class="pm-box">
                <span class="pm-label">Buzishga ketadigan vaqt:</span>
                <div class="pm-val highlight">{{ passwordStats.crackTime }}</div>
              </div>
            </div>

            <div class="pass-checklist">
              <span class="pc-item" :class="{ ok: passwordStats.len >= 12 }">
                {{ passwordStats.len >= 12 ? '✓' : '✗' }} Kamida 12 belgi
              </span>
              <span class="pc-item" :class="{ ok: passwordStats.hasUpper }">
                {{ passwordStats.hasUpper ? '✓' : '✗' }} Katta harf (A-Z)
              </span>
              <span class="pc-item" :class="{ ok: passwordStats.hasLower }">
                {{ passwordStats.hasLower ? '✓' : '✗' }} Kichik harf (a-z)
              </span>
              <span class="pc-item" :class="{ ok: passwordStats.hasNumber }">
                {{ passwordStats.hasNumber ? '✓' : '✗' }} Raqamlar (0-9)
              </span>
              <span class="pc-item" :class="{ ok: passwordStats.hasSymbol }">
                {{ passwordStats.hasSymbol ? '✓' : '✗' }} Maxsus belgi (!@#$)
              </span>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.foundation-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1.5rem 1rem 4rem;
}

/* HERO SECTION */
.foundation-hero {
  background: var(--vp-c-bg-elv, #1e1e1e);
  border: 1px solid var(--vp-c-divider, #333);
  border-radius: 12px;
  padding: 2rem;
  margin-bottom: 2rem;
}
.fh-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--vp-c-brand-1, #007acc);
  background: rgba(0, 122, 204, 0.12);
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  margin-bottom: 0.75rem;
}
.foundation-hero h1 {
  font-size: 2.2rem;
  font-weight: 800;
  margin: 0 0 0.5rem;
  letter-spacing: -0.02em;
}
.fh-sub {
  color: var(--vp-c-text-2, #999);
  font-size: 1.05rem;
  margin: 0 0 1.5rem;
  max-width: 750px;
}

/* TAB NAVIGATION */
.foundation-tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}
.f-tab {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: var(--vp-c-bg, #252526);
  border: 1px solid var(--vp-c-divider, #3e3e42);
  color: var(--vp-c-text-1, #d4d4d4);
  padding: 0.6rem 1.1rem;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.92rem;
  cursor: pointer;
  transition: all 0.2s ease;
}
.f-tab:hover {
  border-color: var(--vp-c-brand-1, #007acc);
  background: rgba(0, 122, 204, 0.08);
}
.f-tab.active {
  background: var(--vp-c-brand-1, #007acc);
  border-color: var(--vp-c-brand-1, #007acc);
  color: #fff;
  box-shadow: 0 4px 12px rgba(0, 122, 204, 0.35);
}

/* LAB CARD */
.lab-card {
  background: var(--vp-c-bg-elv, #1e1e1e);
  border: 1px solid var(--vp-c-divider, #333);
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
}
.card-head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
  margin-bottom: 1.75rem;
}
.card-head h2 {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  font-size: 1.45rem;
  font-weight: 700;
  margin: 0 0 0.35rem;
}
.card-head p {
  color: var(--vp-c-text-2, #999);
  margin: 0;
  font-size: 0.95rem;
}
.head-actions {
  display: flex;
  gap: 0.5rem;
}

/* 1. BINARY BOARD */
.bit-board {
  display: grid;
  grid-template-columns: repeat(8, 1fr);
  gap: 0.75rem;
  margin-bottom: 2rem;
}
.bit-col {
  background: var(--vp-c-bg, #252526);
  border: 2px solid var(--vp-c-divider, #3e3e42);
  border-radius: 10px;
  padding: 1rem 0.5rem;
  text-align: center;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  user-select: none;
}
.bit-col:hover {
  transform: translateY(-3px);
  border-color: var(--vp-c-brand-1, #007acc);
}
.bit-col.active {
  background: rgba(0, 122, 204, 0.15);
  border-color: var(--vp-c-brand-1, #007acc);
  box-shadow: 0 0 16px rgba(0, 122, 204, 0.3);
}
.bit-weight {
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--vp-c-text-1, #fff);
}
.bit-power {
  font-size: 0.75rem;
  color: var(--vp-c-text-2, #888);
  margin-bottom: 0.75rem;
}
.bit-switch {
  width: 48px;
  height: 48px;
  margin: 0 auto 0.5rem;
  border-radius: 50%;
  background: #333;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  font-weight: 900;
  font-family: monospace;
  color: #888;
  transition: all 0.2s;
}
.bit-col.active .bit-switch {
  background: var(--vp-c-brand-1, #007acc);
  color: #fff;
  box-shadow: 0 0 12px rgba(0, 122, 204, 0.6);
}
.bit-state {
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  color: var(--vp-c-text-2, #888);
}
.bit-col.active .bit-state {
  color: var(--vp-c-brand-1, #007acc);
}

/* CALC GRID */
.calc-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem;
  margin-bottom: 1.75rem;
}
.calc-box {
  background: var(--vp-c-bg, #252526);
  border: 1px solid var(--vp-c-divider, #3e3e42);
  border-radius: 10px;
  padding: 1.25rem;
}
.calc-box.highlight {
  border-color: var(--vp-c-brand-1, #007acc);
  background: rgba(0, 122, 204, 0.08);
}
.cb-label {
  display: block;
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--vp-c-text-2, #999);
  margin-bottom: 0.35rem;
}
.cb-val {
  font-size: 2rem;
  font-weight: 800;
  color: var(--vp-c-text-1, #fff);
  line-height: 1.2;
}
.cb-val.mono {
  font-family: monospace;
  letter-spacing: 0.05em;
}
.cb-val.ascii {
  color: #e5c07b;
}
.cb-sub {
  display: block;
  font-size: 0.8rem;
  color: var(--vp-c-text-2, #888);
  margin-top: 0.5rem;
}

/* PRESETS */
.presets-row {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.5rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid var(--vp-c-divider, #333);
  margin-bottom: 1.75rem;
}
.pr-label {
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--vp-c-text-2, #999);
}
.pr-btn {
  background: var(--vp-c-bg, #252526);
  border: 1px solid var(--vp-c-divider, #3e3e42);
  color: var(--vp-c-text-1, #ccc);
  padding: 0.35rem 0.75rem;
  border-radius: 6px;
  font-size: 0.82rem;
  cursor: pointer;
  transition: all 0.15s;
}
.pr-btn:hover {
  border-color: var(--vp-c-brand-1, #007acc);
  color: #fff;
}

/* GAME SECTION */
.game-section {
  background: var(--vp-c-bg, #252526);
  border: 1px solid var(--vp-c-divider, #3e3e42);
  border-radius: 10px;
  padding: 1.5rem;
}
.game-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.25rem;
}
.game-head h3 {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1.15rem;
  font-weight: 700;
  margin: 0 0 0.25rem;
  color: #e5c07b;
}
.game-head p {
  font-size: 0.88rem;
  color: var(--vp-c-text-2, #999);
  margin: 0;
}
.game-stats {
  display: flex;
  gap: 0.5rem;
}
.gs-pill {
  background: rgba(0, 0, 0, 0.3);
  border: 1px solid var(--vp-c-divider, #444);
  padding: 0.35rem 0.75rem;
  border-radius: 20px;
  font-size: 0.85rem;
}
.game-body {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
}
.game-target-box {
  display: flex;
  align-items: center;
  gap: 1rem;
}
.game-target-box span {
  font-size: 1rem;
  color: var(--vp-c-text-2, #aaa);
}
.gt-number {
  font-size: 2.5rem;
  font-weight: 900;
  color: var(--vp-c-brand-1, #007acc);
  background: rgba(0, 122, 204, 0.12);
  padding: 0.2rem 1.2rem;
  border-radius: 10px;
}
.game-action {
  display: flex;
  gap: 0.75rem;
}
.feedback-toast {
  margin-top: 1rem;
  padding: 0.75rem 1rem;
  border-radius: 8px;
  font-size: 0.95rem;
  font-weight: 600;
}
.feedback-toast.success {
  background: rgba(46, 125, 50, 0.2);
  border: 1px solid #2e7d32;
  color: #4caf50;
}
.feedback-toast.error {
  background: rgba(198, 40, 40, 0.2);
  border: 1px solid #c62828;
  color: #ef5350;
}

/* 2. LOGIC GATES */
.gate-selector {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 2rem;
}
.gate-btn {
  background: var(--vp-c-bg, #252526);
  border: 1px solid var(--vp-c-divider, #3e3e42);
  color: var(--vp-c-text-1, #ccc);
  padding: 0.5rem 1.25rem;
  border-radius: 8px;
  font-weight: 700;
  font-size: 0.95rem;
  cursor: pointer;
  transition: all 0.2s;
}
.gate-btn:hover {
  border-color: var(--vp-c-brand-1, #007acc);
}
.gate-btn.active {
  background: var(--vp-c-brand-1, #007acc);
  border-color: var(--vp-c-brand-1, #007acc);
  color: #fff;
}
.circuit-area {
  background: var(--vp-c-bg, #181818);
  border: 1px solid var(--vp-c-divider, #333);
  border-radius: 12px;
  padding: 2.5rem 2rem;
  display: flex;
  align-items: center;
  justify-content: space-around;
  gap: 2rem;
  margin-bottom: 2rem;
}
.circuit-inputs {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}
.sw-wrapper {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}
.sw-label {
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--vp-c-text-2, #aaa);
  min-width: 60px;
}
.switch-btn {
  width: 50px;
  height: 50px;
  border-radius: 10px;
  background: #2d2d30;
  border: 2px solid #444;
  color: #888;
  font-size: 1.5rem;
  font-weight: 900;
  cursor: pointer;
  transition: all 0.2s;
}
.switch-btn.on {
  background: #2e7d32;
  border-color: #4caf50;
  color: #fff;
  box-shadow: 0 0 16px rgba(76, 175, 80, 0.4);
}
.sw-status {
  font-size: 0.8rem;
  color: var(--vp-c-text-2, #888);
}
.gate-visual {
  display: flex;
  align-items: center;
}
.gv-box {
  width: 110px;
  height: 90px;
  background: var(--vp-c-bg-elv, #252526);
  border: 2px solid var(--vp-c-brand-1, #007acc);
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 20px rgba(0, 122, 204, 0.25);
}
.gv-title {
  font-size: 1.4rem;
  font-weight: 900;
  color: var(--vp-c-text-1, #fff);
}
.gv-sub {
  font-size: 0.65rem;
  font-weight: 700;
  color: var(--vp-c-brand-1, #007acc);
}
.gv-wire {
  width: 60px;
  height: 4px;
  background: #444;
  transition: all 0.3s;
}
.gv-wire.live {
  background: #ffeb3b;
  box-shadow: 0 0 12px #ffeb3b;
}
.circuit-output {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}
.out-label {
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--vp-c-text-2, #aaa);
}
.bulb-box {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: #2d2d30;
  border: 2px solid #444;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.8rem;
  color: #555;
  transition: all 0.3s;
  position: relative;
}
.bulb-box.on {
  background: #fbc02d;
  border-color: #fff59d;
  color: #000;
  box-shadow: 0 0 28px #ffeb3b;
}
.out-val {
  font-size: 1.8rem;
  font-weight: 900;
}
.out-text {
  font-size: 0.82rem;
  color: var(--vp-c-text-2, #888);
}
.gate-info-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.25rem;
  margin-bottom: 2rem;
}
.gi-box {
  background: var(--vp-c-bg, #252526);
  border: 1px solid var(--vp-c-divider, #3e3e42);
  border-radius: 10px;
  padding: 1.25rem;
}
.gi-box h4 {
  font-size: 0.95rem;
  font-weight: 700;
  margin: 0 0 0.5rem;
}
.gi-box p {
  font-size: 0.9rem;
  color: var(--vp-c-text-2, #aaa);
  margin: 0 0 0.75rem;
}
.formula-badge {
  display: inline-block;
  font-size: 0.85rem;
  background: rgba(0, 122, 204, 0.12);
  padding: 0.3rem 0.6rem;
  border-radius: 6px;
  color: var(--vp-c-brand-1, #007acc);
}
.code-preview {
  margin: 0;
  padding: 0.75rem;
  background: #111;
  border-radius: 6px;
  font-size: 0.85rem;
  color: #98c379;
}
.truth-table-card h3 {
  font-size: 1.15rem;
  margin: 0 0 1rem;
}
.truth-table {
  width: 100%;
  border-collapse: collapse;
  background: var(--vp-c-bg, #252526);
  border-radius: 8px;
  overflow: hidden;
}
.truth-table th, .truth-table td {
  padding: 0.75rem 1rem;
  text-align: center;
  border-bottom: 1px solid var(--vp-c-divider, #3e3e42);
}
.truth-table th {
  background: rgba(0, 0, 0, 0.2);
  font-size: 0.85rem;
}
.truth-table tr.row-active {
  background: rgba(0, 122, 204, 0.15);
  font-weight: 700;
}
.badge-bit {
  display: inline-block;
  width: 28px;
  height: 28px;
  line-height: 28px;
  border-radius: 6px;
  background: #333;
  color: #888;
  font-weight: 800;
  font-family: monospace;
}
.badge-bit.one {
  background: #2e7d32;
  color: #fff;
}
.badge-bit.out.one {
  background: #fbc02d;
  color: #000;
}
.active-tag {
  color: var(--vp-c-brand-1, #007acc);
  font-size: 0.82rem;
  font-weight: 700;
}
.idle-tag {
  color: #666;
}

/* 3. MEMORY CALCULATOR */
.memory-input-row {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  margin-bottom: 2rem;
}
.mi-field {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
.mi-field label {
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--vp-c-text-2, #aaa);
}
.mem-input {
  background: var(--vp-c-bg, #252526);
  border: 1px solid var(--vp-c-divider, #444);
  color: var(--vp-c-text-1, #fff);
  padding: 0.6rem 1rem;
  border-radius: 8px;
  font-size: 1.1rem;
  font-weight: 700;
  min-width: 160px;
}
.unit-selector {
  display: flex;
  flex-wrap: wrap;
  gap: 0.35rem;
}
.u-btn {
  background: var(--vp-c-bg, #252526);
  border: 1px solid var(--vp-c-divider, #3e3e42);
  color: var(--vp-c-text-1, #ccc);
  padding: 0.5rem 0.85rem;
  border-radius: 6px;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s;
}
.u-btn.active {
  background: var(--vp-c-brand-1, #007acc);
  border-color: var(--vp-c-brand-1, #007acc);
  color: #fff;
}
.units-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
}
.unit-card {
  background: var(--vp-c-bg, #252526);
  border: 1px solid var(--vp-c-divider, #3e3e42);
  border-radius: 10px;
  padding: 1.25rem;
}
.uc-name {
  font-size: 0.82rem;
  color: var(--vp-c-text-2, #888);
}
.uc-val {
  font-size: 1.2rem;
  font-weight: 800;
  margin-top: 0.35rem;
  color: var(--vp-c-brand-1, #007acc);
  word-break: break-all;
}
.ladder-card, .analogies-card {
  background: var(--vp-c-bg, #252526);
  border: 1px solid var(--vp-c-divider, #3e3e42);
  border-radius: 10px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
}
.ladder-card h3, .analogies-card h3 {
  font-size: 1.15rem;
  margin: 0 0 1rem;
}
.ladder-steps {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}
.l-step {
  background: rgba(0, 0, 0, 0.25);
  padding: 0.5rem 0.85rem;
  border-radius: 6px;
  font-size: 0.88rem;
  border: 1px solid #333;
}
.ls-u {
  color: #e5c07b;
  font-weight: 700;
}
.an-sub {
  font-size: 0.9rem;
  color: var(--vp-c-text-2, #aaa);
  margin-bottom: 1.25rem;
}
.an-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem;
}
.an-box {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  background: rgba(0, 0, 0, 0.25);
  padding: 1rem;
  border-radius: 8px;
  border: 1px solid #333;
}
.ab-icon {
  color: #e5c07b;
  font-size: 1.2rem;
}
.ab-title {
  font-size: 0.82rem;
  color: var(--vp-c-text-2, #888);
}
.ab-val {
  font-size: 1.05rem;
  font-weight: 800;
  color: var(--vp-c-text-1, #fff);
}

/* 4. FLOWCHART */
.algo-type-tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}
.at-tab {
  background: var(--vp-c-bg, #252526);
  border: 1px solid var(--vp-c-divider, #3e3e42);
  color: var(--vp-c-text-1, #ccc);
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.88rem;
  cursor: pointer;
  transition: all 0.2s;
}
.at-tab.active {
  background: var(--vp-c-brand-1, #007acc);
  color: #fff;
  border-color: var(--vp-c-brand-1, #007acc);
}
.algo-main-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}
.flowchart-box {
  background: var(--vp-c-bg, #181818);
  border: 1px solid var(--vp-c-divider, #333);
  border-radius: 10px;
  padding: 1.5rem;
}
.fc-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 1.5rem;
  font-size: 0.9rem;
  color: var(--vp-c-text-2, #aaa);
}
.fc-header h4 {
  margin: 0;
  font-size: 1rem;
  color: #fff;
}
.fc-chain {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}
.fc-node-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
}
.fc-node {
  width: 85%;
  max-width: 280px;
  padding: 0.75rem 1rem;
  text-align: center;
  background: #252526;
  border: 2px solid #444;
  border-radius: 6px;
  font-size: 0.88rem;
  font-weight: 600;
  position: relative;
  transition: all 0.2s;
}
.fc-node.oval {
  border-radius: 24px;
  background: #1f2e3d;
  border-color: #2b5b84;
}
.fc-node.rhomb {
  background: #3a2e1f;
  border-color: #855f2b;
}
.fc-node.io {
  border-radius: 0;
  transform: skewX(-10deg);
  background: #253326;
  border-color: #3b6b3e;
}
.fc-node.active {
  border-color: var(--vp-c-brand-1, #007acc);
  box-shadow: 0 0 16px rgba(0, 122, 204, 0.5);
  transform: scale(1.04);
}
.fc-node.done {
  opacity: 0.6;
}
.fcn-idx {
  position: absolute;
  left: 8px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 0.7rem;
  background: rgba(0, 0, 0, 0.4);
  width: 20px;
  height: 20px;
  line-height: 20px;
  border-radius: 50%;
}
.fc-arrow {
  color: #666;
  font-size: 1.2rem;
  margin: 0.2rem 0;
}
.algo-details-col {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.adc-card {
  background: var(--vp-c-bg, #252526);
  border: 1px solid var(--vp-c-divider, #3e3e42);
  border-radius: 8px;
  padding: 1.25rem;
}
.adc-card h4 {
  font-size: 0.9rem;
  margin: 0 0 0.75rem;
  color: var(--vp-c-text-2, #aaa);
}
.code-flow-wrapper {
  background: #111;
  border-radius: 6px;
  padding: 0.5rem 0;
}
.code-line {
  padding: 0.2rem 0.75rem;
  font-family: monospace;
  font-size: 0.85rem;
  display: flex;
  gap: 0.75rem;
}
.code-line.highlight {
  background: rgba(0, 122, 204, 0.25);
  border-left: 3px solid var(--vp-c-brand-1, #007acc);
}
.code-line .ln {
  color: #555;
}
.code-line .code-txt {
  color: #d4d4d4;
}
.vars-json {
  margin: 0;
  background: #111;
  padding: 0.75rem;
  border-radius: 6px;
  font-size: 0.82rem;
  color: #e5c07b;
}
.logs-list {
  margin: 0;
  padding-left: 1.25rem;
  font-size: 0.85rem;
  color: #98c379;
}

/* 5. HARDWARE */
.hardware-nav {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-bottom: 2rem;
}
.hwn-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: var(--vp-c-bg, #252526);
  border: 1px solid var(--vp-c-divider, #3e3e42);
  color: var(--vp-c-text-1, #ccc);
  padding: 0.6rem 1.1rem;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.92rem;
  cursor: pointer;
  transition: all 0.2s;
}
.hwn-btn.active {
  background: var(--vp-c-brand-1, #007acc);
  border-color: var(--vp-c-brand-1, #007acc);
  color: #fff;
}
.part-showcase {
  background: var(--vp-c-bg, #181818);
  border: 1px solid var(--vp-c-divider, #333);
  border-radius: 12px;
  padding: 2rem;
}
.ps-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid var(--vp-c-divider, #333);
}
.ps-badge {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1.3rem;
  font-weight: 800;
  color: #fff;
}
.ps-unit {
  font-size: 0.9rem;
  color: var(--vp-c-text-2, #aaa);
}
.ps-body {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}
.ps-info-block h4 {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.95rem;
  margin: 0 0 0.35rem;
  color: var(--vp-c-brand-1, #007acc);
}
.ps-analogy {
  font-size: 1.05rem;
  color: #e5c07b;
  font-weight: 600;
  margin: 0;
}
.ps-examples {
  margin-top: 0.5rem;
  font-size: 0.88rem;
  color: var(--vp-c-text-2, #888);
}

/* 6. SORTING */
.sort-controls {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}
.sc-group {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.sc-group label {
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--vp-c-text-2, #aaa);
}
.btn-group-sm {
  display: flex;
  gap: 0.3rem;
}
.sc-btn {
  background: var(--vp-c-bg, #252526);
  border: 1px solid var(--vp-c-divider, #3e3e42);
  color: var(--vp-c-text-1, #ccc);
  padding: 0.35rem 0.75rem;
  border-radius: 6px;
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s;
}
.sc-btn.active {
  background: var(--vp-c-brand-1, #007acc);
  border-color: var(--vp-c-brand-1, #007acc);
  color: #fff;
}
.bars-container {
  display: flex;
  align-items: flex-end;
  justify-content: center;
  gap: 8px;
  height: 250px;
  background: var(--vp-c-bg, #141414);
  border: 1px solid var(--vp-c-divider, #333);
  border-radius: 10px;
  padding: 1.5rem 1rem 0.5rem;
  margin-bottom: 1.5rem;
}
.sort-bar {
  flex: 1;
  max-width: 45px;
  background: var(--vp-c-brand-1, #007acc);
  border-radius: 6px 6px 0 0;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  padding: 6px 2px;
  transition: all 0.15s ease;
}
.sort-bar.comparing {
  background: #e5c07b !important;
  box-shadow: 0 0 12px rgba(229, 192, 123, 0.6);
}
.sort-bar.swapping {
  background: #e06c75 !important;
  box-shadow: 0 0 12px rgba(224, 108, 117, 0.8);
}
.sort-bar.sorted {
  background: #98c379 !important;
}
.sort-bar.target {
  background: #c678dd !important;
  box-shadow: 0 0 16px rgba(198, 120, 221, 0.8);
}
.bar-val {
  font-size: 0.75rem;
  font-weight: 800;
  color: #fff;
}
.bar-idx {
  font-size: 0.65rem;
  color: rgba(255, 255, 255, 0.7);
}
.sort-status-bar {
  background: var(--vp-c-bg, #252526);
  border: 1px solid var(--vp-c-divider, #3e3e42);
  border-radius: 8px;
  padding: 1rem 1.25rem;
}
.ss-stats {
  display: flex;
  gap: 1rem;
  margin-bottom: 0.5rem;
}
.ss-pill {
  font-size: 0.85rem;
  color: var(--vp-c-text-2, #aaa);
}
.ss-pill b {
  color: var(--vp-c-brand-1, #007acc);
}
.ss-exp {
  font-size: 0.92rem;
  font-weight: 600;
  color: #e5c07b;
}

/* 7. CRYPTO & SECURITY */
.crypto-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}
.crypto-card {
  background: var(--vp-c-bg, #252526);
  border: 1px solid var(--vp-c-divider, #3e3e42);
  border-radius: 10px;
  padding: 1.25rem;
}
.crypto-card.full-width {
  grid-column: 1 / -1;
}
.cc-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1rem;
}
.cc-head h3 {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1.05rem;
  margin: 0;
}
.cc-badge {
  font-size: 0.75rem;
  font-weight: 700;
  background: rgba(0, 122, 204, 0.15);
  color: var(--vp-c-brand-1, #007acc);
  padding: 0.2rem 0.5rem;
  border-radius: 12px;
}
.cc-body {
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
}
.cc-field label {
  display: block;
  font-size: 0.8rem;
  color: var(--vp-c-text-2, #aaa);
  margin-bottom: 0.35rem;
}
.range-slider {
  width: 100%;
  accent-color: var(--vp-c-brand-1, #007acc);
}
.cc-result {
  background: #181818;
  border-radius: 6px;
  padding: 0.75rem;
}
.cc-res-label {
  display: block;
  font-size: 0.75rem;
  color: #888;
  margin-bottom: 0.25rem;
}
.cc-res-val {
  font-size: 1.15rem;
  font-weight: 800;
  color: #e5c07b;
  word-break: break-all;
}
.base64-bits-box {
  font-size: 0.8rem;
  color: #aaa;
}
.bbb-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
  gap: 0.4rem;
  margin-top: 0.4rem;
}
.bbb-item {
  background: #181818;
  padding: 0.3rem 0.5rem;
  border-radius: 4px;
}
.pass-bar-wrapper {
  height: 8px;
  background: #333;
  border-radius: 4px;
  overflow: hidden;
  margin: 0.5rem 0 1rem;
}
.pass-bar {
  height: 100%;
  transition: all 0.3s ease;
}
.pass-metrics-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin-bottom: 1rem;
}
.pm-box {
  background: #181818;
  padding: 0.75rem;
  border-radius: 6px;
}
.pm-label {
  font-size: 0.75rem;
  color: #888;
}
.pm-val {
  font-size: 1.25rem;
  font-weight: 800;
  margin-top: 0.25rem;
}
.pm-val.highlight {
  color: #98c379;
}
.pass-checklist {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}
.pc-item {
  font-size: 0.82rem;
  padding: 0.25rem 0.6rem;
  border-radius: 6px;
  background: rgba(255, 255, 255, 0.05);
  color: #888;
}
.pc-item.ok {
  background: rgba(152, 195, 121, 0.15);
  color: #98c379;
  font-weight: 600;
}

/* BUTTONS */
.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-weight: 600;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.15s;
  border: none;
}
.btn-sm {
  padding: 0.4rem 0.85rem;
  font-size: 0.85rem;
}
.btn-xs {
  padding: 0.25rem 0.5rem;
  font-size: 0.75rem;
}
.btn-lg {
  padding: 0.65rem 1.4rem;
  font-size: 1rem;
}
.btn-primary {
  background: var(--vp-c-brand-1, #007acc);
  color: #fff;
}
.btn-primary:hover {
  background: #0062a3;
}
.btn-ghost {
  background: rgba(255, 255, 255, 0.08);
  color: var(--vp-c-text-1, #d4d4d4);
  border: 1px solid var(--vp-c-divider, #444);
}
.btn-ghost:hover {
  background: rgba(255, 255, 255, 0.15);
}
.btn-warning {
  background: #d19a66;
  color: #000;
}

@media (max-width: 768px) {
  .bit-board {
    grid-template-columns: repeat(4, 1fr);
  }
  .circuit-area, .algo-main-grid, .gate-info-grid, .crypto-grid {
    grid-template-columns: 1fr;
    flex-direction: column;
  }
}
</style>
