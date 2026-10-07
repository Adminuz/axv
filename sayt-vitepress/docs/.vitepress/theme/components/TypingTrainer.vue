<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted, watch, nextTick } from 'vue'
import { withBase } from 'vitepress'
import Icon from './Icon.vue'
import Crumbs from './Crumbs.vue'

// --- Darslar to'plami ---
interface Lesson {
  id: string
  title: string
  desc: string
  text: string
}

interface Category {
  id: string
  title: string
  icon: string
  lessons: Lesson[]
}

const CATEGORIES: Category[] = [
  {
    id: 'basics',
    title: '10 barmoq asoslari',
    icon: 'keyboard',
    lessons: [
      {
        id: 'b1',
        title: '1-bosqich: F va J tayanch harflari',
        desc: "Ko'rsatkich barmoqlar bilan F va J harflarini hamda bo'sh joyni mashq qilish",
        text: 'f j fj jf ff jj fjf jfj fff jjj fj fj jf jf ff jj ff jj fjf jfj f j f j ff jj fj jf'
      },
      {
        id: 'b2',
        title: '2-bosqich: D va K qo\'shilishi',
        desc: "O'rta barmoqlar: D va K harflari",
        text: 'd k dk kd fd jk df kj fdk jkd dkf kjd ff jj dd kk fjdk jdfk dkk fdd jkd fkd dk kd'
      },
      {
        id: 'b3',
        title: '3-bosqich: Asosiy qator (Home Row)',
        desc: 'A, S, D, F, G, H, J, K, L, ; barcha markaziy qator harflari',
        text: 'asdf hjkl asdfg hjkl; ghaf dakl sash fash flash glad half shall slag flask glass glad fall dash'
      },
      {
        id: 'b4',
        title: '4-bosqich: Yuqori qator (Chap qo\'l)',
        desc: 'Q, W, E, R, T harflari va asosiy qator bilan uyg\'unlik',
        text: 'qwer rewq wert trew qwa swer grew water tree wear rate treat great sweat tweet raw war'
      },
      {
        id: 'b5',
        title: '5-bosqich: Yuqori qator (O\'ng qo\'l)',
        desc: 'Y, U, I, O, P harflari',
        text: 'yuio poiu yui oip uio poi you out put pop loop pool pillow pull open look plot point'
      },
      {
        id: 'b6',
        title: '6-bosqich: To\'liq yuqori va asosiy qator',
        desc: 'Yuqori va o\'rta qator so\'zlari',
        text: 'the quick brown type write loop power user guide write project simple file queue flow logic speed'
      },
      {
        id: 'b7',
        title: '7-bosqich: Quyi qator (Z, X, C, V, B, N, M)',
        desc: 'Pastki qator harflari',
        text: 'zxc vbn mnb vcx zxcv bnm box mix van cab ban man bin nom com net zoom view back next'
      },
      {
        id: 'b8',
        title: '8-bosqich: Barcha harflar va tinish belgilari',
        desc: 'To\'liq klaviatura bo\'ylab matnlar',
        text: 'salom dunyo. axv mentor platformasida tez yozishni o\'rganamiz. har bir barmoq o\'z o\'rnida bo\'lishi shart.'
      },
      {
        id: 'b9',
        title: '9-bosqich: Raqamlar va belgilar',
        desc: '1234567890 hamda asosiy tinish belgilari',
        text: 'kod 102 dars, 2026 yil, 8-sinf, 9-sinf, 10-sinf, 11-sinf. tezlik: 45 wpm, aniqlik: 98%!'
      }
    ]
  },
  {
    id: 'code',
    title: 'Dasturchilar kodi',
    icon: 'code',
    lessons: [
      {
        id: 'c1',
        title: 'Python sintaksisi',
        desc: 'def, for, if, print va Python konstruktsiyalari',
        text: 'def hisobla(a, b):\n    natija = a + b\n    for i in range(10):\n        print(f"Index: {i}, Qiymat: {natija}")\n    return natija'
      },
      {
        id: 'c2',
        title: 'JavaScript / TypeScript',
        desc: 'const, function, arrow functions va metodlar',
        text: 'const filterUsers = async (users) => {\n  const active = users.filter(u => u.isActive);\n  console.log("Faol foydalanuvchilar:", active.length);\n  return active;\n};'
      },
      {
        id: 'c3',
        title: 'HTML va Web teglari',
        desc: 'Teglar, atributlar va sinflar',
        text: '<div class="card-wrapper">\n  <h2 id="main-title">Darslar</h2>\n  <button class="btn btn-primary" onclick="start()">Boshlash</button>\n</div>'
      },
      {
        id: 'c4',
        title: 'SQL so\'rovlari',
        desc: 'SELECT, FROM, WHERE, JOIN va GROUP BY',
        text: 'SELECT u.id, u.username, COUNT(o.id) as total_orders\nFROM users u\nLEFT JOIN orders o ON u.id = o.user_id\nWHERE u.status = "active"\nGROUP BY u.id\nORDER BY total_orders DESC;'
      },
      {
        id: 'c5',
        title: 'Qavslar va maxsus simvollar',
        desc: '{} [] () <> = == === != !== && || => -> ; :',
        text: '{ [ ( < "Hello" > ) ] } => { a: [1, 2, 3], b: (x === y && a != b) || (x >= 10 && y <= 20); }'
      }
    ]
  },
  {
    id: 'words',
    title: 'IT atamalari va matnlar',
    icon: 'book-open',
    lessons: [
      {
        id: 'w1',
        title: 'O\'zbekcha IT atamalari',
        desc: 'Dasturlashda ko\'p uchraydigan so\'zlar',
        text: 'o\'zgaruvchi funksiya massiv obyekt sikl shart algoritm kompilyator rekursiya interfeys xotira ma\'lumotlar bazasi arxitektura'
      },
      {
        id: 'w2',
        title: 'English Programming Keywords',
        desc: 'Dasturlashda eng ko\'p ishlatiladigan inglizcha kalit so\'zlar',
        text: 'function return import export class interface async await const let var boolean string number array object promise resolve reject'
      },
      {
        id: 'w3',
        title: 'Dasturchilar qoidasi va aforizmlar',
        desc: 'Motivatsion IT iqtiboslar',
        text: 'Dasturlash — bu kompyuterga nima qilishni aytish emas, balki boshqa dasturchiga o\'z fikringizni tushuntirish san\'atidir. Har kuni kod yozing va o\'sing.'
      }
    ]
  },
  {
    id: 'custom',
    title: 'O\'z matningiz',
    icon: 'sparkles',
    lessons: [
      {
        id: 'custom_1',
        title: 'Erkin matn',
        desc: 'O\'zingiz xohlagan matnni nusxalab joylashtiring va mashq qiling',
        text: 'Bu yerga o\'zingiz xohlagan matnni yozing yoki paste qiling...'
      }
    ]
  }
]

