from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import AsyncSessionLocal, get_db
from app.crud import (
    create_task_log, 
    get_task_logs,
)
from app.schemas import (
    TaskLogCreate
)

router = APIRouter(
    prefix="/task_logs",
    tags=['logs']
)

@router.post("/")
async def create_task_log_view(log: TaskLogCreate, task_id: int, db: AsyncSession = Depends(get_db)):
    return await create_task_log(db, log, task_id)

@router.get("/{task_id}/logs")
async def get_task_logs_view(task_id: int, db: AsyncSession = Depends(get_db)):
    return await get_task_logs(db, task_id)


    