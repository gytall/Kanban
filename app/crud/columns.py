"""CRUD operations for board columns."""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models import BoardColumn
from app.schemas import BoardColumnCreate


async def create_board_column(
    db: AsyncSession,
    column: BoardColumnCreate,
    project_id: int
):
    """
    Create a new column in a project.
    
    Args:
        db: Database session
        column: Column creation data
        project_id: ID of the project to add the column to
        
    Returns:
        Created column instance
    """
    new_column = BoardColumn(
        name=column.name,
        project_id=project_id
    )
    db.add(new_column)
    await db.commit()
    await db.refresh(new_column)
    return new_column


async def get_columns_by_project(db: AsyncSession, project_id: int):
    """
    Get all columns in a specific project.
    
    Args:
        db: Database session
        project_id: ID of the project
        
    Returns:
        List of columns in the project
    """
    result = await db.execute(
        select(BoardColumn).where(BoardColumn.project_id == project_id)
    )
    return result.scalars().all()


async def get_column_by_id(db: AsyncSession, column_id: int):
    """
    Get a column by ID.
    
    Args:
        db: Database session
        column_id: ID of the column to retrieve
        
    Returns:
        Column instance if found, None otherwise
    """
    result = await db.execute(
        select(BoardColumn).where(BoardColumn.id == column_id)
    )
    return result.scalars().first()


async def update_column(
    db: AsyncSession,
    column_id: int,
    column: BoardColumnCreate
):
    """
    Update an existing column.
    
    Args:
        db: Database session
        column_id: ID of the column to update
        column: Updated column data
        
    Returns:
        Updated column instance if found, None otherwise
    """
    existing_column = await get_column_by_id(db, column_id)
    if existing_column:
        existing_column.name = column.name
        db.add(existing_column)
        await db.commit()
        await db.refresh(existing_column)
        return existing_column
    return None


async def delete_column(db: AsyncSession, column_id: int):
    """
    Delete a column by ID.
    
    Args:
        db: Database session
        column_id: ID of the column to delete
        
    Returns:
        Deleted column instance if found, None otherwise
    """
    column = await get_column_by_id(db, column_id)
    if column:
        await db.delete(column)
        await db.commit()
        return column
    return None