// --- State ---
const activeCategory = ref<string>('basics')
const activeLessonId = ref<string>('b1')
const showLessonModal = ref<boolean>(false)
const customTextInput = ref<string>('')
const isCustomMode = computed(() => activeCategory.value === 'custom')

const currentCategory = computed(() => CATEGORIES.find(c => c.id === activeCategory.value) || CATEGORIES[0])
const currentLesson = computed(() => {
  if (isCustomMode.value) {
    return {
      id: 'custom_1',
      title: 'O\'z matningiz',
      desc: 'Kiritilgan matn bo\'yicha mashq',
      text: customTextInput.value.trim() || 'Bu yerga mashq qilmoqchi bo\'lgan matningizni kiriting.'
    }
  }
  return currentCategory.value.lessons.find(l => l.id === activeLessonId.value) || currentCategory.value.lessons[0]
})

// Typing state
const targetText = ref<string>('')
const currentIndex = ref<number>(0)
const userInput = ref<string>('')
const charStatus = ref<('pending' | 'correct' | 'error')[]>([])
const isStarted = ref<boolean>(false)
const isFinished = ref<boolean>(false)
const startTime = ref<number | null>(null)
const endTime = ref<number | null>(null)
const errorCount = ref<number>(0)
const totalKeystrokes = ref<number>(0)
const soundEnabled = ref<boolean>(true)
const showKeyboard = ref<boolean>(true)
const pressedKey = ref<string | null>(null)

// Stats
const elapsedTimeSec = ref<number>(0)
let timerInterval: any = null

const wpm = computed(() => {
  if (elapsedTimeSec.value === 0) return 0
  const minutes = elapsedTimeSec.value / 60
  const correctChars = charStatus.value.filter(s => s === 'correct').length
  const words = correctChars / 5
  return Math.round(words / minutes)
})

const cpm = computed(() => {
  if (elapsedTimeSec.value === 0) return 0
  const minutes = elapsedTimeSec.value / 60
  const correctChars = charStatus.value.filter(s => s === 'correct').length
  return Math.round(correctChars / minutes)
})

const accuracy = computed(() => {
  if (totalKeystrokes.value === 0) return 100
  const correct = totalKeystrokes.value - errorCount.value
  return Math.max(0, Math.round((correct / totalKeystrokes.value) * 100))
})

const progressPct = computed(() => {
  if (!targetText.value.length) return 0
  return Math.round((currentIndex.value / targetText.value.length) * 100)
})

// Active character & needed finger
const currentChar = computed(() => {
  if (currentIndex.value < targetText.value.length) {
    return targetText.value[currentIndex.value]
  }
  return ''
})

// Finger mapping
interface FingerGuide {
  finger: string
  hand: 'left' | 'right'
  color: string
}

