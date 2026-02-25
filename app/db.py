"""Database configuration and session management."""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://postgres@localhost:5432/kanban_db"

engine = create_async_engine(DATABASE_URL, echo=True)

Base = declarative_base()

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_db():
    """
    Dependency function to get database session.
    
    Yields:
        AsyncSession: Database session instance
    """
    async with AsyncSessionLocal() as session:
        yield session