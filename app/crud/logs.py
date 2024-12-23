from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete
from passlib.context import CryptContext

from app.models import TaskLog
from app.schemas import TaskLogCreate

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