const FINGER_MAP: Record<string, FingerGuide> = {
  // Left Pinky
  '`': { finger: 'Chap jimjiloq', hand: 'left', color: '#e06c75' },
  '~': { finger: 'Chap jimjiloq', hand: 'left', color: '#e06c75' },
  '1': { finger: 'Chap jimjiloq', hand: 'left', color: '#e06c75' },
  '!': { finger: 'Chap jimjiloq', hand: 'left', color: '#e06c75' },
  'q': { finger: 'Chap jimjiloq', hand: 'left', color: '#e06c75' },
  'Q': { finger: 'Chap jimjiloq', hand: 'left', color: '#e06c75' },
  'a': { finger: 'Chap jimjiloq', hand: 'left', color: '#e06c75' },
  'A': { finger: 'Chap jimjiloq', hand: 'left', color: '#e06c75' },
  'z': { finger: 'Chap jimjiloq', hand: 'left', color: '#e06c75' },
  'Z': { finger: 'Chap jimjiloq', hand: 'left', color: '#e06c75' },
  // Left Ring
  '2': { finger: 'Chap nomsiz', hand: 'left', color: '#d19a66' },
  '@': { finger: 'Chap nomsiz', hand: 'left', color: '#d19a66' },
  'w': { finger: 'Chap nomsiz', hand: 'left', color: '#d19a66' },
  'W': { finger: 'Chap nomsiz', hand: 'left', color: '#d19a66' },
  's': { finger: 'Chap nomsiz', hand: 'left', color: '#d19a66' },
  'S': { finger: 'Chap nomsiz', hand: 'left', color: '#d19a66' },
  'x': { finger: 'Chap nomsiz', hand: 'left', color: '#d19a66' },
  'X': { finger: 'Chap nomsiz', hand: 'left', color: '#d19a66' },
  // Left Middle
  '3': { finger: 'Chap o\'rta', hand: 'left', color: '#e5c07b' },
  '#': { finger: 'Chap o\'rta', hand: 'left', color: '#e5c07b' },
  'e': { finger: 'Chap o\'rta', hand: 'left', color: '#e5c07b' },
  'E': { finger: 'Chap o\'rta', hand: 'left', color: '#e5c07b' },
  'd': { finger: 'Chap o\'rta', hand: 'left', color: '#e5c07b' },
  'D': { finger: 'Chap o\'rta', hand: 'left', color: '#e5c07b' },
  'c': { finger: 'Chap o\'rta', hand: 'left', color: '#e5c07b' },
  'C': { finger: 'Chap o\'rta', hand: 'left', color: '#e5c07b' },
  // Left Index
  '4': { finger: 'Chap ko\'rsatkich', hand: 'left', color: '#98c379' },
  '$': { finger: 'Chap ko\'rsatkich', hand: 'left', color: '#98c379' },
  '5': { finger: 'Chap ko\'rsatkich', hand: 'left', color: '#98c379' },
  '%': { finger: 'Chap ko\'rsatkich', hand: 'left', color: '#98c379' },
  'r': { finger: 'Chap ko\'rsatkich', hand: 'left', color: '#98c379' },
  'R': { finger: 'Chap ko\'rsatkich', hand: 'left', color: '#98c379' },
  't': { finger: 'Chap ko\'rsatkich', hand: 'left', color: '#98c379' },
  'T': { finger: 'Chap ko\'rsatkich', hand: 'left', color: '#98c379' },
  'f': { finger: 'Chap ko\'rsatkich', hand: 'left', color: '#98c379' },
  'F': { finger: 'Chap ko\'rsatkich', hand: 'left', color: '#98c379' },
  'g': { finger: 'Chap ko\'rsatkich', hand: 'left', color: '#98c379' },
  'G': { finger: 'Chap ko\'rsatkich', hand: 'left', color: '#98c379' },
  'v': { finger: 'Chap ko\'rsatkich', hand: 'left', color: '#98c379' },
  'V': { finger: 'Chap ko\'rsatkich', hand: 'left', color: '#98c379' },
  'b': { finger: 'Chap ko\'rsatkich', hand: 'left', color: '#98c379' },
  'B': { finger: 'Chap ko\'rsatkich', hand: 'left', color: '#98c379' },
  // Thumbs
  ' ': { finger: 'Katta barmoq (Space)', hand: 'right', color: '#c678dd' },
  // Right Index
  '6': { finger: 'O\'ng ko\'rsatkich', hand: 'right', color: '#56b6c2' },
  '^': { finger: 'O\'ng ko\'rsatkich', hand: 'right', color: '#56b6c2' },
  '7': { finger: 'O\'ng ko\'rsatkich', hand: 'right', color: '#56b6c2' },
  '&': { finger: 'O\'ng ko\'rsatkich', hand: 'right', color: '#56b6c2' },
  'y': { finger: 'O\'ng ko\'rsatkich', hand: 'right', color: '#56b6c2' },
  'Y': { finger: 'O\'ng ko\'rsatkich', hand: 'right', color: '#56b6c2' },
  'u': { finger: 'O\'ng ko\'rsatkich', hand: 'right', color: '#56b6c2' },
  'U': { finger: 'O\'ng ko\'rsatkich', hand: 'right', color: '#56b6c2' },
  'h': { finger: 'O\'ng ko\'rsatkich', hand: 'right', color: '#56b6c2' },
  'H': { finger: 'O\'ng ko\'rsatkich', hand: 'right', color: '#56b6c2' },
  'j': { finger: 'O\'ng ko\'rsatkich', hand: 'right', color: '#56b6c2' },
  'J': { finger: 'O\'ng ko\'rsatkich', hand: 'right', color: '#56b6c2' },
  'n': { finger: 'O\'ng ko\'rsatkich', hand: 'right', color: '#56b6c2' },
  'N': { finger: 'O\'ng ko\'rsatkich', hand: 'right', color: '#56b6c2' },
  'm': { finger: 'O\'ng ko\'rsatkich', hand: 'right', color: '#56b6c2' },
  'M': { finger: 'O\'ng ko\'rsatkich', hand: 'right', color: '#56b6c2' },
  // Right Middle
  '8': { finger: 'O\'ng o\'rta', hand: 'right', color: '#61afef' },
  '*': { finger: 'O\'ng o\'rta', hand: 'right', color: '#61afef' },
  'i': { finger: 'O\'ng o\'rta', hand: 'right', color: '#61afef' },
  'I': { finger: 'O\'ng o\'rta', hand: 'right', color: '#61afef' },
  'k': { finger: 'O\'ng o\'rta', hand: 'right', color: '#61afef' },
  'K': { finger: 'O\'ng o\'rta', hand: 'right', color: '#61afef' },
  ',': { finger: 'O\'ng o\'rta', hand: 'right', color: '#61afef' },
  '<': { finger: 'O\'ng o\'rta', hand: 'right', color: '#61afef' },
  // Right Ring
  '9': { finger: 'O\'ng nomsiz', hand: 'right', color: '#e5c07b' },
  '(': { finger: 'O\'ng nomsiz', hand: 'right', color: '#e5c07b' },
  'o': { finger: 'O\'ng nomsiz', hand: 'right', color: '#e5c07b' },
  'O': { finger: 'O\'ng nomsiz', hand: 'right', color: '#e5c07b' },
  'l': { finger: 'O\'ng nomsiz', hand: 'right', color: '#e5c07b' },
  'L': { finger: 'O\'ng nomsiz', hand: 'right', color: '#e5c07b' },
  '.': { finger: 'O\'ng nomsiz', hand: 'right', color: '#e5c07b' },
  '>': { finger: 'O\'ng nomsiz', hand: 'right', color: '#e5c07b' },
  // Right Pinky
  '0': { finger: 'O\'ng jimjiloq', hand: 'right', color: '#e06c75' },
  ')': { finger: 'O\'ng jimjiloq', hand: 'right', color: '#e06c75' },
  '-': { finger: 'O\'ng jimjiloq', hand: 'right', color: '#e06c75' },
  '_': { finger: 'O\'ng jimjiloq', hand: 'right', color: '#e06c75' },
  '=': { finger: 'O\'ng jimjiloq', hand: 'right', color: '#e06c75' },
  '+': { finger: 'O\'ng jimjiloq', hand: 'right', color: '#e06c75' },
  'p': { finger: 'O\'ng jimjiloq', hand: 'right', color: '#e06c75' },
  'P': { finger: 'O\'ng jimjiloq', hand: 'right', color: '#e06c75' },
  '[': { finger: 'O\'ng jimjiloq', hand: 'right', color: '#e06c75' },
  '{': { finger: 'O\'ng jimjiloq', hand: 'right', color: '#e06c75' },
  ']': { finger: 'O\'ng jimjiloq', hand: 'right', color: '#e06c75' },
  '}': { finger: 'O\'ng jimjiloq', hand: 'right', color: '#e06c75' },
  '\\': { finger: 'O\'ng jimjiloq', hand: 'right', color: '#e06c75' },
  '|': { finger: 'O\'ng jimjiloq', hand: 'right', color: '#e06c75' },
  ';': { finger: 'O\'ng jimjiloq', hand: 'right', color: '#e06c75' },
  ':': { finger: 'O\'ng jimjiloq', hand: 'right', color: '#e06c75' },
  '\'': { finger: 'O\'ng jimjiloq', hand: 'right', color: '#e06c75' },
  '"': { finger: 'O\'ng jimjiloq', hand: 'right', color: '#e06c75' },
  '/': { finger: 'O\'ng jimjiloq', hand: 'right', color: '#e06c75' },
  '?': { finger: 'O\'ng jimjiloq', hand: 'right', color: '#e06c75' },
  '\n': { finger: 'Enter (O\'ng jimjiloq)', hand: 'right', color: '#e06c75' }
}

const currentFingerGuide = computed<FingerGuide>(() => {
  const c = currentChar.value
  return FINGER_MAP[c] || { finger: 'Klaviatura', hand: 'left', color: 'var(--vp-c-brand-1)' }
})

