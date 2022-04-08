from fastapi_crudrouter import SQLAlchemyCRUDRouter
from pydantic import BaseModel, SecretStr
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, FastAPI, HTTPException, status
from typing import Optional
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, Request, FastAPI

from datetime import datetime

from sqlalchemy import Column, String, Integer, Text, DateTime
from sqlalchemy_utils.types.password import PasswordType
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select


app = FastAPI()
engine = create_engine(
    "postgresql+psycopg2cffi://postgres:sourcecode@database-2.clrt6clurscf.us-east-1.rds.amazonaws.com:5432/elearning_data"
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()


class Users(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True


class Courses(BaseModel):
    title: str
    image_url: str
    description: str


class CourseChapters(BaseModel):
    title: str
    course_id: int
    order: int
    content: str


class UserCourseActivity(BaseModel):
    u_id: int
    ch_id: int
    status: str
    activity_datetime: datetime


class schema_Users(Users):
    id: int

    class Config:
        orm_mode = True


class schema_Courses(Courses):
    id: int

    class Config:
        orm_mode = True


class schema_Chapters(CourseChapters):
    id: int

    class Config:
        orm_mode = True


class schema_Activity(UserCourseActivity):
    id: int

    class Config:
        orm_mode = True


Base = declarative_base()


class UsersModel(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)


class CoursesModel(Base):
    __tablename__ = 'Courses'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    image_url = Column(String)
    description = Column(Text)


class ChapterModel(Base):
    __tablename__ = 'Chapter'
    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer)
    title = Column(String)
    order = Column(Integer)
    content = Column(Text)


class ActivityModel(Base):
    __tablename__ = 'Activity'
    id = Column(Integer, primary_key=True, index=True)
    u_id = Column(Integer)
    ch_id = Column(Integer)
    status = Column(String)
    activity_datetime = Column(DateTime)


SECRET_KEY = "55b5f2d2b5f042f6b3c68ca9b5713d9557e91e9f603112ab720259ee9a98236e"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class UserInDB(Users):
    password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(email: str):
    session = SessionLocal()
    query = session.query(UsersModel).filter_by(email=email)
    result_set = query.all()
    if len(result_set) > 0:
        return result_set[0]

    session.close()


def authenticate_user(email: str, _password: str):
    user = get_user(email)
    if not user:
        return False
    if not verify_password(_password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = get_user(email=token_data.email)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: Users = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


async def get_current_user_admin(current_user: Users = Depends(get_current_user)):
    if current_user.admin:
        raise HTTPException(status_code=400, detail="Access Denied")
    return current_user


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/", response_model=Users)
async def read_users_me(current_user: Users = Depends(get_current_user)):
    return current_user


@app.post("/register", response_model=Users)
async def register(request: Request):
    data = await request.json()
    payload = {'name': '', 'email': data['email'],
               'password': get_password_hash(data['password'])}

    session = SessionLocal()
    _user = UsersModel(name=payload["name"],
                       password=payload["password"], email=payload["email"])
    session.add(_user)
    session.commit()
    session.close()
    return


@app.post("/update", response_model=Users)
async def register(request: Request):
    data = await request.json()
    session = SessionLocal()
    query = session.query(UsersModel).filter_by(email=data["email"])

    result_set = query.all()
    if len(result_set) > 0:
        if len(data["name"]) > 0:
            result_set[0].name = data["name"]
        if len(data["password"]) > 0:
            result_set[0].password = get_password_hash(data['password'])

    session.commit()
    session.close()
    return


@app.get("/users/me/items/")
async def read_own_items(current_user: Users = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.email}]

Base.metadata.create_all(bind=engine)

app.include_router(
    SQLAlchemyCRUDRouter(
        schema=schema_Users,
        create_schema=Users,
        db_model=UsersModel,
        db=get_db,
        prefix='User'
    )
)

app.include_router(
    SQLAlchemyCRUDRouter(
        schema=schema_Courses,
        create_schema=Courses,
        db_model=CoursesModel,
        db=get_db,
        prefix='Course'
    )
)

app.include_router(
    SQLAlchemyCRUDRouter(
        schema=schema_Chapters,
        create_schema=CourseChapters,
        db_model=ChapterModel,
        db=get_db,
        prefix='Chapter'
    )
)

app.include_router(
    SQLAlchemyCRUDRouter(
        schema=schema_Activity,
        create_schema=UserCourseActivity,
        db_model=ActivityModel,
        db=get_db,
        prefix='Activity'
    )
)
