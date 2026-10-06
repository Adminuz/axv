# 13-dars. Foydalanuvchilarni boshqarish: Identifikatsiya, autentifikatsiya va avtorizatsiya. Token, session va JWT

## Dars rejasi (80 daqiqa)

**Maqsad:** Identifikatsiya, autentifikatsiya va avtorizatsiya farqini, session va token (JWT) yondashuvlarini tushuntirish; `User` modeli va ro'yxatdan o'tishni yaratish, parollarni bcrypt bilan xeshlash, `OAuth2PasswordBearer` va JWT bilan login hamda `get_current_user` himoyasini qurish.

**Kutiladigan natija:** o'quvchi (1) identifikatsiya, autentifikatsiya va avtorizatsiyani misol bilan ajratadi; (2) session va JWT token farqini tushuntiradi, JWT ning 3 qismini ayta oladi; (3) `User` modeli, `/auth/register` va parol xeshlashni yozadi; (4) `/auth/login`, `OAuth2PasswordBearer`, `get_current_user` va `/auth/me` ni ishlatadi.

| Vaqt | Bosqich |
|---|---|
| 10 daq | Takrorlash: 12-dars: skeleton, `config`, `database` |
| 30 daq | Yangi mavzu: Identifikatsiya, autentifikatsiya, avtorizatsiya; session va JWT; `User` modeli, `bcrypt` xeshlash, `/auth/register` |
| 5 daq | Tanaffus |
| 20 daq | Amaliyot: `/auth/login`, JWT yaratish, `get_current_user`, `/auth/me` (Swagger Authorize) |
| 10 daq | Xavfsizlik: `jwt_secret_key`, muddat, xatolik kodlari; xulosa |
| 5 daq | Xulosa, tezkor nazorat, uyga vazifa |

---

## Mentor konspekti

### 1. Identifikatsiya, autentifikatsiya, avtorizatsiya
**Identifikatsiya** — «Siz kimsiz?» (email yoki login). **Autentifikatsiya** — «Isbotlang» (parol, token). **Avtorizatsiya** — «Sizga nima mumkin?» (rol, ruxsat). Autentifikatsiyaning ikki yondashuvi: **session** (server foydalanuvchi holatini saqlaydi, brauzerga cookie beradi) va **token** (server holat saqlamaydi, mijoz har so'rovda `Authorization: Bearer ...` yuboradi). **JWT** (JSON Web Token) — imzolangan token: `header.payload.signature`. U imzolangan, lekin shifrlanmagan: ichiga parol yozmang.

`payload` ni har kim o'qiy oladi (base64), lekin kalitsiz o'zgartira olmaydi: imzo buzilib qoladi. Shuning uchun maxfiy ma'lumotni payload ga yozmang.

### 2. User modeli, parol xeshlash va ro'yxatdan o'tish
Parol bazada hech qachon ochiq saqlanmaydi: u **xeshlanadi** (bcrypt, passlib orqali). `users` jadvalida faqat `hashed_password` bor. Kirishda kiritilgan parol xeshlanib solishtirilmaydi, `verify_password` bilan tekshiriladi. Ro'yxatdan o'tishda avval email bandligini tekshiramiz: band bo'lsa `409 Conflict`, aks holda yangi `User` yaratiladi va `201` qaytadi. Javob sxemasida (`UserRead`) parol maydoni bo'lmasligi shart.

Xesh har safar boshqacha chiqadi (tuz, salt): bir xil parol uchun ikki xil xesh. Shuning uchun `==` emas, faqat `verify_password` ishlatiladi.

### 3. Login, JWT va get_current_user
Login `OAuth2PasswordRequestForm` qabul qiladi (maydonlar `username` va `password`; bizda `username` = email). Parol to'g'ri bo'lsa `create_access_token` JWT beradi: `sub` — foydalanuvchi id, `exp` — amal qilish muddati. Himoyalangan endpoint `OAuth2PasswordBearer(tokenUrl="/auth/login")` orqali tokenni oladi. `get_current_user` tokenni `jwt.decode` bilan tekshiradi va `User` ni qaytaradi; xato bo'lsa `401`. Rol tekshiruvi: oddiy foydalanuvchi admin yo'liga kirsa `403`.

Swagger da `Authorize` tugmasi orqali login qilib, `/auth/me` ni sinang. `401` — kimligingiz tasdiqlanmadi, `403` — kimligingiz ma'lum, lekin ruxsat yo'q.

---

## Kod namunalari

### 1. `app/models/user.py`
```python
import uuid
from datetime import datetime
from sqlalchemy import Boolean, DateTime, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name: Mapped[str] = mapped_column(String(120))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
```

### 2. `app/schemas/user.py`
```python
import uuid
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    full_name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    full_name: str
    email: EmailStr
    is_admin: bool
```

### 3. `app/core/security.py`
```python
from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def create_access_token(user_id: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    return jwt.encode({"sub": user_id, "exp": expire},
                      settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
```

### 4. `app/api/deps.py`: admin tekshiruvi
```python
async def get_current_admin(user: User = Depends(get_current_user)) -> User:
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Admin huquqi kerak")
    return user
```

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq (Oson): Tushunchalar
Quyidagilarni tasniflang: email kiritish, parol tekshirish, admin yo'liga ruxsat.

**Yechim:** email kiritish — identifikatsiya; parol tekshirish — autentifikatsiya; admin yo'liga ruxsat — avtorizatsiya.

### 2-topshiriq (O'rta): Register
`/auth/register` endpointini yozing: email band bo'lsa 409, aks holda 201 va parol xeshlansin.

**Yechim:** 
```python
@router.post("/register", response_model=UserRead, status_code=201)
async def register(data: UserCreate, db: AsyncSession = Depends(get_db)):
    if await db.scalar(select(User).where(User.email == data.email)):
        raise HTTPException(409, "Email band")
    user = User(full_name=data.full_name, email=data.email,
                hashed_password=hash_password(data.password))
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
```

### 3-topshiriq (Qiyin): Login va me
`/auth/login` (JWT beradi) va `get_current_user` bilan himoyalangan `/auth/me` ni yozing.

**Yechim:** 
```python
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends(),
                db: AsyncSession = Depends(get_db)):
    user = await db.scalar(select(User).where(User.email == form.username))
    if not user or not verify_password(form.password, user.hashed_password):
        raise HTTPException(401, "Email yoki parol noto'g'ri",
                            headers={"WWW-Authenticate": "Bearer"})
    return {"access_token": create_access_token(str(user.id)),
            "token_type": "bearer"}
```

---

## Tezkor nazorat savollari

1. Identifikatsiya va autentifikatsiya farqi?
   - **Javob:** Identifikatsiya — kimligingizni aytish (email); autentifikatsiya — isbotlash (parol, token).
2. Autentifikatsiya va avtorizatsiya farqi?
   - **Javob:** Autentifikatsiya — kimligingizni tekshirish; avtorizatsiya — nimaga ruxsatingiz borligini tekshirish.
3. JWT qanday qismlardan iborat?
   - **Javob:** header, payload, signature.
4. Nega parol xeshlanadi?
   - **Javob:** Baza sizib chiqsa ham ochiq parol ko'rinmasligi uchun; xeshdan parolni tiklab bo'lmaydi.
5. 401 va 403 farqi?
   - **Javob:** 401 — token yo'q yoki yaroqsiz; 403 — token to'g'ri, lekin ruxsat yo'q.

---

## Uyga vazifa

`uyga-vazifa.md` ga qarang.
