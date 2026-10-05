# 10-sinf: o'quv xaritasi (BI va Machine Learning)

Manba: Rasmiy o'quv dasturi (`10-sinf-bi/_matn/oquv-dasturi.txt`), Uslubiy ko'rsatma va O'quv qo'llanma.

**Tuzilma:** 102 dars, haftasiga 3 dars (har biri 80 daqiqa). Hafta = ceil(dars № / 3), jami 34 hafta, 4 chorak.

**Holat belgilari:** ⬜ rejada · 📝 materiallar tayyorlangan · ✅ o'tilgan

## Joriy holat

- Oxirgi o'tilgan dars: **0**
- Keyingi dars: **7** (3-hafta, 1-dars)
- Oxirgi yangilanish: 3-hafta (7–9 darslar) tayyorlandi

---

## I-bob. Ma’lumotlar muhandisligiga kirish va ma’lumotlarni boshqarish (27 dars)

| Dars | Hafta | Mavzu | Holat |
|---|---|---|---|
| 1 | 1 | Ma’lumotlar muhandisligiga kirish (DIKW piramidasi, Data Engineer roli, Data Pipeline) | 📝 |
| 2 | 1 | Ma'lumotlar arxitekturasi va hayot sikli (6 qatlam, 7 bosqich, Data Quality mezonlari) | 📝 |
| 3 | 1 | Ma’lumot formatlari: CSV va JSON bilan ishlash (Tabular vs Nested, Medallion arxitekturasi) | 📝 |
| 4 | 2 | Ma’lumot formatlari: Parquet va Columnar saqlash formati (Snappy siqish, CSV vs Parquet) | 📝 |
| 5 | 2 | Ma’lumot formatlari: Avro va formatlarni chuqur taqqoslash | 📝 |
| 6 | 2 | Ma’lumotlar bazalari: konsept va tuzilma. Relatsion ma’lumotlar bazasi (RDBMS) asoslari | 📝 |
| 7 | 3 | Relyatsion jadvallar, Primary Key, Foreign Key va relyatsion yaxlitlik | 📝 |
| 8 | 3 | R-diagrammalar (ERD) loyihalash va SQLite bilan ishlash | 📝 |
| 9 | 3 | SQL analitik operatorlari: SELECT, WHERE, ORDER BY, LIMIT asoslari | 📝 |
| 10 | 4 | SQL analitik operatorlari: GROUP BY va HAVING bilan ma'lumotlarni guruhlash | 📝 |
| 11 | 4 | SQL JOIN turlari (INNER, LEFT, RIGHT, FULL) va amaliy tahlil | 📝 |
| 12 | 4 | Subquery, CTE (WITH) va CASE WHEN operatorlari | 📝 |
| 13 | 5 | Ma'lumotlar modellashtirish: Kimball metodologiyasi, Star Schema va Snowflake Schema | ⬜ |
| 14 | 5 | Fakt (Fact) va O'lcham (Dimension) jadvallarini loyihalash | ⬜ |
| 15 | 5 | Data Mart tushunchasi va sohaga oid martlar yaratish | ⬜ |
| 16 | 6 | Sekin o'zgaruvchi o'lchamlar (SCD Type 1, Type 2) va surrogat kalitlar | ⬜ |
| 17 | 6 | Ma'lumotlar ombori: Data Warehouse (DWH) tushunchasi, arxitekturasi va afzalliklari | ⬜ |
| 18 | 6 | Data Lake konsepsiyasi, Bronze / Silver / Gold zonalari | ⬜ |
| 19 | 7 | Data Warehouse vs Data Lake vs Modern Lakehouse arxitekturasi | ⬜ |
| 20 | 7 | ETL va ELT asoslari: farqi, afzalliklari va zamonaviy qo'llanilishi | ⬜ |
| 21 | 7 | On-premise va Cloud infratuzilmalarda ETL/ELT jarayonlari | ⬜ |
| 22 | 8 | Data Lake va Data Warehouse integratsiyasi (Data Pipeline amaliyoti) | ⬜ |
| 23 | 8 | Medallion arxitekturasida ELT jarayonlarini tashkil qilish | ⬜ |
| 24 | 8 | Ma’lumotlarni boshqarish: Monitoring va Observability tushunchalari | ⬜ |
| 25 | 9 | Logging tizimlari va xatoliklarni qayd etish | ⬜ |
| 26 | 9 | Data Validation: Sifat nazorati va avtomatlashtirilgan testlar | ⬜ |
| 27 | 9 | 1-nazorat ishi: Data Engineering asoslari va amaliy loyiha himoyasi | ⬜ |

---

## II-bob. Ma’lumotlar oqimi va avtomatlashtirish (21 dars)

