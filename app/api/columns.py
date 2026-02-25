"""API endpoints for board column management."""

from fastapi import APIRouter, Depends
from app.db import AsyncSession, get_db
from app.schemas import BoardColumnCreate
from app.crud import (
    create_board_column,
    update_column,
    delete_column,
    get_columns_by_project,
)

router = APIRouter(
    prefix="/columns",
    tags=['columns']
)


@router.post("/")
async def create_column_view(
    column: BoardColumnCreate,
    project_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Create a new column in a project.
    
    Args:
        column: Column creation data
        project_id: ID of the project to add the column to
        db: Database session
        
    Returns:
        Created column instance
    """
    return await create_board_column(db, column, project_id)


@router.get("/{project_id}/columns")
async def get_columns_view(
    project_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Get all columns in a specific project.
    
    Args:
        project_id: ID of the project
        db: Database session
        
    Returns:
        List of columns in the project
    """
    return await get_columns_by_project(db, project_id)


@router.put("/{column_id}")
async def update_column_view(
    column_id: int,
    column: BoardColumnCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Update an existing column.
    
    Args:
        column_id: ID of the column to update
        column: Updated column data
        db: Database session
        
    Returns:
        Updated column instance if found, None otherwise
    """
    return await update_column(db, column_id, column)


@router.delete("/{column_id}")
async def delete_column_view(
    column_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Delete a column by ID.
    
    Args:
        column_id: ID of the column to delete
        db: Database session
        
    Returns:
        Deleted column instance if found, None otherwise
    """
    return await delete_column(db, column_id)
