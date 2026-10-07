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
    id: 'tracks',
    title: 'Yo\'nalishlar kodi',
    icon: 'laptop',
    lessons: [
      {
        id: 'tr_web',
        title: 'Web Full-stack (React & Vue)',
        desc: 'React hooklari, Vue reaktivligi va zamonaviy front-end',
        text: 'const [items, setItems] = useState([]);\nuseEffect(() => {\n  fetchData().then(data => setItems(data));\n}, []);\nreturn <div className="card-list">{items.map(item => <Card key={item.id} {...item} />)}</div>;'
      },
      {
        id: 'tr_backend',
        title: 'Back-end & DevOps (FastAPI & Docker)',
        desc: 'FastAPI marshrutlari, async funksiyalar va Docker',
        text: 'app = FastAPI(title="AXV Backend API", version="1.0")\n\n@app.get("/api/v1/lessons/{lesson_id}")\nasync def read_lesson(lesson_id: int, db: Session = Depends(get_db)):\n    lesson = await db.query(Lesson).filter(Lesson.id == lesson_id).first()\n    return lesson'
      },
      {
        id: 'tr_android',
        title: 'Android dasturlash (Kotlin & Compose)',
        desc: 'Kotlin funksiyalari va Jetpack Compose interfeysi',
        text: '@Composable\nfun StudentCard(name: String, progress: Int) {\n    Column(modifier = Modifier.padding(16.dp).fillMaxWidth()) {\n        Text(text = name, style = MaterialTheme.typography.titleLarge)\n        LinearProgressIndicator(progress = progress / 100f)\n    }\n}'
      },
      {
        id: 'tr_bi',
        title: 'BI & Ma\'lumotlar tahlili (Pandas & SQL)',
        desc: 'Pandas DataFrame va murakkab SQL tahlillari',
        text: 'import pandas as pd\nimport numpy as np\n\ndf = pd.read_csv("sales_2026.csv")\nmonthly_report = df.groupby(["region", "category"]).agg({\n    "revenue": ["sum", "mean"],\n    "orders": "count"\n}).reset_index()'
      },
      {
        id: 'tr_game',
        title: 'Game Design (C# & Unity)',
        desc: 'O\'yin obyekti harakati va kontroller skriptlari',
        text: 'public class PlayerMovement : MonoBehaviour {\n    [SerializeField] private float speed = 8.5f;\n    private void Update() {\n        float h = Input.GetAxisRaw("Horizontal");\n        float v = Input.GetAxisRaw("Vertical");\n        transform.Translate(new Vector3(h, 0, v).normalized * speed * Time.deltaTime);\n    }\n}'
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
const showSettingsModal = ref<boolean>(false)
const customTextInput = ref<string>('')
const isCustomMode = computed(() => activeCategory.value === 'custom')

// Sound Theme: 'blue' | 'brown' | 'typewriter' | 'mute'
const soundTheme = ref<string>('blue')
const timeLimitMode = ref<number>(0) // 0 = unlimited, 30 = 30s, 60 = 60s

const streamBoxRef = ref<HTMLElement | null>(null)

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
const currentStreak = ref<number>(0)
const maxStreak = ref<number>(0)
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

const currentRank = computed(() => {
  const speed = wpm.value
  if (speed >= 75) return { title: 'Kiber Tezlik', badge: '⚡', color: '#af00db' }
  if (speed >= 50) return { title: 'Pro Dasturchi', badge: '🚀', color: '#007acc' }
  if (speed >= 35) return { title: 'Tezkor Yozuvchi', badge: '🥇', color: '#2e7d32' }
  if (speed >= 20) return { title: 'Ilg\'or O\'quvchi', badge: '🥈', color: '#d19a66' }
  return { title: 'Boshlovchi', badge: '🌱', color: '#8b8b8b' }
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
  if (soundTheme.value === 'mute') return
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
      osc.frequency.setValueAtTime(130, now)
      osc.frequency.exponentialRampToValueAtTime(65, now + 0.12)
      gain.gain.setValueAtTime(0.2, now)
      gain.gain.exponentialRampToValueAtTime(0.01, now + 0.12)
      osc.start(now)
      osc.stop(now + 0.12)
    } else if (soundTheme.value === 'typewriter') {
      // Typewriter vintage punch sound
      osc.type = 'square'
      osc.frequency.setValueAtTime(800, now)
      osc.frequency.exponentialRampToValueAtTime(100, now + 0.035)
      gain.gain.setValueAtTime(0.12, now)
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.035)
      osc.start(now)
      osc.stop(now + 0.035)
    } else if (soundTheme.value === 'brown') {
      // Cherry MX Brown - soft thock
      osc.type = 'sine'
      osc.frequency.setValueAtTime(isSpace ? 280 : 380, now)
      osc.frequency.exponentialRampToValueAtTime(90, now + 0.045)
      gain.gain.setValueAtTime(0.18, now)
      gain.gain.exponentialRampToValueAtTime(0.01, now + 0.045)
      osc.start(now)
      osc.stop(now + 0.045)
    } else {
      // Cherry MX Blue - crisp click
      osc.type = 'triangle'
      const freq = isSpace ? 420 : 620 + Math.random() * 80
      osc.frequency.setValueAtTime(freq, now)
      osc.frequency.exponentialRampToValueAtTime(140, now + 0.04)
      gain.gain.setValueAtTime(0.16, now)
      gain.gain.exponentialRampToValueAtTime(0.01, now + 0.04)
      osc.start(now)
      osc.stop(now + 0.04)
    }
  } catch (e) {}
}

