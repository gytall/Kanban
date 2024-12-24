from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL подключения к базе данных
DATABASE_URL = "postgresql+asyncpg://postgres@localhost:5432/kanban_db"

# Асинхронный движок для SQLAlchemy
engine = create_async_engine(DATABASE_URL, echo=True)

# Базовый класс для моделей
Base = declarative_base()

# Асинхронная сессия
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Функция для получения сессии базы данных
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

