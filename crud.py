from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .models import User, Project, Column, Task, TaskLog
from .schemas import UserCreate, ProjectCreate

# User CRUD
async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).where(User.email == email))
    return result.scalars().first()

async def create_user(db: AsyncSession, user: UserCreate):
    new_user = User(
        username=user.username,
        email=user.email,
        password_hash="hashed_password"  # Замените на реальный хэш
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

# Project CRUD
async def create_project(db: AsyncSession, project: ProjectCreate, user_id: int):
    new_project = Project(name=project.name, description=project.description, user_id=user_id)
    db.add(new_project)
    await db.commit()
    await db.refresh(new_project)
    return new_project

# Add similar CRUD functions for Column, Task, TaskLog...