// Keyboard rows definition
const KEYBOARD_ROWS = [
  [
    { key: '`', shift: '~', finger: 'lp', w: '1' },
    { key: '1', shift: '!', finger: 'lp', w: '1' },
    { key: '2', shift: '@', finger: 'lr', w: '1' },
    { key: '3', shift: '#', finger: 'lm', w: '1' },
    { key: '4', shift: '$', finger: 'li', w: '1' },
    { key: '5', shift: '%', finger: 'li', w: '1' },
    { key: '6', shift: '^', finger: 'ri', w: '1' },
    { key: '7', shift: '&', finger: 'ri', w: '1' },
    { key: '8', shift: '*', finger: 'rm', w: '1' },
    { key: '9', shift: '(', finger: 'rr', w: '1' },
    { key: '0', shift: ')', finger: 'rp', w: '1' },
    { key: '-', shift: '_', finger: 'rp', w: '1' },
    { key: '=', shift: '+', finger: 'rp', w: '1' },
    { key: 'Backspace', label: '⌫', finger: 'rp', w: '1.8', code: 'Backspace' }
  ],
  [
    { key: 'Tab', label: 'Tab', finger: 'lp', w: '1.5', code: 'Tab' },
    { key: 'q', shift: 'Q', finger: 'lp', w: '1' },
    { key: 'w', shift: 'W', finger: 'lr', w: '1' },
    { key: 'e', shift: 'E', finger: 'lm', w: '1' },
    { key: 'r', shift: 'R', finger: 'li', w: '1' },
    { key: 't', shift: 'T', finger: 'li', w: '1' },
    { key: 'y', shift: 'Y', finger: 'ri', w: '1' },
    { key: 'u', shift: 'U', finger: 'ri', w: '1' },
    { key: 'i', shift: 'I', finger: 'rm', w: '1' },
    { key: 'o', shift: 'O', finger: 'rr', w: '1' },
    { key: 'p', shift: 'P', finger: 'rp', w: '1' },
    { key: '[', shift: '{', finger: 'rp', w: '1' },
    { key: ']', shift: '}', finger: 'rp', w: '1' },
    { key: '\\', shift: '|', finger: 'rp', w: '1.3' }
  ],
  [
    { key: 'CapsLock', label: 'Caps', finger: 'lp', w: '1.8', code: 'CapsLock' },
    { key: 'a', shift: 'A', finger: 'lp', w: '1' },
    { key: 's', shift: 'S', finger: 'lr', w: '1' },
    { key: 'd', shift: 'D', finger: 'lm', w: '1' },
    { key: 'f', shift: 'F', finger: 'li', w: '1', home: true },
    { key: 'g', shift: 'G', finger: 'li', w: '1' },
    { key: 'h', shift: 'H', finger: 'ri', w: '1' },
    { key: 'j', shift: 'J', finger: 'ri', w: '1', home: true },
    { key: 'k', shift: 'K', finger: 'rm', w: '1' },
    { key: 'l', shift: 'L', finger: 'rr', w: '1' },
    { key: ';', shift: ':', finger: 'rp', w: '1' },
    { key: '\'', shift: '"', finger: 'rp', w: '1' },
    { key: 'Enter', label: 'Enter ↵', finger: 'rp', w: '2.0', code: 'Enter' }
  ],
  [
    { key: 'ShiftLeft', label: 'Shift', finger: 'lp', w: '2.4', code: 'ShiftLeft' },
    { key: 'z', shift: 'Z', finger: 'lp', w: '1' },
    { key: 'x', shift: 'X', finger: 'lr', w: '1' },
    { key: 'c', shift: 'C', finger: 'lm', w: '1' },
    { key: 'v', shift: 'V', finger: 'li', w: '1' },
    { key: 'b', shift: 'B', finger: 'li', w: '1' },
    { key: 'n', shift: 'N', finger: 'ri', w: '1' },
    { key: 'm', shift: 'M', finger: 'ri', w: '1' },
    { key: ',', shift: '<', finger: 'rm', w: '1' },
    { key: '.', shift: '>', finger: 'rr', w: '1' },
    { key: '/', shift: '?', finger: 'rp', w: '1' },
    { key: 'ShiftRight', label: 'Shift', finger: 'rp', w: '2.4', code: 'ShiftRight' }
  ],
  [
    { key: 'Ctrl', label: 'Ctrl', finger: 'lp', w: '1.5', code: 'ControlLeft' },
    { key: 'Alt', label: 'Alt', finger: 'lt', w: '1.2', code: 'AltLeft' },
    { key: ' ', label: 'Bo\'sh joy (Space)', finger: 'thumb', w: '7.5', code: 'Space' },
    { key: 'Alt', label: 'Alt', finger: 'rt', w: '1.2', code: 'AltRight' },
    { key: 'Ctrl', label: 'Ctrl', finger: 'rp', w: '1.5', code: 'ControlRight' }
  ]
]

// Determine if a key is currently target
const isTargetKey = (k: any) => {
  const c = currentChar.value
  if (!c) return false
  if (k.key === ' ' && c === ' ') return true
  if (k.code === 'Enter' && c === '\n') return true
  if (k.key === c || k.shift === c) return true
  return false
}

const isTargetShift = computed(() => {
  const c = currentChar.value
  if (!c) return false
  for (const row of KEYBOARD_ROWS) {
    for (const k of row) {
      if (k.shift === c && k.key !== c) return true
    }
  }
  return false
})

// Web Audio API Sound Synthesizer
let audioCtx: AudioContext | null = null

const initAudio = () => {
  if (!audioCtx && typeof window !== 'undefined') {
    const AudioContextClass = window.AudioContext || (window as any).webkitAudioContext
    if (AudioContextClass) {
      audioCtx = new AudioContextClass()
    }
  }
  if (audioCtx && audioCtx.state === 'suspended') {
    audioCtx.resume()
  }
}

const playKeySound = (isError = false, isSpace = false) => {
  if (!soundEnabled.value) return
  initAudio()
  if (!audioCtx) return

  try {
    const osc = audioCtx.createOscillator()
    const gain = audioCtx.createGain()
    osc.connect(gain)
    gain.connect(audioCtx.destination)

    const now = audioCtx.currentTime

    if (isError) {
      osc.type = 'sawtooth'
      osc.frequency.setValueAtTime(140, now)
      osc.frequency.exponentialRampToValueAtTime(70, now + 0.12)
      gain.gain.setValueAtTime(0.2, now)
      gain.gain.exponentialRampToValueAtTime(0.01, now + 0.12)
      osc.start(now)
      osc.stop(now + 0.12)
    } else {
      osc.type = 'sine'
      const freq = isSpace ? 380 : 550 + Math.random() * 80
      osc.frequency.setValueAtTime(freq, now)
      osc.frequency.exponentialRampToValueAtTime(120, now + 0.04)
      gain.gain.setValueAtTime(0.15, now)
      gain.gain.exponentialRampToValueAtTime(0.01, now + 0.04)
      osc.start(now)
      osc.stop(now + 0.04)
    }
  } catch (e) {}
}

