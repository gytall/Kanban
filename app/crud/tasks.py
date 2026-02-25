"""CRUD operations for tasks."""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models import Task
from app.schemas import TaskCreate


async def create_task(
    db: AsyncSession,
    task: TaskCreate,
    column_id: int
):
    """
    Create a new task in a column.
    
    Args:
        db: Database session
        task: Task creation data
        column_id: ID of the column to add the task to
        
    Returns:
        Created task instance
    """
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
    """
    Get all tasks in a specific column.
    
    Args:
        db: Database session
        column_id: ID of the column
        
    Returns:
        List of tasks in the column
    """
    result = await db.execute(select(Task).where(Task.column_id == column_id))
    return result.scalars().all()


async def get_task_by_id(db: AsyncSession, task_id: int):
    """
    Get a task by ID.
    
    Args:
        db: Database session
        task_id: ID of the task to retrieve
        
    Returns:
        Task instance if found, None otherwise
    """
    result = await db.execute(select(Task).where(Task.id == task_id))
    return result.scalars().first()


async def update_task(
    db: AsyncSession,
    task_id: int,
    task: TaskCreate
):
    """
    Update an existing task.
    
    Args:
        db: Database session
        task_id: ID of the task to update
        task: Updated task data
        
    Returns:
        Updated task instance if found, None otherwise
    """
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
    """
    Delete a task by ID.
    
    Args:
        db: Database session
        task_id: ID of the task to delete
        
    Returns:
        Deleted task instance if found, None otherwise
    """
    task = await get_task_by_id(db, task_id)
    if task:
        await db.delete(task)
        await db.commit()
        return task
    return None