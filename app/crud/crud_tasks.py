from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete

from app.models import Task
from app.schemas import (
    TaskCreate
)

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

