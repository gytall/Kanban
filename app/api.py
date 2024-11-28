from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from .db import AsyncSessionLocal
from .crud import (
    create_user, create_project, get_projects, get_project_by_id,
    update_project, delete_project, create_board_column, get_columns_by_project,
    update_column, delete_column, create_task, get_tasks_by_column,
    update_task, delete_task, create_task_log, get_task_logs
)
from .schemas import (
    UserCreate, ProjectCreate, ProjectOut, BoardColumnCreate,
    TaskCreate, TaskLogCreate, UserOut
)

router = APIRouter()

# Функция для получения сессии
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# ----------------- POST запросы -----------------

# User
@router.post("/users/")
async def create_user_view(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user)

# Project
@router.post("/projects/")
async def create_project_view(project: ProjectCreate, user_id: int, db: AsyncSession = Depends(get_db)):
    return await create_project(db, project, user_id)

# Column
@router.post("/columns/")
async def create_column_view(column: BoardColumnCreate, project_id: int, db: AsyncSession = Depends(get_db)):
    return await create_board_column(db, column, project_id)

# Task
@router.post("/tasks/")
async def create_task_view(task: TaskCreate, column_id: int, db: AsyncSession = Depends(get_db)):
    return await create_task(db, task, column_id)

# TaskLog
@router.post("/task_logs/")
async def create_task_log_view(log: TaskLogCreate, task_id: int, db: AsyncSession = Depends(get_db)):
    return await create_task_log(db, log, task_id)

# ----------------- GET запросы -----------------

# Users
@router.get("/users/")
async def get_all_users_view(db: AsyncSession = Depends(get_db)):
    users = await get_all_users(db)
    return users

# В роутере для получения конкретного пользователя

@router.get("/users/{user_id}", response_model=UserOut)
async def get_user_view(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found."
        )
    return user


# Projects
@router.get("/projects/")
async def get_all_projects(db: AsyncSession = Depends(get_db)):
    return await get_projects(db)

@router.get("/projects/{project_id}")
async def get_project_view(project_id: int, db: AsyncSession = Depends(get_db)):
    return await get_project_by_id(db, project_id)

# Columns
@router.get("/projects/{project_id}/columns")
async def get_columns_view(project_id: int, db: AsyncSession = Depends(get_db)):
    return await get_columns_by_project(db, project_id)

# Tasks
@router.get("/columns/{column_id}/tasks")
async def get_tasks_view(column_id: int, db: AsyncSession = Depends(get_db)):
    return await get_tasks_by_column(db, column_id)

# TaskLogs
@router.get("/tasks/{task_id}/logs")
async def get_task_logs_view(task_id: int, db: AsyncSession = Depends(get_db)):
    return await get_task_logs(db, task_id)

# ----------------- PUT запросы -----------------

# Project
@router.put("/projects/{project_id}")
async def update_project_view(project_id: int, project: ProjectCreate, db: AsyncSession = Depends(get_db)):
    return await update_project(db, project_id, project)

# Column
@router.put("/columns/{column_id}")
async def update_column_view(column_id: int, column: BoardColumnCreate, db: AsyncSession = Depends(get_db)):
    return await update_column(db, column_id, column)

# Task
@router.put("/tasks/{task_id}")
async def update_task_view(task_id: int, task: TaskCreate, db: AsyncSession = Depends(get_db)):
    return await update_task(db, task_id, task)

# ----------------- DELETE запросы -----------------

# Project
@router.delete("/projects/{project_id}")
async def delete_project_view(project_id: int, db: AsyncSession = Depends(get_db)):
    return await delete_project(db, project_id)

# Column
@router.delete("/columns/{column_id}")
async def delete_column_view(column_id: int, db: AsyncSession = Depends(get_db)):
    return await delete_column(db, column_id)

# Task
@router.delete("/tasks/{task_id}")
async def delete_task_view(task_id: int, db: AsyncSession = Depends(get_db)):
    return await delete_task(db, task_id)

# User
@router.delete("/users/{user_id}")
async def delete_user_view(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await delete_user(db, user_id)
    return result

    