const playVictorySound = () => {
  if (soundTheme.value === 'mute') return
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
  currentStreak.value = 0
  maxStreak.value = 0
  elapsedTimeSec.value = 0
  pressedKey.value = null
  if (streamBoxRef.value) {
    streamBoxRef.value.scrollTop = 0
  }
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
  if (showLessonModal.value || showSettingsModal.value) return

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

        // Time limit check
        if (timeLimitMode.value > 0 && elapsedTimeSec.value >= timeLimitMode.value) {
          finishLesson()
        }
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
    currentStreak.value++
    if (currentStreak.value > maxStreak.value) {
      maxStreak.value = currentStreak.value
    }
    playKeySound(false, inputChar === ' ')

    if (currentIndex.value >= targetText.value.length) {
      finishLesson()
    }
  } else {
    errorCount.value++
    currentStreak.value = 0
    charStatus.value[currentIndex.value] = 'error'
    playKeySound(true)
  }

  nextTick(() => {
    if (streamBoxRef.value) {
      const activeEl = streamBoxRef.value.querySelector('.stamina-char.active') as HTMLElement
      if (activeEl) {
        const relativeTop = activeEl.offsetTop
        if (relativeTop > streamBoxRef.value.clientHeight / 2) {
          streamBoxRef.value.scrollTop = relativeTop - (streamBoxRef.value.clientHeight / 3)
        }
      }
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

// --- Canvas Screenshot / Result Image Exporter ---
const downloadResultImage = () => {
  const canvas = document.createElement('canvas')
  canvas.width = 1000
  canvas.height = 620
  const ctx = canvas.getContext('2d')
  if (!ctx) return

  // Background
  const grad = ctx.createLinearGradient(0, 0, 1000, 620)
  grad.addColorStop(0, '#161922')
  grad.addColorStop(1, '#0e1117')
  ctx.fillStyle = grad
  ctx.fillRect(0, 0, 1000, 620)

  // Glowing border
  ctx.strokeStyle = '#007acc'
  ctx.lineWidth = 4
  ctx.strokeRect(16, 16, 968, 588)

  // Header Title
  ctx.fillStyle = '#4fc1ff'
  ctx.font = 'bold 24px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
  ctx.fillText('MUHAMMAD AL-XORAZMIY VORISLARI', 50, 65)

  ctx.fillStyle = '#8b8b8b'
  ctx.font = '16px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
  ctx.fillText('AXV · Klaviatura Trenajyori Natijasi', 50, 95)

  // Lesson Name
  ctx.fillStyle = '#ffffff'
  ctx.font = 'bold 26px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
  ctx.fillText(currentLesson.value.title, 50, 145)

  // Big Highlight Stat Boxes
  // Box 1: WPM
  ctx.fillStyle = 'rgba(255, 255, 255, 0.05)'
  ctx.fillRect(50, 180, 270, 160)
  ctx.strokeStyle = '#3c3c3c'
  ctx.lineWidth = 1
  ctx.strokeRect(50, 180, 270, 160)
  ctx.fillStyle = '#58a6ff'
  ctx.font = 'bold 64px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
  ctx.fillText(`${wpm.value}`, 75, 260)
  ctx.fillStyle = '#8b8b8b'
  ctx.font = 'bold 16px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
  ctx.fillText('TEZLIK (WPM - SO\'Z/DAQ)', 75, 305)

  // Box 2: CPM
  ctx.fillStyle = 'rgba(255, 255, 255, 0.05)'
  ctx.fillRect(360, 180, 270, 160)
  ctx.strokeRect(360, 180, 270, 160)
  ctx.fillStyle = '#4ec9b0'
  ctx.font = 'bold 64px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
  ctx.fillText(`${cpm.value}`, 385, 260)
  ctx.fillStyle = '#8b8b8b'
  ctx.font = 'bold 16px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
  ctx.fillText('BELGI/DAQ (CPM)', 385, 305)

  // Box 3: Accuracy
  ctx.fillStyle = 'rgba(255, 255, 255, 0.05)'
  ctx.fillRect(670, 180, 270, 160)
  ctx.strokeRect(670, 180, 270, 160)
  ctx.fillStyle = '#89d185'
  ctx.font = 'bold 64px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
  ctx.fillText(`${accuracy.value}%`, 695, 260)
  ctx.fillStyle = '#8b8b8b'
  ctx.font = 'bold 16px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
  ctx.fillText('ANIQLIK DARAJASI', 695, 305)

  // Extra Stats Grid
  const timeStr = `${Math.floor(elapsedTimeSec.value / 60)}:${(elapsedTimeSec.value % 60).toString().padStart(2, '0')}`
  ctx.fillStyle = '#d4d4d4'
  ctx.font = '20px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
  ctx.fillText(`⏱️ Vaqt: ${timeStr}`, 50, 395)
  ctx.fillText(`❌ Xatolar: ${errorCount.value} ta`, 280, 395)
  ctx.fillText(`🔥 Maksimal Streak: ${maxStreak.value}`, 510, 395)
  ctx.fillText(`⌨️ Bosildi: ${totalKeystrokes.value}`, 750, 395)

  // Rank Badge Card
  ctx.fillStyle = 'rgba(0, 102, 184, 0.15)'
  ctx.fillRect(50, 440, 890, 80)
  ctx.strokeStyle = '#007acc'
  ctx.strokeRect(50, 440, 890, 80)

  ctx.fillStyle = currentRank.value.color
  ctx.font = 'bold 28px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
  ctx.fillText(`${currentRank.value.badge} Daraja: ${currentRank.value.title}`, 80, 490)

  // Stars
  ctx.fillStyle = '#e5c07b'
  ctx.font = 'bold 32px sans-serif'
  const starsText = '★'.repeat(starsCount.value) + '☆'.repeat(3 - starsCount.value)
  ctx.fillText(starsText, 760, 492)

  // Footer Date & Domain
  const dateStr = new Date().toLocaleDateString('uz-UZ', { year: 'numeric', month: 'long', day: 'numeric' })
  ctx.fillStyle = '#6e7681'
  ctx.font = '15px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
  ctx.fillText(`📅 Sana: ${dateStr}`, 50, 565)
  ctx.fillText('🌐 https://axvhub.uz/trenajyor/', 700, 565)

  // Trigger Download
  const link = document.createElement('a')
  link.download = `axv-stamina-natija-${Date.now()}.png`
  link.href = canvas.toDataURL('image/png')
  link.click()
}

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
  <div class="stamina-wrapper">
    <div class="stamina-app">
      <!-- TOP CONTROLS & BREADCRUMBS -->
      <div class="stamina-header-bar">
        <Crumbs :items="[{ t: 'Bosh sahifa', l: '/' }, { t: 'Klaviatura trenajyori' }]" />

        <div class="stamina-top-controls">
          <!-- Lesson selector trigger -->
          <button class="stamina-btn-select" @click="showLessonModal = true">
            <span class="sbs-cat"><Icon :name="currentCategory.icon" /> {{ currentCategory.title }}</span>
            <span class="sbs-div">·</span>
            <span class="sbs-les">{{ currentLesson.title }}</span>
            <span class="sbs-arrow">▾</span>
          </button>

          <!-- Quick Action Controls -->
          <div class="stamina-quick-actions">
            <!-- Streak Flame indicator -->
            <div v-if="currentStreak >= 10" class="streak-badge" title="Ketma-ket xatosiz belgilar">
              🔥 {{ currentStreak }}
            </div>

            <!-- Settings Modal Button -->
            <button class="icon-btn" @click="showSettingsModal = true" title="Sozlamalar va Ovoz">
              <Icon name="settings" />
            </button>

            <!-- Reset Button -->
            <button class="icon-btn" @click="resetLesson" title="Qayta boshlash">
              <Icon name="rotate-ccw" />
            </button>
          </div>
        </div>
      </div>

      <!-- CENTERED BEAUTIFUL METRIC CARDS (FLUID SCALING) -->
      <div class="stamina-metrics-row">
        <div class="metric-card">
          <div class="m-icon"><Icon name="zap" /></div>
          <div class="m-content">
            <div class="m-num">{{ wpm }}</div>
            <div class="m-lbl">WPM (so'z/daq)</div>
          </div>
        </div>
        <div class="metric-card">
          <div class="m-icon"><Icon name="gauge" /></div>
          <div class="m-content">
            <div class="m-num">{{ cpm }}</div>
            <div class="m-lbl">CPM (belgi/daq)</div>
          </div>
        </div>
        <div class="metric-card">
          <div class="m-icon"><Icon name="target" /></div>
          <div class="m-content">
            <div class="m-num" :style="{ color: accuracy >= 95 ? 'var(--ax-good)' : 'inherit' }">{{ accuracy }}%</div>
            <div class="m-lbl">Aniqlik</div>
          </div>
        </div>
        <div class="metric-card">
          <div class="m-icon"><Icon name="timer" /></div>
          <div class="m-content">
            <div class="m-num">{{ Math.floor(elapsedTimeSec / 60) }}:{{ (elapsedTimeSec % 60).toString().padStart(2, '0') }}</div>
            <div class="m-lbl">Vaqt</div>
          </div>
        </div>
        <div class="metric-card">
          <div class="m-icon"><Icon name="circle-question-mark" /></div>
          <div class="m-content">
            <div class="m-num error-num">{{ errorCount }}</div>
            <div class="m-lbl">Xatolar</div>
          </div>
        </div>
      </div>

      <!-- SLIM PROGRESS BAR -->
      <div class="stamina-progress-bar">
        <div class="spb-inner" :style="{ width: progressPct + '%' }"></div>
      </div>

      <!-- MAIN INPUT / STREAM BOX (EXPANDED FLUID FONT & PADDING) -->
      <div ref="streamBoxRef" class="stamina-stream-box" tabindex="0">
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
            Tavsiya etilgan barmoq: <b>{{ currentFingerGuide.finger }}</b>
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

      <!-- ENLARGED & ROCK-SOLID KEYBOARD (COMFORTABLE SPACING) -->
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

    <!-- SETTINGS MODAL (SOUND, TIMER & MODES) -->
    <div v-if="showSettingsModal" class="stamina-modal-overlay" @click.self="showSettingsModal = false">
      <div class="stamina-settings-modal">
        <div class="slm-header">
          <h2><Icon name="settings" /> Trenajyor sozlamalari</h2>
          <button class="slm-close" @click="showSettingsModal = false">✕</button>
        </div>

        <div class="settings-body">
          <!-- Sound Theme Selection -->
          <div class="set-section">
            <label class="set-title"><Icon name="volume-2" /> Klaviatura ovoz profili:</label>
            <div class="set-chips">
              <button
                class="set-chip"
                :class="{ active: soundTheme === 'blue' }"
                @click="soundTheme = 'blue'; playKeySound()"
              >
                🔵 Cherry MX Blue (Jarangdor)
              </button>
              <button
                class="set-chip"
                :class="{ active: soundTheme === 'brown' }"
                @click="soundTheme = 'brown'; playKeySound()"
              >
                🟤 Cherry MX Brown (Yumshoq)
              </button>
              <button
                class="set-chip"
                :class="{ active: soundTheme === 'typewriter' }"
                @click="soundTheme = 'typewriter'; playKeySound()"
              >
                📟 Yozuv mashinkasi
              </button>
              <button
                class="set-chip"
                :class="{ active: soundTheme === 'mute' }"
                @click="soundTheme = 'mute'"
              >
                🔇 Ovoz o'chirilgan
              </button>
            </div>
          </div>

          <!-- Time Limit Mode -->
          <div class="set-section">
            <label class="set-title"><Icon name="timer" /> Vaqt rejimi (Sprint):</label>
            <div class="set-chips">
              <button
                class="set-chip"
                :class="{ active: timeLimitMode === 0 }"
                @click="timeLimitMode = 0; resetLesson()"
              >
                Cheksiz (Matn oxirigacha)
              </button>
              <button
                class="set-chip"
                :class="{ active: timeLimitMode === 30 }"
                @click="timeLimitMode = 30; resetLesson()"
              >
                ⏱️ 30 soniya sprint
              </button>
              <button
                class="set-chip"
                :class="{ active: timeLimitMode === 60 }"
                @click="timeLimitMode = 60; resetLesson()"
              >
                ⏱️ 60 soniya test
              </button>
            </div>
          </div>

          <!-- Virtual Keyboard Display Toggle -->
          <div class="set-section">
            <label class="set-title"><Icon name="keyboard" /> Virtual klaviatura:</label>
            <div class="set-chips">
              <button
                class="set-chip"
                :class="{ active: showKeyboard }"
                @click="showKeyboard = true"
              >
                Ko'rsatish
              </button>
              <button
                class="set-chip"
                :class="{ active: !showKeyboard }"
                @click="showKeyboard = false"
              >
                Yashirish (Faqat matn)
              </button>
            </div>
          </div>
        </div>

        <div class="set-footer">
          <button class="btn btn-primary" @click="showSettingsModal = false">
            <Icon name="check" /> Saqlash va yopish
          </button>
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
          <div class="sm-rank-pill" :style="{ borderColor: currentRank.color, color: currentRank.color }">
            {{ currentRank.badge }} {{ currentRank.title }}
          </div>
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
            <span class="sm-lbl">Maksimal Combo</span>
            <span class="sm-val" style="color: #d19a66;">🔥 {{ maxStreak }}</span>
          </div>
        </div>

        <div class="sm-actions">
          <button class="btn btn-ghost" @click="resetLesson">
            <Icon name="rotate-ccw" /> Qaytadan
          </button>
          <button class="btn btn-ghost" @click="downloadResultImage" title="Natijani rasm qilib yuklab olish">
            <Icon name="camera" /> Rasm qilib yuklash
          </button>
          <button class="btn btn-primary" @click="nextLesson">
            Keyingi bosqich <Icon name="arrow-right" />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.stamina-wrapper {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - 90px);
  padding: 0 16px;
  box-sizing: border-box;
}

.stamina-app {
  width: 100%;
  max-width: min(1280px, 96vw);
  display: flex;
  flex-direction: column;
  gap: clamp(8px, 1.3vh, 14px);
  box-sizing: border-box;
}

/* TOP HEADER & CONTROLS */
.stamina-header-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
  min-height: 40px;
}

.stamina-top-controls {
  display: flex;
  align-items: center;
  gap: 10px;
}

.stamina-btn-select {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: var(--ax-card);
  border: 1px solid var(--ax-line);
  padding: 0 16px;
  height: clamp(38px, 4.6vh, 44px);
  border-radius: 10px;
  color: var(--vp-c-text-1);
  font-size: clamp(0.88rem, 1vw, 1rem);
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
  font-weight: 700;
}

.sbs-div {
  opacity: 0.4;
}

.sbs-les {
  max-width: 300px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sbs-arrow {
  opacity: 0.6;
  font-size: 0.85rem;
}

.stamina-quick-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.streak-badge {
  display: inline-flex;
  align-items: center;
  padding: 4px 12px;
  border-radius: 8px;
  background: rgba(209, 154, 102, 0.2);
  color: #d19a66;
  font-weight: 800;
  font-size: 0.95rem;
  animation: pulseFire 0.8s infinite alternate;
}

@keyframes pulseFire {
  from { transform: scale(1); }
  to { transform: scale(1.08); }
}

.icon-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: clamp(38px, 4.6vh, 44px);
  height: clamp(38px, 4.6vh, 44px);
  border-radius: 10px;
  background: var(--ax-card);
  border: 1px solid var(--ax-line);
  color: var(--vp-c-text-2);
  cursor: pointer;
  transition: all 0.15s ease;
  font-size: 1.1rem;
}

.icon-btn:hover {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
}

/* CENTERED METRICS ROW */
.stamina-metrics-row {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: clamp(8px, 1.2vw, 16px);
}

.metric-card {
  display: flex;
  align-items: center;
  gap: clamp(10px, 1.2vw, 14px);
  background: var(--ax-card);
  border: 1px solid var(--ax-line);
  border-radius: 14px;
  padding: clamp(8px, 1vh, 12px) clamp(12px, 1.2vw, 18px);
  height: clamp(58px, 7.2vh, 72px);
  box-sizing: border-box;
}

.m-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: clamp(36px, 4.4vh, 44px);
  height: clamp(36px, 4.4vh, 44px);
  border-radius: 10px;
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
  font-size: clamp(1.1rem, 1.3vw, 1.35rem);
  flex-shrink: 0;
}

.m-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  overflow: hidden;
}