const playVictorySound = () => {
  if (!soundEnabled.value) return
  initAudio()
  if (!audioCtx) return

  try {
    const notes = [440, 554.37, 659.25, 880]
    notes.forEach((freq, idx) => {
      const osc = audioCtx!.createOscillator()
      const gain = audioCtx!.createGain()
      osc.connect(gain)
      gain.connect(audioCtx!.destination)
      const now = audioCtx!.currentTime + idx * 0.09
      osc.type = 'triangle'
      osc.frequency.setValueAtTime(freq, now)
      gain.gain.setValueAtTime(0.2, now)
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.3)
      osc.start(now)
      osc.stop(now + 0.3)
    })
  } catch (e) {}
}

// Reset / Load Lesson
const resetLesson = () => {
  if (timerInterval) clearInterval(timerInterval)
  targetText.value = currentLesson.value.text
  currentIndex.value = 0
  userInput.value = ''
  charStatus.value = new Array(targetText.value.length).fill('pending')
  isStarted.value = false
  isFinished.value = false
  startTime.value = null
  endTime.value = null
  errorCount.value = 0
  totalKeystrokes.value = 0
  elapsedTimeSec.value = 0
  pressedKey.value = null
}

const selectCategory = (catId: string) => {
  activeCategory.value = catId
  if (catId !== 'custom') {
    activeLessonId.value = CATEGORIES.find(c => c.id === catId)?.lessons[0]?.id || ''
  }
  showLessonModal.value = false
  resetLesson()
}

const selectLesson = (lesId: string) => {
  activeLessonId.value = lesId
  showLessonModal.value = false
  resetLesson()
}

// Key handler
const handleKeyDown = (e: KeyboardEvent) => {
  // If modal is open, ignore
  if (showLessonModal.value) return

  if (['Shift', 'Control', 'Alt', 'Meta', 'CapsLock', 'Tab'].includes(e.key)) {
    pressedKey.value = e.key
    return
  }

  if (e.key === ' ' || e.key === 'Enter') {
    e.preventDefault()
  }

  if (isFinished.value) return

  if (!isStarted.value) {
    isStarted.value = true
    startTime.value = Date.now()
    timerInterval = setInterval(() => {
      if (startTime.value) {
        elapsedTimeSec.value = Math.max(1, Math.round((Date.now() - startTime.value) / 1000))
      }
    }, 500)
  }

  totalKeystrokes.value++
  pressedKey.value = e.key

  const expected = targetText.value[currentIndex.value]
  let inputChar = e.key
  if (e.key === 'Enter') inputChar = '\n'

  if (inputChar === expected) {
    charStatus.value[currentIndex.value] = 'correct'
    currentIndex.value++
    playKeySound(false, inputChar === ' ')

    if (currentIndex.value >= targetText.value.length) {
      finishLesson()
    }
  } else {
    errorCount.value++
    charStatus.value[currentIndex.value] = 'error'
    playKeySound(true)
  }

  nextTick(() => {
    const activeEl = document.querySelector('.stamina-char.active')
    if (activeEl) {
      activeEl.scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' })
    }
  })
}

const handleKeyUp = () => {
  pressedKey.value = null
}

const finishLesson = () => {
  if (timerInterval) clearInterval(timerInterval)
  isFinished.value = true
  endTime.value = Date.now()
  if (startTime.value) {
    elapsedTimeSec.value = Math.max(1, Math.round((endTime.value - startTime.value) / 1000))
  }
  playVictorySound()

  if (typeof window !== 'undefined') {
    try {
      const records = JSON.parse(localStorage.getItem('axv_stamina_records') || '{}')
      const currentBest = records[currentLesson.value.id] || { wpm: 0, acc: 0 }
      if (wpm.value > currentBest.wpm) {
        records[currentLesson.value.id] = {
          wpm: wpm.value,
          cpm: cpm.value,
          acc: accuracy.value,
          date: new Date().toISOString()
        }
        localStorage.setItem('axv_stamina_records', JSON.stringify(records))
      }
    } catch (e) {}
  }
}

const nextLesson = () => {
  const currentIdx = currentCategory.value.lessons.findIndex(l => l.id === activeLessonId.value)
  if (currentIdx >= 0 && currentIdx + 1 < currentCategory.value.lessons.length) {
    activeLessonId.value = currentCategory.value.lessons[currentIdx + 1].id
    resetLesson()
  } else {
    const catIdx = CATEGORIES.findIndex(c => c.id === activeCategory.value)
    if (catIdx >= 0 && catIdx + 1 < CATEGORIES.length) {
      selectCategory(CATEGORIES[catIdx + 1].id)
    } else {
      resetLesson()
    }
  }
}

const starsCount = computed(() => {
  if (accuracy.value >= 95 && wpm.value >= 40) return 3
  if (accuracy.value >= 85 && wpm.value >= 25) return 2
  return 1
})

onMounted(() => {
  resetLesson()
  if (typeof window !== 'undefined') {
    window.addEventListener('keydown', handleKeyDown)
    window.addEventListener('keyup', handleKeyUp)
  }
})

onUnmounted(() => {
  if (timerInterval) clearInterval(timerInterval)
  if (typeof window !== 'undefined') {
    window.removeEventListener('keydown', handleKeyDown)
    window.removeEventListener('keyup', handleKeyUp)
  }
})

watch(() => currentLesson.value, () => {
  resetLesson()
})
</script>

