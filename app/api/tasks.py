from fastapi import APIRouter, Depends
from app.db import AsyncSession, get_db
from app.schemas import TaskCreate
from app.crud import (
    create_task,
		get_tasks_by_column,
		update_task,
		delete_task,
    get_task_by_id,
)
router = APIRouter(
	prefix="/tasks",
    tags=['tasks']
)

@router.put("/{task_id}")
async def update_task_view(task_id: int, task: TaskCreate, db: AsyncSession = Depends(get_db)):
  return await update_task(db, task_id, task)

@router.post("/")
async def create_task_view(task: TaskCreate, column_id: int, db: AsyncSession = Depends(get_db)):
  return await create_task(db, task, column_id)

@router.get("/{task_id}")
async def get_tasks_view(column_id: int, db: AsyncSession = Depends(get_db)):
  return await get_task_by_id(db, column_id)

@router.get("/{column_id}/tasks")
async def get_tasks_view(column_id: int, db: AsyncSession = Depends(get_db)):
  return await get_tasks_by_column(db, column_id)

@router.delete("/{task_id}")
async def delete_task_view(task_id: int, db: AsyncSession = Depends(get_db)):
  return await delete_task(db, task_id)
