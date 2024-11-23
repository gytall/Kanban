from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .db import AsyncSessionLocal
from .crud import (
    create_task, create_task_log, create_board_column, get_tasks_by_column, 
    get_task_logs, create_user, create_project
)
from .schemas import TaskCreate, TaskLogCreate, BoardColumnCreate, UserCreate, ProjectCreate

router = APIRouter()

# Функция для получения сессии
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# Роуты для Task
@router.post("/tasks/")
async def create_task_view(task: TaskCreate, column_id: int, db: AsyncSession = Depends(get_db)):
    return await create_task(db, task, column_id)

# Роуты для TaskLog
@router.post("/task_logs/")
async def create_task_log_view(log: TaskLogCreate, task_id: int, db: AsyncSession = Depends(get_db)):
    return await create_task_log(db, log, task_id)

# Роуты для BoardColumn
@router.post("/columns/")
async def create_board_column_view(column: BoardColumnCreate, project_id: int, db: AsyncSession = Depends(get_db)):
    return await create_board_column(db, column, project_id)

# Получение задач по колонке
@router.get("/columns/{column_id}/tasks")
async def get_tasks_view(column_id: int, db: AsyncSession = Depends(get_db)):
    return await get_tasks_by_column(db, column_id)

# Получение логов для задачи
@router.get("/tasks/{task_id}/logs")
async def get_task_logs_view(task_id: int, db: AsyncSession = Depends(get_db)):
    return await get_task_logs(db, task_id)

# Роуты для User
@router.post("/users/")
async def create_user_view(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user)

# Роуты для Project
@router.post("/projects/")
async def create_project_view(project: ProjectCreate, user_id: int, db: AsyncSession = Depends(get_db)):
    return await create_project(db, project, user_id)