<template>
  <div class="stamina-screen">
    <!-- COMPACT TOP BAR: SELECTOR + HUD METRICS + ACTIONS -->
    <header class="stamina-top-bar">
      <!-- Lesson selector trigger -->
      <button class="stamina-btn-select" @click="showLessonModal = true">
        <span class="sbs-cat"><Icon :name="currentCategory.icon" /> {{ currentCategory.title }}</span>
        <span class="sbs-div">·</span>
        <span class="sbs-les">{{ currentLesson.title }}</span>
        <span class="sbs-arrow">▾</span>
      </button>

      <!-- Live HUD Metrics -->
      <div class="stamina-hud">
        <div class="hud-item">
          <span class="hud-num">{{ wpm }}</span>
          <span class="hud-lbl">WPM</span>
        </div>
        <div class="hud-item">
          <span class="hud-num" :style="{ color: accuracy >= 95 ? 'var(--ax-good)' : 'inherit' }">{{ accuracy }}%</span>
          <span class="hud-lbl">Aniqlik</span>
        </div>
        <div class="hud-item">
          <span class="hud-num">{{ Math.floor(elapsedTimeSec / 60) }}:{{ (elapsedTimeSec % 60).toString().padStart(2, '0') }}</span>
          <span class="hud-lbl">Vaqt</span>
        </div>
        <div class="hud-item">
          <span class="hud-num error-num">{{ errorCount }}</span>
          <span class="hud-lbl">Xato</span>
        </div>
      </div>

      <!-- Quick Action Controls -->
      <div class="stamina-actions">
        <button
          class="icon-btn"
          :class="{ active: soundEnabled }"
          @click="soundEnabled = !soundEnabled"
          :title="soundEnabled ? 'Ovozni o\'chirish' : 'Ovozni yoqish'"
        >
          <Icon :name="soundEnabled ? 'volume-2' : 'volume-x'" />
        </button>
        <button
          class="icon-btn"
          :class="{ active: showKeyboard }"
          @click="showKeyboard = !showKeyboard"
          :title="showKeyboard ? 'Klaviaturani yashirish' : 'Klaviaturani ko\'rsatish'"
        >
          <Icon name="keyboard" />
        </button>
        <button class="icon-btn" @click="resetLesson" title="Qayta boshlash">
          <Icon name="rotate-ccw" />
        </button>
      </div>
    </header>

    <!-- SLIM PROGRESS BAR -->
    <div class="stamina-progress-bar">
      <div class="spb-inner" :style="{ width: progressPct + '%' }"></div>
    </div>

    <!-- MAIN TYPING STREAM BOX (LARGE, CRISP, FOCUSED) -->
    <div class="stamina-stream-box" tabindex="0">
      <div class="stream-inner">
        <span
          v-for="(char, idx) in targetText"
          :key="idx"
          class="stamina-char"
          :class="[
            charStatus[idx],
            { active: idx === currentIndex },
            { space: char === ' ' },
            { newline: char === '\n' }
          ]"
        >
          <template v-if="char === ' '">&nbsp;</template>
          <template v-else-if="char === '\n'">↵<br /></template>
          <template v-else>{{ char }}</template>
        </span>
      </div>
      <div v-if="!isStarted && !isFinished" class="stream-hint">
        <Icon name="play" /> Tugmalarni bosib yozishni boshlang...
      </div>
    </div>

    <!-- FINGER & KEY HELPER BAR -->
    <div class="stamina-finger-guide">
      <div class="fg-info">
        <span class="fg-dot" :style="{ background: currentFingerGuide.color }"></span>
        <span class="fg-text">
          Barmoq: <b>{{ currentFingerGuide.finger }}</b>
          <template v-if="isTargetShift"> (Shift bilan)</template>
        </span>
      </div>
      <div class="fg-target">
        Bosiladigan belgi:
        <span class="target-badge">
          {{ currentChar === ' ' ? 'Space (Bo\'sh joy)' : currentChar === '\n' ? 'Enter ↵' : currentChar }}
        </span>
      </div>
    </div>

    <!-- ERGONOMIC ON-SCREEN VIRTUAL KEYBOARD -->
    <div v-if="showKeyboard" class="stamina-keyboard">
      <div v-for="(row, rIdx) in KEYBOARD_ROWS" :key="rIdx" class="kb-row">
        <div
          v-for="k in row"
          :key="k.key"
          class="kb-key"
          :class="[
            `finger-${k.finger}`,
            { 'key-target': isTargetKey(k) },
            { 'key-shift-target': isTargetShift && (k.code === 'ShiftLeft' || k.code === 'ShiftRight') },
            { 'key-pressed': pressedKey === k.key || pressedKey === k.code },
            { 'key-home': k.home }
          ]"
          :style="{ flex: k.w || '1' }"
        >
          <div class="k-top" v-if="k.shift && k.shift !== k.key">{{ k.shift }}</div>
          <div class="k-main">{{ k.label || k.key.toUpperCase() }}</div>
          <div class="k-bump" v-if="k.home">_</div>
        </div>
      </div>
    </div>

    <!-- LESSON SELECTOR MODAL -->
    <div v-if="showLessonModal" class="stamina-modal-overlay" @click.self="showLessonModal = false">
      <div class="stamina-lesson-modal">
        <div class="slm-header">
          <h2><Icon name="keyboard" /> Darslar va mashqlar</h2>
          <button class="slm-close" @click="showLessonModal = false">✕</button>
        </div>

        <div class="slm-cats">
          <button
            v-for="cat in CATEGORIES"
            :key="cat.id"
            class="slm-cat-tab"
            :class="{ active: activeCategory === cat.id }"
            @click="activeCategory = cat.id"
          >
            <Icon :name="cat.icon" />
            <span>{{ cat.title }}</span>
          </button>
        </div>

        <div class="slm-body">
          <div v-if="!isCustomMode" class="slm-lessons-grid">
            <button
              v-for="(les, idx) in currentCategory.lessons"
              :key="les.id"
              class="slm-lesson-card"
              :class="{ active: activeLessonId === les.id }"
              @click="selectLesson(les.id)"
            >
              <div class="slm-card-top">
                <span class="slm-idx">{{ idx + 1 }}</span>
                <span class="slm-title">{{ les.title }}</span>
              </div>
              <p class="slm-desc">{{ les.desc }}</p>
            </button>
          </div>

          <div v-else class="slm-custom-box">
            <label>O'zingiz xohlagan matnni kiriting:</label>
            <textarea
              v-model="customTextInput"
              placeholder="Matnni bu yerga paste qiling yoki yozing..."
              rows="5"
            ></textarea>
            <button class="btn btn-primary" @click="selectCategory('custom')">
              <Icon name="play" /> Matnni yuklash va boshlash
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- RESULTS MODAL -->
    <div v-if="isFinished" class="stamina-modal-overlay">
      <div class="stamina-modal">
        <div class="sm-header">
          <div class="sm-stars">
            <span v-for="s in 3" :key="s" class="star" :class="{ filled: s <= starsCount }">★</span>
          </div>
          <h2>Mashq yakunlandi!</h2>
          <p class="sm-sub">
            {{ starsCount === 3 ? 'Ajoyib natija! Professional tezlik.' : starsCount === 2 ? 'Juda yaxshi! Tezlikni oshirishda davom eting.' : 'Yaxshi boshlanish! Ko\'proq mashq qiling.' }}
          </p>
        </div>

        <div class="sm-grid">
          <div class="sm-stat">
            <span class="sm-lbl">Tezlik (WPM)</span>
            <span class="sm-val highlight">{{ wpm }}</span>
          </div>
          <div class="sm-stat">
            <span class="sm-lbl">Belgi/daq (CPM)</span>
            <span class="sm-val">{{ cpm }}</span>
          </div>
          <div class="sm-stat">
            <span class="sm-lbl">Aniqlik</span>
            <span class="sm-val" :style="{ color: accuracy >= 95 ? 'var(--ax-good)' : 'inherit' }">{{ accuracy }}%</span>
          </div>
          <div class="sm-stat">
            <span class="sm-lbl">Vaqt</span>
            <span class="sm-val">{{ Math.floor(elapsedTimeSec / 60) }}:{{ (elapsedTimeSec % 60).toString().padStart(2, '0') }}</span>
          </div>
          <div class="sm-stat">
            <span class="sm-lbl">Xatolar</span>
            <span class="sm-val">{{ errorCount }}</span>
          </div>
          <div class="sm-stat">
            <span class="sm-lbl">Jami tugmalar</span>
            <span class="sm-val">{{ totalKeystrokes }}</span>
          </div>
        </div>

        <div class="sm-actions">
          <button class="btn btn-ghost btn-lg" @click="resetLesson">
            <Icon name="rotate-ccw" /> Qaytadan urinish
          </button>
          <button class="btn btn-primary btn-lg" @click="nextLesson">
            Keyingi bosqich <Icon name="arrow-right" />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.stamina-screen {
  max-width: 980px;
  margin: 0 auto;
  padding: 4px 12px 16px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

/* TOP BAR */
.stamina-top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  background: var(--ax-card);
  border: 1px solid var(--ax-line);
  border-radius: 12px;
  padding: 8px 14px;
}

