"""API endpoints for task management."""

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


@router.post("/")
async def create_task_view(
    task: TaskCreate,
    column_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Create a new task in a column.
    
    Args:
        task: Task creation data
        column_id: ID of the column to add the task to
        db: Database session
        
    Returns:
        Created task instance
    """
    return await create_task(db, task, column_id)


@router.get("/{task_id}")
async def get_task_view(
    task_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Get a task by ID.
    
    Args:
        task_id: ID of the task to retrieve
        db: Database session
        
    Returns:
        Task instance if found, None otherwise
    """
    return await get_task_by_id(db, task_id)


@router.get("/{column_id}/tasks")
async def get_tasks_by_column_view(
    column_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Get all tasks in a specific column.
    
    Args:
        column_id: ID of the column
        db: Database session
        
    Returns:
        List of tasks in the column
    """
    return await get_tasks_by_column(db, column_id)


@router.put("/{task_id}")
async def update_task_view(
    task_id: int,
    task: TaskCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Update an existing task.
    
    Args:
        task_id: ID of the task to update
        task: Updated task data
        db: Database session
        
    Returns:
        Updated task instance if found, None otherwise
    """
    return await update_task(db, task_id, task)


@router.delete("/{task_id}")
async def delete_task_view(
    task_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Delete a task by ID.
    
    Args:
        task_id: ID of the task to delete
        db: Database session
        
    Returns:
        Deleted task instance if found, None otherwise
    """
    return await delete_task(db, task_id)
