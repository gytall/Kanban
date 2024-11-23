from databases import Database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

# Укажите правильный путь для подключения к базе данных
DATABASE_URL = "postgresql+asyncpg://postgres@localhost:5432/kanban_db"

# Создание асинхронного движка для SQLAlchemy
engine = create_async_engine(DATABASE_URL, echo=True)

# Создание базы данных (асинхронное подключение)
database = Database(DATABASE_URL)

# Базовый класс для моделей
Base = declarative_base()

# Создание асинхронной сессии
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)