.stamina-btn-select {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: var(--vp-c-bg);
  border: 1px solid var(--ax-line);
  padding: 6px 14px;
  border-radius: 8px;
  color: var(--vp-c-text-1);
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s ease;
}

.stamina-btn-select:hover {
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
}

.sbs-cat {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  color: var(--vp-c-brand-1);
}

.sbs-div {
  opacity: 0.4;
}

.sbs-les {
  max-width: 220px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sbs-arrow {
  opacity: 0.6;
  font-size: 0.8rem;
}

/* HUD METRICS */
.stamina-hud {
  display: flex;
  align-items: center;
  gap: 16px;
}

.hud-item {
  display: flex;
  align-items: baseline;
  gap: 5px;
}

.hud-num {
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--vp-c-text-1);
  line-height: 1;
}

.hud-lbl {
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--vp-c-text-2);
}

.error-num {
  color: #e06c75;
}

/* ACTIONS */
.stamina-actions {
  display: flex;
  align-items: center;
  gap: 6px;
}

.icon-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 34px;
  height: 34px;
  border-radius: 8px;
  background: var(--vp-c-bg);
  border: 1px solid var(--ax-line);
  color: var(--vp-c-text-2);
  cursor: pointer;
  transition: all 0.15s ease;
}

.icon-btn:hover {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
}

.icon-btn.active {
  background: var(--vp-c-brand-soft);
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
}

/* PROGRESS */
.stamina-progress-bar {
  height: 4px;
  background: var(--ax-line);
  border-radius: 999px;
  overflow: hidden;
}

.spb-inner {
  height: 100%;
  background: var(--ax-grad);
  transition: width 0.15s ease;
}

/* TYPING STREAM BOX (FOCUSED & CLEAN) */
.stamina-stream-box {
  position: relative;
  background: var(--vp-c-bg-alt);
  border: 2px solid var(--ax-line);
  border-radius: 14px;
  padding: 18px 24px;
  min-height: 110px;
  max-height: 140px;
  overflow-y: auto;
  outline: none;
  cursor: text;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.stamina-stream-box:focus {
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 0 0 3px var(--vp-c-brand-soft);
}

.stream-inner {
  font-family: 'Consolas', 'Fira Code', 'JetBrains Mono', 'Courier New', monospace;
  font-size: 1.55rem;
  line-height: 1.7;
  letter-spacing: 0.05em;
  white-space: pre-wrap;
  word-break: break-word;
}

.stamina-char {
  position: relative;
  border-radius: 3px;
  transition: background-color 0.1s, color 0.1s;
}

.stamina-char.pending {
  color: var(--vp-c-text-2);
  opacity: 0.75;
}

.stamina-char.correct {
  color: var(--ax-good);
}

.stamina-char.error {
  color: #fff;
  background: #e06c75;
  border-radius: 3px;
}

.stamina-char.active {
  color: var(--vp-c-text-1);
  background: rgba(0, 102, 184, 0.25);
  border-bottom: 3px solid var(--vp-c-brand-1);
  font-weight: 700;
  animation: charPulse 0.9s infinite alternate;
}

.stamina-char.active.space {
  background: rgba(0, 102, 184, 0.35);
  display: inline-block;
  min-width: 0.55em;
}

.stream-hint {
  position: absolute;
  right: 14px;
  bottom: 8px;
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.8rem;
  color: var(--vp-c-text-3);
  pointer-events: none;
}

@keyframes charPulse {
  from { box-shadow: 0 0 0 rgba(0, 102, 184, 0); }
  to { box-shadow: 0 0 6px rgba(0, 102, 184, 0.6); }
}

/* FINGER GUIDE */
.stamina-finger-guide {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: var(--ax-card);
  border: 1px solid var(--ax-line);
  border-radius: 10px;
  padding: 6px 14px;
  font-size: 0.88rem;
}

.fg-info {
  display: flex;
  align-items: center;
  gap: 8px;
}

.fg-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  display: inline-block;
}

.fg-target {
  display: flex;
  align-items: center;
  gap: 6px;
  color: var(--vp-c-text-2);
}

.target-badge {
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
  padding: 2px 8px;
  border-radius: 6px;
  font-weight: 700;
  font-family: monospace;
}

/* KEYBOARD */
.stamina-keyboard {
  background: var(--ax-card);
  border: 1px solid var(--ax-line);
  border-radius: 14px;
  padding: 10px;
  display: flex;
  flex-direction: column;
  gap: 5px;
  user-select: none;
  box-shadow: var(--ax-shadow);
}