.m-num {
  font-size: clamp(1.3rem, 1.7vw, 1.75rem);
  font-weight: 800;
  line-height: 1.1;
  color: var(--vp-c-text-1);
  font-variant-numeric: tabular-nums;
}

.m-lbl {
  font-size: clamp(0.68rem, 0.8vw, 0.78rem);
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--vp-c-text-2);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.error-num {
  color: #e06c75;
}

/* PROGRESS BAR */
.stamina-progress-bar {
  height: 4px;
  background: var(--ax-line);
  border-radius: 999px;
  overflow: hidden;
  flex-shrink: 0;
}

.spb-inner {
  height: 100%;
  background: var(--ax-grad);
  transition: width 0.15s ease;
}

/* TYPING STREAM BOX */
.stamina-stream-box {
  position: relative;
  background: var(--vp-c-bg-alt);
  border: 2px solid var(--ax-line);
  border-radius: 16px;
  padding: clamp(16px, 2vh, 22px) clamp(20px, 2.2vw, 32px);
  height: clamp(110px, 14vh, 145px);
  box-sizing: border-box;
  overflow-y: hidden;
  outline: none;
  cursor: text;
  transition: border-color 0.2s, box-shadow 0.2s;
  flex-shrink: 0;
}

.stamina-stream-box:focus {
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 0 0 3px var(--vp-c-brand-soft);
}