| Dars | Hafta | Mavzu | Holat |
|---|---|---|---|
| 28 | 10 | Big Data mazmuni: 3V/5V tamoyillari va taqsimlangan hisoblashlar | ⬜ |
| 29 | 10 | Apache Spark arxitekturasi: Driver, Executor, Cluster Manager | ⬜ |
| 30 | 10 | PySpark asoslari va RDD tushunchasi | ⬜ |
| 31 | 11 | PySpark DataFrame API va asosiy operatsiyalar | ⬜ |
| 32 | 11 | PySpark yordamida katta ma'lumotlarni tozalash va sifatini boshqarish | ⬜ |
| 33 | 11 | Ustunlar darajasida transformatsiyalar va ma'lumot turlarini o'zgartirish | ⬜ |
| 34 | 12 | Datasetlarni boyitish, birlashtirish (Joins) va agregatsiyalar | ⬜ |
| 35 | 12 | PySpark bilan End-to-End Pipeline qurish va optimallashtirish | ⬜ |
| 36 | 12 | dbt (Data Build Tool): Zamonaviy ELT transformatsiyalar va dbt arxitekturasi | ⬜ |
| 37 | 13 | dbt SQL modellari, Jinja templating va model logikasi | ⬜ |
| 38 | 13 | dbt models arxitekturasi: Staging, Intermediate, Marts va Tests | ⬜ |
| 39 | 13 | Apache Airflow: Arxitektura, Scheduler, Webserver va Workerlar | ⬜ |
| 40 | 14 | Airflow DAGs, Operatorlar va Tasklar bilan ishlash | ⬜ |
| 41 | 14 | Airflow Workflow Orchestration, Dependencies va Scheduling | ⬜ |
| 42 | 14 | Airflow va dbt Pipeline integratsiyasi asoslari | ⬜ |
| 43 | 15 | BashOperator va DbtOperator yordamida dbt modellarini Airflow'da ishga tushirish | ⬜ |
| 44 | 15 | Airflow'da XCom, Lineage va vazifalar o'rtasida metadata almashish | ⬜ |
| 45 | 15 | Azure Data Factory: Cloud Orchestration va integratsiya asoslari | ⬜ |
| 46 | 16 | ADF Linked Services, Datasets va Copy Activity bilan ma'lumot yuklash | ⬜ |
| 47 | 16 | ADF Mapping Data Flows, Triggers va Cloud Monitoring | ⬜ |
| 48 | 16 | 2-nazorat ishi: Big Data pipeline va orkestratsiya loyihasi | ⬜ |

---

## III-bob. Machine Learning (ML)ga kirish (30 dars)

| Dars | Hafta | Mavzu | Holat |
|---|---|---|---|
| 49 | 17 | Machine Learningga kirish: AI, ML va Deep Learning farqlari | ⬜ |
| 50 | 17 | ML turlari: Supervised, Unsupervised va Reinforcement Learning | ⬜ |
| 51 | 17 | ML hayot sikli: Data &rarr; Training &rarr; Testing &rarr; Evaluation | ⬜ |
| 52 | 18 | Train-Test Split metodologiyasi va modelni o'qitish (fit/predict) | ⬜ |
| 53 | 18 | Overfitting va Underfitting muammolari va ularning oldini olish | ⬜ |
| 54 | 18 | Model baholash metrikalari: Confusion Matrix, Accuracy va uning cheklovlari | ⬜ |
| 55 | 19 | Precision, Recall va F1-score metrikalari | ⬜ |
| 56 | 19 | Precision-Recall trade-off, ROC-AUC egri chizig'i | ⬜ |
| 57 | 19 | Ma’lumot tayyorlash (Feature Engineering) ahamiyati | ⬜ |
| 58 | 20 | Kategorik ustunlarni kodlash (One-Hot Encoding, Label Encoding) | ⬜ |
| 59 | 20 | Xususiyatlarni masshtablash: MinMax Scaling va StandardScaler | ⬜ |
| 60 | 20 | Yangi xususiyatlar yaratish (Feature Creation) va tanlash (Selection) | ⬜ |
| 61 | 21 | Regressiya modellari: Linear Regression nazariyasi ($y = mx + b$) | ⬜ |
| 62 | 21 | Scikit-learn yordamida Linear Regression modelini qurish va o'qitish | ⬜ |
| 63 | 21 | Regressiya metrikalari: MSE, RMSE, MAE va $R^2$ score | ⬜ |
| 64 | 22 | Qoldiqlar tahlili (Residual Analysis) va natijalarni vizualizatsiya qilish | ⬜ |
| 65 | 22 | Klassifikatsiya vazifasi va KNN (K-Nearest Neighbors) algoritmi | ⬜ |
| 66 | 22 | Decision Tree (Qarorlar daraxti) algoritmi va talqin qilish | ⬜ |
| 67 | 23 | Giperparametrlarni sozlash (Hyperparameter Tuning: GridSearchCV) | ⬜ |
| 68 | 23 | TensorFlow asoslari: Tensorlar, Graf tuzilmasi va Keras kutubxonasi | ⬜ |
| 69 | 23 | Neyron tarmoq qatlamlari (Dense, Activation: ReLU, Sigmoid) | ⬜ |
| 70 | 24 | TensorFlow Sequential modelini qurish, o'qitish va baholash | ⬜ |
| 71 | 24 | PyTorch asoslari: Arxitektura, Tensor operatsiyalari va Autograd | ⬜ |
| 72 | 24 | PyTorch'da Dataset va DataLoader bilan ishlash | ⬜ |
| 73 | 25 | PyTorch `torch.nn` yordamida sodda neyron tarmoq qurish va o'qitish sikli | ⬜ |
| 74 | 25 | Modelni saqlash (joblib, .h5, .pt) va FastAPI ga kirish | ⬜ |
| 75 | 25 | FastAPI yordamida `/predict` REST API endpoint yaratish | ⬜ |
| 76 | 26 | Swagger UI orqali API testlash va Uvicorn bilan ishga tushirish | ⬜ |
| 77 | 26 | ML va Data Pipeline integratsiyasi (Airflow orqali modelni yangilash) | ⬜ |
| 78 | 26 | 3-nazorat ishi: ML modelini o'qitish va API orqali deploy qilish | ⬜ |