.kb-row {
  display: flex;
  gap: 5px;
  justify-content: center;
}

.kb-key {
  position: relative;
  height: 40px;
  background: var(--vp-c-bg);
  border: 1px solid var(--ax-line);
  border-radius: 6px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--vp-c-text-1);
  box-shadow: 0 1.5px 0 var(--ax-line);
  transition: all 0.08s ease;
}

.k-top {
  font-size: 0.6rem;
  opacity: 0.55;
  margin-bottom: -2px;
}

.k-main {
  font-size: 0.8rem;
}

.k-bump {
  position: absolute;
  bottom: 1px;
  font-size: 0.8rem;
  font-weight: bold;
  opacity: 0.6;
}

.finger-lp, .finger-rp { border-bottom: 2.5px solid #e06c75; }
.finger-lr, .finger-rr { border-bottom: 2.5px solid #d19a66; }
.finger-lm, .finger-rm { border-bottom: 2.5px solid #e5c07b; }
.finger-li, .finger-ri { border-bottom: 2.5px solid #98c379; }
.finger-thumb { border-bottom: 2.5px solid #c678dd; }

.key-target {
  background: linear-gradient(135deg, #0e70c0, #2392dc) !important;
  color: #fff !important;
  border-color: #0e70c0 !important;
  transform: translateY(-2px);
  box-shadow: 0 3px 8px rgba(14, 112, 192, 0.45) !important;
  animation: keyPulse 0.8s infinite alternate;
}

.key-shift-target {
  background: linear-gradient(135deg, #af00db, #c586c0) !important;
  color: #fff !important;
  border-color: #af00db !important;
  animation: keyPulse 0.8s infinite alternate;
}

.key-pressed {
  transform: translateY(1.5px) !important;
  box-shadow: 0 0 0 transparent !important;
  background: var(--vp-c-brand-soft) !important;
}

@keyframes keyPulse {
  from { filter: brightness(1); }
  to { filter: brightness(1.2); }
}

/* LESSON SELECTOR MODAL */
.stamina-modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(6px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 16px;
}

.stamina-lesson-modal {
  background: var(--vp-c-bg);
  border: 1px solid var(--ax-line);
  border-radius: 18px;
  width: 100%;
  max-width: 680px;
  max-height: 85vh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
  animation: modalPop 0.2s ease-out;
}

.slm-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 20px;
  border-bottom: 1px solid var(--ax-line);
}

.slm-header h2 {
  font-size: 1.25rem;
  font-weight: 700;
  margin: 0;
  display: flex;
  align-items: center;
  gap: 8px;
}

.slm-close {
  background: transparent;
  border: none;
  font-size: 1.2rem;
  color: var(--vp-c-text-2);
  cursor: pointer;
  padding: 4px 8px;
  border-radius: 6px;
}

.slm-close:hover {
  background: var(--ax-card-hi);
  color: var(--vp-c-text-1);
}

.slm-cats {
  display: flex;
  gap: 6px;
  padding: 12px 20px;
  border-bottom: 1px solid var(--ax-line);
  background: var(--ax-card);
  overflow-x: auto;
}

.slm-cat-tab {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  border-radius: 8px;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--vp-c-text-2);
  background: transparent;
  border: 1px solid transparent;
  cursor: pointer;
  white-space: nowrap;
}

.slm-cat-tab:hover {
  background: var(--ax-card-hi);
  color: var(--vp-c-text-1);
}

.slm-cat-tab.active {
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
  border-color: rgba(0, 102, 184, 0.25);
}

.slm-body {
  padding: 18px 20px;
  overflow-y: auto;
  max-height: 55vh;
}

.slm-lessons-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 10px;
}

.slm-lesson-card {
  text-align: left;
  background: var(--ax-card);
  border: 1px solid var(--ax-line);
  border-radius: 10px;
  padding: 12px 14px;
  cursor: pointer;
  transition: all 0.15s ease;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.slm-lesson-card:hover {
  border-color: var(--vp-c-brand-1);
  background: var(--ax-card-hi);
  transform: translateY(-1px);
}

.slm-lesson-card.active {
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
}

.slm-card-top {
  display: flex;
  align-items: center;
  gap: 8px;
}

.slm-idx {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
  font-size: 0.75rem;
  font-weight: 700;
}

.slm-title {
  font-weight: 700;
  font-size: 0.9rem;
  color: var(--vp-c-text-1);
}

.slm-desc {
  font-size: 0.78rem;
  color: var(--vp-c-text-2);
  margin: 0;
  line-height: 1.35;
}

.slm-custom-box {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.slm-custom-box textarea {
  width: 100%;
  padding: 12px;
  border-radius: 8px;
  border: 1px solid var(--ax-line);
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  font-family: inherit;
  font-size: 0.95rem;
}

/* RESULTS MODAL */
.stamina-modal {
  background: var(--vp-c-bg);
  border: 1px solid var(--ax-line);
  border-radius: 20px;
  padding: 28px;
  max-width: 480px;
  width: 100%;
  text-align: center;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.5);
  animation: modalPop 0.25s ease-out;
}

@keyframes modalPop {
  from { transform: scale(0.92); opacity: 0; }
  to { transform: scale(1); opacity: 1; }
}

.sm-stars {
  display: flex;
  justify-content: center;
  gap: 6px;
  font-size: 2rem;
  margin-bottom: 6px;
}

.sm-stars .star {
  color: var(--ax-line);
}

.sm-stars .star.filled {
  color: #e5c07b;
}

.sm-header h2 {
  font-size: 1.5rem;
  font-weight: 800;
  margin: 0 0 4px;
}

.sm-sub {
  color: var(--vp-c-text-2);
  margin: 0 0 16px;
  font-size: 0.9rem;
}

.sm-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
  background: var(--ax-card);
  border: 1px solid var(--ax-line);
  border-radius: 12px;
  padding: 14px;
  margin-bottom: 20px;
}

.sm-stat {
  display: flex;
  flex-direction: column;
}

.sm-lbl {
  font-size: 0.7rem;
  color: var(--vp-c-text-2);
  margin-bottom: 3px;
}

.sm-val {
  font-size: 1.2rem;
  font-weight: 800;
}

.sm-val.highlight {
  color: var(--vp-c-brand-1);
}

.sm-actions {
  display: flex;
  justify-content: center;
  gap: 10px;
  flex-wrap: wrap;
}

@media (max-width: 768px) {
  .stamina-keyboard {
    display: none;
  }
  .stream-inner {
    font-size: 1.2rem;
  }
  .stamina-hud {
    gap: 10px;
  }
}
</style>