.stream-inner {
  font-family: 'Consolas', 'Fira Code', 'JetBrains Mono', 'Courier New', monospace;
  font-size: clamp(1.6rem, 2vw, 2.15rem);
  line-height: 1.65;
  letter-spacing: 0.06em;
  white-space: pre-wrap;
  word-break: break-word;
  user-select: none;
}

.stamina-char {
  position: relative;
  border-radius: 4px;
}

.stamina-char.pending {
  color: var(--vp-c-text-2);
  opacity: 0.65;
}

.stamina-char.correct {
  color: var(--ax-good);
}

.stamina-char.error {
  color: #fff;
  background: #e06c75;
  border-radius: 4px;
}

.stamina-char.active {
  color: var(--vp-c-text-1);
  background: rgba(0, 102, 184, 0.28);
  border-bottom: 3.5px solid var(--vp-c-brand-1);
  font-weight: 700;
  box-shadow: 0 0 10px rgba(0, 102, 184, 0.6);
}

.stamina-char.active.space {
  background: rgba(0, 102, 184, 0.35);
  display: inline-block;
  min-width: 0.55em;
}

.stream-hint {
  position: absolute;
  right: 16px;
  bottom: 8px;
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: clamp(0.75rem, 0.85vw, 0.88rem);
  color: var(--vp-c-text-3);
  pointer-events: none;
}