---

## IV-bob. Integratsiya, avtomatlashtirish va zamonaviy texnologiyalar (24 dars)

| Dars | Hafta | Mavzu | Holat |
|---|---|---|---|
| 79 | 27 | End-to-End Data Platform arxitekturasi: Source &rarr; ETL &rarr; DWH &rarr; ML &rarr; API &rarr; BI | ⬜ |
| 80 | 27 | DE va ML integratsiyasi amaliyoti | ⬜ |
| 81 | 27 | Bulutli saqlash va arxitektura komponentlari (AWS S3, Azure Blob) | ⬜ |
| 82 | 28 | Ma’lumotlarda xavfsizlik va maxfiylik (Data Privacy) | ⬜ |
| 83 | 28 | GDPR tamoyillari, Sensitive Data va anonimizatsiya usullari | ⬜ |
| 84 | 28 | AI etikasi: Model bias, fairness va shaffoflik | ⬜ |
| 85 | 29 | CI/CD asoslari va GitHub bilan versiyalarni boshqarish | ⬜ |
| 86 | 29 | GitHub Actions orqali avtomatlashtirilgan pipeline (YAML) yaratish | ⬜ |
| 87 | 29 | Avtomatlashtirilgan testlar (pytest) va linting tekshiruvlari | ⬜ |
| 88 | 30 | Docker texnologiyasi: Image va Container tushunchalari | ⬜ |
| 89 | 30 | Dockerfile yaratish: Python, FastAPI va ML modelni konteynerlash | ⬜ |
| 90 | 30 | Docker Compose: Multi-container tizimlar (API + DB) | ⬜ |
| 91 | 31 | Data & ML monitoring va Observability tizimlari | ⬜ |
| 92 | 31 | Model Drift va Data Drift monitoring qilish usullari | ⬜ |
| 93 | 31 | Prometheus va Grafana yordamida ko'rsatkichlarni vizual kuzatish | ⬜ |
| 94 | 32 | Sun’iy intellekt infratuzilmalari: CPU, GPU va TPU arxitekturasi | ⬜ |
| 95 | 32 | Bulutli ML platformalari (Google Vertex AI, AWS SageMaker) | ⬜ |
| 96 | 32 | AI infratuzilmasi samaradorligi va xarajatlarni boshqarish (Cost Optimization) | ⬜ |
| 97 | 33 | Zamonaviy trendlar: Data Mesh arxitekturasi | ⬜ |
| 98 | 33 | AutoML platformalari va avtomatlashtirilgan ML | ⬜ |
| 99 | 33 | Generative AI va LLM ekotizimi bilan tanishuv | ⬜ |
| 100 | 34 | Data Engineering va ML kasbiy yo'nalishlari, Portfolioni GitHub'da shakllantirish | ⬜ |
| 101 | 34 | 4-nazorat ishi: Yillik yakuniy integratsiyalashgan loyiha taqdimoti | ⬜ |
| 102 | 34 | Kurs yakuniy xulosalari va kelgusi rivojlanish rejasi | ⬜ |
