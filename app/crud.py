from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .models import User, Project, BoardColumn, Task, TaskLog
from .schemas import UserCreate, ProjectCreate, BoardColumnCreate, TaskCreate, TaskLogCreate
from passlib.context import CryptContext

# Контекст для хеширования паролей
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# User CRUD
async def create_user(db: AsyncSession, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)  # Хэшируем пароль
    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

# Project CRUD
async def create_project(db: AsyncSession, project: ProjectCreate, user_id: int):
    new_project = Project(
        name=project.name,
        description=project.description,
        user_id=user_id
    )
    db.add(new_project)
    await db.commit()
    await db.refresh(new_project)
    return new_project

# Task CRUD
async def create_task(db: AsyncSession, task: TaskCreate, column_id: int):
    new_task = Task(
        title=task.title,
        description=task.description,
        column_id=column_id
    )
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task

# TaskLog CRUD
async def create_task_log(db: AsyncSession, log: TaskLogCreate, task_id: int):
    new_log = TaskLog(
        task_id=task_id,
        action=log.action
    )
    db.add(new_log)
    await db.commit()
    await db.refresh(new_log)
    return new_log

# BoardColumn CRUD
async def create_board_column(db: AsyncSession, column: BoardColumnCreate, project_id: int):
    new_column = BoardColumn(
        name=column.name,
        project_id=project_id
    )
    db.add(new_column)
    await db.commit()
    await db.refresh(new_column)
    return new_column

# Получить колонку по ID
async def get_column_by_id(db: AsyncSession, column_id: int):
    result = await db.execute(select(BoardColumn).where(BoardColumn.id == column_id))
    return result.scalars().first()

# Получить все задачи в колонке
async def get_tasks_by_column(db: AsyncSession, column_id: int):
    result = await db.execute(select(Task).where(Task.column_id == column_id))
    return result.scalars().all()

# Получить логи задачи
async def get_task_logs(db: AsyncSession, task_id: int):
    result = await db.execute(select(TaskLog).where(TaskLog.task_id == task_id))
    return result.scalars().all()
