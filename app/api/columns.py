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

@router.get("/{project_id}/columns")
async def get_columns_view(project_id: int, db: AsyncSession = Depends(get_db)):
  return await get_columns_by_project(db, project_id)

@router.post("/")
async def create_column_view(column: BoardColumnCreate, project_id: int, db: AsyncSession = Depends(get_db)):
  return await create_board_column(db, column, project_id)

@router.put("/{column_id}")
async def update_column_view(column_id: int, column: BoardColumnCreate, db: AsyncSession = Depends(get_db)):
  return await update_column(db, column_id, column)

@router.delete("/{column_id}")
async def delete_column_view(column_id: int, db: AsyncSession = Depends(get_db)):
  return await delete_column(db, column_id)