/* FINGER & KEY INDICATOR BAR */
.stamina-finger-guide {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: var(--ax-card);
  border: 1px solid var(--ax-line);
  border-radius: 12px;
  padding: 0 clamp(14px, 1.5vw, 20px);
  height: clamp(38px, 4.6vh, 44px);
  box-sizing: border-box;
  font-size: clamp(0.88rem, 1vw, 1rem);
  margin-bottom: clamp(6px, 1.2vh, 14px);
  flex-shrink: 0;
}

.fg-info {
  display: flex;
  align-items: center;
  gap: 10px;
}

.fg-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  display: inline-block;
}

.fg-target {
  display: flex;
  align-items: center;
  gap: 8px;
  color: var(--vp-c-text-2);
}

.target-badge {
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
  padding: 3px 12px;
  border-radius: 8px;
  font-weight: 700;
  font-family: monospace;
  font-size: 1.05em;
}

/* ENLARGED & ROCK-SOLID ERGONOMIC KEYBOARD */
.stamina-keyboard {
  background: var(--ax-card);
  border: 1px solid var(--ax-line);
  border-radius: 16px;
  padding: clamp(10px, 1.2vh, 16px) clamp(10px, 1.2vw, 16px);
  display: flex;
  flex-direction: column;
  gap: clamp(5px, 0.7vh, 8px);
  user-select: none;
  box-shadow: var(--ax-shadow);
  flex-shrink: 0;
}

