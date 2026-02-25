"""API endpoints for task log management."""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
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
async def create_task_log_view(
    log: TaskLogCreate,
    task_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Create a new task log entry.
    
    Args:
        log: Task log creation data
        task_id: ID of the task to log
        db: Database session
        
    Returns:
        Created task log instance
    """
    return await create_task_log(db, log, task_id)


@router.get("/{task_id}/logs")
async def get_task_logs_view(
    task_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Get all logs for a specific task.
    
    Args:
        task_id: ID of the task
        db: Database session
        
    Returns:
        List of task logs
    """
    return await get_task_logs(db, task_id)