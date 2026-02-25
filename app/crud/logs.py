"""CRUD operations for task logs."""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models import TaskLog
from app.schemas import TaskLogCreate


async def create_task_log(
    db: AsyncSession,
    log: TaskLogCreate,
    task_id: int
):
    """
    Create a new task log entry.
    
    Args:
        db: Database session
        log: Task log creation data
        task_id: ID of the task to log
        
    Returns:
        Created task log instance
    """
    new_log = TaskLog(
        task_id=task_id,
        action=log.action
    )
    db.add(new_log)
    await db.commit()
    await db.refresh(new_log)
    return new_log


async def get_task_logs(db: AsyncSession, task_id: int):
    """
    Get all logs for a specific task.
    
    Args:
        db: Database session
        task_id: ID of the task
        
    Returns:
        List of task logs
    """
    result = await db.execute(
        select(TaskLog).where(TaskLog.task_id == task_id)
    )
    return result.scalars().all()