.kb-row {
  display: flex;
  gap: clamp(5px, 0.6vw, 8px);
  justify-content: center;
}

.kb-key {
  position: relative;
  height: clamp(46px, 5.8vh, 60px);
  background: var(--vp-c-bg);
  border: 1px solid var(--ax-line);
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: clamp(0.82rem, 1.05vw, 1.05rem);
  font-weight: 600;
  color: var(--vp-c-text-1);
  box-shadow: 0 2.5px 0 var(--ax-line);
  box-sizing: border-box;
}

.k-top {
  font-size: clamp(0.62rem, 0.75vw, 0.75rem);
  opacity: 0.6;
  margin-bottom: -2px;
}

.k-main {
  font-size: clamp(0.85rem, 1.05vw, 1.05rem);
}

.k-bump {
  position: absolute;
  bottom: 2px;
  font-size: 0.9rem;
  font-weight: bold;
  opacity: 0.6;
}

.finger-lp, .finger-rp { border-bottom: 3.5px solid #e06c75; }
.finger-lr, .finger-rr { border-bottom: 3.5px solid #d19a66; }
.finger-lm, .finger-rm { border-bottom: 3.5px solid #e5c07b; }
.finger-li, .finger-ri { border-bottom: 3.5px solid #98c379; }
.finger-thumb { border-bottom: 3.5px solid #c678dd; }

.key-target {
  background: linear-gradient(135deg, #0e70c0, #2392dc) !important;
  color: #fff !important;
  border-color: #0e70c0 !important;
  box-shadow: 0 0 14px rgba(14, 112, 192, 0.7) !important;
}

.key-shift-target {
  background: linear-gradient(135deg, #af00db, #c586c0) !important;
  color: #fff !important;
  border-color: #af00db !important;
  box-shadow: 0 0 14px rgba(175, 0, 219, 0.7) !important;
}

.key-pressed {
  background: var(--vp-c-brand-soft) !important;
  filter: brightness(1.15);
}

/* MODALS */
.stamina-modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.75);
  backdrop-filter: blur(6px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 16px;
}

.stamina-lesson-modal, .stamina-settings-modal {
  background: var(--vp-c-bg);
  border: 1px solid var(--ax-line);
  border-radius: 20px;
  width: 100%;
  max-width: 720px;
  max-height: 85vh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  box-shadow: 0 24px 60px rgba(0, 0, 0, 0.6);
}

.slm-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 18px 24px;
  border-bottom: 1px solid var(--ax-line);
}

.slm-header h2 {
  font-size: 1.35rem;
  font-weight: 800;
  margin: 0;
  display: flex;
  align-items: center;
  gap: 10px;
}

.slm-close {
  background: transparent;
  border: none;
  font-size: 1.3rem;
  color: var(--vp-c-text-2);
  cursor: pointer;
  padding: 4px 10px;
  border-radius: 8px;
}

.slm-close:hover {
  background: var(--ax-card-hi);
  color: var(--vp-c-text-1);
}

.slm-cats {
  display: flex;
  gap: 8px;
  padding: 12px 24px;
  border-bottom: 1px solid var(--ax-line);
  background: var(--ax-card);
  overflow-x: auto;
}

.slm-cat-tab {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  border-radius: 10px;
  font-size: 0.9rem;
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
  padding: 20px 24px;
  overflow-y: auto;
  max-height: 55vh;
}

.slm-lessons-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 12px;
}

.slm-lesson-card {
  text-align: left;
  background: var(--ax-card);
  border: 1px solid var(--ax-line);
  border-radius: 12px;
  padding: 14px 16px;
  cursor: pointer;
  transition: all 0.15s ease;
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.slm-lesson-card:hover {
  border-color: var(--vp-c-brand-1);
  background: var(--ax-card-hi);
}

.slm-lesson-card.active {
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
}

.slm-card-top {
  display: flex;
  align-items: center;
  gap: 10px;
}

.slm-idx {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
  font-size: 0.8rem;
  font-weight: 700;
}

.slm-title {
  font-weight: 700;
  font-size: 0.95rem;
  color: var(--vp-c-text-1);
}

.slm-desc {
  font-size: 0.82rem;
  color: var(--vp-c-text-2);
  margin: 0;
  line-height: 1.4;
}

.slm-custom-box {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.slm-custom-box textarea {
  width: 100%;
  padding: 14px;
  border-radius: 10px;
  border: 1px solid var(--ax-line);
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  font-family: inherit;
  font-size: 1rem;
}

/* SETTINGS MODAL */
.settings-body {
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.set-section {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.set-title {
  font-size: 0.95rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 8px;
  color: var(--vp-c-text-1);
}

.set-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.set-chip {
  padding: 8px 16px;
  border-radius: 10px;
  background: var(--ax-card);
  border: 1px solid var(--ax-line);
  color: var(--vp-c-text-2);
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  transition: 0.15s ease;
}

.set-chip:hover {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-text-1);
}

.set-chip.active {
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
  border-color: var(--vp-c-brand-1);
}

.set-footer {
  padding: 16px 24px;
  border-top: 1px solid var(--ax-line);
  display: flex;
  justify-content: flex-end;
}

/* RESULTS MODAL */
.stamina-modal {
  background: var(--vp-c-bg);
  border: 1px solid var(--ax-line);
  border-radius: 22px;
  padding: 32px;
  max-width: 520px;
  width: 100%;
  text-align: center;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
}

.sm-stars {
  display: flex;
  justify-content: center;
  gap: 6px;
  font-size: 2.2rem;
  margin-bottom: 6px;
}

.sm-stars .star {
  color: var(--ax-line);
}

.sm-stars .star.filled {
  color: #e5c07b;
}

.sm-header h2 {
  font-size: 1.6rem;
  font-weight: 800;
  margin: 0 0 4px;
}

.sm-rank-pill {
  display: inline-block;
  font-weight: 800;
  font-size: 0.95rem;
  border: 1.5px solid currentColor;
  padding: 4px 14px;
  border-radius: 999px;
  margin: 6px 0 10px;
}

.sm-sub {
  color: var(--vp-c-text-2);
  margin: 0 0 16px;
  font-size: 0.95rem;
}

.sm-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  background: var(--ax-card);
  border: 1px solid var(--ax-line);
  border-radius: 14px;
  padding: 16px;
  margin-bottom: 24px;
}

.sm-stat {
  display: flex;
  flex-direction: column;
}

.sm-lbl {
  font-size: 0.72rem;
  color: var(--vp-c-text-2);
  margin-bottom: 4px;
}

.sm-val {
  font-size: 1.35rem;
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
  .stamina-metrics-row {
    grid-template-columns: repeat(2, 1fr);
  }
  .stamina-keyboard {
    display: none;
  }
  .stream-inner {
    font-size: 1.25rem;
  }
}
</style>
