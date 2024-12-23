from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete
from passlib.context import CryptContext

from app.models import User, Project, BoardColumn, Task, TaskLog
from app.schemas import (
    UserCreate, ProjectCreate, BoardColumnCreate, TaskCreate, TaskLogCreate
)


# Контекст для хеширования паролей
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# User CRUD
async def create_user(db: AsyncSession, user: UserCreate):
    hashed_password = pwd_context.hash(user.password) 
    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

    # Удаление пользователя
async def delete_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    if user:
        await db.delete(user)
        await db.commit()
        return user
    return None

async def get_all_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()

async def get_user_by_id(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalars().first()


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

async def get_projects(db: AsyncSession):
    result = await db.execute(select(Project))
    return result.scalars().all()

async def get_project_by_id(db: AsyncSession, project_id: int):
    result = await db.execute(select(Project).where(Project.id == project_id))
    return result.scalars().first()

async def update_project(db: AsyncSession, project_id: int, project: ProjectCreate):
    existing_project = await get_project_by_id(db, project_id)
    if existing_project:
        existing_project.name = project.name
        existing_project.description = project.description
        db.add(existing_project)
        await db.commit()
        await db.refresh(existing_project)
        return existing_project
    return None

async def delete_project(db: AsyncSession, project_id: int):
    project = await get_project_by_id(db, project_id)
    if project:
        await db.execute(delete(Project).where(Project.id == project_id))
        await db.commit()
    return None

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

async def get_columns_by_project(db: AsyncSession, project_id: int):
    result = await db.execute(select(BoardColumn).where(BoardColumn.project_id == project_id))
    return result.scalars().all()

async def get_column_by_id(db: AsyncSession, column_id: int):
    result = await db.execute(select(BoardColumn).where(BoardColumn.id == column_id))
    return result.scalars().first()

# async def get_user_by_id_put(db: AsyncSession, user_id: int):
#     result = await db.execute(select(User).where(User.id == user_id))
#     return result.scalars().first()

# async def update_user(db: AsyncSession, user_id: int, user: UserCreate):
#     existing_user = await get_user_by_id_put(db, user_id)
#     if existing_user:
#         existing_user.username = user.username
              
#         db.add(existing_user)
#         await db.commit()
#         await db.refresh(existing_user)
#         return existing_user
#     return None

async def update_column(db: AsyncSession, column_id: int, column: BoardColumnCreate):
    existing_column = await get_column_by_id(db, column_id)
    if existing_column:
        existing_column.name = column.name
        db.add(existing_column)
        await db.commit()
        await db.refresh(existing_column)
        return existing_column
    return None

async def delete_column(db: AsyncSession, column_id: int):
    column = await get_column_by_id(db, column_id)
    if column:
        await db.delete(column)
        await db.commit()
        return column
    return None

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

async def get_tasks_by_column(db: AsyncSession, column_id: int):
    result = await db.execute(select(Task).where(Task.column_id == column_id))
    return result.scalars().all()

async def get_task_by_id(db: AsyncSession, task_id: int):
    result = await db.execute(select(Task).where(Task.id == task_id))
    return result.scalars().first()

async def update_task(db: AsyncSession, task_id: int, task: TaskCreate):
    existing_task = await get_task_by_id(db, task_id)
    if existing_task:
        existing_task.title = task.title 
        existing_task.description = task.description
        db.add(existing_task)
        await db.commit()
        await db.refresh(existing_task)
        return existing_task
    return None

async def delete_task(db: AsyncSession, task_id: int):
    task = await get_task_by_id(db, task_id)
    if task:
        await db.delete(task)
        await db.commit()
        return task
    return None

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

async def get_task_logs(db: AsyncSession, task_id: int):
    result = await db.execute(select(TaskLog).where(TaskLog.task_id == task_id))
    return result.scalars().all()